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


class GsaSearchDetail(ModelBase):
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
        "criteria": "str",
        "description": "str",
        "name": "str",
        "notes": "str",
    }

    attribute_map: dict[str, str] = {
        "criteria": "criteria",
        "description": "description",
        "name": "name",
        "notes": "notes",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        criteria: "Union[str, None, Unset_Type]" = Unset,
        description: "Union[str, None, Unset_Type]" = Unset,
        name: "Union[str, None, Unset_Type]" = Unset,
        notes: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaSearchDetail - a model defined in Swagger

        Parameters
        ----------
        criteria: str, optional
        description: str, optional
        name: str, optional
        notes: str, optional
        """
        self._name: Union[str, None, Unset_Type] = Unset
        self._description: Union[str, None, Unset_Type] = Unset
        self._notes: Union[str, None, Unset_Type] = Unset
        self._criteria: Union[str, None, Unset_Type] = Unset

        if name is not Unset:
            self.name = name
        if description is not Unset:
            self.description = description
        if notes is not Unset:
            self.notes = notes
        if criteria is not Unset:
            self.criteria = criteria

    @property
    def name(self) -> "Union[str, None, Unset_Type]":
        """Gets the name of this GsaSearchDetail.

        Returns
        -------
        Union[str, None, Unset_Type]
            The name of this GsaSearchDetail.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, None, Unset_Type]") -> None:
        """Sets the name of this GsaSearchDetail.

        Parameters
        ----------
        name: Union[str, None, Unset_Type]
            The name of this GsaSearchDetail.
        """
        self._name = name

    @property
    def description(self) -> "Union[str, None, Unset_Type]":
        """Gets the description of this GsaSearchDetail.

        Returns
        -------
        Union[str, None, Unset_Type]
            The description of this GsaSearchDetail.
        """
        return self._description

    @description.setter
    def description(self, description: "Union[str, None, Unset_Type]") -> None:
        """Sets the description of this GsaSearchDetail.

        Parameters
        ----------
        description: Union[str, None, Unset_Type]
            The description of this GsaSearchDetail.
        """
        self._description = description

    @property
    def notes(self) -> "Union[str, None, Unset_Type]":
        """Gets the notes of this GsaSearchDetail.

        Returns
        -------
        Union[str, None, Unset_Type]
            The notes of this GsaSearchDetail.
        """
        return self._notes

    @notes.setter
    def notes(self, notes: "Union[str, None, Unset_Type]") -> None:
        """Sets the notes of this GsaSearchDetail.

        Parameters
        ----------
        notes: Union[str, None, Unset_Type]
            The notes of this GsaSearchDetail.
        """
        self._notes = notes

    @property
    def criteria(self) -> "Union[str, None, Unset_Type]":
        """Gets the criteria of this GsaSearchDetail.

        Returns
        -------
        Union[str, None, Unset_Type]
            The criteria of this GsaSearchDetail.
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria: "Union[str, None, Unset_Type]") -> None:
        """Sets the criteria of this GsaSearchDetail.

        Parameters
        ----------
        criteria: Union[str, None, Unset_Type]
            The criteria of this GsaSearchDetail.
        """
        self._criteria = criteria

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
        if not isinstance(other, GsaSearchDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
