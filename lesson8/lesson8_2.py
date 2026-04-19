from unittest.mock import patch
from lesson8_1 import add
import requests
import pytest


def test_add_positive_numbers():
    assert add(1, 2) == 3


def test_add_negative_numbers():
    assert add(-1, -2) == -3


def get_data_from_api(url):
    response = requests.get(url)
    return response.json()


@patch('requests.get')
def test_get_data_from_api(mock_get):
    mock_get.return_value.json.return_value = {"key": "value"}
    result = get_data_from_api("http://example.com/api")
    assert result == {"key": "value"}

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
