# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_address_response import MerchantAddressResponse

class TestMerchantAddressResponse(unittest.TestCase):
    """MerchantAddressResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantAddressResponse:
        """Test MerchantAddressResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantAddressResponse`
        """
        model = MerchantAddressResponse()
        if include_optional:
            return MerchantAddressResponse(
                line1 = '',
                line2 = '',
                line3 = '',
                gender = 'MALE',
                company_name = '',
                first_name = '',
                last_name = '',
                street_name = '',
                house_nr = '',
                house_nr_addition = '',
                zip_code = '',
                city = '',
                region = '',
                country_iso = '',
                original = ''
            )
        else:
            return MerchantAddressResponse(
        )
        """

    def testMerchantAddressResponse(self):
        """Test MerchantAddressResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
