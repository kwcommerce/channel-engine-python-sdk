# ProductExtraDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** |  | 
**key** | **str** |  | 
**value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.product_extra_data_request import ProductExtraDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductExtraDataRequest from a JSON string
product_extra_data_request_instance = ProductExtraDataRequest.from_json(json)
# print the JSON string representation of the object
print(ProductExtraDataRequest.to_json())

# convert the object into a dict
product_extra_data_request_dict = product_extra_data_request_instance.to_dict()
# create an instance of ProductExtraDataRequest from a dict
product_extra_data_request_from_dict = ProductExtraDataRequest.from_dict(product_extra_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


