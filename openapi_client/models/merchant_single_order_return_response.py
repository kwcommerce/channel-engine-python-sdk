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
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from openapi_client.models.merchant_single_order_return_line_response import MerchantSingleOrderReturnLineResponse
from openapi_client.models.return_reason import ReturnReason
from openapi_client.models.return_status import ReturnStatus
from typing import Optional, Set
from typing_extensions import Self

class MerchantSingleOrderReturnResponse(BaseModel):
    """
    MerchantSingleOrderReturnResponse
    """ # noqa: E501
    merchant_order_no: Optional[StrictStr] = Field(default=None, description="The unique order reference used by the Merchant.", alias="MerchantOrderNo")
    lines: Optional[List[MerchantSingleOrderReturnLineResponse]] = Field(default=None, alias="Lines")
    created_at: Optional[datetime] = Field(default=None, description="The date at which the return was created in ChannelEngine.", alias="CreatedAt")
    updated_at: Optional[datetime] = Field(default=None, description="The date at which the return was last modified in ChannelEngine.", alias="UpdatedAt")
    merchant_return_no: Optional[StrictStr] = Field(default=None, description="The unique return reference used by the Merchant, will be empty in case of a channel or unacknowledged return.", alias="MerchantReturnNo")
    channel_return_no: Optional[StrictStr] = Field(default=None, description="The unique return reference used by the Channel, will be empty in case of a merchant return.", alias="ChannelReturnNo")
    channel_id: Optional[StrictInt] = Field(default=None, description="The id of the channel.", alias="ChannelId")
    global_channel_id: Optional[StrictInt] = Field(default=None, description="The id of the Global Channel.", alias="GlobalChannelId")
    global_channel_name: Optional[StrictStr] = Field(default=None, description="The name of the Global Channel.", alias="GlobalChannelName")
    status: Optional[ReturnStatus] = Field(default=None, alias="Status")
    id: Optional[StrictInt] = Field(default=None, description="The unique return reference used by ChannelEngine.", alias="Id")
    reason: Optional[ReturnReason] = Field(default=None, alias="Reason")
    customer_comment: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=4001)]] = Field(default=None, description="Optional. Comment of customer on the (reason of) the return.", alias="CustomerComment")
    merchant_comment: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=4001)]] = Field(default=None, description="Optional. Comment of merchant on the return.", alias="MerchantComment")
    refund_incl_vat: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Refund amount incl. VAT.", alias="RefundInclVat")
    refund_excl_vat: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Refund amount excl. VAT.", alias="RefundExclVat")
    return_date: Optional[datetime] = Field(default=None, description="The date at which the return was originally created in the source system (if available).", alias="ReturnDate")
    extra_data: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="Extra data on the return. Each item must have an unqiue key", alias="ExtraData")
    __properties: ClassVar[List[str]] = ["MerchantOrderNo", "Lines", "CreatedAt", "UpdatedAt", "MerchantReturnNo", "ChannelReturnNo", "ChannelId", "GlobalChannelId", "GlobalChannelName", "Status", "Id", "Reason", "CustomerComment", "MerchantComment", "RefundInclVat", "RefundExclVat", "ReturnDate", "ExtraData"]

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
        """Create an instance of MerchantSingleOrderReturnResponse from a JSON string"""
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
        # set to None if merchant_order_no (nullable) is None
        # and model_fields_set contains the field
        if self.merchant_order_no is None and "merchant_order_no" in self.model_fields_set:
            _dict['MerchantOrderNo'] = None

        # set to None if lines (nullable) is None
        # and model_fields_set contains the field
        if self.lines is None and "lines" in self.model_fields_set:
            _dict['Lines'] = None

        # set to None if merchant_return_no (nullable) is None
        # and model_fields_set contains the field
        if self.merchant_return_no is None and "merchant_return_no" in self.model_fields_set:
            _dict['MerchantReturnNo'] = None

        # set to None if channel_return_no (nullable) is None
        # and model_fields_set contains the field
        if self.channel_return_no is None and "channel_return_no" in self.model_fields_set:
            _dict['ChannelReturnNo'] = None

        # set to None if channel_id (nullable) is None
        # and model_fields_set contains the field
        if self.channel_id is None and "channel_id" in self.model_fields_set:
            _dict['ChannelId'] = None

        # set to None if global_channel_id (nullable) is None
        # and model_fields_set contains the field
        if self.global_channel_id is None and "global_channel_id" in self.model_fields_set:
            _dict['GlobalChannelId'] = None

        # set to None if global_channel_name (nullable) is None
        # and model_fields_set contains the field
        if self.global_channel_name is None and "global_channel_name" in self.model_fields_set:
            _dict['GlobalChannelName'] = None

        # set to None if customer_comment (nullable) is None
        # and model_fields_set contains the field
        if self.customer_comment is None and "customer_comment" in self.model_fields_set:
            _dict['CustomerComment'] = None

        # set to None if merchant_comment (nullable) is None
        # and model_fields_set contains the field
        if self.merchant_comment is None and "merchant_comment" in self.model_fields_set:
            _dict['MerchantComment'] = None

        # set to None if return_date (nullable) is None
        # and model_fields_set contains the field
        if self.return_date is None and "return_date" in self.model_fields_set:
            _dict['ReturnDate'] = None

        # set to None if extra_data (nullable) is None
        # and model_fields_set contains the field
        if self.extra_data is None and "extra_data" in self.model_fields_set:
            _dict['ExtraData'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MerchantSingleOrderReturnResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "MerchantOrderNo": obj.get("MerchantOrderNo"),
            "Lines": [MerchantSingleOrderReturnLineResponse.from_dict(_item) for _item in obj["Lines"]] if obj.get("Lines") is not None else None,
            "CreatedAt": obj.get("CreatedAt"),
            "UpdatedAt": obj.get("UpdatedAt"),
            "MerchantReturnNo": obj.get("MerchantReturnNo"),
            "ChannelReturnNo": obj.get("ChannelReturnNo"),
            "ChannelId": obj.get("ChannelId"),
            "GlobalChannelId": obj.get("GlobalChannelId"),
            "GlobalChannelName": obj.get("GlobalChannelName"),
            "Status": obj.get("Status"),
            "Id": obj.get("Id"),
            "Reason": obj.get("Reason"),
            "CustomerComment": obj.get("CustomerComment"),
            "MerchantComment": obj.get("MerchantComment"),
            "RefundInclVat": obj.get("RefundInclVat"),
            "RefundExclVat": obj.get("RefundExclVat"),
            "ReturnDate": obj.get("ReturnDate"),
            "ExtraData": obj.get("ExtraData")
        })
        return _obj


