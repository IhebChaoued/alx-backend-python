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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """GithubOrgClient.public_repos: returns the correct value"""
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]
        mock_get_json.return_value = test_payload

        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/orgs/test/repos"

            test_class = GithubOrgClient("test")
            result = test_class.public_repos

            mock_get_json.assert_called_once_with("https://api.github.com/orgs/test/repos")
            mock_public_repos_url.assert_called_once()

            self.assertEqual(result, ["repo1", "repo2"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({"license": None}, "my_license", False),
        ({}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """GithubOrgClient.has_license: returns the correct value"""
        test_class = GithubOrgClient("test")
        result = test_class.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
