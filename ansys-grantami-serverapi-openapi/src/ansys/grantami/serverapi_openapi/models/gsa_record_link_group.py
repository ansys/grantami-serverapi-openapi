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


class GsaRecordLinkGroup(ModelBase):
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
    discriminator_class_map: Dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: Dict[str, str] = {
        "display_names": "dict(str, str)",
        "guid": "str",
        "link_info": "GsaLinkInfo",
        "name": "str",
        "reverse_name": "str",
        "type": "GsaRecordLinkGroupType",
        "identity": "int",
        "reverse_display_names": "dict(str, str)",
    }

    attribute_map: Dict[str, str] = {
        "display_names": "displayNames",
        "guid": "guid",
        "link_info": "linkInfo",
        "name": "name",
        "reverse_name": "reverseName",
        "type": "type",
        "identity": "identity",
        "reverse_display_names": "reverseDisplayNames",
    }

    subtype_mapping: Dict[str, str] = {
        "linkInfo": "GsaLinkInfo",
        "type": "GsaRecordLinkGroupType",
    }

    discriminator_value_class_map = {
        "static".lower(): "#/components/schemas/GsaStaticRecordLinkGroup",
        "dynamic".lower(): "#/components/schemas/GsaDynamicRecordLinkGroup",
        "crossDatabase".lower(): "#/components/schemas/GsaCrossDatabaseRecordLinkGroup",
    }

    discriminator: Optional[str] = "type"

    def __init__(
        self,
        *,
        display_names: "Dict[str, str]",
        guid: "str",
        link_info: "GsaLinkInfo",
        name: "str",
        reverse_name: "str",
        type: "GsaRecordLinkGroupType",
        identity: "Union[int, None, Unset_Type]" = Unset,
        reverse_display_names: "Union[Dict[str, str], None, Unset_Type]" = Unset,
    ) -> None:
        """GsaRecordLinkGroup - a model defined in Swagger

        Parameters
        ----------
        display_names: Dict[str, str]
        guid: str
        link_info: GsaLinkInfo
        name: str
        reverse_name: str
        type: GsaRecordLinkGroupType
        identity: int, optional
        reverse_display_names: Dict[str, str], optional
        """
        self._link_info: GsaLinkInfo
        self._identity: Union[int, None, Unset_Type] = Unset
        self._type: GsaRecordLinkGroupType
        self._reverse_name: str
        self._reverse_display_names: Union[Dict[str, str], None, Unset_Type] = Unset
        self._display_names: Dict[str, str]
        self._name: str
        self._guid: str

        self.link_info = link_info
        if identity is not Unset:
            self.identity = identity
        self.type = type
        self.reverse_name = reverse_name
        if reverse_display_names is not Unset:
            self.reverse_display_names = reverse_display_names
        self.display_names = display_names
        self.name = name
        self.guid = guid

    @property
    def link_info(self) -> "GsaLinkInfo":
        """Gets the link_info of this GsaRecordLinkGroup.

        Returns
        -------
        GsaLinkInfo
            The link_info of this GsaRecordLinkGroup.
        """
        return self._link_info

    @link_info.setter
    def link_info(self, link_info: "GsaLinkInfo") -> None:
        """Sets the link_info of this GsaRecordLinkGroup.

        Parameters
        ----------
        link_info: GsaLinkInfo
            The link_info of this GsaRecordLinkGroup.
        """
        # Field is not nullable
        if link_info is None:
            raise ValueError("Invalid value for 'link_info', must not be 'None'")
        # Field is required
        if link_info is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'link_info', must not be 'Unset'")
        self._link_info = link_info

    @property
    def identity(self) -> "Union[int, None, Unset_Type]":
        """Gets the identity of this GsaRecordLinkGroup.

        Returns
        -------
        Union[int, None, Unset_Type]
            The identity of this GsaRecordLinkGroup.
        """
        return self._identity

    @identity.setter
    def identity(self, identity: "Union[int, None, Unset_Type]") -> None:
        """Sets the identity of this GsaRecordLinkGroup.

        Parameters
        ----------
        identity: Union[int, None, Unset_Type]
            The identity of this GsaRecordLinkGroup.
        """
        self._identity = identity

    @property
    def type(self) -> "GsaRecordLinkGroupType":
        """Gets the type of this GsaRecordLinkGroup.

        Returns
        -------
        GsaRecordLinkGroupType
            The type of this GsaRecordLinkGroup.
        """
        return self._type

    @type.setter
    def type(self, type: "GsaRecordLinkGroupType") -> None:
        """Sets the type of this GsaRecordLinkGroup.

        Parameters
        ----------
        type: GsaRecordLinkGroupType
            The type of this GsaRecordLinkGroup.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

    @property
    def reverse_name(self) -> "str":
        """Gets the reverse_name of this GsaRecordLinkGroup.

        Returns
        -------
        str
            The reverse_name of this GsaRecordLinkGroup.
        """
        return self._reverse_name

    @reverse_name.setter
    def reverse_name(self, reverse_name: "str") -> None:
        """Sets the reverse_name of this GsaRecordLinkGroup.

        Parameters
        ----------
        reverse_name: str
            The reverse_name of this GsaRecordLinkGroup.
        """
        # Field is not nullable
        if reverse_name is None:
            raise ValueError("Invalid value for 'reverse_name', must not be 'None'")
        # Field is required
        if reverse_name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'reverse_name', must not be 'Unset'")
        self._reverse_name = reverse_name

    @property
    def reverse_display_names(self) -> "Union[Dict[str, str], None, Unset_Type]":
        """Gets the reverse_display_names of this GsaRecordLinkGroup.

        Returns
        -------
        Union[Dict[str, str], None, Unset_Type]
            The reverse_display_names of this GsaRecordLinkGroup.
        """
        return self._reverse_display_names

    @reverse_display_names.setter
    def reverse_display_names(
        self, reverse_display_names: "Union[Dict[str, str], None, Unset_Type]"
    ) -> None:
        """Sets the reverse_display_names of this GsaRecordLinkGroup.

        Parameters
        ----------
        reverse_display_names: Union[Dict[str, str], None, Unset_Type]
            The reverse_display_names of this GsaRecordLinkGroup.
        """
        self._reverse_display_names = reverse_display_names

    @property
    def display_names(self) -> "Dict[str, str]":
        """Gets the display_names of this GsaRecordLinkGroup.

        Returns
        -------
        Dict[str, str]
            The display_names of this GsaRecordLinkGroup.
        """
        return self._display_names

    @display_names.setter
    def display_names(self, display_names: "Dict[str, str]") -> None:
        """Sets the display_names of this GsaRecordLinkGroup.

        Parameters
        ----------
        display_names: Dict[str, str]
            The display_names of this GsaRecordLinkGroup.
        """
        # Field is not nullable
        if display_names is None:
            raise ValueError("Invalid value for 'display_names', must not be 'None'")
        # Field is required
        if display_names is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'display_names', must not be 'Unset'")
        self._display_names = display_names

    @property
    def name(self) -> "str":
        """Gets the name of this GsaRecordLinkGroup.

        Returns
        -------
        str
            The name of this GsaRecordLinkGroup.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GsaRecordLinkGroup.

        Parameters
        ----------
        name: str
            The name of this GsaRecordLinkGroup.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        # Field is required
        if name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'name', must not be 'Unset'")
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GsaRecordLinkGroup.

        Returns
        -------
        str
            The guid of this GsaRecordLinkGroup.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GsaRecordLinkGroup.

        Parameters
        ----------
        guid: str
            The guid of this GsaRecordLinkGroup.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        # Field is required
        if guid is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'guid', must not be 'Unset'")
        self._guid = guid

    @classmethod
    def get_real_child_model(cls, data: Dict[str, str]) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[cls._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen,
        # so we have to extract it from the JSON reference
        return cls.discriminator_value_class_map[discriminator_value].rsplit("/", 1)[-1]

    @classmethod
    def _get_discriminator_field_name(cls) -> str:
        assert cls.discriminator
        name_tokens = cls.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GsaRecordLinkGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other