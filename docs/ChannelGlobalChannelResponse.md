# ChannelGlobalChannelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | The country code of the Global Channel. | [optional] 
**global_channel_id** | **int** | The ID of the Global Channel. | [optional] 
**channels** | [**List[ChannelChannelResponse]**](ChannelChannelResponse.md) | The status of the instances. | [optional] 
**language_code** | **str** | The language code of the Global Channel. | [optional] 
**global_channel_name** | **str** | The name of the Global Channel. | [optional] 

## Example

```python
from openapi_client.models.channel_global_channel_response import ChannelGlobalChannelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelGlobalChannelResponse from a JSON string
channel_global_channel_response_instance = ChannelGlobalChannelResponse.from_json(json)
# print the JSON string representation of the object
print(ChannelGlobalChannelResponse.to_json())

# convert the object into a dict
channel_global_channel_response_dict = channel_global_channel_response_instance.to_dict()
# create an instance of ChannelGlobalChannelResponse from a dict
channel_global_channel_response_from_dict = ChannelGlobalChannelResponse.from_dict(channel_global_channel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


