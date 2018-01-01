# -*- coding: utf-8 -*-

import requests
import pytest


@pytest.RequestsData("req")
def test_requests(data_json):
    res = requests.get('https://example.com/test0')
    assert res.status_code == 200
    assert data_json.expected == res.json()
