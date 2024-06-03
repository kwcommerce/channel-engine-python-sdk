# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.channel_global_channel_response import ChannelGlobalChannelResponse

class TestChannelGlobalChannelResponse(unittest.TestCase):
    """ChannelGlobalChannelResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChannelGlobalChannelResponse:
        """Test ChannelGlobalChannelResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChannelGlobalChannelResponse`
        """
        model = ChannelGlobalChannelResponse()
        if include_optional:
            return ChannelGlobalChannelResponse(
                country_code = '',
                global_channel_id = 56,
                channels = [
                    openapi_client.models.channel_channel_response.ChannelChannelResponse(
                        channel_id = 56, 
                        is_enabled = True, 
                        channel_name = '', 
                        reference = '', )
                    ],
                language_code = '',
                global_channel_name = ''
            )
        else:
            return ChannelGlobalChannelResponse(
        )
        """

    def testChannelGlobalChannelResponse(self):
        """Test ChannelGlobalChannelResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
