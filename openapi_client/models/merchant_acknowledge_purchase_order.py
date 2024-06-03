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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.merchant_acknowledge_purchase_order_line import MerchantAcknowledgePurchaseOrderLine
from typing import Optional, Set
from typing_extensions import Self

class MerchantAcknowledgePurchaseOrder(BaseModel):
    """
    MerchantAcknowledgePurchaseOrder
    """ # noqa: E501
    identifier: Optional[StrictStr] = Field(default=None, alias="Identifier")
    merchant_order_no: Optional[StrictStr] = Field(default=None, alias="MerchantOrderNo")
    lines: Optional[List[MerchantAcknowledgePurchaseOrderLine]] = Field(default=None, alias="Lines")
    __properties: ClassVar[List[str]] = ["Identifier", "MerchantOrderNo", "Lines"]

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
        """Create an instance of MerchantAcknowledgePurchaseOrder from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in lines (list)
        _items = []
        if self.lines:
            for _item in self.lines:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Lines'] = _items
        # set to None if identifier (nullable) is None
        # and model_fields_set contains the field
        if self.identifier is None and "identifier" in self.model_fields_set:
            _dict['Identifier'] = None

        # set to None if merchant_order_no (nullable) is None
        # and model_fields_set contains the field
        if self.merchant_order_no is None and "merchant_order_no" in self.model_fields_set:
            _dict['MerchantOrderNo'] = None

        # set to None if lines (nullable) is None
        # and model_fields_set contains the field
        if self.lines is None and "lines" in self.model_fields_set:
            _dict['Lines'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MerchantAcknowledgePurchaseOrder from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Identifier": obj.get("Identifier"),
            "MerchantOrderNo": obj.get("MerchantOrderNo"),
            "Lines": [MerchantAcknowledgePurchaseOrderLine.from_dict(_item) for _item in obj["Lines"]] if obj.get("Lines") is not None else None
        })
        return _obj


