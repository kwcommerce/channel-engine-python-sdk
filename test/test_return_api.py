# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.return_api import ReturnApi


class TestReturnApi(unittest.TestCase):
    """ReturnApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ReturnApi()

    def tearDown(self) -> None:
        pass

    def test_return_acknowledge(self) -> None:
        """Test case for return_acknowledge

        Acknowledges a return
        """
        pass

    def test_return_declare_for_merchant(self) -> None:
        """Test case for return_declare_for_merchant

        Creates merchant return
        """
        pass

    def test_return_get_by_merchant_order_no(self) -> None:
        """Test case for return_get_by_merchant_order_no

        Gets a return
        """
        pass

    def test_return_get_declared_by_channel(self) -> None:
        """Test case for return_get_declared_by_channel

        Gets marketplace returns
        """
        pass

    def test_return_get_returns(self) -> None:
        """Test case for return_get_returns

        Gets returns by filter
        """
        pass

    def test_return_get_unhandled(self) -> None:
        """Test case for return_get_unhandled

        Gets unhandled returns
        """
        pass

    def test_return_update_for_merchant(self) -> None:
        """Test case for return_update_for_merchant

        Marks returns as received
        """
        pass


if __name__ == '__main__':
    unittest.main()
