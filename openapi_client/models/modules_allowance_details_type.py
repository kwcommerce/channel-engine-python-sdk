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


class ModulesAllowanceDetailsType(str, Enum):
    """
    ModulesAllowanceDetailsType
    """

    """
    allowed enum values
    """
    DISCOUNT = 'DISCOUNT'
    DISCOUNT_INCENTIVE = 'DISCOUNT_INCENTIVE'
    DEFECTIVE = 'DEFECTIVE'
    PROMOTIONAL = 'PROMOTIONAL'
    UNSALEABLE_MERCHANDISE = 'UNSALEABLE_MERCHANDISE'
    SPECIAL = 'SPECIAL'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ModulesAllowanceDetailsType from a JSON string"""
        return cls(json.loads(json_str))


