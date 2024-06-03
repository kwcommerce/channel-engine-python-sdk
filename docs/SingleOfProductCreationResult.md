# SingleOfProductCreationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**ProductCreationResult**](ProductCreationResult.md) |  | [optional] 
**status_code** | **int** |  | [optional] 
**request_id** | **str** |  | [optional] 
**log_id** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**exception_type** | **str** |  | [optional] 
**validation_errors** | **Dict[str, Optional[List[str]]]** |  | [optional] 

## Example

```python
from openapi_client.models.single_of_product_creation_result import SingleOfProductCreationResult

# TODO update the JSON string below
json = "{}"
# create an instance of SingleOfProductCreationResult from a JSON string
single_of_product_creation_result_instance = SingleOfProductCreationResult.from_json(json)
# print the JSON string representation of the object
print(SingleOfProductCreationResult.to_json())

# convert the object into a dict
single_of_product_creation_result_dict = single_of_product_creation_result_instance.to_dict()
# create an instance of SingleOfProductCreationResult from a dict
single_of_product_creation_result_from_dict = SingleOfProductCreationResult.from_dict(single_of_product_creation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


