# MerchantProductWithBuyBoxPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** | Product SKU number | [optional] 
**gtin** | **str** | Product GTIN | [optional] 
**buy_box_price** | **float** | Price of Buy box winner (excl. shipping cost)  Note: not all channels have a separate shipping cost field (e.g. bol.com), so can be the same as BuyBoxPriceInclShipping | [optional] 
**buy_box_price_incl_shipping** | **float** | Price of Buy box winner (incl. shipping cost).  If null, then there is no data or no Buy box winner | [optional] 
**is_merchant_buy_box_winner** | **bool** | Are you the Buy box winner or not? | [optional] 

## Example

```python
from openapi_client.models.merchant_product_with_buy_box_price import MerchantProductWithBuyBoxPrice

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantProductWithBuyBoxPrice from a JSON string
merchant_product_with_buy_box_price_instance = MerchantProductWithBuyBoxPrice.from_json(json)
# print the JSON string representation of the object
print(MerchantProductWithBuyBoxPrice.to_json())

# convert the object into a dict
merchant_product_with_buy_box_price_dict = merchant_product_with_buy_box_price_instance.to_dict()
# create an instance of MerchantProductWithBuyBoxPrice from a dict
merchant_product_with_buy_box_price_from_dict = MerchantProductWithBuyBoxPrice.from_dict(merchant_product_with_buy_box_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


