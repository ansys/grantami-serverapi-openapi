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


class GsaFloatSeriesPoint(ModelBase):
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
        "estimated": "bool",
        "x_value": "float",
        "y_high_value": "float",
        "y_low_value": "float",
    }

    attribute_map: dict[str, str] = {
        "estimated": "estimated",
        "x_value": "xValue",
        "y_high_value": "yHighValue",
        "y_low_value": "yLowValue",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        estimated: "bool",
        x_value: "float",
        y_high_value: "float",
        y_low_value: "float",
    ) -> None:
        """GsaFloatSeriesPoint - a model defined in Swagger

        Parameters
        ----------
        estimated: bool
        x_value: float
        y_high_value: float
        y_low_value: float
        """
        self._x_value: float
        self._y_low_value: float
        self._y_high_value: float
        self._estimated: bool

        self.x_value = x_value
        self.y_low_value = y_low_value
        self.y_high_value = y_high_value
        self.estimated = estimated

    @property
    def x_value(self) -> "float":
        """Gets the x_value of this GsaFloatSeriesPoint.

        Returns
        -------
        float
            The x_value of this GsaFloatSeriesPoint.
        """
        return self._x_value

    @x_value.setter
    def x_value(self, x_value: "float") -> None:
        """Sets the x_value of this GsaFloatSeriesPoint.

        Parameters
        ----------
        x_value: float
            The x_value of this GsaFloatSeriesPoint.
        """
        # Field is not nullable
        if x_value is None:
            raise ValueError("Invalid value for 'x_value', must not be 'None'")
        # Field is required
        if x_value is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'x_value', must not be 'Unset'")
        self._x_value = x_value

    @property
    def y_low_value(self) -> "float":
        """Gets the y_low_value of this GsaFloatSeriesPoint.

        Returns
        -------
        float
            The y_low_value of this GsaFloatSeriesPoint.
        """
        return self._y_low_value

    @y_low_value.setter
    def y_low_value(self, y_low_value: "float") -> None:
        """Sets the y_low_value of this GsaFloatSeriesPoint.

        Parameters
        ----------
        y_low_value: float
            The y_low_value of this GsaFloatSeriesPoint.
        """
        # Field is not nullable
        if y_low_value is None:
            raise ValueError("Invalid value for 'y_low_value', must not be 'None'")
        # Field is required
        if y_low_value is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'y_low_value', must not be 'Unset'")
        self._y_low_value = y_low_value

    @property
    def y_high_value(self) -> "float":
        """Gets the y_high_value of this GsaFloatSeriesPoint.

        Returns
        -------
        float
            The y_high_value of this GsaFloatSeriesPoint.
        """
        return self._y_high_value

    @y_high_value.setter
    def y_high_value(self, y_high_value: "float") -> None:
        """Sets the y_high_value of this GsaFloatSeriesPoint.

        Parameters
        ----------
        y_high_value: float
            The y_high_value of this GsaFloatSeriesPoint.
        """
        # Field is not nullable
        if y_high_value is None:
            raise ValueError("Invalid value for 'y_high_value', must not be 'None'")
        # Field is required
        if y_high_value is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'y_high_value', must not be 'Unset'")
        self._y_high_value = y_high_value

    @property
    def estimated(self) -> "bool":
        """Gets the estimated of this GsaFloatSeriesPoint.

        Returns
        -------
        bool
            The estimated of this GsaFloatSeriesPoint.
        """
        return self._estimated

    @estimated.setter
    def estimated(self, estimated: "bool") -> None:
        """Sets the estimated of this GsaFloatSeriesPoint.

        Parameters
        ----------
        estimated: bool
            The estimated of this GsaFloatSeriesPoint.
        """
        # Field is not nullable
        if estimated is None:
            raise ValueError("Invalid value for 'estimated', must not be 'None'")
        # Field is required
        if estimated is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'estimated', must not be 'Unset'")
        self._estimated = estimated

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
        if not isinstance(other, GsaFloatSeriesPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
