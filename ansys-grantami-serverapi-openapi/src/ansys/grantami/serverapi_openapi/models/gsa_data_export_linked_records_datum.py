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

from ansys.grantami.serverapi_openapi.models.gsa_attribute_type import GsaAttributeType
from ansys.grantami.serverapi_openapi.models.gsa_data_export_link_datum import (  # noqa: F401
    GsaDataExportLinkDatum,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaDataExportLinkedRecordsDatum(GsaDataExportLinkDatum):
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
        "datum_type": "GsaAttributeType",
        "link_datum_type": "str",
        "not_applicable": "str",
        "attribute_guid": "str",
        "attribute_identity": "int",
        "export_in_reversed_direction": "bool",
        "link_attribute_type": "GsaLinkAttributeType",
        "link_group_identities_by_database_key": "dict(str, int)",
        "link_group_name": "str",
        "link_group_names_by_database_key": "dict(str, str)",
        "linked_records": "list[GsaRecordWithData]",
        "meta_datums": "list[GsaDataExportDatum]",
        "rolled_up_data": "list[GsaDataExportRollupDatum]",
        "target_database_guid": "str",
    }

    attribute_map: Dict[str, str] = {
        "datum_type": "datumType",
        "link_datum_type": "linkDatumType",
        "not_applicable": "notApplicable",
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "export_in_reversed_direction": "exportInReversedDirection",
        "link_attribute_type": "linkAttributeType",
        "link_group_identities_by_database_key": "linkGroupIdentitiesByDatabaseKey",
        "link_group_name": "linkGroupName",
        "link_group_names_by_database_key": "linkGroupNamesByDatabaseKey",
        "linked_records": "linkedRecords",
        "meta_datums": "metaDatums",
        "rolled_up_data": "rolledUpData",
        "target_database_guid": "targetDatabaseGuid",
    }

    subtype_mapping: Dict[str, str] = {
        "linkAttributeType": "GsaLinkAttributeType",
        "linkedRecords": "GsaRecordWithData",
        "rolledUpData": "GsaDataExportRollupDatum",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        datum_type: "GsaAttributeType" = GsaAttributeType.LINK,
        link_datum_type: "str" = "linkGroup",
        not_applicable: "str" = "applicable",
        attribute_guid: "Union[str, Unset_Type]" = Unset,
        attribute_identity: "Union[int, Unset_Type]" = Unset,
        export_in_reversed_direction: "Union[bool, Unset_Type]" = Unset,
        link_attribute_type: "Union[GsaLinkAttributeType, Unset_Type]" = Unset,
        link_group_identities_by_database_key: "Union[Dict[str, int], None, Unset_Type]" = Unset,
        link_group_name: "Union[str, None, Unset_Type]" = Unset,
        link_group_names_by_database_key: "Union[Dict[str, str], None, Unset_Type]" = Unset,
        linked_records: "Union[List[GsaRecordWithData], None, Unset_Type]" = Unset,
        meta_datums: "Union[List[GsaDataExportDatum], None, Unset_Type]" = Unset,
        rolled_up_data: "Union[List[GsaDataExportRollupDatum], None, Unset_Type]" = Unset,
        target_database_guid: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaDataExportLinkedRecordsDatum - a model defined in Swagger

        Parameters
        ----------
        datum_type: GsaAttributeType
        link_datum_type: str
        not_applicable: str
        attribute_guid: str, optional
        attribute_identity: int, optional
        export_in_reversed_direction: bool, optional
        link_attribute_type: GsaLinkAttributeType, optional
        link_group_identities_by_database_key: Dict[str, int], optional
        link_group_name: str, optional
        link_group_names_by_database_key: Dict[str, str], optional
        linked_records: List[GsaRecordWithData], optional
        meta_datums: List[GsaDataExportDatum], optional
        rolled_up_data: List[GsaDataExportRollupDatum], optional
        target_database_guid: str, optional
        """
        super().__init__(
            datum_type=datum_type,
            link_datum_type=link_datum_type,
            not_applicable=not_applicable,
            attribute_guid=attribute_guid,
            attribute_identity=attribute_identity,
            meta_datums=meta_datums,
        )
        self._link_group_name: Union[str, None, Unset_Type] = Unset
        self._link_attribute_type: Union[GsaLinkAttributeType, Unset_Type] = Unset
        self._export_in_reversed_direction: Union[bool, Unset_Type] = Unset
        self._target_database_guid: Union[str, None, Unset_Type] = Unset
        self._linked_records: Union[List[GsaRecordWithData], None, Unset_Type] = Unset
        self._link_group_names_by_database_key: Union[Dict[str, str], None, Unset_Type] = Unset
        self._link_group_identities_by_database_key: Union[Dict[str, int], None, Unset_Type] = Unset
        self._rolled_up_data: Union[List[GsaDataExportRollupDatum], None, Unset_Type] = Unset

        if link_group_name is not Unset:
            self.link_group_name = link_group_name
        if link_attribute_type is not Unset:
            self.link_attribute_type = link_attribute_type
        if export_in_reversed_direction is not Unset:
            self.export_in_reversed_direction = export_in_reversed_direction
        if target_database_guid is not Unset:
            self.target_database_guid = target_database_guid
        if linked_records is not Unset:
            self.linked_records = linked_records
        if link_group_names_by_database_key is not Unset:
            self.link_group_names_by_database_key = link_group_names_by_database_key
        if link_group_identities_by_database_key is not Unset:
            self.link_group_identities_by_database_key = link_group_identities_by_database_key
        if rolled_up_data is not Unset:
            self.rolled_up_data = rolled_up_data

    @property
    def link_group_name(self) -> "Union[str, None, Unset_Type]":
        """Gets the link_group_name of this GsaDataExportLinkedRecordsDatum.

        Returns
        -------
        Union[str, None, Unset_Type]
            The link_group_name of this GsaDataExportLinkedRecordsDatum.
        """
        return self._link_group_name

    @link_group_name.setter
    def link_group_name(self, link_group_name: "Union[str, None, Unset_Type]") -> None:
        """Sets the link_group_name of this GsaDataExportLinkedRecordsDatum.

        Parameters
        ----------
        link_group_name: Union[str, None, Unset_Type]
            The link_group_name of this GsaDataExportLinkedRecordsDatum.
        """
        self._link_group_name = link_group_name

    @property
    def link_attribute_type(self) -> "Union[GsaLinkAttributeType, Unset_Type]":
        """Gets the link_attribute_type of this GsaDataExportLinkedRecordsDatum.

        Returns
        -------
        Union[GsaLinkAttributeType, Unset_Type]
            The link_attribute_type of this GsaDataExportLinkedRecordsDatum.
        """
        return self._link_attribute_type

    @link_attribute_type.setter
    def link_attribute_type(
        self, link_attribute_type: "Union[GsaLinkAttributeType, Unset_Type]"
    ) -> None:
        """Sets the link_attribute_type of this GsaDataExportLinkedRecordsDatum.

        Parameters
        ----------
        link_attribute_type: Union[GsaLinkAttributeType, Unset_Type]
            The link_attribute_type of this GsaDataExportLinkedRecordsDatum.
        """
        # Field is not nullable
        if link_attribute_type is None:
            raise ValueError("Invalid value for 'link_attribute_type', must not be 'None'")
        self._link_attribute_type = link_attribute_type

    @property
    def export_in_reversed_direction(self) -> "Union[bool, Unset_Type]":
        """Gets the export_in_reversed_direction of this GsaDataExportLinkedRecordsDatum.

        Returns
        -------
        Union[bool, Unset_Type]
            The export_in_reversed_direction of this GsaDataExportLinkedRecordsDatum.
        """
        return self._export_in_reversed_direction

    @export_in_reversed_direction.setter
    def export_in_reversed_direction(
        self, export_in_reversed_direction: "Union[bool, Unset_Type]"
    ) -> None:
        """Sets the export_in_reversed_direction of this GsaDataExportLinkedRecordsDatum.

        Parameters
        ----------
        export_in_reversed_direction: Union[bool, Unset_Type]
            The export_in_reversed_direction of this GsaDataExportLinkedRecordsDatum.
        """
        # Field is not nullable
        if export_in_reversed_direction is None:
            raise ValueError("Invalid value for 'export_in_reversed_direction', must not be 'None'")
        self._export_in_reversed_direction = export_in_reversed_direction

    @property
    def target_database_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the target_database_guid of this GsaDataExportLinkedRecordsDatum.

        Returns
        -------
        Union[str, None, Unset_Type]
            The target_database_guid of this GsaDataExportLinkedRecordsDatum.
        """
        return self._target_database_guid

    @target_database_guid.setter
    def target_database_guid(self, target_database_guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the target_database_guid of this GsaDataExportLinkedRecordsDatum.

        Parameters
        ----------
        target_database_guid: Union[str, None, Unset_Type]
            The target_database_guid of this GsaDataExportLinkedRecordsDatum.
        """
        self._target_database_guid = target_database_guid

    @property
    def linked_records(self) -> "Union[List[GsaRecordWithData], None, Unset_Type]":
        """Gets the linked_records of this GsaDataExportLinkedRecordsDatum.

        Returns
        -------
        Union[List[GsaRecordWithData], None, Unset_Type]
            The linked_records of this GsaDataExportLinkedRecordsDatum.
        """
        return self._linked_records

    @linked_records.setter
    def linked_records(
        self, linked_records: "Union[List[GsaRecordWithData], None, Unset_Type]"
    ) -> None:
        """Sets the linked_records of this GsaDataExportLinkedRecordsDatum.

        Parameters
        ----------
        linked_records: Union[List[GsaRecordWithData], None, Unset_Type]
            The linked_records of this GsaDataExportLinkedRecordsDatum.
        """
        self._linked_records = linked_records

    @property
    def link_group_names_by_database_key(self) -> "Union[Dict[str, str], None, Unset_Type]":
        """Gets the link_group_names_by_database_key of this GsaDataExportLinkedRecordsDatum.

        Returns
        -------
        Union[Dict[str, str], None, Unset_Type]
            The link_group_names_by_database_key of this GsaDataExportLinkedRecordsDatum.
        """
        return self._link_group_names_by_database_key

    @link_group_names_by_database_key.setter
    def link_group_names_by_database_key(
        self, link_group_names_by_database_key: "Union[Dict[str, str], None, Unset_Type]"
    ) -> None:
        """Sets the link_group_names_by_database_key of this GsaDataExportLinkedRecordsDatum.

        Parameters
        ----------
        link_group_names_by_database_key: Union[Dict[str, str], None, Unset_Type]
            The link_group_names_by_database_key of this GsaDataExportLinkedRecordsDatum.
        """
        self._link_group_names_by_database_key = link_group_names_by_database_key

    @property
    def link_group_identities_by_database_key(self) -> "Union[Dict[str, int], None, Unset_Type]":
        """Gets the link_group_identities_by_database_key of this GsaDataExportLinkedRecordsDatum.

        Returns
        -------
        Union[Dict[str, int], None, Unset_Type]
            The link_group_identities_by_database_key of this GsaDataExportLinkedRecordsDatum.
        """
        return self._link_group_identities_by_database_key

    @link_group_identities_by_database_key.setter
    def link_group_identities_by_database_key(
        self, link_group_identities_by_database_key: "Union[Dict[str, int], None, Unset_Type]"
    ) -> None:
        """Sets the link_group_identities_by_database_key of this GsaDataExportLinkedRecordsDatum.

        Parameters
        ----------
        link_group_identities_by_database_key: Union[Dict[str, int], None, Unset_Type]
            The link_group_identities_by_database_key of this GsaDataExportLinkedRecordsDatum.
        """
        self._link_group_identities_by_database_key = link_group_identities_by_database_key

    @property
    def rolled_up_data(self) -> "Union[List[GsaDataExportRollupDatum], None, Unset_Type]":
        """Gets the rolled_up_data of this GsaDataExportLinkedRecordsDatum.

        Returns
        -------
        Union[List[GsaDataExportRollupDatum], None, Unset_Type]
            The rolled_up_data of this GsaDataExportLinkedRecordsDatum.
        """
        return self._rolled_up_data

    @rolled_up_data.setter
    def rolled_up_data(
        self, rolled_up_data: "Union[List[GsaDataExportRollupDatum], None, Unset_Type]"
    ) -> None:
        """Sets the rolled_up_data of this GsaDataExportLinkedRecordsDatum.

        Parameters
        ----------
        rolled_up_data: Union[List[GsaDataExportRollupDatum], None, Unset_Type]
            The rolled_up_data of this GsaDataExportLinkedRecordsDatum.
        """
        self._rolled_up_data = rolled_up_data

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
        if not isinstance(other, GsaDataExportLinkedRecordsDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other