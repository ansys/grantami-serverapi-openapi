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

from ansys.grantami.serverapi_openapi.models.gsa_attribute_type import GsaAttributeType
from ansys.grantami.serverapi_openapi.models.gsa_datum_exists_criterion import (  # noqa: F401
    GsaDatumExistsCriterion,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaLinkExistsDatumCriterion(GsaDatumExistsCriterion):
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
        "target_database_key": "str",
        "type": "GsaAttributeType",
        "indirect_links": "GsaIndirectLinks",
        "link_datum_type": "GsaLinkAttributeType",
        "local_rows_behavior": "GsaLocalRowsBehavior",
        "search_in_reversed_direction": "bool",
        "target_attribute_guid": "str",
        "target_attribute_identity": "int",
        "target_table_guid": "str",
        "target_table_identity": "int",
    }

    attribute_map: dict[str, str] = {
        "target_database_key": "targetDatabaseKey",
        "type": "type",
        "indirect_links": "indirectLinks",
        "link_datum_type": "linkDatumType",
        "local_rows_behavior": "localRowsBehavior",
        "search_in_reversed_direction": "searchInReversedDirection",
        "target_attribute_guid": "targetAttributeGuid",
        "target_attribute_identity": "targetAttributeIdentity",
        "target_table_guid": "targetTableGuid",
        "target_table_identity": "targetTableIdentity",
    }

    subtype_mapping: dict[str, str] = {
        "linkDatumType": "GsaLinkAttributeType",
        "indirectLinks": "GsaIndirectLinks",
        "localRowsBehavior": "GsaLocalRowsBehavior",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        target_database_key: "str",
        type: "GsaAttributeType" = GsaAttributeType.LINK,
        indirect_links: "Union[GsaIndirectLinks, Unset_Type]" = Unset,
        link_datum_type: "Union[GsaLinkAttributeType, Unset_Type]" = Unset,
        local_rows_behavior: "Union[GsaLocalRowsBehavior, Unset_Type]" = Unset,
        search_in_reversed_direction: "Union[bool, Unset_Type]" = Unset,
        target_attribute_guid: "Union[str, None, Unset_Type]" = Unset,
        target_attribute_identity: "Union[int, None, Unset_Type]" = Unset,
        target_table_guid: "Union[str, None, Unset_Type]" = Unset,
        target_table_identity: "Union[int, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaLinkExistsDatumCriterion - a model defined in Swagger

        Parameters
        ----------
        target_database_key: str
        type: GsaAttributeType
        indirect_links: GsaIndirectLinks, optional
        link_datum_type: GsaLinkAttributeType, optional
        local_rows_behavior: GsaLocalRowsBehavior, optional
        search_in_reversed_direction: bool, optional
        target_attribute_guid: str, optional
        target_attribute_identity: int, optional
        target_table_guid: str, optional
        target_table_identity: int, optional
        """
        super().__init__(type=type)
        self._target_table_identity: Union[int, None, Unset_Type] = Unset
        self._target_table_guid: Union[str, None, Unset_Type] = Unset
        self._target_database_key: str
        self._link_datum_type: Union[GsaLinkAttributeType, Unset_Type] = Unset
        self._indirect_links: Union[GsaIndirectLinks, Unset_Type] = Unset
        self._search_in_reversed_direction: Union[bool, Unset_Type] = Unset
        self._local_rows_behavior: Union[GsaLocalRowsBehavior, Unset_Type] = Unset
        self._target_attribute_identity: Union[int, None, Unset_Type] = Unset
        self._target_attribute_guid: Union[str, None, Unset_Type] = Unset

        if target_table_identity is not Unset:
            self.target_table_identity = target_table_identity
        if target_table_guid is not Unset:
            self.target_table_guid = target_table_guid
        self.target_database_key = target_database_key
        if link_datum_type is not Unset:
            self.link_datum_type = link_datum_type
        if indirect_links is not Unset:
            self.indirect_links = indirect_links
        if search_in_reversed_direction is not Unset:
            self.search_in_reversed_direction = search_in_reversed_direction
        if local_rows_behavior is not Unset:
            self.local_rows_behavior = local_rows_behavior
        if target_attribute_identity is not Unset:
            self.target_attribute_identity = target_attribute_identity
        if target_attribute_guid is not Unset:
            self.target_attribute_guid = target_attribute_guid

    @property
    def target_table_identity(self) -> "Union[int, None, Unset_Type]":
        """Gets the target_table_identity of this GsaLinkExistsDatumCriterion.
        Table containing the linked records

        Returns
        -------
        Union[int, None, Unset_Type]
            The target_table_identity of this GsaLinkExistsDatumCriterion.
        """
        return self._target_table_identity

    @target_table_identity.setter
    def target_table_identity(self, target_table_identity: "Union[int, None, Unset_Type]") -> None:
        """Sets the target_table_identity of this GsaLinkExistsDatumCriterion.
        Table containing the linked records

        Parameters
        ----------
        target_table_identity: Union[int, None, Unset_Type]
            The target_table_identity of this GsaLinkExistsDatumCriterion.
        """
        self._target_table_identity = target_table_identity

    @property
    def target_table_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the target_table_guid of this GsaLinkExistsDatumCriterion.
        Table containing the linked records

        Returns
        -------
        Union[str, None, Unset_Type]
            The target_table_guid of this GsaLinkExistsDatumCriterion.
        """
        return self._target_table_guid

    @target_table_guid.setter
    def target_table_guid(self, target_table_guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the target_table_guid of this GsaLinkExistsDatumCriterion.
        Table containing the linked records

        Parameters
        ----------
        target_table_guid: Union[str, None, Unset_Type]
            The target_table_guid of this GsaLinkExistsDatumCriterion.
        """
        self._target_table_guid = target_table_guid

    @property
    def target_database_key(self) -> "str":
        """Gets the target_database_key of this GsaLinkExistsDatumCriterion.
        Database containing the linked records. For reverse cross database links, this is the database where the link is defined

        Returns
        -------
        str
            The target_database_key of this GsaLinkExistsDatumCriterion.
        """
        return self._target_database_key

    @target_database_key.setter
    def target_database_key(self, target_database_key: "str") -> None:
        """Sets the target_database_key of this GsaLinkExistsDatumCriterion.
        Database containing the linked records. For reverse cross database links, this is the database where the link is defined

        Parameters
        ----------
        target_database_key: str
            The target_database_key of this GsaLinkExistsDatumCriterion.
        """
        # Field is not nullable
        if target_database_key is None:
            raise ValueError("Invalid value for 'target_database_key', must not be 'None'")
        # Field is required
        if target_database_key is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'target_database_key', must not be 'Unset'")
        self._target_database_key = target_database_key

    @property
    def link_datum_type(self) -> "Union[GsaLinkAttributeType, Unset_Type]":
        """Gets the link_datum_type of this GsaLinkExistsDatumCriterion.

        Returns
        -------
        Union[GsaLinkAttributeType, Unset_Type]
            The link_datum_type of this GsaLinkExistsDatumCriterion.
        """
        return self._link_datum_type

    @link_datum_type.setter
    def link_datum_type(self, link_datum_type: "Union[GsaLinkAttributeType, Unset_Type]") -> None:
        """Sets the link_datum_type of this GsaLinkExistsDatumCriterion.

        Parameters
        ----------
        link_datum_type: Union[GsaLinkAttributeType, Unset_Type]
            The link_datum_type of this GsaLinkExistsDatumCriterion.
        """
        # Field is not nullable
        if link_datum_type is None:
            raise ValueError("Invalid value for 'link_datum_type', must not be 'None'")
        self._link_datum_type = link_datum_type

    @property
    def indirect_links(self) -> "Union[GsaIndirectLinks, Unset_Type]":
        """Gets the indirect_links of this GsaLinkExistsDatumCriterion.

        Returns
        -------
        Union[GsaIndirectLinks, Unset_Type]
            The indirect_links of this GsaLinkExistsDatumCriterion.
        """
        return self._indirect_links

    @indirect_links.setter
    def indirect_links(self, indirect_links: "Union[GsaIndirectLinks, Unset_Type]") -> None:
        """Sets the indirect_links of this GsaLinkExistsDatumCriterion.

        Parameters
        ----------
        indirect_links: Union[GsaIndirectLinks, Unset_Type]
            The indirect_links of this GsaLinkExistsDatumCriterion.
        """
        # Field is not nullable
        if indirect_links is None:
            raise ValueError("Invalid value for 'indirect_links', must not be 'None'")
        self._indirect_links = indirect_links

    @property
    def search_in_reversed_direction(self) -> "Union[bool, Unset_Type]":
        """Gets the search_in_reversed_direction of this GsaLinkExistsDatumCriterion.

        Returns
        -------
        Union[bool, Unset_Type]
            The search_in_reversed_direction of this GsaLinkExistsDatumCriterion.
        """
        return self._search_in_reversed_direction

    @search_in_reversed_direction.setter
    def search_in_reversed_direction(
        self, search_in_reversed_direction: "Union[bool, Unset_Type]"
    ) -> None:
        """Sets the search_in_reversed_direction of this GsaLinkExistsDatumCriterion.

        Parameters
        ----------
        search_in_reversed_direction: Union[bool, Unset_Type]
            The search_in_reversed_direction of this GsaLinkExistsDatumCriterion.
        """
        # Field is not nullable
        if search_in_reversed_direction is None:
            raise ValueError("Invalid value for 'search_in_reversed_direction', must not be 'None'")
        self._search_in_reversed_direction = search_in_reversed_direction

    @property
    def local_rows_behavior(self) -> "Union[GsaLocalRowsBehavior, Unset_Type]":
        """Gets the local_rows_behavior of this GsaLinkExistsDatumCriterion.

        Returns
        -------
        Union[GsaLocalRowsBehavior, Unset_Type]
            The local_rows_behavior of this GsaLinkExistsDatumCriterion.
        """
        return self._local_rows_behavior

    @local_rows_behavior.setter
    def local_rows_behavior(
        self, local_rows_behavior: "Union[GsaLocalRowsBehavior, Unset_Type]"
    ) -> None:
        """Sets the local_rows_behavior of this GsaLinkExistsDatumCriterion.

        Parameters
        ----------
        local_rows_behavior: Union[GsaLocalRowsBehavior, Unset_Type]
            The local_rows_behavior of this GsaLinkExistsDatumCriterion.
        """
        # Field is not nullable
        if local_rows_behavior is None:
            raise ValueError("Invalid value for 'local_rows_behavior', must not be 'None'")
        self._local_rows_behavior = local_rows_behavior

    @property
    def target_attribute_identity(self) -> "Union[int, None, Unset_Type]":
        """Gets the target_attribute_identity of this GsaLinkExistsDatumCriterion.
        For tabular searching: this is the identity of the short-text linking attribute.  Otherwise null.

        Returns
        -------
        Union[int, None, Unset_Type]
            The target_attribute_identity of this GsaLinkExistsDatumCriterion.
        """
        return self._target_attribute_identity

    @target_attribute_identity.setter
    def target_attribute_identity(
        self, target_attribute_identity: "Union[int, None, Unset_Type]"
    ) -> None:
        """Sets the target_attribute_identity of this GsaLinkExistsDatumCriterion.
        For tabular searching: this is the identity of the short-text linking attribute.  Otherwise null.

        Parameters
        ----------
        target_attribute_identity: Union[int, None, Unset_Type]
            The target_attribute_identity of this GsaLinkExistsDatumCriterion.
        """
        self._target_attribute_identity = target_attribute_identity

    @property
    def target_attribute_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the target_attribute_guid of this GsaLinkExistsDatumCriterion.
        For tabular searching: this is the GUID of the short-text linking attribute.  Otherwise null.

        Returns
        -------
        Union[str, None, Unset_Type]
            The target_attribute_guid of this GsaLinkExistsDatumCriterion.
        """
        return self._target_attribute_guid

    @target_attribute_guid.setter
    def target_attribute_guid(self, target_attribute_guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the target_attribute_guid of this GsaLinkExistsDatumCriterion.
        For tabular searching: this is the GUID of the short-text linking attribute.  Otherwise null.

        Parameters
        ----------
        target_attribute_guid: Union[str, None, Unset_Type]
            The target_attribute_guid of this GsaLinkExistsDatumCriterion.
        """
        self._target_attribute_guid = target_attribute_guid

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
        if not isinstance(other, GsaLinkExistsDatumCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
