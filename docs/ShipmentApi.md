# openapi_client.ShipmentApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shipment_create**](ShipmentApi.md#shipment_create) | **POST** /v2/shipments | Creates shipments
[**shipment_create_for_channel_method**](ShipmentApi.md#shipment_create_for_channel_method) | **POST** /v2/shipments/channelmethod | Creates a shipment and initiates shipping label generation
[**shipment_get_shipment_label_carriers**](ShipmentApi.md#shipment_get_shipment_label_carriers) | **POST** /v2/carriers/{merchantOrderNo} | Gets carriers providing shipping labels
[**shipment_index**](ShipmentApi.md#shipment_index) | **GET** /v2/shipments/merchant | Gets shipments by filter
[**shipment_shipping_label**](ShipmentApi.md#shipment_shipping_label) | **GET** /v2/orders/{merchantShipmentNo}/shippinglabel | Gets a shipping label
[**shipment_update**](ShipmentApi.md#shipment_update) | **PUT** /v2/shipments/{merchantShipmentNo} | Updates a shipment


# **shipment_create**
> ApiResponse shipment_create(merchant_shipment_request=merchant_shipment_request)

Creates shipments

Marks an order as fully or partially shipped, based on the order line and quantity input.<br />Indicate the **Stock location ID** if you make use of multiple stock locations.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.merchant_shipment_request import MerchantShipmentRequest
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
    api_instance = openapi_client.ShipmentApi(api_client)
    merchant_shipment_request = openapi_client.MerchantShipmentRequest() # MerchantShipmentRequest |  (optional)

    try:
        # Creates shipments
        api_response = api_instance.shipment_create(merchant_shipment_request=merchant_shipment_request)
        print("The response of ShipmentApi->shipment_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->shipment_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_shipment_request** | [**MerchantShipmentRequest**](MerchantShipmentRequest.md)|  | [optional] 

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

# **shipment_create_for_channel_method**
> ApiResponse shipment_create_for_channel_method(merchant_channel_label_shipment_request=merchant_channel_label_shipment_request)

Creates a shipment and initiates shipping label generation

Marks an order as either fully or partially shipped, based on the order line and quantity input.<br />It also provides the marketplace with information necessary to generate a shipping label.<br />If you make use of multiple stock locations, indicate the **Stock location ID**.<br /> <br />**NB:** to request a shipping label, include information on the package size (i.e.: dimensions and weight).

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.merchant_channel_label_shipment_request import MerchantChannelLabelShipmentRequest
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
    api_instance = openapi_client.ShipmentApi(api_client)
    merchant_channel_label_shipment_request = openapi_client.MerchantChannelLabelShipmentRequest() # MerchantChannelLabelShipmentRequest | The shipment to create (optional)

    try:
        # Creates a shipment and initiates shipping label generation
        api_response = api_instance.shipment_create_for_channel_method(merchant_channel_label_shipment_request=merchant_channel_label_shipment_request)
        print("The response of ShipmentApi->shipment_create_for_channel_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->shipment_create_for_channel_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_channel_label_shipment_request** | [**MerchantChannelLabelShipmentRequest**](MerchantChannelLabelShipmentRequest.md)| The shipment to create | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_get_shipment_label_carriers**
> CollectionOfMerchantShipmentLabelCarrierResponse shipment_get_shipment_label_carriers(merchant_order_no, merchant_shipment_label_carrier_request=merchant_shipment_label_carrier_request)

Gets carriers providing shipping labels

Posts a request to get the available marketplace carrier offers.<br /><br />**NB:** this endpoint is used to buy a shipping label through the marketplace.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.collection_of_merchant_shipment_label_carrier_response import CollectionOfMerchantShipmentLabelCarrierResponse
from openapi_client.models.merchant_shipment_label_carrier_request import MerchantShipmentLabelCarrierRequest
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
    api_instance = openapi_client.ShipmentApi(api_client)
    merchant_order_no = 'merchant_order_no_example' # str | The merchant's order reference.
    merchant_shipment_label_carrier_request = openapi_client.MerchantShipmentLabelCarrierRequest() # MerchantShipmentLabelCarrierRequest | The parcel information (optional)

    try:
        # Gets carriers providing shipping labels
        api_response = api_instance.shipment_get_shipment_label_carriers(merchant_order_no, merchant_shipment_label_carrier_request=merchant_shipment_label_carrier_request)
        print("The response of ShipmentApi->shipment_get_shipment_label_carriers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->shipment_get_shipment_label_carriers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_order_no** | **str**| The merchant&#39;s order reference. | 
 **merchant_shipment_label_carrier_request** | [**MerchantShipmentLabelCarrierRequest**](MerchantShipmentLabelCarrierRequest.md)| The parcel information | [optional] 

### Return type

[**CollectionOfMerchantShipmentLabelCarrierResponse**](CollectionOfMerchantShipmentLabelCarrierResponse.md)

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

# **shipment_index**
> CollectionOfMerchantShipmentResponse shipment_index(merchant_shipment_nos=merchant_shipment_nos, merchant_order_nos=merchant_order_nos, method=method, shipped_from_country_codes=shipped_from_country_codes, from_shipment_date=from_shipment_date, to_shipment_date=to_shipment_date, from_create_date=from_create_date, to_create_date=to_create_date, from_update_date=from_update_date, to_update_date=to_update_date, fulfillment_type=fulfillment_type, channel_shipment_nos=channel_shipment_nos, channel_order_nos=channel_order_nos, page=page)

Gets shipments by filter

Gets the shipments based on the available filters.<br />Shipments are listed in chronological order, from old to new.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.collection_of_merchant_shipment_response import CollectionOfMerchantShipmentResponse
from openapi_client.models.shipment_fulfillment_type import ShipmentFulfillmentType
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
    api_instance = openapi_client.ShipmentApi(api_client)
    merchant_shipment_nos = ['merchant_shipment_nos_example'] # List[str] | Filter on the unique references (ids) as used by the merchant. (optional)
    merchant_order_nos = ['merchant_order_nos_example'] # List[str] | Filter on the unique references (ids) of order as used by the merchant. (optional)
    method = 'method_example' # str | Filter on the shipping method. (optional)
    shipped_from_country_codes = ['shipped_from_country_codes_example'] # List[str] | 2-digit Country code (optional)
    from_shipment_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the shipment date, starting from this date. This date is inclusive. (optional)
    to_shipment_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the shipment date, until this date. This date is exclusive. (optional)
    from_create_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the create date of the shipment in ChannelEngine, starting from this date. This date is inclusive. (optional)
    to_create_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the create date of the shipment in ChannelEngine, until this date. This date is exclusive. (optional)
    from_update_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the update date of the shipment in ChannelEngine, starting from this date. This date is inclusive. (optional)
    to_update_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the update date of the shipment in ChannelEngine, until this date. This date is exclusive. (optional)
    fulfillment_type = openapi_client.ShipmentFulfillmentType() # ShipmentFulfillmentType | Filter on the fulfillment type of the shipment. (optional)
    channel_shipment_nos = ['channel_shipment_nos_example'] # List[str] | Filter on the unique references (ids) as used by the channel. (optional)
    channel_order_nos = ['channel_order_nos_example'] # List[str] | Filter on the unique references (ids) of order as used by the channel. (optional)
    page = 56 # int | The page to filter on. Starts at 1. (optional)

    try:
        # Gets shipments by filter
        api_response = api_instance.shipment_index(merchant_shipment_nos=merchant_shipment_nos, merchant_order_nos=merchant_order_nos, method=method, shipped_from_country_codes=shipped_from_country_codes, from_shipment_date=from_shipment_date, to_shipment_date=to_shipment_date, from_create_date=from_create_date, to_create_date=to_create_date, from_update_date=from_update_date, to_update_date=to_update_date, fulfillment_type=fulfillment_type, channel_shipment_nos=channel_shipment_nos, channel_order_nos=channel_order_nos, page=page)
        print("The response of ShipmentApi->shipment_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->shipment_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_shipment_nos** | [**List[str]**](str.md)| Filter on the unique references (ids) as used by the merchant. | [optional] 
 **merchant_order_nos** | [**List[str]**](str.md)| Filter on the unique references (ids) of order as used by the merchant. | [optional] 
 **method** | **str**| Filter on the shipping method. | [optional] 
 **shipped_from_country_codes** | [**List[str]**](str.md)| 2-digit Country code | [optional] 
 **from_shipment_date** | **datetime**| Filter on the shipment date, starting from this date. This date is inclusive. | [optional] 
 **to_shipment_date** | **datetime**| Filter on the shipment date, until this date. This date is exclusive. | [optional] 
 **from_create_date** | **datetime**| Filter on the create date of the shipment in ChannelEngine, starting from this date. This date is inclusive. | [optional] 
 **to_create_date** | **datetime**| Filter on the create date of the shipment in ChannelEngine, until this date. This date is exclusive. | [optional] 
 **from_update_date** | **datetime**| Filter on the update date of the shipment in ChannelEngine, starting from this date. This date is inclusive. | [optional] 
 **to_update_date** | **datetime**| Filter on the update date of the shipment in ChannelEngine, until this date. This date is exclusive. | [optional] 
 **fulfillment_type** | [**ShipmentFulfillmentType**](.md)| Filter on the fulfillment type of the shipment. | [optional] 
 **channel_shipment_nos** | [**List[str]**](str.md)| Filter on the unique references (ids) as used by the channel. | [optional] 
 **channel_order_nos** | [**List[str]**](str.md)| Filter on the unique references (ids) of order as used by the channel. | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantShipmentResponse**](CollectionOfMerchantShipmentResponse.md)

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

# **shipment_shipping_label**
> bytearray shipment_shipping_label(merchant_shipment_no)

Gets a shipping label

 Downloads the shipping label for the shipment.<br /> <br /> **NB:** it may take some time between the creation of the shipment and the availability of the label.<br />A \"404 not found\" error might indicate that the label is not available yet.

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
    api_instance = openapi_client.ShipmentApi(api_client)
    merchant_shipment_no = 'merchant_shipment_no_example' # str | The unique shipment reference as used by the merchant.

    try:
        # Gets a shipping label
        api_response = api_instance.shipment_shipping_label(merchant_shipment_no)
        print("The response of ShipmentApi->shipment_shipping_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->shipment_shipping_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_shipment_no** | **str**| The unique shipment reference as used by the merchant. | 

### Return type

**bytearray**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.shippingLabel, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | shippingLabel |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_update**
> ApiResponse shipment_update(merchant_shipment_no, merchant_shipment_tracking_request=merchant_shipment_tracking_request)

Updates a shipment

Updates an existing shipment with tracking information and shipping method.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.merchant_shipment_tracking_request import MerchantShipmentTrackingRequest
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
    api_instance = openapi_client.ShipmentApi(api_client)
    merchant_shipment_no = 'merchant_shipment_no_example' # str | The merchant's shipment reference.
    merchant_shipment_tracking_request = openapi_client.MerchantShipmentTrackingRequest() # MerchantShipmentTrackingRequest | The updated tracking information. (optional)

    try:
        # Updates a shipment
        api_response = api_instance.shipment_update(merchant_shipment_no, merchant_shipment_tracking_request=merchant_shipment_tracking_request)
        print("The response of ShipmentApi->shipment_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->shipment_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_shipment_no** | **str**| The merchant&#39;s shipment reference. | 
 **merchant_shipment_tracking_request** | [**MerchantShipmentTrackingRequest**](MerchantShipmentTrackingRequest.md)| The updated tracking information. | [optional] 

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

