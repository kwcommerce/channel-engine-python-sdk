# openapi_client.WebhookApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhooks_create**](WebhookApi.md#webhooks_create) | **POST** /v2/webhooks | Creates a webhook
[**webhooks_delete**](WebhookApi.md#webhooks_delete) | **DELETE** /v2/webhooks/{webhookName} | Deletes a webhook
[**webhooks_get_all**](WebhookApi.md#webhooks_get_all) | **GET** /v2/webhooks | Gets webhooks
[**webhooks_update**](WebhookApi.md#webhooks_update) | **PUT** /v2/webhooks | Updates a webhook


# **webhooks_create**
> ApiResponse webhooks_create(merchant_webhook_request=merchant_webhook_request)

Creates a webhook

Creates a webhook on ChannelEngine.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.merchant_webhook_request import MerchantWebhookRequest
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
    api_instance = openapi_client.WebhookApi(api_client)
    merchant_webhook_request = openapi_client.MerchantWebhookRequest() # MerchantWebhookRequest |  (optional)

    try:
        # Creates a webhook
        api_response = api_instance.webhooks_create(merchant_webhook_request=merchant_webhook_request)
        print("The response of WebhookApi->webhooks_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhooks_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_webhook_request** | [**MerchantWebhookRequest**](MerchantWebhookRequest.md)|  | [optional] 

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
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_delete**
> ApiResponse webhooks_delete(webhook_name)

Deletes a webhook

Deletes a webhook from ChannelEngine.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.api_response import ApiResponse
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
    api_instance = openapi_client.WebhookApi(api_client)
    webhook_name = 'webhook_name_example' # str | The unique name of a webhook you want to delete.

    try:
        # Deletes a webhook
        api_response = api_instance.webhooks_delete(webhook_name)
        print("The response of WebhookApi->webhooks_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhooks_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_name** | **str**| The unique name of a webhook you want to delete. | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_get_all**
> CollectionOfMerchantWebhookResponse webhooks_get_all()

Gets webhooks

Gets all webhooks created on ChannelEngine.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.collection_of_merchant_webhook_response import CollectionOfMerchantWebhookResponse
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
    api_instance = openapi_client.WebhookApi(api_client)

    try:
        # Gets webhooks
        api_response = api_instance.webhooks_get_all()
        print("The response of WebhookApi->webhooks_get_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhooks_get_all: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CollectionOfMerchantWebhookResponse**](CollectionOfMerchantWebhookResponse.md)

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

# **webhooks_update**
> ApiResponse webhooks_update(merchant_webhook_request=merchant_webhook_request)

Updates a webhook

Updates a webhook on ChannelEngine.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.merchant_webhook_request import MerchantWebhookRequest
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
    api_instance = openapi_client.WebhookApi(api_client)
    merchant_webhook_request = openapi_client.MerchantWebhookRequest() # MerchantWebhookRequest |  (optional)

    try:
        # Updates a webhook
        api_response = api_instance.webhooks_update(merchant_webhook_request=merchant_webhook_request)
        print("The response of WebhookApi->webhooks_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhooks_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_webhook_request** | [**MerchantWebhookRequest**](MerchantWebhookRequest.md)|  | [optional] 

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
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

