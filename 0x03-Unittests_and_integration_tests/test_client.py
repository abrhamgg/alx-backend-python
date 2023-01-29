#!/usr/bin/env pytohn3
"""test _github_org_client"""
from typing import Dict
import unittest
from unittest.mock import MagicMock, patch, Mock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test class for github org client"""
    @parameterized.expand([
            ("google", {'login': "google"}),
            ("abc", {'login': "abc"}),
        ])
    @patch('client.get_json')
    def test_org(self, org: str, resp: Dict, mocked_fn: MagicMock) -> None:
        """tests test_org method"""
        mocked_fn.return_value = MagicMock(return_value=resp)
        github_org_client = GithubOrgClient(org)
        self.assertEqual(github_org_client.org(), resp)
        mocked_fn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )
