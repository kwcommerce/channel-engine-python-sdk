# openapi_client.NotificationApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notification_index**](NotificationApi.md#notification_index) | **GET** /v2/notifications | Gets notifications


# **notification_index**
> CollectionOfMerchantNotificationResponse notification_index(from_date=from_date, to_date=to_date, types=types, merchant_order_nos=merchant_order_nos, channel_order_nos=channel_order_nos, merchant_return_nos=merchant_return_nos, channel_return_nos=channel_return_nos, merchant_shipment_nos=merchant_shipment_nos, page=page)

Gets notifications

Gets ChannelEngine notifications based on the available filters.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.collection_of_merchant_notification_response import CollectionOfMerchantNotificationResponse
from openapi_client.models.notification_type import NotificationType
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
    api_instance = openapi_client.NotificationApi(api_client)
    from_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the notification date, starting from this date. This date is inclusive. (optional)
    to_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the notification date, until this date. This date is exclusive. (optional)
    types = [openapi_client.NotificationType()] # List[NotificationType] | Notification type(s) to filter on. (optional)
    merchant_order_nos = ['merchant_order_nos_example'] # List[str] | Filter on unique order reference used by the merchant. (optional)
    channel_order_nos = ['channel_order_nos_example'] # List[str] | Filter on unique order reference used by the channel. (optional)
    merchant_return_nos = ['merchant_return_nos_example'] # List[str] | Filter on unique return reference used by the merchant. (optional)
    channel_return_nos = ['channel_return_nos_example'] # List[str] | Filter on unique return reference used by the channel. (optional)
    merchant_shipment_nos = ['merchant_shipment_nos_example'] # List[str] | Filter on unique shipment reference used by the merchant. (optional)
    page = 56 # int | The page to filter on. Starts at 1. (optional)

    try:
        # Gets notifications
        api_response = api_instance.notification_index(from_date=from_date, to_date=to_date, types=types, merchant_order_nos=merchant_order_nos, channel_order_nos=channel_order_nos, merchant_return_nos=merchant_return_nos, channel_return_nos=channel_return_nos, merchant_shipment_nos=merchant_shipment_nos, page=page)
        print("The response of NotificationApi->notification_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->notification_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_date** | **datetime**| Filter on the notification date, starting from this date. This date is inclusive. | [optional] 
 **to_date** | **datetime**| Filter on the notification date, until this date. This date is exclusive. | [optional] 
 **types** | [**List[NotificationType]**](NotificationType.md)| Notification type(s) to filter on. | [optional] 
 **merchant_order_nos** | [**List[str]**](str.md)| Filter on unique order reference used by the merchant. | [optional] 
 **channel_order_nos** | [**List[str]**](str.md)| Filter on unique order reference used by the channel. | [optional] 
 **merchant_return_nos** | [**List[str]**](str.md)| Filter on unique return reference used by the merchant. | [optional] 
 **channel_return_nos** | [**List[str]**](str.md)| Filter on unique return reference used by the channel. | [optional] 
 **merchant_shipment_nos** | [**List[str]**](str.md)| Filter on unique shipment reference used by the merchant. | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantNotificationResponse**](CollectionOfMerchantNotificationResponse.md)

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

