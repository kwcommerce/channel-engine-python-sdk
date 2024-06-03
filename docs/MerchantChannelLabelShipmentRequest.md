# MerchantChannelLabelShipmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimensions** | [**MerchantShipmentPackageDimensionsRequest**](MerchantShipmentPackageDimensionsRequest.md) |  | 
**weight** | [**MerchantShipmentPackageWeightRequest**](MerchantShipmentPackageWeightRequest.md) |  | 
**channel_method_code** | **str** |  | 
**merchant_shipment_no** | **str** | The unique shipment reference used by the Merchant. | 
**merchant_order_no** | **str** | The unique order reference used by the Merchant. | 
**shipped_from_country_code** | **str** | The code of the country from where the package is being shipped. | [optional] 
**shipped_from_stock_location_id** | **int** |  | [optional] 
**lines** | [**List[MerchantShipmentLineRequest]**](MerchantShipmentLineRequest.md) |  | 

## Example

```python
from openapi_client.models.merchant_channel_label_shipment_request import MerchantChannelLabelShipmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantChannelLabelShipmentRequest from a JSON string
merchant_channel_label_shipment_request_instance = MerchantChannelLabelShipmentRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantChannelLabelShipmentRequest.to_json())

# convert the object into a dict
merchant_channel_label_shipment_request_dict = merchant_channel_label_shipment_request_instance.to_dict()
# create an instance of MerchantChannelLabelShipmentRequest from a dict
merchant_channel_label_shipment_request_from_dict = MerchantChannelLabelShipmentRequest.from_dict(merchant_channel_label_shipment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


