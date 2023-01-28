#!/usr/bin/env python3
"""test utils module"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from nose.tools import assert_equal


class TestAccessNestedMap(unittest.TestCase):
    """test for utility module"""
    """TODO: understand decorators first"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, sequence, expected):
        """test for access nested map function"""
        assert_equal(access_nested_map(nested_map, sequence), expected)
