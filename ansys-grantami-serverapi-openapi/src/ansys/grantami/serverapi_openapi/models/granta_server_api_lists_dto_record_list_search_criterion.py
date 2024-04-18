"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import (
    TYPE_CHECKING,
    Any,
    BinaryIO,
    Dict,
    List,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.models.granta_server_api_lists_dto_list_criterion import (
    GrantaServerApiListsDtoListCriterion,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiListsDtoRecordListSearchCriterion(
    GrantaServerApiListsDtoListCriterion
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
        "contains_records": "list[str]",
        "contains_records_in_databases": "list[str]",
        "contains_records_in_integration_schemas": "list[str]",
        "contains_records_in_tables": "list[str]",
        "is_awaiting_approval": "bool",
        "is_internal_use": "bool",
        "is_published": "bool",
        "is_revision": "bool",
        "name_contains": "str",
        "type": "str",
        "user_can_add_or_remove_items": "bool",
        "user_role": "GrantaServerApiListsDtoUserRole",
    }

    attribute_map: Dict[str, str] = {
        "contains_records": "containsRecords",
        "contains_records_in_databases": "containsRecordsInDatabases",
        "contains_records_in_integration_schemas": "containsRecordsInIntegrationSchemas",
        "contains_records_in_tables": "containsRecordsInTables",
        "is_awaiting_approval": "isAwaitingApproval",
        "is_internal_use": "isInternalUse",
        "is_published": "isPublished",
        "is_revision": "isRevision",
        "name_contains": "nameContains",
        "type": "type",
        "user_can_add_or_remove_items": "userCanAddOrRemoveItems",
        "user_role": "userRole",
    }

    subtype_mapping: Dict[str, str] = {
        "userRole": "GrantaServerApiListsDtoUserRole",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        contains_records: "Union[List[str], None, Unset_Type]" = Unset,
        contains_records_in_databases: "Union[List[str], None, Unset_Type]" = Unset,
        contains_records_in_integration_schemas: "Union[List[str], None, Unset_Type]" = Unset,
        contains_records_in_tables: "Union[List[str], None, Unset_Type]" = Unset,
        is_awaiting_approval: "Union[bool, None, Unset_Type]" = Unset,
        is_internal_use: "Union[bool, None, Unset_Type]" = Unset,
        is_published: "Union[bool, None, Unset_Type]" = Unset,
        is_revision: "Union[bool, None, Unset_Type]" = Unset,
        name_contains: "Union[str, None, Unset_Type]" = Unset,
        type: "str" = "recordList",
        user_can_add_or_remove_items: "Union[bool, None, Unset_Type]" = Unset,
        user_role: "Union[GrantaServerApiListsDtoUserRole, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiListsDtoRecordListSearchCriterion - a model defined in Swagger

        Parameters
        ----------
        contains_records: List[str], optional
        contains_records_in_databases: List[str], optional
        contains_records_in_integration_schemas: List[str], optional
        contains_records_in_tables: List[str], optional
        is_awaiting_approval: bool, optional
        is_internal_use: bool, optional
        is_published: bool, optional
        is_revision: bool, optional
        name_contains: str, optional
        type: str
        user_can_add_or_remove_items: bool, optional
        user_role: GrantaServerApiListsDtoUserRole, optional
        """
        super().__init__()
        self._name_contains: Union[str, None, Unset_Type] = Unset
        self._user_role: Union[GrantaServerApiListsDtoUserRole, Unset_Type] = Unset
        self._is_published: Union[bool, None, Unset_Type] = Unset
        self._is_awaiting_approval: Union[bool, None, Unset_Type] = Unset
        self._is_internal_use: Union[bool, None, Unset_Type] = Unset
        self._is_revision: Union[bool, None, Unset_Type] = Unset
        self._contains_records_in_databases: Union[List[str], None, Unset_Type] = Unset
        self._contains_records_in_integration_schemas: Union[
            List[str], None, Unset_Type
        ] = Unset
        self._contains_records_in_tables: Union[List[str], None, Unset_Type] = Unset
        self._contains_records: Union[List[str], None, Unset_Type] = Unset
        self._user_can_add_or_remove_items: Union[bool, None, Unset_Type] = Unset
        self._type: str

        if name_contains is not Unset:
            self.name_contains = name_contains
        if user_role is not Unset:
            self.user_role = user_role
        if is_published is not Unset:
            self.is_published = is_published
        if is_awaiting_approval is not Unset:
            self.is_awaiting_approval = is_awaiting_approval
        if is_internal_use is not Unset:
            self.is_internal_use = is_internal_use
        if is_revision is not Unset:
            self.is_revision = is_revision
        if contains_records_in_databases is not Unset:
            self.contains_records_in_databases = contains_records_in_databases
        if contains_records_in_integration_schemas is not Unset:
            self.contains_records_in_integration_schemas = (
                contains_records_in_integration_schemas
            )
        if contains_records_in_tables is not Unset:
            self.contains_records_in_tables = contains_records_in_tables
        if contains_records is not Unset:
            self.contains_records = contains_records
        if user_can_add_or_remove_items is not Unset:
            self.user_can_add_or_remove_items = user_can_add_or_remove_items
        self.type = type

    @property
    def name_contains(self) -> "Union[str, None, Unset_Type]":
        """Gets the name_contains of this GrantaServerApiListsDtoRecordListSearchCriterion.

        Returns
        -------
        Union[str, None, Unset_Type]
            The name_contains of this GrantaServerApiListsDtoRecordListSearchCriterion.
        """
        return self._name_contains

    @name_contains.setter
    def name_contains(self, name_contains: "Union[str, None, Unset_Type]") -> None:
        """Sets the name_contains of this GrantaServerApiListsDtoRecordListSearchCriterion.

        Parameters
        ----------
        name_contains: Union[str, None, Unset_Type]
            The name_contains of this GrantaServerApiListsDtoRecordListSearchCriterion.
        """
        self._name_contains = name_contains

    @property
    def user_role(self) -> "Union[GrantaServerApiListsDtoUserRole, Unset_Type]":
        """Gets the user_role of this GrantaServerApiListsDtoRecordListSearchCriterion.

        Returns
        -------
        Union[GrantaServerApiListsDtoUserRole, Unset_Type]
            The user_role of this GrantaServerApiListsDtoRecordListSearchCriterion.
        """
        return self._user_role

    @user_role.setter
    def user_role(
        self, user_role: "Union[GrantaServerApiListsDtoUserRole, Unset_Type]"
    ) -> None:
        """Sets the user_role of this GrantaServerApiListsDtoRecordListSearchCriterion.

        Parameters
        ----------
        user_role: Union[GrantaServerApiListsDtoUserRole, Unset_Type]
            The user_role of this GrantaServerApiListsDtoRecordListSearchCriterion.
        """
        # Field is not nullable
        if user_role is None:
            raise ValueError("Invalid value for 'user_role', must not be 'None'")
        self._user_role = user_role

    @property
    def is_published(self) -> "Union[bool, None, Unset_Type]":
        """Gets the is_published of this GrantaServerApiListsDtoRecordListSearchCriterion.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The is_published of this GrantaServerApiListsDtoRecordListSearchCriterion.
        """
        return self._is_published

    @is_published.setter
    def is_published(self, is_published: "Union[bool, None, Unset_Type]") -> None:
        """Sets the is_published of this GrantaServerApiListsDtoRecordListSearchCriterion.

        Parameters
        ----------
        is_published: Union[bool, None, Unset_Type]
            The is_published of this GrantaServerApiListsDtoRecordListSearchCriterion.
        """
        self._is_published = is_published

    @property
    def is_awaiting_approval(self) -> "Union[bool, None, Unset_Type]":
        """Gets the is_awaiting_approval of this GrantaServerApiListsDtoRecordListSearchCriterion.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The is_awaiting_approval of this GrantaServerApiListsDtoRecordListSearchCriterion.
        """
        return self._is_awaiting_approval

    @is_awaiting_approval.setter
    def is_awaiting_approval(
        self, is_awaiting_approval: "Union[bool, None, Unset_Type]"
    ) -> None:
        """Sets the is_awaiting_approval of this GrantaServerApiListsDtoRecordListSearchCriterion.

        Parameters
        ----------
        is_awaiting_approval: Union[bool, None, Unset_Type]
            The is_awaiting_approval of this GrantaServerApiListsDtoRecordListSearchCriterion.
        """
        self._is_awaiting_approval = is_awaiting_approval

    @property
    def is_internal_use(self) -> "Union[bool, None, Unset_Type]":
        """Gets the is_internal_use of this GrantaServerApiListsDtoRecordListSearchCriterion.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The is_internal_use of this GrantaServerApiListsDtoRecordListSearchCriterion.
        """
        return self._is_internal_use

    @is_internal_use.setter
    def is_internal_use(self, is_internal_use: "Union[bool, None, Unset_Type]") -> None:
        """Sets the is_internal_use of this GrantaServerApiListsDtoRecordListSearchCriterion.

        Parameters
        ----------
        is_internal_use: Union[bool, None, Unset_Type]
            The is_internal_use of this GrantaServerApiListsDtoRecordListSearchCriterion.
        """
        self._is_internal_use = is_internal_use

    @property
    def is_revision(self) -> "Union[bool, None, Unset_Type]":
        """Gets the is_revision of this GrantaServerApiListsDtoRecordListSearchCriterion.
        Restrict to record lists that are (non discarded) revisions.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The is_revision of this GrantaServerApiListsDtoRecordListSearchCriterion.
        """
        return self._is_revision

    @is_revision.setter
    def is_revision(self, is_revision: "Union[bool, None, Unset_Type]") -> None:
        """Sets the is_revision of this GrantaServerApiListsDtoRecordListSearchCriterion.
        Restrict to record lists that are (non discarded) revisions.

        Parameters
        ----------
        is_revision: Union[bool, None, Unset_Type]
            The is_revision of this GrantaServerApiListsDtoRecordListSearchCriterion.
        """
        self._is_revision = is_revision

    @property
    def contains_records_in_databases(self) -> "Union[List[str], None, Unset_Type]":
        """Gets the contains_records_in_databases of this GrantaServerApiListsDtoRecordListSearchCriterion.
        Limits results to lists containing records in any of of the specified databases

        Returns
        -------
        Union[List[str], None, Unset_Type]
            The contains_records_in_databases of this GrantaServerApiListsDtoRecordListSearchCriterion.
        """
        return self._contains_records_in_databases

    @contains_records_in_databases.setter
    def contains_records_in_databases(
        self, contains_records_in_databases: "Union[List[str], None, Unset_Type]"
    ) -> None:
        """Sets the contains_records_in_databases of this GrantaServerApiListsDtoRecordListSearchCriterion.
        Limits results to lists containing records in any of of the specified databases

        Parameters
        ----------
        contains_records_in_databases: Union[List[str], None, Unset_Type]
            The contains_records_in_databases of this GrantaServerApiListsDtoRecordListSearchCriterion.
        """
        self._contains_records_in_databases = contains_records_in_databases

    @property
    def contains_records_in_integration_schemas(
        self,
    ) -> "Union[List[str], None, Unset_Type]":
        """Gets the contains_records_in_integration_schemas of this GrantaServerApiListsDtoRecordListSearchCriterion.
        Limits results to lists containing records in any of the specified integration schemas

        Returns
        -------
        Union[List[str], None, Unset_Type]
            The contains_records_in_integration_schemas of this GrantaServerApiListsDtoRecordListSearchCriterion.
        """
        return self._contains_records_in_integration_schemas

    @contains_records_in_integration_schemas.setter
    def contains_records_in_integration_schemas(
        self,
        contains_records_in_integration_schemas: "Union[List[str], None, Unset_Type]",
    ) -> None:
        """Sets the contains_records_in_integration_schemas of this GrantaServerApiListsDtoRecordListSearchCriterion.
        Limits results to lists containing records in any of the specified integration schemas

        Parameters
        ----------
        contains_records_in_integration_schemas: Union[List[str], None, Unset_Type]
            The contains_records_in_integration_schemas of this GrantaServerApiListsDtoRecordListSearchCriterion.
        """
        self._contains_records_in_integration_schemas = (
            contains_records_in_integration_schemas
        )

    @property
    def contains_records_in_tables(self) -> "Union[List[str], None, Unset_Type]":
        """Gets the contains_records_in_tables of this GrantaServerApiListsDtoRecordListSearchCriterion.
        Limits results to lists containing records in any of the specified tables

        Returns
        -------
        Union[List[str], None, Unset_Type]
            The contains_records_in_tables of this GrantaServerApiListsDtoRecordListSearchCriterion.
        """
        return self._contains_records_in_tables

    @contains_records_in_tables.setter
    def contains_records_in_tables(
        self, contains_records_in_tables: "Union[List[str], None, Unset_Type]"
    ) -> None:
        """Sets the contains_records_in_tables of this GrantaServerApiListsDtoRecordListSearchCriterion.
        Limits results to lists containing records in any of the specified tables

        Parameters
        ----------
        contains_records_in_tables: Union[List[str], None, Unset_Type]
            The contains_records_in_tables of this GrantaServerApiListsDtoRecordListSearchCriterion.
        """
        self._contains_records_in_tables = contains_records_in_tables

    @property
    def contains_records(self) -> "Union[List[str], None, Unset_Type]":
        """Gets the contains_records of this GrantaServerApiListsDtoRecordListSearchCriterion.
        Limits results to lists containing any of the given records

        Returns
        -------
        Union[List[str], None, Unset_Type]
            The contains_records of this GrantaServerApiListsDtoRecordListSearchCriterion.
        """
        return self._contains_records

    @contains_records.setter
    def contains_records(
        self, contains_records: "Union[List[str], None, Unset_Type]"
    ) -> None:
        """Sets the contains_records of this GrantaServerApiListsDtoRecordListSearchCriterion.
        Limits results to lists containing any of the given records

        Parameters
        ----------
        contains_records: Union[List[str], None, Unset_Type]
            The contains_records of this GrantaServerApiListsDtoRecordListSearchCriterion.
        """
        self._contains_records = contains_records

    @property
    def user_can_add_or_remove_items(self) -> "Union[bool, None, Unset_Type]":
        """Gets the user_can_add_or_remove_items of this GrantaServerApiListsDtoRecordListSearchCriterion.
        Limits results to lists where the current user can add or remove items.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The user_can_add_or_remove_items of this GrantaServerApiListsDtoRecordListSearchCriterion.
        """
        return self._user_can_add_or_remove_items

    @user_can_add_or_remove_items.setter
    def user_can_add_or_remove_items(
        self, user_can_add_or_remove_items: "Union[bool, None, Unset_Type]"
    ) -> None:
        """Sets the user_can_add_or_remove_items of this GrantaServerApiListsDtoRecordListSearchCriterion.
        Limits results to lists where the current user can add or remove items.

        Parameters
        ----------
        user_can_add_or_remove_items: Union[bool, None, Unset_Type]
            The user_can_add_or_remove_items of this GrantaServerApiListsDtoRecordListSearchCriterion.
        """
        self._user_can_add_or_remove_items = user_can_add_or_remove_items

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiListsDtoRecordListSearchCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiListsDtoRecordListSearchCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiListsDtoRecordListSearchCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiListsDtoRecordListSearchCriterion.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

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
        if not isinstance(other, GrantaServerApiListsDtoRecordListSearchCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
