# -*- coding: utf-8 -*-

import requests
import pytest


def assert_test0(data):
    res = requests.get('https://example.com/test0')
    assert res.status_code == 200
    assert data.expected == res.json()


@pytest.RequestsData("req")
def test_decorator(data_json):
    assert_test0(data_json)


def test_context(data_json):
    with pytest.RequestsData("req"):
        assert_test0(data_json)


@pytest.RequestsData("json")
def test_input_extension(data_json):
    assert_test0(data_json)


@pytest.RequestsData("req")
def test_multiple_files():
    with pytest.raises(NotImplementedError):
        requests.get('https://example.com/multiple_files')


@pytest.RequestsData("req")
def test_missing_data():
    with pytest.raises(ValueError):
        requests.get('https://example.com/nonexistant')


@pytest.RequestsData("req")
def test_status_code():
    res = requests.get('https://example.com/test404')
    res.status_code == 404
