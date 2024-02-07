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


class GrantaServerApiListsDtoUserPermission(ModelBase):
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
        "flags": "GrantaServerApiListsDtoRecordListPermissionFlags",
        "user_or_group_identifier": "str",
        "user_or_group_name": "str",
    }

    attribute_map = {
        "flags": "flags",
        "user_or_group_identifier": "userOrGroupIdentifier",
        "user_or_group_name": "userOrGroupName",
    }

    subtype_mapping = {
        "flags": "GrantaServerApiListsDtoRecordListPermissionFlags",
    }

    discriminator = None

    def __init__(
        self,
        *,
        flags: "GrantaServerApiListsDtoRecordListPermissionFlags",
        user_or_group_identifier: "str",
        user_or_group_name: "str",
    ) -> None:
        """GrantaServerApiListsDtoUserPermission - a model defined in Swagger

        Parameters
        ----------
            flags: GrantaServerApiListsDtoRecordListPermissionFlags
            user_or_group_identifier: str
            user_or_group_name: str
        """
        self._user_or_group_name = None
        self._user_or_group_identifier = None
        self._flags = None

        self.user_or_group_name = user_or_group_name
        self.user_or_group_identifier = user_or_group_identifier
        self.flags = flags

    @property
    def user_or_group_name(self) -> "str":
        """Gets the user_or_group_name of this GrantaServerApiListsDtoUserPermission.
        The user or group name.

        Returns
        -------
        str
            The user_or_group_name of this GrantaServerApiListsDtoUserPermission.
        """
        return self._user_or_group_name

    @user_or_group_name.setter
    def user_or_group_name(self, user_or_group_name: "str") -> None:
        """Sets the user_or_group_name of this GrantaServerApiListsDtoUserPermission.
        The user or group name.

        Parameters
        ----------
        user_or_group_name: str
            The user_or_group_name of this GrantaServerApiListsDtoUserPermission.
        """
        if user_or_group_name is None:
            raise ValueError(
                "Invalid value for 'user_or_group_name', must not be 'None'"
            )
        self._user_or_group_name = user_or_group_name

    @property
    def user_or_group_identifier(self) -> "str":
        """Gets the user_or_group_identifier of this GrantaServerApiListsDtoUserPermission.
        The user or group identifier

        Returns
        -------
        str
            The user_or_group_identifier of this GrantaServerApiListsDtoUserPermission.
        """
        return self._user_or_group_identifier

    @user_or_group_identifier.setter
    def user_or_group_identifier(self, user_or_group_identifier: "str") -> None:
        """Sets the user_or_group_identifier of this GrantaServerApiListsDtoUserPermission.
        The user or group identifier

        Parameters
        ----------
        user_or_group_identifier: str
            The user_or_group_identifier of this GrantaServerApiListsDtoUserPermission.
        """
        if user_or_group_identifier is None:
            raise ValueError(
                "Invalid value for 'user_or_group_identifier', must not be 'None'"
            )
        self._user_or_group_identifier = user_or_group_identifier

    @property
    def flags(self) -> "GrantaServerApiListsDtoRecordListPermissionFlags":
        """Gets the flags of this GrantaServerApiListsDtoUserPermission.

        Returns
        -------
        GrantaServerApiListsDtoRecordListPermissionFlags
            The flags of this GrantaServerApiListsDtoUserPermission.
        """
        return self._flags

    @flags.setter
    def flags(self, flags: "GrantaServerApiListsDtoRecordListPermissionFlags") -> None:
        """Sets the flags of this GrantaServerApiListsDtoUserPermission.

        Parameters
        ----------
        flags: GrantaServerApiListsDtoRecordListPermissionFlags
            The flags of this GrantaServerApiListsDtoUserPermission.
        """
        if flags is None:
            raise ValueError("Invalid value for 'flags', must not be 'None'")
        self._flags = flags

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
        if not isinstance(other, GrantaServerApiListsDtoUserPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other