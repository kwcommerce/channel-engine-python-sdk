# MerchantShipmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_shipment_no** | **str** | The unique shipment reference used by the Merchant. | 
**merchant_order_no** | **str** | The unique order reference used by the Merchant. | [optional] 
**channel_shipment_no** | **str** | The unique shipment reference used by the Channel. | [optional] 
**channel_order_no** | **str** | The unique order reference used by the Channel. | [optional] 
**channel_id** | **int** | The unique ID of the channel for this specific environment/account. | [optional] 
**global_channel_id** | **int** | The unique ID of the channel across all of ChannelEngine. | [optional] 
**lines** | [**List[MerchantShipmentLineResponse]**](MerchantShipmentLineResponse.md) |  | [optional] 
**created_at** | **datetime** | The date at which the shipment was created in ChannelEngine. | [optional] 
**updated_at** | **datetime** | The date at which the shipment was last modified in ChannelEngine. | [optional] 
**extra_data** | **Dict[str, Optional[str]]** | Extra data on the order. Each item must have an unqiue key | [optional] 
**track_trace_no** | **str** | The unique shipping reference used by the Shipping carrier (track&amp;trace number). | [optional] 
**track_trace_url** | **str** | A link to a page of the carrier where the customer can track the shipping of her package. | [optional] 
**return_track_trace_no** | **str** | The unique return shipping reference that may be used by the Shipping carrier (track &amp; trace number) if the shipment is returned. | [optional] 
**method** | **str** | Shipment method: the carrier used for shipping the package. E.g. DHL, postNL. | [optional] 
**shipped_from_country_code** | **str** | The code of the country from where the package is being shipped. | [optional] 
**shipped_from_stock_location_id** | **int** | The id of the stock location where you ship the package from | [optional] 
**shipment_date** | **datetime** | The date at which the shipment was originally created in the source system (if available). | [optional] 

## Example

```python
from openapi_client.models.merchant_shipment_response import MerchantShipmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantShipmentResponse from a JSON string
merchant_shipment_response_instance = MerchantShipmentResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantShipmentResponse.to_json())

# convert the object into a dict
merchant_shipment_response_dict = merchant_shipment_response_instance.to_dict()
# create an instance of MerchantShipmentResponse from a dict
merchant_shipment_response_from_dict = MerchantShipmentResponse.from_dict(merchant_shipment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


