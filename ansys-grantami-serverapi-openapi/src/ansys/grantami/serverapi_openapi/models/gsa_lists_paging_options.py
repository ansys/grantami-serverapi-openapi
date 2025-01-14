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


class GsaListsPagingOptions(ModelBase):
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
        "page_size": "int",
        "start_index": "int",
    }

    attribute_map: dict[str, str] = {
        "page_size": "pageSize",
        "start_index": "startIndex",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        page_size: "Union[int, None, Unset_Type]" = Unset,
        start_index: "Union[int, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaListsPagingOptions - a model defined in Swagger

        Parameters
        ----------
        page_size: int, optional
        start_index: int, optional
        """
        self._start_index: Union[int, None, Unset_Type] = Unset
        self._page_size: Union[int, None, Unset_Type] = Unset

        if start_index is not Unset:
            self.start_index = start_index
        if page_size is not Unset:
            self.page_size = page_size

    @property
    def start_index(self) -> "Union[int, None, Unset_Type]":
        """Gets the start_index of this GsaListsPagingOptions.
        The index of the first item in the collection to be returned. If not provided it will start at index 0.

        Returns
        -------
        Union[int, None, Unset_Type]
            The start_index of this GsaListsPagingOptions.
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index: "Union[int, None, Unset_Type]") -> None:
        """Sets the start_index of this GsaListsPagingOptions.
        The index of the first item in the collection to be returned. If not provided it will start at index 0.

        Parameters
        ----------
        start_index: Union[int, None, Unset_Type]
            The start_index of this GsaListsPagingOptions.
        """
        self._start_index = start_index

    @property
    def page_size(self) -> "Union[int, None, Unset_Type]":
        """Gets the page_size of this GsaListsPagingOptions.
        The number of items to be returned per page. If not provided the number of returned lists will be unlimited.

        Returns
        -------
        Union[int, None, Unset_Type]
            The page_size of this GsaListsPagingOptions.
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size: "Union[int, None, Unset_Type]") -> None:
        """Sets the page_size of this GsaListsPagingOptions.
        The number of items to be returned per page. If not provided the number of returned lists will be unlimited.

        Parameters
        ----------
        page_size: Union[int, None, Unset_Type]
            The page_size of this GsaListsPagingOptions.
        """
        self._page_size = page_size

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
        if not isinstance(other, GsaListsPagingOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
