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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.report_type import ReportType
from openapi_client.models.settlement_custom_json_mapper import SettlementCustomJsonMapper
from typing import Optional, Set
from typing_extensions import Self

class MerchantCreateSettlementsReportRequest(BaseModel):
    """
    MerchantCreateSettlementsReportRequest
    """ # noqa: E501
    settlement_ids: List[StrictInt] = Field(alias="SettlementIds")
    type: ReportType = Field(alias="Type")
    custom_json_mapper: Optional[SettlementCustomJsonMapper] = Field(default=None, alias="CustomJsonMapper")
    channel_references_by_channel_id: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, alias="ChannelReferencesByChannelId")
    __properties: ClassVar[List[str]] = ["SettlementIds", "Type", "CustomJsonMapper", "ChannelReferencesByChannelId"]

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
        """Create an instance of MerchantCreateSettlementsReportRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of custom_json_mapper
        if self.custom_json_mapper:
            _dict['CustomJsonMapper'] = self.custom_json_mapper.to_dict()
        # set to None if channel_references_by_channel_id (nullable) is None
        # and model_fields_set contains the field
        if self.channel_references_by_channel_id is None and "channel_references_by_channel_id" in self.model_fields_set:
            _dict['ChannelReferencesByChannelId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MerchantCreateSettlementsReportRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "SettlementIds": obj.get("SettlementIds"),
            "Type": obj.get("Type"),
            "CustomJsonMapper": SettlementCustomJsonMapper.from_dict(obj["CustomJsonMapper"]) if obj.get("CustomJsonMapper") is not None else None,
            "ChannelReferencesByChannelId": obj.get("ChannelReferencesByChannelId")
        })
        return _obj


