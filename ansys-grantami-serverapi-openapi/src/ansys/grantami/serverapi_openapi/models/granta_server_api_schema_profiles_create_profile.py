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


class GrantaServerApiSchemaProfilesCreateProfile(ModelBase):
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
        "name": "str",
        "description": "str",
        "group_name": "str",
        "guid": "str",
        "homepage_url": "str",
    }

    attribute_map: Dict[str, str] = {
        "name": "name",
        "description": "description",
        "group_name": "groupName",
        "guid": "guid",
        "homepage_url": "homepageUrl",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        name: "str",
        description: "Union[str, None, Unset_Type]" = Unset,
        group_name: "Union[str, None, Unset_Type]" = Unset,
        guid: "Union[str, Unset_Type]" = Unset,
        homepage_url: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaProfilesCreateProfile - a model defined in Swagger

        Parameters
        ----------
        name: str
        description: str, optional
        group_name: str, optional
        guid: str, optional
        homepage_url: str, optional
        """
        self._description: Union[str, None, Unset_Type] = Unset
        self._homepage_url: Union[str, None, Unset_Type] = Unset
        self._group_name: Union[str, None, Unset_Type] = Unset
        self._name: str
        self._guid: Union[str, Unset_Type] = Unset

        if description is not Unset:
            self.description = description
        if homepage_url is not Unset:
            self.homepage_url = homepage_url
        if group_name is not Unset:
            self.group_name = group_name
        self.name = name
        if guid is not Unset:
            self.guid = guid

    @property
    def description(self) -> "Union[str, None, Unset_Type]":
        """Gets the description of this GrantaServerApiSchemaProfilesCreateProfile.

        Returns
        -------
        Union[str, None, Unset_Type]
            The description of this GrantaServerApiSchemaProfilesCreateProfile.
        """
        return self._description

    @description.setter
    def description(self, description: "Union[str, None, Unset_Type]") -> None:
        """Sets the description of this GrantaServerApiSchemaProfilesCreateProfile.

        Parameters
        ----------
        description: Union[str, None, Unset_Type]
            The description of this GrantaServerApiSchemaProfilesCreateProfile.
        """
        self._description = description

    @property
    def homepage_url(self) -> "Union[str, None, Unset_Type]":
        """Gets the homepage_url of this GrantaServerApiSchemaProfilesCreateProfile.

        Returns
        -------
        Union[str, None, Unset_Type]
            The homepage_url of this GrantaServerApiSchemaProfilesCreateProfile.
        """
        return self._homepage_url

    @homepage_url.setter
    def homepage_url(self, homepage_url: "Union[str, None, Unset_Type]") -> None:
        """Sets the homepage_url of this GrantaServerApiSchemaProfilesCreateProfile.

        Parameters
        ----------
        homepage_url: Union[str, None, Unset_Type]
            The homepage_url of this GrantaServerApiSchemaProfilesCreateProfile.
        """
        self._homepage_url = homepage_url

    @property
    def group_name(self) -> "Union[str, None, Unset_Type]":
        """Gets the group_name of this GrantaServerApiSchemaProfilesCreateProfile.

        Returns
        -------
        Union[str, None, Unset_Type]
            The group_name of this GrantaServerApiSchemaProfilesCreateProfile.
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name: "Union[str, None, Unset_Type]") -> None:
        """Sets the group_name of this GrantaServerApiSchemaProfilesCreateProfile.

        Parameters
        ----------
        group_name: Union[str, None, Unset_Type]
            The group_name of this GrantaServerApiSchemaProfilesCreateProfile.
        """
        self._group_name = group_name

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaProfilesCreateProfile.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaProfilesCreateProfile.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaProfilesCreateProfile.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaProfilesCreateProfile.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        # Field is required
        if name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'name', must not be 'Unset'")
        self._name = name

    @property
    def guid(self) -> "Union[str, Unset_Type]":
        """Gets the guid of this GrantaServerApiSchemaProfilesCreateProfile.

        Returns
        -------
        Union[str, Unset_Type]
            The guid of this GrantaServerApiSchemaProfilesCreateProfile.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, Unset_Type]") -> None:
        """Sets the guid of this GrantaServerApiSchemaProfilesCreateProfile.

        Parameters
        ----------
        guid: Union[str, Unset_Type]
            The guid of this GrantaServerApiSchemaProfilesCreateProfile.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        self._guid = guid

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
        if not isinstance(other, GrantaServerApiSchemaProfilesCreateProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
