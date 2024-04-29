import requests
import pytest
import pytest_filedata


def assert_test0(data):
    res = requests.get("https://example.com/test0")
    assert res.status_code == 200
    assert data.expected == res.json()


@pytest_filedata.RequestsData("req")
def test_decorator(data_json):
    assert_test0(data_json)


def test_context(data_json):
    with pytest_filedata.RequestsData("req"):
        assert_test0(data_json)


@pytest_filedata.RequestsData("json")
def test_input_extension(data_json):
    assert_test0(data_json)


@pytest_filedata.RequestsData("req")
def test_multiple_files():
    with pytest.raises(NotImplementedError):
        requests.get("https://example.com/multiple_files")


@pytest_filedata.RequestsData("req")
def test_missing_data():
    with pytest.raises(ValueError):
        requests.get("https://example.com/nonexistant")


@pytest_filedata.RequestsData("req")
def test_status_code():
    res = requests.get("https://example.com/test404")
    res.status_code == 404
