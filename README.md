
# pytest filedata

[![PyPI](https://img.shields.io/pypi/v/pytest-filedata.svg?maxAge=3600)](https://pypi.python.org/pypi/pytest-filedata)
[![PyPI](https://img.shields.io/pypi/pyversions/pytest-filedata.svg?maxAge=3600)](https://pypi.python.org/pypi/pytest-filedata)
[![Travis CI](https://img.shields.io/travis/20c/pytest-filedata.svg?maxAge=3600)](https://travis-ci.org/20c/pytest-filedata)
[![Code Health](https://landscape.io/github/20c/pytest-filedata/master/landscape.svg?style=flat)](https://landscape.io/github/20c/pytest-filedata/master)
[![Codecov](https://img.shields.io/codecov/c/github/20c/pytest-filedata/master.svg?maxAge=3600)](https://codecov.io/github/20c/pytest-filedata)

Easily load test data from files

### Introduction

This was created to save the tediousness of working with sets of data for
testing inside the test files.

### Installing

```sh
pip install pytest-filedata
```

### Using

Add this to your `conftest.py` file:

```python
import pytest_filedata

pytest_filedata.setup(os.path.dirname(__file__))


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith('data_'):
            data = pytest_filedata.get_data(fixture)
            metafunc.parametrize(fixture, list(data.values()), ids=list(data.keys()))
```


### License

Copyright 2016-2024 20C, LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this software except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
