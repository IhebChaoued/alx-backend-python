#!/usr/bin/env python3
"""Unit tests for GithubOrgClient"""

import unittest
from unittest.mock import patch, PropertyMock
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
        """GithubOrgClient.org: return the correct value"""
        test_payload = {"login": input}
        mock_get_json.return_value = test_payload

        test_class = GithubOrgClient(input)
        result = test_class.org

        mock_get_json.assert_called_once_with(
                f'https://api.github.com/orgs/{input}'
                )
        self.assertEqual(result, test_payload)

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test GithubOrgClient._public_repos_url"""
        test_payload = {
                "repos_url": "https://api.github.com/orgs/test/repos"
                }
        mock_org.return_value = test_payload

        test_class = GithubOrgClient("test")
        result = test_class._public_repos_url

        self.assertEqual(result, test_payload["repos_url"])


if __name__ == "__main__":
    unittest.main()
