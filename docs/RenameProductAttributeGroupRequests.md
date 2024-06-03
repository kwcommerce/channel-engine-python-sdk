# RenameProductAttributeGroupRequests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_name** | **str** |  | [optional] 
**new_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.rename_product_attribute_group_requests import RenameProductAttributeGroupRequests

# TODO update the JSON string below
json = "{}"
# create an instance of RenameProductAttributeGroupRequests from a JSON string
rename_product_attribute_group_requests_instance = RenameProductAttributeGroupRequests.from_json(json)
# print the JSON string representation of the object
print(RenameProductAttributeGroupRequests.to_json())

# convert the object into a dict
rename_product_attribute_group_requests_dict = rename_product_attribute_group_requests_instance.to_dict()
# create an instance of RenameProductAttributeGroupRequests from a dict
rename_product_attribute_group_requests_from_dict = RenameProductAttributeGroupRequests.from_dict(rename_product_attribute_group_requests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


