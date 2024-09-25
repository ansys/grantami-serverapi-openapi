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

from ansys.grantami.serverapi_openapi.models.gsa_attribute import GsaAttribute  # noqa: F401
from ansys.grantami.serverapi_openapi.models.gsa_attribute_type import GsaAttributeType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaMathsFunctionalAttribute(GsaAttribute):
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
        "allow_all_compatible_expressions": "bool",
        "allow_anonymous_expressions": "bool",
        "allow_extrapolation": "bool",
        "attribute_parameters": "list[GsaSlimNamedEntity]",
        "default_content": "GsaMathsContent",
        "default_threshold_type": "GsaAttributeThresholdType",
        "display_names": "dict(str, str)",
        "expressions": "list[GsaSlimExpression]",
        "guid": "str",
        "info": "GsaAttributeInfo",
        "is_hidden_from_search_criteria": "bool",
        "is_range": "bool",
        "name": "str",
        "table": "GsaSlimEntity",
        "type": "GsaAttributeType",
        "about_attribute": "GsaSlimNamedEntity",
        "axis_name": "str",
        "help_path": "str",
        "unit": "GsaSlimUnit",
    }

    attribute_map: Dict[str, str] = {
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
        "is_hidden_from_search_criteria": "isHiddenFromSearchCriteria",
        "is_range": "isRange",
        "name": "name",
        "table": "table",
        "type": "type",
        "about_attribute": "aboutAttribute",
        "axis_name": "axisName",
        "help_path": "helpPath",
        "unit": "unit",
    }

    subtype_mapping: Dict[str, str] = {
        "unit": "GsaSlimUnit",
        "attributeParameters": "GsaSlimNamedEntity",
        "expressions": "GsaSlimExpression",
        "defaultContent": "GsaMathsContent",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        allow_all_compatible_expressions: "bool",
        allow_anonymous_expressions: "bool",
        allow_extrapolation: "bool",
        attribute_parameters: "List[GsaSlimNamedEntity]",
        default_content: "GsaMathsContent",
        default_threshold_type: "GsaAttributeThresholdType",
        display_names: "Dict[str, str]",
        expressions: "List[GsaSlimExpression]",
        guid: "str",
        info: "GsaAttributeInfo",
        is_hidden_from_search_criteria: "bool",
        is_range: "bool",
        name: "str",
        table: "GsaSlimEntity",
        type: "GsaAttributeType" = GsaAttributeType.MATHSFUNCTIONAL,
        about_attribute: "Union[GsaSlimNamedEntity, Unset_Type]" = Unset,
        axis_name: "Union[str, None, Unset_Type]" = Unset,
        help_path: "Union[str, None, Unset_Type]" = Unset,
        unit: "Union[GsaSlimUnit, Unset_Type]" = Unset,
    ) -> None:
        """GsaMathsFunctionalAttribute - a model defined in Swagger

        Parameters
        ----------
        allow_all_compatible_expressions: bool
        allow_anonymous_expressions: bool
        allow_extrapolation: bool
        attribute_parameters: List[GsaSlimNamedEntity]
        default_content: GsaMathsContent
        default_threshold_type: GsaAttributeThresholdType
        display_names: Dict[str, str]
        expressions: List[GsaSlimExpression]
        guid: str
        info: GsaAttributeInfo
        is_hidden_from_search_criteria: bool
        is_range: bool
        name: str
        table: GsaSlimEntity
        type: GsaAttributeType
        about_attribute: GsaSlimNamedEntity, optional
        axis_name: str, optional
        help_path: str, optional
        unit: GsaSlimUnit, optional
        """
        super().__init__(
            default_threshold_type=default_threshold_type,
            display_names=display_names,
            guid=guid,
            info=info,
            is_hidden_from_search_criteria=is_hidden_from_search_criteria,
            name=name,
            table=table,
            type=type,
            about_attribute=about_attribute,
            axis_name=axis_name,
            help_path=help_path,
        )
        self._unit: Union[GsaSlimUnit, Unset_Type] = Unset
        self._attribute_parameters: List[GsaSlimNamedEntity]
        self._expressions: List[GsaSlimExpression]
        self._allow_extrapolation: bool
        self._is_range: bool
        self._allow_all_compatible_expressions: bool
        self._allow_anonymous_expressions: bool
        self._default_content: GsaMathsContent

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
    def unit(self) -> "Union[GsaSlimUnit, Unset_Type]":
        """Gets the unit of this GsaMathsFunctionalAttribute.

        Returns
        -------
        Union[GsaSlimUnit, Unset_Type]
            The unit of this GsaMathsFunctionalAttribute.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "Union[GsaSlimUnit, Unset_Type]") -> None:
        """Sets the unit of this GsaMathsFunctionalAttribute.

        Parameters
        ----------
        unit: Union[GsaSlimUnit, Unset_Type]
            The unit of this GsaMathsFunctionalAttribute.
        """
        # Field is not nullable
        if unit is None:
            raise ValueError("Invalid value for 'unit', must not be 'None'")
        self._unit = unit

    @property
    def attribute_parameters(self) -> "List[GsaSlimNamedEntity]":
        """Gets the attribute_parameters of this GsaMathsFunctionalAttribute.

        Returns
        -------
        List[GsaSlimNamedEntity]
            The attribute_parameters of this GsaMathsFunctionalAttribute.
        """
        return self._attribute_parameters

    @attribute_parameters.setter
    def attribute_parameters(self, attribute_parameters: "List[GsaSlimNamedEntity]") -> None:
        """Sets the attribute_parameters of this GsaMathsFunctionalAttribute.

        Parameters
        ----------
        attribute_parameters: List[GsaSlimNamedEntity]
            The attribute_parameters of this GsaMathsFunctionalAttribute.
        """
        # Field is not nullable
        if attribute_parameters is None:
            raise ValueError("Invalid value for 'attribute_parameters', must not be 'None'")
        # Field is required
        if attribute_parameters is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'attribute_parameters', must not be 'Unset'")
        self._attribute_parameters = attribute_parameters

    @property
    def expressions(self) -> "List[GsaSlimExpression]":
        """Gets the expressions of this GsaMathsFunctionalAttribute.

        Returns
        -------
        List[GsaSlimExpression]
            The expressions of this GsaMathsFunctionalAttribute.
        """
        return self._expressions

    @expressions.setter
    def expressions(self, expressions: "List[GsaSlimExpression]") -> None:
        """Sets the expressions of this GsaMathsFunctionalAttribute.

        Parameters
        ----------
        expressions: List[GsaSlimExpression]
            The expressions of this GsaMathsFunctionalAttribute.
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
        """Gets the allow_extrapolation of this GsaMathsFunctionalAttribute.

        Returns
        -------
        bool
            The allow_extrapolation of this GsaMathsFunctionalAttribute.
        """
        return self._allow_extrapolation

    @allow_extrapolation.setter
    def allow_extrapolation(self, allow_extrapolation: "bool") -> None:
        """Sets the allow_extrapolation of this GsaMathsFunctionalAttribute.

        Parameters
        ----------
        allow_extrapolation: bool
            The allow_extrapolation of this GsaMathsFunctionalAttribute.
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
        """Gets the is_range of this GsaMathsFunctionalAttribute.

        Returns
        -------
        bool
            The is_range of this GsaMathsFunctionalAttribute.
        """
        return self._is_range

    @is_range.setter
    def is_range(self, is_range: "bool") -> None:
        """Sets the is_range of this GsaMathsFunctionalAttribute.

        Parameters
        ----------
        is_range: bool
            The is_range of this GsaMathsFunctionalAttribute.
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
        """Gets the allow_all_compatible_expressions of this GsaMathsFunctionalAttribute.

        Returns
        -------
        bool
            The allow_all_compatible_expressions of this GsaMathsFunctionalAttribute.
        """
        return self._allow_all_compatible_expressions

    @allow_all_compatible_expressions.setter
    def allow_all_compatible_expressions(self, allow_all_compatible_expressions: "bool") -> None:
        """Sets the allow_all_compatible_expressions of this GsaMathsFunctionalAttribute.

        Parameters
        ----------
        allow_all_compatible_expressions: bool
            The allow_all_compatible_expressions of this GsaMathsFunctionalAttribute.
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
        """Gets the allow_anonymous_expressions of this GsaMathsFunctionalAttribute.

        Returns
        -------
        bool
            The allow_anonymous_expressions of this GsaMathsFunctionalAttribute.
        """
        return self._allow_anonymous_expressions

    @allow_anonymous_expressions.setter
    def allow_anonymous_expressions(self, allow_anonymous_expressions: "bool") -> None:
        """Sets the allow_anonymous_expressions of this GsaMathsFunctionalAttribute.

        Parameters
        ----------
        allow_anonymous_expressions: bool
            The allow_anonymous_expressions of this GsaMathsFunctionalAttribute.
        """
        # Field is not nullable
        if allow_anonymous_expressions is None:
            raise ValueError("Invalid value for 'allow_anonymous_expressions', must not be 'None'")
        # Field is required
        if allow_anonymous_expressions is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'allow_anonymous_expressions', must not be 'Unset'")
        self._allow_anonymous_expressions = allow_anonymous_expressions

    @property
    def default_content(self) -> "GsaMathsContent":
        """Gets the default_content of this GsaMathsFunctionalAttribute.

        Returns
        -------
        GsaMathsContent
            The default_content of this GsaMathsFunctionalAttribute.
        """
        return self._default_content

    @default_content.setter
    def default_content(self, default_content: "GsaMathsContent") -> None:
        """Sets the default_content of this GsaMathsFunctionalAttribute.

        Parameters
        ----------
        default_content: GsaMathsContent
            The default_content of this GsaMathsFunctionalAttribute.
        """
        # Field is not nullable
        if default_content is None:
            raise ValueError("Invalid value for 'default_content', must not be 'None'")
        # Field is required
        if default_content is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'default_content', must not be 'Unset'")
        self._default_content = default_content

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
        if not isinstance(other, GsaMathsFunctionalAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other