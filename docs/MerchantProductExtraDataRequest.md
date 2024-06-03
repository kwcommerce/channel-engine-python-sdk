# MerchantProductExtraDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_product_no** | **str** |  | 
**operations** | [**List[ProductExtraDataRequest]**](ProductExtraDataRequest.md) |  | 

## Example

```python
from openapi_client.models.merchant_product_extra_data_request import MerchantProductExtraDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantProductExtraDataRequest from a JSON string
merchant_product_extra_data_request_instance = MerchantProductExtraDataRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantProductExtraDataRequest.to_json())

# convert the object into a dict
merchant_product_extra_data_request_dict = merchant_product_extra_data_request_instance.to_dict()
# create an instance of MerchantProductExtraDataRequest from a dict
merchant_product_extra_data_request_from_dict = MerchantProductExtraDataRequest.from_dict(merchant_product_extra_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


