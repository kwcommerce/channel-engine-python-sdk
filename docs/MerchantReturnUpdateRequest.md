# MerchantReturnUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_id** | **int** | The ChannelEngine return ID of the return you would like to update. | 
**lines** | [**List[MerchantReturnLineUpdateRequest]**](MerchantReturnLineUpdateRequest.md) |  | 

## Example

```python
from openapi_client.models.merchant_return_update_request import MerchantReturnUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantReturnUpdateRequest from a JSON string
merchant_return_update_request_instance = MerchantReturnUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantReturnUpdateRequest.to_json())

# convert the object into a dict
merchant_return_update_request_dict = merchant_return_update_request_instance.to_dict()
# create an instance of MerchantReturnUpdateRequest from a dict
merchant_return_update_request_from_dict = MerchantReturnUpdateRequest.from_dict(merchant_return_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


