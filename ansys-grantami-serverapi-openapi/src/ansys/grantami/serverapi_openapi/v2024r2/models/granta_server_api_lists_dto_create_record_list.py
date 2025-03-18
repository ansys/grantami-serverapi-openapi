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


class GrantaServerApiListsDtoCreateRecordList(ModelBase):
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
        "awaiting_approval": "bool",
        "description": "str",
        "identifier": "str",
        "internal_use": "bool",
        "items": "GrantaServerApiListsDtoCreateRecordListItemsInfo",
        "notes": "str",
        "published": "bool",
    }

    attribute_map: dict[str, str] = {
        "name": "name",
        "awaiting_approval": "awaitingApproval",
        "description": "description",
        "identifier": "identifier",
        "internal_use": "internalUse",
        "items": "items",
        "notes": "notes",
        "published": "published",
    }

    subtype_mapping: dict[str, str] = {
        "items": "GrantaServerApiListsDtoCreateRecordListItemsInfo",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        name: "str",
        awaiting_approval: "Union[bool, Unset_Type]" = Unset,
        description: "Union[str, None, Unset_Type]" = Unset,
        identifier: "Union[str, None, Unset_Type]" = Unset,
        internal_use: "Union[bool, Unset_Type]" = Unset,
        items: "Union[GrantaServerApiListsDtoCreateRecordListItemsInfo, Unset_Type]" = Unset,
        notes: "Union[str, None, Unset_Type]" = Unset,
        published: "Union[bool, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiListsDtoCreateRecordList - a model defined in Swagger

        Parameters
        ----------
        name: str
        awaiting_approval: bool, optional
        description: str, optional
        identifier: str, optional
        internal_use: bool, optional
        items: GrantaServerApiListsDtoCreateRecordListItemsInfo, optional
        notes: str, optional
        published: bool, optional
        """
        self._items: Union[GrantaServerApiListsDtoCreateRecordListItemsInfo, Unset_Type] = Unset
        self._identifier: Union[str, None, Unset_Type] = Unset
        self._name: str
        self._description: Union[str, None, Unset_Type] = Unset
        self._notes: Union[str, None, Unset_Type] = Unset
        self._published: Union[bool, Unset_Type] = Unset
        self._awaiting_approval: Union[bool, Unset_Type] = Unset
        self._internal_use: Union[bool, Unset_Type] = Unset

        if items is not Unset:
            self.items = items
        if identifier is not Unset:
            self.identifier = identifier
        self.name = name
        if description is not Unset:
            self.description = description
        if notes is not Unset:
            self.notes = notes
        if published is not Unset:
            self.published = published
        if awaiting_approval is not Unset:
            self.awaiting_approval = awaiting_approval
        if internal_use is not Unset:
            self.internal_use = internal_use

    @property
    def items(self) -> "Union[GrantaServerApiListsDtoCreateRecordListItemsInfo, Unset_Type]":
        """Gets the items of this GrantaServerApiListsDtoCreateRecordList.

        Returns
        -------
        Union[GrantaServerApiListsDtoCreateRecordListItemsInfo, Unset_Type]
            The items of this GrantaServerApiListsDtoCreateRecordList.
        """
        return self._items

    @items.setter
    def items(
        self, items: "Union[GrantaServerApiListsDtoCreateRecordListItemsInfo, Unset_Type]"
    ) -> None:
        """Sets the items of this GrantaServerApiListsDtoCreateRecordList.

        Parameters
        ----------
        items: Union[GrantaServerApiListsDtoCreateRecordListItemsInfo, Unset_Type]
            The items of this GrantaServerApiListsDtoCreateRecordList.
        """
        # Field is not nullable
        if items is None:
            raise ValueError("Invalid value for 'items', must not be 'None'")
        self._items = items

    @property
    def identifier(self) -> "Union[str, None, Unset_Type]":
        """Gets the identifier of this GrantaServerApiListsDtoCreateRecordList.

        Returns
        -------
        Union[str, None, Unset_Type]
            The identifier of this GrantaServerApiListsDtoCreateRecordList.
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier: "Union[str, None, Unset_Type]") -> None:
        """Sets the identifier of this GrantaServerApiListsDtoCreateRecordList.

        Parameters
        ----------
        identifier: Union[str, None, Unset_Type]
            The identifier of this GrantaServerApiListsDtoCreateRecordList.
        """
        self._identifier = identifier

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiListsDtoCreateRecordList.

        Returns
        -------
        str
            The name of this GrantaServerApiListsDtoCreateRecordList.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiListsDtoCreateRecordList.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiListsDtoCreateRecordList.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        # Field is required
        if name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'name', must not be 'Unset'")
        self._name = name

    @property
    def description(self) -> "Union[str, None, Unset_Type]":
        """Gets the description of this GrantaServerApiListsDtoCreateRecordList.

        Returns
        -------
        Union[str, None, Unset_Type]
            The description of this GrantaServerApiListsDtoCreateRecordList.
        """
        return self._description

    @description.setter
    def description(self, description: "Union[str, None, Unset_Type]") -> None:
        """Sets the description of this GrantaServerApiListsDtoCreateRecordList.

        Parameters
        ----------
        description: Union[str, None, Unset_Type]
            The description of this GrantaServerApiListsDtoCreateRecordList.
        """
        self._description = description

    @property
    def notes(self) -> "Union[str, None, Unset_Type]":
        """Gets the notes of this GrantaServerApiListsDtoCreateRecordList.

        Returns
        -------
        Union[str, None, Unset_Type]
            The notes of this GrantaServerApiListsDtoCreateRecordList.
        """
        return self._notes

    @notes.setter
    def notes(self, notes: "Union[str, None, Unset_Type]") -> None:
        """Sets the notes of this GrantaServerApiListsDtoCreateRecordList.

        Parameters
        ----------
        notes: Union[str, None, Unset_Type]
            The notes of this GrantaServerApiListsDtoCreateRecordList.
        """
        self._notes = notes

    @property
    def published(self) -> "Union[bool, Unset_Type]":
        """Gets the published of this GrantaServerApiListsDtoCreateRecordList.

        Returns
        -------
        Union[bool, Unset_Type]
            The published of this GrantaServerApiListsDtoCreateRecordList.
        """
        return self._published

    @published.setter
    def published(self, published: "Union[bool, Unset_Type]") -> None:
        """Sets the published of this GrantaServerApiListsDtoCreateRecordList.

        Parameters
        ----------
        published: Union[bool, Unset_Type]
            The published of this GrantaServerApiListsDtoCreateRecordList.
        """
        # Field is not nullable
        if published is None:
            raise ValueError("Invalid value for 'published', must not be 'None'")
        self._published = published

    @property
    def awaiting_approval(self) -> "Union[bool, Unset_Type]":
        """Gets the awaiting_approval of this GrantaServerApiListsDtoCreateRecordList.

        Returns
        -------
        Union[bool, Unset_Type]
            The awaiting_approval of this GrantaServerApiListsDtoCreateRecordList.
        """
        return self._awaiting_approval

    @awaiting_approval.setter
    def awaiting_approval(self, awaiting_approval: "Union[bool, Unset_Type]") -> None:
        """Sets the awaiting_approval of this GrantaServerApiListsDtoCreateRecordList.

        Parameters
        ----------
        awaiting_approval: Union[bool, Unset_Type]
            The awaiting_approval of this GrantaServerApiListsDtoCreateRecordList.
        """
        # Field is not nullable
        if awaiting_approval is None:
            raise ValueError("Invalid value for 'awaiting_approval', must not be 'None'")
        self._awaiting_approval = awaiting_approval

    @property
    def internal_use(self) -> "Union[bool, Unset_Type]":
        """Gets the internal_use of this GrantaServerApiListsDtoCreateRecordList.

        Returns
        -------
        Union[bool, Unset_Type]
            The internal_use of this GrantaServerApiListsDtoCreateRecordList.
        """
        return self._internal_use

    @internal_use.setter
    def internal_use(self, internal_use: "Union[bool, Unset_Type]") -> None:
        """Sets the internal_use of this GrantaServerApiListsDtoCreateRecordList.

        Parameters
        ----------
        internal_use: Union[bool, Unset_Type]
            The internal_use of this GrantaServerApiListsDtoCreateRecordList.
        """
        # Field is not nullable
        if internal_use is None:
            raise ValueError("Invalid value for 'internal_use', must not be 'None'")
        self._internal_use = internal_use

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
        if not isinstance(other, GrantaServerApiListsDtoCreateRecordList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
