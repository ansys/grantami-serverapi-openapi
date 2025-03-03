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

from ansys.grantami.serverapi_openapi.v2025r2.models.gsa_layout_item import (  # noqa: F401
    GsaLayoutItem,
)
from ansys.grantami.serverapi_openapi.v2025r2.models.gsa_layout_item_type import GsaLayoutItemType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaLayoutLinkItem(GsaLayoutItem):
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
        "forwards": "bool",
        "guid": "str",
        "item_type": "GsaLayoutItemType",
        "link_type": "GsaLayoutItemLinkType",
        "name": "str",
        "target_table": "str",
        "underlying_entity_guid": "str",
        "next_link": "GsaLayoutLinkItem",
        "target_database": "str",
        "target_database_version": "str",
    }

    attribute_map: dict[str, str] = {
        "forwards": "forwards",
        "guid": "guid",
        "item_type": "itemType",
        "link_type": "linkType",
        "name": "name",
        "target_table": "targetTable",
        "underlying_entity_guid": "underlyingEntityGuid",
        "next_link": "nextLink",
        "target_database": "targetDatabase",
        "target_database_version": "targetDatabaseVersion",
    }

    subtype_mapping: dict[str, str] = {
        "linkType": "GsaLayoutItemLinkType",
        "nextLink": "GsaLayoutLinkItem",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        forwards: "bool",
        guid: "str",
        item_type: "GsaLayoutItemType" = GsaLayoutItemType.LINK,
        link_type: "GsaLayoutItemLinkType",
        name: "str",
        target_table: "str",
        underlying_entity_guid: "str",
        next_link: "Union[GsaLayoutLinkItem, Unset_Type]" = Unset,
        target_database: "Union[str, None, Unset_Type]" = Unset,
        target_database_version: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaLayoutLinkItem - a model defined in Swagger

        Parameters
        ----------
        forwards: bool
        guid: str
        item_type: GsaLayoutItemType
        link_type: GsaLayoutItemLinkType
        name: str
        target_table: str
        underlying_entity_guid: str
        next_link: GsaLayoutLinkItem, optional
        target_database: str, optional
        target_database_version: str, optional
        """
        super().__init__(
            guid=guid, item_type=item_type, name=name, underlying_entity_guid=underlying_entity_guid
        )
        self._link_type: GsaLayoutItemLinkType
        self._target_database: Union[str, None, Unset_Type] = Unset
        self._target_database_version: Union[str, None, Unset_Type] = Unset
        self._target_table: str
        self._forwards: bool
        self._next_link: Union[GsaLayoutLinkItem, Unset_Type] = Unset

        self.link_type = link_type
        if target_database is not Unset:
            self.target_database = target_database
        if target_database_version is not Unset:
            self.target_database_version = target_database_version
        self.target_table = target_table
        self.forwards = forwards
        if next_link is not Unset:
            self.next_link = next_link

    @property
    def link_type(self) -> "GsaLayoutItemLinkType":
        """Gets the link_type of this GsaLayoutLinkItem.

        Returns
        -------
        GsaLayoutItemLinkType
            The link_type of this GsaLayoutLinkItem.
        """
        return self._link_type

    @link_type.setter
    def link_type(self, link_type: "GsaLayoutItemLinkType") -> None:
        """Sets the link_type of this GsaLayoutLinkItem.

        Parameters
        ----------
        link_type: GsaLayoutItemLinkType
            The link_type of this GsaLayoutLinkItem.
        """
        # Field is not nullable
        if link_type is None:
            raise ValueError("Invalid value for 'link_type', must not be 'None'")
        # Field is required
        if link_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'link_type', must not be 'Unset'")
        self._link_type = link_type

    @property
    def target_database(self) -> "Union[str, None, Unset_Type]":
        """Gets the target_database of this GsaLayoutLinkItem.
        May be null for a cross database link group that can target multiple databases

        Returns
        -------
        Union[str, None, Unset_Type]
            The target_database of this GsaLayoutLinkItem.
        """
        return self._target_database

    @target_database.setter
    def target_database(self, target_database: "Union[str, None, Unset_Type]") -> None:
        """Sets the target_database of this GsaLayoutLinkItem.
        May be null for a cross database link group that can target multiple databases

        Parameters
        ----------
        target_database: Union[str, None, Unset_Type]
            The target_database of this GsaLayoutLinkItem.
        """
        self._target_database = target_database

    @property
    def target_database_version(self) -> "Union[str, None, Unset_Type]":
        """Gets the target_database_version of this GsaLayoutLinkItem.
        May be null for a cross database link group that can target multiple databases

        Returns
        -------
        Union[str, None, Unset_Type]
            The target_database_version of this GsaLayoutLinkItem.
        """
        return self._target_database_version

    @target_database_version.setter
    def target_database_version(
        self, target_database_version: "Union[str, None, Unset_Type]"
    ) -> None:
        """Sets the target_database_version of this GsaLayoutLinkItem.
        May be null for a cross database link group that can target multiple databases

        Parameters
        ----------
        target_database_version: Union[str, None, Unset_Type]
            The target_database_version of this GsaLayoutLinkItem.
        """
        self._target_database_version = target_database_version

    @property
    def target_table(self) -> "str":
        """Gets the target_table of this GsaLayoutLinkItem.

        Returns
        -------
        str
            The target_table of this GsaLayoutLinkItem.
        """
        return self._target_table

    @target_table.setter
    def target_table(self, target_table: "str") -> None:
        """Sets the target_table of this GsaLayoutLinkItem.

        Parameters
        ----------
        target_table: str
            The target_table of this GsaLayoutLinkItem.
        """
        # Field is not nullable
        if target_table is None:
            raise ValueError("Invalid value for 'target_table', must not be 'None'")
        # Field is required
        if target_table is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'target_table', must not be 'Unset'")
        self._target_table = target_table

    @property
    def forwards(self) -> "bool":
        """Gets the forwards of this GsaLayoutLinkItem.
        true if the link points from the table the layout is in; or false if it points towards the table the layout is in (an inbound link).

        Returns
        -------
        bool
            The forwards of this GsaLayoutLinkItem.
        """
        return self._forwards

    @forwards.setter
    def forwards(self, forwards: "bool") -> None:
        """Sets the forwards of this GsaLayoutLinkItem.
        true if the link points from the table the layout is in; or false if it points towards the table the layout is in (an inbound link).

        Parameters
        ----------
        forwards: bool
            The forwards of this GsaLayoutLinkItem.
        """
        # Field is not nullable
        if forwards is None:
            raise ValueError("Invalid value for 'forwards', must not be 'None'")
        # Field is required
        if forwards is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'forwards', must not be 'Unset'")
        self._forwards = forwards

    @property
    def next_link(self) -> "Union[GsaLayoutLinkItem, Unset_Type]":
        """Gets the next_link of this GsaLayoutLinkItem.

        Returns
        -------
        Union[GsaLayoutLinkItem, Unset_Type]
            The next_link of this GsaLayoutLinkItem.
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link: "Union[GsaLayoutLinkItem, Unset_Type]") -> None:
        """Sets the next_link of this GsaLayoutLinkItem.

        Parameters
        ----------
        next_link: Union[GsaLayoutLinkItem, Unset_Type]
            The next_link of this GsaLayoutLinkItem.
        """
        # Field is not nullable
        if next_link is None:
            raise ValueError("Invalid value for 'next_link', must not be 'None'")
        self._next_link = next_link

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
        if not isinstance(other, GsaLayoutLinkItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
