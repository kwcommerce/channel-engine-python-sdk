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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.purchase_order_line_unit_of_measure import PurchaseOrderLineUnitOfMeasure
from typing import Optional, Set
from typing_extensions import Self

class ChangePurchaseOrderShipmentLine(BaseModel):
    """
    For Create or Update
    """ # noqa: E501
    channel_order_no: Annotated[str, Field(min_length=0, strict=True, max_length=60)] = Field(description="Channel's identifier of the purchase order", alias="ChannelOrderNo")
    merchant_product_no: Annotated[str, Field(min_length=0, strict=True, max_length=64)] = Field(description="Merchant's identifier of the product.  The combination of ChannelOrderNo + MerchantProductNo identifies the order line this shipment line  ships.", alias="MerchantProductNo")
    quantity_unit_of_measure: Optional[PurchaseOrderLineUnitOfMeasure] = Field(default=None, alias="QuantityUnitOfMeasure")
    quantity: Optional[StrictInt] = Field(default=None, description="The quantity", alias="Quantity")
    quantity_unit_size: Optional[StrictInt] = Field(default=None, description="The case size, when QuantityUnitOfMeasure is 'CASES'. Otherwise, it is 1.", alias="QuantityUnitSize")
    expiry_date: Optional[datetime] = Field(default=None, description="The date that determines the limit of consumption or use of a product.  For perishable products.", alias="ExpiryDate")
    __properties: ClassVar[List[str]] = ["ChannelOrderNo", "MerchantProductNo", "QuantityUnitOfMeasure", "Quantity", "QuantityUnitSize", "ExpiryDate"]

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
        """Create an instance of ChangePurchaseOrderShipmentLine from a JSON string"""
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
        # set to None if quantity_unit_size (nullable) is None
        # and model_fields_set contains the field
        if self.quantity_unit_size is None and "quantity_unit_size" in self.model_fields_set:
            _dict['QuantityUnitSize'] = None

        # set to None if expiry_date (nullable) is None
        # and model_fields_set contains the field
        if self.expiry_date is None and "expiry_date" in self.model_fields_set:
            _dict['ExpiryDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChangePurchaseOrderShipmentLine from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ChannelOrderNo": obj.get("ChannelOrderNo"),
            "MerchantProductNo": obj.get("MerchantProductNo"),
            "QuantityUnitOfMeasure": obj.get("QuantityUnitOfMeasure"),
            "Quantity": obj.get("Quantity"),
            "QuantityUnitSize": obj.get("QuantityUnitSize"),
            "ExpiryDate": obj.get("ExpiryDate")
        })
        return _obj


