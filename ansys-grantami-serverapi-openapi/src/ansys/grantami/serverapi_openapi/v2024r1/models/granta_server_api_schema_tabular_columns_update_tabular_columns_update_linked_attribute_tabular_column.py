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

from ansys.grantami.serverapi_openapi.v2024r1.models.granta_server_api_schema_tabular_columns_update_tabular_columns_update_tabular_column import (  # noqa: F401
    GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLinkedAttributeTabularColumn(
    GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn
):
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
        "column_type": "str",
        "guid": "str",
        "linked_attribute": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "name": "str",
        "roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "show_as_link": "bool",
        "summary_row_enabled": "bool",
        "summary_row_roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "summary_row_text": "str",
    }

    attribute_map: dict[str, str] = {
        "column_type": "columnType",
        "guid": "guid",
        "linked_attribute": "linkedAttribute",
        "name": "name",
        "roll_up_type": "rollUpType",
        "show_as_link": "showAsLink",
        "summary_row_enabled": "summaryRowEnabled",
        "summary_row_roll_up_type": "summaryRowRollUpType",
        "summary_row_text": "summaryRowText",
    }

    subtype_mapping: dict[str, str] = {
        "linkedAttribute": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        column_type: "str" = "linkedAttribute",
        guid: "str | Unset_Type" = Unset,
        linked_attribute: "GrantaServerApiSchemaSlimEntitiesSlimEntity | Unset_Type" = Unset,
        name: "str | Unset_Type" = Unset,
        roll_up_type: "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType | Unset_Type" = Unset,
        show_as_link: "bool | Unset_Type" = Unset,
        summary_row_enabled: "bool | Unset_Type" = Unset,
        summary_row_roll_up_type: "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType | Unset_Type" = Unset,
        summary_row_text: "str | None | Unset_Type" = Unset,
    ) -> None:
        """GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLinkedAttributeTabularColumn - a model defined in Swagger

        Parameters
        ----------
        column_type: str
        guid: str, optional
        linked_attribute: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
        name: str, optional
        roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, optional
        show_as_link: bool, optional
        summary_row_enabled: bool, optional
        summary_row_roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, optional
        summary_row_text: str | None, optional
        """
        super().__init__(
            guid=guid,
            name=name,
            roll_up_type=roll_up_type,
            show_as_link=show_as_link,
            summary_row_enabled=summary_row_enabled,
            summary_row_roll_up_type=summary_row_roll_up_type,
            summary_row_text=summary_row_text,
        )
        self._column_type: str
        self._linked_attribute: GrantaServerApiSchemaSlimEntitiesSlimEntity | Unset_Type = Unset

        self.column_type = column_type
        if linked_attribute is not Unset:
            self.linked_attribute = linked_attribute

    @property
    def column_type(self) -> "str":
        """Gets the column_type of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLinkedAttributeTabularColumn.

        Returns
        -------
        str
            The column_type of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLinkedAttributeTabularColumn.
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type: "str") -> None:
        """Sets the column_type of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLinkedAttributeTabularColumn.

        Parameters
        ----------
        column_type: str
            The column_type of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLinkedAttributeTabularColumn.
        """
        # Field is not nullable
        if column_type is None:
            raise ValueError("Invalid value for 'column_type', must not be 'None'")
        # Field is required
        if column_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'column_type', must not be 'Unset'")
        self._column_type = column_type

    @property
    def linked_attribute(self) -> "GrantaServerApiSchemaSlimEntitiesSlimEntity | Unset_Type":
        """Gets the linked_attribute of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLinkedAttributeTabularColumn.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimEntity | Unset_Type
            The linked_attribute of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLinkedAttributeTabularColumn.
        """
        return self._linked_attribute

    @linked_attribute.setter
    def linked_attribute(
        self, linked_attribute: "GrantaServerApiSchemaSlimEntitiesSlimEntity | Unset_Type"
    ) -> None:
        """Sets the linked_attribute of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLinkedAttributeTabularColumn.

        Parameters
        ----------
        linked_attribute: GrantaServerApiSchemaSlimEntitiesSlimEntity | Unset_Type
            The linked_attribute of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLinkedAttributeTabularColumn.
        """
        # Field is not nullable
        if linked_attribute is None:
            raise ValueError("Invalid value for 'linked_attribute', must not be 'None'")
        self._linked_attribute = linked_attribute

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
        if not isinstance(
            other,
            GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLinkedAttributeTabularColumn,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
