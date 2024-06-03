# openapi_client.FulfillmentStockApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fulfillment_stock_get_fulfillement_stock_with_stock_locations**](FulfillmentStockApi.md#fulfillment_stock_get_fulfillement_stock_with_stock_locations) | **GET** /v2/fulfillmentstock | Gets product stock across all warehouses with stock locations


# **fulfillment_stock_get_fulfillement_stock_with_stock_locations**
> CollectionOfMerchantFulfillmentStockGetStockLocationsRequest fulfillment_stock_get_fulfillement_stock_with_stock_locations(merchant_product_nos=merchant_product_nos, page_index=page_index, page_size=page_size)

Gets product stock across all warehouses with stock locations

Gets the stocks. The warehouses must be set up as stock locations on ChannelEngine.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.collection_of_merchant_fulfillment_stock_get_stock_locations_request import CollectionOfMerchantFulfillmentStockGetStockLocationsRequest
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
    api_instance = openapi_client.FulfillmentStockApi(api_client)
    merchant_product_nos = ['merchant_product_nos_example'] # List[str] | List of your products' MerchantProductNo's. (optional)
    page_index = 56 # int | A page index to get the items (starts from 0) (optional)
    page_size = 56 # int | Number of items to return (default 100) (optional)

    try:
        # Gets product stock across all warehouses with stock locations
        api_response = api_instance.fulfillment_stock_get_fulfillement_stock_with_stock_locations(merchant_product_nos=merchant_product_nos, page_index=page_index, page_size=page_size)
        print("The response of FulfillmentStockApi->fulfillment_stock_get_fulfillement_stock_with_stock_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FulfillmentStockApi->fulfillment_stock_get_fulfillement_stock_with_stock_locations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_product_nos** | [**List[str]**](str.md)| List of your products&#39; MerchantProductNo&#39;s. | [optional] 
 **page_index** | **int**| A page index to get the items (starts from 0) | [optional] 
 **page_size** | **int**| Number of items to return (default 100) | [optional] 

### Return type

[**CollectionOfMerchantFulfillmentStockGetStockLocationsRequest**](CollectionOfMerchantFulfillmentStockGetStockLocationsRequest.md)

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

