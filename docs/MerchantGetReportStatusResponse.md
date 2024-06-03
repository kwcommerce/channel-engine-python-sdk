# MerchantGetReportStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ReportStatus**](ReportStatus.md) |  | [optional] 
**resource_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.merchant_get_report_status_response import MerchantGetReportStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantGetReportStatusResponse from a JSON string
merchant_get_report_status_response_instance = MerchantGetReportStatusResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantGetReportStatusResponse.to_json())

# convert the object into a dict
merchant_get_report_status_response_dict = merchant_get_report_status_response_instance.to_dict()
# create an instance of MerchantGetReportStatusResponse from a dict
merchant_get_report_status_response_from_dict = MerchantGetReportStatusResponse.from_dict(merchant_get_report_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


