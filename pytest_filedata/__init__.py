
from future import standard_library
standard_library.install_aliases()
from builtins import map
from builtins import object
import collections
from datetime import datetime
import json
import os
import urllib.parse

import requests_mock
import decorator


test_dir = None


def setup_filedata(base_dir, fixture_prefixes=None):
    """
    setup filedata with base dir for data
    """
    global test_dir
    test_dir = base_dir


def json_hook(data):
    date_keys = (
        'last_change',
        'last_reboot',
        'last_reconfiguration',
        )
    for key in date_keys:
        if key in data:
            data[key] = datetime.strptime(data[key], "%Y-%m-%dT%H:%M:%S")
    return data



class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)


def dumps(data):
    return json.dumps(data, cls=JSONEncoder)


def load(fobj):
    return json.load(fobj, object_hook=json_hook)


def loads(data):
    return json.loads(data, object_hook=json_hook)


class FileTestData(object):
    """ object to hold file test data """
    def __init__(self, inp=None, exp=None, name=None, path=None):
        self.input = inp
        self.expected = exp
        self.name = name
        self.path = path

    def dumps(self, data):
        """ dump data in configured output method """
        return dumps(data)

    def loads(self, data):
        """ load data in configured output method """
        return loads(data)


def get_test_files(dirname):
    """
    gets a list of files in directory specified by name
    """
    if not os.path.isdir(dirname):
        return []
    path = dirname + "/{}"
    return list(map(path.format, sorted(os.listdir(dirname))))


def get_filedata(name):
    data = collections.OrderedDict()
    dirname = os.path.join(test_dir, *name.split('_'))

    if not os.path.isdir(dirname):
        raise ValueError("data directory '{}' does not exist".format(dirname))

    for each in get_test_files(dirname):
        if os.path.isdir(each):
            continue

        fname = os.path.basename(each)
        if fname.startswith('.'):
            continue

        test_name, ext = os.path.splitext(fname)
        data.setdefault(test_name, FileTestData(name=test_name, path=dirname))

        # could setattr
        attr = ext[1:]
        if ext == '.expected':
            with open(each) as fobj:
                data[test_name].expected = json.load(fobj, object_hook=json_hook)
        else:
            with open(each) as fobj:
                setattr(data[test_name], attr, fobj.read())

    return data


class RequestsData(object):
    """
    class to use test data from requests
    """
    def __init__(self, prefix, real_http=False):
        self.prefix = prefix
        adapter = requests_mock.Adapter()
        adapter.register_uri(requests_mock.ANY, requests_mock.ANY, text=self.callback)
        self.mocker = requests_mock.Mocker(adapter=adapter, real_http=real_http)

    def callback(self, request, context):
        path = urllib.parse.urlparse(request.url).path
        path = os.path.join(test_dir, 'data', self.prefix, path.lstrip('/'))

        files = get_test_files(path)

        if len(files) > 1:
            raise NotImplementedError("Currently there must be only one response file")

        if len(files) == 0:
            # dir not found, check for file.input
            fname = path + '.input'
            if not os.path.exists(fname):
                raise ValueError("failed to find data for {}".format(path))

        else:
            fname = files[0]

        try:
            # file extension is status code
            context.status_code = int(os.path.splitext(fname)[1].lstrip('.'))

        except ValueError:
            context.status_code = 200

        with open(fname) as fobj:
            return fobj.read()

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            with self.mocker:
                # FIXME -- why is the test func arg 0?
                func(*args[1:], **kwargs)

        # use decorator because functools.wrap changes the function sig
        return decorator.decorator(wrapper, func)

    def __enter__(self):
        self.mocker.start()

    def __exit__(self, typ, value, traceback):
        self.mocker.stop()


def pytest_namespace():
    """Register pytest plugin."""
    return dict(
        get_filedata=get_filedata,
        RequestsData=RequestsData,
        setup_filedata=setup_filedata,
        )
