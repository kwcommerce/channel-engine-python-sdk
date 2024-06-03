# openapi_client.SettlementApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settlement_get_by_filter**](SettlementApi.md#settlement_get_by_filter) | **GET** /v2/settlements | Gets settlements
[**settlement_upload_settlement**](SettlementApi.md#settlement_upload_settlement) | **POST** /v2/settlements/upload | Imports a settlement file.


# **settlement_get_by_filter**
> CollectionOfMerchantSettlementReportsResponse settlement_get_by_filter(un_exported_only=un_exported_only, settlement_ids=settlement_ids, channel_settlement_nos=channel_settlement_nos, channel_ids=channel_ids, from_start_date=from_start_date, to_start_date=to_start_date, from_end_date=from_end_date, to_end_date=to_end_date, from_create_date=from_create_date, to_create_date=to_create_date, from_update_date=from_update_date, to_update_date=to_update_date, page=page)

Gets settlements

Gets the settlements based on the available filters.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.collection_of_merchant_settlement_reports_response import CollectionOfMerchantSettlementReportsResponse
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
    api_instance = openapi_client.SettlementApi(api_client)
    un_exported_only = True # bool | Filter on settlements that have not been exported before. (optional)
    settlement_ids = [56] # List[int] | Filter on settlement IDs. (optional)
    channel_settlement_nos = ['channel_settlement_nos_example'] # List[str] | Filter on channel settlement nos. (optional)
    channel_ids = [56] # List[int] | Filter on channel id list. (optional)
    from_start_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the start date of the settlement in ChannelEngine, until this date. This date is exclusive. (optional)
    to_start_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the start date of the settlement in ChannelEngine, until this date. This date is exclusive. (optional)
    from_end_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the end date of the settlement in ChannelEngine, starting from this date. This date is inclusive. (optional)
    to_end_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the end date of the settlement in ChannelEngine, until this date. This date is exclusive. (optional)
    from_create_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the create date of the settlement in ChannelEngine, until this date. This date is exclusive. (optional)
    to_create_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the create date of the settlement in ChannelEngine, until this date. This date is exclusive. (optional)
    from_update_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the update date of the settlement in ChannelEngine, starting from this date. This date is inclusive. (optional)
    to_update_date = '2013-10-20T19:20:30+01:00' # datetime | Filter on the update date of the settlement in ChannelEngine, until this date. This date is exclusive. (optional)
    page = 56 # int | The page to filter on. Starts at 1. (optional)

    try:
        # Gets settlements
        api_response = api_instance.settlement_get_by_filter(un_exported_only=un_exported_only, settlement_ids=settlement_ids, channel_settlement_nos=channel_settlement_nos, channel_ids=channel_ids, from_start_date=from_start_date, to_start_date=to_start_date, from_end_date=from_end_date, to_end_date=to_end_date, from_create_date=from_create_date, to_create_date=to_create_date, from_update_date=from_update_date, to_update_date=to_update_date, page=page)
        print("The response of SettlementApi->settlement_get_by_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettlementApi->settlement_get_by_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **un_exported_only** | **bool**| Filter on settlements that have not been exported before. | [optional] 
 **settlement_ids** | [**List[int]**](int.md)| Filter on settlement IDs. | [optional] 
 **channel_settlement_nos** | [**List[str]**](str.md)| Filter on channel settlement nos. | [optional] 
 **channel_ids** | [**List[int]**](int.md)| Filter on channel id list. | [optional] 
 **from_start_date** | **datetime**| Filter on the start date of the settlement in ChannelEngine, until this date. This date is exclusive. | [optional] 
 **to_start_date** | **datetime**| Filter on the start date of the settlement in ChannelEngine, until this date. This date is exclusive. | [optional] 
 **from_end_date** | **datetime**| Filter on the end date of the settlement in ChannelEngine, starting from this date. This date is inclusive. | [optional] 
 **to_end_date** | **datetime**| Filter on the end date of the settlement in ChannelEngine, until this date. This date is exclusive. | [optional] 
 **from_create_date** | **datetime**| Filter on the create date of the settlement in ChannelEngine, until this date. This date is exclusive. | [optional] 
 **to_create_date** | **datetime**| Filter on the create date of the settlement in ChannelEngine, until this date. This date is exclusive. | [optional] 
 **from_update_date** | **datetime**| Filter on the update date of the settlement in ChannelEngine, starting from this date. This date is inclusive. | [optional] 
 **to_update_date** | **datetime**| Filter on the update date of the settlement in ChannelEngine, until this date. This date is exclusive. | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantSettlementReportsResponse**](CollectionOfMerchantSettlementReportsResponse.md)

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

# **settlement_upload_settlement**
> ApiResponse settlement_upload_settlement(settlement, channel_id=channel_id)

Imports a settlement file.

Imports a settlement file.

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
    api_instance = openapi_client.SettlementApi(api_client)
    settlement = None # bytearray | Settlement file up to 1 MB with additional data.  Format should be the one that the channel expects.
    channel_id = 56 # int | The channel ID for which the settlement is for. (optional)

    try:
        # Imports a settlement file.
        api_response = api_instance.settlement_upload_settlement(settlement, channel_id=channel_id)
        print("The response of SettlementApi->settlement_upload_settlement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettlementApi->settlement_upload_settlement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement** | **bytearray**| Settlement file up to 1 MB with additional data.  Format should be the one that the channel expects. | 
 **channel_id** | **int**| The channel ID for which the settlement is for. | [optional] 

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
**201** | Created |  -  |
**400** | Bad Request |  -  |
**422** | Client Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

