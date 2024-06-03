# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.purchase_order_invoice_charge_details import PurchaseOrderInvoiceChargeDetails

class TestPurchaseOrderInvoiceChargeDetails(unittest.TestCase):
    """PurchaseOrderInvoiceChargeDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PurchaseOrderInvoiceChargeDetails:
        """Test PurchaseOrderInvoiceChargeDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PurchaseOrderInvoiceChargeDetails`
        """
        model = PurchaseOrderInvoiceChargeDetails()
        if include_optional:
            return PurchaseOrderInvoiceChargeDetails(
                type = 'FREIGHT',
                description = '',
                charge_amount = 1.337,
                charge_amount_currency_code = '',
                tax_details = openapi_client.models.purchase_order_invoice_tax_details.PurchaseOrderInvoiceTaxDetails(
                    tax_type = 'CGST', 
                    tax_rate = 1.337, 
                    tax_amount = 1.337, 
                    tax_amount_currency_code = '', 
                    taxable_amount = 1.337, 
                    taxable_amount_currency_code = '', )
            )
        else:
            return PurchaseOrderInvoiceChargeDetails(
        )
        """

    def testPurchaseOrderInvoiceChargeDetails(self):
        """Test PurchaseOrderInvoiceChargeDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
