"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase


if TYPE_CHECKING:
    from . import *


class GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute(ModelBase):
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
    swagger_types = {
        "type": "GrantaServerApiAttributeType",
        "discrete_type_guid": "str",
        "graph_type": "str",
        "guid": "str",
        "is_unitted": "bool",
        "name": "str",
        "parameters": "list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationParameterInfo]",
        "target_database": "GrantaServerApiObjectIdentifier",
        "target_table": "GrantaServerApiObjectIdentifier",
        "unit_symbol": "str",
        "x_axis_parameter": "str",
    }

    attribute_map = {
        "type": "type",
        "discrete_type_guid": "discreteTypeGuid",
        "graph_type": "graphType",
        "guid": "guid",
        "is_unitted": "isUnitted",
        "name": "name",
        "parameters": "parameters",
        "target_database": "targetDatabase",
        "target_table": "targetTable",
        "unit_symbol": "unitSymbol",
        "x_axis_parameter": "xAxisParameter",
    }

    subtype_mapping = {
        "type": "GrantaServerApiAttributeType",
        "parameters": "GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationParameterInfo",
        "targetDatabase": "GrantaServerApiObjectIdentifier",
        "targetTable": "GrantaServerApiObjectIdentifier",
    }

    discriminator = None

    def __init__(
        self,
        *,
        type: "GrantaServerApiAttributeType",
        discrete_type_guid: "Optional[str]" = None,
        graph_type: "Optional[str]" = None,
        guid: "Optional[str]" = None,
        is_unitted: "Optional[bool]" = None,
        name: "Optional[str]" = None,
        parameters: "Optional[List[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationParameterInfo]]" = None,
        target_database: "Optional[GrantaServerApiObjectIdentifier]" = None,
        target_table: "Optional[GrantaServerApiObjectIdentifier]" = None,
        unit_symbol: "Optional[str]" = None,
        x_axis_parameter: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute - a model defined in Swagger

        Parameters
        ----------
            type: GrantaServerApiAttributeType
            discrete_type_guid: str, optional
            graph_type: str, optional
            guid: str, optional
            is_unitted: bool, optional
            name: str, optional
            parameters: List[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationParameterInfo], optional
            target_database: GrantaServerApiObjectIdentifier, optional
            target_table: GrantaServerApiObjectIdentifier, optional
            unit_symbol: str, optional
            x_axis_parameter: str, optional
        """
        self._name = None
        self._guid = None
        self._type = None
        self._unit_symbol = None
        self._is_unitted = None
        self._discrete_type_guid = None
        self._parameters = None
        self._target_database = None
        self._target_table = None
        self._graph_type = None
        self._x_axis_parameter = None

        if name is not None:
            self.name = name
        if guid is not None:
            self.guid = guid
        self.type = type
        if unit_symbol is not None:
            self.unit_symbol = unit_symbol
        if is_unitted is not None:
            self.is_unitted = is_unitted
        if discrete_type_guid is not None:
            self.discrete_type_guid = discrete_type_guid
        if parameters is not None:
            self.parameters = parameters
        if target_database is not None:
            self.target_database = target_database
        if target_table is not None:
            self.target_table = target_table
        if graph_type is not None:
            self.graph_type = graph_type
        if x_axis_parameter is not None:
            self.x_axis_parameter = x_axis_parameter

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.

        Returns
        -------
        str
            The name of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        """
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.

        Returns
        -------
        str
            The guid of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        """
        self._guid = guid

    @property
    def type(self) -> "GrantaServerApiAttributeType":
        """Gets the type of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.

        Returns
        -------
        GrantaServerApiAttributeType
            The type of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "GrantaServerApiAttributeType") -> None:
        """Sets the type of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.

        Parameters
        ----------
        type: GrantaServerApiAttributeType
            The type of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @property
    def unit_symbol(self) -> "str":
        """Gets the unit_symbol of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        If isUnitted is true, then this must have a non empty value

        Returns
        -------
        str
            The unit_symbol of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        """
        return self._unit_symbol

    @unit_symbol.setter
    def unit_symbol(self, unit_symbol: "str") -> None:
        """Sets the unit_symbol of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        If isUnitted is true, then this must have a non empty value

        Parameters
        ----------
        unit_symbol: str
            The unit_symbol of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        """
        self._unit_symbol = unit_symbol

    @property
    def is_unitted(self) -> "bool":
        """Gets the is_unitted of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.

        Returns
        -------
        bool
            The is_unitted of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        """
        return self._is_unitted

    @is_unitted.setter
    def is_unitted(self, is_unitted: "bool") -> None:
        """Sets the is_unitted of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.

        Parameters
        ----------
        is_unitted: bool
            The is_unitted of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        """
        self._is_unitted = is_unitted

    @property
    def discrete_type_guid(self) -> "str":
        """Gets the discrete_type_guid of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        A discrete attribute must define the guid of its discrete type (i.e. list of possible values)

        Returns
        -------
        str
            The discrete_type_guid of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        """
        return self._discrete_type_guid

    @discrete_type_guid.setter
    def discrete_type_guid(self, discrete_type_guid: "str") -> None:
        """Sets the discrete_type_guid of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        A discrete attribute must define the guid of its discrete type (i.e. list of possible values)

        Parameters
        ----------
        discrete_type_guid: str
            The discrete_type_guid of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        """
        self._discrete_type_guid = discrete_type_guid

    @property
    def parameters(
        self,
    ) -> "list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationParameterInfo]":
        """Gets the parameters of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        A float functional attribute must define a list of parameters.

        Returns
        -------
        list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationParameterInfo]
            The parameters of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        """
        return self._parameters

    @parameters.setter
    def parameters(
        self,
        parameters: "list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationParameterInfo]",
    ) -> None:
        """Sets the parameters of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        A float functional attribute must define a list of parameters.

        Parameters
        ----------
        parameters: list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationParameterInfo]
            The parameters of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        """
        self._parameters = parameters

    @property
    def target_database(self) -> "GrantaServerApiObjectIdentifier":
        """Gets the target_database of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.

        Returns
        -------
        GrantaServerApiObjectIdentifier
            The target_database of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        """
        return self._target_database

    @target_database.setter
    def target_database(
        self, target_database: "GrantaServerApiObjectIdentifier"
    ) -> None:
        """Sets the target_database of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.

        Parameters
        ----------
        target_database: GrantaServerApiObjectIdentifier
            The target_database of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        """
        self._target_database = target_database

    @property
    def target_table(self) -> "GrantaServerApiObjectIdentifier":
        """Gets the target_table of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.

        Returns
        -------
        GrantaServerApiObjectIdentifier
            The target_table of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        """
        return self._target_table

    @target_table.setter
    def target_table(self, target_table: "GrantaServerApiObjectIdentifier") -> None:
        """Sets the target_table of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.

        Parameters
        ----------
        target_table: GrantaServerApiObjectIdentifier
            The target_table of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        """
        self._target_table = target_table

    @property
    def graph_type(self) -> "str":
        """Gets the graph_type of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        A float functional attribute must be either a Series or a Grid type graph.

        Returns
        -------
        str
            The graph_type of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        """
        return self._graph_type

    @graph_type.setter
    def graph_type(self, graph_type: "str") -> None:
        """Sets the graph_type of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        A float functional attribute must be either a Series or a Grid type graph.

        Parameters
        ----------
        graph_type: str
            The graph_type of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        """
        self._graph_type = graph_type

    @property
    def x_axis_parameter(self) -> "str":
        """Gets the x_axis_parameter of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        A float functional attribute must define an x-axis. This will be one of the parameters listed in parameters

        Returns
        -------
        str
            The x_axis_parameter of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        """
        return self._x_axis_parameter

    @x_axis_parameter.setter
    def x_axis_parameter(self, x_axis_parameter: "str") -> None:
        """Sets the x_axis_parameter of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        A float functional attribute must define an x-axis. This will be one of the parameters listed in parameters

        Parameters
        ----------
        x_axis_parameter: str
            The x_axis_parameter of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute.
        """
        self._x_axis_parameter = x_axis_parameter

    @classmethod
    def get_real_child_model(cls, data: ModelBase) -> str:
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

    def to_dict(self) -> Dict:
        """Returns the model properties as a dict

        Returns
        -------
        Dict
            Dictionary indexed by property name containing all the model properties
        """
        result = {}

        for attr in self.swagger_types.keys():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(
            GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute, dict
        ):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model

        Returns
        -------
        str
            String representation of the model as a dictionary
        """
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(
            other, GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other