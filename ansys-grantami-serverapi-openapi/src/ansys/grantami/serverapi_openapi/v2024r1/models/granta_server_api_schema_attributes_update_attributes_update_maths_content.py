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


class GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent(ModelBase):
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
        "curve_label": "str",
        "expression": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "free_parameter": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "parameter_contents": "list[GrantaServerApiSchemaParametersUpdateParameterContent]",
        "transpose_axes": "bool",
        "use_logarithmic_scale": "bool",
    }

    attribute_map: dict[str, str] = {
        "curve_label": "curveLabel",
        "expression": "expression",
        "free_parameter": "freeParameter",
        "parameter_contents": "parameterContents",
        "transpose_axes": "transposeAxes",
        "use_logarithmic_scale": "useLogarithmicScale",
    }

    subtype_mapping: dict[str, str] = {
        "expression": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "freeParameter": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "parameterContents": "GrantaServerApiSchemaParametersUpdateParameterContent",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        curve_label: "str | None | Unset_Type" = Unset,
        expression: "GrantaServerApiSchemaSlimEntitiesSlimEntity | Unset_Type" = Unset,
        free_parameter: "GrantaServerApiSchemaSlimEntitiesSlimEntity | Unset_Type" = Unset,
        parameter_contents: "list[GrantaServerApiSchemaParametersUpdateParameterContent] | Unset_Type" = Unset,
        transpose_axes: "bool | Unset_Type" = Unset,
        use_logarithmic_scale: "bool | Unset_Type" = Unset,
    ) -> None:
        """GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent - a model defined in Swagger

        Parameters
        ----------
        curve_label: str | None, optional
        expression: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
        free_parameter: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
        parameter_contents: list[GrantaServerApiSchemaParametersUpdateParameterContent], optional
        transpose_axes: bool, optional
        use_logarithmic_scale: bool, optional
        """
        self._curve_label: str | None | Unset_Type = Unset
        self._transpose_axes: bool | Unset_Type = Unset
        self._use_logarithmic_scale: bool | Unset_Type = Unset
        self._expression: GrantaServerApiSchemaSlimEntitiesSlimEntity | Unset_Type = Unset
        self._free_parameter: GrantaServerApiSchemaSlimEntitiesSlimEntity | Unset_Type = Unset
        self._parameter_contents: (
            list[GrantaServerApiSchemaParametersUpdateParameterContent] | Unset_Type
        ) = Unset

        if curve_label is not Unset:
            self.curve_label = curve_label
        if transpose_axes is not Unset:
            self.transpose_axes = transpose_axes
        if use_logarithmic_scale is not Unset:
            self.use_logarithmic_scale = use_logarithmic_scale
        if expression is not Unset:
            self.expression = expression
        if free_parameter is not Unset:
            self.free_parameter = free_parameter
        if parameter_contents is not Unset:
            self.parameter_contents = parameter_contents

    @property
    def curve_label(self) -> "str | None | Unset_Type":
        """Gets the curve_label of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent.

        Returns
        -------
        str | None | Unset_Type
            The curve_label of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent.
        """
        return self._curve_label

    @curve_label.setter
    def curve_label(self, curve_label: "str | None | Unset_Type") -> None:
        """Sets the curve_label of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent.

        Parameters
        ----------
        curve_label: str | None | Unset_Type
            The curve_label of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent.
        """
        self._curve_label = curve_label

    @property
    def transpose_axes(self) -> "bool | Unset_Type":
        """Gets the transpose_axes of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent.

        Returns
        -------
        bool | Unset_Type
            The transpose_axes of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent.
        """
        return self._transpose_axes

    @transpose_axes.setter
    def transpose_axes(self, transpose_axes: "bool | Unset_Type") -> None:
        """Sets the transpose_axes of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent.

        Parameters
        ----------
        transpose_axes: bool | Unset_Type
            The transpose_axes of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent.
        """
        # Field is not nullable
        if transpose_axes is None:
            raise ValueError("Invalid value for 'transpose_axes', must not be 'None'")
        self._transpose_axes = transpose_axes

    @property
    def use_logarithmic_scale(self) -> "bool | Unset_Type":
        """Gets the use_logarithmic_scale of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent.

        Returns
        -------
        bool | Unset_Type
            The use_logarithmic_scale of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent.
        """
        return self._use_logarithmic_scale

    @use_logarithmic_scale.setter
    def use_logarithmic_scale(self, use_logarithmic_scale: "bool | Unset_Type") -> None:
        """Sets the use_logarithmic_scale of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent.

        Parameters
        ----------
        use_logarithmic_scale: bool | Unset_Type
            The use_logarithmic_scale of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent.
        """
        # Field is not nullable
        if use_logarithmic_scale is None:
            raise ValueError("Invalid value for 'use_logarithmic_scale', must not be 'None'")
        self._use_logarithmic_scale = use_logarithmic_scale

    @property
    def expression(self) -> "GrantaServerApiSchemaSlimEntitiesSlimEntity | Unset_Type":
        """Gets the expression of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimEntity | Unset_Type
            The expression of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent.
        """
        return self._expression

    @expression.setter
    def expression(
        self, expression: "GrantaServerApiSchemaSlimEntitiesSlimEntity | Unset_Type"
    ) -> None:
        """Sets the expression of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent.

        Parameters
        ----------
        expression: GrantaServerApiSchemaSlimEntitiesSlimEntity | Unset_Type
            The expression of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent.
        """
        # Field is not nullable
        if expression is None:
            raise ValueError("Invalid value for 'expression', must not be 'None'")
        self._expression = expression

    @property
    def free_parameter(self) -> "GrantaServerApiSchemaSlimEntitiesSlimEntity | Unset_Type":
        """Gets the free_parameter of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimEntity | Unset_Type
            The free_parameter of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent.
        """
        return self._free_parameter

    @free_parameter.setter
    def free_parameter(
        self, free_parameter: "GrantaServerApiSchemaSlimEntitiesSlimEntity | Unset_Type"
    ) -> None:
        """Sets the free_parameter of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent.

        Parameters
        ----------
        free_parameter: GrantaServerApiSchemaSlimEntitiesSlimEntity | Unset_Type
            The free_parameter of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent.
        """
        # Field is not nullable
        if free_parameter is None:
            raise ValueError("Invalid value for 'free_parameter', must not be 'None'")
        self._free_parameter = free_parameter

    @property
    def parameter_contents(
        self,
    ) -> "list[GrantaServerApiSchemaParametersUpdateParameterContent] | Unset_Type":
        """Gets the parameter_contents of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent.

        Returns
        -------
        list[GrantaServerApiSchemaParametersUpdateParameterContent] | Unset_Type
            The parameter_contents of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent.
        """
        return self._parameter_contents

    @parameter_contents.setter
    def parameter_contents(
        self,
        parameter_contents: "list[GrantaServerApiSchemaParametersUpdateParameterContent] | Unset_Type",
    ) -> None:
        """Sets the parameter_contents of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent.

        Parameters
        ----------
        parameter_contents: list[GrantaServerApiSchemaParametersUpdateParameterContent] | Unset_Type
            The parameter_contents of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent.
        """
        # Field is not nullable
        if parameter_contents is None:
            raise ValueError("Invalid value for 'parameter_contents', must not be 'None'")
        self._parameter_contents = parameter_contents

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
        if not isinstance(other, GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
