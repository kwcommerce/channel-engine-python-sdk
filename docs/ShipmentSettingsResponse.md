# ShipmentSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_tracked_shipment_method** | **str** |  | [optional] 
**default_untracked_shipment_method** | **str** |  | [optional] 
**automatically_set_shipment_method_after_minutes** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.shipment_settings_response import ShipmentSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentSettingsResponse from a JSON string
shipment_settings_response_instance = ShipmentSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(ShipmentSettingsResponse.to_json())

# convert the object into a dict
shipment_settings_response_dict = shipment_settings_response_instance.to_dict()
# create an instance of ShipmentSettingsResponse from a dict
shipment_settings_response_from_dict = ShipmentSettingsResponse.from_dict(shipment_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


