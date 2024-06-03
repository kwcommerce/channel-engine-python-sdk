# MerchantOrderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier used by ChannelEngine. This identifier does  not have to be saved. It should only be used in a call to acknowledge the order. | [optional] 
**channel_name** | **str** | The name of the channel for this specific environment/account. | [optional] 
**channel_id** | **int** | The unique ID of the channel for this specific environment/account. | [optional] 
**global_channel_name** | **str** | The name of the channel across all of ChannelEngine. | [optional] 
**global_channel_id** | **int** | The unique ID of the channel across all of ChannelEngine. | [optional] 
**channel_order_support** | [**OrderSupport**](OrderSupport.md) |  | [optional] 
**channel_order_no** | **str** | The order reference used by the channel.  This number is not guaranteed to be unique accross all orders,  because different channels can use the same order number format. | [optional] 
**commercial_order_no** | **str** | The order reference used by the channel for commercial purposes (e.g. on the invoice). Can be different from the ChannelOrderNo.  For example when the internal unique order reference is a unique id or guid, while the commercial order reference is (usually) a human readable reference that can be reused or used for multiple sellers by the channel. | [optional] 
**merchant_order_no** | **str** | The unique order reference used by the Merchant | [optional] 
**status** | [**OrderStatusView**](OrderStatusView.md) |  | [optional] 
**is_business_order** | **bool** | Indicating whether the order is a business order. | [optional] 
**acknowledged_date** | **datetime** | The date the order was acknowledged in ChannelEngine. | [optional] 
**created_at** | **datetime** | The date the order was created in ChannelEngine. | [optional] 
**updated_at** | **datetime** | The date the order was last updated in ChannelEngine. | [optional] 
**merchant_comment** | **str** | The optional comment a merchant can add to an order. | [optional] 
**billing_address** | [**MerchantAddressResponse**](MerchantAddressResponse.md) |  | [optional] 
**shipping_address** | [**MerchantAddressResponse**](MerchantAddressResponse.md) |  | [optional] 
**sub_total_incl_vat** | **float** | The total value of the order lines including VAT  (in the shop&#39;s base currency calculated using the exchange rate at the time of ordering). | [optional] 
**sub_total_vat** | **float** | The total amount of VAT charged over the order lines  (in the shop&#39;s base currency calculated using the exchange rate at the time of ordering). | [optional] 
**shipping_costs_vat** | **float** | The total amount of VAT charged over the shipping fee  (in the shop&#39;s base currency calculated using the exchange rate at the time of ordering). | [optional] 
**total_incl_vat** | **float** | The total value of the order including VAT  (in the shop&#39;s base currency calculated using the exchange rate at the time of ordering). | [optional] 
**total_vat** | **float** | The total amount of VAT charged over the total value of te order  (in the shop&#39;s base currency calculated using the exchange rate at the time of ordering). | [optional] 
**original_sub_total_incl_vat** | **float** | The total value of the order lines including VAT  (in the currency in which the order was paid for, see CurrencyCode). | [optional] 
**original_sub_total_vat** | **float** | The total amount of VAT charged over the order lines  (in the currency in which the order was paid for, see CurrencyCode). | [optional] 
**original_shipping_costs_incl_vat** | **float** | The shipping fee including VAT  (in the currency in which the order was paid for, see CurrencyCode). | [optional] 
**original_shipping_costs_vat** | **float** | The total amount of VAT charged over the shipping fee  (in the currency in which the order was paid for, see CurrencyCode). | [optional] 
**original_total_incl_vat** | **float** | The total value of the order including VAT  (in the currency in which the order was paid for, see CurrencyCode). | [optional] 
**original_total_vat** | **float** | The total amount of VAT charged over the total value of te order  (in the currency in which the order was paid for, see CurrencyCode). | [optional] 
**sub_total_excl_vat** | **float** |  | [optional] 
**total_excl_vat** | **float** |  | [optional] 
**shipping_costs_excl_vat** | **float** |  | [optional] 
**original_sub_total_excl_vat** | **float** |  | [optional] 
**original_shipping_costs_excl_vat** | **float** |  | [optional] 
**original_total_excl_vat** | **float** |  | [optional] 
**lines** | [**List[MerchantOrderLineResponse]**](MerchantOrderLineResponse.md) |  | [optional] 
**shipping_costs_incl_vat** | **float** |  | [optional] 
**phone** | **str** | The customer&#39;s telephone number. | [optional] 
**email** | **str** | The customer&#39;s email. | 
**language_code** | **str** | The language of the order. Has to be a 2-letter ISO language code. | [optional] 
**company_registration_no** | **str** | Optional. A company&#39;s chamber of commerce number. | [optional] 
**vat_no** | **str** | Optional. A company&#39;s VAT number. | [optional] 
**payment_method** | **str** | The payment method used on the order. | [optional] 
**payment_reference_no** | **str** | Reference or transaction id for the payment | [optional] 
**currency_code** | **str** | The currency code for the amounts of the order. | 
**order_date** | **datetime** | The date the order was created at the channel. | 
**channel_customer_no** | **str** | The unique customer reference used by the channel. | [optional] 
**extra_data** | **Dict[str, Optional[str]]** | Extra data on the order. | [optional] 

## Example

```python
from openapi_client.models.merchant_order_response import MerchantOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantOrderResponse from a JSON string
merchant_order_response_instance = MerchantOrderResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantOrderResponse.to_json())

# convert the object into a dict
merchant_order_response_dict = merchant_order_response_instance.to_dict()
# create an instance of MerchantOrderResponse from a dict
merchant_order_response_from_dict = MerchantOrderResponse.from_dict(merchant_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


