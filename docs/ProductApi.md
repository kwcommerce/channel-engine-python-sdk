# openapi_client.ProductApi

All URIs are relative to *https://demo.channelengine.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_bulk_delete**](ProductApi.md#product_bulk_delete) | **POST** /v2/products/bulkdelete | Deletes products
[**product_bulk_patch**](ProductApi.md#product_bulk_patch) | **PATCH** /v2/products | Updates products attributes
[**product_bulk_patch_extra_data_items**](ProductApi.md#product_bulk_patch_extra_data_items) | **PATCH** /v2/products/extra-data/bulk | Adds, updates, or deletes custom attributes
[**product_create**](ProductApi.md#product_create) | **POST** /v2/products | Updates or creates products
[**product_delete**](ProductApi.md#product_delete) | **DELETE** /v2/products/{merchantProductNo} | Deletes a product
[**product_freeze**](ProductApi.md#product_freeze) | **POST** /v2/products/freeze | Updates selected products and sets them either to frozen or not-frozen status.
[**product_get_by_filter**](ProductApi.md#product_get_by_filter) | **GET** /v2/products | Gets products
[**product_get_by_merchant_product_no**](ProductApi.md#product_get_by_merchant_product_no) | **GET** /v2/products/{merchantProductNo} | Gets a product
[**product_patch**](ProductApi.md#product_patch) | **PATCH** /v2/products/{merchantProductNo} | Updates product attributes
[**product_patch_extra_data_items**](ProductApi.md#product_patch_extra_data_items) | **PATCH** /v2/products/extra-data | Adds, updates, or deletes a custom attribute


# **product_bulk_delete**
> ApiResponse product_bulk_delete(request_body)

Deletes products

Deletes a products based on the **Merchant product number**.<br /> <br />**NB:** ChannelEngine deactivates but does not delete the products entirely, as they might be still referenced in orders.<br />Therefore, the references used for these products cannot be reused.

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
    api_instance = openapi_client.ProductApi(api_client)
    request_body = ['request_body_example'] # List[str] | The list of MerchantProductNo of the products you wish to delete.

    try:
        # Deletes products
        api_response = api_instance.product_bulk_delete(request_body)
        print("The response of ProductApi->product_bulk_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_bulk_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| The list of MerchantProductNo of the products you wish to delete. | 

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
**200** | **Message** can be **\&quot;Items successfully deleted\&quot;** or in case of validations **\&quot;Items successfully deleted. Warning:...\&quot;** |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_bulk_patch**
> SingleOfProductCreationResult product_bulk_patch(patch_merchant_product_dto=patch_merchant_product_dto)

Updates products attributes

Updates specific attributes of product data. You can update single or multiple attributes for one or multiple products.<br />You can also add custom attributes via this endpoint. The format of this endpoint is JSON Patch.<br />Products are updated for the fields listed in the array **PropertiesToUpdate**:<br />[name, <br />description, <br />details, <br />brand, <br />size, <br />color, <br />ean, <br />groupno **or** ParentMerchantProductNo, <br />groupno2 **or** ParentMerchantProductNo2, <br />type, <br />merchantproductno,<br />vendorproductno, <br />stock, <br />price, <br />listprice **or** MSRP, <br />purchaseprice, <br />minprice, <br />maxprice, <br />discountrate, <br />vatrate, <br />margin, <br />shippingcost, <br />shippingtime, <br />url, <br />imageurl, <br />extraimageurl1, <br />extraimageurl2, <br />extraimageurl3, <br />extraimageurl4, <br />extraimageurl5, <br />extraimageurl6, <br />extraimageurl7, <br />extraimageurl8, <br />extraimageurl9, <br />categoryid,<br />vatratetype]<br /> <br />Sample request:<br /><pre><br />PATCH /v2/products<br />{<br /> \"PropertiesToUpdate\": [<br /> \"name\",<br /> \"description\"<br /> ],<br /> \"MerchantProductRequestModels\": [<br /> {<br /> \"MerchantProductNo\": \"testMerchantProductNo\",<br /> \"Name\": \"testName\",<br /> \"Description\": \"testDescription\",<br /> },<br /> {<br /> \"MerchantProductNo\": \"testMerchantProductNo2\",<br /> \"Name\": \"testName3\",<br /> \"Description\": \"testDescription1\",<br /> }<br /> ]<br />}<br /></pre>

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.patch_merchant_product_dto import PatchMerchantProductDto
from openapi_client.models.single_of_product_creation_result import SingleOfProductCreationResult
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
    api_instance = openapi_client.ProductApi(api_client)
    patch_merchant_product_dto = openapi_client.PatchMerchantProductDto() # PatchMerchantProductDto | 1) PropertiesToUpdate: Fields to update<br />2) MerchantProductRequestModels: Products to be updated (optional)

    try:
        # Updates products attributes
        api_response = api_instance.product_bulk_patch(patch_merchant_product_dto=patch_merchant_product_dto)
        print("The response of ProductApi->product_bulk_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_bulk_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_merchant_product_dto** | [**PatchMerchantProductDto**](PatchMerchantProductDto.md)| 1) PropertiesToUpdate: Fields to update&lt;br /&gt;2) MerchantProductRequestModels: Products to be updated | [optional] 

### Return type

[**SingleOfProductCreationResult**](SingleOfProductCreationResult.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_bulk_patch_extra_data_items**
> SingleOfProductCreationResult product_bulk_patch_extra_data_items(merchant_product_extra_data_request=merchant_product_extra_data_request)

Adds, updates, or deletes custom attributes

Adds, updates, or deletes the custom attributes (a.k.a. extra data keys) for multiple products.<br />You can update single or multiple attributes for one or multiple products. The format of this endpoint is [JSON Patch](http://jsonpatch.com/).<br /><br />**NB:** the **Merchant product number** must be unique.<br /><br />Sample request:<br /><pre><br />PATCH /v2/products/extra-data/bulk<br />[<br /> {<br /> \"MerchantProductNo\": \"{merchantProductNo}\",<br /> \"Operations\": [<br /> {<br /> \"Op\": \"add\",<br /> \"Key\": \"{Key}\",<br /> \"Value\": \"{Value}\"<br /> }<br /> ]<br /> },<br /> {<br /> \"MerchantProductNo\": \"{merchantProductNo}\",<br /> \"Operations\": [<br /> {<br /> \"Op\": \"replace\",<br /> \"Key\": \"{Key}\",<br /> \"Value\": \"{Value}\"<br /> },<br /> {<br /> \"Op\": \"add\",<br /> \"Key\": \"{Key}\",<br /> \"Value\": \"{Value}\"<br /> }<br /> ]<br /> },<br /> {<br /> \"MerchantProductNo\": \"{merchantProductNo}\",<br /> \"Operations\": [<br /> {<br /> \"Op\": \"remove\",<br /> \"Key\": \"{Key}\",<br /> \"Value\": \"{Value}\"<br /> }<br /> ]<br /> }<br /> ]<br /></pre>

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.merchant_product_extra_data_request import MerchantProductExtraDataRequest
from openapi_client.models.single_of_product_creation_result import SingleOfProductCreationResult
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
    api_instance = openapi_client.ProductApi(api_client)
    merchant_product_extra_data_request = [openapi_client.MerchantProductExtraDataRequest()] # List[MerchantProductExtraDataRequest] |  (optional)

    try:
        # Adds, updates, or deletes custom attributes
        api_response = api_instance.product_bulk_patch_extra_data_items(merchant_product_extra_data_request=merchant_product_extra_data_request)
        print("The response of ProductApi->product_bulk_patch_extra_data_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_bulk_patch_extra_data_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_product_extra_data_request** | [**List[MerchantProductExtraDataRequest]**](MerchantProductExtraDataRequest.md)|  | [optional] 

### Return type

[**SingleOfProductCreationResult**](SingleOfProductCreationResult.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_create**
> SingleOfProductCreationResult product_create(merchant_product_request, ignore_stock=ignore_stock, ignore_price=ignore_price)

Updates or creates products

Updates or creates products. The endpoint is purge and replace.<br />If you do not include an attribute, it is overwritten with null.<br />Extra data arrays are not effected by purge and replace, and remain unchanged.<br />To exclude stock from the update, set the **Ignore stock** attribute to **true**.<br />To exclude price from the update, set the **Ignore price** attribute to **true**.<br /><br />**NB:** the **Merchant product number** must be unique.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.merchant_product_request import MerchantProductRequest
from openapi_client.models.single_of_product_creation_result import SingleOfProductCreationResult
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
    api_instance = openapi_client.ProductApi(api_client)
    merchant_product_request = [openapi_client.MerchantProductRequest()] # List[MerchantProductRequest] | 
    ignore_stock = False # bool |  (optional) (default to False)
    ignore_price = False # bool |  (optional) (default to False)

    try:
        # Updates or creates products
        api_response = api_instance.product_create(merchant_product_request, ignore_stock=ignore_stock, ignore_price=ignore_price)
        print("The response of ProductApi->product_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_product_request** | [**List[MerchantProductRequest]**](MerchantProductRequest.md)|  | 
 **ignore_stock** | **bool**|  | [optional] [default to False]
 **ignore_price** | **bool**|  | [optional] [default to False]

### Return type

[**SingleOfProductCreationResult**](SingleOfProductCreationResult.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If products don&#39;t pass validations then **ProductMessages** in &#39;Content&#39; are filled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_delete**
> ApiResponse product_delete(merchant_product_no)

Deletes a product

Deletes a product based on the **Merchant product number**.<br /> <br />**NB:** ChannelEngine deactivates but does not delete the product entirely, as it might be still referenced in orders.<br />Therefore, the references used for this product cannot be reused.

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
    api_instance = openapi_client.ProductApi(api_client)
    merchant_product_no = 'merchant_product_no_example' # str | The MerchantProductNo of the product you wish to delete.

    try:
        # Deletes a product
        api_response = api_instance.product_delete(merchant_product_no)
        print("The response of ProductApi->product_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_product_no** | **str**| The MerchantProductNo of the product you wish to delete. | 

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

# **product_freeze**
> SingleOfApiResponse product_freeze(freeze_product_request=freeze_product_request)

Updates selected products and sets them either to frozen or not-frozen status.

Changes state of products by updating it with FREEZE or UNFREEZE state.<br />All fields are required.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.freeze_product_request import FreezeProductRequest
from openapi_client.models.single_of_api_response import SingleOfApiResponse
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
    api_instance = openapi_client.ProductApi(api_client)
    freeze_product_request = [openapi_client.FreezeProductRequest()] # List[FreezeProductRequest] |  (optional)

    try:
        # Updates selected products and sets them either to frozen or not-frozen status.
        api_response = api_instance.product_freeze(freeze_product_request=freeze_product_request)
        print("The response of ProductApi->product_freeze:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_freeze: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **freeze_product_request** | [**List[FreezeProductRequest]**](FreezeProductRequest.md)|  | [optional] 

### Return type

[**SingleOfApiResponse**](SingleOfApiResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_get_by_filter**
> CollectionOfMerchantProductResponse product_get_by_filter(search=search, ean_list=ean_list, merchant_product_no_list=merchant_product_no_list, page=page)

Gets products

Retrieve all products. Apply available filters to narrow down your search.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.collection_of_merchant_product_response import CollectionOfMerchantProductResponse
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
    api_instance = openapi_client.ProductApi(api_client)
    search = 'search_example' # str | Search product(s) by Name, MerchantProductNo, Ean or Brand<br />This search is applied to the result after applying the other filters. (optional)
    ean_list = ['ean_list_example'] # List[str] | Search products by submitting a list of EAN's. (optional)
    merchant_product_no_list = ['merchant_product_no_list_example'] # List[str] | Search products by submitting a list of MerchantProductNo's. (optional)
    page = 56 # int | The page to filter on. Starts at 1. (optional)

    try:
        # Gets products
        api_response = api_instance.product_get_by_filter(search=search, ean_list=ean_list, merchant_product_no_list=merchant_product_no_list, page=page)
        print("The response of ProductApi->product_get_by_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_get_by_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search product(s) by Name, MerchantProductNo, Ean or Brand&lt;br /&gt;This search is applied to the result after applying the other filters. | [optional] 
 **ean_list** | [**List[str]**](str.md)| Search products by submitting a list of EAN&#39;s. | [optional] 
 **merchant_product_no_list** | [**List[str]**](str.md)| Search products by submitting a list of MerchantProductNo&#39;s. | [optional] 
 **page** | **int**| The page to filter on. Starts at 1. | [optional] 

### Return type

[**CollectionOfMerchantProductResponse**](CollectionOfMerchantProductResponse.md)

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

# **product_get_by_merchant_product_no**
> SingleOfMerchantProductResponse product_get_by_merchant_product_no(merchant_product_no)

Gets a product

Retrieves a product based on the **Merchant product number**.

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.single_of_merchant_product_response import SingleOfMerchantProductResponse
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
    api_instance = openapi_client.ProductApi(api_client)
    merchant_product_no = 'merchant_product_no_example' # str | The unique product reference used by the Merchant (sku).

    try:
        # Gets a product
        api_response = api_instance.product_get_by_merchant_product_no(merchant_product_no)
        print("The response of ProductApi->product_get_by_merchant_product_no:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_get_by_merchant_product_no: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_product_no** | **str**| The unique product reference used by the Merchant (sku). | 

### Return type

[**SingleOfMerchantProductResponse**](SingleOfMerchantProductResponse.md)

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

# **product_patch**
> SingleOfProductCreationResult product_patch(merchant_product_no, operation=operation)

Updates product attributes

Updates specific attributes of a single product based on the **Merchant product number**. The endpoint uses the [JSON Patch](http://jsonpatch.com/).<br /><br />Sample request:<br /><pre><br /> PATCH /v2/products/{merchantProductNo}<br /> {<br /> \"value\": \"Value\",<br /> \"path\": \"Name\",<br /> \"op\": \"replace\"<br /> }<br /></pre><br />Adding ExtraData:<br /><pre><br /> PATCH /v2/products/{merchantProductNo}<br /> {<br /> \"value\": {\"key\": \"Key1\", \"value\": \"value1\"},<br /> \"path\": \"extraData/0\",<br /> \"op\": \"add\"<br /> }<br /></pre><br />Replacing ExtraData (will replace entire ExtraData collection):<br /><pre><br /> PATCH /v2/products/{merchantProductNo}<br /> {<br /> \"value\": [{\"key\": \"Key1\", \"value\": \"value1\"}],<br /> \"path\": \"extraData\",<br /> \"op\": \"replace\"<br /> }<br /></pre><br />Removing all ExtraData:<br /><pre><br /> PATCH /v2/products/{merchantProductNo}<br /> {<br /> \"path\": \"extraData\",<br /> \"op\": \"replace\"<br /> }<br /></pre><br /> Or:<br /><pre><br /> PATCH /v2/products/{merchantProductNo}<br /> {<br /> \"path\": \"extraData\",<br /> \"op\": \"remove\"<br /> }<br /></pre>

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.operation import Operation
from openapi_client.models.single_of_product_creation_result import SingleOfProductCreationResult
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
    api_instance = openapi_client.ProductApi(api_client)
    merchant_product_no = 'merchant_product_no_example' # str | The MerchantProductNo of the product you wish to patch
    operation = [openapi_client.Operation()] # List[Operation] | The JsonPatchDocument providing the operations you wish to perform on the product. <br /> Value contains the value you wish to set on the property you're updating (used with operations \"add\" and \"replace\").<br /> Path contains the path to the property you're updating (e.g. Description). Every property in the model used for creation an updating can be used.<br /> Op contains the operation you wish to perform (\"add\",\"replace\",\"remove\").<br /> From is only used when using the \"move\" operation. It refers to the source path of the value to be moved. (optional)

    try:
        # Updates product attributes
        api_response = api_instance.product_patch(merchant_product_no, operation=operation)
        print("The response of ProductApi->product_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_product_no** | **str**| The MerchantProductNo of the product you wish to patch | 
 **operation** | [**List[Operation]**](Operation.md)| The JsonPatchDocument providing the operations you wish to perform on the product. &lt;br /&gt; Value contains the value you wish to set on the property you&#39;re updating (used with operations \&quot;add\&quot; and \&quot;replace\&quot;).&lt;br /&gt; Path contains the path to the property you&#39;re updating (e.g. Description). Every property in the model used for creation an updating can be used.&lt;br /&gt; Op contains the operation you wish to perform (\&quot;add\&quot;,\&quot;replace\&quot;,\&quot;remove\&quot;).&lt;br /&gt; From is only used when using the \&quot;move\&quot; operation. It refers to the source path of the value to be moved. | [optional] 

### Return type

[**SingleOfProductCreationResult**](SingleOfProductCreationResult.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_patch_extra_data_items**
> SingleOfProductCreationResult product_patch_extra_data_items(merchant_product_extra_data_request=merchant_product_extra_data_request)

Adds, updates, or deletes a custom attribute

Adds, updates, or deletes the specific custom attribute (a.k.a. extra data key) for a single product.<br />You can update a single attribute for a product. The format of this endpoint is [JSON Patch](http://jsonpatch.com/).<br /><br />**NB:** the **Merchant product number** must be unique.<br /><br />Sample requests:<br /> <br />Adding ExtraData:<br /><pre><br /> PATCH /v2/products/extra-data<br /> {<br /> \"MerchantProductNo\": \"{merchantProductNo}\",<br /> \"Operations\": [<br /> {<br /> \"Op\": \"add\",<br /> \"Key\": \"{Key}\",<br /> \"Value\": \"{Value}\"<br /> }<br /> ]<br /> }<br /> </pre><br />Updating ExtraData:<br /><pre><br /> PATCH /v2/products/extra-data<br /> {<br /> \"MerchantProductNo\": \"{merchantProductNo}\",<br /> \"Operations\": [<br /> {<br /> \"Op\": \"replace\",<br /> \"Key\": \"{Key}\",<br /> \"Value\": \"{Value}\"<br /> }<br /> ]<br /> }<br /></pre><br />Removing ExtraData with key:<br /><pre><br /> PATCH /v2/products/extra-data<br /> {<br /> \"MerchantProductNo\": \"{merchantProductNo}\",<br /> \"Operations\": [<br /> {<br /> \"Op\": \"remove\",<br /> \"Key\": \"{Key}\",<br /> }<br /> ]<br /> }<br /></pre>

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.merchant_product_extra_data_request import MerchantProductExtraDataRequest
from openapi_client.models.single_of_product_creation_result import SingleOfProductCreationResult
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
    api_instance = openapi_client.ProductApi(api_client)
    merchant_product_extra_data_request = openapi_client.MerchantProductExtraDataRequest() # MerchantProductExtraDataRequest |  (optional)

    try:
        # Adds, updates, or deletes a custom attribute
        api_response = api_instance.product_patch_extra_data_items(merchant_product_extra_data_request=merchant_product_extra_data_request)
        print("The response of ProductApi->product_patch_extra_data_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_patch_extra_data_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_product_extra_data_request** | [**MerchantProductExtraDataRequest**](MerchantProductExtraDataRequest.md)|  | [optional] 

### Return type

[**SingleOfProductCreationResult**](SingleOfProductCreationResult.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

