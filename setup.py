
from setuptools import find_packages, setup


def read_file(name):
    with open(name) as fobj:
        return fobj.read().strip()


LONG_DESCRIPTION = read_file("README.md")
VERSION = read_file("Ctl/VERSION")
REQUIREMENTS = read_file("Ctl/requirements.txt").split('\n')
TEST_REQUIREMENTS = read_file("Ctl/requirements-test.txt").split('\n')


setup(
    name='pytest_filedata',
    version=VERSION,
    author='20C',
    author_email='code@20c.com',
    description='easily load data from files',
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license='LICENSE.txt',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Testing',
    ],
    packages = find_packages(),
    include_package_data=True,
    url='https://github.com/20c/pytest-filedata',
    download_url='https://github.com/20c/pytest-filedata/archive/{}.zip'.format(VERSION),

    install_requires=REQUIREMENTS,
    test_requires=TEST_REQUIREMENTS,

    zip_safe=True,
    entry_points={
        'pytest11': [
            'filedata = pytest_filedata',
        ],
    },
)
