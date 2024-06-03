# MerchantReturnAcknowledgeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_id** | **int** |  | [optional] 
**merchant_return_no** | **str** |  | 

## Example

```python
from openapi_client.models.merchant_return_acknowledge_request import MerchantReturnAcknowledgeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantReturnAcknowledgeRequest from a JSON string
merchant_return_acknowledge_request_instance = MerchantReturnAcknowledgeRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantReturnAcknowledgeRequest.to_json())

# convert the object into a dict
merchant_return_acknowledge_request_dict = merchant_return_acknowledge_request_instance.to_dict()
# create an instance of MerchantReturnAcknowledgeRequest from a dict
merchant_return_acknowledge_request_from_dict = MerchantReturnAcknowledgeRequest.from_dict(merchant_return_acknowledge_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


