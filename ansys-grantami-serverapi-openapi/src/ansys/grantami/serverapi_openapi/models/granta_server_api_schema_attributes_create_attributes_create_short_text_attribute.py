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
from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_attributes_create_attributes_create_attribute import (
    GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute(
    GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute
):
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
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "data_rule": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "guid": "str",
        "help_path": "str",
        "is_unique": "bool",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "name": "name",
        "about_attribute": "aboutAttribute",
        "data_rule": "dataRule",
        "default_threshold_type": "defaultThresholdType",
        "guid": "guid",
        "help_path": "helpPath",
        "is_unique": "isUnique",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {
        "dataRule": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        name: "str",
        about_attribute: "Optional[GrantaServerApiSchemaSlimEntitiesSlimEntity]" = None,
        data_rule: "Optional[GrantaServerApiSchemaSlimEntitiesSlimEntity]" = None,
        default_threshold_type: "Optional[GrantaServerApiSchemaAttributesAttributeThresholdType]" = None,
        guid: "Optional[str]" = None,
        help_path: "Optional[str]" = None,
        is_unique: "Optional[bool]" = None,
        type: "str" = "shortText",
    ) -> None:
        """GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute - a model defined in Swagger

        Parameters
        ----------
            name: str
            about_attribute: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
            data_rule: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
            default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType, optional
            guid: str, optional
            help_path: str, optional
            is_unique: bool, optional
            type: str
        """
        super().__init__(
            name=name,
            about_attribute=about_attribute,
            default_threshold_type=default_threshold_type,
            guid=guid,
            help_path=help_path,
        )
        self._type: str = None  # type: ignore[assignment]
        self._is_unique = None
        self._data_rule = None

        self.type = type
        if is_unique is not None:
            self.is_unique = is_unique
        if data_rule is not None:
            self.data_rule = data_rule

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @property
    def is_unique(self) -> "Optional[bool]":
        """Gets the is_unique of this GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute.
        Whether or not the attribute is constrained to contain a unique value

        Returns
        -------
        bool
            The is_unique of this GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute.
        """
        return self._is_unique

    @is_unique.setter
    def is_unique(self, is_unique: "Optional[bool]") -> None:
        """Sets the is_unique of this GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute.
        Whether or not the attribute is constrained to contain a unique value

        Parameters
        ----------
        is_unique: bool
            The is_unique of this GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute.
        """
        self._is_unique = is_unique

    @property
    def data_rule(self) -> "Optional[GrantaServerApiSchemaSlimEntitiesSlimEntity]":
        """Gets the data_rule of this GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimEntity
            The data_rule of this GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute.
        """
        return self._data_rule

    @data_rule.setter
    def data_rule(
        self, data_rule: "Optional[GrantaServerApiSchemaSlimEntitiesSlimEntity]"
    ) -> None:
        """Sets the data_rule of this GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute.

        Parameters
        ----------
        data_rule: GrantaServerApiSchemaSlimEntitiesSlimEntity
            The data_rule of this GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute.
        """
        self._data_rule = data_rule

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
        if not isinstance(
            other,
            GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
