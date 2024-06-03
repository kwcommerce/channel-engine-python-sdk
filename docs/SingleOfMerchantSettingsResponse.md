# SingleOfMerchantSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**MerchantSettingsResponse**](MerchantSettingsResponse.md) |  | [optional] 
**status_code** | **int** |  | [optional] 
**request_id** | **str** |  | [optional] 
**log_id** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**exception_type** | **str** |  | [optional] 
**validation_errors** | **Dict[str, Optional[List[str]]]** |  | [optional] 

## Example

```python
from openapi_client.models.single_of_merchant_settings_response import SingleOfMerchantSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleOfMerchantSettingsResponse from a JSON string
single_of_merchant_settings_response_instance = SingleOfMerchantSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(SingleOfMerchantSettingsResponse.to_json())

# convert the object into a dict
single_of_merchant_settings_response_dict = single_of_merchant_settings_response_instance.to_dict()
# create an instance of SingleOfMerchantSettingsResponse from a dict
single_of_merchant_settings_response_from_dict = SingleOfMerchantSettingsResponse.from_dict(single_of_merchant_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


