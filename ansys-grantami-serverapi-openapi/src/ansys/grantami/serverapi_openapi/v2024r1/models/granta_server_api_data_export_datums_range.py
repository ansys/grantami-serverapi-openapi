# Copyright (C) 2023 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
MI Server API

No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

OpenAPI spec version: v1

Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiDataExportDatumsRange(ModelBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes
    ----------
    swagger_types: dict[str, str]
        The key is attribute name and the value is attribute type.
    attribute_map: dict[str, str]
        The key is attribute name and the value is json key in definition.
    subtype_mapping: dict[str, str]
        The key is the unmangled property name and the value is the corresponding type.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "high_value": "float",
        "high_value_is_inclusive": "bool",
        "low_value": "float",
        "low_value_is_inclusive": "bool",
    }

    attribute_map: dict[str, str] = {
        "high_value": "highValue",
        "high_value_is_inclusive": "highValueIsInclusive",
        "low_value": "lowValue",
        "low_value_is_inclusive": "lowValueIsInclusive",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        high_value: "Union[float, None, Unset_Type]" = Unset,
        high_value_is_inclusive: "Union[bool, Unset_Type]" = Unset,
        low_value: "Union[float, None, Unset_Type]" = Unset,
        low_value_is_inclusive: "Union[bool, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiDataExportDatumsRange - a model defined in Swagger

        Parameters
        ----------
        high_value: float, optional
        high_value_is_inclusive: bool, optional
        low_value: float, optional
        low_value_is_inclusive: bool, optional
        """
        self._high_value: Union[float, None, Unset_Type] = Unset
        self._low_value: Union[float, None, Unset_Type] = Unset
        self._high_value_is_inclusive: Union[bool, Unset_Type] = Unset
        self._low_value_is_inclusive: Union[bool, Unset_Type] = Unset

        if high_value is not Unset:
            self.high_value = high_value
        if low_value is not Unset:
            self.low_value = low_value
        if high_value_is_inclusive is not Unset:
            self.high_value_is_inclusive = high_value_is_inclusive
        if low_value_is_inclusive is not Unset:
            self.low_value_is_inclusive = low_value_is_inclusive

    @property
    def high_value(self) -> "Union[float, None, Unset_Type]":
        """Gets the high_value of this GrantaServerApiDataExportDatumsRange.

        Returns
        -------
        Union[float, None, Unset_Type]
            The high_value of this GrantaServerApiDataExportDatumsRange.
        """
        return self._high_value

    @high_value.setter
    def high_value(self, high_value: "Union[float, None, Unset_Type]") -> None:
        """Sets the high_value of this GrantaServerApiDataExportDatumsRange.

        Parameters
        ----------
        high_value: Union[float, None, Unset_Type]
            The high_value of this GrantaServerApiDataExportDatumsRange.
        """
        self._high_value = high_value

    @property
    def low_value(self) -> "Union[float, None, Unset_Type]":
        """Gets the low_value of this GrantaServerApiDataExportDatumsRange.

        Returns
        -------
        Union[float, None, Unset_Type]
            The low_value of this GrantaServerApiDataExportDatumsRange.
        """
        return self._low_value

    @low_value.setter
    def low_value(self, low_value: "Union[float, None, Unset_Type]") -> None:
        """Sets the low_value of this GrantaServerApiDataExportDatumsRange.

        Parameters
        ----------
        low_value: Union[float, None, Unset_Type]
            The low_value of this GrantaServerApiDataExportDatumsRange.
        """
        self._low_value = low_value

    @property
    def high_value_is_inclusive(self) -> "Union[bool, Unset_Type]":
        """Gets the high_value_is_inclusive of this GrantaServerApiDataExportDatumsRange.

        Returns
        -------
        Union[bool, Unset_Type]
            The high_value_is_inclusive of this GrantaServerApiDataExportDatumsRange.
        """
        return self._high_value_is_inclusive

    @high_value_is_inclusive.setter
    def high_value_is_inclusive(self, high_value_is_inclusive: "Union[bool, Unset_Type]") -> None:
        """Sets the high_value_is_inclusive of this GrantaServerApiDataExportDatumsRange.

        Parameters
        ----------
        high_value_is_inclusive: Union[bool, Unset_Type]
            The high_value_is_inclusive of this GrantaServerApiDataExportDatumsRange.
        """
        # Field is not nullable
        if high_value_is_inclusive is None:
            raise ValueError("Invalid value for 'high_value_is_inclusive', must not be 'None'")
        self._high_value_is_inclusive = high_value_is_inclusive

    @property
    def low_value_is_inclusive(self) -> "Union[bool, Unset_Type]":
        """Gets the low_value_is_inclusive of this GrantaServerApiDataExportDatumsRange.

        Returns
        -------
        Union[bool, Unset_Type]
            The low_value_is_inclusive of this GrantaServerApiDataExportDatumsRange.
        """
        return self._low_value_is_inclusive

    @low_value_is_inclusive.setter
    def low_value_is_inclusive(self, low_value_is_inclusive: "Union[bool, Unset_Type]") -> None:
        """Sets the low_value_is_inclusive of this GrantaServerApiDataExportDatumsRange.

        Parameters
        ----------
        low_value_is_inclusive: Union[bool, Unset_Type]
            The low_value_is_inclusive of this GrantaServerApiDataExportDatumsRange.
        """
        # Field is not nullable
        if low_value_is_inclusive is None:
            raise ValueError("Invalid value for 'low_value_is_inclusive', must not be 'None'")
        self._low_value_is_inclusive = low_value_is_inclusive

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
        """Raises a NotImplementedError for a type without a discriminator defined.

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class

        Raises
        ------
        NotImplementedError
            This class has no discriminator, and hence no subclasses
        """
        raise NotImplementedError()

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiDataExportDatumsRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
