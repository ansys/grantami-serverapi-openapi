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


class GsaCreateRecordHistory(ModelBase):
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
        "name": "str",
        "record_type": "GsaRecordType",
        "guid": "str",
        "parent": "GsaSlimRecordHistory",
        "record_color": "GsaRecordColor",
        "short_name": "str",
    }

    attribute_map: dict[str, str] = {
        "name": "name",
        "record_type": "recordType",
        "guid": "guid",
        "parent": "parent",
        "record_color": "recordColor",
        "short_name": "shortName",
    }

    subtype_mapping: dict[str, str] = {
        "recordType": "GsaRecordType",
        "parent": "GsaSlimRecordHistory",
        "recordColor": "GsaRecordColor",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        name: "str",
        record_type: "GsaRecordType",
        guid: "str | Unset_Type" = Unset,
        parent: "GsaSlimRecordHistory | Unset_Type" = Unset,
        record_color: "GsaRecordColor | Unset_Type" = Unset,
        short_name: "str | None | Unset_Type" = Unset,
    ) -> None:
        """GsaCreateRecordHistory - a model defined in Swagger

        Parameters
        ----------
        name: str
        record_type: GsaRecordType
        guid: str, optional
        parent: GsaSlimRecordHistory, optional
        record_color: GsaRecordColor, optional
        short_name: str | None, optional
        """
        self._record_type: GsaRecordType
        self._name: str
        self._short_name: str | None | Unset_Type = Unset
        self._parent: GsaSlimRecordHistory | Unset_Type = Unset
        self._record_color: GsaRecordColor | Unset_Type = Unset
        self._guid: str | Unset_Type = Unset

        self.record_type = record_type
        self.name = name
        if short_name is not Unset:
            self.short_name = short_name
        if parent is not Unset:
            self.parent = parent
        if record_color is not Unset:
            self.record_color = record_color
        if guid is not Unset:
            self.guid = guid

    @property
    def record_type(self) -> "GsaRecordType":
        """Gets the record_type of this GsaCreateRecordHistory.

        Returns
        -------
        GsaRecordType
            The record_type of this GsaCreateRecordHistory.
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type: "GsaRecordType") -> None:
        """Sets the record_type of this GsaCreateRecordHistory.

        Parameters
        ----------
        record_type: GsaRecordType
            The record_type of this GsaCreateRecordHistory.
        """
        # Field is not nullable
        if record_type is None:
            raise ValueError("Invalid value for 'record_type', must not be 'None'")
        # Field is required
        if record_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'record_type', must not be 'Unset'")
        self._record_type = record_type

    @property
    def name(self) -> "str":
        """Gets the name of this GsaCreateRecordHistory.

        Returns
        -------
        str
            The name of this GsaCreateRecordHistory.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GsaCreateRecordHistory.

        Parameters
        ----------
        name: str
            The name of this GsaCreateRecordHistory.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        # Field is required
        if name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'name', must not be 'Unset'")
        self._name = name

    @property
    def short_name(self) -> "str | None | Unset_Type":
        """Gets the short_name of this GsaCreateRecordHistory.

        Returns
        -------
        str | None | Unset_Type
            The short_name of this GsaCreateRecordHistory.
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name: "str | None | Unset_Type") -> None:
        """Sets the short_name of this GsaCreateRecordHistory.

        Parameters
        ----------
        short_name: str | None | Unset_Type
            The short_name of this GsaCreateRecordHistory.
        """
        self._short_name = short_name

    @property
    def parent(self) -> "GsaSlimRecordHistory | Unset_Type":
        """Gets the parent of this GsaCreateRecordHistory.

        Returns
        -------
        GsaSlimRecordHistory | Unset_Type
            The parent of this GsaCreateRecordHistory.
        """
        return self._parent

    @parent.setter
    def parent(self, parent: "GsaSlimRecordHistory | Unset_Type") -> None:
        """Sets the parent of this GsaCreateRecordHistory.

        Parameters
        ----------
        parent: GsaSlimRecordHistory | Unset_Type
            The parent of this GsaCreateRecordHistory.
        """
        # Field is not nullable
        if parent is None:
            raise ValueError("Invalid value for 'parent', must not be 'None'")
        self._parent = parent

    @property
    def record_color(self) -> "GsaRecordColor | Unset_Type":
        """Gets the record_color of this GsaCreateRecordHistory.

        Returns
        -------
        GsaRecordColor | Unset_Type
            The record_color of this GsaCreateRecordHistory.
        """
        return self._record_color

    @record_color.setter
    def record_color(self, record_color: "GsaRecordColor | Unset_Type") -> None:
        """Sets the record_color of this GsaCreateRecordHistory.

        Parameters
        ----------
        record_color: GsaRecordColor | Unset_Type
            The record_color of this GsaCreateRecordHistory.
        """
        # Field is not nullable
        if record_color is None:
            raise ValueError("Invalid value for 'record_color', must not be 'None'")
        self._record_color = record_color

    @property
    def guid(self) -> "str | Unset_Type":
        """Gets the guid of this GsaCreateRecordHistory.

        Returns
        -------
        str | Unset_Type
            The guid of this GsaCreateRecordHistory.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str | Unset_Type") -> None:
        """Sets the guid of this GsaCreateRecordHistory.

        Parameters
        ----------
        guid: str | Unset_Type
            The guid of this GsaCreateRecordHistory.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
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
        if not isinstance(other, GsaCreateRecordHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
