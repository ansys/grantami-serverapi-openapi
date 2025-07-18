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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaDataExportSeriesPoint(ModelBase):
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
        "is_estimated": "bool",
        "x_name": "str",
        "x_value": "float",
        "y_high_value": "float",
        "y_low_value": "float",
    }

    attribute_map: dict[str, str] = {
        "is_estimated": "isEstimated",
        "x_name": "xName",
        "x_value": "xValue",
        "y_high_value": "yHighValue",
        "y_low_value": "yLowValue",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        is_estimated: "bool",
        x_name: "str | None | Unset_Type" = Unset,
        x_value: "float | Unset_Type" = Unset,
        y_high_value: "float | Unset_Type" = Unset,
        y_low_value: "float | Unset_Type" = Unset,
    ) -> None:
        """GsaDataExportSeriesPoint - a model defined in Swagger

        Parameters
        ----------
        is_estimated: bool
        x_name: str | None, optional
        x_value: float, optional
        y_high_value: float, optional
        y_low_value: float, optional
        """
        self._x_value: float | Unset_Type = Unset
        self._x_name: str | None | Unset_Type = Unset
        self._y_low_value: float | Unset_Type = Unset
        self._y_high_value: float | Unset_Type = Unset
        self._is_estimated: bool

        if x_value is not Unset:
            self.x_value = x_value
        if x_name is not Unset:
            self.x_name = x_name
        if y_low_value is not Unset:
            self.y_low_value = y_low_value
        if y_high_value is not Unset:
            self.y_high_value = y_high_value
        self.is_estimated = is_estimated

    @property
    def x_value(self) -> "float | Unset_Type":
        """Gets the x_value of this GsaDataExportSeriesPoint.

        Returns
        -------
        float | Unset_Type
            The x_value of this GsaDataExportSeriesPoint.
        """
        return self._x_value

    @x_value.setter
    def x_value(self, x_value: "float | Unset_Type") -> None:
        """Sets the x_value of this GsaDataExportSeriesPoint.

        Parameters
        ----------
        x_value: float | Unset_Type
            The x_value of this GsaDataExportSeriesPoint.
        """
        # Field is not nullable
        if x_value is None:
            raise ValueError("Invalid value for 'x_value', must not be 'None'")
        self._x_value = x_value

    @property
    def x_name(self) -> "str | None | Unset_Type":
        """Gets the x_name of this GsaDataExportSeriesPoint.

        Returns
        -------
        str | None | Unset_Type
            The x_name of this GsaDataExportSeriesPoint.
        """
        return self._x_name

    @x_name.setter
    def x_name(self, x_name: "str | None | Unset_Type") -> None:
        """Sets the x_name of this GsaDataExportSeriesPoint.

        Parameters
        ----------
        x_name: str | None | Unset_Type
            The x_name of this GsaDataExportSeriesPoint.
        """
        self._x_name = x_name

    @property
    def y_low_value(self) -> "float | Unset_Type":
        """Gets the y_low_value of this GsaDataExportSeriesPoint.

        Returns
        -------
        float | Unset_Type
            The y_low_value of this GsaDataExportSeriesPoint.
        """
        return self._y_low_value

    @y_low_value.setter
    def y_low_value(self, y_low_value: "float | Unset_Type") -> None:
        """Sets the y_low_value of this GsaDataExportSeriesPoint.

        Parameters
        ----------
        y_low_value: float | Unset_Type
            The y_low_value of this GsaDataExportSeriesPoint.
        """
        # Field is not nullable
        if y_low_value is None:
            raise ValueError("Invalid value for 'y_low_value', must not be 'None'")
        self._y_low_value = y_low_value

    @property
    def y_high_value(self) -> "float | Unset_Type":
        """Gets the y_high_value of this GsaDataExportSeriesPoint.

        Returns
        -------
        float | Unset_Type
            The y_high_value of this GsaDataExportSeriesPoint.
        """
        return self._y_high_value

    @y_high_value.setter
    def y_high_value(self, y_high_value: "float | Unset_Type") -> None:
        """Sets the y_high_value of this GsaDataExportSeriesPoint.

        Parameters
        ----------
        y_high_value: float | Unset_Type
            The y_high_value of this GsaDataExportSeriesPoint.
        """
        # Field is not nullable
        if y_high_value is None:
            raise ValueError("Invalid value for 'y_high_value', must not be 'None'")
        self._y_high_value = y_high_value

    @property
    def is_estimated(self) -> "bool":
        """Gets the is_estimated of this GsaDataExportSeriesPoint.

        Returns
        -------
        bool
            The is_estimated of this GsaDataExportSeriesPoint.
        """
        return self._is_estimated

    @is_estimated.setter
    def is_estimated(self, is_estimated: "bool") -> None:
        """Sets the is_estimated of this GsaDataExportSeriesPoint.

        Parameters
        ----------
        is_estimated: bool
            The is_estimated of this GsaDataExportSeriesPoint.
        """
        # Field is not nullable
        if is_estimated is None:
            raise ValueError("Invalid value for 'is_estimated', must not be 'None'")
        # Field is required
        if is_estimated is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'is_estimated', must not be 'Unset'")
        self._is_estimated = is_estimated

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
        if not isinstance(other, GsaDataExportSeriesPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
