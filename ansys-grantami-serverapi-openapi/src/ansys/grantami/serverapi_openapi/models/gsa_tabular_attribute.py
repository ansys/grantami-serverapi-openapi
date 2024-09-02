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
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, Union  # noqa: F401

from ansys.grantami.serverapi_openapi.models.gsa_attribute import GsaAttribute  # noqa: F401
from ansys.grantami.serverapi_openapi.models.gsa_attribute_type import GsaAttributeType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaTabularAttribute(GsaAttribute):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes
    ----------
    swagger_types: Dict[str, str]
        The key is attribute name and the value is attribute type.
    attribute_map: Dict[str, str]
        The key is attribute name and the value is json key in definition.
    subtype_mapping: Dict[str, str]
        The key is the unmangled property name and the value is the corresponding type.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: Dict[str, str] = {
        "default_threshold_type": "GsaAttributeThresholdType",
        "display_full_table": "bool",
        "display_names": "dict(str, str)",
        "display_summary_row_inline": "bool",
        "guid": "str",
        "hide_unlinked_rows": "bool",
        "info": "GsaAttributeInfo",
        "is_hidden_from_search_criteria": "bool",
        "name": "str",
        "table": "GsaSlimEntity",
        "tabular_columns": "list[GsaTabularColumn]",
        "type": "GsaAttributeType",
        "about_attribute": "GsaSlimNamedEntity",
        "axis_name": "str",
        "help_path": "str",
        "target": "GsaTabularAttributeTarget",
    }

    attribute_map: Dict[str, str] = {
        "default_threshold_type": "defaultThresholdType",
        "display_full_table": "displayFullTable",
        "display_names": "displayNames",
        "display_summary_row_inline": "displaySummaryRowInline",
        "guid": "guid",
        "hide_unlinked_rows": "hideUnlinkedRows",
        "info": "info",
        "is_hidden_from_search_criteria": "isHiddenFromSearchCriteria",
        "name": "name",
        "table": "table",
        "tabular_columns": "tabularColumns",
        "type": "type",
        "about_attribute": "aboutAttribute",
        "axis_name": "axisName",
        "help_path": "helpPath",
        "target": "target",
    }

    subtype_mapping: Dict[str, str] = {
        "target": "GsaTabularAttributeTarget",
        "tabularColumns": "GsaTabularColumn",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        default_threshold_type: "GsaAttributeThresholdType",
        display_full_table: "bool",
        display_names: "Dict[str, str]",
        display_summary_row_inline: "bool",
        guid: "str",
        hide_unlinked_rows: "bool",
        info: "GsaAttributeInfo",
        is_hidden_from_search_criteria: "bool",
        name: "str",
        table: "GsaSlimEntity",
        tabular_columns: "List[GsaTabularColumn]",
        type: "GsaAttributeType" = GsaAttributeType.LINK,
        about_attribute: "Union[GsaSlimNamedEntity, Unset_Type]" = Unset,
        axis_name: "Union[str, None, Unset_Type]" = Unset,
        help_path: "Union[str, None, Unset_Type]" = Unset,
        target: "Union[GsaTabularAttributeTarget, Unset_Type]" = Unset,
    ) -> None:
        """GsaTabularAttribute - a model defined in Swagger

        Parameters
        ----------
        default_threshold_type: GsaAttributeThresholdType
        display_full_table: bool
        display_names: Dict[str, str]
        display_summary_row_inline: bool
        guid: str
        hide_unlinked_rows: bool
        info: GsaAttributeInfo
        is_hidden_from_search_criteria: bool
        name: str
        table: GsaSlimEntity
        tabular_columns: List[GsaTabularColumn]
        type: GsaAttributeType
        about_attribute: GsaSlimNamedEntity, optional
        axis_name: str, optional
        help_path: str, optional
        target: GsaTabularAttributeTarget, optional
        """
        super().__init__(
            default_threshold_type=default_threshold_type,
            display_names=display_names,
            guid=guid,
            info=info,
            is_hidden_from_search_criteria=is_hidden_from_search_criteria,
            name=name,
            table=table,
            type=type,
            about_attribute=about_attribute,
            axis_name=axis_name,
            help_path=help_path,
        )
        self._display_full_table: bool
        self._display_summary_row_inline: bool
        self._hide_unlinked_rows: bool
        self._target: Union[GsaTabularAttributeTarget, Unset_Type] = Unset
        self._tabular_columns: List[GsaTabularColumn]

        self.display_full_table = display_full_table
        self.display_summary_row_inline = display_summary_row_inline
        self.hide_unlinked_rows = hide_unlinked_rows
        if target is not Unset:
            self.target = target
        self.tabular_columns = tabular_columns

    @property
    def display_full_table(self) -> "bool":
        """Gets the display_full_table of this GsaTabularAttribute.

        Returns
        -------
        bool
            The display_full_table of this GsaTabularAttribute.
        """
        return self._display_full_table

    @display_full_table.setter
    def display_full_table(self, display_full_table: "bool") -> None:
        """Sets the display_full_table of this GsaTabularAttribute.

        Parameters
        ----------
        display_full_table: bool
            The display_full_table of this GsaTabularAttribute.
        """
        # Field is not nullable
        if display_full_table is None:
            raise ValueError("Invalid value for 'display_full_table', must not be 'None'")
        # Field is required
        if display_full_table is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'display_full_table', must not be 'Unset'")
        self._display_full_table = display_full_table

    @property
    def display_summary_row_inline(self) -> "bool":
        """Gets the display_summary_row_inline of this GsaTabularAttribute.

        Returns
        -------
        bool
            The display_summary_row_inline of this GsaTabularAttribute.
        """
        return self._display_summary_row_inline

    @display_summary_row_inline.setter
    def display_summary_row_inline(self, display_summary_row_inline: "bool") -> None:
        """Sets the display_summary_row_inline of this GsaTabularAttribute.

        Parameters
        ----------
        display_summary_row_inline: bool
            The display_summary_row_inline of this GsaTabularAttribute.
        """
        # Field is not nullable
        if display_summary_row_inline is None:
            raise ValueError("Invalid value for 'display_summary_row_inline', must not be 'None'")
        # Field is required
        if display_summary_row_inline is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'display_summary_row_inline', must not be 'Unset'")
        self._display_summary_row_inline = display_summary_row_inline

    @property
    def hide_unlinked_rows(self) -> "bool":
        """Gets the hide_unlinked_rows of this GsaTabularAttribute.

        Returns
        -------
        bool
            The hide_unlinked_rows of this GsaTabularAttribute.
        """
        return self._hide_unlinked_rows

    @hide_unlinked_rows.setter
    def hide_unlinked_rows(self, hide_unlinked_rows: "bool") -> None:
        """Sets the hide_unlinked_rows of this GsaTabularAttribute.

        Parameters
        ----------
        hide_unlinked_rows: bool
            The hide_unlinked_rows of this GsaTabularAttribute.
        """
        # Field is not nullable
        if hide_unlinked_rows is None:
            raise ValueError("Invalid value for 'hide_unlinked_rows', must not be 'None'")
        # Field is required
        if hide_unlinked_rows is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'hide_unlinked_rows', must not be 'Unset'")
        self._hide_unlinked_rows = hide_unlinked_rows

    @property
    def target(self) -> "Union[GsaTabularAttributeTarget, Unset_Type]":
        """Gets the target of this GsaTabularAttribute.

        Returns
        -------
        Union[GsaTabularAttributeTarget, Unset_Type]
            The target of this GsaTabularAttribute.
        """
        return self._target

    @target.setter
    def target(self, target: "Union[GsaTabularAttributeTarget, Unset_Type]") -> None:
        """Sets the target of this GsaTabularAttribute.

        Parameters
        ----------
        target: Union[GsaTabularAttributeTarget, Unset_Type]
            The target of this GsaTabularAttribute.
        """
        # Field is not nullable
        if target is None:
            raise ValueError("Invalid value for 'target', must not be 'None'")
        self._target = target

    @property
    def tabular_columns(self) -> "List[GsaTabularColumn]":
        """Gets the tabular_columns of this GsaTabularAttribute.

        Returns
        -------
        List[GsaTabularColumn]
            The tabular_columns of this GsaTabularAttribute.
        """
        return self._tabular_columns

    @tabular_columns.setter
    def tabular_columns(self, tabular_columns: "List[GsaTabularColumn]") -> None:
        """Sets the tabular_columns of this GsaTabularAttribute.

        Parameters
        ----------
        tabular_columns: List[GsaTabularColumn]
            The tabular_columns of this GsaTabularAttribute.
        """
        # Field is not nullable
        if tabular_columns is None:
            raise ValueError("Invalid value for 'tabular_columns', must not be 'None'")
        # Field is required
        if tabular_columns is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'tabular_columns', must not be 'Unset'")
        self._tabular_columns = tabular_columns

    @classmethod
    def get_real_child_model(cls, data: Dict[str, str]) -> str:
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
        if not isinstance(other, GsaTabularAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
