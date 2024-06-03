# MerchantStockLocationAddressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_iso** | **str** |  | 
**street_name** | **str** |  | [optional] 
**zip_code** | **str** |  | [optional] 
**house_nr** | **str** |  | [optional] 
**house_nr_addition** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**region** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.merchant_stock_location_address_request import MerchantStockLocationAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantStockLocationAddressRequest from a JSON string
merchant_stock_location_address_request_instance = MerchantStockLocationAddressRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantStockLocationAddressRequest.to_json())

# convert the object into a dict
merchant_stock_location_address_request_dict = merchant_stock_location_address_request_instance.to_dict()
# create an instance of MerchantStockLocationAddressRequest from a dict
merchant_stock_location_address_request_from_dict = MerchantStockLocationAddressRequest.from_dict(merchant_stock_location_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


