# -*- coding: utf-8 -*-


import pytest


def assert_json(data, parsed):
    # dump in json format for easily adding expected
    print("echo \\\n'{}'\\\n > {}/{}.expected".format(data.dumps(parsed), data.path, data.name))
    assert data.expected == parsed
    assert data.name
    assert data.path


def test_json_data(data_json):
    parsed = data_json.loads(data_json.input)
    assert_json(data_json, parsed)


#with pytest.raises(ValueError):
#    def test_nonexistant(data_nonexistant):
#        pass
