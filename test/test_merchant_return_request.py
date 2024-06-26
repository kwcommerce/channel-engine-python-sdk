# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_return_request import MerchantReturnRequest

class TestMerchantReturnRequest(unittest.TestCase):
    """MerchantReturnRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantReturnRequest:
        """Test MerchantReturnRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantReturnRequest`
        """
        model = MerchantReturnRequest()
        if include_optional:
            return MerchantReturnRequest(
                merchant_order_no = '',
                merchant_return_no = '',
                lines = [
                    openapi_client.models.merchant_return_line_request.MerchantReturnLineRequest(
                        merchant_product_no = '', 
                        quantity = 0, 
                        extra_data = {
                            'key' : ''
                            }, )
                    ],
                id = 56,
                reason = 'PRODUCT_DEFECT',
                customer_comment = '',
                merchant_comment = '',
                refund_incl_vat = 0,
                refund_excl_vat = 0,
                return_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                extra_data = {
                    'key' : ''
                    }
            )
        else:
            return MerchantReturnRequest(
                merchant_order_no = '',
                merchant_return_no = '',
                lines = [
                    openapi_client.models.merchant_return_line_request.MerchantReturnLineRequest(
                        merchant_product_no = '', 
                        quantity = 0, 
                        extra_data = {
                            'key' : ''
                            }, )
                    ],
        )
        """

    def testMerchantReturnRequest(self):
        """Test MerchantReturnRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
