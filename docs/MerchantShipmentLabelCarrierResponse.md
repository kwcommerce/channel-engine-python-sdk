# MerchantShipmentLabelCarrierResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The channel&#39;s name for the shipping label carrier | [optional] 
**code** | **str** | The channel&#39;s code for the shipping label carrier | [optional] 
**restrictions** | **str** | Optional. Any restrictions on this carriers, e.g. weight and/or dimensions | [optional] 
**price** | **float** | Optional. Price for this shipping label | [optional] 
**recommendation** | [**ChannelCarrierRecommendationApi**](ChannelCarrierRecommendationApi.md) |  | [optional] 
**collection_method** | [**ChannelCarrierCollectionMethodApi**](ChannelCarrierCollectionMethodApi.md) |  | [optional] 
**handover_date_time** | **datetime** | Optional. When to handover the package to the carrier  It is in the ISO format including the timezone offset.  E.g. 2020-10-03T18:00:00+02:00  which is 3rd Oct 2020, at 18:00 PM in Amsterdam (Summer Time aka CEST: UTC +2:00 ) | [optional] 

## Example

```python
from openapi_client.models.merchant_shipment_label_carrier_response import MerchantShipmentLabelCarrierResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantShipmentLabelCarrierResponse from a JSON string
merchant_shipment_label_carrier_response_instance = MerchantShipmentLabelCarrierResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantShipmentLabelCarrierResponse.to_json())

# convert the object into a dict
merchant_shipment_label_carrier_response_dict = merchant_shipment_label_carrier_response_instance.to_dict()
# create an instance of MerchantShipmentLabelCarrierResponse from a dict
merchant_shipment_label_carrier_response_from_dict = MerchantShipmentLabelCarrierResponse.from_dict(merchant_shipment_label_carrier_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


