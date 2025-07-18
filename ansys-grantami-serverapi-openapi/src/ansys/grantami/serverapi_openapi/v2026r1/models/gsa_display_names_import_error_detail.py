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


class GsaDisplayNamesImportErrorDetail(ModelBase):
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
        "message": "str",
        "column_header": "str",
        "field_value": "str",
        "item_type": "str",
        "reason": "GsaDisplayNamesImportErrorReason",
        "row_index": "int",
    }

    attribute_map: dict[str, str] = {
        "message": "message",
        "column_header": "columnHeader",
        "field_value": "fieldValue",
        "item_type": "itemType",
        "reason": "reason",
        "row_index": "rowIndex",
    }

    subtype_mapping: dict[str, str] = {
        "reason": "GsaDisplayNamesImportErrorReason",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        message: "str",
        column_header: "str | None | Unset_Type" = Unset,
        field_value: "str | None | Unset_Type" = Unset,
        item_type: "str | None | Unset_Type" = Unset,
        reason: "GsaDisplayNamesImportErrorReason | Unset_Type" = Unset,
        row_index: "int | None | Unset_Type" = Unset,
    ) -> None:
        """GsaDisplayNamesImportErrorDetail - a model defined in Swagger

        Parameters
        ----------
        message: str
        column_header: str | None, optional
        field_value: str | None, optional
        item_type: str | None, optional
        reason: GsaDisplayNamesImportErrorReason, optional
        row_index: int | None, optional
        """
        self._message: str
        self._reason: GsaDisplayNamesImportErrorReason | Unset_Type = Unset
        self._row_index: int | None | Unset_Type = Unset
        self._field_value: str | None | Unset_Type = Unset
        self._column_header: str | None | Unset_Type = Unset
        self._item_type: str | None | Unset_Type = Unset

        self.message = message
        if reason is not Unset:
            self.reason = reason
        if row_index is not Unset:
            self.row_index = row_index
        if field_value is not Unset:
            self.field_value = field_value
        if column_header is not Unset:
            self.column_header = column_header
        if item_type is not Unset:
            self.item_type = item_type

    @property
    def message(self) -> "str":
        """Gets the message of this GsaDisplayNamesImportErrorDetail.

        Returns
        -------
        str
            The message of this GsaDisplayNamesImportErrorDetail.
        """
        return self._message

    @message.setter
    def message(self, message: "str") -> None:
        """Sets the message of this GsaDisplayNamesImportErrorDetail.

        Parameters
        ----------
        message: str
            The message of this GsaDisplayNamesImportErrorDetail.
        """
        # Field is not nullable
        if message is None:
            raise ValueError("Invalid value for 'message', must not be 'None'")
        # Field is required
        if message is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'message', must not be 'Unset'")
        self._message = message

    @property
    def reason(self) -> "GsaDisplayNamesImportErrorReason | Unset_Type":
        """Gets the reason of this GsaDisplayNamesImportErrorDetail.

        Returns
        -------
        GsaDisplayNamesImportErrorReason | Unset_Type
            The reason of this GsaDisplayNamesImportErrorDetail.
        """
        return self._reason

    @reason.setter
    def reason(self, reason: "GsaDisplayNamesImportErrorReason | Unset_Type") -> None:
        """Sets the reason of this GsaDisplayNamesImportErrorDetail.

        Parameters
        ----------
        reason: GsaDisplayNamesImportErrorReason | Unset_Type
            The reason of this GsaDisplayNamesImportErrorDetail.
        """
        # Field is not nullable
        if reason is None:
            raise ValueError("Invalid value for 'reason', must not be 'None'")
        self._reason = reason

    @property
    def row_index(self) -> "int | None | Unset_Type":
        """Gets the row_index of this GsaDisplayNamesImportErrorDetail.

        Returns
        -------
        int | None | Unset_Type
            The row_index of this GsaDisplayNamesImportErrorDetail.
        """
        return self._row_index

    @row_index.setter
    def row_index(self, row_index: "int | None | Unset_Type") -> None:
        """Sets the row_index of this GsaDisplayNamesImportErrorDetail.

        Parameters
        ----------
        row_index: int | None | Unset_Type
            The row_index of this GsaDisplayNamesImportErrorDetail.
        """
        self._row_index = row_index

    @property
    def field_value(self) -> "str | None | Unset_Type":
        """Gets the field_value of this GsaDisplayNamesImportErrorDetail.

        Returns
        -------
        str | None | Unset_Type
            The field_value of this GsaDisplayNamesImportErrorDetail.
        """
        return self._field_value

    @field_value.setter
    def field_value(self, field_value: "str | None | Unset_Type") -> None:
        """Sets the field_value of this GsaDisplayNamesImportErrorDetail.

        Parameters
        ----------
        field_value: str | None | Unset_Type
            The field_value of this GsaDisplayNamesImportErrorDetail.
        """
        self._field_value = field_value

    @property
    def column_header(self) -> "str | None | Unset_Type":
        """Gets the column_header of this GsaDisplayNamesImportErrorDetail.

        Returns
        -------
        str | None | Unset_Type
            The column_header of this GsaDisplayNamesImportErrorDetail.
        """
        return self._column_header

    @column_header.setter
    def column_header(self, column_header: "str | None | Unset_Type") -> None:
        """Sets the column_header of this GsaDisplayNamesImportErrorDetail.

        Parameters
        ----------
        column_header: str | None | Unset_Type
            The column_header of this GsaDisplayNamesImportErrorDetail.
        """
        self._column_header = column_header

    @property
    def item_type(self) -> "str | None | Unset_Type":
        """Gets the item_type of this GsaDisplayNamesImportErrorDetail.

        Returns
        -------
        str | None | Unset_Type
            The item_type of this GsaDisplayNamesImportErrorDetail.
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type: "str | None | Unset_Type") -> None:
        """Sets the item_type of this GsaDisplayNamesImportErrorDetail.

        Parameters
        ----------
        item_type: str | None | Unset_Type
            The item_type of this GsaDisplayNamesImportErrorDetail.
        """
        self._item_type = item_type

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
        if not isinstance(other, GsaDisplayNamesImportErrorDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
