# MerchantVendorParty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**address_line3** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**county** | **str** |  | [optional] 
**district** | **str** |  | [optional] 
**state_or_region** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**tax_registration_type** | [**ModulesTaxRegistrationType**](ModulesTaxRegistrationType.md) |  | [optional] 
**tax_registration_no** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.merchant_vendor_party import MerchantVendorParty

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantVendorParty from a JSON string
merchant_vendor_party_instance = MerchantVendorParty.from_json(json)
# print the JSON string representation of the object
print(MerchantVendorParty.to_json())

# convert the object into a dict
merchant_vendor_party_dict = merchant_vendor_party_instance.to_dict()
# create an instance of MerchantVendorParty from a dict
merchant_vendor_party_from_dict = MerchantVendorParty.from_dict(merchant_vendor_party_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


