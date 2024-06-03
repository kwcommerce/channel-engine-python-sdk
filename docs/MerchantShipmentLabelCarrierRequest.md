# MerchantShipmentLabelCarrierRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lines** | [**List[MerchantShipmentLineRequest]**](MerchantShipmentLineRequest.md) |  | 
**dimensions** | [**MerchantShipmentPackageDimensionsRequest**](MerchantShipmentPackageDimensionsRequest.md) |  | 
**weight** | [**MerchantShipmentPackageWeightRequest**](MerchantShipmentPackageWeightRequest.md) |  | 

## Example

```python
from openapi_client.models.merchant_shipment_label_carrier_request import MerchantShipmentLabelCarrierRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantShipmentLabelCarrierRequest from a JSON string
merchant_shipment_label_carrier_request_instance = MerchantShipmentLabelCarrierRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantShipmentLabelCarrierRequest.to_json())

# convert the object into a dict
merchant_shipment_label_carrier_request_dict = merchant_shipment_label_carrier_request_instance.to_dict()
# create an instance of MerchantShipmentLabelCarrierRequest from a dict
merchant_shipment_label_carrier_request_from_dict = MerchantShipmentLabelCarrierRequest.from_dict(merchant_shipment_label_carrier_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


