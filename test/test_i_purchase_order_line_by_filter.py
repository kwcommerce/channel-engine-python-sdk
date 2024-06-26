# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.i_purchase_order_line_by_filter import IPurchaseOrderLineByFilter

class TestIPurchaseOrderLineByFilter(unittest.TestCase):
    """IPurchaseOrderLineByFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IPurchaseOrderLineByFilter:
        """Test IPurchaseOrderLineByFilter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IPurchaseOrderLineByFilter`
        """
        model = IPurchaseOrderLineByFilter()
        if include_optional:
            return IPurchaseOrderLineByFilter(
                id = 56,
                channel_order_line_no = '',
                channel_product_no = '',
                merchant_product_no = '',
                quantity = 56,
                is_back_order_allowed = True,
                unit_of_measure = 'CASES',
                unit_size = 56,
                net_cost_amount = 1.337,
                net_cost_currency = '',
                list_price_amount = 1.337,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                acknowledged_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                line_total = 1.337
            )
        else:
            return IPurchaseOrderLineByFilter(
        )
        """

    def testIPurchaseOrderLineByFilter(self):
        """Test IPurchaseOrderLineByFilter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
