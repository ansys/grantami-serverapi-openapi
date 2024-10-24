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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaIntegrationSchemaOfObjectIdentifier(ModelBase):
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
        "access_control_category_values": "dict(str, list[str])",
        "attributes": "list[GsaIntegrationAttribute]",
        "discrete_types": "list[GsaIntegrationDiscreteType]",
        "key": "str",
        "layouts": "list[GsaIntegrationLayout]",
        "security_groups": "GsaSecurityGroups",
        "sources": "list[GsaSourceOfObjectIdentifier]",
        "unit_system": "str",
        "version": "int",
    }

    attribute_map: dict[str, str] = {
        "access_control_category_values": "accessControlCategoryValues",
        "attributes": "attributes",
        "discrete_types": "discreteTypes",
        "key": "key",
        "layouts": "layouts",
        "security_groups": "securityGroups",
        "sources": "sources",
        "unit_system": "unitSystem",
        "version": "version",
    }

    subtype_mapping: dict[str, str] = {
        "attributes": "GsaIntegrationAttribute",
        "layouts": "GsaIntegrationLayout",
        "discreteTypes": "GsaIntegrationDiscreteType",
        "sources": "GsaSourceOfObjectIdentifier",
        "securityGroups": "GsaSecurityGroups",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        access_control_category_values: "Union[Dict[str, list[str]], None, Unset_Type]" = Unset,
        attributes: "Union[list[GsaIntegrationAttribute], None, Unset_Type]" = Unset,
        discrete_types: "Union[list[GsaIntegrationDiscreteType], None, Unset_Type]" = Unset,
        key: "Union[str, None, Unset_Type]" = Unset,
        layouts: "Union[list[GsaIntegrationLayout], None, Unset_Type]" = Unset,
        security_groups: "Union[GsaSecurityGroups, Unset_Type]" = Unset,
        sources: "Union[list[GsaSourceOfObjectIdentifier], None, Unset_Type]" = Unset,
        unit_system: "Union[str, None, Unset_Type]" = Unset,
        version: "Union[int, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaIntegrationSchemaOfObjectIdentifier - a model defined in Swagger

        Parameters
        ----------
        access_control_category_values: Dict[str, list[str]], optional
        attributes: list[GsaIntegrationAttribute], optional
        discrete_types: list[GsaIntegrationDiscreteType], optional
        key: str, optional
        layouts: list[GsaIntegrationLayout], optional
        security_groups: GsaSecurityGroups, optional
        sources: list[GsaSourceOfObjectIdentifier], optional
        unit_system: str, optional
        version: int, optional
        """
        self._key: Union[str, None, Unset_Type] = Unset
        self._version: Union[int, None, Unset_Type] = Unset
        self._attributes: Union[list[GsaIntegrationAttribute], None, Unset_Type] = Unset
        self._layouts: Union[list[GsaIntegrationLayout], None, Unset_Type] = Unset
        self._unit_system: Union[str, None, Unset_Type] = Unset
        self._discrete_types: Union[list[GsaIntegrationDiscreteType], None, Unset_Type] = Unset
        self._sources: Union[list[GsaSourceOfObjectIdentifier], None, Unset_Type] = Unset
        self._access_control_category_values: Union[Dict[str, list[str]], None, Unset_Type] = Unset
        self._security_groups: Union[GsaSecurityGroups, Unset_Type] = Unset

        if key is not Unset:
            self.key = key
        if version is not Unset:
            self.version = version
        if attributes is not Unset:
            self.attributes = attributes
        if layouts is not Unset:
            self.layouts = layouts
        if unit_system is not Unset:
            self.unit_system = unit_system
        if discrete_types is not Unset:
            self.discrete_types = discrete_types
        if sources is not Unset:
            self.sources = sources
        if access_control_category_values is not Unset:
            self.access_control_category_values = access_control_category_values
        if security_groups is not Unset:
            self.security_groups = security_groups

    @property
    def key(self) -> "Union[str, None, Unset_Type]":
        """Gets the key of this GsaIntegrationSchemaOfObjectIdentifier.

        Returns
        -------
        Union[str, None, Unset_Type]
            The key of this GsaIntegrationSchemaOfObjectIdentifier.
        """
        return self._key

    @key.setter
    def key(self, key: "Union[str, None, Unset_Type]") -> None:
        """Sets the key of this GsaIntegrationSchemaOfObjectIdentifier.

        Parameters
        ----------
        key: Union[str, None, Unset_Type]
            The key of this GsaIntegrationSchemaOfObjectIdentifier.
        """
        self._key = key

    @property
    def version(self) -> "Union[int, None, Unset_Type]":
        """Gets the version of this GsaIntegrationSchemaOfObjectIdentifier.

        Returns
        -------
        Union[int, None, Unset_Type]
            The version of this GsaIntegrationSchemaOfObjectIdentifier.
        """
        return self._version

    @version.setter
    def version(self, version: "Union[int, None, Unset_Type]") -> None:
        """Sets the version of this GsaIntegrationSchemaOfObjectIdentifier.

        Parameters
        ----------
        version: Union[int, None, Unset_Type]
            The version of this GsaIntegrationSchemaOfObjectIdentifier.
        """
        self._version = version

    @property
    def attributes(self) -> "Union[list[GsaIntegrationAttribute], None, Unset_Type]":
        """Gets the attributes of this GsaIntegrationSchemaOfObjectIdentifier.

        Returns
        -------
        Union[list[GsaIntegrationAttribute], None, Unset_Type]
            The attributes of this GsaIntegrationSchemaOfObjectIdentifier.
        """
        return self._attributes

    @attributes.setter
    def attributes(
        self, attributes: "Union[list[GsaIntegrationAttribute], None, Unset_Type]"
    ) -> None:
        """Sets the attributes of this GsaIntegrationSchemaOfObjectIdentifier.

        Parameters
        ----------
        attributes: Union[list[GsaIntegrationAttribute], None, Unset_Type]
            The attributes of this GsaIntegrationSchemaOfObjectIdentifier.
        """
        self._attributes = attributes

    @property
    def layouts(self) -> "Union[list[GsaIntegrationLayout], None, Unset_Type]":
        """Gets the layouts of this GsaIntegrationSchemaOfObjectIdentifier.

        Returns
        -------
        Union[list[GsaIntegrationLayout], None, Unset_Type]
            The layouts of this GsaIntegrationSchemaOfObjectIdentifier.
        """
        return self._layouts

    @layouts.setter
    def layouts(self, layouts: "Union[list[GsaIntegrationLayout], None, Unset_Type]") -> None:
        """Sets the layouts of this GsaIntegrationSchemaOfObjectIdentifier.

        Parameters
        ----------
        layouts: Union[list[GsaIntegrationLayout], None, Unset_Type]
            The layouts of this GsaIntegrationSchemaOfObjectIdentifier.
        """
        self._layouts = layouts

    @property
    def unit_system(self) -> "Union[str, None, Unset_Type]":
        """Gets the unit_system of this GsaIntegrationSchemaOfObjectIdentifier.

        Returns
        -------
        Union[str, None, Unset_Type]
            The unit_system of this GsaIntegrationSchemaOfObjectIdentifier.
        """
        return self._unit_system

    @unit_system.setter
    def unit_system(self, unit_system: "Union[str, None, Unset_Type]") -> None:
        """Sets the unit_system of this GsaIntegrationSchemaOfObjectIdentifier.

        Parameters
        ----------
        unit_system: Union[str, None, Unset_Type]
            The unit_system of this GsaIntegrationSchemaOfObjectIdentifier.
        """
        self._unit_system = unit_system

    @property
    def discrete_types(self) -> "Union[list[GsaIntegrationDiscreteType], None, Unset_Type]":
        """Gets the discrete_types of this GsaIntegrationSchemaOfObjectIdentifier.

        Returns
        -------
        Union[list[GsaIntegrationDiscreteType], None, Unset_Type]
            The discrete_types of this GsaIntegrationSchemaOfObjectIdentifier.
        """
        return self._discrete_types

    @discrete_types.setter
    def discrete_types(
        self, discrete_types: "Union[list[GsaIntegrationDiscreteType], None, Unset_Type]"
    ) -> None:
        """Sets the discrete_types of this GsaIntegrationSchemaOfObjectIdentifier.

        Parameters
        ----------
        discrete_types: Union[list[GsaIntegrationDiscreteType], None, Unset_Type]
            The discrete_types of this GsaIntegrationSchemaOfObjectIdentifier.
        """
        self._discrete_types = discrete_types

    @property
    def sources(self) -> "Union[list[GsaSourceOfObjectIdentifier], None, Unset_Type]":
        """Gets the sources of this GsaIntegrationSchemaOfObjectIdentifier.

        Returns
        -------
        Union[list[GsaSourceOfObjectIdentifier], None, Unset_Type]
            The sources of this GsaIntegrationSchemaOfObjectIdentifier.
        """
        return self._sources

    @sources.setter
    def sources(
        self, sources: "Union[list[GsaSourceOfObjectIdentifier], None, Unset_Type]"
    ) -> None:
        """Sets the sources of this GsaIntegrationSchemaOfObjectIdentifier.

        Parameters
        ----------
        sources: Union[list[GsaSourceOfObjectIdentifier], None, Unset_Type]
            The sources of this GsaIntegrationSchemaOfObjectIdentifier.
        """
        self._sources = sources

    @property
    def access_control_category_values(self) -> "Union[Dict[str, list[str]], None, Unset_Type]":
        """Gets the access_control_category_values of this GsaIntegrationSchemaOfObjectIdentifier.

        Returns
        -------
        Union[Dict[str, list[str]], None, Unset_Type]
            The access_control_category_values of this GsaIntegrationSchemaOfObjectIdentifier.
        """
        return self._access_control_category_values

    @access_control_category_values.setter
    def access_control_category_values(
        self, access_control_category_values: "Union[Dict[str, list[str]], None, Unset_Type]"
    ) -> None:
        """Sets the access_control_category_values of this GsaIntegrationSchemaOfObjectIdentifier.

        Parameters
        ----------
        access_control_category_values: Union[Dict[str, list[str]], None, Unset_Type]
            The access_control_category_values of this GsaIntegrationSchemaOfObjectIdentifier.
        """
        self._access_control_category_values = access_control_category_values

    @property
    def security_groups(self) -> "Union[GsaSecurityGroups, Unset_Type]":
        """Gets the security_groups of this GsaIntegrationSchemaOfObjectIdentifier.

        Returns
        -------
        Union[GsaSecurityGroups, Unset_Type]
            The security_groups of this GsaIntegrationSchemaOfObjectIdentifier.
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups: "Union[GsaSecurityGroups, Unset_Type]") -> None:
        """Sets the security_groups of this GsaIntegrationSchemaOfObjectIdentifier.

        Parameters
        ----------
        security_groups: Union[GsaSecurityGroups, Unset_Type]
            The security_groups of this GsaIntegrationSchemaOfObjectIdentifier.
        """
        # Field is not nullable
        if security_groups is None:
            raise ValueError("Invalid value for 'security_groups', must not be 'None'")
        self._security_groups = security_groups

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
        if not isinstance(other, GsaIntegrationSchemaOfObjectIdentifier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
