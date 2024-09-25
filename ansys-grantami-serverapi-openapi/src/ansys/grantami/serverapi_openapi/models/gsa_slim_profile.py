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


class GsaSlimProfile(ModelBase):
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
        "is_implicit": "bool",
        "key": "str",
        "name": "str",
        "group_name": "str",
        "guid": "str",
    }

    attribute_map: Dict[str, str] = {
        "is_implicit": "isImplicit",
        "key": "key",
        "name": "name",
        "group_name": "groupName",
        "guid": "guid",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        is_implicit: "bool",
        key: "str",
        name: "str",
        group_name: "Union[str, None, Unset_Type]" = Unset,
        guid: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaSlimProfile - a model defined in Swagger

        Parameters
        ----------
        is_implicit: bool
        key: str
        name: str
        group_name: str, optional
        guid: str, optional
        """
        self._key: str
        self._guid: Union[str, None, Unset_Type] = Unset
        self._group_name: Union[str, None, Unset_Type] = Unset
        self._is_implicit: bool
        self._name: str

        self.key = key
        if guid is not Unset:
            self.guid = guid
        if group_name is not Unset:
            self.group_name = group_name
        self.is_implicit = is_implicit
        self.name = name

    @property
    def key(self) -> "str":
        """Gets the key of this GsaSlimProfile.
        Key is a unique identifier of a profile. Separate from guid.

        Returns
        -------
        str
            The key of this GsaSlimProfile.
        """
        return self._key

    @key.setter
    def key(self, key: "str") -> None:
        """Sets the key of this GsaSlimProfile.
        Key is a unique identifier of a profile. Separate from guid.

        Parameters
        ----------
        key: str
            The key of this GsaSlimProfile.
        """
        # Field is not nullable
        if key is None:
            raise ValueError("Invalid value for 'key', must not be 'None'")
        # Field is required
        if key is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'key', must not be 'Unset'")
        self._key = key

    @property
    def guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the guid of this GsaSlimProfile.
        Guid is a unique identifier of a profile. Separate from key.

        Returns
        -------
        Union[str, None, Unset_Type]
            The guid of this GsaSlimProfile.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the guid of this GsaSlimProfile.
        Guid is a unique identifier of a profile. Separate from key.

        Parameters
        ----------
        guid: Union[str, None, Unset_Type]
            The guid of this GsaSlimProfile.
        """
        self._guid = guid

    @property
    def group_name(self) -> "Union[str, None, Unset_Type]":
        """Gets the group_name of this GsaSlimProfile.

        Returns
        -------
        Union[str, None, Unset_Type]
            The group_name of this GsaSlimProfile.
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name: "Union[str, None, Unset_Type]") -> None:
        """Sets the group_name of this GsaSlimProfile.

        Parameters
        ----------
        group_name: Union[str, None, Unset_Type]
            The group_name of this GsaSlimProfile.
        """
        self._group_name = group_name

    @property
    def is_implicit(self) -> "bool":
        """Gets the is_implicit of this GsaSlimProfile.

        Returns
        -------
        bool
            The is_implicit of this GsaSlimProfile.
        """
        return self._is_implicit

    @is_implicit.setter
    def is_implicit(self, is_implicit: "bool") -> None:
        """Sets the is_implicit of this GsaSlimProfile.

        Parameters
        ----------
        is_implicit: bool
            The is_implicit of this GsaSlimProfile.
        """
        # Field is not nullable
        if is_implicit is None:
            raise ValueError("Invalid value for 'is_implicit', must not be 'None'")
        # Field is required
        if is_implicit is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'is_implicit', must not be 'Unset'")
        self._is_implicit = is_implicit

    @property
    def name(self) -> "str":
        """Gets the name of this GsaSlimProfile.

        Returns
        -------
        str
            The name of this GsaSlimProfile.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GsaSlimProfile.

        Parameters
        ----------
        name: str
            The name of this GsaSlimProfile.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        # Field is required
        if name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'name', must not be 'Unset'")
        self._name = name

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
        if not isinstance(other, GsaSlimProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other