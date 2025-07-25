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


class GrantaServerApiSchemaRecordLinkGroupsUpdateRecordLinkGroup(ModelBase):
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
    discriminator_class_map: dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "guid": "str",
        "name": "str",
        "reverse_name": "str",
    }

    attribute_map: dict[str, str] = {
        "guid": "guid",
        "name": "name",
        "reverse_name": "reverseName",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator_value_class_map = {
        "static".lower(): "#/components/schemas/GrantaServerApiSchemaRecordLinkGroupsUpdateStaticRecordLinkGroup",
        "dynamic".lower(): "#/components/schemas/GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup",
        "crossDatabase".lower(): "#/components/schemas/GrantaServerApiSchemaRecordLinkGroupsUpdateCrossDatabaseRecordLinkGroup",
    }

    discriminator: Optional[str] = "type"

    def __init__(
        self,
        *,
        guid: "str | Unset_Type" = Unset,
        name: "str | Unset_Type" = Unset,
        reverse_name: "str | Unset_Type" = Unset,
    ) -> None:
        """GrantaServerApiSchemaRecordLinkGroupsUpdateRecordLinkGroup - a model defined in Swagger

        Parameters
        ----------
        guid: str, optional
        name: str, optional
        reverse_name: str, optional
        """
        self._reverse_name: str | Unset_Type = Unset
        self._name: str | Unset_Type = Unset
        self._guid: str | Unset_Type = Unset

        if reverse_name is not Unset:
            self.reverse_name = reverse_name
        if name is not Unset:
            self.name = name
        if guid is not Unset:
            self.guid = guid

    @property
    def reverse_name(self) -> "str | Unset_Type":
        """Gets the reverse_name of this GrantaServerApiSchemaRecordLinkGroupsUpdateRecordLinkGroup.

        Returns
        -------
        str | Unset_Type
            The reverse_name of this GrantaServerApiSchemaRecordLinkGroupsUpdateRecordLinkGroup.
        """
        return self._reverse_name

    @reverse_name.setter
    def reverse_name(self, reverse_name: "str | Unset_Type") -> None:
        """Sets the reverse_name of this GrantaServerApiSchemaRecordLinkGroupsUpdateRecordLinkGroup.

        Parameters
        ----------
        reverse_name: str | Unset_Type
            The reverse_name of this GrantaServerApiSchemaRecordLinkGroupsUpdateRecordLinkGroup.
        """
        # Field is not nullable
        if reverse_name is None:
            raise ValueError("Invalid value for 'reverse_name', must not be 'None'")
        self._reverse_name = reverse_name

    @property
    def name(self) -> "str | Unset_Type":
        """Gets the name of this GrantaServerApiSchemaRecordLinkGroupsUpdateRecordLinkGroup.

        Returns
        -------
        str | Unset_Type
            The name of this GrantaServerApiSchemaRecordLinkGroupsUpdateRecordLinkGroup.
        """
        return self._name

    @name.setter
    def name(self, name: "str | Unset_Type") -> None:
        """Sets the name of this GrantaServerApiSchemaRecordLinkGroupsUpdateRecordLinkGroup.

        Parameters
        ----------
        name: str | Unset_Type
            The name of this GrantaServerApiSchemaRecordLinkGroupsUpdateRecordLinkGroup.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

    @property
    def guid(self) -> "str | Unset_Type":
        """Gets the guid of this GrantaServerApiSchemaRecordLinkGroupsUpdateRecordLinkGroup.

        Returns
        -------
        str | Unset_Type
            The guid of this GrantaServerApiSchemaRecordLinkGroupsUpdateRecordLinkGroup.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str | Unset_Type") -> None:
        """Sets the guid of this GrantaServerApiSchemaRecordLinkGroupsUpdateRecordLinkGroup.

        Parameters
        ----------
        guid: str | Unset_Type
            The guid of this GrantaServerApiSchemaRecordLinkGroupsUpdateRecordLinkGroup.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        self._guid = guid

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
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
        if not isinstance(other, GrantaServerApiSchemaRecordLinkGroupsUpdateRecordLinkGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
