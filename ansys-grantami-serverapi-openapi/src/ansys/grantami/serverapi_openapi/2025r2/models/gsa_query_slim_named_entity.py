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


class GsaQuerySlimNamedEntity(ModelBase):
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
        "name": "str",
    }

    attribute_map: dict[str, str] = {
        "guid": "guid",
        "name": "name",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        guid: "Union[str, None, Unset_Type]" = Unset,
        name: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaQuerySlimNamedEntity - a model defined in Swagger

        Parameters
        ----------
        guid: str, optional
        name: str, optional
        """
        self._name: Union[str, None, Unset_Type] = Unset
        self._guid: Union[str, None, Unset_Type] = Unset

        if name is not Unset:
            self.name = name
        if guid is not Unset:
            self.guid = guid

    @property
    def name(self) -> "Union[str, None, Unset_Type]":
        """Gets the name of this GsaQuerySlimNamedEntity.

        Returns
        -------
        Union[str, None, Unset_Type]
            The name of this GsaQuerySlimNamedEntity.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, None, Unset_Type]") -> None:
        """Sets the name of this GsaQuerySlimNamedEntity.

        Parameters
        ----------
        name: Union[str, None, Unset_Type]
            The name of this GsaQuerySlimNamedEntity.
        """
        self._name = name

    @property
    def guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the guid of this GsaQuerySlimNamedEntity.

        Returns
        -------
        Union[str, None, Unset_Type]
            The guid of this GsaQuerySlimNamedEntity.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the guid of this GsaQuerySlimNamedEntity.

        Parameters
        ----------
        guid: Union[str, None, Unset_Type]
            The guid of this GsaQuerySlimNamedEntity.
        """
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
        if not isinstance(other, GsaQuerySlimNamedEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
