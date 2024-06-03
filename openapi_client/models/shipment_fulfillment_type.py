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


class ShipmentFulfillmentType(str, Enum):
    """
    Shipment is fully fulfilled by channel or merchant  so no make sense to use FulfillmentType for orders  It is created to keep it consistent with others
    """

    """
    allowed enum values
    """
    ALL = 'ALL'
    ONLY_MERCHANT = 'ONLY_MERCHANT'
    ONLY_CHANNEL = 'ONLY_CHANNEL'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ShipmentFulfillmentType from a JSON string"""
        return cls(json.loads(json_str))


