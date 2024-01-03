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


class GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier(
    ModelBase
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
    swagger_types = {
        "database": "GrantaServerApiObjectIdentifier",
        "database_key": "str",
        "mappings": "list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyMappingOfGrantaServerApiObjectIdentifier]",
        "table": "GrantaServerApiObjectIdentifier",
    }

    attribute_map = {
        "database": "database",
        "database_key": "databaseKey",
        "mappings": "mappings",
        "table": "table",
    }

    subtype_mapping = {
        "database": "GrantaServerApiObjectIdentifier",
        "table": "GrantaServerApiObjectIdentifier",
        "mappings": "GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyMappingOfGrantaServerApiObjectIdentifier",
    }

    discriminator = None

    def __init__(
        self,
        *,
        database: "Optional[GrantaServerApiObjectIdentifier]" = None,
        database_key: "Optional[str]" = None,
        mappings: "Optional[List[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyMappingOfGrantaServerApiObjectIdentifier]]" = None,
        table: "Optional[GrantaServerApiObjectIdentifier]" = None,
    ) -> None:
        """GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier - a model defined in Swagger

        Parameters
        ----------
            database: GrantaServerApiObjectIdentifier, optional
            database_key: str, optional
            mappings: List[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyMappingOfGrantaServerApiObjectIdentifier], optional
            table: GrantaServerApiObjectIdentifier, optional
        """
        self._database = None
        self._database_key = None
        self._table = None
        self._mappings = None

        if database is not None:
            self.database = database
        if database_key is not None:
            self.database_key = database_key
        if table is not None:
            self.table = table
        if mappings is not None:
            self.mappings = mappings

    @property
    def database(self) -> "GrantaServerApiObjectIdentifier":
        """Gets the database of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        GrantaServerApiObjectIdentifier
            The database of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier.
        """
        return self._database

    @database.setter
    def database(self, database: "GrantaServerApiObjectIdentifier") -> None:
        """Sets the database of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        database: GrantaServerApiObjectIdentifier
            The database of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier.
        """
        self._database = database

    @property
    def database_key(self) -> "str":
        """Gets the database_key of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        str
            The database_key of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier.
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key: "str") -> None:
        """Sets the database_key of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        database_key: str
            The database_key of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier.
        """
        self._database_key = database_key

    @property
    def table(self) -> "GrantaServerApiObjectIdentifier":
        """Gets the table of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        GrantaServerApiObjectIdentifier
            The table of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier.
        """
        return self._table

    @table.setter
    def table(self, table: "GrantaServerApiObjectIdentifier") -> None:
        """Sets the table of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        table: GrantaServerApiObjectIdentifier
            The table of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier.
        """
        self._table = table

    @property
    def mappings(
        self,
    ) -> "list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyMappingOfGrantaServerApiObjectIdentifier]":
        """Gets the mappings of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier.
        Mappings for items from this table to the integration schema attributes.

        Returns
        -------
        list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyMappingOfGrantaServerApiObjectIdentifier]
            The mappings of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier.
        """
        return self._mappings

    @mappings.setter
    def mappings(
        self,
        mappings: "list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyMappingOfGrantaServerApiObjectIdentifier]",
    ) -> None:
        """Sets the mappings of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier.
        Mappings for items from this table to the integration schema attributes.

        Parameters
        ----------
        mappings: list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyMappingOfGrantaServerApiObjectIdentifier]
            The mappings of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier.
        """
        self._mappings = mappings

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
        if not isinstance(
            other,
            GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
