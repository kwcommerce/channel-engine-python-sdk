# openapi_client.StockLocationApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stock_location_create**](StockLocationApi.md#stock_location_create) | **POST** /v2/stocklocations | Creates a stock location
[**stock_location_index**](StockLocationApi.md#stock_location_index) | **GET** /v2/stocklocations | Gets stock locations


# **stock_location_create**
> ApiResponse stock_location_create(merchant_stock_location_create_request=merchant_stock_location_create_request)

Creates a stock location

Creates a stock location on ChannelEngine.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.merchant_stock_location_create_request import MerchantStockLocationCreateRequest
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
    api_instance = openapi_client.StockLocationApi(api_client)
    merchant_stock_location_create_request = openapi_client.MerchantStockLocationCreateRequest() # MerchantStockLocationCreateRequest |  (optional)

    try:
        # Creates a stock location
        api_response = api_instance.stock_location_create(merchant_stock_location_create_request=merchant_stock_location_create_request)
        print("The response of StockLocationApi->stock_location_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockLocationApi->stock_location_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_stock_location_create_request** | [**MerchantStockLocationCreateRequest**](MerchantStockLocationCreateRequest.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_location_index**
> CollectionOfMerchantStockLocationWithCountryIsoResponse stock_location_index()

Gets stock locations

Gets the different stock locations in use. <br />**NB:** the response may include stock locations for 'marketplace fulfilment' solutions (e.g.: FBA, LVB, ZFS, etc.).<br />Use the retrieved IDs to get the stock of products in specific stock locations, such as the FBA stock.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.collection_of_merchant_stock_location_with_country_iso_response import CollectionOfMerchantStockLocationWithCountryIsoResponse
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
    api_instance = openapi_client.StockLocationApi(api_client)

    try:
        # Gets stock locations
        api_response = api_instance.stock_location_index()
        print("The response of StockLocationApi->stock_location_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockLocationApi->stock_location_index: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CollectionOfMerchantStockLocationWithCountryIsoResponse**](CollectionOfMerchantStockLocationWithCountryIsoResponse.md)

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

