# MerchantProductResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** | Is the product active for the Merchant?. | [optional] 
**extra_data** | [**List[MerchantProductExtraDataItemResponse]**](MerchantProductExtraDataItemResponse.md) |  | [optional] 
**parent_merchant_product_no** | **str** | A unique identifier of the parent product. (parent sku). | [optional] 
**parent_merchant_product_no2** | **str** | A unique identifier of the grandparent product. (grandparent sku). | [optional] 
**name** | **str** | The name of the product. | [optional] 
**description** | **str** | A description of the product. Can contain these HTML tags:  div, span, pre, p, br, hr, hgroup, h1, h2, h3, h4, h5, h6, ul, ol, li, dl, dt, dd, strong, em, b, i, u, img, a, abbr, address, blockquote, area, audio, video, caption, table, tbody, td, tfoot, th, thead, tr. | [optional] 
**brand** | **str** | The brand of the product. | [optional] 
**size** | **str** | Optional. The size of the product (variant). E.g. fashion size (S-XL, 46-56, etc), width of the watch, etc.. | [optional] 
**color** | **str** | Optional. The color of the product (variant). | [optional] 
**ean** | **str** | The EAN of GTIN of the product. | [optional] 
**manufacturer_product_number** | **str** | The unique product reference used by the manufacturer/vendor of the product. | [optional] 
**merchant_product_no** | **str** | A unique identifier of the product. (sku). | 
**stock** | **int** | The number of items in stock. | [optional] 
**price** | **float** | Price, including VAT. | [optional] 
**min_price** | **float** | Min price, including VAT. | [optional] 
**max_price** | **float** | Max price, including VAT. | [optional] 
**msrp** | **float** | Manufacturer&#39;s suggested retail price. | [optional] 
**purchase_price** | **float** | Optional. The purchase price of the product. Useful for repricing. | [optional] 
**vat_rate_type** | [**VatRateType**](VatRateType.md) |  | [optional] 
**shipping_cost** | **float** | Shipping cost of the product. | [optional] 
**shipping_time** | **str** | A textual representation of the shippingtime.  For example, in Dutch: &#39;Op werkdagen voor 22:00 uur besteld, morgen in huis&#39;. | [optional] 
**url** | **str** | A URL pointing to the merchant&#39;s webpage  which displays this product. | [optional] 
**image_url** | **str** | A URL at which an image of this product  can be found. | [optional] 
**extra_image_url1** | **str** | Url to an additional image of product (1). | [optional] 
**extra_image_url2** | **str** | Url to an additional image of product (2). | [optional] 
**extra_image_url3** | **str** | Url to an additional image of product (3). | [optional] 
**extra_image_url4** | **str** | Url to an additional image of product (4). | [optional] 
**extra_image_url5** | **str** | Url to an additional image of product (5). | [optional] 
**extra_image_url6** | **str** | Url to an additional image of product (6). | [optional] 
**extra_image_url7** | **str** | Url to an additional image of product (7). | [optional] 
**extra_image_url8** | **str** | Url to an additional image of product (8). | [optional] 
**extra_image_url9** | **str** | Url to an additional image of product (9). | [optional] 
**is_frozen** | **bool** | Specifies whether Product is disabled on all channels. | [optional] 
**category_trail** | **str** | The category to which this product belongs.  Please supply this field in the following format:  &#39;maincategory &gt; category &gt; subcategory&#39;  For example:  &#39;vehicles &gt; bikes &gt; mountainbike&#39;. | [optional] 

## Example

```python
from openapi_client.models.merchant_product_response import MerchantProductResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantProductResponse from a JSON string
merchant_product_response_instance = MerchantProductResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantProductResponse.to_json())

# convert the object into a dict
merchant_product_response_dict = merchant_product_response_instance.to_dict()
# create an instance of MerchantProductResponse from a dict
merchant_product_response_from_dict = MerchantProductResponse.from_dict(merchant_product_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


