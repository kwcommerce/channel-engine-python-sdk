# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.merchant_product_attribute_group_with_product_extra_data_response import MerchantProductAttributeGroupWithProductExtraDataResponse
from typing import Optional, Set
from typing_extensions import Self

class CollectionOfMerchantProductAttributeGroupWithProductExtraDataResponse(BaseModel):
    """
    CollectionOfMerchantProductAttributeGroupWithProductExtraDataResponse
    """ # noqa: E501
    content: Optional[List[MerchantProductAttributeGroupWithProductExtraDataResponse]] = Field(default=None, alias="Content")
    count: Optional[StrictInt] = Field(default=None, description="The number of items in the current response.", alias="Count")
    total_count: Optional[StrictInt] = Field(default=None, description="The total number of items.", alias="TotalCount")
    items_per_page: Optional[StrictInt] = Field(default=None, description="The number of items per page.", alias="ItemsPerPage")
    status_code: Optional[StrictInt] = Field(default=None, alias="StatusCode")
    request_id: Optional[StrictStr] = Field(default=None, alias="RequestId")
    log_id: Optional[StrictStr] = Field(default=None, alias="LogId")
    success: Optional[StrictBool] = Field(default=None, alias="Success")
    message: Optional[StrictStr] = Field(default=None, alias="Message")
    exception_type: Optional[StrictStr] = Field(default=None, alias="ExceptionType")
    validation_errors: Optional[Dict[str, Optional[List[StrictStr]]]] = Field(default=None, alias="ValidationErrors")
    __properties: ClassVar[List[str]] = ["Content", "Count", "TotalCount", "ItemsPerPage", "StatusCode", "RequestId", "LogId", "Success", "Message", "ExceptionType", "ValidationErrors"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CollectionOfMerchantProductAttributeGroupWithProductExtraDataResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in content (list)
        _items = []
        if self.content:
            for _item in self.content:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Content'] = _items
        # set to None if content (nullable) is None
        # and model_fields_set contains the field
        if self.content is None and "content" in self.model_fields_set:
            _dict['Content'] = None

        # set to None if request_id (nullable) is None
        # and model_fields_set contains the field
        if self.request_id is None and "request_id" in self.model_fields_set:
            _dict['RequestId'] = None

        # set to None if log_id (nullable) is None
        # and model_fields_set contains the field
        if self.log_id is None and "log_id" in self.model_fields_set:
            _dict['LogId'] = None

        # set to None if message (nullable) is None
        # and model_fields_set contains the field
        if self.message is None and "message" in self.model_fields_set:
            _dict['Message'] = None

        # set to None if exception_type (nullable) is None
        # and model_fields_set contains the field
        if self.exception_type is None and "exception_type" in self.model_fields_set:
            _dict['ExceptionType'] = None

        # set to None if validation_errors (nullable) is None
        # and model_fields_set contains the field
        if self.validation_errors is None and "validation_errors" in self.model_fields_set:
            _dict['ValidationErrors'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CollectionOfMerchantProductAttributeGroupWithProductExtraDataResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Content": [MerchantProductAttributeGroupWithProductExtraDataResponse.from_dict(_item) for _item in obj["Content"]] if obj.get("Content") is not None else None,
            "Count": obj.get("Count"),
            "TotalCount": obj.get("TotalCount"),
            "ItemsPerPage": obj.get("ItemsPerPage"),
            "StatusCode": obj.get("StatusCode"),
            "RequestId": obj.get("RequestId"),
            "LogId": obj.get("LogId"),
            "Success": obj.get("Success"),
            "Message": obj.get("Message"),
            "ExceptionType": obj.get("ExceptionType"),
            "ValidationErrors": obj.get("ValidationErrors")
        })
        return _obj


