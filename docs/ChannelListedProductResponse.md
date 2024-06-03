# ChannelListedProductResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_product_no** | **str** | The unique product reference used by the Channel | [optional] 
**channel_status** | [**ListedProductChannelStatus**](ListedProductChannelStatus.md) |  | [optional] 
**ean** | **str** | EAN | [optional] 
**export_status** | [**ListedProductExportStatus**](ListedProductExportStatus.md) |  | [optional] 
**merchant_product_no** | **str** | Your product number (SKU) | [optional] 
**last_exported_price** | **float** | Your product last exported price | [optional] 
**last_exported_stock** | **int** | Your product last exported stock | [optional] 

## Example

```python
from openapi_client.models.channel_listed_product_response import ChannelListedProductResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelListedProductResponse from a JSON string
channel_listed_product_response_instance = ChannelListedProductResponse.from_json(json)
# print the JSON string representation of the object
print(ChannelListedProductResponse.to_json())

# convert the object into a dict
channel_listed_product_response_dict = channel_listed_product_response_instance.to_dict()
# create an instance of ChannelListedProductResponse from a dict
channel_listed_product_response_from_dict = ChannelListedProductResponse.from_dict(channel_listed_product_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


