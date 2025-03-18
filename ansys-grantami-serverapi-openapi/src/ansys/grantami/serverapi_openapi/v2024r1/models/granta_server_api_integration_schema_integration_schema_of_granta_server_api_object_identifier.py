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


class GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier(ModelBase):
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
        "attributes": "list[GrantaServerApiIntegrationSchemaAttribute]",
        "discrete_types": "list[GrantaServerApiIntegrationSchemaDiscreteType]",
        "key": "str",
        "layouts": "list[GrantaServerApiIntegrationSchemaLayout]",
        "security_groups": "GrantaServerApiIntegrationSchemaSecurityGroups",
        "sources": "list[GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier]",
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
        "attributes": "GrantaServerApiIntegrationSchemaAttribute",
        "layouts": "GrantaServerApiIntegrationSchemaLayout",
        "discreteTypes": "GrantaServerApiIntegrationSchemaDiscreteType",
        "sources": "GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier",
        "securityGroups": "GrantaServerApiIntegrationSchemaSecurityGroups",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        access_control_category_values: "Union[dict[str, list[str]], None, Unset_Type]" = Unset,
        attributes: "Union[list[GrantaServerApiIntegrationSchemaAttribute], None, Unset_Type]" = Unset,
        discrete_types: "Union[list[GrantaServerApiIntegrationSchemaDiscreteType], None, Unset_Type]" = Unset,
        key: "Union[str, None, Unset_Type]" = Unset,
        layouts: "Union[list[GrantaServerApiIntegrationSchemaLayout], None, Unset_Type]" = Unset,
        security_groups: "Union[GrantaServerApiIntegrationSchemaSecurityGroups, Unset_Type]" = Unset,
        sources: "Union[list[GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier], None, Unset_Type]" = Unset,
        unit_system: "Union[str, None, Unset_Type]" = Unset,
        version: "Union[int, None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier - a model defined in Swagger

        Parameters
        ----------
        access_control_category_values: dict[str, list[str]], optional
        attributes: list[GrantaServerApiIntegrationSchemaAttribute], optional
        discrete_types: list[GrantaServerApiIntegrationSchemaDiscreteType], optional
        key: str, optional
        layouts: list[GrantaServerApiIntegrationSchemaLayout], optional
        security_groups: GrantaServerApiIntegrationSchemaSecurityGroups, optional
        sources: list[GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier], optional
        unit_system: str, optional
        version: int, optional
        """
        self._key: Union[str, None, Unset_Type] = Unset
        self._version: Union[int, None, Unset_Type] = Unset
        self._attributes: Union[
            list[GrantaServerApiIntegrationSchemaAttribute], None, Unset_Type
        ] = Unset
        self._layouts: Union[list[GrantaServerApiIntegrationSchemaLayout], None, Unset_Type] = Unset
        self._unit_system: Union[str, None, Unset_Type] = Unset
        self._discrete_types: Union[
            list[GrantaServerApiIntegrationSchemaDiscreteType], None, Unset_Type
        ] = Unset
        self._sources: Union[
            list[GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier],
            None,
            Unset_Type,
        ] = Unset
        self._access_control_category_values: Union[dict[str, list[str]], None, Unset_Type] = Unset
        self._security_groups: Union[GrantaServerApiIntegrationSchemaSecurityGroups, Unset_Type] = (
            Unset
        )

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
        """Gets the key of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        Union[str, None, Unset_Type]
            The key of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        return self._key

    @key.setter
    def key(self, key: "Union[str, None, Unset_Type]") -> None:
        """Sets the key of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        key: Union[str, None, Unset_Type]
            The key of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        self._key = key

    @property
    def version(self) -> "Union[int, None, Unset_Type]":
        """Gets the version of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        Union[int, None, Unset_Type]
            The version of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        return self._version

    @version.setter
    def version(self, version: "Union[int, None, Unset_Type]") -> None:
        """Sets the version of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        version: Union[int, None, Unset_Type]
            The version of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        self._version = version

    @property
    def attributes(
        self,
    ) -> "Union[list[GrantaServerApiIntegrationSchemaAttribute], None, Unset_Type]":
        """Gets the attributes of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        Union[list[GrantaServerApiIntegrationSchemaAttribute], None, Unset_Type]
            The attributes of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        return self._attributes

    @attributes.setter
    def attributes(
        self, attributes: "Union[list[GrantaServerApiIntegrationSchemaAttribute], None, Unset_Type]"
    ) -> None:
        """Sets the attributes of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        attributes: Union[list[GrantaServerApiIntegrationSchemaAttribute], None, Unset_Type]
            The attributes of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        self._attributes = attributes

    @property
    def layouts(self) -> "Union[list[GrantaServerApiIntegrationSchemaLayout], None, Unset_Type]":
        """Gets the layouts of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        Union[list[GrantaServerApiIntegrationSchemaLayout], None, Unset_Type]
            The layouts of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        return self._layouts

    @layouts.setter
    def layouts(
        self, layouts: "Union[list[GrantaServerApiIntegrationSchemaLayout], None, Unset_Type]"
    ) -> None:
        """Sets the layouts of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        layouts: Union[list[GrantaServerApiIntegrationSchemaLayout], None, Unset_Type]
            The layouts of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        self._layouts = layouts

    @property
    def unit_system(self) -> "Union[str, None, Unset_Type]":
        """Gets the unit_system of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        Union[str, None, Unset_Type]
            The unit_system of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        return self._unit_system

    @unit_system.setter
    def unit_system(self, unit_system: "Union[str, None, Unset_Type]") -> None:
        """Sets the unit_system of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        unit_system: Union[str, None, Unset_Type]
            The unit_system of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        self._unit_system = unit_system

    @property
    def discrete_types(
        self,
    ) -> "Union[list[GrantaServerApiIntegrationSchemaDiscreteType], None, Unset_Type]":
        """Gets the discrete_types of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        Union[list[GrantaServerApiIntegrationSchemaDiscreteType], None, Unset_Type]
            The discrete_types of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        return self._discrete_types

    @discrete_types.setter
    def discrete_types(
        self,
        discrete_types: "Union[list[GrantaServerApiIntegrationSchemaDiscreteType], None, Unset_Type]",
    ) -> None:
        """Sets the discrete_types of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        discrete_types: Union[list[GrantaServerApiIntegrationSchemaDiscreteType], None, Unset_Type]
            The discrete_types of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        self._discrete_types = discrete_types

    @property
    def sources(
        self,
    ) -> "Union[list[GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier], None, Unset_Type]":
        """Gets the sources of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        Union[list[GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier], None, Unset_Type]
            The sources of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        return self._sources

    @sources.setter
    def sources(
        self,
        sources: "Union[list[GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier], None, Unset_Type]",
    ) -> None:
        """Sets the sources of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        sources: Union[list[GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier], None, Unset_Type]
            The sources of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        self._sources = sources

    @property
    def access_control_category_values(self) -> "Union[dict[str, list[str]], None, Unset_Type]":
        """Gets the access_control_category_values of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        Union[dict[str, list[str]], None, Unset_Type]
            The access_control_category_values of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        return self._access_control_category_values

    @access_control_category_values.setter
    def access_control_category_values(
        self, access_control_category_values: "Union[dict[str, list[str]], None, Unset_Type]"
    ) -> None:
        """Sets the access_control_category_values of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        access_control_category_values: Union[dict[str, list[str]], None, Unset_Type]
            The access_control_category_values of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        self._access_control_category_values = access_control_category_values

    @property
    def security_groups(
        self,
    ) -> "Union[GrantaServerApiIntegrationSchemaSecurityGroups, Unset_Type]":
        """Gets the security_groups of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        Union[GrantaServerApiIntegrationSchemaSecurityGroups, Unset_Type]
            The security_groups of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(
        self, security_groups: "Union[GrantaServerApiIntegrationSchemaSecurityGroups, Unset_Type]"
    ) -> None:
        """Sets the security_groups of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        security_groups: Union[GrantaServerApiIntegrationSchemaSecurityGroups, Unset_Type]
            The security_groups of this GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier.
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
        if not isinstance(
            other,
            GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
