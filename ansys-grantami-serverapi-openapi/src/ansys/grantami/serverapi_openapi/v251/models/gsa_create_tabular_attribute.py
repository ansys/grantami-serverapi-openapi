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

from ansys.grantami.serverapi_openapi.v251.models.gsa_attribute_type import GsaAttributeType
from ansys.grantami.serverapi_openapi.v251.models.gsa_create_attribute import (  # noqa: F401
    GsaCreateAttribute,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaCreateTabularAttribute(GsaCreateAttribute):
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
        "type": "GsaAttributeType",
        "about_attribute": "GsaSlimEntity",
        "default_threshold_type": "GsaAttributeThresholdType",
        "display_full_table": "bool",
        "display_summary_row_inline": "bool",
        "guid": "str",
        "help_path": "str",
        "hide_unlinked_rows": "bool",
        "is_hidden_from_search_criteria": "bool",
        "tabular_columns": "list[GsaCreateTabularColumn]",
        "target": "GsaTabularAttributeTarget",
    }

    attribute_map: dict[str, str] = {
        "name": "name",
        "type": "type",
        "about_attribute": "aboutAttribute",
        "default_threshold_type": "defaultThresholdType",
        "display_full_table": "displayFullTable",
        "display_summary_row_inline": "displaySummaryRowInline",
        "guid": "guid",
        "help_path": "helpPath",
        "hide_unlinked_rows": "hideUnlinkedRows",
        "is_hidden_from_search_criteria": "isHiddenFromSearchCriteria",
        "tabular_columns": "tabularColumns",
        "target": "target",
    }

    subtype_mapping: dict[str, str] = {
        "tabularColumns": "GsaCreateTabularColumn",
        "target": "GsaTabularAttributeTarget",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        name: "str",
        type: "GsaAttributeType" = GsaAttributeType.LINK,
        about_attribute: "Union[GsaSlimEntity, Unset_Type]" = Unset,
        default_threshold_type: "Union[GsaAttributeThresholdType, Unset_Type]" = Unset,
        display_full_table: "Union[bool, Unset_Type]" = Unset,
        display_summary_row_inline: "Union[bool, Unset_Type]" = Unset,
        guid: "Union[str, Unset_Type]" = Unset,
        help_path: "Union[str, None, Unset_Type]" = Unset,
        hide_unlinked_rows: "Union[bool, Unset_Type]" = Unset,
        is_hidden_from_search_criteria: "Union[bool, None, Unset_Type]" = Unset,
        tabular_columns: "Union[list[GsaCreateTabularColumn], None, Unset_Type]" = Unset,
        target: "Union[GsaTabularAttributeTarget, Unset_Type]" = Unset,
    ) -> None:
        """GsaCreateTabularAttribute - a model defined in Swagger

        Parameters
        ----------
        name: str
        type: GsaAttributeType
        about_attribute: GsaSlimEntity, optional
        default_threshold_type: GsaAttributeThresholdType, optional
        display_full_table: bool, optional
        display_summary_row_inline: bool, optional
        guid: str, optional
        help_path: str, optional
        hide_unlinked_rows: bool, optional
        is_hidden_from_search_criteria: bool, optional
        tabular_columns: list[GsaCreateTabularColumn], optional
        target: GsaTabularAttributeTarget, optional
        """
        super().__init__(
            name=name,
            type=type,
            about_attribute=about_attribute,
            default_threshold_type=default_threshold_type,
            guid=guid,
            help_path=help_path,
            is_hidden_from_search_criteria=is_hidden_from_search_criteria,
        )
        self._display_full_table: Union[bool, Unset_Type] = Unset
        self._display_summary_row_inline: Union[bool, Unset_Type] = Unset
        self._hide_unlinked_rows: Union[bool, Unset_Type] = Unset
        self._tabular_columns: Union[list[GsaCreateTabularColumn], None, Unset_Type] = Unset
        self._target: Union[GsaTabularAttributeTarget, Unset_Type] = Unset

        if display_full_table is not Unset:
            self.display_full_table = display_full_table
        if display_summary_row_inline is not Unset:
            self.display_summary_row_inline = display_summary_row_inline
        if hide_unlinked_rows is not Unset:
            self.hide_unlinked_rows = hide_unlinked_rows
        if tabular_columns is not Unset:
            self.tabular_columns = tabular_columns
        if target is not Unset:
            self.target = target

    @property
    def display_full_table(self) -> "Union[bool, Unset_Type]":
        """Gets the display_full_table of this GsaCreateTabularAttribute.

        Returns
        -------
        Union[bool, Unset_Type]
            The display_full_table of this GsaCreateTabularAttribute.
        """
        return self._display_full_table

    @display_full_table.setter
    def display_full_table(self, display_full_table: "Union[bool, Unset_Type]") -> None:
        """Sets the display_full_table of this GsaCreateTabularAttribute.

        Parameters
        ----------
        display_full_table: Union[bool, Unset_Type]
            The display_full_table of this GsaCreateTabularAttribute.
        """
        # Field is not nullable
        if display_full_table is None:
            raise ValueError("Invalid value for 'display_full_table', must not be 'None'")
        self._display_full_table = display_full_table

    @property
    def display_summary_row_inline(self) -> "Union[bool, Unset_Type]":
        """Gets the display_summary_row_inline of this GsaCreateTabularAttribute.

        Returns
        -------
        Union[bool, Unset_Type]
            The display_summary_row_inline of this GsaCreateTabularAttribute.
        """
        return self._display_summary_row_inline

    @display_summary_row_inline.setter
    def display_summary_row_inline(
        self, display_summary_row_inline: "Union[bool, Unset_Type]"
    ) -> None:
        """Sets the display_summary_row_inline of this GsaCreateTabularAttribute.

        Parameters
        ----------
        display_summary_row_inline: Union[bool, Unset_Type]
            The display_summary_row_inline of this GsaCreateTabularAttribute.
        """
        # Field is not nullable
        if display_summary_row_inline is None:
            raise ValueError("Invalid value for 'display_summary_row_inline', must not be 'None'")
        self._display_summary_row_inline = display_summary_row_inline

    @property
    def hide_unlinked_rows(self) -> "Union[bool, Unset_Type]":
        """Gets the hide_unlinked_rows of this GsaCreateTabularAttribute.

        Returns
        -------
        Union[bool, Unset_Type]
            The hide_unlinked_rows of this GsaCreateTabularAttribute.
        """
        return self._hide_unlinked_rows

    @hide_unlinked_rows.setter
    def hide_unlinked_rows(self, hide_unlinked_rows: "Union[bool, Unset_Type]") -> None:
        """Sets the hide_unlinked_rows of this GsaCreateTabularAttribute.

        Parameters
        ----------
        hide_unlinked_rows: Union[bool, Unset_Type]
            The hide_unlinked_rows of this GsaCreateTabularAttribute.
        """
        # Field is not nullable
        if hide_unlinked_rows is None:
            raise ValueError("Invalid value for 'hide_unlinked_rows', must not be 'None'")
        self._hide_unlinked_rows = hide_unlinked_rows

    @property
    def tabular_columns(self) -> "Union[list[GsaCreateTabularColumn], None, Unset_Type]":
        """Gets the tabular_columns of this GsaCreateTabularAttribute.

        Returns
        -------
        Union[list[GsaCreateTabularColumn], None, Unset_Type]
            The tabular_columns of this GsaCreateTabularAttribute.
        """
        return self._tabular_columns

    @tabular_columns.setter
    def tabular_columns(
        self, tabular_columns: "Union[list[GsaCreateTabularColumn], None, Unset_Type]"
    ) -> None:
        """Sets the tabular_columns of this GsaCreateTabularAttribute.

        Parameters
        ----------
        tabular_columns: Union[list[GsaCreateTabularColumn], None, Unset_Type]
            The tabular_columns of this GsaCreateTabularAttribute.
        """
        self._tabular_columns = tabular_columns

    @property
    def target(self) -> "Union[GsaTabularAttributeTarget, Unset_Type]":
        """Gets the target of this GsaCreateTabularAttribute.

        Returns
        -------
        Union[GsaTabularAttributeTarget, Unset_Type]
            The target of this GsaCreateTabularAttribute.
        """
        return self._target

    @target.setter
    def target(self, target: "Union[GsaTabularAttributeTarget, Unset_Type]") -> None:
        """Sets the target of this GsaCreateTabularAttribute.

        Parameters
        ----------
        target: Union[GsaTabularAttributeTarget, Unset_Type]
            The target of this GsaCreateTabularAttribute.
        """
        # Field is not nullable
        if target is None:
            raise ValueError("Invalid value for 'target', must not be 'None'")
        self._target = target

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
        if not isinstance(other, GsaCreateTabularAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
