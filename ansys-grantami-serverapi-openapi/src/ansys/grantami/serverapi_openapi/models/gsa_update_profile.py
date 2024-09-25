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

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaUpdateProfile(ModelBase):
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
        "description": "str",
        "group_name": "str",
        "guid": "str",
        "homepage_url": "str",
        "name": "str",
        "profile_table_guids": "list[str]",
    }

    attribute_map: Dict[str, str] = {
        "description": "description",
        "group_name": "groupName",
        "guid": "guid",
        "homepage_url": "homepageUrl",
        "name": "name",
        "profile_table_guids": "profileTableGuids",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        description: "Union[str, None, Unset_Type]" = Unset,
        group_name: "Union[str, None, Unset_Type]" = Unset,
        guid: "Union[str, None, Unset_Type]" = Unset,
        homepage_url: "Union[str, None, Unset_Type]" = Unset,
        name: "Union[str, Unset_Type]" = Unset,
        profile_table_guids: "Union[List[str], None, Unset_Type]" = Unset,
    ) -> None:
        """GsaUpdateProfile - a model defined in Swagger

        Parameters
        ----------
        description: str, optional
        group_name: str, optional
        guid: str, optional
        homepage_url: str, optional
        name: str, optional
        profile_table_guids: List[str], optional
        """
        self._description: Union[str, None, Unset_Type] = Unset
        self._homepage_url: Union[str, None, Unset_Type] = Unset
        self._profile_table_guids: Union[List[str], None, Unset_Type] = Unset
        self._guid: Union[str, None, Unset_Type] = Unset
        self._group_name: Union[str, None, Unset_Type] = Unset
        self._name: Union[str, Unset_Type] = Unset

        if description is not Unset:
            self.description = description
        if homepage_url is not Unset:
            self.homepage_url = homepage_url
        if profile_table_guids is not Unset:
            self.profile_table_guids = profile_table_guids
        if guid is not Unset:
            self.guid = guid
        if group_name is not Unset:
            self.group_name = group_name
        if name is not Unset:
            self.name = name

    @property
    def description(self) -> "Union[str, None, Unset_Type]":
        """Gets the description of this GsaUpdateProfile.

        Returns
        -------
        Union[str, None, Unset_Type]
            The description of this GsaUpdateProfile.
        """
        return self._description

    @description.setter
    def description(self, description: "Union[str, None, Unset_Type]") -> None:
        """Sets the description of this GsaUpdateProfile.

        Parameters
        ----------
        description: Union[str, None, Unset_Type]
            The description of this GsaUpdateProfile.
        """
        self._description = description

    @property
    def homepage_url(self) -> "Union[str, None, Unset_Type]":
        """Gets the homepage_url of this GsaUpdateProfile.

        Returns
        -------
        Union[str, None, Unset_Type]
            The homepage_url of this GsaUpdateProfile.
        """
        return self._homepage_url

    @homepage_url.setter
    def homepage_url(self, homepage_url: "Union[str, None, Unset_Type]") -> None:
        """Sets the homepage_url of this GsaUpdateProfile.

        Parameters
        ----------
        homepage_url: Union[str, None, Unset_Type]
            The homepage_url of this GsaUpdateProfile.
        """
        self._homepage_url = homepage_url

    @property
    def profile_table_guids(self) -> "Union[List[str], None, Unset_Type]":
        """Gets the profile_table_guids of this GsaUpdateProfile.

        Returns
        -------
        Union[List[str], None, Unset_Type]
            The profile_table_guids of this GsaUpdateProfile.
        """
        return self._profile_table_guids

    @profile_table_guids.setter
    def profile_table_guids(
        self, profile_table_guids: "Union[List[str], None, Unset_Type]"
    ) -> None:
        """Sets the profile_table_guids of this GsaUpdateProfile.

        Parameters
        ----------
        profile_table_guids: Union[List[str], None, Unset_Type]
            The profile_table_guids of this GsaUpdateProfile.
        """
        self._profile_table_guids = profile_table_guids

    @property
    def guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the guid of this GsaUpdateProfile.
        Guid is a unique identifier of a profile. Separate from key.

        Returns
        -------
        Union[str, None, Unset_Type]
            The guid of this GsaUpdateProfile.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the guid of this GsaUpdateProfile.
        Guid is a unique identifier of a profile. Separate from key.

        Parameters
        ----------
        guid: Union[str, None, Unset_Type]
            The guid of this GsaUpdateProfile.
        """
        self._guid = guid

    @property
    def group_name(self) -> "Union[str, None, Unset_Type]":
        """Gets the group_name of this GsaUpdateProfile.

        Returns
        -------
        Union[str, None, Unset_Type]
            The group_name of this GsaUpdateProfile.
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name: "Union[str, None, Unset_Type]") -> None:
        """Sets the group_name of this GsaUpdateProfile.

        Parameters
        ----------
        group_name: Union[str, None, Unset_Type]
            The group_name of this GsaUpdateProfile.
        """
        self._group_name = group_name

    @property
    def name(self) -> "Union[str, Unset_Type]":
        """Gets the name of this GsaUpdateProfile.

        Returns
        -------
        Union[str, Unset_Type]
            The name of this GsaUpdateProfile.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, Unset_Type]") -> None:
        """Sets the name of this GsaUpdateProfile.

        Parameters
        ----------
        name: Union[str, Unset_Type]
            The name of this GsaUpdateProfile.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

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
        if not isinstance(other, GsaUpdateProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other