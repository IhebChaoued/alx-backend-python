#!/usr/bin/env python3
"""Unit test"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test cases: access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self, nested_map: dict, path: tuple, expected: any
            ) -> None:
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
