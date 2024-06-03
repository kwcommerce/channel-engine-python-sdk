# SettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment** | [**ShipmentSettingsResponse**](ShipmentSettingsResponse.md) |  | [optional] 
**advanced** | [**AdvanceSettingsResponse**](AdvanceSettingsResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.settings_response import SettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsResponse from a JSON string
settings_response_instance = SettingsResponse.from_json(json)
# print the JSON string representation of the object
print(SettingsResponse.to_json())

# convert the object into a dict
settings_response_dict = settings_response_instance.to_dict()
# create an instance of SettingsResponse from a dict
settings_response_from_dict = SettingsResponse.from_dict(settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


