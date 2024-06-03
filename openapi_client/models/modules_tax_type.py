# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ModulesTaxType(str, Enum):
    """
    ModulesTaxType
    """

    """
    allowed enum values
    """
    CGST = 'CGST'
    SGST = 'SGST'
    CESS = 'CESS'
    UTGST = 'UTGST'
    IGST = 'IGST'
    MWST = 'MWST'
    PST = 'PST'
    TVA = 'TVA'
    VAT = 'VAT'
    GST = 'GST'
    ST = 'ST'
    CONSUMPTION = 'CONSUMPTION'
    MUTUALLY_DEFINED = 'MUTUALLY_DEFINED'
    DOMESTIC_VAT = 'DOMESTIC_VAT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ModulesTaxType from a JSON string"""
        return cls(json.loads(json_str))

