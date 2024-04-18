# Copyright (C) 2023 - 2024 ANSYS, Inc. and/or its affiliates.
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
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier(ModelBase):
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
        "database": "GrantaServerApiObjectIdentifier",
        "database_key": "str",
        "mappings": "list[GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier]",
        "table": "GrantaServerApiObjectIdentifier",
    }

    attribute_map: Dict[str, str] = {
        "database": "database",
        "database_key": "databaseKey",
        "mappings": "mappings",
        "table": "table",
    }

    subtype_mapping: Dict[str, str] = {
        "database": "GrantaServerApiObjectIdentifier",
        "table": "GrantaServerApiObjectIdentifier",
        "mappings": "GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        database: "Union[GrantaServerApiObjectIdentifier, Unset_Type]" = Unset,
        database_key: "Union[str, None, Unset_Type]" = Unset,
        mappings: "Union[List[GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier], None, Unset_Type]" = Unset,
        table: "Union[GrantaServerApiObjectIdentifier, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier - a model defined in Swagger

        Parameters
        ----------
        database: GrantaServerApiObjectIdentifier, optional
        database_key: str, optional
        mappings: List[GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier], optional
        table: GrantaServerApiObjectIdentifier, optional
        """
        self._database: Union[GrantaServerApiObjectIdentifier, Unset_Type] = Unset
        self._database_key: Union[str, None, Unset_Type] = Unset
        self._table: Union[GrantaServerApiObjectIdentifier, Unset_Type] = Unset
        self._mappings: Union[
            List[GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier],
            None,
            Unset_Type,
        ] = Unset

        if database is not Unset:
            self.database = database
        if database_key is not Unset:
            self.database_key = database_key
        if table is not Unset:
            self.table = table
        if mappings is not Unset:
            self.mappings = mappings

    @property
    def database(self) -> "Union[GrantaServerApiObjectIdentifier, Unset_Type]":
        """Gets the database of this GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        Union[GrantaServerApiObjectIdentifier, Unset_Type]
            The database of this GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier.
        """
        return self._database

    @database.setter
    def database(self, database: "Union[GrantaServerApiObjectIdentifier, Unset_Type]") -> None:
        """Sets the database of this GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        database: Union[GrantaServerApiObjectIdentifier, Unset_Type]
            The database of this GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier.
        """
        # Field is not nullable
        if database is None:
            raise ValueError("Invalid value for 'database', must not be 'None'")
        self._database = database

    @property
    def database_key(self) -> "Union[str, None, Unset_Type]":
        """Gets the database_key of this GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        Union[str, None, Unset_Type]
            The database_key of this GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier.
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key: "Union[str, None, Unset_Type]") -> None:
        """Sets the database_key of this GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        database_key: Union[str, None, Unset_Type]
            The database_key of this GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier.
        """
        self._database_key = database_key

    @property
    def table(self) -> "Union[GrantaServerApiObjectIdentifier, Unset_Type]":
        """Gets the table of this GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        Union[GrantaServerApiObjectIdentifier, Unset_Type]
            The table of this GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier.
        """
        return self._table

    @table.setter
    def table(self, table: "Union[GrantaServerApiObjectIdentifier, Unset_Type]") -> None:
        """Sets the table of this GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        table: Union[GrantaServerApiObjectIdentifier, Unset_Type]
            The table of this GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier.
        """
        # Field is not nullable
        if table is None:
            raise ValueError("Invalid value for 'table', must not be 'None'")
        self._table = table

    @property
    def mappings(
        self,
    ) -> "Union[List[GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier], None, Unset_Type]":
        """Gets the mappings of this GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier.
        Mappings for items from this table to the integration schema attributes.

        Returns
        -------
        Union[List[GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier], None, Unset_Type]
            The mappings of this GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier.
        """
        return self._mappings

    @mappings.setter
    def mappings(
        self,
        mappings: "Union[List[GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier], None, Unset_Type]",
    ) -> None:
        """Sets the mappings of this GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier.
        Mappings for items from this table to the integration schema attributes.

        Parameters
        ----------
        mappings: Union[List[GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier], None, Unset_Type]
            The mappings of this GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier.
        """
        self._mappings = mappings

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
            other,
            GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
