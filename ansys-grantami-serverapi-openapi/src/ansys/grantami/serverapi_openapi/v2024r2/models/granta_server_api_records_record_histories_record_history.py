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


class GrantaServerApiRecordsRecordHistoriesRecordHistory(ModelBase):
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
        "guid": "str",
        "is_folder": "bool",
        "record_versions": "list[GrantaServerApiRecordsRecordVersionsSlimRecordVersion]",
        "subsets": "list[GrantaServerApiSchemaSlimEntitiesSlimSubset]",
        "table": "GrantaServerApiSchemaSlimEntitiesSlimTable",
        "parent": "GrantaServerApiRecordsRecordHistoriesSlimRecordHistory",
    }

    attribute_map: dict[str, str] = {
        "guid": "guid",
        "is_folder": "isFolder",
        "record_versions": "recordVersions",
        "subsets": "subsets",
        "table": "table",
        "parent": "parent",
    }

    subtype_mapping: dict[str, str] = {
        "table": "GrantaServerApiSchemaSlimEntitiesSlimTable",
        "parent": "GrantaServerApiRecordsRecordHistoriesSlimRecordHistory",
        "recordVersions": "GrantaServerApiRecordsRecordVersionsSlimRecordVersion",
        "subsets": "GrantaServerApiSchemaSlimEntitiesSlimSubset",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        guid: "str",
        is_folder: "bool",
        record_versions: "list[GrantaServerApiRecordsRecordVersionsSlimRecordVersion]",
        subsets: "list[GrantaServerApiSchemaSlimEntitiesSlimSubset]",
        table: "GrantaServerApiSchemaSlimEntitiesSlimTable",
        parent: "GrantaServerApiRecordsRecordHistoriesSlimRecordHistory | Unset_Type" = Unset,
    ) -> None:
        """GrantaServerApiRecordsRecordHistoriesRecordHistory - a model defined in Swagger

        Parameters
        ----------
        guid: str
        is_folder: bool
        record_versions: list[GrantaServerApiRecordsRecordVersionsSlimRecordVersion]
        subsets: list[GrantaServerApiSchemaSlimEntitiesSlimSubset]
        table: GrantaServerApiSchemaSlimEntitiesSlimTable
        parent: GrantaServerApiRecordsRecordHistoriesSlimRecordHistory, optional
        """
        self._is_folder: bool
        self._table: GrantaServerApiSchemaSlimEntitiesSlimTable
        self._parent: GrantaServerApiRecordsRecordHistoriesSlimRecordHistory | Unset_Type = Unset
        self._record_versions: list[GrantaServerApiRecordsRecordVersionsSlimRecordVersion]
        self._subsets: list[GrantaServerApiSchemaSlimEntitiesSlimSubset]
        self._guid: str

        self.is_folder = is_folder
        self.table = table
        if parent is not Unset:
            self.parent = parent
        self.record_versions = record_versions
        self.subsets = subsets
        self.guid = guid

    @property
    def is_folder(self) -> "bool":
        """Gets the is_folder of this GrantaServerApiRecordsRecordHistoriesRecordHistory.

        Returns
        -------
        bool
            The is_folder of this GrantaServerApiRecordsRecordHistoriesRecordHistory.
        """
        return self._is_folder

    @is_folder.setter
    def is_folder(self, is_folder: "bool") -> None:
        """Sets the is_folder of this GrantaServerApiRecordsRecordHistoriesRecordHistory.

        Parameters
        ----------
        is_folder: bool
            The is_folder of this GrantaServerApiRecordsRecordHistoriesRecordHistory.
        """
        # Field is not nullable
        if is_folder is None:
            raise ValueError("Invalid value for 'is_folder', must not be 'None'")
        # Field is required
        if is_folder is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'is_folder', must not be 'Unset'")
        self._is_folder = is_folder

    @property
    def table(self) -> "GrantaServerApiSchemaSlimEntitiesSlimTable":
        """Gets the table of this GrantaServerApiRecordsRecordHistoriesRecordHistory.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimTable
            The table of this GrantaServerApiRecordsRecordHistoriesRecordHistory.
        """
        return self._table

    @table.setter
    def table(self, table: "GrantaServerApiSchemaSlimEntitiesSlimTable") -> None:
        """Sets the table of this GrantaServerApiRecordsRecordHistoriesRecordHistory.

        Parameters
        ----------
        table: GrantaServerApiSchemaSlimEntitiesSlimTable
            The table of this GrantaServerApiRecordsRecordHistoriesRecordHistory.
        """
        # Field is not nullable
        if table is None:
            raise ValueError("Invalid value for 'table', must not be 'None'")
        # Field is required
        if table is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'table', must not be 'Unset'")
        self._table = table

    @property
    def parent(self) -> "GrantaServerApiRecordsRecordHistoriesSlimRecordHistory | Unset_Type":
        """Gets the parent of this GrantaServerApiRecordsRecordHistoriesRecordHistory.

        Returns
        -------
        GrantaServerApiRecordsRecordHistoriesSlimRecordHistory | Unset_Type
            The parent of this GrantaServerApiRecordsRecordHistoriesRecordHistory.
        """
        return self._parent

    @parent.setter
    def parent(
        self, parent: "GrantaServerApiRecordsRecordHistoriesSlimRecordHistory | Unset_Type"
    ) -> None:
        """Sets the parent of this GrantaServerApiRecordsRecordHistoriesRecordHistory.

        Parameters
        ----------
        parent: GrantaServerApiRecordsRecordHistoriesSlimRecordHistory | Unset_Type
            The parent of this GrantaServerApiRecordsRecordHistoriesRecordHistory.
        """
        # Field is not nullable
        if parent is None:
            raise ValueError("Invalid value for 'parent', must not be 'None'")
        self._parent = parent

    @property
    def record_versions(self) -> "list[GrantaServerApiRecordsRecordVersionsSlimRecordVersion]":
        """Gets the record_versions of this GrantaServerApiRecordsRecordHistoriesRecordHistory.

        Returns
        -------
        list[GrantaServerApiRecordsRecordVersionsSlimRecordVersion]
            The record_versions of this GrantaServerApiRecordsRecordHistoriesRecordHistory.
        """
        return self._record_versions

    @record_versions.setter
    def record_versions(
        self, record_versions: "list[GrantaServerApiRecordsRecordVersionsSlimRecordVersion]"
    ) -> None:
        """Sets the record_versions of this GrantaServerApiRecordsRecordHistoriesRecordHistory.

        Parameters
        ----------
        record_versions: list[GrantaServerApiRecordsRecordVersionsSlimRecordVersion]
            The record_versions of this GrantaServerApiRecordsRecordHistoriesRecordHistory.
        """
        # Field is not nullable
        if record_versions is None:
            raise ValueError("Invalid value for 'record_versions', must not be 'None'")
        # Field is required
        if record_versions is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'record_versions', must not be 'Unset'")
        self._record_versions = record_versions

    @property
    def subsets(self) -> "list[GrantaServerApiSchemaSlimEntitiesSlimSubset]":
        """Gets the subsets of this GrantaServerApiRecordsRecordHistoriesRecordHistory.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimSubset]
            The subsets of this GrantaServerApiRecordsRecordHistoriesRecordHistory.
        """
        return self._subsets

    @subsets.setter
    def subsets(self, subsets: "list[GrantaServerApiSchemaSlimEntitiesSlimSubset]") -> None:
        """Sets the subsets of this GrantaServerApiRecordsRecordHistoriesRecordHistory.

        Parameters
        ----------
        subsets: list[GrantaServerApiSchemaSlimEntitiesSlimSubset]
            The subsets of this GrantaServerApiRecordsRecordHistoriesRecordHistory.
        """
        # Field is not nullable
        if subsets is None:
            raise ValueError("Invalid value for 'subsets', must not be 'None'")
        # Field is required
        if subsets is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'subsets', must not be 'Unset'")
        self._subsets = subsets

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiRecordsRecordHistoriesRecordHistory.

        Returns
        -------
        str
            The guid of this GrantaServerApiRecordsRecordHistoriesRecordHistory.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiRecordsRecordHistoriesRecordHistory.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiRecordsRecordHistoriesRecordHistory.
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
        if not isinstance(other, GrantaServerApiRecordsRecordHistoriesRecordHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
