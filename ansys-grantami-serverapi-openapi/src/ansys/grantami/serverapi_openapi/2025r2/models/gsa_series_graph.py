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

from ansys.grantami.serverapi_openapi.2025r2.models.gsa_graph import GsaGraph  # noqa: F401
from ansys.grantami.serverapi_openapi.2025r2.models.gsa_graph_type import GsaGraphType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaSeriesGraph(GsaGraph):
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
    discriminator_class_map: dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "constraint_parameters": "list[GsaSlimParameter]",
        "functional_type": "GsaFunctionalType",
        "graph_type": "GsaGraphType",
        "number_of_points": "int",
        "x_axis_parameter": "GsaSlimParameter",
    }

    attribute_map: dict[str, str] = {
        "constraint_parameters": "constraintParameters",
        "functional_type": "functionalType",
        "graph_type": "graphType",
        "number_of_points": "numberOfPoints",
        "x_axis_parameter": "xAxisParameter",
    }

    subtype_mapping: dict[str, str] = {
        "functionalType": "GsaFunctionalType",
        "xAxisParameter": "GsaSlimParameter",
        "constraintParameters": "GsaSlimParameter",
    }

    discriminator_value_class_map = {
        "float".lower(): "#/components/schemas/GsaFloatSeriesGraph",
        "discrete".lower(): "#/components/schemas/GsaDiscreteSeriesGraph",
    }

    discriminator: Optional[str] = "functional_type"

    def __init__(self, *, constraint_parameters: "list[GsaSlimParameter]", functional_type: "GsaFunctionalType", graph_type: "GsaGraphType" = GsaGraphType.SERIES, number_of_points: "int", x_axis_parameter: "GsaSlimParameter",) -> None:
        """GsaSeriesGraph - a model defined in Swagger

        Parameters
        ----------
        constraint_parameters: list[GsaSlimParameter]
        functional_type: GsaFunctionalType
        graph_type: GsaGraphType
        number_of_points: int
        x_axis_parameter: GsaSlimParameter
        """
        super().__init__(graph_type=graph_type)
        self._functional_type: GsaFunctionalType
        self._x_axis_parameter: GsaSlimParameter
        self._constraint_parameters: list[GsaSlimParameter]
        self._number_of_points: int

        self.functional_type = functional_type
        self.x_axis_parameter = x_axis_parameter
        self.constraint_parameters = constraint_parameters
        self.number_of_points = number_of_points

    @property
    def functional_type(self) -> "GsaFunctionalType":
        """Gets the functional_type of this GsaSeriesGraph.

        Returns
        -------
        GsaFunctionalType
            The functional_type of this GsaSeriesGraph.
        """
        return self._functional_type

    @functional_type.setter
    def functional_type(self, functional_type: "GsaFunctionalType") -> None:
        """Sets the functional_type of this GsaSeriesGraph.

        Parameters
        ----------
        functional_type: GsaFunctionalType
            The functional_type of this GsaSeriesGraph.
        """
        # Field is not nullable
        if functional_type is None:
            raise ValueError("Invalid value for 'functional_type', must not be 'None'")
        # Field is required
        if functional_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'functional_type', must not be 'Unset'")
        self._functional_type = functional_type

    @property
    def x_axis_parameter(self) -> "GsaSlimParameter":
        """Gets the x_axis_parameter of this GsaSeriesGraph.

        Returns
        -------
        GsaSlimParameter
            The x_axis_parameter of this GsaSeriesGraph.
        """
        return self._x_axis_parameter

    @x_axis_parameter.setter
    def x_axis_parameter(self, x_axis_parameter: "GsaSlimParameter") -> None:
        """Sets the x_axis_parameter of this GsaSeriesGraph.

        Parameters
        ----------
        x_axis_parameter: GsaSlimParameter
            The x_axis_parameter of this GsaSeriesGraph.
        """
        # Field is not nullable
        if x_axis_parameter is None:
            raise ValueError("Invalid value for 'x_axis_parameter', must not be 'None'")
        # Field is required
        if x_axis_parameter is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'x_axis_parameter', must not be 'Unset'")
        self._x_axis_parameter = x_axis_parameter

    @property
    def constraint_parameters(self) -> "list[GsaSlimParameter]":
        """Gets the constraint_parameters of this GsaSeriesGraph.

        Returns
        -------
        list[GsaSlimParameter]
            The constraint_parameters of this GsaSeriesGraph.
        """
        return self._constraint_parameters

    @constraint_parameters.setter
    def constraint_parameters(self, constraint_parameters: "list[GsaSlimParameter]") -> None:
        """Sets the constraint_parameters of this GsaSeriesGraph.

        Parameters
        ----------
        constraint_parameters: list[GsaSlimParameter]
            The constraint_parameters of this GsaSeriesGraph.
        """
        # Field is not nullable
        if constraint_parameters is None:
            raise ValueError("Invalid value for 'constraint_parameters', must not be 'None'")
        # Field is required
        if constraint_parameters is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'constraint_parameters', must not be 'Unset'")
        self._constraint_parameters = constraint_parameters

    @property
    def number_of_points(self) -> "int":
        """Gets the number_of_points of this GsaSeriesGraph.

        Returns
        -------
        int
            The number_of_points of this GsaSeriesGraph.
        """
        return self._number_of_points

    @number_of_points.setter
    def number_of_points(self, number_of_points: "int") -> None:
        """Sets the number_of_points of this GsaSeriesGraph.

        Parameters
        ----------
        number_of_points: int
            The number_of_points of this GsaSeriesGraph.
        """
        # Field is not nullable
        if number_of_points is None:
            raise ValueError("Invalid value for 'number_of_points', must not be 'None'")
        # Field is required
        if number_of_points is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'number_of_points', must not be 'Unset'")
        self._number_of_points = number_of_points

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[cls._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen,
        # so we have to extract it from the JSON reference
        return cls.discriminator_value_class_map[discriminator_value].rsplit("/", 1)[-1]

    @classmethod
    def _get_discriminator_field_name(cls) -> str:
        assert cls.discriminator
        name_tokens = cls.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GsaSeriesGraph):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

