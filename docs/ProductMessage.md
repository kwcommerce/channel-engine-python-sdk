# ProductMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**key_reference** | **str** |  | [optional] 
**warnings** | **List[str]** |  | [optional] 
**errors** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.product_message import ProductMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ProductMessage from a JSON string
product_message_instance = ProductMessage.from_json(json)
# print the JSON string representation of the object
print(ProductMessage.to_json())

# convert the object into a dict
product_message_dict = product_message_instance.to_dict()
# create an instance of ProductMessage from a dict
product_message_from_dict = ProductMessage.from_dict(product_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


