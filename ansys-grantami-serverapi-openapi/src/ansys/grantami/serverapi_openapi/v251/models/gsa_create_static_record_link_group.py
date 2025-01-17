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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from ansys.grantami.serverapi_openapi.v251.models.gsa_create_record_link_group import (  # noqa: F401
    GsaCreateRecordLinkGroup,
)
from ansys.grantami.serverapi_openapi.v251.models.gsa_record_link_group_type import (
    GsaRecordLinkGroupType,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaCreateStaticRecordLinkGroup(GsaCreateRecordLinkGroup):
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
        "link_target": "GsaLinkTarget",
        "name": "str",
        "reverse_name": "str",
        "type": "GsaRecordLinkGroupType",
        "guid": "str",
        "include_indirect_links": "bool",
    }

    attribute_map: dict[str, str] = {
        "link_target": "linkTarget",
        "name": "name",
        "reverse_name": "reverseName",
        "type": "type",
        "guid": "guid",
        "include_indirect_links": "includeIndirectLinks",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        link_target: "GsaLinkTarget",
        name: "str",
        reverse_name: "str",
        type: "GsaRecordLinkGroupType" = GsaRecordLinkGroupType.STATIC,
        guid: "Union[str, Unset_Type]" = Unset,
        include_indirect_links: "Union[bool, Unset_Type]" = Unset,
    ) -> None:
        """GsaCreateStaticRecordLinkGroup - a model defined in Swagger

        Parameters
        ----------
        link_target: GsaLinkTarget
        name: str
        reverse_name: str
        type: GsaRecordLinkGroupType
        guid: str, optional
        include_indirect_links: bool, optional
        """
        super().__init__(
            link_target=link_target, name=name, reverse_name=reverse_name, type=type, guid=guid
        )
        self._include_indirect_links: Union[bool, Unset_Type] = Unset

        if include_indirect_links is not Unset:
            self.include_indirect_links = include_indirect_links

    @property
    def include_indirect_links(self) -> "Union[bool, Unset_Type]":
        """Gets the include_indirect_links of this GsaCreateStaticRecordLinkGroup.

        Returns
        -------
        Union[bool, Unset_Type]
            The include_indirect_links of this GsaCreateStaticRecordLinkGroup.
        """
        return self._include_indirect_links

    @include_indirect_links.setter
    def include_indirect_links(self, include_indirect_links: "Union[bool, Unset_Type]") -> None:
        """Sets the include_indirect_links of this GsaCreateStaticRecordLinkGroup.

        Parameters
        ----------
        include_indirect_links: Union[bool, Unset_Type]
            The include_indirect_links of this GsaCreateStaticRecordLinkGroup.
        """
        # Field is not nullable
        if include_indirect_links is None:
            raise ValueError("Invalid value for 'include_indirect_links', must not be 'None'")
        self._include_indirect_links = include_indirect_links

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
        if not isinstance(other, GsaCreateStaticRecordLinkGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
