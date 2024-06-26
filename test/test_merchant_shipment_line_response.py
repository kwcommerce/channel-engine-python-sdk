# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_shipment_line_response import MerchantShipmentLineResponse

class TestMerchantShipmentLineResponse(unittest.TestCase):
    """MerchantShipmentLineResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantShipmentLineResponse:
        """Test MerchantShipmentLineResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantShipmentLineResponse`
        """
        model = MerchantShipmentLineResponse()
        if include_optional:
            return MerchantShipmentLineResponse(
                merchant_product_no = '0',
                merchant_bundle_product_no = '',
                channel_product_no = '',
                order_line = openapi_client.models.merchant_order_line_response.MerchantOrderLineResponse(
                    id = 56, 
                    channel_order_line_no = '', 
                    status = 'IN_PROGRESS', 
                    is_fulfillment_by_marketplace = True, 
                    gtin = '', 
                    description = '', 
                    stock_location = openapi_client.models.merchant_stock_location_response.MerchantStockLocationResponse(
                        id = 56, 
                        name = '', ), 
                    unit_vat = 1.337, 
                    line_total_incl_vat = 1.337, 
                    line_vat = 1.337, 
                    original_unit_price_incl_vat = 1.337, 
                    original_unit_vat = 1.337, 
                    original_line_total_incl_vat = 1.337, 
                    original_line_vat = 1.337, 
                    original_fee_fixed = 1.337, 
                    bundle_product_merchant_product_no = '', 
                    juris_code = '', 
                    juris_name = '', 
                    vat_rate = 1.337, 
                    unit_price_excl_vat = 1.337, 
                    line_total_excl_vat = 1.337, 
                    original_unit_price_excl_vat = 1.337, 
                    original_line_total_excl_vat = 1.337, 
                    extra_data = [
                        openapi_client.models.merchant_order_line_extra_data_response.MerchantOrderLineExtraDataResponse(
                            key = '', 
                            value = '', )
                        ], 
                    channel_product_no = '', 
                    merchant_product_no = '', 
                    quantity = 0, 
                    cancellation_requested_quantity = 0, 
                    unit_price_incl_vat = 0, 
                    fee_fixed = 0, 
                    fee_rate = 0, 
                    condition = 'NEW', 
                    expected_delivery_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    latest_delivery_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    expected_shipment_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    latest_shipment_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                shipment_status = 'SHIPPED',
                extra_data = {
                    'key' : ''
                    },
                quantity = 0
            )
        else:
            return MerchantShipmentLineResponse(
                merchant_product_no = '0',
                quantity = 0,
        )
        """

    def testMerchantShipmentLineResponse(self):
        """Test MerchantShipmentLineResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
