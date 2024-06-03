# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.vat_settings_response import VatSettingsResponse

class TestVatSettingsResponse(unittest.TestCase):
    """VatSettingsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VatSettingsResponse:
        """Test VatSettingsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VatSettingsResponse`
        """
        model = VatSettingsResponse()
        if include_optional:
            return VatSettingsResponse(
                country_iso = '',
                no = '',
                standard_rate = 1.337,
                reduced_rate = 1.337,
                super_reduced_rate = 1.337
            )
        else:
            return VatSettingsResponse(
        )
        """

    def testVatSettingsResponse(self):
        """Test VatSettingsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
