# openapi_client.ReportApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**report_create_settlements_report**](ReportApi.md#report_create_settlements_report) | **POST** /v2/reports/settlements | Creates a settlement report
[**report_get_report**](ReportApi.md#report_get_report) | **GET** /v2/reports/{reportId} | Gets a settlement report
[**report_get_status**](ReportApi.md#report_get_status) | **GET** /v2/reports/{reportId}/status | Gets the status of a settlement report


# **report_create_settlements_report**
> MerchantCreateReportResponse report_create_settlements_report(merchant_create_settlements_report_request)

Creates a settlement report

Creates a settlement report based on the **Settlement ID** provided. There are 3 types of reports:<br />**SUMMARY** - a high level financial overview.<br />**DETAILED** - a detailed report containing all transactions.<br />**CUSTOM_JSON** - a report grouped by orders, you can name the csv columns with a JSON file.<br /> <br />All the settlements are automatically acknowledged if that was not already the case.<br />**NB:** depending on the number of transactions within the settlement, it can take a few minutes for the report to be generated.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.merchant_create_report_response import MerchantCreateReportResponse
from openapi_client.models.merchant_create_settlements_report_request import MerchantCreateSettlementsReportRequest
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
    api_instance = openapi_client.ReportApi(api_client)
    merchant_create_settlements_report_request = openapi_client.MerchantCreateSettlementsReportRequest() # MerchantCreateSettlementsReportRequest | To provide settlementIds and type of report SUMMARY or DETAILED.

    try:
        # Creates a settlement report
        api_response = api_instance.report_create_settlements_report(merchant_create_settlements_report_request)
        print("The response of ReportApi->report_create_settlements_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->report_create_settlements_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_create_settlements_report_request** | [**MerchantCreateSettlementsReportRequest**](MerchantCreateSettlementsReportRequest.md)| To provide settlementIds and type of report SUMMARY or DETAILED. | 

### Return type

[**MerchantCreateReportResponse**](MerchantCreateReportResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_get_report**
> bytearray report_get_report(report_id)

Gets a settlement report

Gets a settlement report based on the **Report ID** provided. The generated report is a CSV file with a semicolon (;) as a delimiter.<br />If a field has a comma (,) then it is enclosed in quotes (\"\").

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
    api_instance = openapi_client.ReportApi(api_client)
    report_id = 'report_id_example' # str | 

    try:
        # Gets a settlement report
        api_response = api_instance.report_get_report(report_id)
        print("The response of ReportApi->report_get_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->report_get_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**|  | 

### Return type

**bytearray**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report csv |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_get_status**
> MerchantGetReportStatusResponse report_get_status(report_id)

Gets the status of a settlement report

Returns a report status based on the **Report ID** provided. There are four statuses:<br />**IN_PROGRESS** - the report is still being created.<br />**DONE** - the report has been created.<br />**FAILED** - the report creation failed.<br />**NOT_FOUND** - the Report ID was not found.<br /> <br />**NB:** if the status is **DONE**, the response contains a URL with a download path.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.merchant_get_report_status_response import MerchantGetReportStatusResponse
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
    api_instance = openapi_client.ReportApi(api_client)
    report_id = 'report_id_example' # str | 

    try:
        # Gets the status of a settlement report
        api_response = api_instance.report_get_status(report_id)
        print("The response of ReportApi->report_get_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->report_get_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**|  | 

### Return type

[**MerchantGetReportStatusResponse**](MerchantGetReportStatusResponse.md)

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

