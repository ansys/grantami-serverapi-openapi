# Copyright (C) 2023 - 2024 ANSYS, Inc. and/or its affiliates.
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


class GsaSlimParameter(ModelBase):
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
        "display_names": "dict(str, str)",
        "guid": "str",
        "name": "str",
        "type": "GsaParameterType",
    }

    attribute_map: dict[str, str] = {
        "display_names": "displayNames",
        "guid": "guid",
        "name": "name",
        "type": "type",
    }

    subtype_mapping: dict[str, str] = {
        "type": "GsaParameterType",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        display_names: "Dict[str, str]",
        guid: "str",
        name: "str",
        type: "GsaParameterType",
    ) -> None:
        """GsaSlimParameter - a model defined in Swagger

        Parameters
        ----------
        display_names: Dict[str, str]
        guid: str
        name: str
        type: GsaParameterType
        """
        self._type: GsaParameterType
        self._display_names: Dict[str, str]
        self._name: str
        self._guid: str

        self.type = type
        self.display_names = display_names
        self.name = name
        self.guid = guid

    @property
    def type(self) -> "GsaParameterType":
        """Gets the type of this GsaSlimParameter.

        Returns
        -------
        GsaParameterType
            The type of this GsaSlimParameter.
        """
        return self._type

    @type.setter
    def type(self, type: "GsaParameterType") -> None:
        """Sets the type of this GsaSlimParameter.

        Parameters
        ----------
        type: GsaParameterType
            The type of this GsaSlimParameter.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

    @property
    def display_names(self) -> "Dict[str, str]":
        """Gets the display_names of this GsaSlimParameter.

        Returns
        -------
        Dict[str, str]
            The display_names of this GsaSlimParameter.
        """
        return self._display_names

    @display_names.setter
    def display_names(self, display_names: "Dict[str, str]") -> None:
        """Sets the display_names of this GsaSlimParameter.

        Parameters
        ----------
        display_names: Dict[str, str]
            The display_names of this GsaSlimParameter.
        """
        # Field is not nullable
        if display_names is None:
            raise ValueError("Invalid value for 'display_names', must not be 'None'")
        # Field is required
        if display_names is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'display_names', must not be 'Unset'")
        self._display_names = display_names

    @property
    def name(self) -> "str":
        """Gets the name of this GsaSlimParameter.

        Returns
        -------
        str
            The name of this GsaSlimParameter.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GsaSlimParameter.

        Parameters
        ----------
        name: str
            The name of this GsaSlimParameter.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        # Field is required
        if name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'name', must not be 'Unset'")
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GsaSlimParameter.

        Returns
        -------
        str
            The guid of this GsaSlimParameter.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GsaSlimParameter.

        Parameters
        ----------
        guid: str
            The guid of this GsaSlimParameter.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        # Field is required
        if guid is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'guid', must not be 'Unset'")
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
        if not isinstance(other, GsaSlimParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
