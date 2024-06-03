# MerchantSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**default_culture_code** | **str** |  | [optional] 
**settings** | [**SettingsResponse**](SettingsResponse.md) |  | [optional] 
**vat** | [**List[VatSettingsResponse]**](VatSettingsResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_settings_response import MerchantSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantSettingsResponse from a JSON string
merchant_settings_response_instance = MerchantSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantSettingsResponse.to_json())

# convert the object into a dict
merchant_settings_response_dict = merchant_settings_response_instance.to_dict()
# create an instance of MerchantSettingsResponse from a dict
merchant_settings_response_from_dict = MerchantSettingsResponse.from_dict(merchant_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


