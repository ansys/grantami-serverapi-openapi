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

from ansys.grantami.serverapi_openapi.v2025r2.models.gsa_parameter_content import (  # noqa: F401
    GsaParameterContent,
)
from ansys.grantami.serverapi_openapi.v2025r2.models.gsa_parameter_type import GsaParameterType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaNumericParameterContent(GsaParameterContent):
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
        "parameter_range": "GsaContinuousRange",
        "value": "float",
    }

    attribute_map: dict[str, str] = {
        "parameter": "parameter",
        "type": "type",
        "parameter_range": "parameterRange",
        "value": "value",
    }

    subtype_mapping: dict[str, str] = {
        "parameterRange": "GsaContinuousRange",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        parameter: "GsaSlimNamedEntity",
        type: "GsaParameterType" = GsaParameterType.NUMERIC,
        parameter_range: "Union[GsaContinuousRange, Unset_Type]" = Unset,
        value: "Union[float, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaNumericParameterContent - a model defined in Swagger

        Parameters
        ----------
        parameter: GsaSlimNamedEntity
        type: GsaParameterType
        parameter_range: GsaContinuousRange, optional
        value: float, optional
        """
        super().__init__(parameter=parameter, type=type)
        self._value: Union[float, None, Unset_Type] = Unset
        self._parameter_range: Union[GsaContinuousRange, Unset_Type] = Unset

        if value is not Unset:
            self.value = value
        if parameter_range is not Unset:
            self.parameter_range = parameter_range

    @property
    def value(self) -> "Union[float, None, Unset_Type]":
        """Gets the value of this GsaNumericParameterContent.

        Returns
        -------
        Union[float, None, Unset_Type]
            The value of this GsaNumericParameterContent.
        """
        return self._value

    @value.setter
    def value(self, value: "Union[float, None, Unset_Type]") -> None:
        """Sets the value of this GsaNumericParameterContent.

        Parameters
        ----------
        value: Union[float, None, Unset_Type]
            The value of this GsaNumericParameterContent.
        """
        self._value = value

    @property
    def parameter_range(self) -> "Union[GsaContinuousRange, Unset_Type]":
        """Gets the parameter_range of this GsaNumericParameterContent.

        Returns
        -------
        Union[GsaContinuousRange, Unset_Type]
            The parameter_range of this GsaNumericParameterContent.
        """
        return self._parameter_range

    @parameter_range.setter
    def parameter_range(self, parameter_range: "Union[GsaContinuousRange, Unset_Type]") -> None:
        """Sets the parameter_range of this GsaNumericParameterContent.

        Parameters
        ----------
        parameter_range: Union[GsaContinuousRange, Unset_Type]
            The parameter_range of this GsaNumericParameterContent.
        """
        # Field is not nullable
        if parameter_range is None:
            raise ValueError("Invalid value for 'parameter_range', must not be 'None'")
        self._parameter_range = parameter_range

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
        if not isinstance(other, GsaNumericParameterContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
