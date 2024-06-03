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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class MerchantStockLocationAddressRequest(BaseModel):
    """
    MerchantStockLocationAddressRequest
    """ # noqa: E501
    country_iso: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="CountryIso")
    street_name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=50)]] = Field(default=None, alias="StreetName")
    zip_code: Optional[StrictStr] = Field(default=None, alias="ZipCode")
    house_nr: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=50)]] = Field(default=None, alias="HouseNr")
    house_nr_addition: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=50)]] = Field(default=None, alias="HouseNrAddition")
    city: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=50)]] = Field(default=None, alias="City")
    region: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=50)]] = Field(default=None, alias="Region")
    __properties: ClassVar[List[str]] = ["CountryIso", "StreetName", "ZipCode", "HouseNr", "HouseNrAddition", "City", "Region"]

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
        """Create an instance of MerchantStockLocationAddressRequest from a JSON string"""
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
        # set to None if street_name (nullable) is None
        # and model_fields_set contains the field
        if self.street_name is None and "street_name" in self.model_fields_set:
            _dict['StreetName'] = None

        # set to None if zip_code (nullable) is None
        # and model_fields_set contains the field
        if self.zip_code is None and "zip_code" in self.model_fields_set:
            _dict['ZipCode'] = None

        # set to None if house_nr (nullable) is None
        # and model_fields_set contains the field
        if self.house_nr is None and "house_nr" in self.model_fields_set:
            _dict['HouseNr'] = None

        # set to None if house_nr_addition (nullable) is None
        # and model_fields_set contains the field
        if self.house_nr_addition is None and "house_nr_addition" in self.model_fields_set:
            _dict['HouseNrAddition'] = None

        # set to None if city (nullable) is None
        # and model_fields_set contains the field
        if self.city is None and "city" in self.model_fields_set:
            _dict['City'] = None

        # set to None if region (nullable) is None
        # and model_fields_set contains the field
        if self.region is None and "region" in self.model_fields_set:
            _dict['Region'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MerchantStockLocationAddressRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "CountryIso": obj.get("CountryIso"),
            "StreetName": obj.get("StreetName"),
            "ZipCode": obj.get("ZipCode"),
            "HouseNr": obj.get("HouseNr"),
            "HouseNrAddition": obj.get("HouseNrAddition"),
            "City": obj.get("City"),
            "Region": obj.get("Region")
        })
        return _obj


