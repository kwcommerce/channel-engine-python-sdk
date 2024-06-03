# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_create_settlements_report_request import MerchantCreateSettlementsReportRequest

class TestMerchantCreateSettlementsReportRequest(unittest.TestCase):
    """MerchantCreateSettlementsReportRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantCreateSettlementsReportRequest:
        """Test MerchantCreateSettlementsReportRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantCreateSettlementsReportRequest`
        """
        model = MerchantCreateSettlementsReportRequest()
        if include_optional:
            return MerchantCreateSettlementsReportRequest(
                settlement_ids = [
                    56
                    ],
                type = 'SUMMARY',
                custom_json_mapper = openapi_client.models.settlement_custom_json_mapper.SettlementCustomJsonMapper(
                    mapping = {
                        'key' : null
                        }, ),
                channel_references_by_channel_id = {
                    'key' : ''
                    }
            )
        else:
            return MerchantCreateSettlementsReportRequest(
                settlement_ids = [
                    56
                    ],
                type = 'SUMMARY',
        )
        """

    def testMerchantCreateSettlementsReportRequest(self):
        """Test MerchantCreateSettlementsReportRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
