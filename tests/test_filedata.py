# -*- coding: utf-8 -*-

import pytest
import json


def test_json_data(data_json):
	parsed = json.loads(data_json.input)
	assert data_json.expected == parsed


#with pytest.raises(ValueError):
#    def test_nonexistant(data_nonexistant):
#        pass
