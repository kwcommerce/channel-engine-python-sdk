# ProductCreationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rejected_count** | **int** |  | [optional] 
**accepted_count** | **int** |  | [optional] 
**product_messages** | [**List[ProductMessage]**](ProductMessage.md) | Messages about the rejected products. | [optional] 

## Example

```python
from openapi_client.models.product_creation_result import ProductCreationResult

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCreationResult from a JSON string
product_creation_result_instance = ProductCreationResult.from_json(json)
# print the JSON string representation of the object
print(ProductCreationResult.to_json())

# convert the object into a dict
product_creation_result_dict = product_creation_result_instance.to_dict()
# create an instance of ProductCreationResult from a dict
product_creation_result_from_dict = ProductCreationResult.from_dict(product_creation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


