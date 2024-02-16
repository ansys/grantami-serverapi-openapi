"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    BinaryIO,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaExpressionsExpression(ModelBase):  # type: ignore[misc]
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
        "attribute_dependencies": "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
        "constant_dependencies": "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
        "guid": "str",
        "name": "str",
        "parameter_dependencies": "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
        "value": "str",
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimUnit",
    }

    attribute_map: Dict[str, str] = {
        "attribute_dependencies": "attributeDependencies",
        "constant_dependencies": "constantDependencies",
        "guid": "guid",
        "name": "name",
        "parameter_dependencies": "parameterDependencies",
        "value": "value",
        "unit": "unit",
    }

    subtype_mapping: Dict[str, str] = {
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimUnit",
        "attributeDependencies": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "constantDependencies": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "parameterDependencies": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_dependencies: "List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
        constant_dependencies: "List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
        guid: "str",
        name: "str",
        parameter_dependencies: "List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
        value: "str",
        unit: "Optional[GrantaServerApiSchemaSlimEntitiesSlimUnit]" = None,
    ) -> None:
        """GrantaServerApiSchemaExpressionsExpression - a model defined in Swagger

        Parameters
        ----------
            attribute_dependencies: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            constant_dependencies: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            guid: str
            name: str
            parameter_dependencies: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            value: str
            unit: GrantaServerApiSchemaSlimEntitiesSlimUnit, optional
        """
        self._value: str = None  # type: ignore[assignment]
        self._unit = None
        self._attribute_dependencies: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity] = None  # type: ignore[assignment]
        self._constant_dependencies: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity] = None  # type: ignore[assignment]
        self._parameter_dependencies: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity] = None  # type: ignore[assignment]
        self._name: str = None  # type: ignore[assignment]
        self._guid: str = None  # type: ignore[assignment]

        self.value = value
        if unit is not None:
            self.unit = unit
        self.attribute_dependencies = attribute_dependencies
        self.constant_dependencies = constant_dependencies
        self.parameter_dependencies = parameter_dependencies
        self.name = name
        self.guid = guid

    @property
    def value(self) -> "str":
        """Gets the value of this GrantaServerApiSchemaExpressionsExpression.

        Returns
        -------
        str
            The value of this GrantaServerApiSchemaExpressionsExpression.
        """
        return self._value

    @value.setter
    def value(self, value: "str") -> None:
        """Sets the value of this GrantaServerApiSchemaExpressionsExpression.

        Parameters
        ----------
        value: str
            The value of this GrantaServerApiSchemaExpressionsExpression.
        """
        if value is None:
            raise ValueError("Invalid value for 'value', must not be 'None'")
        self._value = value

    @property
    def unit(self) -> "Optional[GrantaServerApiSchemaSlimEntitiesSlimUnit]":
        """Gets the unit of this GrantaServerApiSchemaExpressionsExpression.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimUnit
            The unit of this GrantaServerApiSchemaExpressionsExpression.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "Optional[GrantaServerApiSchemaSlimEntitiesSlimUnit]") -> None:
        """Sets the unit of this GrantaServerApiSchemaExpressionsExpression.

        Parameters
        ----------
        unit: GrantaServerApiSchemaSlimEntitiesSlimUnit
            The unit of this GrantaServerApiSchemaExpressionsExpression.
        """
        self._unit = unit

    @property
    def attribute_dependencies(
        self,
    ) -> "List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]":
        """Gets the attribute_dependencies of this GrantaServerApiSchemaExpressionsExpression.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The attribute_dependencies of this GrantaServerApiSchemaExpressionsExpression.
        """
        return self._attribute_dependencies

    @attribute_dependencies.setter
    def attribute_dependencies(
        self,
        attribute_dependencies: "List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
    ) -> None:
        """Sets the attribute_dependencies of this GrantaServerApiSchemaExpressionsExpression.

        Parameters
        ----------
        attribute_dependencies: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The attribute_dependencies of this GrantaServerApiSchemaExpressionsExpression.
        """
        if attribute_dependencies is None:
            raise ValueError(
                "Invalid value for 'attribute_dependencies', must not be 'None'"
            )
        self._attribute_dependencies = attribute_dependencies

    @property
    def constant_dependencies(
        self,
    ) -> "List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]":
        """Gets the constant_dependencies of this GrantaServerApiSchemaExpressionsExpression.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The constant_dependencies of this GrantaServerApiSchemaExpressionsExpression.
        """
        return self._constant_dependencies

    @constant_dependencies.setter
    def constant_dependencies(
        self,
        constant_dependencies: "List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
    ) -> None:
        """Sets the constant_dependencies of this GrantaServerApiSchemaExpressionsExpression.

        Parameters
        ----------
        constant_dependencies: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The constant_dependencies of this GrantaServerApiSchemaExpressionsExpression.
        """
        if constant_dependencies is None:
            raise ValueError(
                "Invalid value for 'constant_dependencies', must not be 'None'"
            )
        self._constant_dependencies = constant_dependencies

    @property
    def parameter_dependencies(
        self,
    ) -> "List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]":
        """Gets the parameter_dependencies of this GrantaServerApiSchemaExpressionsExpression.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The parameter_dependencies of this GrantaServerApiSchemaExpressionsExpression.
        """
        return self._parameter_dependencies

    @parameter_dependencies.setter
    def parameter_dependencies(
        self,
        parameter_dependencies: "List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
    ) -> None:
        """Sets the parameter_dependencies of this GrantaServerApiSchemaExpressionsExpression.

        Parameters
        ----------
        parameter_dependencies: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The parameter_dependencies of this GrantaServerApiSchemaExpressionsExpression.
        """
        if parameter_dependencies is None:
            raise ValueError(
                "Invalid value for 'parameter_dependencies', must not be 'None'"
            )
        self._parameter_dependencies = parameter_dependencies

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaExpressionsExpression.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaExpressionsExpression.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaExpressionsExpression.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaExpressionsExpression.
        """
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaExpressionsExpression.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaExpressionsExpression.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaExpressionsExpression.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaExpressionsExpression.
        """
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        self._guid = guid

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

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()  # type: ignore[no-any-return]

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiSchemaExpressionsExpression):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
