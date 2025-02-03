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


class GsaPagingOptions(ModelBase):
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
        "keep_alive_in_minutes": "int",
        "page_number": "int",
        "page_size": "int",
    }

    attribute_map: dict[str, str] = {
        "keep_alive_in_minutes": "keepAliveInMinutes",
        "page_number": "pageNumber",
        "page_size": "pageSize",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        keep_alive_in_minutes: "Union[int, None, Unset_Type]" = Unset,
        page_number: "Union[int, None, Unset_Type]" = Unset,
        page_size: "Union[int, Unset_Type]" = Unset,
    ) -> None:
        """GsaPagingOptions - a model defined in Swagger

        Parameters
        ----------
        keep_alive_in_minutes: int, optional
        page_number: int, optional
        page_size: int, optional
        """
        self._page_size: Union[int, Unset_Type] = Unset
        self._keep_alive_in_minutes: Union[int, None, Unset_Type] = Unset
        self._page_number: Union[int, None, Unset_Type] = Unset

        if page_size is not Unset:
            self.page_size = page_size
        if keep_alive_in_minutes is not Unset:
            self.keep_alive_in_minutes = keep_alive_in_minutes
        if page_number is not Unset:
            self.page_number = page_number

    @property
    def page_size(self) -> "Union[int, Unset_Type]":
        """Gets the page_size of this GsaPagingOptions.
        The number of results that should be returned in each page

        Returns
        -------
        Union[int, Unset_Type]
            The page_size of this GsaPagingOptions.
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size: "Union[int, Unset_Type]") -> None:
        """Sets the page_size of this GsaPagingOptions.
        The number of results that should be returned in each page

        Parameters
        ----------
        page_size: Union[int, Unset_Type]
            The page_size of this GsaPagingOptions.
        """
        # Field is not nullable
        if page_size is None:
            raise ValueError("Invalid value for 'page_size', must not be 'None'")
        self._page_size = page_size

    @property
    def keep_alive_in_minutes(self) -> "Union[int, None, Unset_Type]":
        """Gets the keep_alive_in_minutes of this GsaPagingOptions.
        The length of time that the paginated search should be kept in memory

        Returns
        -------
        Union[int, None, Unset_Type]
            The keep_alive_in_minutes of this GsaPagingOptions.
        """
        return self._keep_alive_in_minutes

    @keep_alive_in_minutes.setter
    def keep_alive_in_minutes(self, keep_alive_in_minutes: "Union[int, None, Unset_Type]") -> None:
        """Sets the keep_alive_in_minutes of this GsaPagingOptions.
        The length of time that the paginated search should be kept in memory

        Parameters
        ----------
        keep_alive_in_minutes: Union[int, None, Unset_Type]
            The keep_alive_in_minutes of this GsaPagingOptions.
        """
        self._keep_alive_in_minutes = keep_alive_in_minutes

    @property
    def page_number(self) -> "Union[int, None, Unset_Type]":
        """Gets the page_number of this GsaPagingOptions.
        (Optional) the (1-indexed) number of the page to return from the search. No pages are returned if not provided

        Returns
        -------
        Union[int, None, Unset_Type]
            The page_number of this GsaPagingOptions.
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number: "Union[int, None, Unset_Type]") -> None:
        """Sets the page_number of this GsaPagingOptions.
        (Optional) the (1-indexed) number of the page to return from the search. No pages are returned if not provided

        Parameters
        ----------
        page_number: Union[int, None, Unset_Type]
            The page_number of this GsaPagingOptions.
        """
        self._page_number = page_number

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
        if not isinstance(other, GsaPagingOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
