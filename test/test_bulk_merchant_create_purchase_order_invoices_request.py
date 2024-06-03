# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.bulk_merchant_create_purchase_order_invoices_request import BulkMerchantCreatePurchaseOrderInvoicesRequest

class TestBulkMerchantCreatePurchaseOrderInvoicesRequest(unittest.TestCase):
    """BulkMerchantCreatePurchaseOrderInvoicesRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BulkMerchantCreatePurchaseOrderInvoicesRequest:
        """Test BulkMerchantCreatePurchaseOrderInvoicesRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BulkMerchantCreatePurchaseOrderInvoicesRequest`
        """
        model = BulkMerchantCreatePurchaseOrderInvoicesRequest()
        if include_optional:
            return BulkMerchantCreatePurchaseOrderInvoicesRequest(
                model = [
                    openapi_client.models.merchant_purchase_order_invoice.MerchantPurchaseOrderInvoice(
                        invoice_no = '', 
                        invoice_type = 'INVOICE', 
                        invoice_total_amount = 1.337, 
                        invoice_total_currency_code = '', 
                        remit_to_party = openapi_client.models.merchant_vendor_party.MerchantVendorParty(
                            name = '', 
                            address_line1 = '', 
                            address_line2 = '', 
                            address_line3 = '', 
                            city = '', 
                            county = '', 
                            district = '', 
                            state_or_region = '', 
                            postal_code = '', 
                            country_code = '', 
                            phone = '', 
                            tax_registration_type = 'VAT', 
                            tax_registration_no = '', ), 
                        ship_to_party_id = 56, 
                        bill_to_party_id = 56, 
                        additional_details = [
                            openapi_client.models.purchase_order_invoice_additional_details.PurchaseOrderInvoiceAdditionalDetails(
                                type = 'SUR', 
                                detail = '', 
                                language_code = '', )
                            ], 
                        lines = [
                            openapi_client.models.merchant_purchase_order_invoice_line.MerchantPurchaseOrderInvoiceLine(
                                channel_purchase_order_no = '', 
                                merchant_purchase_order_no = '', 
                                channel_product_no = '', 
                                merchant_product_no = '', 
                                quantity = 56, 
                                net_cost_currency_code = '', 
                                net_cost_amount = 1.337, 
                                hsn_code = '', 
                                cn_reference_invoice_number = '', 
                                cn_debit_note_number = '', 
                                cn_returns_reference_number = '', 
                                cn_rma_id = '', 
                                cn_goods_return_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                cn_coop_reference_number = '', 
                                cn_consignors_reference_number = '', 
                                allowance_details = [
                                    openapi_client.models.purchase_order_invoice_allowance_details.PurchaseOrderInvoiceAllowanceDetails(
                                        description = '', 
                                        charge_amount = 1.337, 
                                        charge_amount_currency_code = '', 
                                        tax_details = openapi_client.models.purchase_order_invoice_tax_details.PurchaseOrderInvoiceTaxDetails(
                                            tax_type = 'CGST', 
                                            tax_rate = 1.337, 
                                            tax_amount = 1.337, 
                                            tax_amount_currency_code = '', 
                                            taxable_amount = 1.337, 
                                            taxable_amount_currency_code = '', ), )
                                    ], 
                                tax_details = [
                                    openapi_client.models.purchase_order_invoice_tax_details.PurchaseOrderInvoiceTaxDetails(
                                        tax_rate = 1.337, 
                                        tax_amount = 1.337, 
                                        tax_amount_currency_code = '', 
                                        taxable_amount = 1.337, 
                                        taxable_amount_currency_code = '', )
                                    ], 
                                charge_details = [
                                    openapi_client.models.purchase_order_invoice_charge_details.PurchaseOrderInvoiceChargeDetails(
                                        description = '', 
                                        charge_amount = 1.337, 
                                        charge_amount_currency_code = '', )
                                    ], )
                            ], )
                    ],
                channel_id = 56
            )
        else:
            return BulkMerchantCreatePurchaseOrderInvoicesRequest(
        )
        """

    def testBulkMerchantCreatePurchaseOrderInvoicesRequest(self):
        """Test BulkMerchantCreatePurchaseOrderInvoicesRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()