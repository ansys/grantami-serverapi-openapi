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


class GrantaServerApiSchemaConfigurationsConfigurationsInfo(ModelBase):
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
        "configurations": "list[GrantaServerApiSchemaSlimEntitiesSlimConfiguration]",
    }

    attribute_map: Dict[str, str] = {
        "configurations": "configurations",
    }

    subtype_mapping: Dict[str, str] = {
        "configurations": "GrantaServerApiSchemaSlimEntitiesSlimConfiguration",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        configurations: "List[GrantaServerApiSchemaSlimEntitiesSlimConfiguration]",
    ) -> None:
        """GrantaServerApiSchemaConfigurationsConfigurationsInfo - a model defined in Swagger

        Parameters
        ----------
        configurations: List[GrantaServerApiSchemaSlimEntitiesSlimConfiguration]
        """
        self._configurations: List[GrantaServerApiSchemaSlimEntitiesSlimConfiguration]

        self.configurations = configurations

    @property
    def configurations(
        self,
    ) -> "List[GrantaServerApiSchemaSlimEntitiesSlimConfiguration]":
        """Gets the configurations of this GrantaServerApiSchemaConfigurationsConfigurationsInfo.

        Returns
        -------
        List[GrantaServerApiSchemaSlimEntitiesSlimConfiguration]
            The configurations of this GrantaServerApiSchemaConfigurationsConfigurationsInfo.
        """
        return self._configurations

    @configurations.setter
    def configurations(
        self, configurations: "List[GrantaServerApiSchemaSlimEntitiesSlimConfiguration]"
    ) -> None:
        """Sets the configurations of this GrantaServerApiSchemaConfigurationsConfigurationsInfo.

        Parameters
        ----------
        configurations: List[GrantaServerApiSchemaSlimEntitiesSlimConfiguration]
            The configurations of this GrantaServerApiSchemaConfigurationsConfigurationsInfo.
        """
        # Field is not nullable
        if configurations is None:
            raise ValueError("Invalid value for 'configurations', must not be 'None'")
        # Field is required
        if configurations is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'configurations', must not be 'Unset'")
        self._configurations = configurations

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
        if not isinstance(other, GrantaServerApiSchemaConfigurationsConfigurationsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
