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


class GsaGetJobsResponse(ModelBase):
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
        "results": "list[GsaJob]",
        "total_result_count": "int",
    }

    attribute_map: Dict[str, str] = {
        "results": "results",
        "total_result_count": "totalResultCount",
    }

    subtype_mapping: Dict[str, str] = {
        "results": "GsaJob",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        results: "Union[List[GsaJob], None, Unset_Type]" = Unset,
        total_result_count: "Union[int, Unset_Type]" = Unset,
    ) -> None:
        """GsaGetJobsResponse - a model defined in Swagger

        Parameters
        ----------
        results: List[GsaJob], optional
        total_result_count: int, optional
        """
        self._total_result_count: Union[int, Unset_Type] = Unset
        self._results: Union[List[GsaJob], None, Unset_Type] = Unset

        if total_result_count is not Unset:
            self.total_result_count = total_result_count
        if results is not Unset:
            self.results = results

    @property
    def total_result_count(self) -> "Union[int, Unset_Type]":
        """Gets the total_result_count of this GsaGetJobsResponse.

        Returns
        -------
        Union[int, Unset_Type]
            The total_result_count of this GsaGetJobsResponse.
        """
        return self._total_result_count

    @total_result_count.setter
    def total_result_count(self, total_result_count: "Union[int, Unset_Type]") -> None:
        """Sets the total_result_count of this GsaGetJobsResponse.

        Parameters
        ----------
        total_result_count: Union[int, Unset_Type]
            The total_result_count of this GsaGetJobsResponse.
        """
        # Field is not nullable
        if total_result_count is None:
            raise ValueError("Invalid value for 'total_result_count', must not be 'None'")
        self._total_result_count = total_result_count

    @property
    def results(self) -> "Union[List[GsaJob], None, Unset_Type]":
        """Gets the results of this GsaGetJobsResponse.

        Returns
        -------
        Union[List[GsaJob], None, Unset_Type]
            The results of this GsaGetJobsResponse.
        """
        return self._results

    @results.setter
    def results(self, results: "Union[List[GsaJob], None, Unset_Type]") -> None:
        """Sets the results of this GsaGetJobsResponse.

        Parameters
        ----------
        results: Union[List[GsaJob], None, Unset_Type]
            The results of this GsaGetJobsResponse.
        """
        self._results = results

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
        if not isinstance(other, GsaGetJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other