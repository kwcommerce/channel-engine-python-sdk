# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_product_attribute_group_with_linked_channels_response import MerchantProductAttributeGroupWithLinkedChannelsResponse

class TestMerchantProductAttributeGroupWithLinkedChannelsResponse(unittest.TestCase):
    """MerchantProductAttributeGroupWithLinkedChannelsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantProductAttributeGroupWithLinkedChannelsResponse:
        """Test MerchantProductAttributeGroupWithLinkedChannelsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantProductAttributeGroupWithLinkedChannelsResponse`
        """
        model = MerchantProductAttributeGroupWithLinkedChannelsResponse()
        if include_optional:
            return MerchantProductAttributeGroupWithLinkedChannelsResponse(
                product_attribute_group_id = 56,
                group_name = '',
                linked_channels = [
                    openapi_client.models.merchant_product_attribute_group_channel_info_response.MerchantProductAttributeGroupChannelInfoResponse(
                        channel_id = 56, 
                        channel_name = '', 
                        is_enabled = True, 
                        global_channel_id = 56, 
                        global_channel_name = '', )
                    ]
            )
        else:
            return MerchantProductAttributeGroupWithLinkedChannelsResponse(
        )
        """

    def testMerchantProductAttributeGroupWithLinkedChannelsResponse(self):
        """Test MerchantProductAttributeGroupWithLinkedChannelsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()