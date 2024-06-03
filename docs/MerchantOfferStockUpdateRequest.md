# MerchantOfferStockUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_product_no** | **str** | The unique product reference used by the Merchant (sku). | 
**stock_locations** | [**List[MerchantStockLocationUpdateRequest]**](MerchantStockLocationUpdateRequest.md) | Stock locations data | 

## Example

```python
from openapi_client.models.merchant_offer_stock_update_request import MerchantOfferStockUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantOfferStockUpdateRequest from a JSON string
merchant_offer_stock_update_request_instance = MerchantOfferStockUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantOfferStockUpdateRequest.to_json())

# convert the object into a dict
merchant_offer_stock_update_request_dict = merchant_offer_stock_update_request_instance.to_dict()
# create an instance of MerchantOfferStockUpdateRequest from a dict
merchant_offer_stock_update_request_from_dict = MerchantOfferStockUpdateRequest.from_dict(merchant_offer_stock_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


