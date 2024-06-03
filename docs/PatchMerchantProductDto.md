# PatchMerchantProductDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties_to_update** | **List[str]** | Fields to update | [optional] 
**merchant_product_request_models** | [**List[MerchantProductRequest]**](MerchantProductRequest.md) | Products to be updated | [optional] 

## Example

```python
from openapi_client.models.patch_merchant_product_dto import PatchMerchantProductDto

# TODO update the JSON string below
json = "{}"
# create an instance of PatchMerchantProductDto from a JSON string
patch_merchant_product_dto_instance = PatchMerchantProductDto.from_json(json)
# print the JSON string representation of the object
print(PatchMerchantProductDto.to_json())

# convert the object into a dict
patch_merchant_product_dto_dict = patch_merchant_product_dto_instance.to_dict()
# create an instance of PatchMerchantProductDto from a dict
patch_merchant_product_dto_from_dict = PatchMerchantProductDto.from_dict(patch_merchant_product_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


