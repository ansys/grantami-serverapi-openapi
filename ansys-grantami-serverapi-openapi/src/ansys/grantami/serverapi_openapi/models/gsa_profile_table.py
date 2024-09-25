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

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaProfileTable(ModelBase):
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
        "database_guid": "str",
        "table_guid": "str",
        "database_fallback_hint": "str",
        "guid": "str",
        "layout_fallback_hint": "str",
        "layout_guid": "str",
        "subset_fallback_hint": "str",
        "subset_guid": "str",
        "table_fallback_hint": "str",
    }

    attribute_map: Dict[str, str] = {
        "database_guid": "databaseGuid",
        "table_guid": "tableGuid",
        "database_fallback_hint": "databaseFallbackHint",
        "guid": "guid",
        "layout_fallback_hint": "layoutFallbackHint",
        "layout_guid": "layoutGuid",
        "subset_fallback_hint": "subsetFallbackHint",
        "subset_guid": "subsetGuid",
        "table_fallback_hint": "tableFallbackHint",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        database_guid: "str",
        table_guid: "str",
        database_fallback_hint: "Union[str, None, Unset_Type]" = Unset,
        guid: "Union[str, None, Unset_Type]" = Unset,
        layout_fallback_hint: "Union[str, None, Unset_Type]" = Unset,
        layout_guid: "Union[str, None, Unset_Type]" = Unset,
        subset_fallback_hint: "Union[str, None, Unset_Type]" = Unset,
        subset_guid: "Union[str, None, Unset_Type]" = Unset,
        table_fallback_hint: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaProfileTable - a model defined in Swagger

        Parameters
        ----------
        database_guid: str
        table_guid: str
        database_fallback_hint: str, optional
        guid: str, optional
        layout_fallback_hint: str, optional
        layout_guid: str, optional
        subset_fallback_hint: str, optional
        subset_guid: str, optional
        table_fallback_hint: str, optional
        """
        self._subset_guid: Union[str, None, Unset_Type] = Unset
        self._subset_fallback_hint: Union[str, None, Unset_Type] = Unset
        self._layout_guid: Union[str, None, Unset_Type] = Unset
        self._layout_fallback_hint: Union[str, None, Unset_Type] = Unset
        self._guid: Union[str, None, Unset_Type] = Unset
        self._database_guid: str
        self._database_fallback_hint: Union[str, None, Unset_Type] = Unset
        self._table_guid: str
        self._table_fallback_hint: Union[str, None, Unset_Type] = Unset

        if subset_guid is not Unset:
            self.subset_guid = subset_guid
        if subset_fallback_hint is not Unset:
            self.subset_fallback_hint = subset_fallback_hint
        if layout_guid is not Unset:
            self.layout_guid = layout_guid
        if layout_fallback_hint is not Unset:
            self.layout_fallback_hint = layout_fallback_hint
        if guid is not Unset:
            self.guid = guid
        self.database_guid = database_guid
        if database_fallback_hint is not Unset:
            self.database_fallback_hint = database_fallback_hint
        self.table_guid = table_guid
        if table_fallback_hint is not Unset:
            self.table_fallback_hint = table_fallback_hint

    @property
    def subset_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the subset_guid of this GsaProfileTable.

        Returns
        -------
        Union[str, None, Unset_Type]
            The subset_guid of this GsaProfileTable.
        """
        return self._subset_guid

    @subset_guid.setter
    def subset_guid(self, subset_guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the subset_guid of this GsaProfileTable.

        Parameters
        ----------
        subset_guid: Union[str, None, Unset_Type]
            The subset_guid of this GsaProfileTable.
        """
        self._subset_guid = subset_guid

    @property
    def subset_fallback_hint(self) -> "Union[str, None, Unset_Type]":
        """Gets the subset_fallback_hint of this GsaProfileTable.

        Returns
        -------
        Union[str, None, Unset_Type]
            The subset_fallback_hint of this GsaProfileTable.
        """
        return self._subset_fallback_hint

    @subset_fallback_hint.setter
    def subset_fallback_hint(self, subset_fallback_hint: "Union[str, None, Unset_Type]") -> None:
        """Sets the subset_fallback_hint of this GsaProfileTable.

        Parameters
        ----------
        subset_fallback_hint: Union[str, None, Unset_Type]
            The subset_fallback_hint of this GsaProfileTable.
        """
        self._subset_fallback_hint = subset_fallback_hint

    @property
    def layout_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the layout_guid of this GsaProfileTable.

        Returns
        -------
        Union[str, None, Unset_Type]
            The layout_guid of this GsaProfileTable.
        """
        return self._layout_guid

    @layout_guid.setter
    def layout_guid(self, layout_guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the layout_guid of this GsaProfileTable.

        Parameters
        ----------
        layout_guid: Union[str, None, Unset_Type]
            The layout_guid of this GsaProfileTable.
        """
        self._layout_guid = layout_guid

    @property
    def layout_fallback_hint(self) -> "Union[str, None, Unset_Type]":
        """Gets the layout_fallback_hint of this GsaProfileTable.

        Returns
        -------
        Union[str, None, Unset_Type]
            The layout_fallback_hint of this GsaProfileTable.
        """
        return self._layout_fallback_hint

    @layout_fallback_hint.setter
    def layout_fallback_hint(self, layout_fallback_hint: "Union[str, None, Unset_Type]") -> None:
        """Sets the layout_fallback_hint of this GsaProfileTable.

        Parameters
        ----------
        layout_fallback_hint: Union[str, None, Unset_Type]
            The layout_fallback_hint of this GsaProfileTable.
        """
        self._layout_fallback_hint = layout_fallback_hint

    @property
    def guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the guid of this GsaProfileTable.

        Returns
        -------
        Union[str, None, Unset_Type]
            The guid of this GsaProfileTable.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the guid of this GsaProfileTable.

        Parameters
        ----------
        guid: Union[str, None, Unset_Type]
            The guid of this GsaProfileTable.
        """
        self._guid = guid

    @property
    def database_guid(self) -> "str":
        """Gets the database_guid of this GsaProfileTable.

        Returns
        -------
        str
            The database_guid of this GsaProfileTable.
        """
        return self._database_guid

    @database_guid.setter
    def database_guid(self, database_guid: "str") -> None:
        """Sets the database_guid of this GsaProfileTable.

        Parameters
        ----------
        database_guid: str
            The database_guid of this GsaProfileTable.
        """
        # Field is not nullable
        if database_guid is None:
            raise ValueError("Invalid value for 'database_guid', must not be 'None'")
        # Field is required
        if database_guid is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'database_guid', must not be 'Unset'")
        self._database_guid = database_guid

    @property
    def database_fallback_hint(self) -> "Union[str, None, Unset_Type]":
        """Gets the database_fallback_hint of this GsaProfileTable.

        Returns
        -------
        Union[str, None, Unset_Type]
            The database_fallback_hint of this GsaProfileTable.
        """
        return self._database_fallback_hint

    @database_fallback_hint.setter
    def database_fallback_hint(
        self, database_fallback_hint: "Union[str, None, Unset_Type]"
    ) -> None:
        """Sets the database_fallback_hint of this GsaProfileTable.

        Parameters
        ----------
        database_fallback_hint: Union[str, None, Unset_Type]
            The database_fallback_hint of this GsaProfileTable.
        """
        self._database_fallback_hint = database_fallback_hint

    @property
    def table_guid(self) -> "str":
        """Gets the table_guid of this GsaProfileTable.

        Returns
        -------
        str
            The table_guid of this GsaProfileTable.
        """
        return self._table_guid

    @table_guid.setter
    def table_guid(self, table_guid: "str") -> None:
        """Sets the table_guid of this GsaProfileTable.

        Parameters
        ----------
        table_guid: str
            The table_guid of this GsaProfileTable.
        """
        # Field is not nullable
        if table_guid is None:
            raise ValueError("Invalid value for 'table_guid', must not be 'None'")
        # Field is required
        if table_guid is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'table_guid', must not be 'Unset'")
        self._table_guid = table_guid

    @property
    def table_fallback_hint(self) -> "Union[str, None, Unset_Type]":
        """Gets the table_fallback_hint of this GsaProfileTable.

        Returns
        -------
        Union[str, None, Unset_Type]
            The table_fallback_hint of this GsaProfileTable.
        """
        return self._table_fallback_hint

    @table_fallback_hint.setter
    def table_fallback_hint(self, table_fallback_hint: "Union[str, None, Unset_Type]") -> None:
        """Sets the table_fallback_hint of this GsaProfileTable.

        Parameters
        ----------
        table_fallback_hint: Union[str, None, Unset_Type]
            The table_fallback_hint of this GsaProfileTable.
        """
        self._table_fallback_hint = table_fallback_hint

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
        if not isinstance(other, GsaProfileTable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other