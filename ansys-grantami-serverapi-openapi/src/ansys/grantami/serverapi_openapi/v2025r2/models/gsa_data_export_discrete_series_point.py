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


class GsaDataExportDiscreteSeriesPoint(ModelBase):
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
        "x": "float",
        "x_name": "str",
        "y": "GsaDiscreteValue",
    }

    attribute_map: dict[str, str] = {
        "is_estimated": "isEstimated",
        "x": "x",
        "x_name": "xName",
        "y": "y",
    }

    subtype_mapping: dict[str, str] = {
        "y": "GsaDiscreteValue",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        is_estimated: "bool | Unset_Type" = Unset,
        x: "float | Unset_Type" = Unset,
        x_name: "str | None | Unset_Type" = Unset,
        y: "GsaDiscreteValue | Unset_Type" = Unset,
    ) -> None:
        """GsaDataExportDiscreteSeriesPoint - a model defined in Swagger

        Parameters
        ----------
        is_estimated: bool, optional
        x: float, optional
        x_name: str | None, optional
        y: GsaDiscreteValue, optional
        """
        self._x: float | Unset_Type = Unset
        self._x_name: str | None | Unset_Type = Unset
        self._y: GsaDiscreteValue | Unset_Type = Unset
        self._is_estimated: bool | Unset_Type = Unset

        if x is not Unset:
            self.x = x
        if x_name is not Unset:
            self.x_name = x_name
        if y is not Unset:
            self.y = y
        if is_estimated is not Unset:
            self.is_estimated = is_estimated

    @property
    def x(self) -> "float | Unset_Type":
        """Gets the x of this GsaDataExportDiscreteSeriesPoint.

        Returns
        -------
        float | Unset_Type
            The x of this GsaDataExportDiscreteSeriesPoint.
        """
        return self._x

    @x.setter
    def x(self, x: "float | Unset_Type") -> None:
        """Sets the x of this GsaDataExportDiscreteSeriesPoint.

        Parameters
        ----------
        x: float | Unset_Type
            The x of this GsaDataExportDiscreteSeriesPoint.
        """
        # Field is not nullable
        if x is None:
            raise ValueError("Invalid value for 'x', must not be 'None'")
        self._x = x

    @property
    def x_name(self) -> "str | None | Unset_Type":
        """Gets the x_name of this GsaDataExportDiscreteSeriesPoint.

        Returns
        -------
        str | None | Unset_Type
            The x_name of this GsaDataExportDiscreteSeriesPoint.
        """
        return self._x_name

    @x_name.setter
    def x_name(self, x_name: "str | None | Unset_Type") -> None:
        """Sets the x_name of this GsaDataExportDiscreteSeriesPoint.

        Parameters
        ----------
        x_name: str | None | Unset_Type
            The x_name of this GsaDataExportDiscreteSeriesPoint.
        """
        self._x_name = x_name

    @property
    def y(self) -> "GsaDiscreteValue | Unset_Type":
        """Gets the y of this GsaDataExportDiscreteSeriesPoint.

        Returns
        -------
        GsaDiscreteValue | Unset_Type
            The y of this GsaDataExportDiscreteSeriesPoint.
        """
        return self._y

    @y.setter
    def y(self, y: "GsaDiscreteValue | Unset_Type") -> None:
        """Sets the y of this GsaDataExportDiscreteSeriesPoint.

        Parameters
        ----------
        y: GsaDiscreteValue | Unset_Type
            The y of this GsaDataExportDiscreteSeriesPoint.
        """
        # Field is not nullable
        if y is None:
            raise ValueError("Invalid value for 'y', must not be 'None'")
        self._y = y

    @property
    def is_estimated(self) -> "bool | Unset_Type":
        """Gets the is_estimated of this GsaDataExportDiscreteSeriesPoint.

        Returns
        -------
        bool | Unset_Type
            The is_estimated of this GsaDataExportDiscreteSeriesPoint.
        """
        return self._is_estimated

    @is_estimated.setter
    def is_estimated(self, is_estimated: "bool | Unset_Type") -> None:
        """Sets the is_estimated of this GsaDataExportDiscreteSeriesPoint.

        Parameters
        ----------
        is_estimated: bool | Unset_Type
            The is_estimated of this GsaDataExportDiscreteSeriesPoint.
        """
        # Field is not nullable
        if is_estimated is None:
            raise ValueError("Invalid value for 'is_estimated', must not be 'None'")
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
        if not isinstance(other, GsaDataExportDiscreteSeriesPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
