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


class ChannelCarrierCollectionMethodApi(str, Enum):
    """
    ChannelCarrierCollectionMethodApi
    """

    """
    allowed enum values
    """
    DROP_OFF = 'DROP_OFF'
    PICK_UP = 'PICK_UP'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ChannelCarrierCollectionMethodApi from a JSON string"""
        return cls(json.loads(json_str))


