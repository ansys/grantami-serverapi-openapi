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

from ansys.grantami.serverapi_openapi.2024r2.models.granta_server_api_search_criterion import (  # noqa: F401
    GrantaServerApiSearchCriterion,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiSearchFreeTextCriterion(GrantaServerApiSearchCriterion):
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
        "attribute_guids_to_boost": "list[GrantaServerApiSearchBoostByGuid]",
        "attribute_identities_to_boost": "list[GrantaServerApiSearchBoostByIdentity]",
        "attributes": "GrantaServerApiValueSpecifier",
        "column_guids_to_boost": "list[GrantaServerApiSearchBoostByGuid]",
        "column_identities_to_boost": "list[GrantaServerApiSearchBoostByIdentity]",
        "local_columns": "GrantaServerApiValueSpecifier",
        "type": "str",
        "value": "str",
    }

    attribute_map: dict[str, str] = {
        "attribute_guids_to_boost": "attributeGuidsToBoost",
        "attribute_identities_to_boost": "attributeIdentitiesToBoost",
        "attributes": "attributes",
        "column_guids_to_boost": "columnGuidsToBoost",
        "column_identities_to_boost": "columnIdentitiesToBoost",
        "local_columns": "localColumns",
        "type": "type",
        "value": "value",
    }

    subtype_mapping: dict[str, str] = {
        "attributes": "GrantaServerApiValueSpecifier",
        "localColumns": "GrantaServerApiValueSpecifier",
        "attributeIdentitiesToBoost": "GrantaServerApiSearchBoostByIdentity",
        "attributeGuidsToBoost": "GrantaServerApiSearchBoostByGuid",
        "columnIdentitiesToBoost": "GrantaServerApiSearchBoostByIdentity",
        "columnGuidsToBoost": "GrantaServerApiSearchBoostByGuid",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, attribute_guids_to_boost: "Union[list[GrantaServerApiSearchBoostByGuid], None, Unset_Type]" = Unset, attribute_identities_to_boost: "Union[list[GrantaServerApiSearchBoostByIdentity], None, Unset_Type]" = Unset, attributes: "Union[GrantaServerApiValueSpecifier, Unset_Type]" = Unset, column_guids_to_boost: "Union[list[GrantaServerApiSearchBoostByGuid], None, Unset_Type]" = Unset, column_identities_to_boost: "Union[list[GrantaServerApiSearchBoostByIdentity], None, Unset_Type]" = Unset, local_columns: "Union[GrantaServerApiValueSpecifier, Unset_Type]" = Unset, type: "str" = 'text', value: "Union[str, None, Unset_Type]" = Unset,) -> None:
        """GrantaServerApiSearchFreeTextCriterion - a model defined in Swagger

        Parameters
        ----------
        attribute_guids_to_boost: list[GrantaServerApiSearchBoostByGuid], optional
        attribute_identities_to_boost: list[GrantaServerApiSearchBoostByIdentity], optional
        attributes: GrantaServerApiValueSpecifier, optional
        column_guids_to_boost: list[GrantaServerApiSearchBoostByGuid], optional
        column_identities_to_boost: list[GrantaServerApiSearchBoostByIdentity], optional
        local_columns: GrantaServerApiValueSpecifier, optional
        type: str
        value: str, optional
        """
        super().__init__()
        self._value: Union[str, None, Unset_Type] = Unset
        self._attributes: Union[GrantaServerApiValueSpecifier, Unset_Type] = Unset
        self._local_columns: Union[GrantaServerApiValueSpecifier, Unset_Type] = Unset
        self._attribute_identities_to_boost: Union[list[GrantaServerApiSearchBoostByIdentity], None, Unset_Type] = Unset
        self._attribute_guids_to_boost: Union[list[GrantaServerApiSearchBoostByGuid], None, Unset_Type] = Unset
        self._column_identities_to_boost: Union[list[GrantaServerApiSearchBoostByIdentity], None, Unset_Type] = Unset
        self._column_guids_to_boost: Union[list[GrantaServerApiSearchBoostByGuid], None, Unset_Type] = Unset
        self._type: str

        if value is not Unset:
            self.value = value
        if attributes is not Unset:
            self.attributes = attributes
        if local_columns is not Unset:
            self.local_columns = local_columns
        if attribute_identities_to_boost is not Unset:
            self.attribute_identities_to_boost = attribute_identities_to_boost
        if attribute_guids_to_boost is not Unset:
            self.attribute_guids_to_boost = attribute_guids_to_boost
        if column_identities_to_boost is not Unset:
            self.column_identities_to_boost = column_identities_to_boost
        if column_guids_to_boost is not Unset:
            self.column_guids_to_boost = column_guids_to_boost
        self.type = type

    @property
    def value(self) -> "Union[str, None, Unset_Type]":
        """Gets the value of this GrantaServerApiSearchFreeTextCriterion.

        Returns
        -------
        Union[str, None, Unset_Type]
            The value of this GrantaServerApiSearchFreeTextCriterion.
        """
        return self._value

    @value.setter
    def value(self, value: "Union[str, None, Unset_Type]") -> None:
        """Sets the value of this GrantaServerApiSearchFreeTextCriterion.

        Parameters
        ----------
        value: Union[str, None, Unset_Type]
            The value of this GrantaServerApiSearchFreeTextCriterion.
        """
        self._value = value

    @property
    def attributes(self) -> "Union[GrantaServerApiValueSpecifier, Unset_Type]":
        """Gets the attributes of this GrantaServerApiSearchFreeTextCriterion.

        Returns
        -------
        Union[GrantaServerApiValueSpecifier, Unset_Type]
            The attributes of this GrantaServerApiSearchFreeTextCriterion.
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes: "Union[GrantaServerApiValueSpecifier, Unset_Type]") -> None:
        """Sets the attributes of this GrantaServerApiSearchFreeTextCriterion.

        Parameters
        ----------
        attributes: Union[GrantaServerApiValueSpecifier, Unset_Type]
            The attributes of this GrantaServerApiSearchFreeTextCriterion.
        """
        # Field is not nullable
        if attributes is None:
            raise ValueError("Invalid value for 'attributes', must not be 'None'")
        self._attributes = attributes

    @property
    def local_columns(self) -> "Union[GrantaServerApiValueSpecifier, Unset_Type]":
        """Gets the local_columns of this GrantaServerApiSearchFreeTextCriterion.

        Returns
        -------
        Union[GrantaServerApiValueSpecifier, Unset_Type]
            The local_columns of this GrantaServerApiSearchFreeTextCriterion.
        """
        return self._local_columns

    @local_columns.setter
    def local_columns(self, local_columns: "Union[GrantaServerApiValueSpecifier, Unset_Type]") -> None:
        """Sets the local_columns of this GrantaServerApiSearchFreeTextCriterion.

        Parameters
        ----------
        local_columns: Union[GrantaServerApiValueSpecifier, Unset_Type]
            The local_columns of this GrantaServerApiSearchFreeTextCriterion.
        """
        # Field is not nullable
        if local_columns is None:
            raise ValueError("Invalid value for 'local_columns', must not be 'None'")
        self._local_columns = local_columns

    @property
    def attribute_identities_to_boost(self) -> "Union[list[GrantaServerApiSearchBoostByIdentity], None, Unset_Type]":
        """Gets the attribute_identities_to_boost of this GrantaServerApiSearchFreeTextCriterion.

        Returns
        -------
        Union[list[GrantaServerApiSearchBoostByIdentity], None, Unset_Type]
            The attribute_identities_to_boost of this GrantaServerApiSearchFreeTextCriterion.
        """
        return self._attribute_identities_to_boost

    @attribute_identities_to_boost.setter
    def attribute_identities_to_boost(self, attribute_identities_to_boost: "Union[list[GrantaServerApiSearchBoostByIdentity], None, Unset_Type]") -> None:
        """Sets the attribute_identities_to_boost of this GrantaServerApiSearchFreeTextCriterion.

        Parameters
        ----------
        attribute_identities_to_boost: Union[list[GrantaServerApiSearchBoostByIdentity], None, Unset_Type]
            The attribute_identities_to_boost of this GrantaServerApiSearchFreeTextCriterion.
        """
        self._attribute_identities_to_boost = attribute_identities_to_boost

    @property
    def attribute_guids_to_boost(self) -> "Union[list[GrantaServerApiSearchBoostByGuid], None, Unset_Type]":
        """Gets the attribute_guids_to_boost of this GrantaServerApiSearchFreeTextCriterion.

        Returns
        -------
        Union[list[GrantaServerApiSearchBoostByGuid], None, Unset_Type]
            The attribute_guids_to_boost of this GrantaServerApiSearchFreeTextCriterion.
        """
        return self._attribute_guids_to_boost

    @attribute_guids_to_boost.setter
    def attribute_guids_to_boost(self, attribute_guids_to_boost: "Union[list[GrantaServerApiSearchBoostByGuid], None, Unset_Type]") -> None:
        """Sets the attribute_guids_to_boost of this GrantaServerApiSearchFreeTextCriterion.

        Parameters
        ----------
        attribute_guids_to_boost: Union[list[GrantaServerApiSearchBoostByGuid], None, Unset_Type]
            The attribute_guids_to_boost of this GrantaServerApiSearchFreeTextCriterion.
        """
        self._attribute_guids_to_boost = attribute_guids_to_boost

    @property
    def column_identities_to_boost(self) -> "Union[list[GrantaServerApiSearchBoostByIdentity], None, Unset_Type]":
        """Gets the column_identities_to_boost of this GrantaServerApiSearchFreeTextCriterion.

        Returns
        -------
        Union[list[GrantaServerApiSearchBoostByIdentity], None, Unset_Type]
            The column_identities_to_boost of this GrantaServerApiSearchFreeTextCriterion.
        """
        return self._column_identities_to_boost

    @column_identities_to_boost.setter
    def column_identities_to_boost(self, column_identities_to_boost: "Union[list[GrantaServerApiSearchBoostByIdentity], None, Unset_Type]") -> None:
        """Sets the column_identities_to_boost of this GrantaServerApiSearchFreeTextCriterion.

        Parameters
        ----------
        column_identities_to_boost: Union[list[GrantaServerApiSearchBoostByIdentity], None, Unset_Type]
            The column_identities_to_boost of this GrantaServerApiSearchFreeTextCriterion.
        """
        self._column_identities_to_boost = column_identities_to_boost

    @property
    def column_guids_to_boost(self) -> "Union[list[GrantaServerApiSearchBoostByGuid], None, Unset_Type]":
        """Gets the column_guids_to_boost of this GrantaServerApiSearchFreeTextCriterion.

        Returns
        -------
        Union[list[GrantaServerApiSearchBoostByGuid], None, Unset_Type]
            The column_guids_to_boost of this GrantaServerApiSearchFreeTextCriterion.
        """
        return self._column_guids_to_boost

    @column_guids_to_boost.setter
    def column_guids_to_boost(self, column_guids_to_boost: "Union[list[GrantaServerApiSearchBoostByGuid], None, Unset_Type]") -> None:
        """Sets the column_guids_to_boost of this GrantaServerApiSearchFreeTextCriterion.

        Parameters
        ----------
        column_guids_to_boost: Union[list[GrantaServerApiSearchBoostByGuid], None, Unset_Type]
            The column_guids_to_boost of this GrantaServerApiSearchFreeTextCriterion.
        """
        self._column_guids_to_boost = column_guids_to_boost

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchFreeTextCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchFreeTextCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchFreeTextCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchFreeTextCriterion.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

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
        if not isinstance(other, GrantaServerApiSearchFreeTextCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

