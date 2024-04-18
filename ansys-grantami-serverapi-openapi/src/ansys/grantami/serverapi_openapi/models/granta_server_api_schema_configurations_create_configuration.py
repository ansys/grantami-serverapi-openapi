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
    BinaryIO,
    Dict,
    List,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase, Unset, Unset_Type


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaConfigurationsCreateConfiguration(ModelBase):
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
        "name": "str",
        "value": "str",
        "description": "str",
        "guid": "str",
    }

    attribute_map: Dict[str, str] = {
        "name": "name",
        "value": "value",
        "description": "description",
        "guid": "guid",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        name: "str",
        value: "str",
        description: "Union[str, None, Unset_Type]" = Unset,
        guid: "Union[str, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaConfigurationsCreateConfiguration - a model defined in Swagger

        Parameters
        ----------
        name: str
        value: str
        description: str, optional
        guid: str, optional
        """
        self._description: Union[str, None, Unset_Type] = Unset
        self._value: str
        self._name: str
        self._guid: Union[str, Unset_Type] = Unset

        if description is not Unset:
            self.description = description
        self.value = value
        self.name = name
        if guid is not Unset:
            self.guid = guid

    @property
    def description(self) -> "Union[str, None, Unset_Type]":
        """Gets the description of this GrantaServerApiSchemaConfigurationsCreateConfiguration.

        Returns
        -------
        Union[str, None, Unset_Type]
            The description of this GrantaServerApiSchemaConfigurationsCreateConfiguration.
        """
        return self._description

    @description.setter
    def description(self, description: "Union[str, None, Unset_Type]") -> None:
        """Sets the description of this GrantaServerApiSchemaConfigurationsCreateConfiguration.

        Parameters
        ----------
        description: Union[str, None, Unset_Type]
            The description of this GrantaServerApiSchemaConfigurationsCreateConfiguration.
        """
        self._description = description

    @property
    def value(self) -> "str":
        """Gets the value of this GrantaServerApiSchemaConfigurationsCreateConfiguration.

        Returns
        -------
        str
            The value of this GrantaServerApiSchemaConfigurationsCreateConfiguration.
        """
        return self._value

    @value.setter
    def value(self, value: "str") -> None:
        """Sets the value of this GrantaServerApiSchemaConfigurationsCreateConfiguration.

        Parameters
        ----------
        value: str
            The value of this GrantaServerApiSchemaConfigurationsCreateConfiguration.
        """
        # Field is not nullable
        if value is None:
            raise ValueError("Invalid value for 'value', must not be 'None'")
        # Field is required
        if value is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'value', must not be 'Unset'")
        self._value = value

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaConfigurationsCreateConfiguration.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaConfigurationsCreateConfiguration.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaConfigurationsCreateConfiguration.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaConfigurationsCreateConfiguration.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        # Field is required
        if name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'name', must not be 'Unset'")
        self._name = name

    @property
    def guid(self) -> "Union[str, Unset_Type]":
        """Gets the guid of this GrantaServerApiSchemaConfigurationsCreateConfiguration.

        Returns
        -------
        Union[str, Unset_Type]
            The guid of this GrantaServerApiSchemaConfigurationsCreateConfiguration.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, Unset_Type]") -> None:
        """Sets the guid of this GrantaServerApiSchemaConfigurationsCreateConfiguration.

        Parameters
        ----------
        guid: Union[str, Unset_Type]
            The guid of this GrantaServerApiSchemaConfigurationsCreateConfiguration.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        self._guid = guid

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
        if not isinstance(
            other, GrantaServerApiSchemaConfigurationsCreateConfiguration
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
