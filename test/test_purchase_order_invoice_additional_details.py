# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.purchase_order_invoice_additional_details import PurchaseOrderInvoiceAdditionalDetails

class TestPurchaseOrderInvoiceAdditionalDetails(unittest.TestCase):
    """PurchaseOrderInvoiceAdditionalDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PurchaseOrderInvoiceAdditionalDetails:
        """Test PurchaseOrderInvoiceAdditionalDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PurchaseOrderInvoiceAdditionalDetails`
        """
        model = PurchaseOrderInvoiceAdditionalDetails()
        if include_optional:
            return PurchaseOrderInvoiceAdditionalDetails(
                type = 'SUR',
                detail = '',
                language_code = ''
            )
        else:
            return PurchaseOrderInvoiceAdditionalDetails(
        )
        """

    def testPurchaseOrderInvoiceAdditionalDetails(self):
        """Test PurchaseOrderInvoiceAdditionalDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
