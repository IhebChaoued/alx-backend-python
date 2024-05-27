#!/usr/bin/env python3
"""Unit tests for GithubOrgClient"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, input, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        test_payload = {"login": input}
        mock_get_json.return_value = test_payload

        test_class = GithubOrgClient(input)
        result = test_class.org  # Access the property without parentheses

        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{input}')
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
