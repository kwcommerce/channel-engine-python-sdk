# openapi_client.ReturnApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**return_acknowledge**](ReturnApi.md#return_acknowledge) | **POST** /v2/returns/merchant/acknowledge | Acknowledges a return
[**return_declare_for_merchant**](ReturnApi.md#return_declare_for_merchant) | **POST** /v2/returns/merchant | Creates merchant return
[**return_get_by_merchant_order_no**](ReturnApi.md#return_get_by_merchant_order_no) | **GET** /v2/returns/merchant/{merchantOrderNo} | Gets a return
[**return_get_declared_by_channel**](ReturnApi.md#return_get_declared_by_channel) | **GET** /v2/returns/merchant | Gets marketplace returns
[**return_get_returns**](ReturnApi.md#return_get_returns) | **GET** /v2/returns | Gets returns by filter
[**return_get_unhandled**](ReturnApi.md#return_get_unhandled) | **GET** /v2/returns/merchant/new | Gets unhandled returns
[**return_update_for_merchant**](ReturnApi.md#return_update_for_merchant) | **PUT** /v2/returns | Marks returns as received


# **return_acknowledge**
> ApiResponse return_acknowledge(merchant_return_acknowledge_request=merchant_return_acknowledge_request)

Acknowledges a return

Acknowledges a return based on the **Return ID** provided.<br /><br />**NB:** by acknowledging a return, you signal that it was registered in your system.<br />You can later filter your returns on the **Is acknowledged** parameter.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.merchant_return_acknowledge_request import MerchantReturnAcknowledgeRequest
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
    api_instance = openapi_client.ReturnApi(api_client)
    merchant_return_acknowledge_request = openapi_client.MerchantReturnAcknowledgeRequest() # MerchantReturnAcknowledgeRequest |  (optional)

    try:
        # Acknowledges a return
        api_response = api_instance.return_acknowledge(merchant_return_acknowledge_request=merchant_return_acknowledge_request)
        print("The response of ReturnApi->return_acknowledge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnApi->return_acknowledge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_return_acknowledge_request** | [**MerchantReturnAcknowledgeRequest**](MerchantReturnAcknowledgeRequest.md)|  | [optional] 

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
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_declare_for_merchant**
> ApiResponse return_declare_for_merchant(merchant_return_request=merchant_return_request)

Creates merchant return

Marks an order as either fully or partially returned.<br /><br />**NB:** this endpoint is used for merchant returns (i.e.: returns dealt with by the merchant).

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.merchant_return_request import MerchantReturnRequest
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
    api_instance = openapi_client.ReturnApi(api_client)
    merchant_return_request = openapi_client.MerchantReturnRequest() # MerchantReturnRequest |  (optional)

    try:
        # Creates merchant return
        api_response = api_instance.return_declare_for_merchant(merchant_return_request=merchant_return_request)
        print("The response of ReturnApi->return_declare_for_merchant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnApi->return_declare_for_merchant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_return_request** | [**MerchantReturnRequest**](MerchantReturnRequest.md)|  | [optional] 

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

# **return_get_by_merchant_order_no**
> CollectionOfMerchantSingleOrderReturnResponse return_get_by_merchant_order_no(merchant_order_no)

Gets a return

Gets the returns based on the **Merchant order number** provided.<br /><br />**NB:** this endpoint is meant for merchants. Marketplaces should use the **GET /v2/returns/channel** call instead.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.collection_of_merchant_single_order_return_response import CollectionOfMerchantSingleOrderReturnResponse
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
    api_instance = openapi_client.ReturnApi(api_client)
    merchant_order_no = 'merchant_order_no_example' # str | 

    try:
        # Gets a return
        api_response = api_instance.return_get_by_merchant_order_no(merchant_order_no)
        print("The response of ReturnApi->return_get_by_merchant_order_no:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnApi->return_get_by_merchant_order_no: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_order_no** | **str**|  | 

### Return type

[**CollectionOfMerchantSingleOrderReturnResponse**](CollectionOfMerchantSingleOrderReturnResponse.md)

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

# **return_get_declared_by_channel**
> CollectionOfMerchantReturnResponse return_get_declared_by_channel(channel_ids=channel_ids, merchant_order_nos=merchant_order_nos, channel_order_nos=channel_order_nos, fulfillment_type=fulfillment_type, statuses=statuses, reasons=reasons, from_date=from_date, to_date=to_date, is_acknowledged=is_acknowledged, page=page)

Gets marketplace returns

Gets all returns created by the marketplace.<br /><br />**NB:** this endpoint is used for both marketplace and marketplace-fulfilled returns.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.collection_of_merchant_return_response import CollectionOfMerchantReturnResponse
from openapi_client.models.fulfillment_type import FulfillmentType
from openapi_client.models.return_reason import ReturnReason
from openapi_client.models.return_status import ReturnStatus
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
    api_instance = openapi_client.ReturnApi(api_client)
    channel_ids = [56] # List[int] | Filter on Channel IDs (optional)
    merchant_order_nos = ['merchant_order_nos_example'] # List[str] | Filter on unique order reference used by the merchant. (optional)
    channel_order_nos = ['channel_order_nos_example'] # List[str] | Filter on unique order reference used by the channel. (optional)
    fulfillment_type = openapi_client.FulfillmentType() # FulfillmentType | Filter on the fulfillment type of the order. (optional)
    statuses = [openapi_client.ReturnStatus()] # List[ReturnStatus] | Return status(es) to filter on. (optional)
    reasons = [openapi_client.ReturnReason()] # List[ReturnReason] | Return reason(s) to filter on. (optional)
    from_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the creation date, starting from this date. This date is inclusive. (optional)
    to_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the creation date, until this date. This date is exclusive. (optional)
    is_acknowledged = True # bool | Filters based on acknowledgements (optional)
    page = 56 # int | The page to filter on. Starts at 1. (optional)

    try:
        # Gets marketplace returns
        api_response = api_instance.return_get_declared_by_channel(channel_ids=channel_ids, merchant_order_nos=merchant_order_nos, channel_order_nos=channel_order_nos, fulfillment_type=fulfillment_type, statuses=statuses, reasons=reasons, from_date=from_date, to_date=to_date, is_acknowledged=is_acknowledged, page=page)
        print("The response of ReturnApi->return_get_declared_by_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnApi->return_get_declared_by_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_ids** | [**List[int]**](int.md)| Filter on Channel IDs | [optional] 
 **merchant_order_nos** | [**List[str]**](str.md)| Filter on unique order reference used by the merchant. | [optional] 
 **channel_order_nos** | [**List[str]**](str.md)| Filter on unique order reference used by the channel. | [optional] 
 **fulfillment_type** | [**FulfillmentType**](.md)| Filter on the fulfillment type of the order. | [optional] 
 **statuses** | [**List[ReturnStatus]**](ReturnStatus.md)| Return status(es) to filter on. | [optional] 
 **reasons** | [**List[ReturnReason]**](ReturnReason.md)| Return reason(s) to filter on. | [optional] 
 **from_date** | **datetime**| Filter on the creation date, starting from this date. This date is inclusive. | [optional] 
 **to_date** | **datetime**| Filter on the creation date, until this date. This date is exclusive. | [optional] 
 **is_acknowledged** | **bool**| Filters based on acknowledgements | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantReturnResponse**](CollectionOfMerchantReturnResponse.md)

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

# **return_get_returns**
> CollectionOfMerchantReturnResponse return_get_returns(creator_type=creator_type, channel_ids=channel_ids, merchant_order_nos=merchant_order_nos, channel_order_nos=channel_order_nos, fulfillment_type=fulfillment_type, statuses=statuses, reasons=reasons, from_date=from_date, to_date=to_date, is_acknowledged=is_acknowledged, page=page)

Gets returns by filter

Gets the returns based on the filter provided.<br /><br />**NB:** this endpoint is used to retrieve all types of returns: merchant, marketplace, mixed, and marketplace-fulfilled.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.collection_of_merchant_return_response import CollectionOfMerchantReturnResponse
from openapi_client.models.creator_filter import CreatorFilter
from openapi_client.models.fulfillment_type import FulfillmentType
from openapi_client.models.return_reason import ReturnReason
from openapi_client.models.return_status import ReturnStatus
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
    api_instance = openapi_client.ReturnApi(api_client)
    creator_type = openapi_client.CreatorFilter() # CreatorFilter | Filter on the return's creator. Default is MIXED. (optional)
    channel_ids = [56] # List[int] | Filter on Channel IDs (optional)
    merchant_order_nos = ['merchant_order_nos_example'] # List[str] | Filter on unique order reference used by the merchant. (optional)
    channel_order_nos = ['channel_order_nos_example'] # List[str] | Filter on unique order reference used by the channel. (optional)
    fulfillment_type = openapi_client.FulfillmentType() # FulfillmentType | Filter on the fulfillment type of the order. (optional)
    statuses = [openapi_client.ReturnStatus()] # List[ReturnStatus] | Return status(es) to filter on. (optional)
    reasons = [openapi_client.ReturnReason()] # List[ReturnReason] | Return reason(s) to filter on. (optional)
    from_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the creation date, starting from this date. This date is inclusive. (optional)
    to_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the creation date, until this date. This date is exclusive. (optional)
    is_acknowledged = True # bool | Filters based on acknowledgements (optional)
    page = 56 # int | The page to filter on. Starts at 1. (optional)

    try:
        # Gets returns by filter
        api_response = api_instance.return_get_returns(creator_type=creator_type, channel_ids=channel_ids, merchant_order_nos=merchant_order_nos, channel_order_nos=channel_order_nos, fulfillment_type=fulfillment_type, statuses=statuses, reasons=reasons, from_date=from_date, to_date=to_date, is_acknowledged=is_acknowledged, page=page)
        print("The response of ReturnApi->return_get_returns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnApi->return_get_returns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creator_type** | [**CreatorFilter**](.md)| Filter on the return&#39;s creator. Default is MIXED. | [optional] 
 **channel_ids** | [**List[int]**](int.md)| Filter on Channel IDs | [optional] 
 **merchant_order_nos** | [**List[str]**](str.md)| Filter on unique order reference used by the merchant. | [optional] 
 **channel_order_nos** | [**List[str]**](str.md)| Filter on unique order reference used by the channel. | [optional] 
 **fulfillment_type** | [**FulfillmentType**](.md)| Filter on the fulfillment type of the order. | [optional] 
 **statuses** | [**List[ReturnStatus]**](ReturnStatus.md)| Return status(es) to filter on. | [optional] 
 **reasons** | [**List[ReturnReason]**](ReturnReason.md)| Return reason(s) to filter on. | [optional] 
 **from_date** | **datetime**| Filter on the creation date, starting from this date. This date is inclusive. | [optional] 
 **to_date** | **datetime**| Filter on the creation date, until this date. This date is exclusive. | [optional] 
 **is_acknowledged** | **bool**| Filters based on acknowledgements | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantReturnResponse**](CollectionOfMerchantReturnResponse.md)

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

# **return_get_unhandled**
> CollectionOfMerchantReturnResponse return_get_unhandled(channel_ids=channel_ids, page=page)

Gets unhandled returns

Gets all marketplace returns with the status **In progress**.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.collection_of_merchant_return_response import CollectionOfMerchantReturnResponse
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
    api_instance = openapi_client.ReturnApi(api_client)
    channel_ids = [56] # List[int] | Filter on Channel IDs (optional)
    page = 56 # int | The page to filter on. Starts at 1. (optional)

    try:
        # Gets unhandled returns
        api_response = api_instance.return_get_unhandled(channel_ids=channel_ids, page=page)
        print("The response of ReturnApi->return_get_unhandled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnApi->return_get_unhandled: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_ids** | [**List[int]**](int.md)| Filter on Channel IDs | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantReturnResponse**](CollectionOfMerchantReturnResponse.md)

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

# **return_update_for_merchant**
> ApiResponse return_update_for_merchant(merchant_return_update_request=merchant_return_update_request)

Marks returns as received

Marks a return as either fully or partially received.<br /> <br />**NB:** this endpoint is used for marketplace returns, and you can only accept or reject a return once.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.merchant_return_update_request import MerchantReturnUpdateRequest
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
    api_instance = openapi_client.ReturnApi(api_client)
    merchant_return_update_request = openapi_client.MerchantReturnUpdateRequest() # MerchantReturnUpdateRequest |  (optional)

    try:
        # Marks returns as received
        api_response = api_instance.return_update_for_merchant(merchant_return_update_request=merchant_return_update_request)
        print("The response of ReturnApi->return_update_for_merchant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnApi->return_update_for_merchant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_return_update_request** | [**MerchantReturnUpdateRequest**](MerchantReturnUpdateRequest.md)|  | [optional] 

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
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

