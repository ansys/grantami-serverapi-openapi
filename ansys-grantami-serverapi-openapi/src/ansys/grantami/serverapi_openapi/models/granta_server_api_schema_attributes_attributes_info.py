"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase


if TYPE_CHECKING:
    from . import *


class GrantaServerApiSchemaAttributesAttributesInfo(ModelBase):
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
        "attributes": "list[GrantaServerApiSchemaSlimEntitiesSlimAttribute]",
    }

    attribute_map = {
        "attributes": "attributes",
    }

    subtype_mapping = {
        "attributes": "GrantaServerApiSchemaSlimEntitiesSlimAttribute",
    }

    discriminator = None

    def __init__(
        self,
        *,
        attributes: "List[GrantaServerApiSchemaSlimEntitiesSlimAttribute]",
    ) -> None:
        """GrantaServerApiSchemaAttributesAttributesInfo - a model defined in Swagger

        Parameters
        ----------
            attributes: List[GrantaServerApiSchemaSlimEntitiesSlimAttribute]
        """
        self._attributes = None

        self.attributes = attributes

    @property
    def attributes(self) -> "list[GrantaServerApiSchemaSlimEntitiesSlimAttribute]":
        """Gets the attributes of this GrantaServerApiSchemaAttributesAttributesInfo.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimAttribute]
            The attributes of this GrantaServerApiSchemaAttributesAttributesInfo.
        """
        return self._attributes

    @attributes.setter
    def attributes(
        self, attributes: "list[GrantaServerApiSchemaSlimEntitiesSlimAttribute]"
    ) -> None:
        """Sets the attributes of this GrantaServerApiSchemaAttributesAttributesInfo.

        Parameters
        ----------
        attributes: list[GrantaServerApiSchemaSlimEntitiesSlimAttribute]
            The attributes of this GrantaServerApiSchemaAttributesAttributesInfo.
        """
        if attributes is None:
            raise ValueError("Invalid value for 'attributes', must not be 'None'")
        self._attributes = attributes

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
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiSchemaAttributesAttributesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
