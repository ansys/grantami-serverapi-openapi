# Copyright (C) 2023 - 2025 ANSYS, Inc. and/or its affiliates.
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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaStandardName(ModelBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes
    ----------
    swagger_types: dict[str, str]
        The key is attribute name and the value is attribute type.
    attribute_map: dict[str, str]
        The key is attribute name and the value is json key in definition.
    subtype_mapping: dict[str, str]
        The key is the unmangled property name and the value is the corresponding type.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "database_guid": "str",
        "database_key": "str",
        "database_version_guid": "str",
        "guid": "str",
        "mapped_attributes": "list[GsaSlimAttribute]",
        "mapped_cross_database_record_link_groups": "list[GsaSlimNamedEntity]",
        "mapped_parameters": "list[GsaSlimNamedEntity]",
        "mapped_record_link_groups": "list[GsaSlimNamedEntity]",
        "name": "str",
    }

    attribute_map: dict[str, str] = {
        "database_guid": "databaseGuid",
        "database_key": "databaseKey",
        "database_version_guid": "databaseVersionGuid",
        "guid": "guid",
        "mapped_attributes": "mappedAttributes",
        "mapped_cross_database_record_link_groups": "mappedCrossDatabaseRecordLinkGroups",
        "mapped_parameters": "mappedParameters",
        "mapped_record_link_groups": "mappedRecordLinkGroups",
        "name": "name",
    }

    subtype_mapping: dict[str, str] = {
        "mappedAttributes": "GsaSlimAttribute",
        "mappedParameters": "GsaSlimNamedEntity",
        "mappedRecordLinkGroups": "GsaSlimNamedEntity",
        "mappedCrossDatabaseRecordLinkGroups": "GsaSlimNamedEntity",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        database_guid: "str",
        database_key: "str",
        database_version_guid: "str",
        guid: "str",
        mapped_attributes: "list[GsaSlimAttribute]",
        mapped_cross_database_record_link_groups: "list[GsaSlimNamedEntity]",
        mapped_parameters: "list[GsaSlimNamedEntity]",
        mapped_record_link_groups: "list[GsaSlimNamedEntity]",
        name: "str",
    ) -> None:
        """GsaStandardName - a model defined in Swagger

        Parameters
        ----------
        database_guid: str
        database_key: str
        database_version_guid: str
        guid: str
        mapped_attributes: list[GsaSlimAttribute]
        mapped_cross_database_record_link_groups: list[GsaSlimNamedEntity]
        mapped_parameters: list[GsaSlimNamedEntity]
        mapped_record_link_groups: list[GsaSlimNamedEntity]
        name: str
        """
        self._mapped_attributes: list[GsaSlimAttribute]
        self._mapped_parameters: list[GsaSlimNamedEntity]
        self._mapped_record_link_groups: list[GsaSlimNamedEntity]
        self._mapped_cross_database_record_link_groups: list[GsaSlimNamedEntity]
        self._database_key: str
        self._database_guid: str
        self._database_version_guid: str
        self._name: str
        self._guid: str

        self.mapped_attributes = mapped_attributes
        self.mapped_parameters = mapped_parameters
        self.mapped_record_link_groups = mapped_record_link_groups
        self.mapped_cross_database_record_link_groups = mapped_cross_database_record_link_groups
        self.database_key = database_key
        self.database_guid = database_guid
        self.database_version_guid = database_version_guid
        self.name = name
        self.guid = guid

    @property
    def mapped_attributes(self) -> "list[GsaSlimAttribute]":
        """Gets the mapped_attributes of this GsaStandardName.

        Returns
        -------
        list[GsaSlimAttribute]
            The mapped_attributes of this GsaStandardName.
        """
        return self._mapped_attributes

    @mapped_attributes.setter
    def mapped_attributes(self, mapped_attributes: "list[GsaSlimAttribute]") -> None:
        """Sets the mapped_attributes of this GsaStandardName.

        Parameters
        ----------
        mapped_attributes: list[GsaSlimAttribute]
            The mapped_attributes of this GsaStandardName.
        """
        # Field is not nullable
        if mapped_attributes is None:
            raise ValueError("Invalid value for 'mapped_attributes', must not be 'None'")
        # Field is required
        if mapped_attributes is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'mapped_attributes', must not be 'Unset'")
        self._mapped_attributes = mapped_attributes

    @property
    def mapped_parameters(self) -> "list[GsaSlimNamedEntity]":
        """Gets the mapped_parameters of this GsaStandardName.

        Returns
        -------
        list[GsaSlimNamedEntity]
            The mapped_parameters of this GsaStandardName.
        """
        return self._mapped_parameters

    @mapped_parameters.setter
    def mapped_parameters(self, mapped_parameters: "list[GsaSlimNamedEntity]") -> None:
        """Sets the mapped_parameters of this GsaStandardName.

        Parameters
        ----------
        mapped_parameters: list[GsaSlimNamedEntity]
            The mapped_parameters of this GsaStandardName.
        """
        # Field is not nullable
        if mapped_parameters is None:
            raise ValueError("Invalid value for 'mapped_parameters', must not be 'None'")
        # Field is required
        if mapped_parameters is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'mapped_parameters', must not be 'Unset'")
        self._mapped_parameters = mapped_parameters

    @property
    def mapped_record_link_groups(self) -> "list[GsaSlimNamedEntity]":
        """Gets the mapped_record_link_groups of this GsaStandardName.

        Returns
        -------
        list[GsaSlimNamedEntity]
            The mapped_record_link_groups of this GsaStandardName.
        """
        return self._mapped_record_link_groups

    @mapped_record_link_groups.setter
    def mapped_record_link_groups(
        self, mapped_record_link_groups: "list[GsaSlimNamedEntity]"
    ) -> None:
        """Sets the mapped_record_link_groups of this GsaStandardName.

        Parameters
        ----------
        mapped_record_link_groups: list[GsaSlimNamedEntity]
            The mapped_record_link_groups of this GsaStandardName.
        """
        # Field is not nullable
        if mapped_record_link_groups is None:
            raise ValueError("Invalid value for 'mapped_record_link_groups', must not be 'None'")
        # Field is required
        if mapped_record_link_groups is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'mapped_record_link_groups', must not be 'Unset'")
        self._mapped_record_link_groups = mapped_record_link_groups

    @property
    def mapped_cross_database_record_link_groups(self) -> "list[GsaSlimNamedEntity]":
        """Gets the mapped_cross_database_record_link_groups of this GsaStandardName.

        Returns
        -------
        list[GsaSlimNamedEntity]
            The mapped_cross_database_record_link_groups of this GsaStandardName.
        """
        return self._mapped_cross_database_record_link_groups

    @mapped_cross_database_record_link_groups.setter
    def mapped_cross_database_record_link_groups(
        self, mapped_cross_database_record_link_groups: "list[GsaSlimNamedEntity]"
    ) -> None:
        """Sets the mapped_cross_database_record_link_groups of this GsaStandardName.

        Parameters
        ----------
        mapped_cross_database_record_link_groups: list[GsaSlimNamedEntity]
            The mapped_cross_database_record_link_groups of this GsaStandardName.
        """
        # Field is not nullable
        if mapped_cross_database_record_link_groups is None:
            raise ValueError(
                "Invalid value for 'mapped_cross_database_record_link_groups', must not be 'None'"
            )
        # Field is required
        if mapped_cross_database_record_link_groups is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'mapped_cross_database_record_link_groups', must not be 'Unset'"
            )
        self._mapped_cross_database_record_link_groups = mapped_cross_database_record_link_groups

    @property
    def database_key(self) -> "str":
        """Gets the database_key of this GsaStandardName.

        Returns
        -------
        str
            The database_key of this GsaStandardName.
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key: "str") -> None:
        """Sets the database_key of this GsaStandardName.

        Parameters
        ----------
        database_key: str
            The database_key of this GsaStandardName.
        """
        # Field is not nullable
        if database_key is None:
            raise ValueError("Invalid value for 'database_key', must not be 'None'")
        # Field is required
        if database_key is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'database_key', must not be 'Unset'")
        self._database_key = database_key

    @property
    def database_guid(self) -> "str":
        """Gets the database_guid of this GsaStandardName.

        Returns
        -------
        str
            The database_guid of this GsaStandardName.
        """
        return self._database_guid

    @database_guid.setter
    def database_guid(self, database_guid: "str") -> None:
        """Sets the database_guid of this GsaStandardName.

        Parameters
        ----------
        database_guid: str
            The database_guid of this GsaStandardName.
        """
        # Field is not nullable
        if database_guid is None:
            raise ValueError("Invalid value for 'database_guid', must not be 'None'")
        # Field is required
        if database_guid is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'database_guid', must not be 'Unset'")
        self._database_guid = database_guid

    @property
    def database_version_guid(self) -> "str":
        """Gets the database_version_guid of this GsaStandardName.

        Returns
        -------
        str
            The database_version_guid of this GsaStandardName.
        """
        return self._database_version_guid

    @database_version_guid.setter
    def database_version_guid(self, database_version_guid: "str") -> None:
        """Sets the database_version_guid of this GsaStandardName.

        Parameters
        ----------
        database_version_guid: str
            The database_version_guid of this GsaStandardName.
        """
        # Field is not nullable
        if database_version_guid is None:
            raise ValueError("Invalid value for 'database_version_guid', must not be 'None'")
        # Field is required
        if database_version_guid is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'database_version_guid', must not be 'Unset'")
        self._database_version_guid = database_version_guid

    @property
    def name(self) -> "str":
        """Gets the name of this GsaStandardName.

        Returns
        -------
        str
            The name of this GsaStandardName.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GsaStandardName.

        Parameters
        ----------
        name: str
            The name of this GsaStandardName.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        # Field is required
        if name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'name', must not be 'Unset'")
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GsaStandardName.

        Returns
        -------
        str
            The guid of this GsaStandardName.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GsaStandardName.

        Parameters
        ----------
        guid: str
            The guid of this GsaStandardName.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        # Field is required
        if guid is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'guid', must not be 'Unset'")
        self._guid = guid

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
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
        if not isinstance(other, GsaStandardName):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
