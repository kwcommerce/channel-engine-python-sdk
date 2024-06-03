# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.single_of_merchant_settings_response import SingleOfMerchantSettingsResponse

class TestSingleOfMerchantSettingsResponse(unittest.TestCase):
    """SingleOfMerchantSettingsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SingleOfMerchantSettingsResponse:
        """Test SingleOfMerchantSettingsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SingleOfMerchantSettingsResponse`
        """
        model = SingleOfMerchantSettingsResponse()
        if include_optional:
            return SingleOfMerchantSettingsResponse(
                content = openapi_client.models.merchant_settings_response.MerchantSettingsResponse(
                    name = '', 
                    company_name = '', 
                    currency_code = '', 
                    default_culture_code = '', 
                    settings = openapi_client.models.settings_response.SettingsResponse(
                        shipment = openapi_client.models.shipment_settings_response.ShipmentSettingsResponse(
                            default_tracked_shipment_method = '', 
                            default_untracked_shipment_method = '', 
                            automatically_set_shipment_method_after_minutes = 56, ), 
                        advanced = openapi_client.models.advance_settings_response.AdvanceSettingsResponse(
                            manage_stock = True, 
                            disable_address_validation = True, 
                            skip_house_number_validation = True, 
                            skip_house_number_validation_for_country_codes = [
                                ''
                                ], 
                            set_orders_to_closed_on_import = True, 
                            disable_stock_reservation = True, 
                            disable_auto_order_cancellation = True, 
                            automatically_set_phone_number_if_empty = '', 
                            default_vat_rate = 1.337, 
                            order_too_long_on_new_hours_offset = 56, ), ), 
                    vat = [
                        openapi_client.models.vat_settings_response.VatSettingsResponse(
                            country_iso = '', 
                            no = '', 
                            standard_rate = 1.337, 
                            reduced_rate = 1.337, 
                            super_reduced_rate = 1.337, )
                        ], ),
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
            return SingleOfMerchantSettingsResponse(
        )
        """

    def testSingleOfMerchantSettingsResponse(self):
        """Test SingleOfMerchantSettingsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
