# openapi_client.ProductBundleApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_bundle_get_by_filter**](ProductBundleApi.md#product_bundle_get_by_filter) | **GET** /v2/productbundles | Gets product bundles


# **product_bundle_get_by_filter**
> CollectionOfMerchantProductBundleResponse product_bundle_get_by_filter(search=search, ean_list=ean_list, merchant_product_no_list=merchant_product_no_list, page=page)

Gets product bundles

Gets the product bundle details.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.collection_of_merchant_product_bundle_response import CollectionOfMerchantProductBundleResponse
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
    api_instance = openapi_client.ProductBundleApi(api_client)
    search = 'search_example' # str | Search product(s) by Name, MerchantProductNo, Ean or Brand<br />This search is applied to the result after applying the other filters. (optional)
    ean_list = ['ean_list_example'] # List[str] | Search products by submitting a list of EAN's. (optional)
    merchant_product_no_list = ['merchant_product_no_list_example'] # List[str] | Search products by submitting a list of MerchantProductNo's. (optional)
    page = 56 # int | The page to filter on. Starts at 1. (optional)

    try:
        # Gets product bundles
        api_response = api_instance.product_bundle_get_by_filter(search=search, ean_list=ean_list, merchant_product_no_list=merchant_product_no_list, page=page)
        print("The response of ProductBundleApi->product_bundle_get_by_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductBundleApi->product_bundle_get_by_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search product(s) by Name, MerchantProductNo, Ean or Brand&lt;br /&gt;This search is applied to the result after applying the other filters. | [optional] 
 **ean_list** | [**List[str]**](str.md)| Search products by submitting a list of EAN&#39;s. | [optional] 
 **merchant_product_no_list** | [**List[str]**](str.md)| Search products by submitting a list of MerchantProductNo&#39;s. | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantProductBundleResponse**](CollectionOfMerchantProductBundleResponse.md)

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

