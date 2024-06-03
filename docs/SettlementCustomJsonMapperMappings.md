# SettlementCustomJsonMapperMappings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_id** | [**SettlementCustomJsonMapperMapping**](SettlementCustomJsonMapperMapping.md) |  | [optional] 
**channel_settlement_no** | [**SettlementCustomJsonMapperMapping**](SettlementCustomJsonMapperMapping.md) |  | [optional] 
**channel_id** | [**SettlementCustomJsonMapperMapping**](SettlementCustomJsonMapperMapping.md) |  | [optional] 
**channel_order_no** | [**SettlementCustomJsonMapperMapping**](SettlementCustomJsonMapperMapping.md) |  | [optional] 
**order_id** | [**SettlementCustomJsonMapperMapping**](SettlementCustomJsonMapperMapping.md) |  | [optional] 
**merchant_order_no** | [**SettlementCustomJsonMapperMapping**](SettlementCustomJsonMapperMapping.md) |  | [optional] 
**total_amount** | [**SettlementCustomJsonMapperMapping**](SettlementCustomJsonMapperMapping.md) |  | [optional] 
**currency_code** | [**SettlementCustomJsonMapperMapping**](SettlementCustomJsonMapperMapping.md) |  | [optional] 
**order_proceeds_amount** | [**SettlementCustomJsonMapperMapping**](SettlementCustomJsonMapperMapping.md) |  | [optional] 
**commission_amount** | [**SettlementCustomJsonMapperMapping**](SettlementCustomJsonMapperMapping.md) |  | [optional] 
**withheld_vat_amount** | [**SettlementCustomJsonMapperMapping**](SettlementCustomJsonMapperMapping.md) |  | [optional] 
**fee_correction_amount** | [**SettlementCustomJsonMapperMapping**](SettlementCustomJsonMapperMapping.md) |  | [optional] 
**marketplace_fulfillment_fee_amount** | [**SettlementCustomJsonMapperMapping**](SettlementCustomJsonMapperMapping.md) |  | [optional] 
**marketplace_inventory_fee_amount** | [**SettlementCustomJsonMapperMapping**](SettlementCustomJsonMapperMapping.md) |  | [optional] 
**subscription_fee_amount** | [**SettlementCustomJsonMapperMapping**](SettlementCustomJsonMapperMapping.md) |  | [optional] 
**additional_channel_costs_amount** | [**SettlementCustomJsonMapperMapping**](SettlementCustomJsonMapperMapping.md) |  | [optional] 
**channel_reference** | [**SettlementCustomJsonMapperMapping**](SettlementCustomJsonMapperMapping.md) |  | [optional] 
**total_fee_amount** | [**SettlementCustomJsonMapperMapping**](SettlementCustomJsonMapperMapping.md) |  | [optional] 

## Example

```python
from openapi_client.models.settlement_custom_json_mapper_mappings import SettlementCustomJsonMapperMappings

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementCustomJsonMapperMappings from a JSON string
settlement_custom_json_mapper_mappings_instance = SettlementCustomJsonMapperMappings.from_json(json)
# print the JSON string representation of the object
print(SettlementCustomJsonMapperMappings.to_json())

# convert the object into a dict
settlement_custom_json_mapper_mappings_dict = settlement_custom_json_mapper_mappings_instance.to_dict()
# create an instance of SettlementCustomJsonMapperMappings from a dict
settlement_custom_json_mapper_mappings_from_dict = SettlementCustomJsonMapperMappings.from_dict(settlement_custom_json_mapper_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


