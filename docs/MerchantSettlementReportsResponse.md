# MerchantSettlementReportsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_id** | **int** |  | [optional] 
**channel_settlement_no** | **str** |  | [optional] 
**channel_id** | **int** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**transactions_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.merchant_settlement_reports_response import MerchantSettlementReportsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantSettlementReportsResponse from a JSON string
merchant_settlement_reports_response_instance = MerchantSettlementReportsResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantSettlementReportsResponse.to_json())

# convert the object into a dict
merchant_settlement_reports_response_dict = merchant_settlement_reports_response_instance.to_dict()
# create an instance of MerchantSettlementReportsResponse from a dict
merchant_settlement_reports_response_from_dict = MerchantSettlementReportsResponse.from_dict(merchant_settlement_reports_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


