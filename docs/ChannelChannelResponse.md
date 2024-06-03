# ChannelChannelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **int** | The ID of the Channel. | [optional] 
**is_enabled** | **bool** | A boolean value indicating whether the Channel is enabled. | [optional] 
**channel_name** | **str** | The name of the Channel. | [optional] 
**reference** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.channel_channel_response import ChannelChannelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelChannelResponse from a JSON string
channel_channel_response_instance = ChannelChannelResponse.from_json(json)
# print the JSON string representation of the object
print(ChannelChannelResponse.to_json())

# convert the object into a dict
channel_channel_response_dict = channel_channel_response_instance.to_dict()
# create an instance of ChannelChannelResponse from a dict
channel_channel_response_from_dict = ChannelChannelResponse.from_dict(channel_channel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


