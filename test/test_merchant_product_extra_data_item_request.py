# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_product_extra_data_item_request import MerchantProductExtraDataItemRequest

class TestMerchantProductExtraDataItemRequest(unittest.TestCase):
    """MerchantProductExtraDataItemRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantProductExtraDataItemRequest:
        """Test MerchantProductExtraDataItemRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantProductExtraDataItemRequest`
        """
        model = MerchantProductExtraDataItemRequest()
        if include_optional:
            return MerchantProductExtraDataItemRequest(
                key = '',
                value = '',
                type = 'TEXT',
                is_public = True,
                language_iso_code = ''
            )
        else:
            return MerchantProductExtraDataItemRequest(
                key = '',
        )
        """

    def testMerchantProductExtraDataItemRequest(self):
        """Test MerchantProductExtraDataItemRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
