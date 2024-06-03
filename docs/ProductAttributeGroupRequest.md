# ProductAttributeGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_name** | **str** |  | 
**product_extra_data_keys** | **List[str]** |  | 

## Example

```python
from openapi_client.models.product_attribute_group_request import ProductAttributeGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductAttributeGroupRequest from a JSON string
product_attribute_group_request_instance = ProductAttributeGroupRequest.from_json(json)
# print the JSON string representation of the object
print(ProductAttributeGroupRequest.to_json())

# convert the object into a dict
product_attribute_group_request_dict = product_attribute_group_request_instance.to_dict()
# create an instance of ProductAttributeGroupRequest from a dict
product_attribute_group_request_from_dict = ProductAttributeGroupRequest.from_dict(product_attribute_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


