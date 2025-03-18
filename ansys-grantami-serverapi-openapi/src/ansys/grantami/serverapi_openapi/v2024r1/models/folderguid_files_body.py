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


class FolderguidFilesBody(ModelBase):
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
        "content_disposition": "str",
        "content_type": "str",
        "description": "str",
        "file_name": "str",
        "headers": "dict(str, list[str])",
        "length": "int",
        "name": "str",
    }

    attribute_map: dict[str, str] = {
        "content_disposition": "ContentDisposition",
        "content_type": "ContentType",
        "description": "description",
        "file_name": "FileName",
        "headers": "Headers",
        "length": "Length",
        "name": "Name",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        content_disposition: "Union[str, Unset_Type]" = Unset,
        content_type: "Union[str, Unset_Type]" = Unset,
        description: "Union[str, Unset_Type]" = Unset,
        file_name: "Union[str, Unset_Type]" = Unset,
        headers: "Union[dict[str, list[str]], Unset_Type]" = Unset,
        length: "Union[int, Unset_Type]" = Unset,
        name: "Union[str, Unset_Type]" = Unset,
    ) -> None:
        """FolderguidFilesBody - a model defined in Swagger

        Parameters
        ----------
        content_disposition: str, optional
        content_type: str, optional
        description: str, optional
        file_name: str, optional
        headers: dict[str, list[str]], optional
        length: int, optional
        name: str, optional
        """
        self._content_type: Union[str, Unset_Type] = Unset
        self._content_disposition: Union[str, Unset_Type] = Unset
        self._headers: Union[dict[str, list[str]], Unset_Type] = Unset
        self._length: Union[int, Unset_Type] = Unset
        self._name: Union[str, Unset_Type] = Unset
        self._file_name: Union[str, Unset_Type] = Unset
        self._description: Union[str, Unset_Type] = Unset

        if content_type is not Unset:
            self.content_type = content_type
        if content_disposition is not Unset:
            self.content_disposition = content_disposition
        if headers is not Unset:
            self.headers = headers
        if length is not Unset:
            self.length = length
        if name is not Unset:
            self.name = name
        if file_name is not Unset:
            self.file_name = file_name
        if description is not Unset:
            self.description = description

    @property
    def content_type(self) -> "Union[str, Unset_Type]":
        """Gets the content_type of this FolderguidFilesBody.

        Returns
        -------
        Union[str, Unset_Type]
            The content_type of this FolderguidFilesBody.
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type: "Union[str, Unset_Type]") -> None:
        """Sets the content_type of this FolderguidFilesBody.

        Parameters
        ----------
        content_type: Union[str, Unset_Type]
            The content_type of this FolderguidFilesBody.
        """
        # Field is not nullable
        if content_type is None:
            raise ValueError("Invalid value for 'content_type', must not be 'None'")
        self._content_type = content_type

    @property
    def content_disposition(self) -> "Union[str, Unset_Type]":
        """Gets the content_disposition of this FolderguidFilesBody.

        Returns
        -------
        Union[str, Unset_Type]
            The content_disposition of this FolderguidFilesBody.
        """
        return self._content_disposition

    @content_disposition.setter
    def content_disposition(self, content_disposition: "Union[str, Unset_Type]") -> None:
        """Sets the content_disposition of this FolderguidFilesBody.

        Parameters
        ----------
        content_disposition: Union[str, Unset_Type]
            The content_disposition of this FolderguidFilesBody.
        """
        # Field is not nullable
        if content_disposition is None:
            raise ValueError("Invalid value for 'content_disposition', must not be 'None'")
        self._content_disposition = content_disposition

    @property
    def headers(self) -> "Union[dict[str, list[str]], Unset_Type]":
        """Gets the headers of this FolderguidFilesBody.

        Returns
        -------
        Union[dict[str, list[str]], Unset_Type]
            The headers of this FolderguidFilesBody.
        """
        return self._headers

    @headers.setter
    def headers(self, headers: "Union[dict[str, list[str]], Unset_Type]") -> None:
        """Sets the headers of this FolderguidFilesBody.

        Parameters
        ----------
        headers: Union[dict[str, list[str]], Unset_Type]
            The headers of this FolderguidFilesBody.
        """
        # Field is not nullable
        if headers is None:
            raise ValueError("Invalid value for 'headers', must not be 'None'")
        self._headers = headers

    @property
    def length(self) -> "Union[int, Unset_Type]":
        """Gets the length of this FolderguidFilesBody.

        Returns
        -------
        Union[int, Unset_Type]
            The length of this FolderguidFilesBody.
        """
        return self._length

    @length.setter
    def length(self, length: "Union[int, Unset_Type]") -> None:
        """Sets the length of this FolderguidFilesBody.

        Parameters
        ----------
        length: Union[int, Unset_Type]
            The length of this FolderguidFilesBody.
        """
        # Field is not nullable
        if length is None:
            raise ValueError("Invalid value for 'length', must not be 'None'")
        self._length = length

    @property
    def name(self) -> "Union[str, Unset_Type]":
        """Gets the name of this FolderguidFilesBody.

        Returns
        -------
        Union[str, Unset_Type]
            The name of this FolderguidFilesBody.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, Unset_Type]") -> None:
        """Sets the name of this FolderguidFilesBody.

        Parameters
        ----------
        name: Union[str, Unset_Type]
            The name of this FolderguidFilesBody.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

    @property
    def file_name(self) -> "Union[str, Unset_Type]":
        """Gets the file_name of this FolderguidFilesBody.

        Returns
        -------
        Union[str, Unset_Type]
            The file_name of this FolderguidFilesBody.
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name: "Union[str, Unset_Type]") -> None:
        """Sets the file_name of this FolderguidFilesBody.

        Parameters
        ----------
        file_name: Union[str, Unset_Type]
            The file_name of this FolderguidFilesBody.
        """
        # Field is not nullable
        if file_name is None:
            raise ValueError("Invalid value for 'file_name', must not be 'None'")
        self._file_name = file_name

    @property
    def description(self) -> "Union[str, Unset_Type]":
        """Gets the description of this FolderguidFilesBody.

        Returns
        -------
        Union[str, Unset_Type]
            The description of this FolderguidFilesBody.
        """
        return self._description

    @description.setter
    def description(self, description: "Union[str, Unset_Type]") -> None:
        """Sets the description of this FolderguidFilesBody.

        Parameters
        ----------
        description: Union[str, Unset_Type]
            The description of this FolderguidFilesBody.
        """
        # Field is not nullable
        if description is None:
            raise ValueError("Invalid value for 'description', must not be 'None'")
        self._description = description

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
        if not isinstance(other, FolderguidFilesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
