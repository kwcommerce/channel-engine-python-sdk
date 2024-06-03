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


class ModulesPurchaseOrderType(str, Enum):
    """
    ModulesPurchaseOrderType
    """

    """
    allowed enum values
    """
    REGULAR_ORDER = 'REGULAR_ORDER'
    CONSIGNED_ORDER = 'CONSIGNED_ORDER'
    NEW_PRODUCT_INTRODUCTION = 'NEW_PRODUCT_INTRODUCTION'
    RUSH_ORDER = 'RUSH_ORDER'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ModulesPurchaseOrderType from a JSON string"""
        return cls(json.loads(json_str))

