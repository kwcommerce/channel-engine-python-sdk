# MerchantOrderCommentUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_order_no** | **str** | Your own order reference for the order you would like to update the comment for.  Either this field or OrderId is required | [optional] 
**order_id** | **int** | The ChannelEngine order ID of the order you would like to update the comment for.  Either this field or MerchantOrderNo is required | [optional] 
**merchant_comment** | **str** | The merchant comment you would like add / update for the order. | 

## Example

```python
from openapi_client.models.merchant_order_comment_update_request import MerchantOrderCommentUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantOrderCommentUpdateRequest from a JSON string
merchant_order_comment_update_request_instance = MerchantOrderCommentUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantOrderCommentUpdateRequest.to_json())

# convert the object into a dict
merchant_order_comment_update_request_dict = merchant_order_comment_update_request_instance.to_dict()
# create an instance of MerchantOrderCommentUpdateRequest from a dict
merchant_order_comment_update_request_from_dict = MerchantOrderCommentUpdateRequest.from_dict(merchant_order_comment_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


