# openapi_client.ProductAttributeGroupApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_attribute_group_add_product_extra_data**](ProductAttributeGroupApi.md#product_attribute_group_add_product_extra_data) | **PUT** /v2/product-attribute-group/{groupName}/add | Adds custom attributes to a group
[**product_attribute_group_create**](ProductAttributeGroupApi.md#product_attribute_group_create) | **POST** /v2/product-attribute-group | Creates a custom attribute group
[**product_attribute_group_delete**](ProductAttributeGroupApi.md#product_attribute_group_delete) | **DELETE** /v2/product-attribute-group/{groupName} | Deletes a custom attribute group
[**product_attribute_group_get_by_filter**](ProductAttributeGroupApi.md#product_attribute_group_get_by_filter) | **GET** /v2/product-attribute-group | Gets custom attribute groups
[**product_attribute_group_get_with_channels_by_filter**](ProductAttributeGroupApi.md#product_attribute_group_get_with_channels_by_filter) | **GET** /v2/product-attribute-group/linked-channels | Gets custom attribute groups and linked marketplaces
[**product_attribute_group_remove_product_extra_data**](ProductAttributeGroupApi.md#product_attribute_group_remove_product_extra_data) | **PUT** /v2/product-attribute-group/{groupName}/remove | Deletes custom attributes from a group
[**product_attribute_group_rename_product_attribute_group**](ProductAttributeGroupApi.md#product_attribute_group_rename_product_attribute_group) | **POST** /v2/product-attribute-group/rename | Renames custom attribute groups


# **product_attribute_group_add_product_extra_data**
> ApiResponse product_attribute_group_add_product_extra_data(group_name, add_product_extra_data_requests=add_product_extra_data_requests)

Adds custom attributes to a group

Adds the provided custom attributes (a.k.a. extra data keys) to the custom attribute group.<br />**NB:** you can only add existing custom attributes to a group.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.add_product_extra_data_requests import AddProductExtraDataRequests
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
    api_instance = openapi_client.ProductAttributeGroupApi(api_client)
    group_name = 'group_name_example' # str | The group name of the product attribute group you wish to add product extra data.
    add_product_extra_data_requests = openapi_client.AddProductExtraDataRequests() # AddProductExtraDataRequests | Product extra data keys to be added. (optional)

    try:
        # Adds custom attributes to a group
        api_response = api_instance.product_attribute_group_add_product_extra_data(group_name, add_product_extra_data_requests=add_product_extra_data_requests)
        print("The response of ProductAttributeGroupApi->product_attribute_group_add_product_extra_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAttributeGroupApi->product_attribute_group_add_product_extra_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name of the product attribute group you wish to add product extra data. | 
 **add_product_extra_data_requests** | [**AddProductExtraDataRequests**](AddProductExtraDataRequests.md)| Product extra data keys to be added. | [optional] 

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

# **product_attribute_group_create**
> ApiResponse product_attribute_group_create(product_attribute_group_request)

Creates a custom attribute group

Creates a custom attribute group based on the set of custom attributes (a.k.a. extra data keys).

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.product_attribute_group_request import ProductAttributeGroupRequest
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
    api_instance = openapi_client.ProductAttributeGroupApi(api_client)
    product_attribute_group_request = [openapi_client.ProductAttributeGroupRequest()] # List[ProductAttributeGroupRequest] | Collection of product attribute groups with linked product extra data keys.

    try:
        # Creates a custom attribute group
        api_response = api_instance.product_attribute_group_create(product_attribute_group_request)
        print("The response of ProductAttributeGroupApi->product_attribute_group_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAttributeGroupApi->product_attribute_group_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_attribute_group_request** | [**List[ProductAttributeGroupRequest]**](ProductAttributeGroupRequest.md)| Collection of product attribute groups with linked product extra data keys. | 

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

# **product_attribute_group_delete**
> ApiResponse product_attribute_group_delete(group_name)

Deletes a custom attribute group

Deletes the custom attribute group based on the **Group name** provided.<br />**NB:** you can only delete a custom attribute group that does not have any markeplaces (a.k.a. channels) linked to it.

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
    api_instance = openapi_client.ProductAttributeGroupApi(api_client)
    group_name = 'group_name_example' # str | The group name of the product attribute group you wish to delete.

    try:
        # Deletes a custom attribute group
        api_response = api_instance.product_attribute_group_delete(group_name)
        print("The response of ProductAttributeGroupApi->product_attribute_group_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAttributeGroupApi->product_attribute_group_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name of the product attribute group you wish to delete. | 

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
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_attribute_group_get_by_filter**
> CollectionOfMerchantProductAttributeGroupWithProductExtraDataResponse product_attribute_group_get_by_filter(group_names=group_names, page=page)

Gets custom attribute groups

Gets the custom attribute groups based on the **Group name** provided.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.collection_of_merchant_product_attribute_group_with_product_extra_data_response import CollectionOfMerchantProductAttributeGroupWithProductExtraDataResponse
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
    api_instance = openapi_client.ProductAttributeGroupApi(api_client)
    group_names = ['group_names_example'] # List[str] |  (optional)
    page = 56 # int | The page to filter on. Starts at 1. (optional)

    try:
        # Gets custom attribute groups
        api_response = api_instance.product_attribute_group_get_by_filter(group_names=group_names, page=page)
        print("The response of ProductAttributeGroupApi->product_attribute_group_get_by_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAttributeGroupApi->product_attribute_group_get_by_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_names** | [**List[str]**](str.md)|  | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantProductAttributeGroupWithProductExtraDataResponse**](CollectionOfMerchantProductAttributeGroupWithProductExtraDataResponse.md)

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

# **product_attribute_group_get_with_channels_by_filter**
> CollectionOfMerchantProductAttributeGroupWithLinkedChannelsResponse product_attribute_group_get_with_channels_by_filter(group_names=group_names, page=page)

Gets custom attribute groups and linked marketplaces

Gets all custom attribute groups and marketplaces (a.k.a. channels) linked to them.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.collection_of_merchant_product_attribute_group_with_linked_channels_response import CollectionOfMerchantProductAttributeGroupWithLinkedChannelsResponse
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
    api_instance = openapi_client.ProductAttributeGroupApi(api_client)
    group_names = ['group_names_example'] # List[str] |  (optional)
    page = 56 # int | The page to filter on. Starts at 1. (optional)

    try:
        # Gets custom attribute groups and linked marketplaces
        api_response = api_instance.product_attribute_group_get_with_channels_by_filter(group_names=group_names, page=page)
        print("The response of ProductAttributeGroupApi->product_attribute_group_get_with_channels_by_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAttributeGroupApi->product_attribute_group_get_with_channels_by_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_names** | [**List[str]**](str.md)|  | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantProductAttributeGroupWithLinkedChannelsResponse**](CollectionOfMerchantProductAttributeGroupWithLinkedChannelsResponse.md)

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

# **product_attribute_group_remove_product_extra_data**
> ApiResponse product_attribute_group_remove_product_extra_data(group_name, remove_product_extra_data_requests=remove_product_extra_data_requests)

Deletes custom attributes from a group

Removes the custom attributes (a.k.a. extra data keys) from the custom attribute group.<br />**NB:** you can only remove existing custom attributes from a group.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.remove_product_extra_data_requests import RemoveProductExtraDataRequests
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
    api_instance = openapi_client.ProductAttributeGroupApi(api_client)
    group_name = 'group_name_example' # str | The group name of the product attribute group you wish to remove product extra data.
    remove_product_extra_data_requests = openapi_client.RemoveProductExtraDataRequests() # RemoveProductExtraDataRequests | Product extra data keys to be removed. (optional)

    try:
        # Deletes custom attributes from a group
        api_response = api_instance.product_attribute_group_remove_product_extra_data(group_name, remove_product_extra_data_requests=remove_product_extra_data_requests)
        print("The response of ProductAttributeGroupApi->product_attribute_group_remove_product_extra_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAttributeGroupApi->product_attribute_group_remove_product_extra_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name of the product attribute group you wish to remove product extra data. | 
 **remove_product_extra_data_requests** | [**RemoveProductExtraDataRequests**](RemoveProductExtraDataRequests.md)| Product extra data keys to be removed. | [optional] 

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

# **product_attribute_group_rename_product_attribute_group**
> ApiResponse product_attribute_group_rename_product_attribute_group(rename_product_attribute_group_requests=rename_product_attribute_group_requests)

Renames custom attribute groups

Renames the custom attribute groups.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.rename_product_attribute_group_requests import RenameProductAttributeGroupRequests
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
    api_instance = openapi_client.ProductAttributeGroupApi(api_client)
    rename_product_attribute_group_requests = [openapi_client.RenameProductAttributeGroupRequests()] # List[RenameProductAttributeGroupRequests] | List of old and new product attribute group names. (optional)

    try:
        # Renames custom attribute groups
        api_response = api_instance.product_attribute_group_rename_product_attribute_group(rename_product_attribute_group_requests=rename_product_attribute_group_requests)
        print("The response of ProductAttributeGroupApi->product_attribute_group_rename_product_attribute_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAttributeGroupApi->product_attribute_group_rename_product_attribute_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rename_product_attribute_group_requests** | [**List[RenameProductAttributeGroupRequests]**](RenameProductAttributeGroupRequests.md)| List of old and new product attribute group names. | [optional] 

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

