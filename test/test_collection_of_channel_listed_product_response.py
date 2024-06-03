# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.collection_of_channel_listed_product_response import CollectionOfChannelListedProductResponse

class TestCollectionOfChannelListedProductResponse(unittest.TestCase):
    """CollectionOfChannelListedProductResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CollectionOfChannelListedProductResponse:
        """Test CollectionOfChannelListedProductResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CollectionOfChannelListedProductResponse`
        """
        model = CollectionOfChannelListedProductResponse()
        if include_optional:
            return CollectionOfChannelListedProductResponse(
                content = [
                    openapi_client.models.channel_listed_product_response.ChannelListedProductResponse(
                        channel_product_no = '', 
                        channel_status = 'NONE', 
                        ean = '', 
                        export_status = 'CREATED', 
                        merchant_product_no = '', 
                        last_exported_price = 1.337, 
                        last_exported_stock = 56, )
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
            return CollectionOfChannelListedProductResponse(
        )
        """

    def testCollectionOfChannelListedProductResponse(self):
        """Test CollectionOfChannelListedProductResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
