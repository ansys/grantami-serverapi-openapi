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


class GsaQueryUnit(ModelBase):
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
        "equation": "str",
        "guid": "str",
        "name": "str",
        "relative_symbol": "str",
        "symbol": "str",
    }

    attribute_map: dict[str, str] = {
        "equation": "equation",
        "guid": "guid",
        "name": "name",
        "relative_symbol": "relativeSymbol",
        "symbol": "symbol",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        equation: "str | None | Unset_Type" = Unset,
        guid: "str | None | Unset_Type" = Unset,
        name: "str | None | Unset_Type" = Unset,
        relative_symbol: "str | None | Unset_Type" = Unset,
        symbol: "str | None | Unset_Type" = Unset,
    ) -> None:
        """GsaQueryUnit - a model defined in Swagger

        Parameters
        ----------
        equation: str | None, optional
        guid: str | None, optional
        name: str | None, optional
        relative_symbol: str | None, optional
        symbol: str | None, optional
        """
        self._name: str | None | Unset_Type = Unset
        self._equation: str | None | Unset_Type = Unset
        self._symbol: str | None | Unset_Type = Unset
        self._relative_symbol: str | None | Unset_Type = Unset
        self._guid: str | None | Unset_Type = Unset

        if name is not Unset:
            self.name = name
        if equation is not Unset:
            self.equation = equation
        if symbol is not Unset:
            self.symbol = symbol
        if relative_symbol is not Unset:
            self.relative_symbol = relative_symbol
        if guid is not Unset:
            self.guid = guid

    @property
    def name(self) -> "str | None | Unset_Type":
        """Gets the name of this GsaQueryUnit.

        Returns
        -------
        str | None | Unset_Type
            The name of this GsaQueryUnit.
        """
        return self._name

    @name.setter
    def name(self, name: "str | None | Unset_Type") -> None:
        """Sets the name of this GsaQueryUnit.

        Parameters
        ----------
        name: str | None | Unset_Type
            The name of this GsaQueryUnit.
        """
        self._name = name

    @property
    def equation(self) -> "str | None | Unset_Type":
        """Gets the equation of this GsaQueryUnit.

        Returns
        -------
        str | None | Unset_Type
            The equation of this GsaQueryUnit.
        """
        return self._equation

    @equation.setter
    def equation(self, equation: "str | None | Unset_Type") -> None:
        """Sets the equation of this GsaQueryUnit.

        Parameters
        ----------
        equation: str | None | Unset_Type
            The equation of this GsaQueryUnit.
        """
        self._equation = equation

    @property
    def symbol(self) -> "str | None | Unset_Type":
        """Gets the symbol of this GsaQueryUnit.

        Returns
        -------
        str | None | Unset_Type
            The symbol of this GsaQueryUnit.
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol: "str | None | Unset_Type") -> None:
        """Sets the symbol of this GsaQueryUnit.

        Parameters
        ----------
        symbol: str | None | Unset_Type
            The symbol of this GsaQueryUnit.
        """
        self._symbol = symbol

    @property
    def relative_symbol(self) -> "str | None | Unset_Type":
        """Gets the relative_symbol of this GsaQueryUnit.

        Returns
        -------
        str | None | Unset_Type
            The relative_symbol of this GsaQueryUnit.
        """
        return self._relative_symbol

    @relative_symbol.setter
    def relative_symbol(self, relative_symbol: "str | None | Unset_Type") -> None:
        """Sets the relative_symbol of this GsaQueryUnit.

        Parameters
        ----------
        relative_symbol: str | None | Unset_Type
            The relative_symbol of this GsaQueryUnit.
        """
        self._relative_symbol = relative_symbol

    @property
    def guid(self) -> "str | None | Unset_Type":
        """Gets the guid of this GsaQueryUnit.

        Returns
        -------
        str | None | Unset_Type
            The guid of this GsaQueryUnit.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str | None | Unset_Type") -> None:
        """Sets the guid of this GsaQueryUnit.

        Parameters
        ----------
        guid: str | None | Unset_Type
            The guid of this GsaQueryUnit.
        """
        self._guid = guid

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
        if not isinstance(other, GsaQueryUnit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
