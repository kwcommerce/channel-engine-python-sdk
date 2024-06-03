# AdvanceSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manage_stock** | **bool** |  | [optional] 
**disable_address_validation** | **bool** |  | [optional] 
**skip_house_number_validation** | **bool** |  | [optional] 
**skip_house_number_validation_for_country_codes** | **List[str]** |  | [optional] 
**set_orders_to_closed_on_import** | **bool** |  | [optional] 
**disable_stock_reservation** | **bool** |  | [optional] 
**disable_auto_order_cancellation** | **bool** |  | [optional] 
**automatically_set_phone_number_if_empty** | **str** |  | [optional] 
**default_vat_rate** | **float** |  | [optional] 
**order_too_long_on_new_hours_offset** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.advance_settings_response import AdvanceSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AdvanceSettingsResponse from a JSON string
advance_settings_response_instance = AdvanceSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(AdvanceSettingsResponse.to_json())

# convert the object into a dict
advance_settings_response_dict = advance_settings_response_instance.to_dict()
# create an instance of AdvanceSettingsResponse from a dict
advance_settings_response_from_dict = AdvanceSettingsResponse.from_dict(advance_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


