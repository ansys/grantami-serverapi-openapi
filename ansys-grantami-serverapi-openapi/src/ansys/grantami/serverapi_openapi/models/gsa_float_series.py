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
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaFloatSeries(ModelBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes
    ----------
    swagger_types: Dict[str, str]
        The key is attribute name and the value is attribute type.
    attribute_map: Dict[str, str]
        The key is attribute name and the value is json key in definition.
    subtype_mapping: Dict[str, str]
        The key is the unmangled property name and the value is the corresponding type.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: Dict[str, str] = {
        "constraints": "list[GsaParameterWithDataValue]",
        "graph_decoration": "GsaGraphDecorationType",
        "points": "list[GsaFloatSeriesPoint]",
    }

    attribute_map: Dict[str, str] = {
        "constraints": "constraints",
        "graph_decoration": "graphDecoration",
        "points": "points",
    }

    subtype_mapping: Dict[str, str] = {
        "constraints": "GsaParameterWithDataValue",
        "points": "GsaFloatSeriesPoint",
        "graphDecoration": "GsaGraphDecorationType",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        constraints: "List[GsaParameterWithDataValue]",
        graph_decoration: "GsaGraphDecorationType",
        points: "List[GsaFloatSeriesPoint]",
    ) -> None:
        """GsaFloatSeries - a model defined in Swagger

        Parameters
        ----------
        constraints: List[GsaParameterWithDataValue]
        graph_decoration: GsaGraphDecorationType
        points: List[GsaFloatSeriesPoint]
        """
        self._constraints: List[GsaParameterWithDataValue]
        self._points: List[GsaFloatSeriesPoint]
        self._graph_decoration: GsaGraphDecorationType

        self.constraints = constraints
        self.points = points
        self.graph_decoration = graph_decoration

    @property
    def constraints(self) -> "List[GsaParameterWithDataValue]":
        """Gets the constraints of this GsaFloatSeries.

        Returns
        -------
        List[GsaParameterWithDataValue]
            The constraints of this GsaFloatSeries.
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints: "List[GsaParameterWithDataValue]") -> None:
        """Sets the constraints of this GsaFloatSeries.

        Parameters
        ----------
        constraints: List[GsaParameterWithDataValue]
            The constraints of this GsaFloatSeries.
        """
        # Field is not nullable
        if constraints is None:
            raise ValueError("Invalid value for 'constraints', must not be 'None'")
        # Field is required
        if constraints is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'constraints', must not be 'Unset'")
        self._constraints = constraints

    @property
    def points(self) -> "List[GsaFloatSeriesPoint]":
        """Gets the points of this GsaFloatSeries.

        Returns
        -------
        List[GsaFloatSeriesPoint]
            The points of this GsaFloatSeries.
        """
        return self._points

    @points.setter
    def points(self, points: "List[GsaFloatSeriesPoint]") -> None:
        """Sets the points of this GsaFloatSeries.

        Parameters
        ----------
        points: List[GsaFloatSeriesPoint]
            The points of this GsaFloatSeries.
        """
        # Field is not nullable
        if points is None:
            raise ValueError("Invalid value for 'points', must not be 'None'")
        # Field is required
        if points is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'points', must not be 'Unset'")
        self._points = points

    @property
    def graph_decoration(self) -> "GsaGraphDecorationType":
        """Gets the graph_decoration of this GsaFloatSeries.

        Returns
        -------
        GsaGraphDecorationType
            The graph_decoration of this GsaFloatSeries.
        """
        return self._graph_decoration

    @graph_decoration.setter
    def graph_decoration(self, graph_decoration: "GsaGraphDecorationType") -> None:
        """Sets the graph_decoration of this GsaFloatSeries.

        Parameters
        ----------
        graph_decoration: GsaGraphDecorationType
            The graph_decoration of this GsaFloatSeries.
        """
        # Field is not nullable
        if graph_decoration is None:
            raise ValueError("Invalid value for 'graph_decoration', must not be 'None'")
        # Field is required
        if graph_decoration is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'graph_decoration', must not be 'Unset'")
        self._graph_decoration = graph_decoration

    @classmethod
    def get_real_child_model(cls, data: Dict[str, str]) -> str:
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
        if not isinstance(other, GsaFloatSeries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other