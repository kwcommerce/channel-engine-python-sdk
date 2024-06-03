# openapi_client.OrderApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**order_acknowledge**](OrderApi.md#order_acknowledge) | **POST** /v2/orders/acknowledge | Acknowledges orders
[**order_get_by_filter**](OrderApi.md#order_get_by_filter) | **GET** /v2/orders | Gets orders by filter
[**order_get_new**](OrderApi.md#order_get_new) | **GET** /v2/orders/new | Gets new orders
[**order_invoice**](OrderApi.md#order_invoice) | **GET** /v2/orders/{merchantOrderNo}/invoice | Generates an order invoice
[**order_packing_slip**](OrderApi.md#order_packing_slip) | **GET** /v2/orders/{merchantOrderNo}/packingslip | Generates a packing slip
[**order_update**](OrderApi.md#order_update) | **PUT** /v2/orders/comment | Updates an order comment
[**order_upload_invoice**](OrderApi.md#order_upload_invoice) | **POST** /v2/orders/{merchantOrderNo}/invoice | Uploads an order invoice
[**order_upload_invoice_as_string**](OrderApi.md#order_upload_invoice_as_string) | **POST** /v2/orders/{merchantOrderNo}/invoice-base64 | Uploads an order invoice PDF from Base64 string.


# **order_acknowledge**
> ApiResponse order_acknowledge(merchant_order_acknowledgement_request=merchant_order_acknowledgement_request)

Acknowledges orders

Acknowledges an order to confirm order import.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.merchant_order_acknowledgement_request import MerchantOrderAcknowledgementRequest
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
    api_instance = openapi_client.OrderApi(api_client)
    merchant_order_acknowledgement_request = openapi_client.MerchantOrderAcknowledgementRequest() # MerchantOrderAcknowledgementRequest | Relations between the id's returned by ChannelEngine and the references which the merchant uses. (optional)

    try:
        # Acknowledges orders
        api_response = api_instance.order_acknowledge(merchant_order_acknowledgement_request=merchant_order_acknowledgement_request)
        print("The response of OrderApi->order_acknowledge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->order_acknowledge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_order_acknowledgement_request** | [**MerchantOrderAcknowledgementRequest**](MerchantOrderAcknowledgementRequest.md)| Relations between the id&#39;s returned by ChannelEngine and the references which the merchant uses. | [optional] 

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_get_by_filter**
> CollectionOfMerchantOrderResponse order_get_by_filter(statuses=statuses, email_addresses=email_addresses, merchant_order_nos=merchant_order_nos, channel_order_nos=channel_order_nos, commercial_order_nos=commercial_order_nos, from_date=from_date, to_date=to_date, from_created_at_date=from_created_at_date, to_created_at_date=to_created_at_date, exclude_marketplace_fulfilled_orders_and_lines=exclude_marketplace_fulfilled_orders_and_lines, fulfillment_type=fulfillment_type, only_with_cancellation_requests=only_with_cancellation_requests, channel_ids=channel_ids, stock_location_ids=stock_location_ids, is_acknowledged=is_acknowledged, from_updated_at_date=from_updated_at_date, to_updated_at_date=to_updated_at_date, from_acknowledged_date=from_acknowledged_date, to_acknowledged_date=to_acknowledged_date, page=page)

Gets orders by filter

Gets orders based on the available filters.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.collection_of_merchant_order_response import CollectionOfMerchantOrderResponse
from openapi_client.models.fulfillment_type import FulfillmentType
from openapi_client.models.order_status_view import OrderStatusView
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
    api_instance = openapi_client.OrderApi(api_client)
    statuses = [openapi_client.OrderStatusView()] # List[OrderStatusView] | Order status(es) to filter on. AWAITING_PAYMENT orders will be excluded if it is not included in this Statuses filter. (optional)
    email_addresses = ['email_addresses_example'] # List[str] | Client emailaddresses to filter on. (optional)
    merchant_order_nos = ['merchant_order_nos_example'] # List[str] | Filter on unique order reference used by the merchant. (optional)
    channel_order_nos = ['channel_order_nos_example'] # List[str] | Filter on unique order reference used by the channel. (optional)
    commercial_order_nos = ['commercial_order_nos_example'] # List[str] | Filter on commercial order numbers. (optional)
    from_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the order date, starting from this date. This date is inclusive.<br />The order date is based on the data we got from a channel. (optional)
    to_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the order date, until this date. This date is exclusive.<br />The order date is based on the data we got from a channel. (optional)
    from_created_at_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the created at date in ChannelEngine, starting from this date. This date is inclusive.<br />The created date is set on the date and time when the order is created. (optional)
    to_created_at_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the created at date in ChannelEngine, until this date. This date is exclusive.<br />The created date is set on the date and time when the order is created. (optional)
    exclude_marketplace_fulfilled_orders_and_lines = True # bool | Exclude order (lines) fulfilled by the marketplace (amazon:FBA, bol:LVB, etc.) (optional)
    fulfillment_type = openapi_client.FulfillmentType() # FulfillmentType | Filter orders on fulfillment type. This will include all orders lines, even if they are partially fulfilled by the marketplace.<br />To exclude orders and lines that are fulfilled by the marketplace from the response, set ExcludeMarketplaceFulfilledOrdersAndLines to true. (optional)
    only_with_cancellation_requests = True # bool | Filter on orders containing cancellation requests.<br />Some channels allow a customer to cancel an order until it has been shipped.<br />When an order has already been acknowledged in ChannelEngine, it can only be cancelled by creating a cancellation. (optional)
    channel_ids = [56] # List[int] | Filter orders on channel(s). (optional)
    stock_location_ids = [56] # List[int] | Filter on stock locations (optional)
    is_acknowledged = True # bool | Filter on acknowledged value (optional)
    from_updated_at_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the order update date, starting from this date. This date is inclusive. (optional)
    to_updated_at_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the order update date, unitl this date. This date is exclusive. (optional)
    from_acknowledged_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the order acknowledged date, starting from this date. This date is inclusive. (optional)
    to_acknowledged_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the order acknowledged date, unitl this date. This date is exclusive. (optional)
    page = 56 # int | The page to filter on. Starts at 1. (optional)

    try:
        # Gets orders by filter
        api_response = api_instance.order_get_by_filter(statuses=statuses, email_addresses=email_addresses, merchant_order_nos=merchant_order_nos, channel_order_nos=channel_order_nos, commercial_order_nos=commercial_order_nos, from_date=from_date, to_date=to_date, from_created_at_date=from_created_at_date, to_created_at_date=to_created_at_date, exclude_marketplace_fulfilled_orders_and_lines=exclude_marketplace_fulfilled_orders_and_lines, fulfillment_type=fulfillment_type, only_with_cancellation_requests=only_with_cancellation_requests, channel_ids=channel_ids, stock_location_ids=stock_location_ids, is_acknowledged=is_acknowledged, from_updated_at_date=from_updated_at_date, to_updated_at_date=to_updated_at_date, from_acknowledged_date=from_acknowledged_date, to_acknowledged_date=to_acknowledged_date, page=page)
        print("The response of OrderApi->order_get_by_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->order_get_by_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statuses** | [**List[OrderStatusView]**](OrderStatusView.md)| Order status(es) to filter on. AWAITING_PAYMENT orders will be excluded if it is not included in this Statuses filter. | [optional] 
 **email_addresses** | [**List[str]**](str.md)| Client emailaddresses to filter on. | [optional] 
 **merchant_order_nos** | [**List[str]**](str.md)| Filter on unique order reference used by the merchant. | [optional] 
 **channel_order_nos** | [**List[str]**](str.md)| Filter on unique order reference used by the channel. | [optional] 
 **commercial_order_nos** | [**List[str]**](str.md)| Filter on commercial order numbers. | [optional] 
 **from_date** | **datetime**| Filter on the order date, starting from this date. This date is inclusive.&lt;br /&gt;The order date is based on the data we got from a channel. | [optional] 
 **to_date** | **datetime**| Filter on the order date, until this date. This date is exclusive.&lt;br /&gt;The order date is based on the data we got from a channel. | [optional] 
 **from_created_at_date** | **datetime**| Filter on the created at date in ChannelEngine, starting from this date. This date is inclusive.&lt;br /&gt;The created date is set on the date and time when the order is created. | [optional] 
 **to_created_at_date** | **datetime**| Filter on the created at date in ChannelEngine, until this date. This date is exclusive.&lt;br /&gt;The created date is set on the date and time when the order is created. | [optional] 
 **exclude_marketplace_fulfilled_orders_and_lines** | **bool**| Exclude order (lines) fulfilled by the marketplace (amazon:FBA, bol:LVB, etc.) | [optional] 
 **fulfillment_type** | [**FulfillmentType**](.md)| Filter orders on fulfillment type. This will include all orders lines, even if they are partially fulfilled by the marketplace.&lt;br /&gt;To exclude orders and lines that are fulfilled by the marketplace from the response, set ExcludeMarketplaceFulfilledOrdersAndLines to true. | [optional] 
 **only_with_cancellation_requests** | **bool**| Filter on orders containing cancellation requests.&lt;br /&gt;Some channels allow a customer to cancel an order until it has been shipped.&lt;br /&gt;When an order has already been acknowledged in ChannelEngine, it can only be cancelled by creating a cancellation. | [optional] 
 **channel_ids** | [**List[int]**](int.md)| Filter orders on channel(s). | [optional] 
 **stock_location_ids** | [**List[int]**](int.md)| Filter on stock locations | [optional] 
 **is_acknowledged** | **bool**| Filter on acknowledged value | [optional] 
 **from_updated_at_date** | **datetime**| Filter on the order update date, starting from this date. This date is inclusive. | [optional] 
 **to_updated_at_date** | **datetime**| Filter on the order update date, unitl this date. This date is exclusive. | [optional] 
 **from_acknowledged_date** | **datetime**| Filter on the order acknowledged date, starting from this date. This date is inclusive. | [optional] 
 **to_acknowledged_date** | **datetime**| Filter on the order acknowledged date, unitl this date. This date is exclusive. | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantOrderResponse**](CollectionOfMerchantOrderResponse.md)

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

# **order_get_new**
> CollectionOfMerchantOrderResponse order_get_new(stock_location_id=stock_location_id)

Gets new orders

Gets orders with the status **New**.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.collection_of_merchant_order_response import CollectionOfMerchantOrderResponse
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
    api_instance = openapi_client.OrderApi(api_client)
    stock_location_id = 56 # int | The ChannelEngine id of the stock location. (optional)

    try:
        # Gets new orders
        api_response = api_instance.order_get_new(stock_location_id=stock_location_id)
        print("The response of OrderApi->order_get_new:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->order_get_new: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_location_id** | **int**| The ChannelEngine id of the stock location. | [optional] 

### Return type

[**CollectionOfMerchantOrderResponse**](CollectionOfMerchantOrderResponse.md)

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

# **order_invoice**
> bytearray order_invoice(merchant_order_no, use_customer_culture=use_customer_culture)

Generates an order invoice

Generates the ChannelEngine sales tax invoice for an order in PDF.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
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
    api_instance = openapi_client.OrderApi(api_client)
    merchant_order_no = 'merchant_order_no_example' # str | The unique order reference as used by the merchant.
    use_customer_culture = False # bool | Generate the invoice in the billing address' country's language. (optional) (default to False)

    try:
        # Generates an order invoice
        api_response = api_instance.order_invoice(merchant_order_no, use_customer_culture=use_customer_culture)
        print("The response of OrderApi->order_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->order_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_order_no** | **str**| The unique order reference as used by the merchant. | 
 **use_customer_culture** | **bool**| Generate the invoice in the billing address&#39; country&#39;s language. | [optional] [default to False]

### Return type

**bytearray**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invoice PDF |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_packing_slip**
> bytearray order_packing_slip(merchant_order_no, use_customer_culture=use_customer_culture)

Generates a packing slip

Generates the ChannelEngine packing slip for an order in PDF.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
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
    api_instance = openapi_client.OrderApi(api_client)
    merchant_order_no = 'merchant_order_no_example' # str | The unique order reference as used by the merchant.
    use_customer_culture = False # bool | Generate the invoice in the billing address' country's language. (optional) (default to False)

    try:
        # Generates a packing slip
        api_response = api_instance.order_packing_slip(merchant_order_no, use_customer_culture=use_customer_culture)
        print("The response of OrderApi->order_packing_slip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->order_packing_slip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_order_no** | **str**| The unique order reference as used by the merchant. | 
 **use_customer_culture** | **bool**| Generate the invoice in the billing address&#39; country&#39;s language. | [optional] [default to False]

### Return type

**bytearray**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Packing Slip PDF |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_update**
> ApiResponse order_update(merchant_order_comment_update_request=merchant_order_comment_update_request)

Updates an order comment

Updates the merchant comment for an order based on the ChannelEngine **Order ID** or the **Merchant order number**.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.merchant_order_comment_update_request import MerchantOrderCommentUpdateRequest
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
    api_instance = openapi_client.OrderApi(api_client)
    merchant_order_comment_update_request = openapi_client.MerchantOrderCommentUpdateRequest() # MerchantOrderCommentUpdateRequest |  (optional)

    try:
        # Updates an order comment
        api_response = api_instance.order_update(merchant_order_comment_update_request=merchant_order_comment_update_request)
        print("The response of OrderApi->order_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->order_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_order_comment_update_request** | [**MerchantOrderCommentUpdateRequest**](MerchantOrderCommentUpdateRequest.md)|  | [optional] 

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

# **order_upload_invoice**
> ApiResponse order_upload_invoice(merchant_order_no, invoice, invoice_number=invoice_number)

Uploads an order invoice

Uploads the invoice for an order in PDF.

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
    api_instance = openapi_client.OrderApi(api_client)
    merchant_order_no = 'merchant_order_no_example' # str | The unique order reference as used by the merchant.
    invoice = None # bytearray | PDF invoice file up to 1 MB with additional data.
    invoice_number = 'invoice_number_example' # str | The invoice number used in the invoice. (optional)

    try:
        # Uploads an order invoice
        api_response = api_instance.order_upload_invoice(merchant_order_no, invoice, invoice_number=invoice_number)
        print("The response of OrderApi->order_upload_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->order_upload_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_order_no** | **str**| The unique order reference as used by the merchant. | 
 **invoice** | **bytearray**| PDF invoice file up to 1 MB with additional data. | 
 **invoice_number** | **str**| The invoice number used in the invoice. | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_upload_invoice_as_string**
> ApiResponse order_upload_invoice_as_string(merchant_order_no, merchant_invoice_upload_request=merchant_invoice_upload_request)

Uploads an order invoice PDF from Base64 string.

Uploads an order invoice PDF from Base64 string.<br />Invoice size must be less than 1 mb.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.merchant_invoice_upload_request import MerchantInvoiceUploadRequest
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
    api_instance = openapi_client.OrderApi(api_client)
    merchant_order_no = 'merchant_order_no_example' # str | 
    merchant_invoice_upload_request = openapi_client.MerchantInvoiceUploadRequest() # MerchantInvoiceUploadRequest |  (optional)

    try:
        # Uploads an order invoice PDF from Base64 string.
        api_response = api_instance.order_upload_invoice_as_string(merchant_order_no, merchant_invoice_upload_request=merchant_invoice_upload_request)
        print("The response of OrderApi->order_upload_invoice_as_string:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->order_upload_invoice_as_string: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_order_no** | **str**|  | 
 **merchant_invoice_upload_request** | [**MerchantInvoiceUploadRequest**](MerchantInvoiceUploadRequest.md)|  | [optional] 

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

