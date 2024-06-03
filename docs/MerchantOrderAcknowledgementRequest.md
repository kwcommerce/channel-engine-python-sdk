# MerchantOrderAcknowledgementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_order_no** | **str** | Your own order reference, this will be used in consecutive order processing API calls. | 
**order_id** | **int** | The ChannelEngine order ID of the order you would like to acknowledge. | 

## Example

```python
from openapi_client.models.merchant_order_acknowledgement_request import MerchantOrderAcknowledgementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantOrderAcknowledgementRequest from a JSON string
merchant_order_acknowledgement_request_instance = MerchantOrderAcknowledgementRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantOrderAcknowledgementRequest.to_json())

# convert the object into a dict
merchant_order_acknowledgement_request_dict = merchant_order_acknowledgement_request_instance.to_dict()
# create an instance of MerchantOrderAcknowledgementRequest from a dict
merchant_order_acknowledgement_request_from_dict = MerchantOrderAcknowledgementRequest.from_dict(merchant_order_acknowledgement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


