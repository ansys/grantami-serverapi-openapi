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

from ansys.grantami.serverapi_openapi.models.gsa_attribute_type import GsaAttributeType
from ansys.grantami.serverapi_openapi.models.gsa_create_attribute import (  # noqa: F401
    GsaCreateAttribute,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaCreateMathsFunctionalAttribute(GsaCreateAttribute):
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
        "name": "str",
        "type": "GsaAttributeType",
        "allow_all_compatible_expressions": "bool",
        "allow_anonymous_expressions": "bool",
        "allow_extrapolation": "bool",
        "attribute_parameters": "list[GsaSlimEntity]",
        "axis_name": "GsaCreateAxisName",
        "default_content": "GsaCreateMathsContent",
        "default_threshold_type": "GsaAttributeThresholdType",
        "expressions": "list[GsaSlimEntity]",
        "guid": "str",
        "help_path": "str",
        "is_hidden_from_search_criteria": "bool",
        "is_range": "bool",
        "unit": "GsaSlimEntity",
    }

    attribute_map: dict[str, str] = {
        "name": "name",
        "type": "type",
        "allow_all_compatible_expressions": "allowAllCompatibleExpressions",
        "allow_anonymous_expressions": "allowAnonymousExpressions",
        "allow_extrapolation": "allowExtrapolation",
        "attribute_parameters": "attributeParameters",
        "axis_name": "axisName",
        "default_content": "defaultContent",
        "default_threshold_type": "defaultThresholdType",
        "expressions": "expressions",
        "guid": "guid",
        "help_path": "helpPath",
        "is_hidden_from_search_criteria": "isHiddenFromSearchCriteria",
        "is_range": "isRange",
        "unit": "unit",
    }

    subtype_mapping: dict[str, str] = {
        "unit": "GsaSlimEntity",
        "attributeParameters": "GsaSlimEntity",
        "expressions": "GsaSlimEntity",
        "axisName": "GsaCreateAxisName",
        "defaultContent": "GsaCreateMathsContent",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        name: "str",
        type: "GsaAttributeType" = GsaAttributeType.MATHSFUNCTIONAL,
        allow_all_compatible_expressions: "Union[bool, Unset_Type]" = Unset,
        allow_anonymous_expressions: "Union[bool, Unset_Type]" = Unset,
        allow_extrapolation: "Union[bool, Unset_Type]" = Unset,
        attribute_parameters: "Union[list[GsaSlimEntity], None, Unset_Type]" = Unset,
        axis_name: "Union[GsaCreateAxisName, Unset_Type]" = Unset,
        default_content: "Union[GsaCreateMathsContent, Unset_Type]" = Unset,
        default_threshold_type: "Union[GsaAttributeThresholdType, Unset_Type]" = Unset,
        expressions: "Union[list[GsaSlimEntity], None, Unset_Type]" = Unset,
        guid: "Union[str, Unset_Type]" = Unset,
        help_path: "Union[str, None, Unset_Type]" = Unset,
        is_hidden_from_search_criteria: "Union[bool, None, Unset_Type]" = Unset,
        is_range: "Union[bool, Unset_Type]" = Unset,
        unit: "Union[GsaSlimEntity, Unset_Type]" = Unset,
    ) -> None:
        """GsaCreateMathsFunctionalAttribute - a model defined in Swagger

        Parameters
        ----------
        name: str
        type: GsaAttributeType
        allow_all_compatible_expressions: bool, optional
        allow_anonymous_expressions: bool, optional
        allow_extrapolation: bool, optional
        attribute_parameters: list[GsaSlimEntity], optional
        axis_name: GsaCreateAxisName, optional
        default_content: GsaCreateMathsContent, optional
        default_threshold_type: GsaAttributeThresholdType, optional
        expressions: list[GsaSlimEntity], optional
        guid: str, optional
        help_path: str, optional
        is_hidden_from_search_criteria: bool, optional
        is_range: bool, optional
        unit: GsaSlimEntity, optional
        """
        super().__init__(
            name=name,
            type=type,
            default_threshold_type=default_threshold_type,
            guid=guid,
            help_path=help_path,
            is_hidden_from_search_criteria=is_hidden_from_search_criteria,
        )
        self._unit: Union[GsaSlimEntity, Unset_Type] = Unset
        self._attribute_parameters: Union[list[GsaSlimEntity], None, Unset_Type] = Unset
        self._expressions: Union[list[GsaSlimEntity], None, Unset_Type] = Unset
        self._allow_extrapolation: Union[bool, Unset_Type] = Unset
        self._axis_name: Union[GsaCreateAxisName, Unset_Type] = Unset
        self._is_range: Union[bool, Unset_Type] = Unset
        self._default_content: Union[GsaCreateMathsContent, Unset_Type] = Unset
        self._allow_all_compatible_expressions: Union[bool, Unset_Type] = Unset
        self._allow_anonymous_expressions: Union[bool, Unset_Type] = Unset

        if unit is not Unset:
            self.unit = unit
        if attribute_parameters is not Unset:
            self.attribute_parameters = attribute_parameters
        if expressions is not Unset:
            self.expressions = expressions
        if allow_extrapolation is not Unset:
            self.allow_extrapolation = allow_extrapolation
        if axis_name is not Unset:
            self.axis_name = axis_name
        if is_range is not Unset:
            self.is_range = is_range
        if default_content is not Unset:
            self.default_content = default_content
        if allow_all_compatible_expressions is not Unset:
            self.allow_all_compatible_expressions = allow_all_compatible_expressions
        if allow_anonymous_expressions is not Unset:
            self.allow_anonymous_expressions = allow_anonymous_expressions

    @property
    def unit(self) -> "Union[GsaSlimEntity, Unset_Type]":
        """Gets the unit of this GsaCreateMathsFunctionalAttribute.

        Returns
        -------
        Union[GsaSlimEntity, Unset_Type]
            The unit of this GsaCreateMathsFunctionalAttribute.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "Union[GsaSlimEntity, Unset_Type]") -> None:
        """Sets the unit of this GsaCreateMathsFunctionalAttribute.

        Parameters
        ----------
        unit: Union[GsaSlimEntity, Unset_Type]
            The unit of this GsaCreateMathsFunctionalAttribute.
        """
        # Field is not nullable
        if unit is None:
            raise ValueError("Invalid value for 'unit', must not be 'None'")
        self._unit = unit

    @property
    def attribute_parameters(self) -> "Union[list[GsaSlimEntity], None, Unset_Type]":
        """Gets the attribute_parameters of this GsaCreateMathsFunctionalAttribute.

        Returns
        -------
        Union[list[GsaSlimEntity], None, Unset_Type]
            The attribute_parameters of this GsaCreateMathsFunctionalAttribute.
        """
        return self._attribute_parameters

    @attribute_parameters.setter
    def attribute_parameters(
        self, attribute_parameters: "Union[list[GsaSlimEntity], None, Unset_Type]"
    ) -> None:
        """Sets the attribute_parameters of this GsaCreateMathsFunctionalAttribute.

        Parameters
        ----------
        attribute_parameters: Union[list[GsaSlimEntity], None, Unset_Type]
            The attribute_parameters of this GsaCreateMathsFunctionalAttribute.
        """
        self._attribute_parameters = attribute_parameters

    @property
    def expressions(self) -> "Union[list[GsaSlimEntity], None, Unset_Type]":
        """Gets the expressions of this GsaCreateMathsFunctionalAttribute.

        Returns
        -------
        Union[list[GsaSlimEntity], None, Unset_Type]
            The expressions of this GsaCreateMathsFunctionalAttribute.
        """
        return self._expressions

    @expressions.setter
    def expressions(self, expressions: "Union[list[GsaSlimEntity], None, Unset_Type]") -> None:
        """Sets the expressions of this GsaCreateMathsFunctionalAttribute.

        Parameters
        ----------
        expressions: Union[list[GsaSlimEntity], None, Unset_Type]
            The expressions of this GsaCreateMathsFunctionalAttribute.
        """
        self._expressions = expressions

    @property
    def allow_extrapolation(self) -> "Union[bool, Unset_Type]":
        """Gets the allow_extrapolation of this GsaCreateMathsFunctionalAttribute.

        Returns
        -------
        Union[bool, Unset_Type]
            The allow_extrapolation of this GsaCreateMathsFunctionalAttribute.
        """
        return self._allow_extrapolation

    @allow_extrapolation.setter
    def allow_extrapolation(self, allow_extrapolation: "Union[bool, Unset_Type]") -> None:
        """Sets the allow_extrapolation of this GsaCreateMathsFunctionalAttribute.

        Parameters
        ----------
        allow_extrapolation: Union[bool, Unset_Type]
            The allow_extrapolation of this GsaCreateMathsFunctionalAttribute.
        """
        # Field is not nullable
        if allow_extrapolation is None:
            raise ValueError("Invalid value for 'allow_extrapolation', must not be 'None'")
        self._allow_extrapolation = allow_extrapolation

    @property
    def axis_name(self) -> "Union[GsaCreateAxisName, Unset_Type]":
        """Gets the axis_name of this GsaCreateMathsFunctionalAttribute.

        Returns
        -------
        Union[GsaCreateAxisName, Unset_Type]
            The axis_name of this GsaCreateMathsFunctionalAttribute.
        """
        return self._axis_name

    @axis_name.setter
    def axis_name(self, axis_name: "Union[GsaCreateAxisName, Unset_Type]") -> None:
        """Sets the axis_name of this GsaCreateMathsFunctionalAttribute.

        Parameters
        ----------
        axis_name: Union[GsaCreateAxisName, Unset_Type]
            The axis_name of this GsaCreateMathsFunctionalAttribute.
        """
        # Field is not nullable
        if axis_name is None:
            raise ValueError("Invalid value for 'axis_name', must not be 'None'")
        self._axis_name = axis_name

    @property
    def is_range(self) -> "Union[bool, Unset_Type]":
        """Gets the is_range of this GsaCreateMathsFunctionalAttribute.

        Returns
        -------
        Union[bool, Unset_Type]
            The is_range of this GsaCreateMathsFunctionalAttribute.
        """
        return self._is_range

    @is_range.setter
    def is_range(self, is_range: "Union[bool, Unset_Type]") -> None:
        """Sets the is_range of this GsaCreateMathsFunctionalAttribute.

        Parameters
        ----------
        is_range: Union[bool, Unset_Type]
            The is_range of this GsaCreateMathsFunctionalAttribute.
        """
        # Field is not nullable
        if is_range is None:
            raise ValueError("Invalid value for 'is_range', must not be 'None'")
        self._is_range = is_range

    @property
    def default_content(self) -> "Union[GsaCreateMathsContent, Unset_Type]":
        """Gets the default_content of this GsaCreateMathsFunctionalAttribute.

        Returns
        -------
        Union[GsaCreateMathsContent, Unset_Type]
            The default_content of this GsaCreateMathsFunctionalAttribute.
        """
        return self._default_content

    @default_content.setter
    def default_content(self, default_content: "Union[GsaCreateMathsContent, Unset_Type]") -> None:
        """Sets the default_content of this GsaCreateMathsFunctionalAttribute.

        Parameters
        ----------
        default_content: Union[GsaCreateMathsContent, Unset_Type]
            The default_content of this GsaCreateMathsFunctionalAttribute.
        """
        # Field is not nullable
        if default_content is None:
            raise ValueError("Invalid value for 'default_content', must not be 'None'")
        self._default_content = default_content

    @property
    def allow_all_compatible_expressions(self) -> "Union[bool, Unset_Type]":
        """Gets the allow_all_compatible_expressions of this GsaCreateMathsFunctionalAttribute.

        Returns
        -------
        Union[bool, Unset_Type]
            The allow_all_compatible_expressions of this GsaCreateMathsFunctionalAttribute.
        """
        return self._allow_all_compatible_expressions

    @allow_all_compatible_expressions.setter
    def allow_all_compatible_expressions(
        self, allow_all_compatible_expressions: "Union[bool, Unset_Type]"
    ) -> None:
        """Sets the allow_all_compatible_expressions of this GsaCreateMathsFunctionalAttribute.

        Parameters
        ----------
        allow_all_compatible_expressions: Union[bool, Unset_Type]
            The allow_all_compatible_expressions of this GsaCreateMathsFunctionalAttribute.
        """
        # Field is not nullable
        if allow_all_compatible_expressions is None:
            raise ValueError(
                "Invalid value for 'allow_all_compatible_expressions', must not be 'None'"
            )
        self._allow_all_compatible_expressions = allow_all_compatible_expressions

    @property
    def allow_anonymous_expressions(self) -> "Union[bool, Unset_Type]":
        """Gets the allow_anonymous_expressions of this GsaCreateMathsFunctionalAttribute.

        Returns
        -------
        Union[bool, Unset_Type]
            The allow_anonymous_expressions of this GsaCreateMathsFunctionalAttribute.
        """
        return self._allow_anonymous_expressions

    @allow_anonymous_expressions.setter
    def allow_anonymous_expressions(
        self, allow_anonymous_expressions: "Union[bool, Unset_Type]"
    ) -> None:
        """Sets the allow_anonymous_expressions of this GsaCreateMathsFunctionalAttribute.

        Parameters
        ----------
        allow_anonymous_expressions: Union[bool, Unset_Type]
            The allow_anonymous_expressions of this GsaCreateMathsFunctionalAttribute.
        """
        # Field is not nullable
        if allow_anonymous_expressions is None:
            raise ValueError("Invalid value for 'allow_anonymous_expressions', must not be 'None'")
        self._allow_anonymous_expressions = allow_anonymous_expressions

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
        if not isinstance(other, GsaCreateMathsFunctionalAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
