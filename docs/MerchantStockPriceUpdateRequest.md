# MerchantStockPriceUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_product_no** | **str** | The unique product reference used by the Merchant (sku). | 
**stock** | **int** | The stock of the product. Should not be negative. | [optional] 
**price** | **float** | The price of the product. Should not be negative. | [optional] 
**stock_location_id** | **int** | The stock location id of the updated stock. If not provided, the stock from the default stock location will be updated. | [optional] 

## Example

```python
from openapi_client.models.merchant_stock_price_update_request import MerchantStockPriceUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantStockPriceUpdateRequest from a JSON string
merchant_stock_price_update_request_instance = MerchantStockPriceUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantStockPriceUpdateRequest.to_json())

# convert the object into a dict
merchant_stock_price_update_request_dict = merchant_stock_price_update_request_instance.to_dict()
# create an instance of MerchantStockPriceUpdateRequest from a dict
merchant_stock_price_update_request_from_dict = MerchantStockPriceUpdateRequest.from_dict(merchant_stock_price_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


