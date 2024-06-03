# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_shipment_line_request import MerchantShipmentLineRequest

class TestMerchantShipmentLineRequest(unittest.TestCase):
    """MerchantShipmentLineRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantShipmentLineRequest:
        """Test MerchantShipmentLineRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantShipmentLineRequest`
        """
        model = MerchantShipmentLineRequest()
        if include_optional:
            return MerchantShipmentLineRequest(
                merchant_product_no = '',
                extra_data = {
                    'key' : ''
                    },
                quantity = 0
            )
        else:
            return MerchantShipmentLineRequest(
                merchant_product_no = '',
                quantity = 0,
        )
        """

    def testMerchantShipmentLineRequest(self):
        """Test MerchantShipmentLineRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
