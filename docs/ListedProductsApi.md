# openapi_client.ListedProductsApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listed_product_get_by_filter**](ListedProductsApi.md#listed_product_get_by_filter) | **GET** /v2/channels/{channelId}/products | Gets products listed by channel


# **listed_product_get_by_filter**
> CollectionOfChannelListedProductResponse listed_product_get_by_filter(channel_id, merchant_product_nos=merchant_product_nos, page=page)

Gets products listed by channel

Gets the products listed per channel based on the **Channel ID**.<br /> <br />**NB:** not all marketplaces provide adequate options to retrieve the status of a product as seen on the marketplace.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.collection_of_channel_listed_product_response import CollectionOfChannelListedProductResponse
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
    api_instance = openapi_client.ListedProductsApi(api_client)
    channel_id = 56 # int | The id of a channel
    merchant_product_nos = ['merchant_product_nos_example'] # List[str] | The unique product references used by the Merchant (SKUs) (optional)
    page = 56 # int | The page to filter on. Starts at 1. (optional)

    try:
        # Gets products listed by channel
        api_response = api_instance.listed_product_get_by_filter(channel_id, merchant_product_nos=merchant_product_nos, page=page)
        print("The response of ListedProductsApi->listed_product_get_by_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListedProductsApi->listed_product_get_by_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **int**| The id of a channel | 
 **merchant_product_nos** | [**List[str]**](str.md)| The unique product references used by the Merchant (SKUs) | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfChannelListedProductResponse**](CollectionOfChannelListedProductResponse.md)

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

