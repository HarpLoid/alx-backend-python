#!/usr/bin/env python3
"""
Unit Tests and Integration Tests
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Test for access_nested_map
    """
    @paramiterized.expand([
        ({"a": 1}, ("a",), 1)
        ({"a": {"b": 2}}, ("a",), {"b": 2})
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test access_nested_map return value for the given path
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
    
    @paramiterized.expand([
        ({}, ("a",), KeyError)
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Test access_nested_map raises KeyError on wrong path
        """
        self.assertRaises(access_nested_map(nested_map, path), expected)

class TestGetJson(unittest.TestCase):
    """ Tests GetJson
    """
    @paramiterized.expand([
        ("http://example.com", {"payload": True})
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Tests that get_json returns the expected result without
        making external HTTP calls, using patch as a context manager.
        """
        with patch('utils.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            
            result = get_json(test_url)
            
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    """ Test Memoize
    """
    def test_memoize(self):
        """ Test that when calling a property twice, the correct result is
        returned but the method is only called once using patch as a
        decorator.
        """
        class TestClass:
            def a_method(self):
                return 42
            
            @memoize
            def a_property(self):
                return self.a_method()
        
        with patch.object(TestClass, 'a_method', return_value=42) as mock_a_method:
            test_instance = TestClass()
            
            result1 = test_instance.a_property
            result2 = test_instance.a_property
            
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_a_method.assert_called_once()
