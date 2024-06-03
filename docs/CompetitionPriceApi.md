# openapi_client.CompetitionPriceApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**competition_prices_get_buy_box_prices**](CompetitionPriceApi.md#competition_prices_get_buy_box_prices) | **GET** /v2/competitionprices/buyboxprices | Gets the price from the buy box winner


# **competition_prices_get_buy_box_prices**
> CollectionOfMerchantProductWithBuyBoxPrice competition_prices_get_buy_box_prices(channel_id=channel_id, gtin_list=gtin_list, sku_list=sku_list, page=page)

Gets the price from the buy box winner

Gets the current price of the buy box winner per product for a marketplace.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.collection_of_merchant_product_with_buy_box_price import CollectionOfMerchantProductWithBuyBoxPrice
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.channelengine.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo.channelengine.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CompetitionPriceApi(api_client)
    channel_id = 56 # int | The id of the channel (optional)
    gtin_list = ['gtin_list_example'] # List[str] | Search products by submitting a list of GTIN's. (optional)<br />Max. 2000. (optional)
    sku_list = ['sku_list_example'] # List[str] | Search products by submitting a list of Sku's. (optional)<br />Max. 2000. If GtinList is already set, this one is ignored. (optional)
    page = 56 # int | The page to filter on. Starts at 1. (optional)

    try:
        # Gets the price from the buy box winner
        api_response = api_instance.competition_prices_get_buy_box_prices(channel_id=channel_id, gtin_list=gtin_list, sku_list=sku_list, page=page)
        print("The response of CompetitionPriceApi->competition_prices_get_buy_box_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompetitionPriceApi->competition_prices_get_buy_box_prices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **int**| The id of the channel | [optional] 
 **gtin_list** | [**List[str]**](str.md)| Search products by submitting a list of GTIN&#39;s. (optional)&lt;br /&gt;Max. 2000. | [optional] 
 **sku_list** | [**List[str]**](str.md)| Search products by submitting a list of Sku&#39;s. (optional)&lt;br /&gt;Max. 2000. If GtinList is already set, this one is ignored. | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantProductWithBuyBoxPrice**](CollectionOfMerchantProductWithBuyBoxPrice.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

