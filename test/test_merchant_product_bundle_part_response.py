# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_product_bundle_part_response import MerchantProductBundlePartResponse

class TestMerchantProductBundlePartResponse(unittest.TestCase):
    """MerchantProductBundlePartResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantProductBundlePartResponse:
        """Test MerchantProductBundlePartResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantProductBundlePartResponse`
        """
        model = MerchantProductBundlePartResponse()
        if include_optional:
            return MerchantProductBundlePartResponse(
                merchant_product_no = '',
                ean = '',
                name = '',
                quantity = 56,
                price = 1.337
            )
        else:
            return MerchantProductBundlePartResponse(
        )
        """

    def testMerchantProductBundlePartResponse(self):
        """Test MerchantProductBundlePartResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
