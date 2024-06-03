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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.notification_type import NotificationType
from typing import Optional, Set
from typing_extensions import Self

class MerchantNotificationResponse(BaseModel):
    """
    MerchantNotificationResponse
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Unique identifier used by ChannelEngine.", alias="Id")
    read: Optional[StrictBool] = Field(default=None, description="Indicating whether the notification is already read using the backoffice.", alias="Read")
    created_at: Optional[datetime] = Field(default=None, description="Get the created date time.", alias="CreatedAt")
    message: Optional[StrictStr] = Field(default=None, alias="Message")
    subject: Optional[StrictStr] = Field(default=None, alias="Subject")
    count: Optional[StrictInt] = Field(default=None, alias="Count")
    type: Optional[NotificationType] = Field(default=None, alias="Type")
    __properties: ClassVar[List[str]] = ["Id", "Read", "CreatedAt", "Message", "Subject", "Count", "Type"]

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
        """Create an instance of MerchantNotificationResponse from a JSON string"""
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
        # set to None if message (nullable) is None
        # and model_fields_set contains the field
        if self.message is None and "message" in self.model_fields_set:
            _dict['Message'] = None

        # set to None if subject (nullable) is None
        # and model_fields_set contains the field
        if self.subject is None and "subject" in self.model_fields_set:
            _dict['Subject'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MerchantNotificationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Id": obj.get("Id"),
            "Read": obj.get("Read"),
            "CreatedAt": obj.get("CreatedAt"),
            "Message": obj.get("Message"),
            "Subject": obj.get("Subject"),
            "Count": obj.get("Count"),
            "Type": obj.get("Type")
        })
        return _obj


