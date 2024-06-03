# MerchantInvoiceUploadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_content** | **str** | Data needed to upload an invoice. | 
**invoice_number** | **str** | The invoice number used in the invoice. | 

## Example

```python
from openapi_client.models.merchant_invoice_upload_request import MerchantInvoiceUploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantInvoiceUploadRequest from a JSON string
merchant_invoice_upload_request_instance = MerchantInvoiceUploadRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantInvoiceUploadRequest.to_json())

# convert the object into a dict
merchant_invoice_upload_request_dict = merchant_invoice_upload_request_instance.to_dict()
# create an instance of MerchantInvoiceUploadRequest from a dict
merchant_invoice_upload_request_from_dict = MerchantInvoiceUploadRequest.from_dict(merchant_invoice_upload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


