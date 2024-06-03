# MerchantShipmentPackageWeightRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | [optional] 
**unit** | [**PackageWeightUnit**](PackageWeightUnit.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_shipment_package_weight_request import MerchantShipmentPackageWeightRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantShipmentPackageWeightRequest from a JSON string
merchant_shipment_package_weight_request_instance = MerchantShipmentPackageWeightRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantShipmentPackageWeightRequest.to_json())

# convert the object into a dict
merchant_shipment_package_weight_request_dict = merchant_shipment_package_weight_request_instance.to_dict()
# create an instance of MerchantShipmentPackageWeightRequest from a dict
merchant_shipment_package_weight_request_from_dict = MerchantShipmentPackageWeightRequest.from_dict(merchant_shipment_package_weight_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


