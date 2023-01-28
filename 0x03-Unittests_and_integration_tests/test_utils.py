#!/usr/bin/env python3
"""test utils module"""
import unittest
from typing import Mapping, Sequence, Dict, Union, Tuple
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """test for utility module"""
    """TODO: understand decorators first"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               sequence: Tuple[str],
                               expected: Union[Dict, int]) -> None:
        """test for access nested map function"""
        self.assertEqual(access_nested_map(nested_map, sequence), expected)

    @parameterized.expand([
        ({}, ("a", ), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Tuple[str],
                                         exception: Exception):
        """tests the access nested map function"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)
