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


class GsaResponseOptions(ModelBase):
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
        "include_record_list_items": "bool",
        "include_user_actions": "bool",
        "include_user_permissions": "bool",
    }

    attribute_map: Dict[str, str] = {
        "include_record_list_items": "includeRecordListItems",
        "include_user_actions": "includeUserActions",
        "include_user_permissions": "includeUserPermissions",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        include_record_list_items: "Union[bool, Unset_Type]" = Unset,
        include_user_actions: "Union[bool, Unset_Type]" = Unset,
        include_user_permissions: "Union[bool, Unset_Type]" = Unset,
    ) -> None:
        """GsaResponseOptions - a model defined in Swagger

        Parameters
        ----------
        include_record_list_items: bool, optional
        include_user_actions: bool, optional
        include_user_permissions: bool, optional
        """
        self._include_user_actions: Union[bool, Unset_Type] = Unset
        self._include_user_permissions: Union[bool, Unset_Type] = Unset
        self._include_record_list_items: Union[bool, Unset_Type] = Unset

        if include_user_actions is not Unset:
            self.include_user_actions = include_user_actions
        if include_user_permissions is not Unset:
            self.include_user_permissions = include_user_permissions
        if include_record_list_items is not Unset:
            self.include_record_list_items = include_record_list_items

    @property
    def include_user_actions(self) -> "Union[bool, Unset_Type]":
        """Gets the include_user_actions of this GsaResponseOptions.

        Returns
        -------
        Union[bool, Unset_Type]
            The include_user_actions of this GsaResponseOptions.
        """
        return self._include_user_actions

    @include_user_actions.setter
    def include_user_actions(self, include_user_actions: "Union[bool, Unset_Type]") -> None:
        """Sets the include_user_actions of this GsaResponseOptions.

        Parameters
        ----------
        include_user_actions: Union[bool, Unset_Type]
            The include_user_actions of this GsaResponseOptions.
        """
        # Field is not nullable
        if include_user_actions is None:
            raise ValueError("Invalid value for 'include_user_actions', must not be 'None'")
        self._include_user_actions = include_user_actions

    @property
    def include_user_permissions(self) -> "Union[bool, Unset_Type]":
        """Gets the include_user_permissions of this GsaResponseOptions.

        Returns
        -------
        Union[bool, Unset_Type]
            The include_user_permissions of this GsaResponseOptions.
        """
        return self._include_user_permissions

    @include_user_permissions.setter
    def include_user_permissions(self, include_user_permissions: "Union[bool, Unset_Type]") -> None:
        """Sets the include_user_permissions of this GsaResponseOptions.

        Parameters
        ----------
        include_user_permissions: Union[bool, Unset_Type]
            The include_user_permissions of this GsaResponseOptions.
        """
        # Field is not nullable
        if include_user_permissions is None:
            raise ValueError("Invalid value for 'include_user_permissions', must not be 'None'")
        self._include_user_permissions = include_user_permissions

    @property
    def include_record_list_items(self) -> "Union[bool, Unset_Type]":
        """Gets the include_record_list_items of this GsaResponseOptions.

        Returns
        -------
        Union[bool, Unset_Type]
            The include_record_list_items of this GsaResponseOptions.
        """
        return self._include_record_list_items

    @include_record_list_items.setter
    def include_record_list_items(
        self, include_record_list_items: "Union[bool, Unset_Type]"
    ) -> None:
        """Sets the include_record_list_items of this GsaResponseOptions.

        Parameters
        ----------
        include_record_list_items: Union[bool, Unset_Type]
            The include_record_list_items of this GsaResponseOptions.
        """
        # Field is not nullable
        if include_record_list_items is None:
            raise ValueError("Invalid value for 'include_record_list_items', must not be 'None'")
        self._include_record_list_items = include_record_list_items

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
        if not isinstance(other, GsaResponseOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other