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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.merchant_stock_location_address_request import MerchantStockLocationAddressRequest
from typing import Optional, Set
from typing_extensions import Self

class MerchantStockLocationCreateRequest(BaseModel):
    """
    MerchantStockLocationCreateRequest
    """ # noqa: E501
    name: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="Name")
    is_default: Optional[StrictBool] = Field(default=None, alias="IsDefault")
    fall_back_to_default: Optional[StrictBool] = Field(default=None, description="If false: only use fulfillment by channel, else (also) use merchant fulfillment.", alias="FallBackToDefault")
    address: Optional[MerchantStockLocationAddressRequest] = Field(default=None, alias="Address")
    phone_number: Optional[StrictStr] = Field(default=None, alias="PhoneNumber")
    __properties: ClassVar[List[str]] = ["Name", "IsDefault", "FallBackToDefault", "Address", "PhoneNumber"]

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
        """Create an instance of MerchantStockLocationCreateRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['Address'] = self.address.to_dict()
        # set to None if phone_number (nullable) is None
        # and model_fields_set contains the field
        if self.phone_number is None and "phone_number" in self.model_fields_set:
            _dict['PhoneNumber'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MerchantStockLocationCreateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Name": obj.get("Name"),
            "IsDefault": obj.get("IsDefault"),
            "FallBackToDefault": obj.get("FallBackToDefault"),
            "Address": MerchantStockLocationAddressRequest.from_dict(obj["Address"]) if obj.get("Address") is not None else None,
            "PhoneNumber": obj.get("PhoneNumber")
        })
        return _obj


