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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaQueryAttributeProperties(ModelBase):
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
        "attribute_parameters": "GsaQuerySlimNamedEntityProperties",
        "data_rule": "GsaQueryDataRuleProperties",
        "default_threshold_type": "bool",
        "discrete_type": "GsaQueryDiscreteTypeProperties",
        "expressions": "GsaQuerySlimNamedEntityProperties",
        "guid": "bool",
        "info": "GsaQueryAttributeInfoProperties",
        "is_functional_range": "bool",
        "is_hidden_from_search_criteria": "bool",
        "is_multi_valued": "bool",
        "name": "bool",
        "tabular_columns": "GsaQuerySlimNamedEntityProperties",
        "target": "GsaQueryTabularAttributeTargetProperties",
        "type": "bool",
        "unit": "GsaQueryUnitProperties",
    }

    attribute_map: dict[str, str] = {
        "attribute_parameters": "attributeParameters",
        "data_rule": "dataRule",
        "default_threshold_type": "defaultThresholdType",
        "discrete_type": "discreteType",
        "expressions": "expressions",
        "guid": "guid",
        "info": "info",
        "is_functional_range": "isFunctionalRange",
        "is_hidden_from_search_criteria": "isHiddenFromSearchCriteria",
        "is_multi_valued": "isMultiValued",
        "name": "name",
        "tabular_columns": "tabularColumns",
        "target": "target",
        "type": "type",
        "unit": "unit",
    }

    subtype_mapping: dict[str, str] = {
        "info": "GsaQueryAttributeInfoProperties",
        "unit": "GsaQueryUnitProperties",
        "discreteType": "GsaQueryDiscreteTypeProperties",
        "dataRule": "GsaQueryDataRuleProperties",
        "target": "GsaQueryTabularAttributeTargetProperties",
        "tabularColumns": "GsaQuerySlimNamedEntityProperties",
        "attributeParameters": "GsaQuerySlimNamedEntityProperties",
        "expressions": "GsaQuerySlimNamedEntityProperties",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_parameters: "Union[GsaQuerySlimNamedEntityProperties, Unset_Type]" = Unset,
        data_rule: "Union[GsaQueryDataRuleProperties, Unset_Type]" = Unset,
        default_threshold_type: "Union[bool, None, Unset_Type]" = Unset,
        discrete_type: "Union[GsaQueryDiscreteTypeProperties, Unset_Type]" = Unset,
        expressions: "Union[GsaQuerySlimNamedEntityProperties, Unset_Type]" = Unset,
        guid: "Union[bool, None, Unset_Type]" = Unset,
        info: "Union[GsaQueryAttributeInfoProperties, Unset_Type]" = Unset,
        is_functional_range: "Union[bool, None, Unset_Type]" = Unset,
        is_hidden_from_search_criteria: "Union[bool, None, Unset_Type]" = Unset,
        is_multi_valued: "Union[bool, None, Unset_Type]" = Unset,
        name: "Union[bool, None, Unset_Type]" = Unset,
        tabular_columns: "Union[GsaQuerySlimNamedEntityProperties, Unset_Type]" = Unset,
        target: "Union[GsaQueryTabularAttributeTargetProperties, Unset_Type]" = Unset,
        type: "Union[bool, None, Unset_Type]" = Unset,
        unit: "Union[GsaQueryUnitProperties, Unset_Type]" = Unset,
    ) -> None:
        """GsaQueryAttributeProperties - a model defined in Swagger

        Parameters
        ----------
        attribute_parameters: GsaQuerySlimNamedEntityProperties, optional
        data_rule: GsaQueryDataRuleProperties, optional
        default_threshold_type: bool, optional
        discrete_type: GsaQueryDiscreteTypeProperties, optional
        expressions: GsaQuerySlimNamedEntityProperties, optional
        guid: bool, optional
        info: GsaQueryAttributeInfoProperties, optional
        is_functional_range: bool, optional
        is_hidden_from_search_criteria: bool, optional
        is_multi_valued: bool, optional
        name: bool, optional
        tabular_columns: GsaQuerySlimNamedEntityProperties, optional
        target: GsaQueryTabularAttributeTargetProperties, optional
        type: bool, optional
        unit: GsaQueryUnitProperties, optional
        """
        self._type: Union[bool, None, Unset_Type] = Unset
        self._default_threshold_type: Union[bool, None, Unset_Type] = Unset
        self._is_hidden_from_search_criteria: Union[bool, None, Unset_Type] = Unset
        self._is_multi_valued: Union[bool, None, Unset_Type] = Unset
        self._is_functional_range: Union[bool, None, Unset_Type] = Unset
        self._info: Union[GsaQueryAttributeInfoProperties, Unset_Type] = Unset
        self._unit: Union[GsaQueryUnitProperties, Unset_Type] = Unset
        self._discrete_type: Union[GsaQueryDiscreteTypeProperties, Unset_Type] = Unset
        self._data_rule: Union[GsaQueryDataRuleProperties, Unset_Type] = Unset
        self._target: Union[GsaQueryTabularAttributeTargetProperties, Unset_Type] = Unset
        self._tabular_columns: Union[GsaQuerySlimNamedEntityProperties, Unset_Type] = Unset
        self._attribute_parameters: Union[GsaQuerySlimNamedEntityProperties, Unset_Type] = Unset
        self._expressions: Union[GsaQuerySlimNamedEntityProperties, Unset_Type] = Unset
        self._name: Union[bool, None, Unset_Type] = Unset
        self._guid: Union[bool, None, Unset_Type] = Unset

        if type is not Unset:
            self.type = type
        if default_threshold_type is not Unset:
            self.default_threshold_type = default_threshold_type
        if is_hidden_from_search_criteria is not Unset:
            self.is_hidden_from_search_criteria = is_hidden_from_search_criteria
        if is_multi_valued is not Unset:
            self.is_multi_valued = is_multi_valued
        if is_functional_range is not Unset:
            self.is_functional_range = is_functional_range
        if info is not Unset:
            self.info = info
        if unit is not Unset:
            self.unit = unit
        if discrete_type is not Unset:
            self.discrete_type = discrete_type
        if data_rule is not Unset:
            self.data_rule = data_rule
        if target is not Unset:
            self.target = target
        if tabular_columns is not Unset:
            self.tabular_columns = tabular_columns
        if attribute_parameters is not Unset:
            self.attribute_parameters = attribute_parameters
        if expressions is not Unset:
            self.expressions = expressions
        if name is not Unset:
            self.name = name
        if guid is not Unset:
            self.guid = guid

    @property
    def type(self) -> "Union[bool, None, Unset_Type]":
        """Gets the type of this GsaQueryAttributeProperties.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The type of this GsaQueryAttributeProperties.
        """
        return self._type

    @type.setter
    def type(self, type: "Union[bool, None, Unset_Type]") -> None:
        """Sets the type of this GsaQueryAttributeProperties.

        Parameters
        ----------
        type: Union[bool, None, Unset_Type]
            The type of this GsaQueryAttributeProperties.
        """
        self._type = type

    @property
    def default_threshold_type(self) -> "Union[bool, None, Unset_Type]":
        """Gets the default_threshold_type of this GsaQueryAttributeProperties.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The default_threshold_type of this GsaQueryAttributeProperties.
        """
        return self._default_threshold_type

    @default_threshold_type.setter
    def default_threshold_type(
        self, default_threshold_type: "Union[bool, None, Unset_Type]"
    ) -> None:
        """Sets the default_threshold_type of this GsaQueryAttributeProperties.

        Parameters
        ----------
        default_threshold_type: Union[bool, None, Unset_Type]
            The default_threshold_type of this GsaQueryAttributeProperties.
        """
        self._default_threshold_type = default_threshold_type

    @property
    def is_hidden_from_search_criteria(self) -> "Union[bool, None, Unset_Type]":
        """Gets the is_hidden_from_search_criteria of this GsaQueryAttributeProperties.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The is_hidden_from_search_criteria of this GsaQueryAttributeProperties.
        """
        return self._is_hidden_from_search_criteria

    @is_hidden_from_search_criteria.setter
    def is_hidden_from_search_criteria(
        self, is_hidden_from_search_criteria: "Union[bool, None, Unset_Type]"
    ) -> None:
        """Sets the is_hidden_from_search_criteria of this GsaQueryAttributeProperties.

        Parameters
        ----------
        is_hidden_from_search_criteria: Union[bool, None, Unset_Type]
            The is_hidden_from_search_criteria of this GsaQueryAttributeProperties.
        """
        self._is_hidden_from_search_criteria = is_hidden_from_search_criteria

    @property
    def is_multi_valued(self) -> "Union[bool, None, Unset_Type]":
        """Gets the is_multi_valued of this GsaQueryAttributeProperties.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The is_multi_valued of this GsaQueryAttributeProperties.
        """
        return self._is_multi_valued

    @is_multi_valued.setter
    def is_multi_valued(self, is_multi_valued: "Union[bool, None, Unset_Type]") -> None:
        """Sets the is_multi_valued of this GsaQueryAttributeProperties.

        Parameters
        ----------
        is_multi_valued: Union[bool, None, Unset_Type]
            The is_multi_valued of this GsaQueryAttributeProperties.
        """
        self._is_multi_valued = is_multi_valued

    @property
    def is_functional_range(self) -> "Union[bool, None, Unset_Type]":
        """Gets the is_functional_range of this GsaQueryAttributeProperties.
        For a Granta.Server.Api.AttributeType.FloatFunctional attribute, whether the value for this attribute is ranged.  For other attribute types, returns null

        Returns
        -------
        Union[bool, None, Unset_Type]
            The is_functional_range of this GsaQueryAttributeProperties.
        """
        return self._is_functional_range

    @is_functional_range.setter
    def is_functional_range(self, is_functional_range: "Union[bool, None, Unset_Type]") -> None:
        """Sets the is_functional_range of this GsaQueryAttributeProperties.
        For a Granta.Server.Api.AttributeType.FloatFunctional attribute, whether the value for this attribute is ranged.  For other attribute types, returns null

        Parameters
        ----------
        is_functional_range: Union[bool, None, Unset_Type]
            The is_functional_range of this GsaQueryAttributeProperties.
        """
        self._is_functional_range = is_functional_range

    @property
    def info(self) -> "Union[GsaQueryAttributeInfoProperties, Unset_Type]":
        """Gets the info of this GsaQueryAttributeProperties.

        Returns
        -------
        Union[GsaQueryAttributeInfoProperties, Unset_Type]
            The info of this GsaQueryAttributeProperties.
        """
        return self._info

    @info.setter
    def info(self, info: "Union[GsaQueryAttributeInfoProperties, Unset_Type]") -> None:
        """Sets the info of this GsaQueryAttributeProperties.

        Parameters
        ----------
        info: Union[GsaQueryAttributeInfoProperties, Unset_Type]
            The info of this GsaQueryAttributeProperties.
        """
        # Field is not nullable
        if info is None:
            raise ValueError("Invalid value for 'info', must not be 'None'")
        self._info = info

    @property
    def unit(self) -> "Union[GsaQueryUnitProperties, Unset_Type]":
        """Gets the unit of this GsaQueryAttributeProperties.

        Returns
        -------
        Union[GsaQueryUnitProperties, Unset_Type]
            The unit of this GsaQueryAttributeProperties.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "Union[GsaQueryUnitProperties, Unset_Type]") -> None:
        """Sets the unit of this GsaQueryAttributeProperties.

        Parameters
        ----------
        unit: Union[GsaQueryUnitProperties, Unset_Type]
            The unit of this GsaQueryAttributeProperties.
        """
        # Field is not nullable
        if unit is None:
            raise ValueError("Invalid value for 'unit', must not be 'None'")
        self._unit = unit

    @property
    def discrete_type(self) -> "Union[GsaQueryDiscreteTypeProperties, Unset_Type]":
        """Gets the discrete_type of this GsaQueryAttributeProperties.

        Returns
        -------
        Union[GsaQueryDiscreteTypeProperties, Unset_Type]
            The discrete_type of this GsaQueryAttributeProperties.
        """
        return self._discrete_type

    @discrete_type.setter
    def discrete_type(
        self, discrete_type: "Union[GsaQueryDiscreteTypeProperties, Unset_Type]"
    ) -> None:
        """Sets the discrete_type of this GsaQueryAttributeProperties.

        Parameters
        ----------
        discrete_type: Union[GsaQueryDiscreteTypeProperties, Unset_Type]
            The discrete_type of this GsaQueryAttributeProperties.
        """
        # Field is not nullable
        if discrete_type is None:
            raise ValueError("Invalid value for 'discrete_type', must not be 'None'")
        self._discrete_type = discrete_type

    @property
    def data_rule(self) -> "Union[GsaQueryDataRuleProperties, Unset_Type]":
        """Gets the data_rule of this GsaQueryAttributeProperties.

        Returns
        -------
        Union[GsaQueryDataRuleProperties, Unset_Type]
            The data_rule of this GsaQueryAttributeProperties.
        """
        return self._data_rule

    @data_rule.setter
    def data_rule(self, data_rule: "Union[GsaQueryDataRuleProperties, Unset_Type]") -> None:
        """Sets the data_rule of this GsaQueryAttributeProperties.

        Parameters
        ----------
        data_rule: Union[GsaQueryDataRuleProperties, Unset_Type]
            The data_rule of this GsaQueryAttributeProperties.
        """
        # Field is not nullable
        if data_rule is None:
            raise ValueError("Invalid value for 'data_rule', must not be 'None'")
        self._data_rule = data_rule

    @property
    def target(self) -> "Union[GsaQueryTabularAttributeTargetProperties, Unset_Type]":
        """Gets the target of this GsaQueryAttributeProperties.

        Returns
        -------
        Union[GsaQueryTabularAttributeTargetProperties, Unset_Type]
            The target of this GsaQueryAttributeProperties.
        """
        return self._target

    @target.setter
    def target(self, target: "Union[GsaQueryTabularAttributeTargetProperties, Unset_Type]") -> None:
        """Sets the target of this GsaQueryAttributeProperties.

        Parameters
        ----------
        target: Union[GsaQueryTabularAttributeTargetProperties, Unset_Type]
            The target of this GsaQueryAttributeProperties.
        """
        # Field is not nullable
        if target is None:
            raise ValueError("Invalid value for 'target', must not be 'None'")
        self._target = target

    @property
    def tabular_columns(self) -> "Union[GsaQuerySlimNamedEntityProperties, Unset_Type]":
        """Gets the tabular_columns of this GsaQueryAttributeProperties.

        Returns
        -------
        Union[GsaQuerySlimNamedEntityProperties, Unset_Type]
            The tabular_columns of this GsaQueryAttributeProperties.
        """
        return self._tabular_columns

    @tabular_columns.setter
    def tabular_columns(
        self, tabular_columns: "Union[GsaQuerySlimNamedEntityProperties, Unset_Type]"
    ) -> None:
        """Sets the tabular_columns of this GsaQueryAttributeProperties.

        Parameters
        ----------
        tabular_columns: Union[GsaQuerySlimNamedEntityProperties, Unset_Type]
            The tabular_columns of this GsaQueryAttributeProperties.
        """
        # Field is not nullable
        if tabular_columns is None:
            raise ValueError("Invalid value for 'tabular_columns', must not be 'None'")
        self._tabular_columns = tabular_columns

    @property
    def attribute_parameters(self) -> "Union[GsaQuerySlimNamedEntityProperties, Unset_Type]":
        """Gets the attribute_parameters of this GsaQueryAttributeProperties.

        Returns
        -------
        Union[GsaQuerySlimNamedEntityProperties, Unset_Type]
            The attribute_parameters of this GsaQueryAttributeProperties.
        """
        return self._attribute_parameters

    @attribute_parameters.setter
    def attribute_parameters(
        self, attribute_parameters: "Union[GsaQuerySlimNamedEntityProperties, Unset_Type]"
    ) -> None:
        """Sets the attribute_parameters of this GsaQueryAttributeProperties.

        Parameters
        ----------
        attribute_parameters: Union[GsaQuerySlimNamedEntityProperties, Unset_Type]
            The attribute_parameters of this GsaQueryAttributeProperties.
        """
        # Field is not nullable
        if attribute_parameters is None:
            raise ValueError("Invalid value for 'attribute_parameters', must not be 'None'")
        self._attribute_parameters = attribute_parameters

    @property
    def expressions(self) -> "Union[GsaQuerySlimNamedEntityProperties, Unset_Type]":
        """Gets the expressions of this GsaQueryAttributeProperties.

        Returns
        -------
        Union[GsaQuerySlimNamedEntityProperties, Unset_Type]
            The expressions of this GsaQueryAttributeProperties.
        """
        return self._expressions

    @expressions.setter
    def expressions(
        self, expressions: "Union[GsaQuerySlimNamedEntityProperties, Unset_Type]"
    ) -> None:
        """Sets the expressions of this GsaQueryAttributeProperties.

        Parameters
        ----------
        expressions: Union[GsaQuerySlimNamedEntityProperties, Unset_Type]
            The expressions of this GsaQueryAttributeProperties.
        """
        # Field is not nullable
        if expressions is None:
            raise ValueError("Invalid value for 'expressions', must not be 'None'")
        self._expressions = expressions

    @property
    def name(self) -> "Union[bool, None, Unset_Type]":
        """Gets the name of this GsaQueryAttributeProperties.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The name of this GsaQueryAttributeProperties.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[bool, None, Unset_Type]") -> None:
        """Sets the name of this GsaQueryAttributeProperties.

        Parameters
        ----------
        name: Union[bool, None, Unset_Type]
            The name of this GsaQueryAttributeProperties.
        """
        self._name = name

    @property
    def guid(self) -> "Union[bool, None, Unset_Type]":
        """Gets the guid of this GsaQueryAttributeProperties.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The guid of this GsaQueryAttributeProperties.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[bool, None, Unset_Type]") -> None:
        """Sets the guid of this GsaQueryAttributeProperties.

        Parameters
        ----------
        guid: Union[bool, None, Unset_Type]
            The guid of this GsaQueryAttributeProperties.
        """
        self._guid = guid

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
        if not isinstance(other, GsaQueryAttributeProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
