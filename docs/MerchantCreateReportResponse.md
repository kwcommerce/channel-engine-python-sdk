# MerchantCreateReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_id** | **str** |  | [optional] 
**status** | [**ReportStatus**](ReportStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_create_report_response import MerchantCreateReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantCreateReportResponse from a JSON string
merchant_create_report_response_instance = MerchantCreateReportResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantCreateReportResponse.to_json())

# convert the object into a dict
merchant_create_report_response_dict = merchant_create_report_response_instance.to_dict()
# create an instance of MerchantCreateReportResponse from a dict
merchant_create_report_response_from_dict = MerchantCreateReportResponse.from_dict(merchant_create_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


