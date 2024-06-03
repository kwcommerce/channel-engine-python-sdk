# MerchantFulfillmentStockGetStockLocationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_product_nos** | **List[str]** | List of your products&#39; MerchantProductNo&#39;s. | [optional] 
**page_index** | **int** | A page index to get the items (starts from 0) | [optional] 
**page_size** | **int** | Number of items to return (default 100) | [optional] 

## Example

```python
from openapi_client.models.merchant_fulfillment_stock_get_stock_locations_request import MerchantFulfillmentStockGetStockLocationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantFulfillmentStockGetStockLocationsRequest from a JSON string
merchant_fulfillment_stock_get_stock_locations_request_instance = MerchantFulfillmentStockGetStockLocationsRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantFulfillmentStockGetStockLocationsRequest.to_json())

# convert the object into a dict
merchant_fulfillment_stock_get_stock_locations_request_dict = merchant_fulfillment_stock_get_stock_locations_request_instance.to_dict()
# create an instance of MerchantFulfillmentStockGetStockLocationsRequest from a dict
merchant_fulfillment_stock_get_stock_locations_request_from_dict = MerchantFulfillmentStockGetStockLocationsRequest.from_dict(merchant_fulfillment_stock_get_stock_locations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


