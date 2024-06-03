# openapi_client.PurchaseOrdersApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acknowledge**](PurchaseOrdersApi.md#acknowledge) | **POST** /v2/purchase-orders/lines/acknowledge | Acknowledges lines of a purchase order
[**create**](PurchaseOrdersApi.md#create) | **POST** /v2/purchase-orders/shipments | Create a purchase order shipment.
[**create_invoice**](PurchaseOrdersApi.md#create_invoice) | **POST** /v2/purchase-orders/invoice | Creates a purchase order invoice
[**create_invoices**](PurchaseOrdersApi.md#create_invoices) | **POST** /v2/purchase-orders/invoice/bulk | Creates a purchase order invoices in a bulk
[**get_by_filter**](PurchaseOrdersApi.md#get_by_filter) | **GET** /v2/purchase-orders | Gets purchase orders by filter
[**get_by_filter_shipment_merchant**](PurchaseOrdersApi.md#get_by_filter_shipment_merchant) | **GET** /v2/purchase-orders/shipments/merchant | Gets purchase order shipments by filter
[**update**](PurchaseOrdersApi.md#update) | **PUT** /v2/purchase-orders/shipments | Update a purchase order shipment.


# **acknowledge**
> ApiResponse acknowledge(single_merchant_acknowledge_purchase_order_lines_request=single_merchant_acknowledge_purchase_order_lines_request)

Acknowledges lines of a purchase order

Creates line acknowledgements (i.e., accepted, backordered, rejected) for a purchase order.<br />Request will be accepted and data persisted only if all validations passed.<br />Any validation messages and errors will be returned in a HTTP 4xx response.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.single_merchant_acknowledge_purchase_order_lines_request import SingleMerchantAcknowledgePurchaseOrderLinesRequest
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
    api_instance = openapi_client.PurchaseOrdersApi(api_client)
    single_merchant_acknowledge_purchase_order_lines_request = openapi_client.SingleMerchantAcknowledgePurchaseOrderLinesRequest() # SingleMerchantAcknowledgePurchaseOrderLinesRequest | Model for purchase order and lines data to be acknowledged with the channel. (optional)

    try:
        # Acknowledges lines of a purchase order
        api_response = api_instance.acknowledge(single_merchant_acknowledge_purchase_order_lines_request=single_merchant_acknowledge_purchase_order_lines_request)
        print("The response of PurchaseOrdersApi->acknowledge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrdersApi->acknowledge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **single_merchant_acknowledge_purchase_order_lines_request** | [**SingleMerchantAcknowledgePurchaseOrderLinesRequest**](SingleMerchantAcknowledgePurchaseOrderLinesRequest.md)| Model for purchase order and lines data to be acknowledged with the channel. | [optional] 

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

# **create**
> ApiResponse create(single_merchant_create_purchase_order_shipment_request=single_merchant_create_purchase_order_shipment_request)

Create a purchase order shipment.

One shipments can ship (parts of) multiple orders

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.single_merchant_create_purchase_order_shipment_request import SingleMerchantCreatePurchaseOrderShipmentRequest
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
    api_instance = openapi_client.PurchaseOrdersApi(api_client)
    single_merchant_create_purchase_order_shipment_request = openapi_client.SingleMerchantCreatePurchaseOrderShipmentRequest() # SingleMerchantCreatePurchaseOrderShipmentRequest |  (optional)

    try:
        # Create a purchase order shipment.
        api_response = api_instance.create(single_merchant_create_purchase_order_shipment_request=single_merchant_create_purchase_order_shipment_request)
        print("The response of PurchaseOrdersApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrdersApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **single_merchant_create_purchase_order_shipment_request** | [**SingleMerchantCreatePurchaseOrderShipmentRequest**](SingleMerchantCreatePurchaseOrderShipmentRequest.md)|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invoice**
> ApiResponse create_invoice(single_merchant_create_purchase_order_invoice_request=single_merchant_create_purchase_order_invoice_request)

Creates a purchase order invoice

Creates invoice for a purchase order.<br />Request will be accepted and data persisted only if all validations passed.<br />Any validation messages and errors will be returned in a HTTP 4xx response.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.single_merchant_create_purchase_order_invoice_request import SingleMerchantCreatePurchaseOrderInvoiceRequest
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
    api_instance = openapi_client.PurchaseOrdersApi(api_client)
    single_merchant_create_purchase_order_invoice_request = openapi_client.SingleMerchantCreatePurchaseOrderInvoiceRequest() # SingleMerchantCreatePurchaseOrderInvoiceRequest | Model for purchase order invoice. (optional)

    try:
        # Creates a purchase order invoice
        api_response = api_instance.create_invoice(single_merchant_create_purchase_order_invoice_request=single_merchant_create_purchase_order_invoice_request)
        print("The response of PurchaseOrdersApi->create_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrdersApi->create_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **single_merchant_create_purchase_order_invoice_request** | [**SingleMerchantCreatePurchaseOrderInvoiceRequest**](SingleMerchantCreatePurchaseOrderInvoiceRequest.md)| Model for purchase order invoice. | [optional] 

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

# **create_invoices**
> ApiResponse create_invoices(bulk_merchant_create_purchase_order_invoices_request=bulk_merchant_create_purchase_order_invoices_request)

Creates a purchase order invoices in a bulk

Creates invoices for a purchase orders in a bulk.<br />Request will be accepted and data persisted only if all validations passed.<br />Any validation messages and errors will be returned in a HTTP 4xx response.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.bulk_merchant_create_purchase_order_invoices_request import BulkMerchantCreatePurchaseOrderInvoicesRequest
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
    api_instance = openapi_client.PurchaseOrdersApi(api_client)
    bulk_merchant_create_purchase_order_invoices_request = openapi_client.BulkMerchantCreatePurchaseOrderInvoicesRequest() # BulkMerchantCreatePurchaseOrderInvoicesRequest | Model for purchase order invoices. (optional)

    try:
        # Creates a purchase order invoices in a bulk
        api_response = api_instance.create_invoices(bulk_merchant_create_purchase_order_invoices_request=bulk_merchant_create_purchase_order_invoices_request)
        print("The response of PurchaseOrdersApi->create_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrdersApi->create_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_merchant_create_purchase_order_invoices_request** | [**BulkMerchantCreatePurchaseOrderInvoicesRequest**](BulkMerchantCreatePurchaseOrderInvoicesRequest.md)| Model for purchase order invoices. | [optional] 

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

# **get_by_filter**
> CollectionOfIPurchaseOrderByFilter get_by_filter(identifiers_identifier_type=identifiers_identifier_type, identifiers_models=identifiers_models, statuses=statuses, order_date_range_from_date=order_date_range_from_date, order_date_range_to_date=order_date_range_to_date, create_date_range_from_date=create_date_range_from_date, create_date_range_to_date=create_date_range_to_date, update_date_range_from_date=update_date_range_from_date, update_date_range_to_date=update_date_range_to_date, channel_ids=channel_ids, type=type, page_index=page_index, page_size=page_size)

Gets purchase orders by filter

Gets purchase orders based on the available filters.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.collection_of_i_purchase_order_by_filter import CollectionOfIPurchaseOrderByFilter
from openapi_client.models.modules_purchase_order_status import ModulesPurchaseOrderStatus
from openapi_client.models.modules_purchase_order_type import ModulesPurchaseOrderType
from openapi_client.models.purchase_order_identifier_type import PurchaseOrderIdentifierType
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
    api_instance = openapi_client.PurchaseOrdersApi(api_client)
    identifiers_identifier_type = openapi_client.PurchaseOrderIdentifierType() # PurchaseOrderIdentifierType | The type of identifier: which identifier to filter on (optional)
    identifiers_models = ['identifiers_models_example'] # List[str] | The value (of the selected type) to filter on (optional)
    statuses = [openapi_client.ModulesPurchaseOrderStatus()] # List[ModulesPurchaseOrderStatus] |  (optional)
    order_date_range_from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    order_date_range_to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    create_date_range_from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    create_date_range_to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    update_date_range_from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    update_date_range_to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    channel_ids = [56] # List[int] |  (optional)
    type = openapi_client.ModulesPurchaseOrderType() # ModulesPurchaseOrderType |  (optional)
    page_index = 56 # int |  (optional)
    page_size = 56 # int |  (optional)

    try:
        # Gets purchase orders by filter
        api_response = api_instance.get_by_filter(identifiers_identifier_type=identifiers_identifier_type, identifiers_models=identifiers_models, statuses=statuses, order_date_range_from_date=order_date_range_from_date, order_date_range_to_date=order_date_range_to_date, create_date_range_from_date=create_date_range_from_date, create_date_range_to_date=create_date_range_to_date, update_date_range_from_date=update_date_range_from_date, update_date_range_to_date=update_date_range_to_date, channel_ids=channel_ids, type=type, page_index=page_index, page_size=page_size)
        print("The response of PurchaseOrdersApi->get_by_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrdersApi->get_by_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifiers_identifier_type** | [**PurchaseOrderIdentifierType**](.md)| The type of identifier: which identifier to filter on | [optional] 
 **identifiers_models** | [**List[str]**](str.md)| The value (of the selected type) to filter on | [optional] 
 **statuses** | [**List[ModulesPurchaseOrderStatus]**](ModulesPurchaseOrderStatus.md)|  | [optional] 
 **order_date_range_from_date** | **datetime**|  | [optional] 
 **order_date_range_to_date** | **datetime**|  | [optional] 
 **create_date_range_from_date** | **datetime**|  | [optional] 
 **create_date_range_to_date** | **datetime**|  | [optional] 
 **update_date_range_from_date** | **datetime**|  | [optional] 
 **update_date_range_to_date** | **datetime**|  | [optional] 
 **channel_ids** | [**List[int]**](int.md)|  | [optional] 
 **type** | [**ModulesPurchaseOrderType**](.md)|  | [optional] 
 **page_index** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**CollectionOfIPurchaseOrderByFilter**](CollectionOfIPurchaseOrderByFilter.md)

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

# **get_by_filter_shipment_merchant**
> CollectionOfIPurchaseOrderShipmentByFilter get_by_filter_shipment_merchant(channel_id=channel_id, identifiers_identifier_type=identifiers_identifier_type, identifiers_models=identifiers_models, shipped_date_range_from_date=shipped_date_range_from_date, shipped_date_range_to_date=shipped_date_range_to_date, create_date_range_from_date=create_date_range_from_date, create_date_range_to_date=create_date_range_to_date, update_date_range_from_date=update_date_range_from_date, update_date_range_to_date=update_date_range_to_date, bill_of_lading_number=bill_of_lading_number, carrier_name=carrier_name, page_index=page_index, page_size=page_size)

Gets purchase order shipments by filter

Gets purchase order shipments based on the available filters.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.collection_of_i_purchase_order_shipment_by_filter import CollectionOfIPurchaseOrderShipmentByFilter
from openapi_client.models.purchase_order_shipment_identifier_type_value import PurchaseOrderShipmentIdentifierTypeValue
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
    api_instance = openapi_client.PurchaseOrdersApi(api_client)
    channel_id = 56 # int | The identifier of the channel (optional)
    identifiers_identifier_type = openapi_client.PurchaseOrderShipmentIdentifierTypeValue() # PurchaseOrderShipmentIdentifierTypeValue | The type of identifier: which identifier to filter on (optional)
    identifiers_models = ['identifiers_models_example'] # List[str] | The value (of the selected type) to filter on (optional)
    shipped_date_range_from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    shipped_date_range_to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    create_date_range_from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    create_date_range_to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    update_date_range_from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    update_date_range_to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    bill_of_lading_number = 'bill_of_lading_number_example' # str | The Bill of Lading number. Multiple shipments can have the same Bill of Lading number (optional)
    carrier_name = 'carrier_name_example' # str | The name of the carrier (optional)
    page_index = 56 # int |  (optional)
    page_size = 56 # int |  (optional)

    try:
        # Gets purchase order shipments by filter
        api_response = api_instance.get_by_filter_shipment_merchant(channel_id=channel_id, identifiers_identifier_type=identifiers_identifier_type, identifiers_models=identifiers_models, shipped_date_range_from_date=shipped_date_range_from_date, shipped_date_range_to_date=shipped_date_range_to_date, create_date_range_from_date=create_date_range_from_date, create_date_range_to_date=create_date_range_to_date, update_date_range_from_date=update_date_range_from_date, update_date_range_to_date=update_date_range_to_date, bill_of_lading_number=bill_of_lading_number, carrier_name=carrier_name, page_index=page_index, page_size=page_size)
        print("The response of PurchaseOrdersApi->get_by_filter_shipment_merchant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrdersApi->get_by_filter_shipment_merchant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **int**| The identifier of the channel | [optional] 
 **identifiers_identifier_type** | [**PurchaseOrderShipmentIdentifierTypeValue**](.md)| The type of identifier: which identifier to filter on | [optional] 
 **identifiers_models** | [**List[str]**](str.md)| The value (of the selected type) to filter on | [optional] 
 **shipped_date_range_from_date** | **datetime**|  | [optional] 
 **shipped_date_range_to_date** | **datetime**|  | [optional] 
 **create_date_range_from_date** | **datetime**|  | [optional] 
 **create_date_range_to_date** | **datetime**|  | [optional] 
 **update_date_range_from_date** | **datetime**|  | [optional] 
 **update_date_range_to_date** | **datetime**|  | [optional] 
 **bill_of_lading_number** | **str**| The Bill of Lading number. Multiple shipments can have the same Bill of Lading number | [optional] 
 **carrier_name** | **str**| The name of the carrier | [optional] 
 **page_index** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**CollectionOfIPurchaseOrderShipmentByFilter**](CollectionOfIPurchaseOrderShipmentByFilter.md)

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

# **update**
> ApiResponse update(single_merchant_update_purchase_order_shipment_request=single_merchant_update_purchase_order_shipment_request)

Update a purchase order shipment.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.single_merchant_update_purchase_order_shipment_request import SingleMerchantUpdatePurchaseOrderShipmentRequest
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
    api_instance = openapi_client.PurchaseOrdersApi(api_client)
    single_merchant_update_purchase_order_shipment_request = openapi_client.SingleMerchantUpdatePurchaseOrderShipmentRequest() # SingleMerchantUpdatePurchaseOrderShipmentRequest |  (optional)

    try:
        # Update a purchase order shipment.
        api_response = api_instance.update(single_merchant_update_purchase_order_shipment_request=single_merchant_update_purchase_order_shipment_request)
        print("The response of PurchaseOrdersApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrdersApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **single_merchant_update_purchase_order_shipment_request** | [**SingleMerchantUpdatePurchaseOrderShipmentRequest**](SingleMerchantUpdatePurchaseOrderShipmentRequest.md)|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

