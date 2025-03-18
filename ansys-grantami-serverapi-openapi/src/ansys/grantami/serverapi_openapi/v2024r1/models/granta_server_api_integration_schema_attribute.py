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

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiIntegrationSchemaAttribute(ModelBase):
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
        "type": "GrantaServerApiAttributeType",
        "discrete_type_guid": "str",
        "discrete_type_identity": "int",
        "graph_type": "str",
        "guid": "str",
        "identity": "int",
        "is_unitted": "bool",
        "name": "str",
        "parameters": "list[GrantaServerApiIntegrationSchemaIntegrationParameterInfo]",
        "target_database": "GrantaServerApiObjectIdentifier",
        "target_table": "GrantaServerApiObjectIdentifier",
        "unit_symbol": "str",
        "x_axis_parameter": "str",
    }

    attribute_map: dict[str, str] = {
        "type": "type",
        "discrete_type_guid": "discreteTypeGuid",
        "discrete_type_identity": "discreteTypeIdentity",
        "graph_type": "graphType",
        "guid": "guid",
        "identity": "identity",
        "is_unitted": "isUnitted",
        "name": "name",
        "parameters": "parameters",
        "target_database": "targetDatabase",
        "target_table": "targetTable",
        "unit_symbol": "unitSymbol",
        "x_axis_parameter": "xAxisParameter",
    }

    subtype_mapping: dict[str, str] = {
        "type": "GrantaServerApiAttributeType",
        "parameters": "GrantaServerApiIntegrationSchemaIntegrationParameterInfo",
        "targetDatabase": "GrantaServerApiObjectIdentifier",
        "targetTable": "GrantaServerApiObjectIdentifier",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        type: "GrantaServerApiAttributeType",
        discrete_type_guid: "Union[str, None, Unset_Type]" = Unset,
        discrete_type_identity: "Union[int, None, Unset_Type]" = Unset,
        graph_type: "Union[str, None, Unset_Type]" = Unset,
        guid: "Union[str, None, Unset_Type]" = Unset,
        identity: "Union[int, Unset_Type]" = Unset,
        is_unitted: "Union[bool, None, Unset_Type]" = Unset,
        name: "Union[str, None, Unset_Type]" = Unset,
        parameters: "Union[list[GrantaServerApiIntegrationSchemaIntegrationParameterInfo], None, Unset_Type]" = Unset,
        target_database: "Union[GrantaServerApiObjectIdentifier, Unset_Type]" = Unset,
        target_table: "Union[GrantaServerApiObjectIdentifier, Unset_Type]" = Unset,
        unit_symbol: "Union[str, None, Unset_Type]" = Unset,
        x_axis_parameter: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiIntegrationSchemaAttribute - a model defined in Swagger

        Parameters
        ----------
        type: GrantaServerApiAttributeType
        discrete_type_guid: str, optional
        discrete_type_identity: int, optional
        graph_type: str, optional
        guid: str, optional
        identity: int, optional
        is_unitted: bool, optional
        name: str, optional
        parameters: list[GrantaServerApiIntegrationSchemaIntegrationParameterInfo], optional
        target_database: GrantaServerApiObjectIdentifier, optional
        target_table: GrantaServerApiObjectIdentifier, optional
        unit_symbol: str, optional
        x_axis_parameter: str, optional
        """
        self._name: Union[str, None, Unset_Type] = Unset
        self._identity: Union[int, Unset_Type] = Unset
        self._guid: Union[str, None, Unset_Type] = Unset
        self._type: GrantaServerApiAttributeType
        self._unit_symbol: Union[str, None, Unset_Type] = Unset
        self._is_unitted: Union[bool, None, Unset_Type] = Unset
        self._discrete_type_identity: Union[int, None, Unset_Type] = Unset
        self._discrete_type_guid: Union[str, None, Unset_Type] = Unset
        self._parameters: Union[
            list[GrantaServerApiIntegrationSchemaIntegrationParameterInfo], None, Unset_Type
        ] = Unset
        self._target_database: Union[GrantaServerApiObjectIdentifier, Unset_Type] = Unset
        self._target_table: Union[GrantaServerApiObjectIdentifier, Unset_Type] = Unset
        self._graph_type: Union[str, None, Unset_Type] = Unset
        self._x_axis_parameter: Union[str, None, Unset_Type] = Unset

        if name is not Unset:
            self.name = name
        if identity is not Unset:
            self.identity = identity
        if guid is not Unset:
            self.guid = guid
        self.type = type
        if unit_symbol is not Unset:
            self.unit_symbol = unit_symbol
        if is_unitted is not Unset:
            self.is_unitted = is_unitted
        if discrete_type_identity is not Unset:
            self.discrete_type_identity = discrete_type_identity
        if discrete_type_guid is not Unset:
            self.discrete_type_guid = discrete_type_guid
        if parameters is not Unset:
            self.parameters = parameters
        if target_database is not Unset:
            self.target_database = target_database
        if target_table is not Unset:
            self.target_table = target_table
        if graph_type is not Unset:
            self.graph_type = graph_type
        if x_axis_parameter is not Unset:
            self.x_axis_parameter = x_axis_parameter

    @property
    def name(self) -> "Union[str, None, Unset_Type]":
        """Gets the name of this GrantaServerApiIntegrationSchemaAttribute.

        Returns
        -------
        Union[str, None, Unset_Type]
            The name of this GrantaServerApiIntegrationSchemaAttribute.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, None, Unset_Type]") -> None:
        """Sets the name of this GrantaServerApiIntegrationSchemaAttribute.

        Parameters
        ----------
        name: Union[str, None, Unset_Type]
            The name of this GrantaServerApiIntegrationSchemaAttribute.
        """
        self._name = name

    @property
    def identity(self) -> "Union[int, Unset_Type]":
        """Gets the identity of this GrantaServerApiIntegrationSchemaAttribute.

        Returns
        -------
        Union[int, Unset_Type]
            The identity of this GrantaServerApiIntegrationSchemaAttribute.
        """
        return self._identity

    @identity.setter
    def identity(self, identity: "Union[int, Unset_Type]") -> None:
        """Sets the identity of this GrantaServerApiIntegrationSchemaAttribute.

        Parameters
        ----------
        identity: Union[int, Unset_Type]
            The identity of this GrantaServerApiIntegrationSchemaAttribute.
        """
        # Field is not nullable
        if identity is None:
            raise ValueError("Invalid value for 'identity', must not be 'None'")
        self._identity = identity

    @property
    def guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the guid of this GrantaServerApiIntegrationSchemaAttribute.
        Set as nullable for older schema compatibility,  but we expect it to be set almost everywhere,  except during loading from disk.

        Returns
        -------
        Union[str, None, Unset_Type]
            The guid of this GrantaServerApiIntegrationSchemaAttribute.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the guid of this GrantaServerApiIntegrationSchemaAttribute.
        Set as nullable for older schema compatibility,  but we expect it to be set almost everywhere,  except during loading from disk.

        Parameters
        ----------
        guid: Union[str, None, Unset_Type]
            The guid of this GrantaServerApiIntegrationSchemaAttribute.
        """
        self._guid = guid

    @property
    def type(self) -> "GrantaServerApiAttributeType":
        """Gets the type of this GrantaServerApiIntegrationSchemaAttribute.

        Returns
        -------
        GrantaServerApiAttributeType
            The type of this GrantaServerApiIntegrationSchemaAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "GrantaServerApiAttributeType") -> None:
        """Sets the type of this GrantaServerApiIntegrationSchemaAttribute.

        Parameters
        ----------
        type: GrantaServerApiAttributeType
            The type of this GrantaServerApiIntegrationSchemaAttribute.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

    @property
    def unit_symbol(self) -> "Union[str, None, Unset_Type]":
        """Gets the unit_symbol of this GrantaServerApiIntegrationSchemaAttribute.
        If isUnitted is true, then this must have a non empty value

        Returns
        -------
        Union[str, None, Unset_Type]
            The unit_symbol of this GrantaServerApiIntegrationSchemaAttribute.
        """
        return self._unit_symbol

    @unit_symbol.setter
    def unit_symbol(self, unit_symbol: "Union[str, None, Unset_Type]") -> None:
        """Sets the unit_symbol of this GrantaServerApiIntegrationSchemaAttribute.
        If isUnitted is true, then this must have a non empty value

        Parameters
        ----------
        unit_symbol: Union[str, None, Unset_Type]
            The unit_symbol of this GrantaServerApiIntegrationSchemaAttribute.
        """
        self._unit_symbol = unit_symbol

    @property
    def is_unitted(self) -> "Union[bool, None, Unset_Type]":
        """Gets the is_unitted of this GrantaServerApiIntegrationSchemaAttribute.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The is_unitted of this GrantaServerApiIntegrationSchemaAttribute.
        """
        return self._is_unitted

    @is_unitted.setter
    def is_unitted(self, is_unitted: "Union[bool, None, Unset_Type]") -> None:
        """Sets the is_unitted of this GrantaServerApiIntegrationSchemaAttribute.

        Parameters
        ----------
        is_unitted: Union[bool, None, Unset_Type]
            The is_unitted of this GrantaServerApiIntegrationSchemaAttribute.
        """
        self._is_unitted = is_unitted

    @property
    def discrete_type_identity(self) -> "Union[int, None, Unset_Type]":
        """Gets the discrete_type_identity of this GrantaServerApiIntegrationSchemaAttribute.

        Returns
        -------
        Union[int, None, Unset_Type]
            The discrete_type_identity of this GrantaServerApiIntegrationSchemaAttribute.
        """
        return self._discrete_type_identity

    @discrete_type_identity.setter
    def discrete_type_identity(
        self, discrete_type_identity: "Union[int, None, Unset_Type]"
    ) -> None:
        """Sets the discrete_type_identity of this GrantaServerApiIntegrationSchemaAttribute.

        Parameters
        ----------
        discrete_type_identity: Union[int, None, Unset_Type]
            The discrete_type_identity of this GrantaServerApiIntegrationSchemaAttribute.
        """
        self._discrete_type_identity = discrete_type_identity

    @property
    def discrete_type_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the discrete_type_guid of this GrantaServerApiIntegrationSchemaAttribute.
        A discrete attribute must define the guid of its discrete type (i.e. list of possible values)

        Returns
        -------
        Union[str, None, Unset_Type]
            The discrete_type_guid of this GrantaServerApiIntegrationSchemaAttribute.
        """
        return self._discrete_type_guid

    @discrete_type_guid.setter
    def discrete_type_guid(self, discrete_type_guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the discrete_type_guid of this GrantaServerApiIntegrationSchemaAttribute.
        A discrete attribute must define the guid of its discrete type (i.e. list of possible values)

        Parameters
        ----------
        discrete_type_guid: Union[str, None, Unset_Type]
            The discrete_type_guid of this GrantaServerApiIntegrationSchemaAttribute.
        """
        self._discrete_type_guid = discrete_type_guid

    @property
    def parameters(
        self,
    ) -> "Union[list[GrantaServerApiIntegrationSchemaIntegrationParameterInfo], None, Unset_Type]":
        """Gets the parameters of this GrantaServerApiIntegrationSchemaAttribute.
        A float functional attribute must define a list of parameters.

        Returns
        -------
        Union[list[GrantaServerApiIntegrationSchemaIntegrationParameterInfo], None, Unset_Type]
            The parameters of this GrantaServerApiIntegrationSchemaAttribute.
        """
        return self._parameters

    @parameters.setter
    def parameters(
        self,
        parameters: "Union[list[GrantaServerApiIntegrationSchemaIntegrationParameterInfo], None, Unset_Type]",
    ) -> None:
        """Sets the parameters of this GrantaServerApiIntegrationSchemaAttribute.
        A float functional attribute must define a list of parameters.

        Parameters
        ----------
        parameters: Union[list[GrantaServerApiIntegrationSchemaIntegrationParameterInfo], None, Unset_Type]
            The parameters of this GrantaServerApiIntegrationSchemaAttribute.
        """
        self._parameters = parameters

    @property
    def target_database(self) -> "Union[GrantaServerApiObjectIdentifier, Unset_Type]":
        """Gets the target_database of this GrantaServerApiIntegrationSchemaAttribute.

        Returns
        -------
        Union[GrantaServerApiObjectIdentifier, Unset_Type]
            The target_database of this GrantaServerApiIntegrationSchemaAttribute.
        """
        return self._target_database

    @target_database.setter
    def target_database(
        self, target_database: "Union[GrantaServerApiObjectIdentifier, Unset_Type]"
    ) -> None:
        """Sets the target_database of this GrantaServerApiIntegrationSchemaAttribute.

        Parameters
        ----------
        target_database: Union[GrantaServerApiObjectIdentifier, Unset_Type]
            The target_database of this GrantaServerApiIntegrationSchemaAttribute.
        """
        # Field is not nullable
        if target_database is None:
            raise ValueError("Invalid value for 'target_database', must not be 'None'")
        self._target_database = target_database

    @property
    def target_table(self) -> "Union[GrantaServerApiObjectIdentifier, Unset_Type]":
        """Gets the target_table of this GrantaServerApiIntegrationSchemaAttribute.

        Returns
        -------
        Union[GrantaServerApiObjectIdentifier, Unset_Type]
            The target_table of this GrantaServerApiIntegrationSchemaAttribute.
        """
        return self._target_table

    @target_table.setter
    def target_table(
        self, target_table: "Union[GrantaServerApiObjectIdentifier, Unset_Type]"
    ) -> None:
        """Sets the target_table of this GrantaServerApiIntegrationSchemaAttribute.

        Parameters
        ----------
        target_table: Union[GrantaServerApiObjectIdentifier, Unset_Type]
            The target_table of this GrantaServerApiIntegrationSchemaAttribute.
        """
        # Field is not nullable
        if target_table is None:
            raise ValueError("Invalid value for 'target_table', must not be 'None'")
        self._target_table = target_table

    @property
    def graph_type(self) -> "Union[str, None, Unset_Type]":
        """Gets the graph_type of this GrantaServerApiIntegrationSchemaAttribute.
        A float functional attribute must be either a Series or a Grid type graph.

        Returns
        -------
        Union[str, None, Unset_Type]
            The graph_type of this GrantaServerApiIntegrationSchemaAttribute.
        """
        return self._graph_type

    @graph_type.setter
    def graph_type(self, graph_type: "Union[str, None, Unset_Type]") -> None:
        """Sets the graph_type of this GrantaServerApiIntegrationSchemaAttribute.
        A float functional attribute must be either a Series or a Grid type graph.

        Parameters
        ----------
        graph_type: Union[str, None, Unset_Type]
            The graph_type of this GrantaServerApiIntegrationSchemaAttribute.
        """
        self._graph_type = graph_type

    @property
    def x_axis_parameter(self) -> "Union[str, None, Unset_Type]":
        """Gets the x_axis_parameter of this GrantaServerApiIntegrationSchemaAttribute.
        A float functional attribute must define an x-axis. This will be one of the parameters listed in parameters

        Returns
        -------
        Union[str, None, Unset_Type]
            The x_axis_parameter of this GrantaServerApiIntegrationSchemaAttribute.
        """
        return self._x_axis_parameter

    @x_axis_parameter.setter
    def x_axis_parameter(self, x_axis_parameter: "Union[str, None, Unset_Type]") -> None:
        """Sets the x_axis_parameter of this GrantaServerApiIntegrationSchemaAttribute.
        A float functional attribute must define an x-axis. This will be one of the parameters listed in parameters

        Parameters
        ----------
        x_axis_parameter: Union[str, None, Unset_Type]
            The x_axis_parameter of this GrantaServerApiIntegrationSchemaAttribute.
        """
        self._x_axis_parameter = x_axis_parameter

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
        if not isinstance(other, GrantaServerApiIntegrationSchemaAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
