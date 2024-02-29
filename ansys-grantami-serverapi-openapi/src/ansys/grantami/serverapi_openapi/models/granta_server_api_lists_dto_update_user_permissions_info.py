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


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiListsDtoUpdateUserPermissionsInfo(ModelBase):
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
        "user_permissions": "list[GrantaServerApiListsDtoUpdateUserPermission]",
    }

    attribute_map: Dict[str, str] = {
        "user_permissions": "userPermissions",
    }

    subtype_mapping: Dict[str, str] = {
        "userPermissions": "GrantaServerApiListsDtoUpdateUserPermission",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        user_permissions: "List[GrantaServerApiListsDtoUpdateUserPermission]",
    ) -> None:
        """GrantaServerApiListsDtoUpdateUserPermissionsInfo - a model defined in Swagger

        Parameters
        ----------
        user_permissions: List[GrantaServerApiListsDtoUpdateUserPermission]
        """
        self._user_permissions: List[GrantaServerApiListsDtoUpdateUserPermission]

        self.user_permissions = user_permissions

    @property
    def user_permissions(self) -> "List[GrantaServerApiListsDtoUpdateUserPermission]":
        """Gets the user_permissions of this GrantaServerApiListsDtoUpdateUserPermissionsInfo.

        Returns
        -------
        List[GrantaServerApiListsDtoUpdateUserPermission]
            The user_permissions of this GrantaServerApiListsDtoUpdateUserPermissionsInfo.
        """
        return self._user_permissions

    @user_permissions.setter
    def user_permissions(
        self, user_permissions: "List[GrantaServerApiListsDtoUpdateUserPermission]"
    ) -> None:
        """Sets the user_permissions of this GrantaServerApiListsDtoUpdateUserPermissionsInfo.

        Parameters
        ----------
        user_permissions: List[GrantaServerApiListsDtoUpdateUserPermission]
            The user_permissions of this GrantaServerApiListsDtoUpdateUserPermissionsInfo.
        """
        # Field is not nullable
        if user_permissions is None:
            raise ValueError("Invalid value for 'user_permissions', must not be 'None'")
        # Field is required
        if user_permissions is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'user_permissions', must not be 'Unset'"
            )
        self._user_permissions = user_permissions

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
        if not isinstance(other, GrantaServerApiListsDtoUpdateUserPermissionsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
