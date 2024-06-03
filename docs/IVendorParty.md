# IVendorParty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**party_id** | **str** |  | [optional] 
**tax_registration_type** | [**ModulesTaxRegistrationType**](ModulesTaxRegistrationType.md) |  | [optional] 
**tax_registration_no** | **str** |  | [optional] 
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

## Example

```python
from openapi_client.models.i_vendor_party import IVendorParty

# TODO update the JSON string below
json = "{}"
# create an instance of IVendorParty from a JSON string
i_vendor_party_instance = IVendorParty.from_json(json)
# print the JSON string representation of the object
print(IVendorParty.to_json())

# convert the object into a dict
i_vendor_party_dict = i_vendor_party_instance.to_dict()
# create an instance of IVendorParty from a dict
i_vendor_party_from_dict = IVendorParty.from_dict(i_vendor_party_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


