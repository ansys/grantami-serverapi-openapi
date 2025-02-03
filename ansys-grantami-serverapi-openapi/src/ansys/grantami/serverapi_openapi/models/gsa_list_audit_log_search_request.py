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


class GsaListAuditLogSearchRequest(ModelBase):
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
        "list_actions_to_include": "list[GsaListAction]",
        "list_identifiers": "list[str]",
        "paging_options": "GsaListsPagingOptions",
    }

    attribute_map: dict[str, str] = {
        "list_actions_to_include": "listActionsToInclude",
        "list_identifiers": "listIdentifiers",
        "paging_options": "pagingOptions",
    }

    subtype_mapping: dict[str, str] = {
        "listActionsToInclude": "GsaListAction",
        "pagingOptions": "GsaListsPagingOptions",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        list_actions_to_include: "Union[list[GsaListAction], None, Unset_Type]" = Unset,
        list_identifiers: "Union[list[str], None, Unset_Type]" = Unset,
        paging_options: "Union[GsaListsPagingOptions, Unset_Type]" = Unset,
    ) -> None:
        """GsaListAuditLogSearchRequest - a model defined in Swagger

        Parameters
        ----------
        list_actions_to_include: list[GsaListAction], optional
        list_identifiers: list[str], optional
        paging_options: GsaListsPagingOptions, optional
        """
        self._list_identifiers: Union[list[str], None, Unset_Type] = Unset
        self._list_actions_to_include: Union[list[GsaListAction], None, Unset_Type] = Unset
        self._paging_options: Union[GsaListsPagingOptions, Unset_Type] = Unset

        if list_identifiers is not Unset:
            self.list_identifiers = list_identifiers
        if list_actions_to_include is not Unset:
            self.list_actions_to_include = list_actions_to_include
        if paging_options is not Unset:
            self.paging_options = paging_options

    @property
    def list_identifiers(self) -> "Union[list[str], None, Unset_Type]":
        """Gets the list_identifiers of this GsaListAuditLogSearchRequest.
        The lists to include actions for. If null, all items will be returned

        Returns
        -------
        Union[list[str], None, Unset_Type]
            The list_identifiers of this GsaListAuditLogSearchRequest.
        """
        return self._list_identifiers

    @list_identifiers.setter
    def list_identifiers(self, list_identifiers: "Union[list[str], None, Unset_Type]") -> None:
        """Sets the list_identifiers of this GsaListAuditLogSearchRequest.
        The lists to include actions for. If null, all items will be returned

        Parameters
        ----------
        list_identifiers: Union[list[str], None, Unset_Type]
            The list_identifiers of this GsaListAuditLogSearchRequest.
        """
        self._list_identifiers = list_identifiers

    @property
    def list_actions_to_include(self) -> "Union[list[GsaListAction], None, Unset_Type]":
        """Gets the list_actions_to_include of this GsaListAuditLogSearchRequest.
        The types of actions to include. If null, all action types will be returned

        Returns
        -------
        Union[list[GsaListAction], None, Unset_Type]
            The list_actions_to_include of this GsaListAuditLogSearchRequest.
        """
        return self._list_actions_to_include

    @list_actions_to_include.setter
    def list_actions_to_include(
        self, list_actions_to_include: "Union[list[GsaListAction], None, Unset_Type]"
    ) -> None:
        """Sets the list_actions_to_include of this GsaListAuditLogSearchRequest.
        The types of actions to include. If null, all action types will be returned

        Parameters
        ----------
        list_actions_to_include: Union[list[GsaListAction], None, Unset_Type]
            The list_actions_to_include of this GsaListAuditLogSearchRequest.
        """
        self._list_actions_to_include = list_actions_to_include

    @property
    def paging_options(self) -> "Union[GsaListsPagingOptions, Unset_Type]":
        """Gets the paging_options of this GsaListAuditLogSearchRequest.

        Returns
        -------
        Union[GsaListsPagingOptions, Unset_Type]
            The paging_options of this GsaListAuditLogSearchRequest.
        """
        return self._paging_options

    @paging_options.setter
    def paging_options(self, paging_options: "Union[GsaListsPagingOptions, Unset_Type]") -> None:
        """Sets the paging_options of this GsaListAuditLogSearchRequest.

        Parameters
        ----------
        paging_options: Union[GsaListsPagingOptions, Unset_Type]
            The paging_options of this GsaListAuditLogSearchRequest.
        """
        # Field is not nullable
        if paging_options is None:
            raise ValueError("Invalid value for 'paging_options', must not be 'None'")
        self._paging_options = paging_options

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
        if not isinstance(other, GsaListAuditLogSearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
