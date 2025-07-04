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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaTranslateGuidsToIdentitiesResponse(ModelBase):
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
        "database_key": "str",
        "attributes": "list[GsaSlimIdentifiedEntity]",
        "constants": "list[GsaSlimIdentifiedEntity]",
        "data": "list[GsaSlimIdentifiedEntity]",
        "discrete_types": "list[GsaSlimIdentifiedEntity]",
        "discrete_values": "list[GsaSlimIdentifiedEntity]",
        "layouts": "list[GsaSlimIdentifiedEntity]",
        "parameters": "list[GsaSlimIdentifiedEntity]",
        "record_histories": "list[GsaSlimIdentifiedEntity]",
        "record_link_groups": "list[GsaSlimIdentifiedEntity]",
        "record_versions": "list[GsaSlimIdentifiedEntity]",
        "replacement_strings": "list[GsaSlimIdentifiedEntity]",
        "standard_names": "list[GsaSlimIdentifiedEntity]",
        "subsets": "list[GsaSlimIdentifiedEntity]",
        "tables": "list[GsaSlimIdentifiedEntity]",
        "unit_systems": "list[GsaSlimIdentifiedEntity]",
        "units": "list[GsaSlimIdentifiedEntity]",
    }

    attribute_map: dict[str, str] = {
        "database_key": "databaseKey",
        "attributes": "attributes",
        "constants": "constants",
        "data": "data",
        "discrete_types": "discreteTypes",
        "discrete_values": "discreteValues",
        "layouts": "layouts",
        "parameters": "parameters",
        "record_histories": "recordHistories",
        "record_link_groups": "recordLinkGroups",
        "record_versions": "recordVersions",
        "replacement_strings": "replacementStrings",
        "standard_names": "standardNames",
        "subsets": "subsets",
        "tables": "tables",
        "unit_systems": "unitSystems",
        "units": "units",
    }

    subtype_mapping: dict[str, str] = {
        "attributes": "GsaSlimIdentifiedEntity",
        "layouts": "GsaSlimIdentifiedEntity",
        "recordVersions": "GsaSlimIdentifiedEntity",
        "recordHistories": "GsaSlimIdentifiedEntity",
        "units": "GsaSlimIdentifiedEntity",
        "unitSystems": "GsaSlimIdentifiedEntity",
        "parameters": "GsaSlimIdentifiedEntity",
        "subsets": "GsaSlimIdentifiedEntity",
        "tables": "GsaSlimIdentifiedEntity",
        "discreteTypes": "GsaSlimIdentifiedEntity",
        "discreteValues": "GsaSlimIdentifiedEntity",
        "replacementStrings": "GsaSlimIdentifiedEntity",
        "standardNames": "GsaSlimIdentifiedEntity",
        "constants": "GsaSlimIdentifiedEntity",
        "recordLinkGroups": "GsaSlimIdentifiedEntity",
        "data": "GsaSlimIdentifiedEntity",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        database_key: "str",
        attributes: "list[GsaSlimIdentifiedEntity] | None | Unset_Type" = Unset,
        constants: "list[GsaSlimIdentifiedEntity] | None | Unset_Type" = Unset,
        data: "list[GsaSlimIdentifiedEntity] | None | Unset_Type" = Unset,
        discrete_types: "list[GsaSlimIdentifiedEntity] | None | Unset_Type" = Unset,
        discrete_values: "list[GsaSlimIdentifiedEntity] | None | Unset_Type" = Unset,
        layouts: "list[GsaSlimIdentifiedEntity] | None | Unset_Type" = Unset,
        parameters: "list[GsaSlimIdentifiedEntity] | None | Unset_Type" = Unset,
        record_histories: "list[GsaSlimIdentifiedEntity] | None | Unset_Type" = Unset,
        record_link_groups: "list[GsaSlimIdentifiedEntity] | None | Unset_Type" = Unset,
        record_versions: "list[GsaSlimIdentifiedEntity] | None | Unset_Type" = Unset,
        replacement_strings: "list[GsaSlimIdentifiedEntity] | None | Unset_Type" = Unset,
        standard_names: "list[GsaSlimIdentifiedEntity] | None | Unset_Type" = Unset,
        subsets: "list[GsaSlimIdentifiedEntity] | None | Unset_Type" = Unset,
        tables: "list[GsaSlimIdentifiedEntity] | None | Unset_Type" = Unset,
        unit_systems: "list[GsaSlimIdentifiedEntity] | None | Unset_Type" = Unset,
        units: "list[GsaSlimIdentifiedEntity] | None | Unset_Type" = Unset,
    ) -> None:
        """GsaTranslateGuidsToIdentitiesResponse - a model defined in Swagger

        Parameters
        ----------
        database_key: str
        attributes: list[GsaSlimIdentifiedEntity] | None, optional
        constants: list[GsaSlimIdentifiedEntity] | None, optional
        data: list[GsaSlimIdentifiedEntity] | None, optional
        discrete_types: list[GsaSlimIdentifiedEntity] | None, optional
        discrete_values: list[GsaSlimIdentifiedEntity] | None, optional
        layouts: list[GsaSlimIdentifiedEntity] | None, optional
        parameters: list[GsaSlimIdentifiedEntity] | None, optional
        record_histories: list[GsaSlimIdentifiedEntity] | None, optional
        record_link_groups: list[GsaSlimIdentifiedEntity] | None, optional
        record_versions: list[GsaSlimIdentifiedEntity] | None, optional
        replacement_strings: list[GsaSlimIdentifiedEntity] | None, optional
        standard_names: list[GsaSlimIdentifiedEntity] | None, optional
        subsets: list[GsaSlimIdentifiedEntity] | None, optional
        tables: list[GsaSlimIdentifiedEntity] | None, optional
        unit_systems: list[GsaSlimIdentifiedEntity] | None, optional
        units: list[GsaSlimIdentifiedEntity] | None, optional
        """
        self._database_key: str
        self._attributes: list[GsaSlimIdentifiedEntity] | None | Unset_Type = Unset
        self._layouts: list[GsaSlimIdentifiedEntity] | None | Unset_Type = Unset
        self._record_versions: list[GsaSlimIdentifiedEntity] | None | Unset_Type = Unset
        self._record_histories: list[GsaSlimIdentifiedEntity] | None | Unset_Type = Unset
        self._units: list[GsaSlimIdentifiedEntity] | None | Unset_Type = Unset
        self._unit_systems: list[GsaSlimIdentifiedEntity] | None | Unset_Type = Unset
        self._parameters: list[GsaSlimIdentifiedEntity] | None | Unset_Type = Unset
        self._subsets: list[GsaSlimIdentifiedEntity] | None | Unset_Type = Unset
        self._tables: list[GsaSlimIdentifiedEntity] | None | Unset_Type = Unset
        self._discrete_types: list[GsaSlimIdentifiedEntity] | None | Unset_Type = Unset
        self._discrete_values: list[GsaSlimIdentifiedEntity] | None | Unset_Type = Unset
        self._replacement_strings: list[GsaSlimIdentifiedEntity] | None | Unset_Type = Unset
        self._standard_names: list[GsaSlimIdentifiedEntity] | None | Unset_Type = Unset
        self._constants: list[GsaSlimIdentifiedEntity] | None | Unset_Type = Unset
        self._record_link_groups: list[GsaSlimIdentifiedEntity] | None | Unset_Type = Unset
        self._data: list[GsaSlimIdentifiedEntity] | None | Unset_Type = Unset

        self.database_key = database_key
        if attributes is not Unset:
            self.attributes = attributes
        if layouts is not Unset:
            self.layouts = layouts
        if record_versions is not Unset:
            self.record_versions = record_versions
        if record_histories is not Unset:
            self.record_histories = record_histories
        if units is not Unset:
            self.units = units
        if unit_systems is not Unset:
            self.unit_systems = unit_systems
        if parameters is not Unset:
            self.parameters = parameters
        if subsets is not Unset:
            self.subsets = subsets
        if tables is not Unset:
            self.tables = tables
        if discrete_types is not Unset:
            self.discrete_types = discrete_types
        if discrete_values is not Unset:
            self.discrete_values = discrete_values
        if replacement_strings is not Unset:
            self.replacement_strings = replacement_strings
        if standard_names is not Unset:
            self.standard_names = standard_names
        if constants is not Unset:
            self.constants = constants
        if record_link_groups is not Unset:
            self.record_link_groups = record_link_groups
        if data is not Unset:
            self.data = data

    @property
    def database_key(self) -> "str":
        """Gets the database_key of this GsaTranslateGuidsToIdentitiesResponse.

        Returns
        -------
        str
            The database_key of this GsaTranslateGuidsToIdentitiesResponse.
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key: "str") -> None:
        """Sets the database_key of this GsaTranslateGuidsToIdentitiesResponse.

        Parameters
        ----------
        database_key: str
            The database_key of this GsaTranslateGuidsToIdentitiesResponse.
        """
        # Field is not nullable
        if database_key is None:
            raise ValueError("Invalid value for 'database_key', must not be 'None'")
        # Field is required
        if database_key is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'database_key', must not be 'Unset'")
        self._database_key = database_key

    @property
    def attributes(self) -> "list[GsaSlimIdentifiedEntity] | None | Unset_Type":
        """Gets the attributes of this GsaTranslateGuidsToIdentitiesResponse.

        Returns
        -------
        list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The attributes of this GsaTranslateGuidsToIdentitiesResponse.
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes: "list[GsaSlimIdentifiedEntity] | None | Unset_Type") -> None:
        """Sets the attributes of this GsaTranslateGuidsToIdentitiesResponse.

        Parameters
        ----------
        attributes: list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The attributes of this GsaTranslateGuidsToIdentitiesResponse.
        """
        self._attributes = attributes

    @property
    def layouts(self) -> "list[GsaSlimIdentifiedEntity] | None | Unset_Type":
        """Gets the layouts of this GsaTranslateGuidsToIdentitiesResponse.

        Returns
        -------
        list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The layouts of this GsaTranslateGuidsToIdentitiesResponse.
        """
        return self._layouts

    @layouts.setter
    def layouts(self, layouts: "list[GsaSlimIdentifiedEntity] | None | Unset_Type") -> None:
        """Sets the layouts of this GsaTranslateGuidsToIdentitiesResponse.

        Parameters
        ----------
        layouts: list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The layouts of this GsaTranslateGuidsToIdentitiesResponse.
        """
        self._layouts = layouts

    @property
    def record_versions(self) -> "list[GsaSlimIdentifiedEntity] | None | Unset_Type":
        """Gets the record_versions of this GsaTranslateGuidsToIdentitiesResponse.

        Returns
        -------
        list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The record_versions of this GsaTranslateGuidsToIdentitiesResponse.
        """
        return self._record_versions

    @record_versions.setter
    def record_versions(
        self, record_versions: "list[GsaSlimIdentifiedEntity] | None | Unset_Type"
    ) -> None:
        """Sets the record_versions of this GsaTranslateGuidsToIdentitiesResponse.

        Parameters
        ----------
        record_versions: list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The record_versions of this GsaTranslateGuidsToIdentitiesResponse.
        """
        self._record_versions = record_versions

    @property
    def record_histories(self) -> "list[GsaSlimIdentifiedEntity] | None | Unset_Type":
        """Gets the record_histories of this GsaTranslateGuidsToIdentitiesResponse.

        Returns
        -------
        list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The record_histories of this GsaTranslateGuidsToIdentitiesResponse.
        """
        return self._record_histories

    @record_histories.setter
    def record_histories(
        self, record_histories: "list[GsaSlimIdentifiedEntity] | None | Unset_Type"
    ) -> None:
        """Sets the record_histories of this GsaTranslateGuidsToIdentitiesResponse.

        Parameters
        ----------
        record_histories: list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The record_histories of this GsaTranslateGuidsToIdentitiesResponse.
        """
        self._record_histories = record_histories

    @property
    def units(self) -> "list[GsaSlimIdentifiedEntity] | None | Unset_Type":
        """Gets the units of this GsaTranslateGuidsToIdentitiesResponse.

        Returns
        -------
        list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The units of this GsaTranslateGuidsToIdentitiesResponse.
        """
        return self._units

    @units.setter
    def units(self, units: "list[GsaSlimIdentifiedEntity] | None | Unset_Type") -> None:
        """Sets the units of this GsaTranslateGuidsToIdentitiesResponse.

        Parameters
        ----------
        units: list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The units of this GsaTranslateGuidsToIdentitiesResponse.
        """
        self._units = units

    @property
    def unit_systems(self) -> "list[GsaSlimIdentifiedEntity] | None | Unset_Type":
        """Gets the unit_systems of this GsaTranslateGuidsToIdentitiesResponse.

        Returns
        -------
        list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The unit_systems of this GsaTranslateGuidsToIdentitiesResponse.
        """
        return self._unit_systems

    @unit_systems.setter
    def unit_systems(
        self, unit_systems: "list[GsaSlimIdentifiedEntity] | None | Unset_Type"
    ) -> None:
        """Sets the unit_systems of this GsaTranslateGuidsToIdentitiesResponse.

        Parameters
        ----------
        unit_systems: list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The unit_systems of this GsaTranslateGuidsToIdentitiesResponse.
        """
        self._unit_systems = unit_systems

    @property
    def parameters(self) -> "list[GsaSlimIdentifiedEntity] | None | Unset_Type":
        """Gets the parameters of this GsaTranslateGuidsToIdentitiesResponse.

        Returns
        -------
        list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The parameters of this GsaTranslateGuidsToIdentitiesResponse.
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters: "list[GsaSlimIdentifiedEntity] | None | Unset_Type") -> None:
        """Sets the parameters of this GsaTranslateGuidsToIdentitiesResponse.

        Parameters
        ----------
        parameters: list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The parameters of this GsaTranslateGuidsToIdentitiesResponse.
        """
        self._parameters = parameters

    @property
    def subsets(self) -> "list[GsaSlimIdentifiedEntity] | None | Unset_Type":
        """Gets the subsets of this GsaTranslateGuidsToIdentitiesResponse.

        Returns
        -------
        list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The subsets of this GsaTranslateGuidsToIdentitiesResponse.
        """
        return self._subsets

    @subsets.setter
    def subsets(self, subsets: "list[GsaSlimIdentifiedEntity] | None | Unset_Type") -> None:
        """Sets the subsets of this GsaTranslateGuidsToIdentitiesResponse.

        Parameters
        ----------
        subsets: list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The subsets of this GsaTranslateGuidsToIdentitiesResponse.
        """
        self._subsets = subsets

    @property
    def tables(self) -> "list[GsaSlimIdentifiedEntity] | None | Unset_Type":
        """Gets the tables of this GsaTranslateGuidsToIdentitiesResponse.

        Returns
        -------
        list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The tables of this GsaTranslateGuidsToIdentitiesResponse.
        """
        return self._tables

    @tables.setter
    def tables(self, tables: "list[GsaSlimIdentifiedEntity] | None | Unset_Type") -> None:
        """Sets the tables of this GsaTranslateGuidsToIdentitiesResponse.

        Parameters
        ----------
        tables: list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The tables of this GsaTranslateGuidsToIdentitiesResponse.
        """
        self._tables = tables

    @property
    def discrete_types(self) -> "list[GsaSlimIdentifiedEntity] | None | Unset_Type":
        """Gets the discrete_types of this GsaTranslateGuidsToIdentitiesResponse.

        Returns
        -------
        list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The discrete_types of this GsaTranslateGuidsToIdentitiesResponse.
        """
        return self._discrete_types

    @discrete_types.setter
    def discrete_types(
        self, discrete_types: "list[GsaSlimIdentifiedEntity] | None | Unset_Type"
    ) -> None:
        """Sets the discrete_types of this GsaTranslateGuidsToIdentitiesResponse.

        Parameters
        ----------
        discrete_types: list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The discrete_types of this GsaTranslateGuidsToIdentitiesResponse.
        """
        self._discrete_types = discrete_types

    @property
    def discrete_values(self) -> "list[GsaSlimIdentifiedEntity] | None | Unset_Type":
        """Gets the discrete_values of this GsaTranslateGuidsToIdentitiesResponse.

        Returns
        -------
        list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The discrete_values of this GsaTranslateGuidsToIdentitiesResponse.
        """
        return self._discrete_values

    @discrete_values.setter
    def discrete_values(
        self, discrete_values: "list[GsaSlimIdentifiedEntity] | None | Unset_Type"
    ) -> None:
        """Sets the discrete_values of this GsaTranslateGuidsToIdentitiesResponse.

        Parameters
        ----------
        discrete_values: list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The discrete_values of this GsaTranslateGuidsToIdentitiesResponse.
        """
        self._discrete_values = discrete_values

    @property
    def replacement_strings(self) -> "list[GsaSlimIdentifiedEntity] | None | Unset_Type":
        """Gets the replacement_strings of this GsaTranslateGuidsToIdentitiesResponse.

        Returns
        -------
        list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The replacement_strings of this GsaTranslateGuidsToIdentitiesResponse.
        """
        return self._replacement_strings

    @replacement_strings.setter
    def replacement_strings(
        self, replacement_strings: "list[GsaSlimIdentifiedEntity] | None | Unset_Type"
    ) -> None:
        """Sets the replacement_strings of this GsaTranslateGuidsToIdentitiesResponse.

        Parameters
        ----------
        replacement_strings: list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The replacement_strings of this GsaTranslateGuidsToIdentitiesResponse.
        """
        self._replacement_strings = replacement_strings

    @property
    def standard_names(self) -> "list[GsaSlimIdentifiedEntity] | None | Unset_Type":
        """Gets the standard_names of this GsaTranslateGuidsToIdentitiesResponse.

        Returns
        -------
        list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The standard_names of this GsaTranslateGuidsToIdentitiesResponse.
        """
        return self._standard_names

    @standard_names.setter
    def standard_names(
        self, standard_names: "list[GsaSlimIdentifiedEntity] | None | Unset_Type"
    ) -> None:
        """Sets the standard_names of this GsaTranslateGuidsToIdentitiesResponse.

        Parameters
        ----------
        standard_names: list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The standard_names of this GsaTranslateGuidsToIdentitiesResponse.
        """
        self._standard_names = standard_names

    @property
    def constants(self) -> "list[GsaSlimIdentifiedEntity] | None | Unset_Type":
        """Gets the constants of this GsaTranslateGuidsToIdentitiesResponse.

        Returns
        -------
        list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The constants of this GsaTranslateGuidsToIdentitiesResponse.
        """
        return self._constants

    @constants.setter
    def constants(self, constants: "list[GsaSlimIdentifiedEntity] | None | Unset_Type") -> None:
        """Sets the constants of this GsaTranslateGuidsToIdentitiesResponse.

        Parameters
        ----------
        constants: list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The constants of this GsaTranslateGuidsToIdentitiesResponse.
        """
        self._constants = constants

    @property
    def record_link_groups(self) -> "list[GsaSlimIdentifiedEntity] | None | Unset_Type":
        """Gets the record_link_groups of this GsaTranslateGuidsToIdentitiesResponse.

        Returns
        -------
        list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The record_link_groups of this GsaTranslateGuidsToIdentitiesResponse.
        """
        return self._record_link_groups

    @record_link_groups.setter
    def record_link_groups(
        self, record_link_groups: "list[GsaSlimIdentifiedEntity] | None | Unset_Type"
    ) -> None:
        """Sets the record_link_groups of this GsaTranslateGuidsToIdentitiesResponse.

        Parameters
        ----------
        record_link_groups: list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The record_link_groups of this GsaTranslateGuidsToIdentitiesResponse.
        """
        self._record_link_groups = record_link_groups

    @property
    def data(self) -> "list[GsaSlimIdentifiedEntity] | None | Unset_Type":
        """Gets the data of this GsaTranslateGuidsToIdentitiesResponse.

        Returns
        -------
        list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The data of this GsaTranslateGuidsToIdentitiesResponse.
        """
        return self._data

    @data.setter
    def data(self, data: "list[GsaSlimIdentifiedEntity] | None | Unset_Type") -> None:
        """Sets the data of this GsaTranslateGuidsToIdentitiesResponse.

        Parameters
        ----------
        data: list[GsaSlimIdentifiedEntity] | None | Unset_Type
            The data of this GsaTranslateGuidsToIdentitiesResponse.
        """
        self._data = data

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
        if not isinstance(other, GsaTranslateGuidsToIdentitiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
