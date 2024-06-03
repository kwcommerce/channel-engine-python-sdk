# MerchantOrderLineExtraDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.merchant_order_line_extra_data_response import MerchantOrderLineExtraDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantOrderLineExtraDataResponse from a JSON string
merchant_order_line_extra_data_response_instance = MerchantOrderLineExtraDataResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantOrderLineExtraDataResponse.to_json())

# convert the object into a dict
merchant_order_line_extra_data_response_dict = merchant_order_line_extra_data_response_instance.to_dict()
# create an instance of MerchantOrderLineExtraDataResponse from a dict
merchant_order_line_extra_data_response_from_dict = MerchantOrderLineExtraDataResponse.from_dict(merchant_order_line_extra_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


