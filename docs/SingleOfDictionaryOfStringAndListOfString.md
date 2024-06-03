# SingleOfDictionaryOfStringAndListOfString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **Dict[str, Optional[List[str]]]** |  | [optional] 
**status_code** | **int** |  | [optional] 
**request_id** | **str** |  | [optional] 
**log_id** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**exception_type** | **str** |  | [optional] 
**validation_errors** | **Dict[str, Optional[List[str]]]** |  | [optional] 

## Example

```python
from openapi_client.models.single_of_dictionary_of_string_and_list_of_string import SingleOfDictionaryOfStringAndListOfString

# TODO update the JSON string below
json = "{}"
# create an instance of SingleOfDictionaryOfStringAndListOfString from a JSON string
single_of_dictionary_of_string_and_list_of_string_instance = SingleOfDictionaryOfStringAndListOfString.from_json(json)
# print the JSON string representation of the object
print(SingleOfDictionaryOfStringAndListOfString.to_json())

# convert the object into a dict
single_of_dictionary_of_string_and_list_of_string_dict = single_of_dictionary_of_string_and_list_of_string_instance.to_dict()
# create an instance of SingleOfDictionaryOfStringAndListOfString from a dict
single_of_dictionary_of_string_and_list_of_string_from_dict = SingleOfDictionaryOfStringAndListOfString.from_dict(single_of_dictionary_of_string_and_list_of_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


