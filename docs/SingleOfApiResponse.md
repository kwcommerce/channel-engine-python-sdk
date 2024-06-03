# SingleOfApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**ApiResponse**](ApiResponse.md) |  | [optional] 
**status_code** | **int** |  | [optional] 
**request_id** | **str** |  | [optional] 
**log_id** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**exception_type** | **str** |  | [optional] 
**validation_errors** | **Dict[str, Optional[List[str]]]** |  | [optional] 

## Example

```python
from openapi_client.models.single_of_api_response import SingleOfApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleOfApiResponse from a JSON string
single_of_api_response_instance = SingleOfApiResponse.from_json(json)
# print the JSON string representation of the object
print(SingleOfApiResponse.to_json())

# convert the object into a dict
single_of_api_response_dict = single_of_api_response_instance.to_dict()
# create an instance of SingleOfApiResponse from a dict
single_of_api_response_from_dict = SingleOfApiResponse.from_dict(single_of_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


