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


class GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier(ModelBase):  # type: ignore[misc]
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
        "link_source_type": "GrantaServerApiIntegrationSchemaLinkSourceType",
        "parameter_mappings": "list[GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier]",
        "source": "GrantaServerApiObjectIdentifier",
        "target_guid": "str",
        "target_identity": "int",
    }

    attribute_map: Dict[str, str] = {
        "link_source_type": "linkSourceType",
        "parameter_mappings": "parameterMappings",
        "source": "source",
        "target_guid": "targetGuid",
        "target_identity": "targetIdentity",
    }

    subtype_mapping: Dict[str, str] = {
        "source": "GrantaServerApiObjectIdentifier",
        "parameterMappings": "GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier",
        "linkSourceType": "GrantaServerApiIntegrationSchemaLinkSourceType",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        link_source_type: "Optional[GrantaServerApiIntegrationSchemaLinkSourceType]" = None,
        parameter_mappings: "Optional[List[GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier]]" = None,
        source: "Optional[GrantaServerApiObjectIdentifier]" = None,
        target_guid: "Optional[str]" = None,
        target_identity: "Optional[int]" = None,
    ) -> None:
        """GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier - a model defined in Swagger

        Parameters
        ----------
            link_source_type: GrantaServerApiIntegrationSchemaLinkSourceType, optional
            parameter_mappings: List[GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier], optional
            source: GrantaServerApiObjectIdentifier, optional
            target_guid: str, optional
            target_identity: int, optional
        """
        self._source = None
        self._target_identity = None
        self._target_guid = None
        self._parameter_mappings = None
        self._link_source_type = None

        if source is not None:
            self.source = source
        if target_identity is not None:
            self.target_identity = target_identity
        if target_guid is not None:
            self.target_guid = target_guid
        if parameter_mappings is not None:
            self.parameter_mappings = parameter_mappings
        if link_source_type is not None:
            self.link_source_type = link_source_type

    @property
    def source(self) -> "Optional[GrantaServerApiObjectIdentifier]":
        """Gets the source of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        GrantaServerApiObjectIdentifier
            The source of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        """
        return self._source

    @source.setter
    def source(self, source: "Optional[GrantaServerApiObjectIdentifier]") -> None:
        """Sets the source of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        source: GrantaServerApiObjectIdentifier
            The source of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        """
        self._source = source

    @property
    def target_identity(self) -> "Optional[int]":
        """Gets the target_identity of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        The identity of the integration schema attribute

        Returns
        -------
        int
            The target_identity of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        """
        return self._target_identity

    @target_identity.setter
    def target_identity(self, target_identity: "Optional[int]") -> None:
        """Sets the target_identity of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        The identity of the integration schema attribute

        Parameters
        ----------
        target_identity: int
            The target_identity of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        """
        self._target_identity = target_identity

    @property
    def target_guid(self) -> "Optional[str]":
        """Gets the target_guid of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        The guid of the integration schema attribute

        Returns
        -------
        str
            The target_guid of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        """
        return self._target_guid

    @target_guid.setter
    def target_guid(self, target_guid: "Optional[str]") -> None:
        """Sets the target_guid of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        The guid of the integration schema attribute

        Parameters
        ----------
        target_guid: str
            The target_guid of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        """
        self._target_guid = target_guid

    @property
    def parameter_mappings(
        self,
    ) -> "Optional[List[GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier]]":
        """Gets the parameter_mappings of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        Any mapped parameters (float functional attributes only). The target parameters must be defined on the target integration attribute.  Not every parameters from the source database needs to be mapped for each attribute.

        Returns
        -------
        list[GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier]
            The parameter_mappings of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        """
        return self._parameter_mappings

    @parameter_mappings.setter
    def parameter_mappings(
        self,
        parameter_mappings: "Optional[List[GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier]]",
    ) -> None:
        """Sets the parameter_mappings of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        Any mapped parameters (float functional attributes only). The target parameters must be defined on the target integration attribute.  Not every parameters from the source database needs to be mapped for each attribute.

        Parameters
        ----------
        parameter_mappings: List[GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier]
            The parameter_mappings of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        """
        self._parameter_mappings = parameter_mappings

    @property
    def link_source_type(
        self,
    ) -> "Optional[GrantaServerApiIntegrationSchemaLinkSourceType]":
        """Gets the link_source_type of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        GrantaServerApiIntegrationSchemaLinkSourceType
            The link_source_type of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        """
        return self._link_source_type

    @link_source_type.setter
    def link_source_type(
        self,
        link_source_type: "Optional[GrantaServerApiIntegrationSchemaLinkSourceType]",
    ) -> None:
        """Sets the link_source_type of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        link_source_type: GrantaServerApiIntegrationSchemaLinkSourceType
            The link_source_type of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        """
        self._link_source_type = link_source_type

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
            GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
