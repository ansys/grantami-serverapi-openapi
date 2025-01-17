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
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, Union  # noqa: F401

from ansys.grantami.serverapi_openapi.v242.models.granta_server_api_schema_record_link_groups_create_record_link_group import (  # noqa: F401
    GrantaServerApiSchemaRecordLinkGroupsCreateRecordLinkGroup,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiSchemaRecordLinkGroupsCreateDynamicRecordLinkGroup(
    GrantaServerApiSchemaRecordLinkGroupsCreateRecordLinkGroup
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
    swagger_types: Dict[str, str] = {
        "attribute_pairs": "list[GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair]",
        "link_target": "GrantaServerApiSchemaRecordLinkGroupsLinkTarget",
        "name": "str",
        "reverse_name": "str",
        "forbid_orphans": "bool",
        "guid": "str",
        "referential_integrity_model": "GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "attribute_pairs": "attributePairs",
        "link_target": "linkTarget",
        "name": "name",
        "reverse_name": "reverseName",
        "forbid_orphans": "forbidOrphans",
        "guid": "guid",
        "referential_integrity_model": "referentialIntegrityModel",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {
        "referentialIntegrityModel": "GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel",
        "attributePairs": "GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_pairs: "List[GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair]",
        link_target: "GrantaServerApiSchemaRecordLinkGroupsLinkTarget",
        name: "str",
        reverse_name: "str",
        forbid_orphans: "Union[bool, Unset_Type]" = Unset,
        guid: "Union[str, Unset_Type]" = Unset,
        referential_integrity_model: "Union[GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel, Unset_Type]" = Unset,
        type: "str" = "dynamic",
    ) -> None:
        """GrantaServerApiSchemaRecordLinkGroupsCreateDynamicRecordLinkGroup - a model defined in Swagger

        Parameters
        ----------
        attribute_pairs: List[GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair]
        link_target: GrantaServerApiSchemaRecordLinkGroupsLinkTarget
        name: str
        reverse_name: str
        forbid_orphans: bool, optional
        guid: str, optional
        referential_integrity_model: GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel, optional
        type: str
        """
        super().__init__(link_target=link_target, name=name, reverse_name=reverse_name, guid=guid)
        self._type: str
        self._forbid_orphans: Union[bool, Unset_Type] = Unset
        self._referential_integrity_model: Union[
            GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel, Unset_Type
        ] = Unset
        self._attribute_pairs: List[GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair]

        self.type = type
        if forbid_orphans is not Unset:
            self.forbid_orphans = forbid_orphans
        if referential_integrity_model is not Unset:
            self.referential_integrity_model = referential_integrity_model
        self.attribute_pairs = attribute_pairs

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaRecordLinkGroupsCreateDynamicRecordLinkGroup.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaRecordLinkGroupsCreateDynamicRecordLinkGroup.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaRecordLinkGroupsCreateDynamicRecordLinkGroup.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaRecordLinkGroupsCreateDynamicRecordLinkGroup.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

    @property
    def forbid_orphans(self) -> "Union[bool, Unset_Type]":
        """Gets the forbid_orphans of this GrantaServerApiSchemaRecordLinkGroupsCreateDynamicRecordLinkGroup.

        Returns
        -------
        Union[bool, Unset_Type]
            The forbid_orphans of this GrantaServerApiSchemaRecordLinkGroupsCreateDynamicRecordLinkGroup.
        """
        return self._forbid_orphans

    @forbid_orphans.setter
    def forbid_orphans(self, forbid_orphans: "Union[bool, Unset_Type]") -> None:
        """Sets the forbid_orphans of this GrantaServerApiSchemaRecordLinkGroupsCreateDynamicRecordLinkGroup.

        Parameters
        ----------
        forbid_orphans: Union[bool, Unset_Type]
            The forbid_orphans of this GrantaServerApiSchemaRecordLinkGroupsCreateDynamicRecordLinkGroup.
        """
        # Field is not nullable
        if forbid_orphans is None:
            raise ValueError("Invalid value for 'forbid_orphans', must not be 'None'")
        self._forbid_orphans = forbid_orphans

    @property
    def referential_integrity_model(
        self,
    ) -> "Union[GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel, Unset_Type]":
        """Gets the referential_integrity_model of this GrantaServerApiSchemaRecordLinkGroupsCreateDynamicRecordLinkGroup.

        Returns
        -------
        Union[GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel, Unset_Type]
            The referential_integrity_model of this GrantaServerApiSchemaRecordLinkGroupsCreateDynamicRecordLinkGroup.
        """
        return self._referential_integrity_model

    @referential_integrity_model.setter
    def referential_integrity_model(
        self,
        referential_integrity_model: "Union[GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel, Unset_Type]",
    ) -> None:
        """Sets the referential_integrity_model of this GrantaServerApiSchemaRecordLinkGroupsCreateDynamicRecordLinkGroup.

        Parameters
        ----------
        referential_integrity_model: Union[GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel, Unset_Type]
            The referential_integrity_model of this GrantaServerApiSchemaRecordLinkGroupsCreateDynamicRecordLinkGroup.
        """
        # Field is not nullable
        if referential_integrity_model is None:
            raise ValueError("Invalid value for 'referential_integrity_model', must not be 'None'")
        self._referential_integrity_model = referential_integrity_model

    @property
    def attribute_pairs(
        self,
    ) -> "List[GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair]":
        """Gets the attribute_pairs of this GrantaServerApiSchemaRecordLinkGroupsCreateDynamicRecordLinkGroup.

        Returns
        -------
        List[GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair]
            The attribute_pairs of this GrantaServerApiSchemaRecordLinkGroupsCreateDynamicRecordLinkGroup.
        """
        return self._attribute_pairs

    @attribute_pairs.setter
    def attribute_pairs(
        self, attribute_pairs: "List[GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair]"
    ) -> None:
        """Sets the attribute_pairs of this GrantaServerApiSchemaRecordLinkGroupsCreateDynamicRecordLinkGroup.

        Parameters
        ----------
        attribute_pairs: List[GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair]
            The attribute_pairs of this GrantaServerApiSchemaRecordLinkGroupsCreateDynamicRecordLinkGroup.
        """
        # Field is not nullable
        if attribute_pairs is None:
            raise ValueError("Invalid value for 'attribute_pairs', must not be 'None'")
        # Field is required
        if attribute_pairs is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'attribute_pairs', must not be 'Unset'")
        self._attribute_pairs = attribute_pairs

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
        if not isinstance(other, GrantaServerApiSchemaRecordLinkGroupsCreateDynamicRecordLinkGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
