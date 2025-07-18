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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaActivityLogDateFilter(ModelBase):
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
        "date_from": "datetime",
        "date_from_inclusive": "bool",
        "date_to": "datetime",
        "date_to_inclusive": "bool",
    }

    attribute_map: dict[str, str] = {
        "date_from": "dateFrom",
        "date_from_inclusive": "dateFromInclusive",
        "date_to": "dateTo",
        "date_to_inclusive": "dateToInclusive",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        date_from: "datetime | None | Unset_Type" = Unset,
        date_from_inclusive: "bool | Unset_Type" = Unset,
        date_to: "datetime | None | Unset_Type" = Unset,
        date_to_inclusive: "bool | Unset_Type" = Unset,
    ) -> None:
        """GsaActivityLogDateFilter - a model defined in Swagger

        Parameters
        ----------
        date_from: datetime | None, optional
        date_from_inclusive: bool, optional
        date_to: datetime | None, optional
        date_to_inclusive: bool, optional
        """
        self._date_from: datetime | None | Unset_Type = Unset
        self._date_from_inclusive: bool | Unset_Type = Unset
        self._date_to: datetime | None | Unset_Type = Unset
        self._date_to_inclusive: bool | Unset_Type = Unset

        if date_from is not Unset:
            self.date_from = date_from
        if date_from_inclusive is not Unset:
            self.date_from_inclusive = date_from_inclusive
        if date_to is not Unset:
            self.date_to = date_to
        if date_to_inclusive is not Unset:
            self.date_to_inclusive = date_to_inclusive

    @property
    def date_from(self) -> "datetime | None | Unset_Type":
        """Gets the date_from of this GsaActivityLogDateFilter.

        Returns
        -------
        datetime | None | Unset_Type
            The date_from of this GsaActivityLogDateFilter.
        """
        return self._date_from

    @date_from.setter
    def date_from(self, date_from: "datetime | None | Unset_Type") -> None:
        """Sets the date_from of this GsaActivityLogDateFilter.

        Parameters
        ----------
        date_from: datetime | None | Unset_Type
            The date_from of this GsaActivityLogDateFilter.
        """
        self._date_from = date_from

    @property
    def date_from_inclusive(self) -> "bool | Unset_Type":
        """Gets the date_from_inclusive of this GsaActivityLogDateFilter.

        Returns
        -------
        bool | Unset_Type
            The date_from_inclusive of this GsaActivityLogDateFilter.
        """
        return self._date_from_inclusive

    @date_from_inclusive.setter
    def date_from_inclusive(self, date_from_inclusive: "bool | Unset_Type") -> None:
        """Sets the date_from_inclusive of this GsaActivityLogDateFilter.

        Parameters
        ----------
        date_from_inclusive: bool | Unset_Type
            The date_from_inclusive of this GsaActivityLogDateFilter.
        """
        # Field is not nullable
        if date_from_inclusive is None:
            raise ValueError("Invalid value for 'date_from_inclusive', must not be 'None'")
        self._date_from_inclusive = date_from_inclusive

    @property
    def date_to(self) -> "datetime | None | Unset_Type":
        """Gets the date_to of this GsaActivityLogDateFilter.

        Returns
        -------
        datetime | None | Unset_Type
            The date_to of this GsaActivityLogDateFilter.
        """
        return self._date_to

    @date_to.setter
    def date_to(self, date_to: "datetime | None | Unset_Type") -> None:
        """Sets the date_to of this GsaActivityLogDateFilter.

        Parameters
        ----------
        date_to: datetime | None | Unset_Type
            The date_to of this GsaActivityLogDateFilter.
        """
        self._date_to = date_to

    @property
    def date_to_inclusive(self) -> "bool | Unset_Type":
        """Gets the date_to_inclusive of this GsaActivityLogDateFilter.

        Returns
        -------
        bool | Unset_Type
            The date_to_inclusive of this GsaActivityLogDateFilter.
        """
        return self._date_to_inclusive

    @date_to_inclusive.setter
    def date_to_inclusive(self, date_to_inclusive: "bool | Unset_Type") -> None:
        """Sets the date_to_inclusive of this GsaActivityLogDateFilter.

        Parameters
        ----------
        date_to_inclusive: bool | Unset_Type
            The date_to_inclusive of this GsaActivityLogDateFilter.
        """
        # Field is not nullable
        if date_to_inclusive is None:
            raise ValueError("Invalid value for 'date_to_inclusive', must not be 'None'")
        self._date_to_inclusive = date_to_inclusive

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
        if not isinstance(other, GsaActivityLogDateFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
