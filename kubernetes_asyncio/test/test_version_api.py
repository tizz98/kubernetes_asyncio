# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.16.14
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes_asyncio.client
from kubernetes_asyncio.client.api.version_api import VersionApi  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException


class TestVersionApi(unittest.TestCase):
    """VersionApi unit test stubs"""

    def setUp(self):
        self.api = kubernetes_asyncio.client.api.version_api.VersionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_code(self):
        """Test case for get_code

        """
        pass


if __name__ == '__main__':
    unittest.main()
