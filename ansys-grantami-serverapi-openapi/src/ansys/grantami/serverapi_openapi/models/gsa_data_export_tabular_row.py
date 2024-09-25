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


class GsaDataExportTabularRow(ModelBase):
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
        "linked_data": "list[GsaRecordWithData]",
        "linked_records": "list[GsaRecordReference]",
        "linking_value": "str",
        "local_data": "list[GsaDataExportDatum]",
        "rolled_up_data": "list[GsaDataExportRollupDatum]",
        "row_guid": "str",
        "row_number": "int",
    }

    attribute_map: Dict[str, str] = {
        "linked_data": "linkedData",
        "linked_records": "linkedRecords",
        "linking_value": "linkingValue",
        "local_data": "localData",
        "rolled_up_data": "rolledUpData",
        "row_guid": "rowGuid",
        "row_number": "rowNumber",
    }

    subtype_mapping: Dict[str, str] = {
        "localData": "GsaDataExportDatum",
        "linkedRecords": "GsaRecordReference",
        "linkedData": "GsaRecordWithData",
        "rolledUpData": "GsaDataExportRollupDatum",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        linked_data: "Union[List[GsaRecordWithData], None, Unset_Type]" = Unset,
        linked_records: "Union[List[GsaRecordReference], None, Unset_Type]" = Unset,
        linking_value: "Union[str, None, Unset_Type]" = Unset,
        local_data: "Union[List[GsaDataExportDatum], None, Unset_Type]" = Unset,
        rolled_up_data: "Union[List[GsaDataExportRollupDatum], None, Unset_Type]" = Unset,
        row_guid: "Union[str, Unset_Type]" = Unset,
        row_number: "Union[int, Unset_Type]" = Unset,
    ) -> None:
        """GsaDataExportTabularRow - a model defined in Swagger

        Parameters
        ----------
        linked_data: List[GsaRecordWithData], optional
        linked_records: List[GsaRecordReference], optional
        linking_value: str, optional
        local_data: List[GsaDataExportDatum], optional
        rolled_up_data: List[GsaDataExportRollupDatum], optional
        row_guid: str, optional
        row_number: int, optional
        """
        self._row_guid: Union[str, Unset_Type] = Unset
        self._linking_value: Union[str, None, Unset_Type] = Unset
        self._row_number: Union[int, Unset_Type] = Unset
        self._local_data: Union[List[GsaDataExportDatum], None, Unset_Type] = Unset
        self._linked_records: Union[List[GsaRecordReference], None, Unset_Type] = Unset
        self._linked_data: Union[List[GsaRecordWithData], None, Unset_Type] = Unset
        self._rolled_up_data: Union[List[GsaDataExportRollupDatum], None, Unset_Type] = Unset

        if row_guid is not Unset:
            self.row_guid = row_guid
        if linking_value is not Unset:
            self.linking_value = linking_value
        if row_number is not Unset:
            self.row_number = row_number
        if local_data is not Unset:
            self.local_data = local_data
        if linked_records is not Unset:
            self.linked_records = linked_records
        if linked_data is not Unset:
            self.linked_data = linked_data
        if rolled_up_data is not Unset:
            self.rolled_up_data = rolled_up_data

    @property
    def row_guid(self) -> "Union[str, Unset_Type]":
        """Gets the row_guid of this GsaDataExportTabularRow.

        Returns
        -------
        Union[str, Unset_Type]
            The row_guid of this GsaDataExportTabularRow.
        """
        return self._row_guid

    @row_guid.setter
    def row_guid(self, row_guid: "Union[str, Unset_Type]") -> None:
        """Sets the row_guid of this GsaDataExportTabularRow.

        Parameters
        ----------
        row_guid: Union[str, Unset_Type]
            The row_guid of this GsaDataExportTabularRow.
        """
        # Field is not nullable
        if row_guid is None:
            raise ValueError("Invalid value for 'row_guid', must not be 'None'")
        self._row_guid = row_guid

    @property
    def linking_value(self) -> "Union[str, None, Unset_Type]":
        """Gets the linking_value of this GsaDataExportTabularRow.

        Returns
        -------
        Union[str, None, Unset_Type]
            The linking_value of this GsaDataExportTabularRow.
        """
        return self._linking_value

    @linking_value.setter
    def linking_value(self, linking_value: "Union[str, None, Unset_Type]") -> None:
        """Sets the linking_value of this GsaDataExportTabularRow.

        Parameters
        ----------
        linking_value: Union[str, None, Unset_Type]
            The linking_value of this GsaDataExportTabularRow.
        """
        self._linking_value = linking_value

    @property
    def row_number(self) -> "Union[int, Unset_Type]":
        """Gets the row_number of this GsaDataExportTabularRow.

        Returns
        -------
        Union[int, Unset_Type]
            The row_number of this GsaDataExportTabularRow.
        """
        return self._row_number

    @row_number.setter
    def row_number(self, row_number: "Union[int, Unset_Type]") -> None:
        """Sets the row_number of this GsaDataExportTabularRow.

        Parameters
        ----------
        row_number: Union[int, Unset_Type]
            The row_number of this GsaDataExportTabularRow.
        """
        # Field is not nullable
        if row_number is None:
            raise ValueError("Invalid value for 'row_number', must not be 'None'")
        self._row_number = row_number

    @property
    def local_data(self) -> "Union[List[GsaDataExportDatum], None, Unset_Type]":
        """Gets the local_data of this GsaDataExportTabularRow.

        Returns
        -------
        Union[List[GsaDataExportDatum], None, Unset_Type]
            The local_data of this GsaDataExportTabularRow.
        """
        return self._local_data

    @local_data.setter
    def local_data(self, local_data: "Union[List[GsaDataExportDatum], None, Unset_Type]") -> None:
        """Sets the local_data of this GsaDataExportTabularRow.

        Parameters
        ----------
        local_data: Union[List[GsaDataExportDatum], None, Unset_Type]
            The local_data of this GsaDataExportTabularRow.
        """
        self._local_data = local_data

    @property
    def linked_records(self) -> "Union[List[GsaRecordReference], None, Unset_Type]":
        """Gets the linked_records of this GsaDataExportTabularRow.
        Records linked to this tabular row (only populated if the target table/attribute was provided in the request)

        Returns
        -------
        Union[List[GsaRecordReference], None, Unset_Type]
            The linked_records of this GsaDataExportTabularRow.
        """
        return self._linked_records

    @linked_records.setter
    def linked_records(
        self, linked_records: "Union[List[GsaRecordReference], None, Unset_Type]"
    ) -> None:
        """Sets the linked_records of this GsaDataExportTabularRow.
        Records linked to this tabular row (only populated if the target table/attribute was provided in the request)

        Parameters
        ----------
        linked_records: Union[List[GsaRecordReference], None, Unset_Type]
            The linked_records of this GsaDataExportTabularRow.
        """
        self._linked_records = linked_records

    @property
    def linked_data(self) -> "Union[List[GsaRecordWithData], None, Unset_Type]":
        """Gets the linked_data of this GsaDataExportTabularRow.
        Data for the linked records, if the request included linked data to export

        Returns
        -------
        Union[List[GsaRecordWithData], None, Unset_Type]
            The linked_data of this GsaDataExportTabularRow.
        """
        return self._linked_data

    @linked_data.setter
    def linked_data(self, linked_data: "Union[List[GsaRecordWithData], None, Unset_Type]") -> None:
        """Sets the linked_data of this GsaDataExportTabularRow.
        Data for the linked records, if the request included linked data to export

        Parameters
        ----------
        linked_data: Union[List[GsaRecordWithData], None, Unset_Type]
            The linked_data of this GsaDataExportTabularRow.
        """
        self._linked_data = linked_data

    @property
    def rolled_up_data(self) -> "Union[List[GsaDataExportRollupDatum], None, Unset_Type]":
        """Gets the rolled_up_data of this GsaDataExportTabularRow.

        Returns
        -------
        Union[List[GsaDataExportRollupDatum], None, Unset_Type]
            The rolled_up_data of this GsaDataExportTabularRow.
        """
        return self._rolled_up_data

    @rolled_up_data.setter
    def rolled_up_data(
        self, rolled_up_data: "Union[List[GsaDataExportRollupDatum], None, Unset_Type]"
    ) -> None:
        """Sets the rolled_up_data of this GsaDataExportTabularRow.

        Parameters
        ----------
        rolled_up_data: Union[List[GsaDataExportRollupDatum], None, Unset_Type]
            The rolled_up_data of this GsaDataExportTabularRow.
        """
        self._rolled_up_data = rolled_up_data

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
        if not isinstance(other, GsaDataExportTabularRow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other