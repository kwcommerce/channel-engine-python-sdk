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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.purchase_order_acknowledgement_code import PurchaseOrderAcknowledgementCode
from openapi_client.models.purchase_order_rejection_reason import PurchaseOrderRejectionReason
from typing import Optional, Set
from typing_extensions import Self

class MerchantAcknowledgePurchaseOrderLine(BaseModel):
    """
    MerchantAcknowledgePurchaseOrderLine
    """ # noqa: E501
    order_line_identifier: Optional[StrictStr] = Field(default=None, alias="OrderLineIdentifier")
    acknowledgement_code: Optional[PurchaseOrderAcknowledgementCode] = Field(default=None, alias="AcknowledgementCode")
    acknowledged_quantity: Optional[StrictInt] = Field(default=None, alias="AcknowledgedQuantity")
    rejection_reason: Optional[PurchaseOrderRejectionReason] = Field(default=None, alias="RejectionReason")
    scheduled_ship_date: Optional[datetime] = Field(default=None, alias="ScheduledShipDate")
    __properties: ClassVar[List[str]] = ["OrderLineIdentifier", "AcknowledgementCode", "AcknowledgedQuantity", "RejectionReason", "ScheduledShipDate"]

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
        """Create an instance of MerchantAcknowledgePurchaseOrderLine from a JSON string"""
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
        # set to None if order_line_identifier (nullable) is None
        # and model_fields_set contains the field
        if self.order_line_identifier is None and "order_line_identifier" in self.model_fields_set:
            _dict['OrderLineIdentifier'] = None

        # set to None if scheduled_ship_date (nullable) is None
        # and model_fields_set contains the field
        if self.scheduled_ship_date is None and "scheduled_ship_date" in self.model_fields_set:
            _dict['ScheduledShipDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MerchantAcknowledgePurchaseOrderLine from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "OrderLineIdentifier": obj.get("OrderLineIdentifier"),
            "AcknowledgementCode": obj.get("AcknowledgementCode"),
            "AcknowledgedQuantity": obj.get("AcknowledgedQuantity"),
            "RejectionReason": obj.get("RejectionReason"),
            "ScheduledShipDate": obj.get("ScheduledShipDate")
        })
        return _obj


