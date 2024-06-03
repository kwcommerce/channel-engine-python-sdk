# MerchantCreateSettlementsReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_ids** | **List[int]** |  | 
**type** | [**ReportType**](ReportType.md) |  | 
**custom_json_mapper** | [**SettlementCustomJsonMapper**](SettlementCustomJsonMapper.md) |  | [optional] 
**channel_references_by_channel_id** | **Dict[str, Optional[str]]** |  | [optional] 

## Example

```python
from openapi_client.models.merchant_create_settlements_report_request import MerchantCreateSettlementsReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantCreateSettlementsReportRequest from a JSON string
merchant_create_settlements_report_request_instance = MerchantCreateSettlementsReportRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantCreateSettlementsReportRequest.to_json())

# convert the object into a dict
merchant_create_settlements_report_request_dict = merchant_create_settlements_report_request_instance.to_dict()
# create an instance of MerchantCreateSettlementsReportRequest from a dict
merchant_create_settlements_report_request_from_dict = MerchantCreateSettlementsReportRequest.from_dict(merchant_create_settlements_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


