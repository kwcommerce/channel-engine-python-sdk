# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.collection_of_merchant_fulfillment_stock_get_stock_locations_request import CollectionOfMerchantFulfillmentStockGetStockLocationsRequest

class TestCollectionOfMerchantFulfillmentStockGetStockLocationsRequest(unittest.TestCase):
    """CollectionOfMerchantFulfillmentStockGetStockLocationsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CollectionOfMerchantFulfillmentStockGetStockLocationsRequest:
        """Test CollectionOfMerchantFulfillmentStockGetStockLocationsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CollectionOfMerchantFulfillmentStockGetStockLocationsRequest`
        """
        model = CollectionOfMerchantFulfillmentStockGetStockLocationsRequest()
        if include_optional:
            return CollectionOfMerchantFulfillmentStockGetStockLocationsRequest(
                content = [
                    openapi_client.models.merchant_fulfillment_stock_get_stock_locations_request.MerchantFulfillmentStockGetStockLocationsRequest(
                        merchant_product_nos = [
                            ''
                            ], 
                        page_index = 0, 
                        page_size = 0, )
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
            return CollectionOfMerchantFulfillmentStockGetStockLocationsRequest(
        )
        """

    def testCollectionOfMerchantFulfillmentStockGetStockLocationsRequest(self):
        """Test CollectionOfMerchantFulfillmentStockGetStockLocationsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
