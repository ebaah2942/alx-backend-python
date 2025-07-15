#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map  
from unittest.mock import patch, Mock
from utils import get_json

# class TestAccessNestedMap(unittest.TestCase):
#     @parameterized.expand([
#         ({"a": 1}, ("a",), 1),
#         ({"a": {"b": 2}}, ("a",), {"b": 2}),
#         ({"a": {"b": 2}}, ("a", "b"), 2),
#     ])
#     def test_access_nested_map(self, nested_map, path, expected):
#         self.assertEqual(access_nested_map(nested_map, path), expected)
 


#     @parameterized.expand([
#         ({}, ("a",), 'a'),
#         ({"a": 1}, ("a", "b"), 'b'),
#     ])
#     def test_access_nested_map_exception(self, nested_map, path, expected_key):
#         with self.assertRaises(KeyError) as context:
#             access_nested_map(nested_map, path)
#         self.assertEqual(str(context.exception), f"'{expected_key}'")


    

class TestGetJson(unittest.TestCase):

    @parameterized.expand([
        ("example_com", "http://example.com", {"payload": True}),
        ("holberton_io", "http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, name, test_url, test_payload):
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch("utils.requests.get", return_value=mock_response) as mock_get:
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)

        
                


 
