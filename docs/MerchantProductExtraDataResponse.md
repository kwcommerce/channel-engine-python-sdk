# MerchantProductExtraDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_extra_data_id** | **int** |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.merchant_product_extra_data_response import MerchantProductExtraDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantProductExtraDataResponse from a JSON string
merchant_product_extra_data_response_instance = MerchantProductExtraDataResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantProductExtraDataResponse.to_json())

# convert the object into a dict
merchant_product_extra_data_response_dict = merchant_product_extra_data_response_instance.to_dict()
# create an instance of MerchantProductExtraDataResponse from a dict
merchant_product_extra_data_response_from_dict = MerchantProductExtraDataResponse.from_dict(merchant_product_extra_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


