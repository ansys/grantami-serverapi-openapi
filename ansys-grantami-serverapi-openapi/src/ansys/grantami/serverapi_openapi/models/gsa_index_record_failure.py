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


class GsaIndexRecordFailure(ModelBase):
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
        "error": "str",
        "record_history_guid": "str",
        "record_name": "str",
        "record_was_oversized": "bool",
    }

    attribute_map: dict[str, str] = {
        "error": "error",
        "record_history_guid": "recordHistoryGuid",
        "record_name": "recordName",
        "record_was_oversized": "recordWasOversized",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        error: "Union[str, None, Unset_Type]" = Unset,
        record_history_guid: "Union[str, Unset_Type]" = Unset,
        record_name: "Union[str, None, Unset_Type]" = Unset,
        record_was_oversized: "Union[bool, Unset_Type]" = Unset,
    ) -> None:
        """GsaIndexRecordFailure - a model defined in Swagger

        Parameters
        ----------
        error: str, optional
        record_history_guid: str, optional
        record_name: str, optional
        record_was_oversized: bool, optional
        """
        self._record_history_guid: Union[str, Unset_Type] = Unset
        self._record_name: Union[str, None, Unset_Type] = Unset
        self._error: Union[str, None, Unset_Type] = Unset
        self._record_was_oversized: Union[bool, Unset_Type] = Unset

        if record_history_guid is not Unset:
            self.record_history_guid = record_history_guid
        if record_name is not Unset:
            self.record_name = record_name
        if error is not Unset:
            self.error = error
        if record_was_oversized is not Unset:
            self.record_was_oversized = record_was_oversized

    @property
    def record_history_guid(self) -> "Union[str, Unset_Type]":
        """Gets the record_history_guid of this GsaIndexRecordFailure.

        Returns
        -------
        Union[str, Unset_Type]
            The record_history_guid of this GsaIndexRecordFailure.
        """
        return self._record_history_guid

    @record_history_guid.setter
    def record_history_guid(self, record_history_guid: "Union[str, Unset_Type]") -> None:
        """Sets the record_history_guid of this GsaIndexRecordFailure.

        Parameters
        ----------
        record_history_guid: Union[str, Unset_Type]
            The record_history_guid of this GsaIndexRecordFailure.
        """
        # Field is not nullable
        if record_history_guid is None:
            raise ValueError("Invalid value for 'record_history_guid', must not be 'None'")
        self._record_history_guid = record_history_guid

    @property
    def record_name(self) -> "Union[str, None, Unset_Type]":
        """Gets the record_name of this GsaIndexRecordFailure.

        Returns
        -------
        Union[str, None, Unset_Type]
            The record_name of this GsaIndexRecordFailure.
        """
        return self._record_name

    @record_name.setter
    def record_name(self, record_name: "Union[str, None, Unset_Type]") -> None:
        """Sets the record_name of this GsaIndexRecordFailure.

        Parameters
        ----------
        record_name: Union[str, None, Unset_Type]
            The record_name of this GsaIndexRecordFailure.
        """
        self._record_name = record_name

    @property
    def error(self) -> "Union[str, None, Unset_Type]":
        """Gets the error of this GsaIndexRecordFailure.
        This is the error message from the indexing exception. It may have been returned directly from Elasticsearch.

        Returns
        -------
        Union[str, None, Unset_Type]
            The error of this GsaIndexRecordFailure.
        """
        return self._error

    @error.setter
    def error(self, error: "Union[str, None, Unset_Type]") -> None:
        """Sets the error of this GsaIndexRecordFailure.
        This is the error message from the indexing exception. It may have been returned directly from Elasticsearch.

        Parameters
        ----------
        error: Union[str, None, Unset_Type]
            The error of this GsaIndexRecordFailure.
        """
        self._error = error

    @property
    def record_was_oversized(self) -> "Union[bool, Unset_Type]":
        """Gets the record_was_oversized of this GsaIndexRecordFailure.
        Records that contain a large amount of data are intentionally not sent to the index. This size limit is configurable through  MIServer.exe.config

        Returns
        -------
        Union[bool, Unset_Type]
            The record_was_oversized of this GsaIndexRecordFailure.
        """
        return self._record_was_oversized

    @record_was_oversized.setter
    def record_was_oversized(self, record_was_oversized: "Union[bool, Unset_Type]") -> None:
        """Sets the record_was_oversized of this GsaIndexRecordFailure.
        Records that contain a large amount of data are intentionally not sent to the index. This size limit is configurable through  MIServer.exe.config

        Parameters
        ----------
        record_was_oversized: Union[bool, Unset_Type]
            The record_was_oversized of this GsaIndexRecordFailure.
        """
        # Field is not nullable
        if record_was_oversized is None:
            raise ValueError("Invalid value for 'record_was_oversized', must not be 'None'")
        self._record_was_oversized = record_was_oversized

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
        if not isinstance(other, GsaIndexRecordFailure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
