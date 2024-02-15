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


class GrantaServerApiSchemaSlimEntitiesSlimAttribute(ModelBase):  # type: ignore[misc]
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
        "display_names": "dict(str, str)",
        "guid": "str",
        "name": "str",
        "type": "GrantaServerApiAttributeType",
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
    }

    attribute_map: Dict[str, str] = {
        "display_names": "displayNames",
        "guid": "guid",
        "name": "name",
        "type": "type",
        "about_attribute": "aboutAttribute",
    }

    subtype_mapping: Dict[str, str] = {
        "type": "GrantaServerApiAttributeType",
        "aboutAttribute": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        display_names: "Dict[str, str]",
        guid: "str",
        name: "str",
        type: "GrantaServerApiAttributeType",
        about_attribute: "Optional[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]" = None,
    ) -> None:
        """GrantaServerApiSchemaSlimEntitiesSlimAttribute - a model defined in Swagger

        Parameters
        ----------
            display_names: Dict[str, str]
            guid: str
            name: str
            type: GrantaServerApiAttributeType
            about_attribute: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, optional
        """
        self._type: GrantaServerApiAttributeType = None  # type: ignore[assignment]
        self._about_attribute = None
        self._display_names: Dict[str, str] = None  # type: ignore[assignment]
        self._name: str = None  # type: ignore[assignment]
        self._guid: str = None  # type: ignore[assignment]

        self.type = type
        if about_attribute is not None:
            self.about_attribute = about_attribute
        self.display_names = display_names
        self.name = name
        self.guid = guid

    @property
    def type(self) -> "GrantaServerApiAttributeType":
        """Gets the type of this GrantaServerApiSchemaSlimEntitiesSlimAttribute.

        Returns
        -------
        GrantaServerApiAttributeType
            The type of this GrantaServerApiSchemaSlimEntitiesSlimAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "GrantaServerApiAttributeType") -> None:
        """Sets the type of this GrantaServerApiSchemaSlimEntitiesSlimAttribute.

        Parameters
        ----------
        type: GrantaServerApiAttributeType
            The type of this GrantaServerApiSchemaSlimEntitiesSlimAttribute.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @property
    def about_attribute(
        self,
    ) -> "Optional[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]":
        """Gets the about_attribute of this GrantaServerApiSchemaSlimEntitiesSlimAttribute.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
            The about_attribute of this GrantaServerApiSchemaSlimEntitiesSlimAttribute.
        """
        return self._about_attribute

    @about_attribute.setter
    def about_attribute(
        self,
        about_attribute: "Optional[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
    ) -> None:
        """Sets the about_attribute of this GrantaServerApiSchemaSlimEntitiesSlimAttribute.

        Parameters
        ----------
        about_attribute: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
            The about_attribute of this GrantaServerApiSchemaSlimEntitiesSlimAttribute.
        """
        self._about_attribute = about_attribute

    @property
    def display_names(self) -> "Dict[str, str]":
        """Gets the display_names of this GrantaServerApiSchemaSlimEntitiesSlimAttribute.

        Returns
        -------
        dict(str, str)
            The display_names of this GrantaServerApiSchemaSlimEntitiesSlimAttribute.
        """
        return self._display_names

    @display_names.setter
    def display_names(self, display_names: "Dict[str, str]") -> None:
        """Sets the display_names of this GrantaServerApiSchemaSlimEntitiesSlimAttribute.

        Parameters
        ----------
        display_names: Dict[str, str]
            The display_names of this GrantaServerApiSchemaSlimEntitiesSlimAttribute.
        """
        if display_names is None:
            raise ValueError("Invalid value for 'display_names', must not be 'None'")
        self._display_names = display_names

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaSlimEntitiesSlimAttribute.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaSlimEntitiesSlimAttribute.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaSlimEntitiesSlimAttribute.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaSlimEntitiesSlimAttribute.
        """
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaSlimEntitiesSlimAttribute.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaSlimEntitiesSlimAttribute.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaSlimEntitiesSlimAttribute.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaSlimEntitiesSlimAttribute.
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
        if not isinstance(other, GrantaServerApiSchemaSlimEntitiesSlimAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
