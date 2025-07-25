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


class GrantaServerApiListsDtoRecordListHeader(ModelBase):
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
        "awaiting_approval": "bool",
        "created_timestamp": "datetime",
        "created_user": "GrantaServerApiListsDtoUserOrGroup",
        "description": "str",
        "identifier": "str",
        "internal_use": "bool",
        "is_revision": "bool",
        "last_modified_timestamp": "datetime",
        "last_modified_user": "GrantaServerApiListsDtoUserOrGroup",
        "metadata": "dict(str, dict(str, object))",
        "name": "str",
        "notes": "str",
        "parent_record_list_identifier": "str",
        "published": "bool",
        "published_timestamp": "datetime",
        "published_user": "GrantaServerApiListsDtoUserOrGroup",
    }

    attribute_map: dict[str, str] = {
        "awaiting_approval": "awaitingApproval",
        "created_timestamp": "createdTimestamp",
        "created_user": "createdUser",
        "description": "description",
        "identifier": "identifier",
        "internal_use": "internalUse",
        "is_revision": "isRevision",
        "last_modified_timestamp": "lastModifiedTimestamp",
        "last_modified_user": "lastModifiedUser",
        "metadata": "metadata",
        "name": "name",
        "notes": "notes",
        "parent_record_list_identifier": "parentRecordListIdentifier",
        "published": "published",
        "published_timestamp": "publishedTimestamp",
        "published_user": "publishedUser",
    }

    subtype_mapping: dict[str, str] = {
        "createdUser": "GrantaServerApiListsDtoUserOrGroup",
        "lastModifiedUser": "GrantaServerApiListsDtoUserOrGroup",
        "publishedUser": "GrantaServerApiListsDtoUserOrGroup",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        awaiting_approval: "bool | Unset_Type" = Unset,
        created_timestamp: "datetime | Unset_Type" = Unset,
        created_user: "GrantaServerApiListsDtoUserOrGroup | Unset_Type" = Unset,
        description: "str | None | Unset_Type" = Unset,
        identifier: "str | Unset_Type" = Unset,
        internal_use: "bool | Unset_Type" = Unset,
        is_revision: "bool | Unset_Type" = Unset,
        last_modified_timestamp: "datetime | Unset_Type" = Unset,
        last_modified_user: "GrantaServerApiListsDtoUserOrGroup | Unset_Type" = Unset,
        metadata: "dict[str, dict[str, object]] | None | Unset_Type" = Unset,
        name: "str | None | Unset_Type" = Unset,
        notes: "str | None | Unset_Type" = Unset,
        parent_record_list_identifier: "str | None | Unset_Type" = Unset,
        published: "bool | Unset_Type" = Unset,
        published_timestamp: "datetime | None | Unset_Type" = Unset,
        published_user: "GrantaServerApiListsDtoUserOrGroup | Unset_Type" = Unset,
    ) -> None:
        """GrantaServerApiListsDtoRecordListHeader - a model defined in Swagger

        Parameters
        ----------
        awaiting_approval: bool, optional
        created_timestamp: datetime, optional
        created_user: GrantaServerApiListsDtoUserOrGroup, optional
        description: str | None, optional
        identifier: str, optional
        internal_use: bool, optional
        is_revision: bool, optional
        last_modified_timestamp: datetime, optional
        last_modified_user: GrantaServerApiListsDtoUserOrGroup, optional
        metadata: dict[str, dict[str, object]] | None, optional
        name: str | None, optional
        notes: str | None, optional
        parent_record_list_identifier: str | None, optional
        published: bool, optional
        published_timestamp: datetime | None, optional
        published_user: GrantaServerApiListsDtoUserOrGroup, optional
        """
        self._identifier: str | Unset_Type = Unset
        self._metadata: dict[str, dict[str, object]] | None | Unset_Type = Unset
        self._parent_record_list_identifier: str | None | Unset_Type = Unset
        self._created_timestamp: datetime | Unset_Type = Unset
        self._created_user: GrantaServerApiListsDtoUserOrGroup | Unset_Type = Unset
        self._last_modified_timestamp: datetime | Unset_Type = Unset
        self._last_modified_user: GrantaServerApiListsDtoUserOrGroup | Unset_Type = Unset
        self._published_timestamp: datetime | None | Unset_Type = Unset
        self._published_user: GrantaServerApiListsDtoUserOrGroup | Unset_Type = Unset
        self._is_revision: bool | Unset_Type = Unset
        self._name: str | None | Unset_Type = Unset
        self._description: str | None | Unset_Type = Unset
        self._notes: str | None | Unset_Type = Unset
        self._published: bool | Unset_Type = Unset
        self._awaiting_approval: bool | Unset_Type = Unset
        self._internal_use: bool | Unset_Type = Unset

        if identifier is not Unset:
            self.identifier = identifier
        if metadata is not Unset:
            self.metadata = metadata
        if parent_record_list_identifier is not Unset:
            self.parent_record_list_identifier = parent_record_list_identifier
        if created_timestamp is not Unset:
            self.created_timestamp = created_timestamp
        if created_user is not Unset:
            self.created_user = created_user
        if last_modified_timestamp is not Unset:
            self.last_modified_timestamp = last_modified_timestamp
        if last_modified_user is not Unset:
            self.last_modified_user = last_modified_user
        if published_timestamp is not Unset:
            self.published_timestamp = published_timestamp
        if published_user is not Unset:
            self.published_user = published_user
        if is_revision is not Unset:
            self.is_revision = is_revision
        if name is not Unset:
            self.name = name
        if description is not Unset:
            self.description = description
        if notes is not Unset:
            self.notes = notes
        if published is not Unset:
            self.published = published
        if awaiting_approval is not Unset:
            self.awaiting_approval = awaiting_approval
        if internal_use is not Unset:
            self.internal_use = internal_use

    @property
    def identifier(self) -> "str | Unset_Type":
        """Gets the identifier of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        str | Unset_Type
            The identifier of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier: "str | Unset_Type") -> None:
        """Sets the identifier of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        identifier: str | Unset_Type
            The identifier of this GrantaServerApiListsDtoRecordListHeader.
        """
        # Field is not nullable
        if identifier is None:
            raise ValueError("Invalid value for 'identifier', must not be 'None'")
        self._identifier = identifier

    @property
    def metadata(self) -> "dict[str, dict[str, object]] | None | Unset_Type":
        """Gets the metadata of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        dict[str, dict[str, object]] | None | Unset_Type
            The metadata of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: "dict[str, dict[str, object]] | None | Unset_Type") -> None:
        """Sets the metadata of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        metadata: dict[str, dict[str, object]] | None | Unset_Type
            The metadata of this GrantaServerApiListsDtoRecordListHeader.
        """
        self._metadata = metadata

    @property
    def parent_record_list_identifier(self) -> "str | None | Unset_Type":
        """Gets the parent_record_list_identifier of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        str | None | Unset_Type
            The parent_record_list_identifier of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._parent_record_list_identifier

    @parent_record_list_identifier.setter
    def parent_record_list_identifier(
        self, parent_record_list_identifier: "str | None | Unset_Type"
    ) -> None:
        """Sets the parent_record_list_identifier of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        parent_record_list_identifier: str | None | Unset_Type
            The parent_record_list_identifier of this GrantaServerApiListsDtoRecordListHeader.
        """
        self._parent_record_list_identifier = parent_record_list_identifier

    @property
    def created_timestamp(self) -> "datetime | Unset_Type":
        """Gets the created_timestamp of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        datetime | Unset_Type
            The created_timestamp of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._created_timestamp

    @created_timestamp.setter
    def created_timestamp(self, created_timestamp: "datetime | Unset_Type") -> None:
        """Sets the created_timestamp of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        created_timestamp: datetime | Unset_Type
            The created_timestamp of this GrantaServerApiListsDtoRecordListHeader.
        """
        # Field is not nullable
        if created_timestamp is None:
            raise ValueError("Invalid value for 'created_timestamp', must not be 'None'")
        self._created_timestamp = created_timestamp

    @property
    def created_user(self) -> "GrantaServerApiListsDtoUserOrGroup | Unset_Type":
        """Gets the created_user of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        GrantaServerApiListsDtoUserOrGroup | Unset_Type
            The created_user of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._created_user

    @created_user.setter
    def created_user(self, created_user: "GrantaServerApiListsDtoUserOrGroup | Unset_Type") -> None:
        """Sets the created_user of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        created_user: GrantaServerApiListsDtoUserOrGroup | Unset_Type
            The created_user of this GrantaServerApiListsDtoRecordListHeader.
        """
        # Field is not nullable
        if created_user is None:
            raise ValueError("Invalid value for 'created_user', must not be 'None'")
        self._created_user = created_user

    @property
    def last_modified_timestamp(self) -> "datetime | Unset_Type":
        """Gets the last_modified_timestamp of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        datetime | Unset_Type
            The last_modified_timestamp of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._last_modified_timestamp

    @last_modified_timestamp.setter
    def last_modified_timestamp(self, last_modified_timestamp: "datetime | Unset_Type") -> None:
        """Sets the last_modified_timestamp of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        last_modified_timestamp: datetime | Unset_Type
            The last_modified_timestamp of this GrantaServerApiListsDtoRecordListHeader.
        """
        # Field is not nullable
        if last_modified_timestamp is None:
            raise ValueError("Invalid value for 'last_modified_timestamp', must not be 'None'")
        self._last_modified_timestamp = last_modified_timestamp

    @property
    def last_modified_user(self) -> "GrantaServerApiListsDtoUserOrGroup | Unset_Type":
        """Gets the last_modified_user of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        GrantaServerApiListsDtoUserOrGroup | Unset_Type
            The last_modified_user of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._last_modified_user

    @last_modified_user.setter
    def last_modified_user(
        self, last_modified_user: "GrantaServerApiListsDtoUserOrGroup | Unset_Type"
    ) -> None:
        """Sets the last_modified_user of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        last_modified_user: GrantaServerApiListsDtoUserOrGroup | Unset_Type
            The last_modified_user of this GrantaServerApiListsDtoRecordListHeader.
        """
        # Field is not nullable
        if last_modified_user is None:
            raise ValueError("Invalid value for 'last_modified_user', must not be 'None'")
        self._last_modified_user = last_modified_user

    @property
    def published_timestamp(self) -> "datetime | None | Unset_Type":
        """Gets the published_timestamp of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        datetime | None | Unset_Type
            The published_timestamp of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._published_timestamp

    @published_timestamp.setter
    def published_timestamp(self, published_timestamp: "datetime | None | Unset_Type") -> None:
        """Sets the published_timestamp of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        published_timestamp: datetime | None | Unset_Type
            The published_timestamp of this GrantaServerApiListsDtoRecordListHeader.
        """
        self._published_timestamp = published_timestamp

    @property
    def published_user(self) -> "GrantaServerApiListsDtoUserOrGroup | Unset_Type":
        """Gets the published_user of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        GrantaServerApiListsDtoUserOrGroup | Unset_Type
            The published_user of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._published_user

    @published_user.setter
    def published_user(
        self, published_user: "GrantaServerApiListsDtoUserOrGroup | Unset_Type"
    ) -> None:
        """Sets the published_user of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        published_user: GrantaServerApiListsDtoUserOrGroup | Unset_Type
            The published_user of this GrantaServerApiListsDtoRecordListHeader.
        """
        # Field is not nullable
        if published_user is None:
            raise ValueError("Invalid value for 'published_user', must not be 'None'")
        self._published_user = published_user

    @property
    def is_revision(self) -> "bool | Unset_Type":
        """Gets the is_revision of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        bool | Unset_Type
            The is_revision of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._is_revision

    @is_revision.setter
    def is_revision(self, is_revision: "bool | Unset_Type") -> None:
        """Sets the is_revision of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        is_revision: bool | Unset_Type
            The is_revision of this GrantaServerApiListsDtoRecordListHeader.
        """
        # Field is not nullable
        if is_revision is None:
            raise ValueError("Invalid value for 'is_revision', must not be 'None'")
        self._is_revision = is_revision

    @property
    def name(self) -> "str | None | Unset_Type":
        """Gets the name of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        str | None | Unset_Type
            The name of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._name

    @name.setter
    def name(self, name: "str | None | Unset_Type") -> None:
        """Sets the name of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        name: str | None | Unset_Type
            The name of this GrantaServerApiListsDtoRecordListHeader.
        """
        self._name = name

    @property
    def description(self) -> "str | None | Unset_Type":
        """Gets the description of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        str | None | Unset_Type
            The description of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._description

    @description.setter
    def description(self, description: "str | None | Unset_Type") -> None:
        """Sets the description of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        description: str | None | Unset_Type
            The description of this GrantaServerApiListsDtoRecordListHeader.
        """
        self._description = description

    @property
    def notes(self) -> "str | None | Unset_Type":
        """Gets the notes of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        str | None | Unset_Type
            The notes of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._notes

    @notes.setter
    def notes(self, notes: "str | None | Unset_Type") -> None:
        """Sets the notes of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        notes: str | None | Unset_Type
            The notes of this GrantaServerApiListsDtoRecordListHeader.
        """
        self._notes = notes

    @property
    def published(self) -> "bool | Unset_Type":
        """Gets the published of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        bool | Unset_Type
            The published of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._published

    @published.setter
    def published(self, published: "bool | Unset_Type") -> None:
        """Sets the published of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        published: bool | Unset_Type
            The published of this GrantaServerApiListsDtoRecordListHeader.
        """
        # Field is not nullable
        if published is None:
            raise ValueError("Invalid value for 'published', must not be 'None'")
        self._published = published

    @property
    def awaiting_approval(self) -> "bool | Unset_Type":
        """Gets the awaiting_approval of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        bool | Unset_Type
            The awaiting_approval of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._awaiting_approval

    @awaiting_approval.setter
    def awaiting_approval(self, awaiting_approval: "bool | Unset_Type") -> None:
        """Sets the awaiting_approval of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        awaiting_approval: bool | Unset_Type
            The awaiting_approval of this GrantaServerApiListsDtoRecordListHeader.
        """
        # Field is not nullable
        if awaiting_approval is None:
            raise ValueError("Invalid value for 'awaiting_approval', must not be 'None'")
        self._awaiting_approval = awaiting_approval

    @property
    def internal_use(self) -> "bool | Unset_Type":
        """Gets the internal_use of this GrantaServerApiListsDtoRecordListHeader.

        Returns
        -------
        bool | Unset_Type
            The internal_use of this GrantaServerApiListsDtoRecordListHeader.
        """
        return self._internal_use

    @internal_use.setter
    def internal_use(self, internal_use: "bool | Unset_Type") -> None:
        """Sets the internal_use of this GrantaServerApiListsDtoRecordListHeader.

        Parameters
        ----------
        internal_use: bool | Unset_Type
            The internal_use of this GrantaServerApiListsDtoRecordListHeader.
        """
        # Field is not nullable
        if internal_use is None:
            raise ValueError("Invalid value for 'internal_use', must not be 'None'")
        self._internal_use = internal_use

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
        if not isinstance(other, GrantaServerApiListsDtoRecordListHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
