# VatSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_iso** | **str** |  | [optional] 
**no** | **str** |  | [optional] 
**standard_rate** | **float** |  | [optional] 
**reduced_rate** | **float** |  | [optional] 
**super_reduced_rate** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.vat_settings_response import VatSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VatSettingsResponse from a JSON string
vat_settings_response_instance = VatSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(VatSettingsResponse.to_json())

# convert the object into a dict
vat_settings_response_dict = vat_settings_response_instance.to_dict()
# create an instance of VatSettingsResponse from a dict
vat_settings_response_from_dict = VatSettingsResponse.from_dict(vat_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


