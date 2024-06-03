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
from typing_extensions import Annotated
from openapi_client.models.merchant_shipment_line_response import MerchantShipmentLineResponse
from typing import Optional, Set
from typing_extensions import Self

class MerchantShipmentResponse(BaseModel):
    """
    MerchantShipmentResponse
    """ # noqa: E501
    merchant_shipment_no: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The unique shipment reference used by the Merchant.", alias="MerchantShipmentNo")
    merchant_order_no: Optional[StrictStr] = Field(default=None, description="The unique order reference used by the Merchant.", alias="MerchantOrderNo")
    channel_shipment_no: Optional[StrictStr] = Field(default=None, description="The unique shipment reference used by the Channel.", alias="ChannelShipmentNo")
    channel_order_no: Optional[StrictStr] = Field(default=None, description="The unique order reference used by the Channel.", alias="ChannelOrderNo")
    channel_id: Optional[StrictInt] = Field(default=None, description="The unique ID of the channel for this specific environment/account.", alias="ChannelId")
    global_channel_id: Optional[StrictInt] = Field(default=None, description="The unique ID of the channel across all of ChannelEngine.", alias="GlobalChannelId")
    lines: Optional[List[MerchantShipmentLineResponse]] = Field(default=None, alias="Lines")
    created_at: Optional[datetime] = Field(default=None, description="The date at which the shipment was created in ChannelEngine.", alias="CreatedAt")
    updated_at: Optional[datetime] = Field(default=None, description="The date at which the shipment was last modified in ChannelEngine.", alias="UpdatedAt")
    extra_data: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="Extra data on the order. Each item must have an unqiue key", alias="ExtraData")
    track_trace_no: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=50)]] = Field(default=None, description="The unique shipping reference used by the Shipping carrier (track&trace number).", alias="TrackTraceNo")
    track_trace_url: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=250)]] = Field(default=None, description="A link to a page of the carrier where the customer can track the shipping of her package.", alias="TrackTraceUrl")
    return_track_trace_no: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=50)]] = Field(default=None, description="The unique return shipping reference that may be used by the Shipping carrier (track & trace number) if the shipment is returned.", alias="ReturnTrackTraceNo")
    method: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=50)]] = Field(default=None, description="Shipment method: the carrier used for shipping the package. E.g. DHL, postNL.", alias="Method")
    shipped_from_country_code: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=3)]] = Field(default=None, description="The code of the country from where the package is being shipped.", alias="ShippedFromCountryCode")
    shipped_from_stock_location_id: Optional[StrictInt] = Field(default=None, description="The id of the stock location where you ship the package from", alias="ShippedFromStockLocationId")
    shipment_date: Optional[datetime] = Field(default=None, description="The date at which the shipment was originally created in the source system (if available).", alias="ShipmentDate")
    __properties: ClassVar[List[str]] = ["MerchantShipmentNo", "MerchantOrderNo", "ChannelShipmentNo", "ChannelOrderNo", "ChannelId", "GlobalChannelId", "Lines", "CreatedAt", "UpdatedAt", "ExtraData", "TrackTraceNo", "TrackTraceUrl", "ReturnTrackTraceNo", "Method", "ShippedFromCountryCode", "ShippedFromStockLocationId", "ShipmentDate"]

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
        """Create an instance of MerchantShipmentResponse from a JSON string"""
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

        # set to None if channel_shipment_no (nullable) is None
        # and model_fields_set contains the field
        if self.channel_shipment_no is None and "channel_shipment_no" in self.model_fields_set:
            _dict['ChannelShipmentNo'] = None

        # set to None if channel_order_no (nullable) is None
        # and model_fields_set contains the field
        if self.channel_order_no is None and "channel_order_no" in self.model_fields_set:
            _dict['ChannelOrderNo'] = None

        # set to None if channel_id (nullable) is None
        # and model_fields_set contains the field
        if self.channel_id is None and "channel_id" in self.model_fields_set:
            _dict['ChannelId'] = None

        # set to None if global_channel_id (nullable) is None
        # and model_fields_set contains the field
        if self.global_channel_id is None and "global_channel_id" in self.model_fields_set:
            _dict['GlobalChannelId'] = None

        # set to None if lines (nullable) is None
        # and model_fields_set contains the field
        if self.lines is None and "lines" in self.model_fields_set:
            _dict['Lines'] = None

        # set to None if extra_data (nullable) is None
        # and model_fields_set contains the field
        if self.extra_data is None and "extra_data" in self.model_fields_set:
            _dict['ExtraData'] = None

        # set to None if track_trace_no (nullable) is None
        # and model_fields_set contains the field
        if self.track_trace_no is None and "track_trace_no" in self.model_fields_set:
            _dict['TrackTraceNo'] = None

        # set to None if track_trace_url (nullable) is None
        # and model_fields_set contains the field
        if self.track_trace_url is None and "track_trace_url" in self.model_fields_set:
            _dict['TrackTraceUrl'] = None

        # set to None if return_track_trace_no (nullable) is None
        # and model_fields_set contains the field
        if self.return_track_trace_no is None and "return_track_trace_no" in self.model_fields_set:
            _dict['ReturnTrackTraceNo'] = None

        # set to None if method (nullable) is None
        # and model_fields_set contains the field
        if self.method is None and "method" in self.model_fields_set:
            _dict['Method'] = None

        # set to None if shipped_from_country_code (nullable) is None
        # and model_fields_set contains the field
        if self.shipped_from_country_code is None and "shipped_from_country_code" in self.model_fields_set:
            _dict['ShippedFromCountryCode'] = None

        # set to None if shipped_from_stock_location_id (nullable) is None
        # and model_fields_set contains the field
        if self.shipped_from_stock_location_id is None and "shipped_from_stock_location_id" in self.model_fields_set:
            _dict['ShippedFromStockLocationId'] = None

        # set to None if shipment_date (nullable) is None
        # and model_fields_set contains the field
        if self.shipment_date is None and "shipment_date" in self.model_fields_set:
            _dict['ShipmentDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MerchantShipmentResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "MerchantShipmentNo": obj.get("MerchantShipmentNo"),
            "MerchantOrderNo": obj.get("MerchantOrderNo"),
            "ChannelShipmentNo": obj.get("ChannelShipmentNo"),
            "ChannelOrderNo": obj.get("ChannelOrderNo"),
            "ChannelId": obj.get("ChannelId"),
            "GlobalChannelId": obj.get("GlobalChannelId"),
            "Lines": [MerchantShipmentLineResponse.from_dict(_item) for _item in obj["Lines"]] if obj.get("Lines") is not None else None,
            "CreatedAt": obj.get("CreatedAt"),
            "UpdatedAt": obj.get("UpdatedAt"),
            "ExtraData": obj.get("ExtraData"),
            "TrackTraceNo": obj.get("TrackTraceNo"),
            "TrackTraceUrl": obj.get("TrackTraceUrl"),
            "ReturnTrackTraceNo": obj.get("ReturnTrackTraceNo"),
            "Method": obj.get("Method"),
            "ShippedFromCountryCode": obj.get("ShippedFromCountryCode"),
            "ShippedFromStockLocationId": obj.get("ShippedFromStockLocationId"),
            "ShipmentDate": obj.get("ShipmentDate")
        })
        return _obj


