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

from ansys.grantami.serverapi_openapi.v2024r1.models.granta_server_api_search_datum_criterion import (  # noqa: F401
    GrantaServerApiSearchDatumCriterion,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiSearchLinkDatumCriterion(GrantaServerApiSearchDatumCriterion):
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
        "indirect_links": "GrantaServerApiIndirectLinks",
        "inner_criterion": "GrantaServerApiSearchCriterion",
        "link_datum_type": "GrantaServerApiLinkAttributeType",
        "local_criterion": "GrantaServerApiSearchCriterion",
        "local_rows_behaviour": "GrantaServerApiSearchLocalRowsBehaviour",
        "search_in_reversed_direction": "bool",
        "target_attribute_guid": "str",
        "target_attribute_identity": "int",
        "target_database_key": "str",
        "target_table_guid": "str",
        "target_table_identity": "int",
        "type": "str",
    }

    attribute_map: dict[str, str] = {
        "indirect_links": "indirectLinks",
        "inner_criterion": "innerCriterion",
        "link_datum_type": "linkDatumType",
        "local_criterion": "localCriterion",
        "local_rows_behaviour": "localRowsBehaviour",
        "search_in_reversed_direction": "searchInReversedDirection",
        "target_attribute_guid": "targetAttributeGuid",
        "target_attribute_identity": "targetAttributeIdentity",
        "target_database_key": "targetDatabaseKey",
        "target_table_guid": "targetTableGuid",
        "target_table_identity": "targetTableIdentity",
        "type": "type",
    }

    subtype_mapping: dict[str, str] = {
        "localCriterion": "GrantaServerApiSearchCriterion",
        "linkDatumType": "GrantaServerApiLinkAttributeType",
        "indirectLinks": "GrantaServerApiIndirectLinks",
        "innerCriterion": "GrantaServerApiSearchCriterion",
        "localRowsBehaviour": "GrantaServerApiSearchLocalRowsBehaviour",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        indirect_links: "Union[GrantaServerApiIndirectLinks, Unset_Type]" = Unset,
        inner_criterion: "Union[GrantaServerApiSearchCriterion, Unset_Type]" = Unset,
        link_datum_type: "Union[GrantaServerApiLinkAttributeType, Unset_Type]" = Unset,
        local_criterion: "Union[GrantaServerApiSearchCriterion, Unset_Type]" = Unset,
        local_rows_behaviour: "Union[GrantaServerApiSearchLocalRowsBehaviour, Unset_Type]" = Unset,
        search_in_reversed_direction: "Union[bool, Unset_Type]" = Unset,
        target_attribute_guid: "Union[str, None, Unset_Type]" = Unset,
        target_attribute_identity: "Union[int, None, Unset_Type]" = Unset,
        target_database_key: "Union[str, None, Unset_Type]" = Unset,
        target_table_guid: "Union[str, None, Unset_Type]" = Unset,
        target_table_identity: "Union[int, None, Unset_Type]" = Unset,
        type: "str" = "link",
    ) -> None:
        """GrantaServerApiSearchLinkDatumCriterion - a model defined in Swagger

        Parameters
        ----------
        indirect_links: GrantaServerApiIndirectLinks, optional
        inner_criterion: GrantaServerApiSearchCriterion, optional
        link_datum_type: GrantaServerApiLinkAttributeType, optional
        local_criterion: GrantaServerApiSearchCriterion, optional
        local_rows_behaviour: GrantaServerApiSearchLocalRowsBehaviour, optional
        search_in_reversed_direction: bool, optional
        target_attribute_guid: str, optional
        target_attribute_identity: int, optional
        target_database_key: str, optional
        target_table_guid: str, optional
        target_table_identity: int, optional
        type: str
        """
        super().__init__()
        self._target_table_identity: Union[int, None, Unset_Type] = Unset
        self._target_table_guid: Union[str, None, Unset_Type] = Unset
        self._target_database_key: Union[str, None, Unset_Type] = Unset
        self._local_criterion: Union[GrantaServerApiSearchCriterion, Unset_Type] = Unset
        self._link_datum_type: Union[GrantaServerApiLinkAttributeType, Unset_Type] = Unset
        self._indirect_links: Union[GrantaServerApiIndirectLinks, Unset_Type] = Unset
        self._search_in_reversed_direction: Union[bool, Unset_Type] = Unset
        self._target_attribute_identity: Union[int, None, Unset_Type] = Unset
        self._target_attribute_guid: Union[str, None, Unset_Type] = Unset
        self._inner_criterion: Union[GrantaServerApiSearchCriterion, Unset_Type] = Unset
        self._type: str
        self._local_rows_behaviour: Union[GrantaServerApiSearchLocalRowsBehaviour, Unset_Type] = (
            Unset
        )

        if target_table_identity is not Unset:
            self.target_table_identity = target_table_identity
        if target_table_guid is not Unset:
            self.target_table_guid = target_table_guid
        if target_database_key is not Unset:
            self.target_database_key = target_database_key
        if local_criterion is not Unset:
            self.local_criterion = local_criterion
        if link_datum_type is not Unset:
            self.link_datum_type = link_datum_type
        if indirect_links is not Unset:
            self.indirect_links = indirect_links
        if search_in_reversed_direction is not Unset:
            self.search_in_reversed_direction = search_in_reversed_direction
        if target_attribute_identity is not Unset:
            self.target_attribute_identity = target_attribute_identity
        if target_attribute_guid is not Unset:
            self.target_attribute_guid = target_attribute_guid
        if inner_criterion is not Unset:
            self.inner_criterion = inner_criterion
        self.type = type
        if local_rows_behaviour is not Unset:
            self.local_rows_behaviour = local_rows_behaviour

    @property
    def target_table_identity(self) -> "Union[int, None, Unset_Type]":
        """Gets the target_table_identity of this GrantaServerApiSearchLinkDatumCriterion.
        Table containing the linked records.  The target table can be omitted; it is likely to improve performance if it is included.  For tabular search, if either the target attribute or the target table is provided, they should both be provided.

        Returns
        -------
        Union[int, None, Unset_Type]
            The target_table_identity of this GrantaServerApiSearchLinkDatumCriterion.
        """
        return self._target_table_identity

    @target_table_identity.setter
    def target_table_identity(self, target_table_identity: "Union[int, None, Unset_Type]") -> None:
        """Sets the target_table_identity of this GrantaServerApiSearchLinkDatumCriterion.
        Table containing the linked records.  The target table can be omitted; it is likely to improve performance if it is included.  For tabular search, if either the target attribute or the target table is provided, they should both be provided.

        Parameters
        ----------
        target_table_identity: Union[int, None, Unset_Type]
            The target_table_identity of this GrantaServerApiSearchLinkDatumCriterion.
        """
        self._target_table_identity = target_table_identity

    @property
    def target_table_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the target_table_guid of this GrantaServerApiSearchLinkDatumCriterion.
        Table containing the linked records.  The target table can be omitted; it is likely to improve performance if it is included.  For tabular search, if either the target attribute or the target table is provided, they should both be provided.

        Returns
        -------
        Union[str, None, Unset_Type]
            The target_table_guid of this GrantaServerApiSearchLinkDatumCriterion.
        """
        return self._target_table_guid

    @target_table_guid.setter
    def target_table_guid(self, target_table_guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the target_table_guid of this GrantaServerApiSearchLinkDatumCriterion.
        Table containing the linked records.  The target table can be omitted; it is likely to improve performance if it is included.  For tabular search, if either the target attribute or the target table is provided, they should both be provided.

        Parameters
        ----------
        target_table_guid: Union[str, None, Unset_Type]
            The target_table_guid of this GrantaServerApiSearchLinkDatumCriterion.
        """
        self._target_table_guid = target_table_guid

    @property
    def target_database_key(self) -> "Union[str, None, Unset_Type]":
        """Gets the target_database_key of this GrantaServerApiSearchLinkDatumCriterion.
        Database containing the linked records. For reverse cross database links, this is the database where the link is defined

        Returns
        -------
        Union[str, None, Unset_Type]
            The target_database_key of this GrantaServerApiSearchLinkDatumCriterion.
        """
        return self._target_database_key

    @target_database_key.setter
    def target_database_key(self, target_database_key: "Union[str, None, Unset_Type]") -> None:
        """Sets the target_database_key of this GrantaServerApiSearchLinkDatumCriterion.
        Database containing the linked records. For reverse cross database links, this is the database where the link is defined

        Parameters
        ----------
        target_database_key: Union[str, None, Unset_Type]
            The target_database_key of this GrantaServerApiSearchLinkDatumCriterion.
        """
        self._target_database_key = target_database_key

    @property
    def local_criterion(self) -> "Union[GrantaServerApiSearchCriterion, Unset_Type]":
        """Gets the local_criterion of this GrantaServerApiSearchLinkDatumCriterion.

        Returns
        -------
        Union[GrantaServerApiSearchCriterion, Unset_Type]
            The local_criterion of this GrantaServerApiSearchLinkDatumCriterion.
        """
        return self._local_criterion

    @local_criterion.setter
    def local_criterion(
        self, local_criterion: "Union[GrantaServerApiSearchCriterion, Unset_Type]"
    ) -> None:
        """Sets the local_criterion of this GrantaServerApiSearchLinkDatumCriterion.

        Parameters
        ----------
        local_criterion: Union[GrantaServerApiSearchCriterion, Unset_Type]
            The local_criterion of this GrantaServerApiSearchLinkDatumCriterion.
        """
        # Field is not nullable
        if local_criterion is None:
            raise ValueError("Invalid value for 'local_criterion', must not be 'None'")
        self._local_criterion = local_criterion

    @property
    def link_datum_type(self) -> "Union[GrantaServerApiLinkAttributeType, Unset_Type]":
        """Gets the link_datum_type of this GrantaServerApiSearchLinkDatumCriterion.

        Returns
        -------
        Union[GrantaServerApiLinkAttributeType, Unset_Type]
            The link_datum_type of this GrantaServerApiSearchLinkDatumCriterion.
        """
        return self._link_datum_type

    @link_datum_type.setter
    def link_datum_type(
        self, link_datum_type: "Union[GrantaServerApiLinkAttributeType, Unset_Type]"
    ) -> None:
        """Sets the link_datum_type of this GrantaServerApiSearchLinkDatumCriterion.

        Parameters
        ----------
        link_datum_type: Union[GrantaServerApiLinkAttributeType, Unset_Type]
            The link_datum_type of this GrantaServerApiSearchLinkDatumCriterion.
        """
        # Field is not nullable
        if link_datum_type is None:
            raise ValueError("Invalid value for 'link_datum_type', must not be 'None'")
        self._link_datum_type = link_datum_type

    @property
    def indirect_links(self) -> "Union[GrantaServerApiIndirectLinks, Unset_Type]":
        """Gets the indirect_links of this GrantaServerApiSearchLinkDatumCriterion.

        Returns
        -------
        Union[GrantaServerApiIndirectLinks, Unset_Type]
            The indirect_links of this GrantaServerApiSearchLinkDatumCriterion.
        """
        return self._indirect_links

    @indirect_links.setter
    def indirect_links(
        self, indirect_links: "Union[GrantaServerApiIndirectLinks, Unset_Type]"
    ) -> None:
        """Sets the indirect_links of this GrantaServerApiSearchLinkDatumCriterion.

        Parameters
        ----------
        indirect_links: Union[GrantaServerApiIndirectLinks, Unset_Type]
            The indirect_links of this GrantaServerApiSearchLinkDatumCriterion.
        """
        # Field is not nullable
        if indirect_links is None:
            raise ValueError("Invalid value for 'indirect_links', must not be 'None'")
        self._indirect_links = indirect_links

    @property
    def search_in_reversed_direction(self) -> "Union[bool, Unset_Type]":
        """Gets the search_in_reversed_direction of this GrantaServerApiSearchLinkDatumCriterion.

        Returns
        -------
        Union[bool, Unset_Type]
            The search_in_reversed_direction of this GrantaServerApiSearchLinkDatumCriterion.
        """
        return self._search_in_reversed_direction

    @search_in_reversed_direction.setter
    def search_in_reversed_direction(
        self, search_in_reversed_direction: "Union[bool, Unset_Type]"
    ) -> None:
        """Sets the search_in_reversed_direction of this GrantaServerApiSearchLinkDatumCriterion.

        Parameters
        ----------
        search_in_reversed_direction: Union[bool, Unset_Type]
            The search_in_reversed_direction of this GrantaServerApiSearchLinkDatumCriterion.
        """
        # Field is not nullable
        if search_in_reversed_direction is None:
            raise ValueError("Invalid value for 'search_in_reversed_direction', must not be 'None'")
        self._search_in_reversed_direction = search_in_reversed_direction

    @property
    def target_attribute_identity(self) -> "Union[int, None, Unset_Type]":
        """Gets the target_attribute_identity of this GrantaServerApiSearchLinkDatumCriterion.
        For tabular searching: this is the identity of the short-text linking attribute.  The target attribute and table can both be omitted; it is likely to improve performance if they are included.  If either the target attribute or the target table is provided, they should both be provided.  Otherwise null.

        Returns
        -------
        Union[int, None, Unset_Type]
            The target_attribute_identity of this GrantaServerApiSearchLinkDatumCriterion.
        """
        return self._target_attribute_identity

    @target_attribute_identity.setter
    def target_attribute_identity(
        self, target_attribute_identity: "Union[int, None, Unset_Type]"
    ) -> None:
        """Sets the target_attribute_identity of this GrantaServerApiSearchLinkDatumCriterion.
        For tabular searching: this is the identity of the short-text linking attribute.  The target attribute and table can both be omitted; it is likely to improve performance if they are included.  If either the target attribute or the target table is provided, they should both be provided.  Otherwise null.

        Parameters
        ----------
        target_attribute_identity: Union[int, None, Unset_Type]
            The target_attribute_identity of this GrantaServerApiSearchLinkDatumCriterion.
        """
        self._target_attribute_identity = target_attribute_identity

    @property
    def target_attribute_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the target_attribute_guid of this GrantaServerApiSearchLinkDatumCriterion.
        For tabular searching: this is the GUID of the short-text linking attribute.  /// The target attribute and table can both be omitted; it is likely to improve performance if they are included.  If either the target attribute or the target table is provided, they should both be provided.  Otherwise null.

        Returns
        -------
        Union[str, None, Unset_Type]
            The target_attribute_guid of this GrantaServerApiSearchLinkDatumCriterion.
        """
        return self._target_attribute_guid

    @target_attribute_guid.setter
    def target_attribute_guid(self, target_attribute_guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the target_attribute_guid of this GrantaServerApiSearchLinkDatumCriterion.
        For tabular searching: this is the GUID of the short-text linking attribute.  /// The target attribute and table can both be omitted; it is likely to improve performance if they are included.  If either the target attribute or the target table is provided, they should both be provided.  Otherwise null.

        Parameters
        ----------
        target_attribute_guid: Union[str, None, Unset_Type]
            The target_attribute_guid of this GrantaServerApiSearchLinkDatumCriterion.
        """
        self._target_attribute_guid = target_attribute_guid

    @property
    def inner_criterion(self) -> "Union[GrantaServerApiSearchCriterion, Unset_Type]":
        """Gets the inner_criterion of this GrantaServerApiSearchLinkDatumCriterion.

        Returns
        -------
        Union[GrantaServerApiSearchCriterion, Unset_Type]
            The inner_criterion of this GrantaServerApiSearchLinkDatumCriterion.
        """
        return self._inner_criterion

    @inner_criterion.setter
    def inner_criterion(
        self, inner_criterion: "Union[GrantaServerApiSearchCriterion, Unset_Type]"
    ) -> None:
        """Sets the inner_criterion of this GrantaServerApiSearchLinkDatumCriterion.

        Parameters
        ----------
        inner_criterion: Union[GrantaServerApiSearchCriterion, Unset_Type]
            The inner_criterion of this GrantaServerApiSearchLinkDatumCriterion.
        """
        # Field is not nullable
        if inner_criterion is None:
            raise ValueError("Invalid value for 'inner_criterion', must not be 'None'")
        self._inner_criterion = inner_criterion

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchLinkDatumCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchLinkDatumCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchLinkDatumCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchLinkDatumCriterion.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

    @property
    def local_rows_behaviour(self) -> "Union[GrantaServerApiSearchLocalRowsBehaviour, Unset_Type]":
        """Gets the local_rows_behaviour of this GrantaServerApiSearchLinkDatumCriterion.

        Returns
        -------
        Union[GrantaServerApiSearchLocalRowsBehaviour, Unset_Type]
            The local_rows_behaviour of this GrantaServerApiSearchLinkDatumCriterion.
        """
        return self._local_rows_behaviour

    @local_rows_behaviour.setter
    def local_rows_behaviour(
        self, local_rows_behaviour: "Union[GrantaServerApiSearchLocalRowsBehaviour, Unset_Type]"
    ) -> None:
        """Sets the local_rows_behaviour of this GrantaServerApiSearchLinkDatumCriterion.

        Parameters
        ----------
        local_rows_behaviour: Union[GrantaServerApiSearchLocalRowsBehaviour, Unset_Type]
            The local_rows_behaviour of this GrantaServerApiSearchLinkDatumCriterion.
        """
        # Field is not nullable
        if local_rows_behaviour is None:
            raise ValueError("Invalid value for 'local_rows_behaviour', must not be 'None'")
        self._local_rows_behaviour = local_rows_behaviour

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
        if not isinstance(other, GrantaServerApiSearchLinkDatumCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
