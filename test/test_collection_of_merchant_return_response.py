# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.collection_of_merchant_return_response import CollectionOfMerchantReturnResponse

class TestCollectionOfMerchantReturnResponse(unittest.TestCase):
    """CollectionOfMerchantReturnResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CollectionOfMerchantReturnResponse:
        """Test CollectionOfMerchantReturnResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CollectionOfMerchantReturnResponse`
        """
        model = CollectionOfMerchantReturnResponse()
        if include_optional:
            return CollectionOfMerchantReturnResponse(
                content = [
                    openapi_client.models.merchant_return_response.MerchantReturnResponse(
                        merchant_order_no = '', 
                        channel_order_no = '', 
                        channel_id = 56, 
                        global_channel_id = 56, 
                        global_channel_name = '', 
                        lines = [
                            openapi_client.models.merchant_return_line_response.MerchantReturnLineResponse(
                                merchant_product_no = '', 
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
                                stock_location = openapi_client.models.merchant_stock_location_response.MerchantStockLocationResponse(
                                    id = 56, 
                                    name = '', ), 
                                quantity = 0, 
                                extra_data = {
                                    'key' : ''
                                    }, )
                            ], 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        merchant_return_no = '', 
                        channel_return_no = '', 
                        status = 'IN_PROGRESS', 
                        acknowledged_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = 56, 
                        reason = 'PRODUCT_DEFECT', 
                        customer_comment = '', 
                        merchant_comment = '', 
                        refund_incl_vat = 0, 
                        refund_excl_vat = 0, 
                        return_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        extra_data = {
                            'key' : ''
                            }, )
                    ],
                count = 56,
                total_count = 56,
                items_per_page = 56,
                status_code = 56,
                request_id = '',
                log_id = '',
                success = True,
                message = '',
                exception_type = '',
                validation_errors = {
                    'key' : [
                        ''
                        ]
                    }
            )
        else:
            return CollectionOfMerchantReturnResponse(
        )
        """

    def testCollectionOfMerchantReturnResponse(self):
        """Test CollectionOfMerchantReturnResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()