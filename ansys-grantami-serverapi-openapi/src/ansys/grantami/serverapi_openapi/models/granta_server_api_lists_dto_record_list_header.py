"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase


if TYPE_CHECKING:
    from . import *


class GrantaServerApiListsDtoRecordListHeader(ModelBase):
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
    swagger_types = {
        "awaiting_approval": "bool",
        "created_timestamp": "datetime",
        "created_user": "GrantaServerApiListsDtoUserOrGroup",
        "identifier": "str",
        "internal_use": "bool",
        "is_revision": "bool",
        "last_modified_timestamp": "datetime",
        "last_modified_user": "GrantaServerApiListsDtoUserOrGroup",
        "metadata": "dict(str, dict(str, object))",
        "name": "str",
        "published": "bool",
        "description": "str",
        "notes": "str",
        "parent_record_list_identifier": "str",
        "published_timestamp": "datetime",
        "published_user": "GrantaServerApiListsDtoUserOrGroup",
    }

    attribute_map = {
        "awaiting_approval": "awaitingApproval",
        "created_timestamp": "createdTimestamp",
        "created_user": "createdUser",
        "identifier": "identifier",
        "internal_use": "internalUse",
        "is_revision": "isRevision",
        "last_modified_timestamp": "lastModifiedTimestamp",
        "last_modified_user": "lastModifiedUser",
        "metadata": "metadata",
        "name": "name",
        "published": "published",
        "description": "description",
        "notes": "notes",
        "parent_record_list_identifier": "parentRecordListIdentifier",
        "published_timestamp": "publishedTimestamp",
        "published_user": "publishedUser",
    }

    subtype_mapping = {
        "createdUser": "GrantaServerApiListsDtoUserOrGroup",
        "lastModifiedUser": "GrantaServerApiListsDtoUserOrGroup",
        "publishedUser": "GrantaServerApiListsDtoUserOrGroup",
    }

    discriminator = None

    def __init__(
        self,
        *,
        awaiting_approval: "bool",
        created_timestamp: "datetime",
        created_user: "GrantaServerApiListsDtoUserOrGroup",
        identifier: "str",
        internal_use: "bool",
        is_revision: "bool",
        last_modified_timestamp: "datetime",
        last_modified_user: "GrantaServerApiListsDtoUserOrGroup",
        metadata: "Dict[str, Dict[str, object]]",
        name: "str",
        published: "bool",
        description: "Optional[str]" = None,
        notes: "Optional[str]" = None,
        parent_record_list_identifier: "Optional[str]" = None,
        published_timestamp: "Optional[datetime]" = None,
        published_user: "Optional[GrantaServerApiListsDtoUserOrGroup]" = None,
    ) -> None:
        """GrantaServerApiListsDtoRecordListHeader - a model defined in Swagger

        Parameters
        ----------
            awaiting_approval: bool
            created_timestamp: datetime
            created_user: GrantaServerApiListsDtoUserOrGroup
            identifier: str
            internal_use: bool
            is_revision: bool
            last_modified_timestamp: datetime
            last_modified_user: GrantaServerApiListsDtoUserOrGroup
            metadata: Dict[str, Dict[str, object]]
            name: str
            published: bool
            description: str, optional
            notes: str, optional
            parent_record_list_identifier: str, optional
            published_timestamp: datetime, optional
            published_user: GrantaServerApiListsDtoUserOrGroup, optional
        """
        self._identifier = None
        self._metadata = None
        self._parent_record_list_identifier = None
        self._created_timestamp = None
        self._created_user = None
        self._last_modified_timestamp = None
        self._last_modified_user = None
        self._published_timestamp = None
        self._published_user = None
        self._is_revision = None
        self._name = None
        self._description = None
        self._notes = None
        self._published = None
        self._awaiting_approval = None
        self._internal_use = None

        self.identifier = identifier
        self.metadata = metadata
        if parent_record_list_identifier is not None:
            self.parent_record_list_identifier = parent_record_list_identifier
        self.created_timestamp = created_timestamp
        self.created_user = created_user
        self.last_modified_timestamp = last_modified_timestamp
        self.last_modified_user = last_modified_user
        if published_timestamp is not None:
            self.published_timestamp = published_timestamp
        if published_user is not None:
            self.published_user = published_user
        self.is_revision = is_revision
        self.name = name
        if description is not None:
            self.description = description
        if notes is not None:
            self.notes = notes
        self.published = published
        self.awaiting_approval = awaiting_approval
        self.internal_use = internal_use

    @property
    def identifier(self) -> "str":
        """Gets the identifier of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        str
            The identifier of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier: "str") -> None:
        """Sets the identifier of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        identifier: str
            The identifier of this GrantaServerApiListsDtoRecordListHeader.
        """
        if identifier is None:
            raise ValueError("Invalid value for 'identifier', must not be 'None'")
        self._identifier = identifier

    @property
    def metadata(self) -> "dict(str, dict(str, object))":
        """Gets the metadata of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        dict(str, dict(str, object))
            The metadata of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: "dict(str, dict(str, object))") -> None:
        """Sets the metadata of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        metadata: dict(str, dict(str, object))
            The metadata of this GrantaServerApiListsDtoRecordListHeader.
        """
        if metadata is None:
            raise ValueError("Invalid value for 'metadata', must not be 'None'")
        self._metadata = metadata

    @property
    def parent_record_list_identifier(self) -> "str":
        """Gets the parent_record_list_identifier of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        str
            The parent_record_list_identifier of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._parent_record_list_identifier

    @parent_record_list_identifier.setter
    def parent_record_list_identifier(
        self, parent_record_list_identifier: "str"
    ) -> None:
        """Sets the parent_record_list_identifier of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        parent_record_list_identifier: str
            The parent_record_list_identifier of this GrantaServerApiListsDtoRecordListHeader.
        """
        self._parent_record_list_identifier = parent_record_list_identifier

    @property
    def created_timestamp(self) -> "datetime":
        """Gets the created_timestamp of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        datetime
            The created_timestamp of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._created_timestamp

    @created_timestamp.setter
    def created_timestamp(self, created_timestamp: "datetime") -> None:
        """Sets the created_timestamp of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        created_timestamp: datetime
            The created_timestamp of this GrantaServerApiListsDtoRecordListHeader.
        """
        if created_timestamp is None:
            raise ValueError(
                "Invalid value for 'created_timestamp', must not be 'None'"
            )
        self._created_timestamp = created_timestamp

    @property
    def created_user(self) -> "GrantaServerApiListsDtoUserOrGroup":
        """Gets the created_user of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        GrantaServerApiListsDtoUserOrGroup
            The created_user of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._created_user

    @created_user.setter
    def created_user(self, created_user: "GrantaServerApiListsDtoUserOrGroup") -> None:
        """Sets the created_user of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        created_user: GrantaServerApiListsDtoUserOrGroup
            The created_user of this GrantaServerApiListsDtoRecordListHeader.
        """
        if created_user is None:
            raise ValueError("Invalid value for 'created_user', must not be 'None'")
        self._created_user = created_user

    @property
    def last_modified_timestamp(self) -> "datetime":
        """Gets the last_modified_timestamp of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        datetime
            The last_modified_timestamp of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._last_modified_timestamp

    @last_modified_timestamp.setter
    def last_modified_timestamp(self, last_modified_timestamp: "datetime") -> None:
        """Sets the last_modified_timestamp of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        last_modified_timestamp: datetime
            The last_modified_timestamp of this GrantaServerApiListsDtoRecordListHeader.
        """
        if last_modified_timestamp is None:
            raise ValueError(
                "Invalid value for 'last_modified_timestamp', must not be 'None'"
            )
        self._last_modified_timestamp = last_modified_timestamp

    @property
    def last_modified_user(self) -> "GrantaServerApiListsDtoUserOrGroup":
        """Gets the last_modified_user of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        GrantaServerApiListsDtoUserOrGroup
            The last_modified_user of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._last_modified_user

    @last_modified_user.setter
    def last_modified_user(
        self, last_modified_user: "GrantaServerApiListsDtoUserOrGroup"
    ) -> None:
        """Sets the last_modified_user of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        last_modified_user: GrantaServerApiListsDtoUserOrGroup
            The last_modified_user of this GrantaServerApiListsDtoRecordListHeader.
        """
        if last_modified_user is None:
            raise ValueError(
                "Invalid value for 'last_modified_user', must not be 'None'"
            )
        self._last_modified_user = last_modified_user

    @property
    def published_timestamp(self) -> "datetime":
        """Gets the published_timestamp of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        datetime
            The published_timestamp of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._published_timestamp

    @published_timestamp.setter
    def published_timestamp(self, published_timestamp: "datetime") -> None:
        """Sets the published_timestamp of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        published_timestamp: datetime
            The published_timestamp of this GrantaServerApiListsDtoRecordListHeader.
        """
        self._published_timestamp = published_timestamp

    @property
    def published_user(self) -> "GrantaServerApiListsDtoUserOrGroup":
        """Gets the published_user of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        GrantaServerApiListsDtoUserOrGroup
            The published_user of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._published_user

    @published_user.setter
    def published_user(
        self, published_user: "GrantaServerApiListsDtoUserOrGroup"
    ) -> None:
        """Sets the published_user of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        published_user: GrantaServerApiListsDtoUserOrGroup
            The published_user of this GrantaServerApiListsDtoRecordListHeader.
        """
        self._published_user = published_user

    @property
    def is_revision(self) -> "bool":
        """Gets the is_revision of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        bool
            The is_revision of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._is_revision

    @is_revision.setter
    def is_revision(self, is_revision: "bool") -> None:
        """Sets the is_revision of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        is_revision: bool
            The is_revision of this GrantaServerApiListsDtoRecordListHeader.
        """
        if is_revision is None:
            raise ValueError("Invalid value for 'is_revision', must not be 'None'")
        self._is_revision = is_revision

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        str
            The name of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiListsDtoRecordListHeader.
        """
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

    @property
    def description(self) -> "str":
        """Gets the description of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        str
            The description of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._description

    @description.setter
    def description(self, description: "str") -> None:
        """Sets the description of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        description: str
            The description of this GrantaServerApiListsDtoRecordListHeader.
        """
        self._description = description

    @property
    def notes(self) -> "str":
        """Gets the notes of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        str
            The notes of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._notes

    @notes.setter
    def notes(self, notes: "str") -> None:
        """Sets the notes of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        notes: str
            The notes of this GrantaServerApiListsDtoRecordListHeader.
        """
        self._notes = notes

    @property
    def published(self) -> "bool":
        """Gets the published of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        bool
            The published of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._published

    @published.setter
    def published(self, published: "bool") -> None:
        """Sets the published of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        published: bool
            The published of this GrantaServerApiListsDtoRecordListHeader.
        """
        if published is None:
            raise ValueError("Invalid value for 'published', must not be 'None'")
        self._published = published

    @property
    def awaiting_approval(self) -> "bool":
        """Gets the awaiting_approval of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        bool
            The awaiting_approval of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._awaiting_approval

    @awaiting_approval.setter
    def awaiting_approval(self, awaiting_approval: "bool") -> None:
        """Sets the awaiting_approval of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        awaiting_approval: bool
            The awaiting_approval of this GrantaServerApiListsDtoRecordListHeader.
        """
        if awaiting_approval is None:
            raise ValueError(
                "Invalid value for 'awaiting_approval', must not be 'None'"
            )
        self._awaiting_approval = awaiting_approval

    @property
    def internal_use(self) -> "bool":
        """Gets the internal_use of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        bool
            The internal_use of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._internal_use

    @internal_use.setter
    def internal_use(self, internal_use: "bool") -> None:
        """Sets the internal_use of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        internal_use: bool
            The internal_use of this GrantaServerApiListsDtoRecordListHeader.
        """
        if internal_use is None:
            raise ValueError("Invalid value for 'internal_use', must not be 'None'")
        self._internal_use = internal_use

    @classmethod
    def get_real_child_model(cls, data: ModelBase) -> str:
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
        if not isinstance(other, GrantaServerApiListsDtoRecordListHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
