# MerchantOfferGetStockResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_product_no** | **str** | The product SKU. | [optional] 
**stock_location_id** | **int** | The ChannelEngine id of the stock location. | [optional] 
**stock** | **int** | The quantity of products in stock at the stock location. | [optional] 
**updated_at** | **datetime** | The timestamp of the last stock update for the stock location. | [optional] 

## Example

```python
from openapi_client.models.merchant_offer_get_stock_response import MerchantOfferGetStockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantOfferGetStockResponse from a JSON string
merchant_offer_get_stock_response_instance = MerchantOfferGetStockResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantOfferGetStockResponse.to_json())

# convert the object into a dict
merchant_offer_get_stock_response_dict = merchant_offer_get_stock_response_instance.to_dict()
# create an instance of MerchantOfferGetStockResponse from a dict
merchant_offer_get_stock_response_from_dict = MerchantOfferGetStockResponse.from_dict(merchant_offer_get_stock_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


