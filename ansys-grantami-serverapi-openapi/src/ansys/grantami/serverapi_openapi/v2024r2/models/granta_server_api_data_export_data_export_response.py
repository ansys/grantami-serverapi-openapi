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


class GrantaServerApiDataExportDataExportResponse(ModelBase):
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
        "failures": "list[GrantaServerApiDataExportExportFailuresExportFailure]",
        "results": "list[GrantaServerApiDataExportRecordWithData]",
    }

    attribute_map: dict[str, str] = {
        "failures": "failures",
        "results": "results",
    }

    subtype_mapping: dict[str, str] = {
        "results": "GrantaServerApiDataExportRecordWithData",
        "failures": "GrantaServerApiDataExportExportFailuresExportFailure",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        failures: "list[GrantaServerApiDataExportExportFailuresExportFailure]",
        results: "list[GrantaServerApiDataExportRecordWithData]",
    ) -> None:
        """GrantaServerApiDataExportDataExportResponse - a model defined in Swagger

        Parameters
        ----------
        failures: list[GrantaServerApiDataExportExportFailuresExportFailure]
        results: list[GrantaServerApiDataExportRecordWithData]
        """
        self._results: list[GrantaServerApiDataExportRecordWithData]
        self._failures: list[GrantaServerApiDataExportExportFailuresExportFailure]

        self.results = results
        self.failures = failures

    @property
    def results(self) -> "list[GrantaServerApiDataExportRecordWithData]":
        """Gets the results of this GrantaServerApiDataExportDataExportResponse.

        Returns
        -------
        list[GrantaServerApiDataExportRecordWithData]
            The results of this GrantaServerApiDataExportDataExportResponse.
        """
        return self._results

    @results.setter
    def results(self, results: "list[GrantaServerApiDataExportRecordWithData]") -> None:
        """Sets the results of this GrantaServerApiDataExportDataExportResponse.

        Parameters
        ----------
        results: list[GrantaServerApiDataExportRecordWithData]
            The results of this GrantaServerApiDataExportDataExportResponse.
        """
        # Field is not nullable
        if results is None:
            raise ValueError("Invalid value for 'results', must not be 'None'")
        # Field is required
        if results is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'results', must not be 'Unset'")
        self._results = results

    @property
    def failures(self) -> "list[GrantaServerApiDataExportExportFailuresExportFailure]":
        """Gets the failures of this GrantaServerApiDataExportDataExportResponse.
        List the records that were requested, but that we failed to export any data for.

        Returns
        -------
        list[GrantaServerApiDataExportExportFailuresExportFailure]
            The failures of this GrantaServerApiDataExportDataExportResponse.
        """
        return self._failures

    @failures.setter
    def failures(
        self, failures: "list[GrantaServerApiDataExportExportFailuresExportFailure]"
    ) -> None:
        """Sets the failures of this GrantaServerApiDataExportDataExportResponse.
        List the records that were requested, but that we failed to export any data for.

        Parameters
        ----------
        failures: list[GrantaServerApiDataExportExportFailuresExportFailure]
            The failures of this GrantaServerApiDataExportDataExportResponse.
        """
        # Field is not nullable
        if failures is None:
            raise ValueError("Invalid value for 'failures', must not be 'None'")
        # Field is required
        if failures is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'failures', must not be 'Unset'")
        self._failures = failures

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
        if not isinstance(other, GrantaServerApiDataExportDataExportResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
