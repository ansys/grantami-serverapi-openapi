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

from ansys.grantami.serverapi_openapi.v2025r2.models.gsa_float_functional_attribute_parameter import (  # noqa: F401
    GsaFloatFunctionalAttributeParameter,
)
from ansys.grantami.serverapi_openapi.v2025r2.models.gsa_parameter_type import GsaParameterType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaFloatFunctionalAttributeNumericParameter(GsaFloatFunctionalAttributeParameter):
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
        "parameter": "GsaSlimNamedEntity",
        "type": "GsaParameterType",
        "default_value": "float",
        "interpolation_method": "GsaAttributeInterpolationMethod",
        "scale_type": "GsaAttributeScaleType",
    }

    attribute_map: dict[str, str] = {
        "parameter": "parameter",
        "type": "type",
        "default_value": "defaultValue",
        "interpolation_method": "interpolationMethod",
        "scale_type": "scaleType",
    }

    subtype_mapping: dict[str, str] = {
        "interpolationMethod": "GsaAttributeInterpolationMethod",
        "scaleType": "GsaAttributeScaleType",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        parameter: "GsaSlimNamedEntity",
        type: "GsaParameterType" = GsaParameterType.NUMERIC,
        default_value: "Union[float, None, Unset_Type]" = Unset,
        interpolation_method: "Union[GsaAttributeInterpolationMethod, Unset_Type]" = Unset,
        scale_type: "Union[GsaAttributeScaleType, Unset_Type]" = Unset,
    ) -> None:
        """GsaFloatFunctionalAttributeNumericParameter - a model defined in Swagger

        Parameters
        ----------
        parameter: GsaSlimNamedEntity
        type: GsaParameterType
        default_value: float, optional
        interpolation_method: GsaAttributeInterpolationMethod, optional
        scale_type: GsaAttributeScaleType, optional
        """
        super().__init__(parameter=parameter, type=type)
        self._default_value: Union[float, None, Unset_Type] = Unset
        self._interpolation_method: Union[GsaAttributeInterpolationMethod, Unset_Type] = Unset
        self._scale_type: Union[GsaAttributeScaleType, Unset_Type] = Unset

        if default_value is not Unset:
            self.default_value = default_value
        if interpolation_method is not Unset:
            self.interpolation_method = interpolation_method
        if scale_type is not Unset:
            self.scale_type = scale_type

    @property
    def default_value(self) -> "Union[float, None, Unset_Type]":
        """Gets the default_value of this GsaFloatFunctionalAttributeNumericParameter.
        If there is no default value, fallback to the parameter default.

        Returns
        -------
        Union[float, None, Unset_Type]
            The default_value of this GsaFloatFunctionalAttributeNumericParameter.
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value: "Union[float, None, Unset_Type]") -> None:
        """Sets the default_value of this GsaFloatFunctionalAttributeNumericParameter.
        If there is no default value, fallback to the parameter default.

        Parameters
        ----------
        default_value: Union[float, None, Unset_Type]
            The default_value of this GsaFloatFunctionalAttributeNumericParameter.
        """
        self._default_value = default_value

    @property
    def interpolation_method(self) -> "Union[GsaAttributeInterpolationMethod, Unset_Type]":
        """Gets the interpolation_method of this GsaFloatFunctionalAttributeNumericParameter.

        Returns
        -------
        Union[GsaAttributeInterpolationMethod, Unset_Type]
            The interpolation_method of this GsaFloatFunctionalAttributeNumericParameter.
        """
        return self._interpolation_method

    @interpolation_method.setter
    def interpolation_method(
        self, interpolation_method: "Union[GsaAttributeInterpolationMethod, Unset_Type]"
    ) -> None:
        """Sets the interpolation_method of this GsaFloatFunctionalAttributeNumericParameter.

        Parameters
        ----------
        interpolation_method: Union[GsaAttributeInterpolationMethod, Unset_Type]
            The interpolation_method of this GsaFloatFunctionalAttributeNumericParameter.
        """
        # Field is not nullable
        if interpolation_method is None:
            raise ValueError("Invalid value for 'interpolation_method', must not be 'None'")
        self._interpolation_method = interpolation_method

    @property
    def scale_type(self) -> "Union[GsaAttributeScaleType, Unset_Type]":
        """Gets the scale_type of this GsaFloatFunctionalAttributeNumericParameter.

        Returns
        -------
        Union[GsaAttributeScaleType, Unset_Type]
            The scale_type of this GsaFloatFunctionalAttributeNumericParameter.
        """
        return self._scale_type

    @scale_type.setter
    def scale_type(self, scale_type: "Union[GsaAttributeScaleType, Unset_Type]") -> None:
        """Sets the scale_type of this GsaFloatFunctionalAttributeNumericParameter.

        Parameters
        ----------
        scale_type: Union[GsaAttributeScaleType, Unset_Type]
            The scale_type of this GsaFloatFunctionalAttributeNumericParameter.
        """
        # Field is not nullable
        if scale_type is None:
            raise ValueError("Invalid value for 'scale_type', must not be 'None'")
        self._scale_type = scale_type

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
        if not isinstance(other, GsaFloatFunctionalAttributeNumericParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
