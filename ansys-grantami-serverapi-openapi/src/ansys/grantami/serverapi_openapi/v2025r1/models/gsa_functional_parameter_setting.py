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


class GsaFunctionalParameterSetting(ModelBase):
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
        "default_value": "GsaParameterDataValue",
        "interpolation_type": "GsaParameterInterpolationType",
        "parameter": "GsaSlimParameter",
        "scale_type": "GsaParameterScaleType",
    }

    attribute_map: dict[str, str] = {
        "default_value": "defaultValue",
        "interpolation_type": "interpolationType",
        "parameter": "parameter",
        "scale_type": "scaleType",
    }

    subtype_mapping: dict[str, str] = {
        "parameter": "GsaSlimParameter",
        "defaultValue": "GsaParameterDataValue",
        "scaleType": "GsaParameterScaleType",
        "interpolationType": "GsaParameterInterpolationType",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        default_value: "GsaParameterDataValue",
        interpolation_type: "GsaParameterInterpolationType",
        parameter: "GsaSlimParameter",
        scale_type: "GsaParameterScaleType",
    ) -> None:
        """GsaFunctionalParameterSetting - a model defined in Swagger

        Parameters
        ----------
        default_value: GsaParameterDataValue
        interpolation_type: GsaParameterInterpolationType
        parameter: GsaSlimParameter
        scale_type: GsaParameterScaleType
        """
        self._parameter: GsaSlimParameter
        self._default_value: GsaParameterDataValue
        self._scale_type: GsaParameterScaleType
        self._interpolation_type: GsaParameterInterpolationType

        self.parameter = parameter
        self.default_value = default_value
        self.scale_type = scale_type
        self.interpolation_type = interpolation_type

    @property
    def parameter(self) -> "GsaSlimParameter":
        """Gets the parameter of this GsaFunctionalParameterSetting.

        Returns
        -------
        GsaSlimParameter
            The parameter of this GsaFunctionalParameterSetting.
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter: "GsaSlimParameter") -> None:
        """Sets the parameter of this GsaFunctionalParameterSetting.

        Parameters
        ----------
        parameter: GsaSlimParameter
            The parameter of this GsaFunctionalParameterSetting.
        """
        # Field is not nullable
        if parameter is None:
            raise ValueError("Invalid value for 'parameter', must not be 'None'")
        # Field is required
        if parameter is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'parameter', must not be 'Unset'")
        self._parameter = parameter

    @property
    def default_value(self) -> "GsaParameterDataValue":
        """Gets the default_value of this GsaFunctionalParameterSetting.

        Returns
        -------
        GsaParameterDataValue
            The default_value of this GsaFunctionalParameterSetting.
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value: "GsaParameterDataValue") -> None:
        """Sets the default_value of this GsaFunctionalParameterSetting.

        Parameters
        ----------
        default_value: GsaParameterDataValue
            The default_value of this GsaFunctionalParameterSetting.
        """
        # Field is not nullable
        if default_value is None:
            raise ValueError("Invalid value for 'default_value', must not be 'None'")
        # Field is required
        if default_value is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'default_value', must not be 'Unset'")
        self._default_value = default_value

    @property
    def scale_type(self) -> "GsaParameterScaleType":
        """Gets the scale_type of this GsaFunctionalParameterSetting.

        Returns
        -------
        GsaParameterScaleType
            The scale_type of this GsaFunctionalParameterSetting.
        """
        return self._scale_type

    @scale_type.setter
    def scale_type(self, scale_type: "GsaParameterScaleType") -> None:
        """Sets the scale_type of this GsaFunctionalParameterSetting.

        Parameters
        ----------
        scale_type: GsaParameterScaleType
            The scale_type of this GsaFunctionalParameterSetting.
        """
        # Field is not nullable
        if scale_type is None:
            raise ValueError("Invalid value for 'scale_type', must not be 'None'")
        # Field is required
        if scale_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'scale_type', must not be 'Unset'")
        self._scale_type = scale_type

    @property
    def interpolation_type(self) -> "GsaParameterInterpolationType":
        """Gets the interpolation_type of this GsaFunctionalParameterSetting.

        Returns
        -------
        GsaParameterInterpolationType
            The interpolation_type of this GsaFunctionalParameterSetting.
        """
        return self._interpolation_type

    @interpolation_type.setter
    def interpolation_type(self, interpolation_type: "GsaParameterInterpolationType") -> None:
        """Sets the interpolation_type of this GsaFunctionalParameterSetting.

        Parameters
        ----------
        interpolation_type: GsaParameterInterpolationType
            The interpolation_type of this GsaFunctionalParameterSetting.
        """
        # Field is not nullable
        if interpolation_type is None:
            raise ValueError("Invalid value for 'interpolation_type', must not be 'None'")
        # Field is required
        if interpolation_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'interpolation_type', must not be 'Unset'")
        self._interpolation_type = interpolation_type

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
        if not isinstance(other, GsaFunctionalParameterSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
