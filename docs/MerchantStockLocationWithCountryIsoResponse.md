# MerchantStockLocationWithCountryIsoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ChannelEngine id of the stock location. | [optional] 
**name** | **str** | The ChannelEngine name of the stock location. | [optional] 
**country_iso** | **str** | For example: NL, BE, FR. | [optional] 

## Example

```python
from openapi_client.models.merchant_stock_location_with_country_iso_response import MerchantStockLocationWithCountryIsoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantStockLocationWithCountryIsoResponse from a JSON string
merchant_stock_location_with_country_iso_response_instance = MerchantStockLocationWithCountryIsoResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantStockLocationWithCountryIsoResponse.to_json())

# convert the object into a dict
merchant_stock_location_with_country_iso_response_dict = merchant_stock_location_with_country_iso_response_instance.to_dict()
# create an instance of MerchantStockLocationWithCountryIsoResponse from a dict
merchant_stock_location_with_country_iso_response_from_dict = MerchantStockLocationWithCountryIsoResponse.from_dict(merchant_stock_location_with_country_iso_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


