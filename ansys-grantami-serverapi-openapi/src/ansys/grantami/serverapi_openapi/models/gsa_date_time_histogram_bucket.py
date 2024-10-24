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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaDateTimeHistogramBucket(ModelBase):
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
        "count": "int",
        "lower": "datetime",
    }

    attribute_map: dict[str, str] = {
        "count": "count",
        "lower": "lower",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        count: "Union[int, Unset_Type]" = Unset,
        lower: "Union[datetime, Unset_Type]" = Unset,
    ) -> None:
        """GsaDateTimeHistogramBucket - a model defined in Swagger

        Parameters
        ----------
        count: int, optional
        lower: datetime, optional
        """
        self._lower: Union[datetime, Unset_Type] = Unset
        self._count: Union[int, Unset_Type] = Unset

        if lower is not Unset:
            self.lower = lower
        if count is not Unset:
            self.count = count

    @property
    def lower(self) -> "Union[datetime, Unset_Type]":
        """Gets the lower of this GsaDateTimeHistogramBucket.

        Returns
        -------
        Union[datetime, Unset_Type]
            The lower of this GsaDateTimeHistogramBucket.
        """
        return self._lower

    @lower.setter
    def lower(self, lower: "Union[datetime, Unset_Type]") -> None:
        """Sets the lower of this GsaDateTimeHistogramBucket.

        Parameters
        ----------
        lower: Union[datetime, Unset_Type]
            The lower of this GsaDateTimeHistogramBucket.
        """
        # Field is not nullable
        if lower is None:
            raise ValueError("Invalid value for 'lower', must not be 'None'")
        self._lower = lower

    @property
    def count(self) -> "Union[int, Unset_Type]":
        """Gets the count of this GsaDateTimeHistogramBucket.

        Returns
        -------
        Union[int, Unset_Type]
            The count of this GsaDateTimeHistogramBucket.
        """
        return self._count

    @count.setter
    def count(self, count: "Union[int, Unset_Type]") -> None:
        """Sets the count of this GsaDateTimeHistogramBucket.

        Parameters
        ----------
        count: Union[int, Unset_Type]
            The count of this GsaDateTimeHistogramBucket.
        """
        # Field is not nullable
        if count is None:
            raise ValueError("Invalid value for 'count', must not be 'None'")
        self._count = count

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
        if not isinstance(other, GsaDateTimeHistogramBucket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
