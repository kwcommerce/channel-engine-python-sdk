# MerchantStockLocationUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock** | **int** | The stock of the product. Should not be negative. | [optional] 
**stock_location_id** | **int** | The stock location id of the updated stock. If not provided, the stock from the default stock location will be updated. | [optional] 

## Example

```python
from openapi_client.models.merchant_stock_location_update_request import MerchantStockLocationUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantStockLocationUpdateRequest from a JSON string
merchant_stock_location_update_request_instance = MerchantStockLocationUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantStockLocationUpdateRequest.to_json())

# convert the object into a dict
merchant_stock_location_update_request_dict = merchant_stock_location_update_request_instance.to_dict()
# create an instance of MerchantStockLocationUpdateRequest from a dict
merchant_stock_location_update_request_from_dict = MerchantStockLocationUpdateRequest.from_dict(merchant_stock_location_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


