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

from ansys.grantami.serverapi_openapi.v251.models.gsa_parameter_data_value import (  # noqa: F401
    GsaParameterDataValue,
)
from ansys.grantami.serverapi_openapi.v251.models.gsa_parameter_type import GsaParameterType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaNumericParameterDataValue(GsaParameterDataValue):
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
        "parameter_type": "GsaParameterType",
        "parameter_value": "float",
        "name": "str",
        "unit": "GsaSlimUnit",
    }

    attribute_map: dict[str, str] = {
        "parameter_type": "parameterType",
        "parameter_value": "parameterValue",
        "name": "name",
        "unit": "unit",
    }

    subtype_mapping: dict[str, str] = {
        "unit": "GsaSlimUnit",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        parameter_type: "GsaParameterType" = GsaParameterType.NUMERIC,
        parameter_value: "float",
        name: "Union[str, None, Unset_Type]" = Unset,
        unit: "Union[GsaSlimUnit, Unset_Type]" = Unset,
    ) -> None:
        """GsaNumericParameterDataValue - a model defined in Swagger

        Parameters
        ----------
        parameter_type: GsaParameterType
        parameter_value: float
        name: str, optional
        unit: GsaSlimUnit, optional
        """
        super().__init__(parameter_type=parameter_type)
        self._parameter_value: float
        self._unit: Union[GsaSlimUnit, Unset_Type] = Unset
        self._name: Union[str, None, Unset_Type] = Unset

        self.parameter_value = parameter_value
        if unit is not Unset:
            self.unit = unit
        if name is not Unset:
            self.name = name

    @property
    def parameter_value(self) -> "float":
        """Gets the parameter_value of this GsaNumericParameterDataValue.

        Returns
        -------
        float
            The parameter_value of this GsaNumericParameterDataValue.
        """
        return self._parameter_value

    @parameter_value.setter
    def parameter_value(self, parameter_value: "float") -> None:
        """Sets the parameter_value of this GsaNumericParameterDataValue.

        Parameters
        ----------
        parameter_value: float
            The parameter_value of this GsaNumericParameterDataValue.
        """
        # Field is not nullable
        if parameter_value is None:
            raise ValueError("Invalid value for 'parameter_value', must not be 'None'")
        # Field is required
        if parameter_value is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'parameter_value', must not be 'Unset'")
        self._parameter_value = parameter_value

    @property
    def unit(self) -> "Union[GsaSlimUnit, Unset_Type]":
        """Gets the unit of this GsaNumericParameterDataValue.

        Returns
        -------
        Union[GsaSlimUnit, Unset_Type]
            The unit of this GsaNumericParameterDataValue.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "Union[GsaSlimUnit, Unset_Type]") -> None:
        """Sets the unit of this GsaNumericParameterDataValue.

        Parameters
        ----------
        unit: Union[GsaSlimUnit, Unset_Type]
            The unit of this GsaNumericParameterDataValue.
        """
        # Field is not nullable
        if unit is None:
            raise ValueError("Invalid value for 'unit', must not be 'None'")
        self._unit = unit

    @property
    def name(self) -> "Union[str, None, Unset_Type]":
        """Gets the name of this GsaNumericParameterDataValue.

        Returns
        -------
        Union[str, None, Unset_Type]
            The name of this GsaNumericParameterDataValue.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, None, Unset_Type]") -> None:
        """Sets the name of this GsaNumericParameterDataValue.

        Parameters
        ----------
        name: Union[str, None, Unset_Type]
            The name of this GsaNumericParameterDataValue.
        """
        self._name = name

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
        if not isinstance(other, GsaNumericParameterDataValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
