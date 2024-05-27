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
        """GithubOrgClient.org: returns the correct value"""
        test_payload = {"login": input}
        mock_get_json.return_value = test_payload

        test_class = GithubOrgClient(input)
        result = test_class.org

        mock_get_json.assert_called_once_with(
                f'https://api.github.com/orgs/{input}'
                )
        self.assertEqual(result, test_payload)

    @patch('client.GithubOrgClient._public_repos_url')
    @patch('client.get_json')
    def test_public_repos(self, mock_get_json, mock_public_repos_url):
        """Test GithubOrgClient.public_repos"""
        test_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = test_payload

        mock_public_repos_url.return_value = "https://api.github.com/orgs/test/repos"

        test_class = GithubOrgClient("test")
        
        result = test_class.public_repos()

        mock_get_json.assert_called_once()
        mock_public_repos_url.assert_called_once()

        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
