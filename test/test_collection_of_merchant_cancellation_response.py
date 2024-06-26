# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.collection_of_merchant_cancellation_response import CollectionOfMerchantCancellationResponse

class TestCollectionOfMerchantCancellationResponse(unittest.TestCase):
    """CollectionOfMerchantCancellationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CollectionOfMerchantCancellationResponse:
        """Test CollectionOfMerchantCancellationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CollectionOfMerchantCancellationResponse`
        """
        model = CollectionOfMerchantCancellationResponse()
        if include_optional:
            return CollectionOfMerchantCancellationResponse(
                content = [
                    openapi_client.models.merchant_cancellation_response.MerchantCancellationResponse(
                        id = 56, 
                        merchant_cancellation_no = '', 
                        merchant_order_no = '0', 
                        channel_order_no = '', 
                        lines = [
                            openapi_client.models.merchant_cancellation_line_response.MerchantCancellationLineResponse(
                                id = 56, 
                                merchant_product_no = '', 
                                channel_product_no = '', 
                                quantity = 0, )
                            ], 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        reason = '', 
                        reason_code = 'NOT_IN_STOCK', )
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
            return CollectionOfMerchantCancellationResponse(
        )
        """

    def testCollectionOfMerchantCancellationResponse(self):
        """Test CollectionOfMerchantCancellationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
