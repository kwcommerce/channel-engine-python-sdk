# FreezeProductRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_product_no** | **str** |  | 
**reason** | **str** |  | 
**action** | [**FreezingActionRequest**](FreezingActionRequest.md) |  | 

## Example

```python
from openapi_client.models.freeze_product_request import FreezeProductRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FreezeProductRequest from a JSON string
freeze_product_request_instance = FreezeProductRequest.from_json(json)
# print the JSON string representation of the object
print(FreezeProductRequest.to_json())

# convert the object into a dict
freeze_product_request_dict = freeze_product_request_instance.to_dict()
# create an instance of FreezeProductRequest from a dict
freeze_product_request_from_dict = FreezeProductRequest.from_dict(freeze_product_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


