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

from ansys.grantami.serverapi_openapi.v2024r2.models.granta_server_api_schema_layouts_layout_item import (  # noqa: F401
    GrantaServerApiSchemaLayoutsLayoutItem,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiSchemaLayoutsLayoutAttributeItem(GrantaServerApiSchemaLayoutsLayoutItem):
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
        "attribute_type": "GrantaServerApiAttributeType",
        "guid": "str",
        "name": "str",
        "read_only": "bool",
        "required": "bool",
        "underlying_entity_guid": "str",
        "item_type": "str",
        "meta_attributes": "list[GrantaServerApiSchemaLayoutsLayoutAttributeItem]",
        "tabular_columns": "list[GrantaServerApiSchemaLayoutsLayoutTabularColumn]",
    }

    attribute_map: dict[str, str] = {
        "attribute_type": "attributeType",
        "guid": "guid",
        "name": "name",
        "read_only": "readOnly",
        "required": "required",
        "underlying_entity_guid": "underlyingEntityGuid",
        "item_type": "itemType",
        "meta_attributes": "metaAttributes",
        "tabular_columns": "tabularColumns",
    }

    subtype_mapping: dict[str, str] = {
        "attributeType": "GrantaServerApiAttributeType",
        "metaAttributes": "GrantaServerApiSchemaLayoutsLayoutAttributeItem",
        "tabularColumns": "GrantaServerApiSchemaLayoutsLayoutTabularColumn",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_type: "GrantaServerApiAttributeType",
        guid: "str",
        name: "str",
        read_only: "bool",
        required: "bool",
        underlying_entity_guid: "str",
        item_type: "str" = "attribute",
        meta_attributes: "Union[list[GrantaServerApiSchemaLayoutsLayoutAttributeItem], None, Unset_Type]" = Unset,
        tabular_columns: "Union[list[GrantaServerApiSchemaLayoutsLayoutTabularColumn], None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaLayoutsLayoutAttributeItem - a model defined in Swagger

        Parameters
        ----------
        attribute_type: GrantaServerApiAttributeType
        guid: str
        name: str
        read_only: bool
        required: bool
        underlying_entity_guid: str
        item_type: str
        meta_attributes: list[GrantaServerApiSchemaLayoutsLayoutAttributeItem], optional
        tabular_columns: list[GrantaServerApiSchemaLayoutsLayoutTabularColumn], optional
        """
        super().__init__(guid=guid, name=name, underlying_entity_guid=underlying_entity_guid)
        self._item_type: str
        self._attribute_type: GrantaServerApiAttributeType
        self._required: bool
        self._read_only: bool
        self._meta_attributes: Union[
            list[GrantaServerApiSchemaLayoutsLayoutAttributeItem], None, Unset_Type
        ] = Unset
        self._tabular_columns: Union[
            list[GrantaServerApiSchemaLayoutsLayoutTabularColumn], None, Unset_Type
        ] = Unset

        self.item_type = item_type
        self.attribute_type = attribute_type
        self.required = required
        self.read_only = read_only
        if meta_attributes is not Unset:
            self.meta_attributes = meta_attributes
        if tabular_columns is not Unset:
            self.tabular_columns = tabular_columns

    @property
    def item_type(self) -> "str":
        """Gets the item_type of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.

        Returns
        -------
        str
            The item_type of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type: "str") -> None:
        """Sets the item_type of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.

        Parameters
        ----------
        item_type: str
            The item_type of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.
        """
        # Field is not nullable
        if item_type is None:
            raise ValueError("Invalid value for 'item_type', must not be 'None'")
        # Field is required
        if item_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'item_type', must not be 'Unset'")
        self._item_type = item_type

    @property
    def attribute_type(self) -> "GrantaServerApiAttributeType":
        """Gets the attribute_type of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.

        Returns
        -------
        GrantaServerApiAttributeType
            The attribute_type of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.
        """
        return self._attribute_type

    @attribute_type.setter
    def attribute_type(self, attribute_type: "GrantaServerApiAttributeType") -> None:
        """Sets the attribute_type of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.

        Parameters
        ----------
        attribute_type: GrantaServerApiAttributeType
            The attribute_type of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.
        """
        # Field is not nullable
        if attribute_type is None:
            raise ValueError("Invalid value for 'attribute_type', must not be 'None'")
        # Field is required
        if attribute_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'attribute_type', must not be 'Unset'")
        self._attribute_type = attribute_type

    @property
    def required(self) -> "bool":
        """Gets the required of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.

        Returns
        -------
        bool
            The required of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.
        """
        return self._required

    @required.setter
    def required(self, required: "bool") -> None:
        """Sets the required of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.

        Parameters
        ----------
        required: bool
            The required of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.
        """
        # Field is not nullable
        if required is None:
            raise ValueError("Invalid value for 'required', must not be 'None'")
        # Field is required
        if required is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'required', must not be 'Unset'")
        self._required = required

    @property
    def read_only(self) -> "bool":
        """Gets the read_only of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.

        Returns
        -------
        bool
            The read_only of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only: "bool") -> None:
        """Sets the read_only of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.

        Parameters
        ----------
        read_only: bool
            The read_only of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.
        """
        # Field is not nullable
        if read_only is None:
            raise ValueError("Invalid value for 'read_only', must not be 'None'")
        # Field is required
        if read_only is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'read_only', must not be 'Unset'")
        self._read_only = read_only

    @property
    def meta_attributes(
        self,
    ) -> "Union[list[GrantaServerApiSchemaLayoutsLayoutAttributeItem], None, Unset_Type]":
        """Gets the meta_attributes of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.

        Returns
        -------
        Union[list[GrantaServerApiSchemaLayoutsLayoutAttributeItem], None, Unset_Type]
            The meta_attributes of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.
        """
        return self._meta_attributes

    @meta_attributes.setter
    def meta_attributes(
        self,
        meta_attributes: "Union[list[GrantaServerApiSchemaLayoutsLayoutAttributeItem], None, Unset_Type]",
    ) -> None:
        """Sets the meta_attributes of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.

        Parameters
        ----------
        meta_attributes: Union[list[GrantaServerApiSchemaLayoutsLayoutAttributeItem], None, Unset_Type]
            The meta_attributes of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.
        """
        self._meta_attributes = meta_attributes

    @property
    def tabular_columns(
        self,
    ) -> "Union[list[GrantaServerApiSchemaLayoutsLayoutTabularColumn], None, Unset_Type]":
        """Gets the tabular_columns of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.

        Returns
        -------
        Union[list[GrantaServerApiSchemaLayoutsLayoutTabularColumn], None, Unset_Type]
            The tabular_columns of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.
        """
        return self._tabular_columns

    @tabular_columns.setter
    def tabular_columns(
        self,
        tabular_columns: "Union[list[GrantaServerApiSchemaLayoutsLayoutTabularColumn], None, Unset_Type]",
    ) -> None:
        """Sets the tabular_columns of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.

        Parameters
        ----------
        tabular_columns: Union[list[GrantaServerApiSchemaLayoutsLayoutTabularColumn], None, Unset_Type]
            The tabular_columns of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.
        """
        self._tabular_columns = tabular_columns

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
        if not isinstance(other, GrantaServerApiSchemaLayoutsLayoutAttributeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
