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
