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

from ansys.grantami.serverapi_openapi.v2024r1.models.granta_server_api_schema_attributes_attribute import (  # noqa: F401
    GrantaServerApiSchemaAttributesAttribute,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiSchemaAttributesMathsFunctionalAttribute(
    GrantaServerApiSchemaAttributesAttribute
):
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
        "allow_all_compatible_expressions": "bool",
        "allow_anonymous_expressions": "bool",
        "allow_extrapolation": "bool",
        "attribute_parameters": "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
        "default_content": "GrantaServerApiSchemaAttributesMathsContent",
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "display_names": "dict(str, str)",
        "expressions": "list[GrantaServerApiSchemaSlimEntitiesSlimExpression]",
        "guid": "str",
        "info": "GrantaServerApiSchemaAttributesAttributeAttributeInfo",
        "is_range": "bool",
        "name": "str",
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "axis_name": "str",
        "help_path": "str",
        "type": "str",
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimUnit",
    }

    attribute_map: dict[str, str] = {
        "allow_all_compatible_expressions": "allowAllCompatibleExpressions",
        "allow_anonymous_expressions": "allowAnonymousExpressions",
        "allow_extrapolation": "allowExtrapolation",
        "attribute_parameters": "attributeParameters",
        "default_content": "defaultContent",
        "default_threshold_type": "defaultThresholdType",
        "display_names": "displayNames",
        "expressions": "expressions",
        "guid": "guid",
        "info": "info",
        "is_range": "isRange",
        "name": "name",
        "about_attribute": "aboutAttribute",
        "axis_name": "axisName",
        "help_path": "helpPath",
        "type": "type",
        "unit": "unit",
    }

    subtype_mapping: dict[str, str] = {
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimUnit",
        "attributeParameters": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "expressions": "GrantaServerApiSchemaSlimEntitiesSlimExpression",
        "defaultContent": "GrantaServerApiSchemaAttributesMathsContent",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        allow_all_compatible_expressions: "bool",
        allow_anonymous_expressions: "bool",
        allow_extrapolation: "bool",
        attribute_parameters: "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
        default_content: "GrantaServerApiSchemaAttributesMathsContent",
        default_threshold_type: "GrantaServerApiSchemaAttributesAttributeThresholdType",
        display_names: "dict[str, str]",
        expressions: "list[GrantaServerApiSchemaSlimEntitiesSlimExpression]",
        guid: "str",
        info: "GrantaServerApiSchemaAttributesAttributeAttributeInfo",
        is_range: "bool",
        name: "str",
        about_attribute: "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity | Unset_Type" = Unset,
        axis_name: "str | None | Unset_Type" = Unset,
        help_path: "str | None | Unset_Type" = Unset,
        type: "str" = "mathsFunctional",
        unit: "GrantaServerApiSchemaSlimEntitiesSlimUnit | Unset_Type" = Unset,
    ) -> None:
        """GrantaServerApiSchemaAttributesMathsFunctionalAttribute - a model defined in Swagger

        Parameters
        ----------
        allow_all_compatible_expressions: bool
        allow_anonymous_expressions: bool
        allow_extrapolation: bool
        attribute_parameters: list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
        default_content: GrantaServerApiSchemaAttributesMathsContent
        default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType
        display_names: dict[str, str]
        expressions: list[GrantaServerApiSchemaSlimEntitiesSlimExpression]
        guid: str
        info: GrantaServerApiSchemaAttributesAttributeAttributeInfo
        is_range: bool
        name: str
        about_attribute: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, optional
        axis_name: str | None, optional
        help_path: str | None, optional
        type: str
        unit: GrantaServerApiSchemaSlimEntitiesSlimUnit, optional
        """
        super().__init__(
            default_threshold_type=default_threshold_type,
            display_names=display_names,
            guid=guid,
            info=info,
            name=name,
            about_attribute=about_attribute,
            axis_name=axis_name,
            help_path=help_path,
        )
        self._type: str
        self._unit: GrantaServerApiSchemaSlimEntitiesSlimUnit | Unset_Type = Unset
        self._attribute_parameters: list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
        self._expressions: list[GrantaServerApiSchemaSlimEntitiesSlimExpression]
        self._allow_extrapolation: bool
        self._is_range: bool
        self._allow_all_compatible_expressions: bool
        self._allow_anonymous_expressions: bool
        self._default_content: GrantaServerApiSchemaAttributesMathsContent

        self.type = type
        if unit is not Unset:
            self.unit = unit
        self.attribute_parameters = attribute_parameters
        self.expressions = expressions
        self.allow_extrapolation = allow_extrapolation
        self.is_range = is_range
        self.allow_all_compatible_expressions = allow_all_compatible_expressions
        self.allow_anonymous_expressions = allow_anonymous_expressions
        self.default_content = default_content

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

    @property
    def unit(self) -> "GrantaServerApiSchemaSlimEntitiesSlimUnit | Unset_Type":
        """Gets the unit of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimUnit | Unset_Type
            The unit of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "GrantaServerApiSchemaSlimEntitiesSlimUnit | Unset_Type") -> None:
        """Sets the unit of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.

        Parameters
        ----------
        unit: GrantaServerApiSchemaSlimEntitiesSlimUnit | Unset_Type
            The unit of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.
        """
        # Field is not nullable
        if unit is None:
            raise ValueError("Invalid value for 'unit', must not be 'None'")
        self._unit = unit

    @property
    def attribute_parameters(self) -> "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]":
        """Gets the attribute_parameters of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The attribute_parameters of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.
        """
        return self._attribute_parameters

    @attribute_parameters.setter
    def attribute_parameters(
        self, attribute_parameters: "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]"
    ) -> None:
        """Sets the attribute_parameters of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.

        Parameters
        ----------
        attribute_parameters: list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The attribute_parameters of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.
        """
        # Field is not nullable
        if attribute_parameters is None:
            raise ValueError("Invalid value for 'attribute_parameters', must not be 'None'")
        # Field is required
        if attribute_parameters is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'attribute_parameters', must not be 'Unset'")
        self._attribute_parameters = attribute_parameters

    @property
    def expressions(self) -> "list[GrantaServerApiSchemaSlimEntitiesSlimExpression]":
        """Gets the expressions of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimExpression]
            The expressions of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.
        """
        return self._expressions

    @expressions.setter
    def expressions(
        self, expressions: "list[GrantaServerApiSchemaSlimEntitiesSlimExpression]"
    ) -> None:
        """Sets the expressions of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.

        Parameters
        ----------
        expressions: list[GrantaServerApiSchemaSlimEntitiesSlimExpression]
            The expressions of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.
        """
        # Field is not nullable
        if expressions is None:
            raise ValueError("Invalid value for 'expressions', must not be 'None'")
        # Field is required
        if expressions is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'expressions', must not be 'Unset'")
        self._expressions = expressions

    @property
    def allow_extrapolation(self) -> "bool":
        """Gets the allow_extrapolation of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.

        Returns
        -------
        bool
            The allow_extrapolation of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.
        """
        return self._allow_extrapolation

    @allow_extrapolation.setter
    def allow_extrapolation(self, allow_extrapolation: "bool") -> None:
        """Sets the allow_extrapolation of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.

        Parameters
        ----------
        allow_extrapolation: bool
            The allow_extrapolation of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.
        """
        # Field is not nullable
        if allow_extrapolation is None:
            raise ValueError("Invalid value for 'allow_extrapolation', must not be 'None'")
        # Field is required
        if allow_extrapolation is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'allow_extrapolation', must not be 'Unset'")
        self._allow_extrapolation = allow_extrapolation

    @property
    def is_range(self) -> "bool":
        """Gets the is_range of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.

        Returns
        -------
        bool
            The is_range of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.
        """
        return self._is_range

    @is_range.setter
    def is_range(self, is_range: "bool") -> None:
        """Sets the is_range of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.

        Parameters
        ----------
        is_range: bool
            The is_range of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.
        """
        # Field is not nullable
        if is_range is None:
            raise ValueError("Invalid value for 'is_range', must not be 'None'")
        # Field is required
        if is_range is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'is_range', must not be 'Unset'")
        self._is_range = is_range

    @property
    def allow_all_compatible_expressions(self) -> "bool":
        """Gets the allow_all_compatible_expressions of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.

        Returns
        -------
        bool
            The allow_all_compatible_expressions of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.
        """
        return self._allow_all_compatible_expressions

    @allow_all_compatible_expressions.setter
    def allow_all_compatible_expressions(self, allow_all_compatible_expressions: "bool") -> None:
        """Sets the allow_all_compatible_expressions of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.

        Parameters
        ----------
        allow_all_compatible_expressions: bool
            The allow_all_compatible_expressions of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.
        """
        # Field is not nullable
        if allow_all_compatible_expressions is None:
            raise ValueError(
                "Invalid value for 'allow_all_compatible_expressions', must not be 'None'"
            )
        # Field is required
        if allow_all_compatible_expressions is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'allow_all_compatible_expressions', must not be 'Unset'"
            )
        self._allow_all_compatible_expressions = allow_all_compatible_expressions

    @property
    def allow_anonymous_expressions(self) -> "bool":
        """Gets the allow_anonymous_expressions of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.

        Returns
        -------
        bool
            The allow_anonymous_expressions of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.
        """
        return self._allow_anonymous_expressions

    @allow_anonymous_expressions.setter
    def allow_anonymous_expressions(self, allow_anonymous_expressions: "bool") -> None:
        """Sets the allow_anonymous_expressions of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.

        Parameters
        ----------
        allow_anonymous_expressions: bool
            The allow_anonymous_expressions of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.
        """
        # Field is not nullable
        if allow_anonymous_expressions is None:
            raise ValueError("Invalid value for 'allow_anonymous_expressions', must not be 'None'")
        # Field is required
        if allow_anonymous_expressions is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'allow_anonymous_expressions', must not be 'Unset'")
        self._allow_anonymous_expressions = allow_anonymous_expressions

    @property
    def default_content(self) -> "GrantaServerApiSchemaAttributesMathsContent":
        """Gets the default_content of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.

        Returns
        -------
        GrantaServerApiSchemaAttributesMathsContent
            The default_content of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.
        """
        return self._default_content

    @default_content.setter
    def default_content(
        self, default_content: "GrantaServerApiSchemaAttributesMathsContent"
    ) -> None:
        """Sets the default_content of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.

        Parameters
        ----------
        default_content: GrantaServerApiSchemaAttributesMathsContent
            The default_content of this GrantaServerApiSchemaAttributesMathsFunctionalAttribute.
        """
        # Field is not nullable
        if default_content is None:
            raise ValueError("Invalid value for 'default_content', must not be 'None'")
        # Field is required
        if default_content is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'default_content', must not be 'Unset'")
        self._default_content = default_content

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
        if not isinstance(other, GrantaServerApiSchemaAttributesMathsFunctionalAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
