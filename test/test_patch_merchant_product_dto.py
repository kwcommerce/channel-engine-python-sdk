# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.patch_merchant_product_dto import PatchMerchantProductDto

class TestPatchMerchantProductDto(unittest.TestCase):
    """PatchMerchantProductDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchMerchantProductDto:
        """Test PatchMerchantProductDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchMerchantProductDto`
        """
        model = PatchMerchantProductDto()
        if include_optional:
            return PatchMerchantProductDto(
                properties_to_update = [
                    ''
                    ],
                merchant_product_request_models = [
                    openapi_client.models.merchant_product_request.MerchantProductRequest(
                        parent_merchant_product_no = '', 
                        parent_merchant_product_no2 = '', 
                        extra_data = [
                            openapi_client.models.merchant_product_extra_data_item_request.MerchantProductExtraDataItemRequest(
                                key = '', 
                                value = '', 
                                type = 'TEXT', 
                                is_public = True, 
                                language_iso_code = '', )
                            ], 
                        name = '', 
                        description = '', 
                        brand = '', 
                        size = '', 
                        color = '', 
                        ean = '', 
                        manufacturer_product_number = '', 
                        merchant_product_no = '', 
                        stock = 0, 
                        price = 0, 
                        min_price = 0, 
                        max_price = 0, 
                        msrp = 1.337, 
                        purchase_price = 1.337, 
                        vat_rate_type = 'STANDARD', 
                        shipping_cost = 1.337, 
                        shipping_time = '', 
                        url = '', 
                        image_url = '', 
                        extra_image_url1 = '', 
                        extra_image_url2 = '', 
                        extra_image_url3 = '', 
                        extra_image_url4 = '', 
                        extra_image_url5 = '', 
                        extra_image_url6 = '', 
                        extra_image_url7 = '', 
                        extra_image_url8 = '', 
                        extra_image_url9 = '', 
                        is_frozen = True, 
                        category_trail = '', )
                    ]
            )
        else:
            return PatchMerchantProductDto(
        )
        """

    def testPatchMerchantProductDto(self):
        """Test PatchMerchantProductDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
