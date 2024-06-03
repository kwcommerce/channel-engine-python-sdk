# IImportInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_containers** | **str** |  | [optional] 
**international_commercial_terms** | **str** |  | [optional] 
**method_of_payment** | **str** |  | [optional] 
**port_of_delivery** | **str** |  | [optional] 
**shipping_instructions** | **str** |  | [optional] 
**deal_code** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.i_import_information import IImportInformation

# TODO update the JSON string below
json = "{}"
# create an instance of IImportInformation from a JSON string
i_import_information_instance = IImportInformation.from_json(json)
# print the JSON string representation of the object
print(IImportInformation.to_json())

# convert the object into a dict
i_import_information_dict = i_import_information_instance.to_dict()
# create an instance of IImportInformation from a dict
i_import_information_from_dict = IImportInformation.from_dict(i_import_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


