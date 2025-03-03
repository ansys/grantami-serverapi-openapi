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

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaDataExportBinaryData(ModelBase):
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
        "content_type": "str",
        "data": "str",
        "description": "str",
        "name": "str",
    }

    attribute_map: dict[str, str] = {
        "content_type": "contentType",
        "data": "data",
        "description": "description",
        "name": "name",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        content_type: "Union[str, None, Unset_Type]" = Unset,
        data: "Union[str, None, Unset_Type]" = Unset,
        description: "Union[str, None, Unset_Type]" = Unset,
        name: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaDataExportBinaryData - a model defined in Swagger

        Parameters
        ----------
        content_type: str, optional
        data: str, optional
        description: str, optional
        name: str, optional
        """
        self._name: Union[str, None, Unset_Type] = Unset
        self._description: Union[str, None, Unset_Type] = Unset
        self._content_type: Union[str, None, Unset_Type] = Unset
        self._data: Union[str, None, Unset_Type] = Unset

        if name is not Unset:
            self.name = name
        if description is not Unset:
            self.description = description
        if content_type is not Unset:
            self.content_type = content_type
        if data is not Unset:
            self.data = data

    @property
    def name(self) -> "Union[str, None, Unset_Type]":
        """Gets the name of this GsaDataExportBinaryData.

        Returns
        -------
        Union[str, None, Unset_Type]
            The name of this GsaDataExportBinaryData.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, None, Unset_Type]") -> None:
        """Sets the name of this GsaDataExportBinaryData.

        Parameters
        ----------
        name: Union[str, None, Unset_Type]
            The name of this GsaDataExportBinaryData.
        """
        self._name = name

    @property
    def description(self) -> "Union[str, None, Unset_Type]":
        """Gets the description of this GsaDataExportBinaryData.

        Returns
        -------
        Union[str, None, Unset_Type]
            The description of this GsaDataExportBinaryData.
        """
        return self._description

    @description.setter
    def description(self, description: "Union[str, None, Unset_Type]") -> None:
        """Sets the description of this GsaDataExportBinaryData.

        Parameters
        ----------
        description: Union[str, None, Unset_Type]
            The description of this GsaDataExportBinaryData.
        """
        self._description = description

    @property
    def content_type(self) -> "Union[str, None, Unset_Type]":
        """Gets the content_type of this GsaDataExportBinaryData.

        Returns
        -------
        Union[str, None, Unset_Type]
            The content_type of this GsaDataExportBinaryData.
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type: "Union[str, None, Unset_Type]") -> None:
        """Sets the content_type of this GsaDataExportBinaryData.

        Parameters
        ----------
        content_type: Union[str, None, Unset_Type]
            The content_type of this GsaDataExportBinaryData.
        """
        self._content_type = content_type

    @property
    def data(self) -> "Union[str, None, Unset_Type]":
        """Gets the data of this GsaDataExportBinaryData.

        Returns
        -------
        Union[str, None, Unset_Type]
            The data of this GsaDataExportBinaryData.
        """
        return self._data

    @data.setter
    def data(self, data: "Union[str, None, Unset_Type]") -> None:
        """Sets the data of this GsaDataExportBinaryData.

        Parameters
        ----------
        data: Union[str, None, Unset_Type]
            The data of this GsaDataExportBinaryData.
        """
        self._data = data

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
        if not isinstance(other, GsaDataExportBinaryData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
