# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_acknowledge_purchase_order_line import MerchantAcknowledgePurchaseOrderLine

class TestMerchantAcknowledgePurchaseOrderLine(unittest.TestCase):
    """MerchantAcknowledgePurchaseOrderLine unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantAcknowledgePurchaseOrderLine:
        """Test MerchantAcknowledgePurchaseOrderLine
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantAcknowledgePurchaseOrderLine`
        """
        model = MerchantAcknowledgePurchaseOrderLine()
        if include_optional:
            return MerchantAcknowledgePurchaseOrderLine(
                order_line_identifier = '',
                acknowledgement_code = 'REJECTED',
                acknowledged_quantity = 56,
                rejection_reason = 'INVALID_PRODUCT',
                scheduled_ship_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return MerchantAcknowledgePurchaseOrderLine(
        )
        """

    def testMerchantAcknowledgePurchaseOrderLine(self):
        """Test MerchantAcknowledgePurchaseOrderLine"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
