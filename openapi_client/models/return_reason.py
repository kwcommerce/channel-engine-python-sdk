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


class ReturnReason(str, Enum):
    """
    ReturnReason
    """

    """
    allowed enum values
    """
    PRODUCT_DEFECT = 'PRODUCT_DEFECT'
    PRODUCT_UNSATISFACTORY = 'PRODUCT_UNSATISFACTORY'
    WRONG_PRODUCT = 'WRONG_PRODUCT'
    TOO_MANY_PRODUCTS = 'TOO_MANY_PRODUCTS'
    REFUSED = 'REFUSED'
    REFUSED_DAMAGED = 'REFUSED_DAMAGED'
    WRONG_ADDRESS = 'WRONG_ADDRESS'
    NOT_COLLECTED = 'NOT_COLLECTED'
    WRONG_SIZE = 'WRONG_SIZE'
    OTHER = 'OTHER'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ReturnReason from a JSON string"""
        return cls(json.loads(json_str))


