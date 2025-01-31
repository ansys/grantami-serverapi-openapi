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


class GsaDiscreteSeriesPoint(ModelBase):
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
        "value": "GsaDiscreteValuesDiscreteValue",
        "x_value": "float",
    }

    attribute_map: dict[str, str] = {
        "estimated": "estimated",
        "value": "value",
        "x_value": "xValue",
    }

    subtype_mapping: dict[str, str] = {
        "value": "GsaDiscreteValuesDiscreteValue",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        estimated: "bool",
        value: "GsaDiscreteValuesDiscreteValue",
        x_value: "float",
    ) -> None:
        """GsaDiscreteSeriesPoint - a model defined in Swagger

        Parameters
        ----------
        estimated: bool
        value: GsaDiscreteValuesDiscreteValue
        x_value: float
        """
        self._x_value: float
        self._value: GsaDiscreteValuesDiscreteValue
        self._estimated: bool

        self.x_value = x_value
        self.value = value
        self.estimated = estimated

    @property
    def x_value(self) -> "float":
        """Gets the x_value of this GsaDiscreteSeriesPoint.

        Returns
        -------
        float
            The x_value of this GsaDiscreteSeriesPoint.
        """
        return self._x_value

    @x_value.setter
    def x_value(self, x_value: "float") -> None:
        """Sets the x_value of this GsaDiscreteSeriesPoint.

        Parameters
        ----------
        x_value: float
            The x_value of this GsaDiscreteSeriesPoint.
        """
        # Field is not nullable
        if x_value is None:
            raise ValueError("Invalid value for 'x_value', must not be 'None'")
        # Field is required
        if x_value is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'x_value', must not be 'Unset'")
        self._x_value = x_value

    @property
    def value(self) -> "GsaDiscreteValuesDiscreteValue":
        """Gets the value of this GsaDiscreteSeriesPoint.

        Returns
        -------
        GsaDiscreteValuesDiscreteValue
            The value of this GsaDiscreteSeriesPoint.
        """
        return self._value

    @value.setter
    def value(self, value: "GsaDiscreteValuesDiscreteValue") -> None:
        """Sets the value of this GsaDiscreteSeriesPoint.

        Parameters
        ----------
        value: GsaDiscreteValuesDiscreteValue
            The value of this GsaDiscreteSeriesPoint.
        """
        # Field is not nullable
        if value is None:
            raise ValueError("Invalid value for 'value', must not be 'None'")
        # Field is required
        if value is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'value', must not be 'Unset'")
        self._value = value

    @property
    def estimated(self) -> "bool":
        """Gets the estimated of this GsaDiscreteSeriesPoint.

        Returns
        -------
        bool
            The estimated of this GsaDiscreteSeriesPoint.
        """
        return self._estimated

    @estimated.setter
    def estimated(self, estimated: "bool") -> None:
        """Sets the estimated of this GsaDiscreteSeriesPoint.

        Parameters
        ----------
        estimated: bool
            The estimated of this GsaDiscreteSeriesPoint.
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
        if not isinstance(other, GsaDiscreteSeriesPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
