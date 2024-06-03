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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class MerchantProductBundlePartResponse(BaseModel):
    """
    MerchantProductBundlePartResponse
    """ # noqa: E501
    merchant_product_no: Optional[StrictStr] = Field(default=None, alias="MerchantProductNo")
    ean: Optional[StrictStr] = Field(default=None, alias="Ean")
    name: Optional[StrictStr] = Field(default=None, alias="Name")
    quantity: Optional[StrictInt] = Field(default=None, alias="Quantity")
    price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Price")
    __properties: ClassVar[List[str]] = ["MerchantProductNo", "Ean", "Name", "Quantity", "Price"]

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
        """Create an instance of MerchantProductBundlePartResponse from a JSON string"""
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
        # set to None if merchant_product_no (nullable) is None
        # and model_fields_set contains the field
        if self.merchant_product_no is None and "merchant_product_no" in self.model_fields_set:
            _dict['MerchantProductNo'] = None

        # set to None if ean (nullable) is None
        # and model_fields_set contains the field
        if self.ean is None and "ean" in self.model_fields_set:
            _dict['Ean'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['Name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MerchantProductBundlePartResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "MerchantProductNo": obj.get("MerchantProductNo"),
            "Ean": obj.get("Ean"),
            "Name": obj.get("Name"),
            "Quantity": obj.get("Quantity"),
            "Price": obj.get("Price")
        })
        return _obj


