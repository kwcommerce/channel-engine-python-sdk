# openapi_client.OfferApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offer_get_stock**](OfferApi.md#offer_get_stock) | **GET** /v2/offer/stock | Gets product stock across all warehouses
[**offer_stock_price_update**](OfferApi.md#offer_stock_price_update) | **PUT** /v2/offer | Updates stock and price
[**offer_stock_update**](OfferApi.md#offer_stock_update) | **PUT** /v2/offer/stock | Updates stock


# **offer_get_stock**
> CollectionOfMerchantOfferGetStockResponse offer_get_stock(stock_location_ids, skus=skus, page_index=page_index, page_size=page_size)

Gets product stock across all warehouses

Gets the stock available in the warehouses. The warehouses must be set up as stock locations on ChannelEngine.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.collection_of_merchant_offer_get_stock_response import CollectionOfMerchantOfferGetStockResponse
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
    api_instance = openapi_client.OfferApi(api_client)
    stock_location_ids = [56] # List[int] | The ChannelEngine id of the stock location(s).
    skus = ['skus_example'] # List[str] | List of your products' sku's. (optional)
    page_index = 56 # int | A page index to get the items (starts from 0) (optional)
    page_size = 56 # int | Number of items to return (default 100) (optional)

    try:
        # Gets product stock across all warehouses
        api_response = api_instance.offer_get_stock(stock_location_ids, skus=skus, page_index=page_index, page_size=page_size)
        print("The response of OfferApi->offer_get_stock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->offer_get_stock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_location_ids** | [**List[int]**](int.md)| The ChannelEngine id of the stock location(s). | 
 **skus** | [**List[str]**](str.md)| List of your products&#39; sku&#39;s. | [optional] 
 **page_index** | **int**| A page index to get the items (starts from 0) | [optional] 
 **page_size** | **int**| Number of items to return (default 100) | [optional] 

### Return type

[**CollectionOfMerchantOfferGetStockResponse**](CollectionOfMerchantOfferGetStockResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **offer_stock_price_update**
> SingleOfDictionaryOfStringAndListOfString offer_stock_price_update(merchant_stock_price_update_request)

Updates stock and price

Updates product stock and price.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.merchant_stock_price_update_request import MerchantStockPriceUpdateRequest
from openapi_client.models.single_of_dictionary_of_string_and_list_of_string import SingleOfDictionaryOfStringAndListOfString
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
    api_instance = openapi_client.OfferApi(api_client)
    merchant_stock_price_update_request = [openapi_client.MerchantStockPriceUpdateRequest()] # List[MerchantStockPriceUpdateRequest] | References to the products that should be updated, and the new values<br />for the stock or price fields. It is possible to supply only one of the two fields<br />or both.

    try:
        # Updates stock and price
        api_response = api_instance.offer_stock_price_update(merchant_stock_price_update_request)
        print("The response of OfferApi->offer_stock_price_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->offer_stock_price_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_stock_price_update_request** | [**List[MerchantStockPriceUpdateRequest]**](MerchantStockPriceUpdateRequest.md)| References to the products that should be updated, and the new values&lt;br /&gt;for the stock or price fields. It is possible to supply only one of the two fields&lt;br /&gt;or both. | 

### Return type

[**SingleOfDictionaryOfStringAndListOfString**](SingleOfDictionaryOfStringAndListOfString.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | **Message** can be **\&quot;Updates processed without warnings\&quot;** or in case of validations **\&quot;Updates processed, see &#39;Content&#39; for warnings\&quot;** |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **offer_stock_update**
> SingleOfDictionaryOfStringAndListOfString offer_stock_update(merchant_offer_stock_update_request)

Updates stock

Updates product stock.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.merchant_offer_stock_update_request import MerchantOfferStockUpdateRequest
from openapi_client.models.single_of_dictionary_of_string_and_list_of_string import SingleOfDictionaryOfStringAndListOfString
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
    api_instance = openapi_client.OfferApi(api_client)
    merchant_offer_stock_update_request = [openapi_client.MerchantOfferStockUpdateRequest()] # List[MerchantOfferStockUpdateRequest] | References to the new values for the stock fields.

    try:
        # Updates stock
        api_response = api_instance.offer_stock_update(merchant_offer_stock_update_request)
        print("The response of OfferApi->offer_stock_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->offer_stock_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_offer_stock_update_request** | [**List[MerchantOfferStockUpdateRequest]**](MerchantOfferStockUpdateRequest.md)| References to the new values for the stock fields. | 

### Return type

[**SingleOfDictionaryOfStringAndListOfString**](SingleOfDictionaryOfStringAndListOfString.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | **Message** can be **\&quot;Updates processed without warnings\&quot;** or in case of validations **\&quot;Updates processed, see &#39;Content&#39; for warnings\&quot;** |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

