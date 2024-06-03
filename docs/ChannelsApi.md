# openapi_client.ChannelsApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channel_plugins_get**](ChannelsApi.md#channel_plugins_get) | **GET** /v2/channels | Gets channels


# **channel_plugins_get**
> CollectionOfChannelGlobalChannelResponse channel_plugins_get()

Gets channels

Gets the complete list of channels available on ChannelEngine including their **Global channel ID**.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.collection_of_channel_global_channel_response import CollectionOfChannelGlobalChannelResponse
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
    api_instance = openapi_client.ChannelsApi(api_client)

    try:
        # Gets channels
        api_response = api_instance.channel_plugins_get()
        print("The response of ChannelsApi->channel_plugins_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->channel_plugins_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CollectionOfChannelGlobalChannelResponse**](CollectionOfChannelGlobalChannelResponse.md)

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

