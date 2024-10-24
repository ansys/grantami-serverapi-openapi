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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaDataExportRequest(ModelBase):
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
        "attributes": "list[GsaAttributeToExport]",
        "record_properties": "list[GsaRecordProperty]",
        "record_history_guids": "list[str]",
        "record_history_identities": "list[int]",
    }

    attribute_map: dict[str, str] = {
        "attributes": "attributes",
        "record_properties": "recordProperties",
        "record_history_guids": "recordHistoryGuids",
        "record_history_identities": "recordHistoryIdentities",
    }

    subtype_mapping: dict[str, str] = {
        "attributes": "GsaAttributeToExport",
        "recordProperties": "GsaRecordProperty",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attributes: "list[GsaAttributeToExport]",
        record_properties: "list[GsaRecordProperty]",
        record_history_guids: "Union[list[str], None, Unset_Type]" = Unset,
        record_history_identities: "Union[list[int], None, Unset_Type]" = Unset,
    ) -> None:
        """GsaDataExportRequest - a model defined in Swagger

        Parameters
        ----------
        attributes: list[GsaAttributeToExport]
        record_properties: list[GsaRecordProperty]
        record_history_guids: list[str], optional
        record_history_identities: list[int], optional
        """
        self._attributes: list[GsaAttributeToExport]
        self._record_properties: list[GsaRecordProperty]
        self._record_history_identities: Union[list[int], None, Unset_Type] = Unset
        self._record_history_guids: Union[list[str], None, Unset_Type] = Unset

        self.attributes = attributes
        self.record_properties = record_properties
        if record_history_identities is not Unset:
            self.record_history_identities = record_history_identities
        if record_history_guids is not Unset:
            self.record_history_guids = record_history_guids

    @property
    def attributes(self) -> "list[GsaAttributeToExport]":
        """Gets the attributes of this GsaDataExportRequest.

        Returns
        -------
        list[GsaAttributeToExport]
            The attributes of this GsaDataExportRequest.
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes: "list[GsaAttributeToExport]") -> None:
        """Sets the attributes of this GsaDataExportRequest.

        Parameters
        ----------
        attributes: list[GsaAttributeToExport]
            The attributes of this GsaDataExportRequest.
        """
        # Field is not nullable
        if attributes is None:
            raise ValueError("Invalid value for 'attributes', must not be 'None'")
        # Field is required
        if attributes is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'attributes', must not be 'Unset'")
        self._attributes = attributes

    @property
    def record_properties(self) -> "list[GsaRecordProperty]":
        """Gets the record_properties of this GsaDataExportRequest.

        Returns
        -------
        list[GsaRecordProperty]
            The record_properties of this GsaDataExportRequest.
        """
        return self._record_properties

    @record_properties.setter
    def record_properties(self, record_properties: "list[GsaRecordProperty]") -> None:
        """Sets the record_properties of this GsaDataExportRequest.

        Parameters
        ----------
        record_properties: list[GsaRecordProperty]
            The record_properties of this GsaDataExportRequest.
        """
        # Field is not nullable
        if record_properties is None:
            raise ValueError("Invalid value for 'record_properties', must not be 'None'")
        # Field is required
        if record_properties is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'record_properties', must not be 'Unset'")
        self._record_properties = record_properties

    @property
    def record_history_identities(self) -> "Union[list[int], None, Unset_Type]":
        """Gets the record_history_identities of this GsaDataExportRequest.

        Returns
        -------
        Union[list[int], None, Unset_Type]
            The record_history_identities of this GsaDataExportRequest.
        """
        return self._record_history_identities

    @record_history_identities.setter
    def record_history_identities(
        self, record_history_identities: "Union[list[int], None, Unset_Type]"
    ) -> None:
        """Sets the record_history_identities of this GsaDataExportRequest.

        Parameters
        ----------
        record_history_identities: Union[list[int], None, Unset_Type]
            The record_history_identities of this GsaDataExportRequest.
        """
        self._record_history_identities = record_history_identities

    @property
    def record_history_guids(self) -> "Union[list[str], None, Unset_Type]":
        """Gets the record_history_guids of this GsaDataExportRequest.

        Returns
        -------
        Union[list[str], None, Unset_Type]
            The record_history_guids of this GsaDataExportRequest.
        """
        return self._record_history_guids

    @record_history_guids.setter
    def record_history_guids(
        self, record_history_guids: "Union[list[str], None, Unset_Type]"
    ) -> None:
        """Sets the record_history_guids of this GsaDataExportRequest.

        Parameters
        ----------
        record_history_guids: Union[list[str], None, Unset_Type]
            The record_history_guids of this GsaDataExportRequest.
        """
        self._record_history_guids = record_history_guids

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
        if not isinstance(other, GsaDataExportRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
