# MerchantShipmentTrackingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | Shipment method (carrier). | 
**track_trace_no** | **str** | The unique shipping reference used by the Shipping carrier (track &amp; trace number). | 
**return_track_trace_no** | **str** | The unique return shipping reference that may be used by the Shipping carrier (track &amp; trace number) if the shipment is returned. | [optional] 
**track_trace_url** | **str** | A link to a page of the carrier where the customer can track the shipping of her package. | [optional] 
**shipped_from_country_code** | **str** | The code of the country from where the package is being shipped. | [optional] 

## Example

```python
from openapi_client.models.merchant_shipment_tracking_request import MerchantShipmentTrackingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantShipmentTrackingRequest from a JSON string
merchant_shipment_tracking_request_instance = MerchantShipmentTrackingRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantShipmentTrackingRequest.to_json())

# convert the object into a dict
merchant_shipment_tracking_request_dict = merchant_shipment_tracking_request_instance.to_dict()
# create an instance of MerchantShipmentTrackingRequest from a dict
merchant_shipment_tracking_request_from_dict = MerchantShipmentTrackingRequest.from_dict(merchant_shipment_tracking_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


