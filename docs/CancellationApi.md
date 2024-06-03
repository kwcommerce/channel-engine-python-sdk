# openapi_client.CancellationApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancellation_create**](CancellationApi.md#cancellation_create) | **POST** /v2/cancellations | Creates a cancelation
[**cancellation_get_for_merchant**](CancellationApi.md#cancellation_get_for_merchant) | **GET** /v2/cancellations/merchant | Gets cancelations


# **cancellation_create**
> ApiResponse cancellation_create(merchant_cancellation_request=merchant_cancellation_request)

Creates a cancelation

Marks an order as fully or partially canceled based on order line and quantity input.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.merchant_cancellation_request import MerchantCancellationRequest
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
    api_instance = openapi_client.CancellationApi(api_client)
    merchant_cancellation_request = openapi_client.MerchantCancellationRequest() # MerchantCancellationRequest |  (optional)

    try:
        # Creates a cancelation
        api_response = api_instance.cancellation_create(merchant_cancellation_request=merchant_cancellation_request)
        print("The response of CancellationApi->cancellation_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CancellationApi->cancellation_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_cancellation_request** | [**MerchantCancellationRequest**](MerchantCancellationRequest.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancellation_get_for_merchant**
> CollectionOfMerchantCancellationResponse cancellation_get_for_merchant(created_since=created_since, page=page)

Gets cancelations

Gets cancelations based on their creation date.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.collection_of_merchant_cancellation_response import CollectionOfMerchantCancellationResponse
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
    api_instance = openapi_client.CancellationApi(api_client)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter on the create date of the cancellation in ChannelEngine, starting from this date. This date is inclusive. (optional)
    page = 56 # int | The page to filter on. Starts at 1. (optional)

    try:
        # Gets cancelations
        api_response = api_instance.cancellation_get_for_merchant(created_since=created_since, page=page)
        print("The response of CancellationApi->cancellation_get_for_merchant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CancellationApi->cancellation_get_for_merchant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_since** | **datetime**| Filter on the create date of the cancellation in ChannelEngine, starting from this date. This date is inclusive. | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantCancellationResponse**](CollectionOfMerchantCancellationResponse.md)

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

