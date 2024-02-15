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
    Dict,
    List,
    BinaryIO,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSelectionSearchesSelectionSearch(ModelBase):  # type: ignore[misc]
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
        "created_timestamp": "datetime",
        "created_user_or_group": "GrantaServerApiSelectionSearchesUserOrGroup",
        "criteria": "str",
        "current_user_access_info": "dict(str, dict(str, bool))",
        "description": "str",
        "explore_config": "str",
        "last_modified_timestamp": "datetime",
        "last_modified_user_or_group": "GrantaServerApiSelectionSearchesUserOrGroup",
        "name": "str",
        "notes": "str",
        "search_identifier": "str",
    }

    attribute_map: Dict[str, str] = {
        "created_timestamp": "createdTimestamp",
        "created_user_or_group": "createdUserOrGroup",
        "criteria": "criteria",
        "current_user_access_info": "currentUserAccessInfo",
        "description": "description",
        "explore_config": "exploreConfig",
        "last_modified_timestamp": "lastModifiedTimestamp",
        "last_modified_user_or_group": "lastModifiedUserOrGroup",
        "name": "name",
        "notes": "notes",
        "search_identifier": "searchIdentifier",
    }

    subtype_mapping: Dict[str, str] = {
        "createdUserOrGroup": "GrantaServerApiSelectionSearchesUserOrGroup",
        "lastModifiedUserOrGroup": "GrantaServerApiSelectionSearchesUserOrGroup",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        created_timestamp: "Optional[datetime]" = None,
        created_user_or_group: "Optional[GrantaServerApiSelectionSearchesUserOrGroup]" = None,
        criteria: "Optional[str]" = None,
        current_user_access_info: "Optional[Dict[str, Dict[str, bool]]]" = None,
        description: "Optional[str]" = None,
        explore_config: "Optional[str]" = None,
        last_modified_timestamp: "Optional[datetime]" = None,
        last_modified_user_or_group: "Optional[GrantaServerApiSelectionSearchesUserOrGroup]" = None,
        name: "Optional[str]" = None,
        notes: "Optional[str]" = None,
        search_identifier: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiSelectionSearchesSelectionSearch - a model defined in Swagger

        Parameters
        ----------
            created_timestamp: datetime, optional
            created_user_or_group: GrantaServerApiSelectionSearchesUserOrGroup, optional
            criteria: str, optional
            current_user_access_info: Dict[str, Dict[str, bool]], optional
            description: str, optional
            explore_config: str, optional
            last_modified_timestamp: datetime, optional
            last_modified_user_or_group: GrantaServerApiSelectionSearchesUserOrGroup, optional
            name: str, optional
            notes: str, optional
            search_identifier: str, optional
        """
        self._search_identifier = None
        self._name = None
        self._description = None
        self._notes = None
        self._current_user_access_info = None
        self._criteria = None
        self._explore_config = None
        self._created_timestamp = None
        self._created_user_or_group = None
        self._last_modified_timestamp = None
        self._last_modified_user_or_group = None

        if search_identifier is not None:
            self.search_identifier = search_identifier
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if notes is not None:
            self.notes = notes
        if current_user_access_info is not None:
            self.current_user_access_info = current_user_access_info
        if criteria is not None:
            self.criteria = criteria
        if explore_config is not None:
            self.explore_config = explore_config
        if created_timestamp is not None:
            self.created_timestamp = created_timestamp
        if created_user_or_group is not None:
            self.created_user_or_group = created_user_or_group
        if last_modified_timestamp is not None:
            self.last_modified_timestamp = last_modified_timestamp
        if last_modified_user_or_group is not None:
            self.last_modified_user_or_group = last_modified_user_or_group

    @property
    def search_identifier(self) -> "Optional[str]":
        """Gets the search_identifier of this GrantaServerApiSelectionSearchesSelectionSearch.

        Returns
        -------
        str
            The search_identifier of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        return self._search_identifier

    @search_identifier.setter
    def search_identifier(self, search_identifier: "Optional[str]") -> None:
        """Sets the search_identifier of this GrantaServerApiSelectionSearchesSelectionSearch.

        Parameters
        ----------
        search_identifier: str
            The search_identifier of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        self._search_identifier = search_identifier

    @property
    def name(self) -> "Optional[str]":
        """Gets the name of this GrantaServerApiSelectionSearchesSelectionSearch.

        Returns
        -------
        str
            The name of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        return self._name

    @name.setter
    def name(self, name: "Optional[str]") -> None:
        """Sets the name of this GrantaServerApiSelectionSearchesSelectionSearch.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        self._name = name

    @property
    def description(self) -> "Optional[str]":
        """Gets the description of this GrantaServerApiSelectionSearchesSelectionSearch.

        Returns
        -------
        str
            The description of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        return self._description

    @description.setter
    def description(self, description: "Optional[str]") -> None:
        """Sets the description of this GrantaServerApiSelectionSearchesSelectionSearch.

        Parameters
        ----------
        description: str
            The description of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        self._description = description

    @property
    def notes(self) -> "Optional[str]":
        """Gets the notes of this GrantaServerApiSelectionSearchesSelectionSearch.

        Returns
        -------
        str
            The notes of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        return self._notes

    @notes.setter
    def notes(self, notes: "Optional[str]") -> None:
        """Sets the notes of this GrantaServerApiSelectionSearchesSelectionSearch.

        Parameters
        ----------
        notes: str
            The notes of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        self._notes = notes

    @property
    def current_user_access_info(self) -> "Optional[Dict[str, Dict[str, bool]]]":
        """Gets the current_user_access_info of this GrantaServerApiSelectionSearchesSelectionSearch.

        Returns
        -------
        dict(str, dict(str, bool))
            The current_user_access_info of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        return self._current_user_access_info

    @current_user_access_info.setter
    def current_user_access_info(
        self, current_user_access_info: "Optional[Dict[str, Dict[str, bool]]]"
    ) -> None:
        """Sets the current_user_access_info of this GrantaServerApiSelectionSearchesSelectionSearch.

        Parameters
        ----------
        current_user_access_info: Dict[str, Dict[str, bool]]
            The current_user_access_info of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        self._current_user_access_info = current_user_access_info

    @property
    def criteria(self) -> "Optional[str]":
        """Gets the criteria of this GrantaServerApiSelectionSearchesSelectionSearch.

        Returns
        -------
        str
            The criteria of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria: "Optional[str]") -> None:
        """Sets the criteria of this GrantaServerApiSelectionSearchesSelectionSearch.

        Parameters
        ----------
        criteria: str
            The criteria of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        self._criteria = criteria

    @property
    def explore_config(self) -> "Optional[str]":
        """Gets the explore_config of this GrantaServerApiSelectionSearchesSelectionSearch.

        Returns
        -------
        str
            The explore_config of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        return self._explore_config

    @explore_config.setter
    def explore_config(self, explore_config: "Optional[str]") -> None:
        """Sets the explore_config of this GrantaServerApiSelectionSearchesSelectionSearch.

        Parameters
        ----------
        explore_config: str
            The explore_config of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        self._explore_config = explore_config

    @property
    def created_timestamp(self) -> "Optional[datetime]":
        """Gets the created_timestamp of this GrantaServerApiSelectionSearchesSelectionSearch.

        Returns
        -------
        datetime
            The created_timestamp of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        return self._created_timestamp

    @created_timestamp.setter
    def created_timestamp(self, created_timestamp: "Optional[datetime]") -> None:
        """Sets the created_timestamp of this GrantaServerApiSelectionSearchesSelectionSearch.

        Parameters
        ----------
        created_timestamp: datetime
            The created_timestamp of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        self._created_timestamp = created_timestamp

    @property
    def created_user_or_group(
        self,
    ) -> "Optional[GrantaServerApiSelectionSearchesUserOrGroup]":
        """Gets the created_user_or_group of this GrantaServerApiSelectionSearchesSelectionSearch.

        Returns
        -------
        GrantaServerApiSelectionSearchesUserOrGroup
            The created_user_or_group of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        return self._created_user_or_group

    @created_user_or_group.setter
    def created_user_or_group(
        self,
        created_user_or_group: "Optional[GrantaServerApiSelectionSearchesUserOrGroup]",
    ) -> None:
        """Sets the created_user_or_group of this GrantaServerApiSelectionSearchesSelectionSearch.

        Parameters
        ----------
        created_user_or_group: GrantaServerApiSelectionSearchesUserOrGroup
            The created_user_or_group of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        self._created_user_or_group = created_user_or_group

    @property
    def last_modified_timestamp(self) -> "Optional[datetime]":
        """Gets the last_modified_timestamp of this GrantaServerApiSelectionSearchesSelectionSearch.

        Returns
        -------
        datetime
            The last_modified_timestamp of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        return self._last_modified_timestamp

    @last_modified_timestamp.setter
    def last_modified_timestamp(
        self, last_modified_timestamp: "Optional[datetime]"
    ) -> None:
        """Sets the last_modified_timestamp of this GrantaServerApiSelectionSearchesSelectionSearch.

        Parameters
        ----------
        last_modified_timestamp: datetime
            The last_modified_timestamp of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        self._last_modified_timestamp = last_modified_timestamp

    @property
    def last_modified_user_or_group(
        self,
    ) -> "Optional[GrantaServerApiSelectionSearchesUserOrGroup]":
        """Gets the last_modified_user_or_group of this GrantaServerApiSelectionSearchesSelectionSearch.

        Returns
        -------
        GrantaServerApiSelectionSearchesUserOrGroup
            The last_modified_user_or_group of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        return self._last_modified_user_or_group

    @last_modified_user_or_group.setter
    def last_modified_user_or_group(
        self,
        last_modified_user_or_group: "Optional[GrantaServerApiSelectionSearchesUserOrGroup]",
    ) -> None:
        """Sets the last_modified_user_or_group of this GrantaServerApiSelectionSearchesSelectionSearch.

        Parameters
        ----------
        last_modified_user_or_group: GrantaServerApiSelectionSearchesUserOrGroup
            The last_modified_user_or_group of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        self._last_modified_user_or_group = last_modified_user_or_group

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
        return self.to_str()  # type: ignore[no-any-return]

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiSelectionSearchesSelectionSearch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
