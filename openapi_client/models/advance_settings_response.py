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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class AdvanceSettingsResponse(BaseModel):
    """
    AdvanceSettingsResponse
    """ # noqa: E501
    manage_stock: Optional[StrictBool] = Field(default=None, alias="ManageStock")
    disable_address_validation: Optional[StrictBool] = Field(default=None, alias="DisableAddressValidation")
    skip_house_number_validation: Optional[StrictBool] = Field(default=None, alias="SkipHouseNumberValidation")
    skip_house_number_validation_for_country_codes: Optional[List[StrictStr]] = Field(default=None, alias="SkipHouseNumberValidationForCountryCodes")
    set_orders_to_closed_on_import: Optional[StrictBool] = Field(default=None, alias="SetOrdersToClosedOnImport")
    disable_stock_reservation: Optional[StrictBool] = Field(default=None, alias="DisableStockReservation")
    disable_auto_order_cancellation: Optional[StrictBool] = Field(default=None, alias="DisableAutoOrderCancellation")
    automatically_set_phone_number_if_empty: Optional[StrictStr] = Field(default=None, alias="AutomaticallySetPhoneNumberIfEmpty")
    default_vat_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="DefaultVatRate")
    order_too_long_on_new_hours_offset: Optional[StrictInt] = Field(default=None, alias="OrderTooLongOnNewHoursOffset")
    __properties: ClassVar[List[str]] = ["ManageStock", "DisableAddressValidation", "SkipHouseNumberValidation", "SkipHouseNumberValidationForCountryCodes", "SetOrdersToClosedOnImport", "DisableStockReservation", "DisableAutoOrderCancellation", "AutomaticallySetPhoneNumberIfEmpty", "DefaultVatRate", "OrderTooLongOnNewHoursOffset"]

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
        """Create an instance of AdvanceSettingsResponse from a JSON string"""
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
        # set to None if skip_house_number_validation_for_country_codes (nullable) is None
        # and model_fields_set contains the field
        if self.skip_house_number_validation_for_country_codes is None and "skip_house_number_validation_for_country_codes" in self.model_fields_set:
            _dict['SkipHouseNumberValidationForCountryCodes'] = None

        # set to None if automatically_set_phone_number_if_empty (nullable) is None
        # and model_fields_set contains the field
        if self.automatically_set_phone_number_if_empty is None and "automatically_set_phone_number_if_empty" in self.model_fields_set:
            _dict['AutomaticallySetPhoneNumberIfEmpty'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdvanceSettingsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ManageStock": obj.get("ManageStock"),
            "DisableAddressValidation": obj.get("DisableAddressValidation"),
            "SkipHouseNumberValidation": obj.get("SkipHouseNumberValidation"),
            "SkipHouseNumberValidationForCountryCodes": obj.get("SkipHouseNumberValidationForCountryCodes"),
            "SetOrdersToClosedOnImport": obj.get("SetOrdersToClosedOnImport"),
            "DisableStockReservation": obj.get("DisableStockReservation"),
            "DisableAutoOrderCancellation": obj.get("DisableAutoOrderCancellation"),
            "AutomaticallySetPhoneNumberIfEmpty": obj.get("AutomaticallySetPhoneNumberIfEmpty"),
            "DefaultVatRate": obj.get("DefaultVatRate"),
            "OrderTooLongOnNewHoursOffset": obj.get("OrderTooLongOnNewHoursOffset")
        })
        return _obj

