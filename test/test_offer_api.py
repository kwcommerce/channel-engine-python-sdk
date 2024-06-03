# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.offer_api import OfferApi


class TestOfferApi(unittest.TestCase):
    """OfferApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OfferApi()

    def tearDown(self) -> None:
        pass

    def test_offer_get_stock(self) -> None:
        """Test case for offer_get_stock

        Gets product stock across all warehouses
        """
        pass

    def test_offer_stock_price_update(self) -> None:
        """Test case for offer_stock_price_update

        Updates stock and price
        """
        pass

    def test_offer_stock_update(self) -> None:
        """Test case for offer_stock_update

        Updates stock
        """
        pass


if __name__ == '__main__':
    unittest.main()
