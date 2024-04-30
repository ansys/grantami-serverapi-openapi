# Copyright (C) 2021 - 2024 ANSYS, Inc. and/or its affiliates.
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


class GrantaServerApiDataExportDataExportRequest(ModelBase):
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
        "attributes": "list[GrantaServerApiDataExportAttributeToExport]",
        "record_history_identities": "list[int]",
        "record_properties": "list[GrantaServerApiRecordProperty]",
    }

    attribute_map: Dict[str, str] = {
        "attributes": "attributes",
        "record_history_identities": "recordHistoryIdentities",
        "record_properties": "recordProperties",
    }

    subtype_mapping: Dict[str, str] = {
        "attributes": "GrantaServerApiDataExportAttributeToExport",
        "recordProperties": "GrantaServerApiRecordProperty",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attributes: "Union[List[GrantaServerApiDataExportAttributeToExport], None, Unset_Type]" = Unset,
        record_history_identities: "Union[List[int], None, Unset_Type]" = Unset,
        record_properties: "Union[List[GrantaServerApiRecordProperty], None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiDataExportDataExportRequest - a model defined in Swagger

        Parameters
        ----------
        attributes: List[GrantaServerApiDataExportAttributeToExport], optional
        record_history_identities: List[int], optional
        record_properties: List[GrantaServerApiRecordProperty], optional
        """
        self._attributes: Union[
            List[GrantaServerApiDataExportAttributeToExport], None, Unset_Type
        ] = Unset
        self._record_properties: Union[List[GrantaServerApiRecordProperty], None, Unset_Type] = (
            Unset
        )
        self._record_history_identities: Union[List[int], None, Unset_Type] = Unset

        if attributes is not Unset:
            self.attributes = attributes
        if record_properties is not Unset:
            self.record_properties = record_properties
        if record_history_identities is not Unset:
            self.record_history_identities = record_history_identities

    @property
    def attributes(
        self,
    ) -> "Union[List[GrantaServerApiDataExportAttributeToExport], None, Unset_Type]":
        """Gets the attributes of this GrantaServerApiDataExportDataExportRequest.

        Returns
        -------
        Union[List[GrantaServerApiDataExportAttributeToExport], None, Unset_Type]
            The attributes of this GrantaServerApiDataExportDataExportRequest.
        """
        return self._attributes

    @attributes.setter
    def attributes(
        self,
        attributes: "Union[List[GrantaServerApiDataExportAttributeToExport], None, Unset_Type]",
    ) -> None:
        """Sets the attributes of this GrantaServerApiDataExportDataExportRequest.

        Parameters
        ----------
        attributes: Union[List[GrantaServerApiDataExportAttributeToExport], None, Unset_Type]
            The attributes of this GrantaServerApiDataExportDataExportRequest.
        """
        self._attributes = attributes

    @property
    def record_properties(self) -> "Union[List[GrantaServerApiRecordProperty], None, Unset_Type]":
        """Gets the record_properties of this GrantaServerApiDataExportDataExportRequest.

        Returns
        -------
        Union[List[GrantaServerApiRecordProperty], None, Unset_Type]
            The record_properties of this GrantaServerApiDataExportDataExportRequest.
        """
        return self._record_properties

    @record_properties.setter
    def record_properties(
        self, record_properties: "Union[List[GrantaServerApiRecordProperty], None, Unset_Type]"
    ) -> None:
        """Sets the record_properties of this GrantaServerApiDataExportDataExportRequest.

        Parameters
        ----------
        record_properties: Union[List[GrantaServerApiRecordProperty], None, Unset_Type]
            The record_properties of this GrantaServerApiDataExportDataExportRequest.
        """
        self._record_properties = record_properties

    @property
    def record_history_identities(self) -> "Union[List[int], None, Unset_Type]":
        """Gets the record_history_identities of this GrantaServerApiDataExportDataExportRequest.

        Returns
        -------
        Union[List[int], None, Unset_Type]
            The record_history_identities of this GrantaServerApiDataExportDataExportRequest.
        """
        return self._record_history_identities

    @record_history_identities.setter
    def record_history_identities(
        self, record_history_identities: "Union[List[int], None, Unset_Type]"
    ) -> None:
        """Sets the record_history_identities of this GrantaServerApiDataExportDataExportRequest.

        Parameters
        ----------
        record_history_identities: Union[List[int], None, Unset_Type]
            The record_history_identities of this GrantaServerApiDataExportDataExportRequest.
        """
        self._record_history_identities = record_history_identities

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
        if not isinstance(other, GrantaServerApiDataExportDataExportRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
