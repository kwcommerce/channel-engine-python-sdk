# MerchantShipmentPackageDimensionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **float** |  | [optional] 
**width** | **float** |  | [optional] 
**length** | **float** |  | [optional] 
**unit** | [**PackageDimensionsUnit**](PackageDimensionsUnit.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_shipment_package_dimensions_request import MerchantShipmentPackageDimensionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantShipmentPackageDimensionsRequest from a JSON string
merchant_shipment_package_dimensions_request_instance = MerchantShipmentPackageDimensionsRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantShipmentPackageDimensionsRequest.to_json())

# convert the object into a dict
merchant_shipment_package_dimensions_request_dict = merchant_shipment_package_dimensions_request_instance.to_dict()
# create an instance of MerchantShipmentPackageDimensionsRequest from a dict
merchant_shipment_package_dimensions_request_from_dict = MerchantShipmentPackageDimensionsRequest.from_dict(merchant_shipment_package_dimensions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


