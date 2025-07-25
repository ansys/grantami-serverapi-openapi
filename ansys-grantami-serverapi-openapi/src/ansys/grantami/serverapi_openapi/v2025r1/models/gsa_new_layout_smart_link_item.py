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

from ansys.grantami.serverapi_openapi.v2025r1.models.gsa_new_layout_item import (  # noqa: F401
    GsaNewLayoutItem,
)
from ansys.grantami.serverapi_openapi.v2025r1.models.gsa_new_layout_item_type import (
    GsaNewLayoutItemType,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaNewLayoutSmartLinkItem(GsaNewLayoutItem):
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
        "item_type": "GsaNewLayoutItemType",
        "link_group_guid": "str",
        "forwards": "bool",
        "guid": "str",
    }

    attribute_map: dict[str, str] = {
        "item_type": "itemType",
        "link_group_guid": "linkGroupGuid",
        "forwards": "forwards",
        "guid": "guid",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        item_type: "GsaNewLayoutItemType" = GsaNewLayoutItemType.SMARTLINK,
        link_group_guid: "str",
        forwards: "bool | Unset_Type" = Unset,
        guid: "str | Unset_Type" = Unset,
    ) -> None:
        """GsaNewLayoutSmartLinkItem - a model defined in Swagger

        Parameters
        ----------
        item_type: GsaNewLayoutItemType
        link_group_guid: str
        forwards: bool, optional
        guid: str, optional
        """
        super().__init__(item_type=item_type, guid=guid)
        self._forwards: bool | Unset_Type = Unset
        self._link_group_guid: str

        if forwards is not Unset:
            self.forwards = forwards
        self.link_group_guid = link_group_guid

    @property
    def forwards(self) -> "bool | Unset_Type":
        """Gets the forwards of this GsaNewLayoutSmartLinkItem.
        true if the smart link points from the table the layout is in; or false if it points towards the table the layout is in (an inbound link).

        Returns
        -------
        bool | Unset_Type
            The forwards of this GsaNewLayoutSmartLinkItem.
        """
        return self._forwards

    @forwards.setter
    def forwards(self, forwards: "bool | Unset_Type") -> None:
        """Sets the forwards of this GsaNewLayoutSmartLinkItem.
        true if the smart link points from the table the layout is in; or false if it points towards the table the layout is in (an inbound link).

        Parameters
        ----------
        forwards: bool | Unset_Type
            The forwards of this GsaNewLayoutSmartLinkItem.
        """
        # Field is not nullable
        if forwards is None:
            raise ValueError("Invalid value for 'forwards', must not be 'None'")
        self._forwards = forwards

    @property
    def link_group_guid(self) -> "str":
        """Gets the link_group_guid of this GsaNewLayoutSmartLinkItem.

        Returns
        -------
        str
            The link_group_guid of this GsaNewLayoutSmartLinkItem.
        """
        return self._link_group_guid

    @link_group_guid.setter
    def link_group_guid(self, link_group_guid: "str") -> None:
        """Sets the link_group_guid of this GsaNewLayoutSmartLinkItem.

        Parameters
        ----------
        link_group_guid: str
            The link_group_guid of this GsaNewLayoutSmartLinkItem.
        """
        # Field is not nullable
        if link_group_guid is None:
            raise ValueError("Invalid value for 'link_group_guid', must not be 'None'")
        # Field is required
        if link_group_guid is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'link_group_guid', must not be 'Unset'")
        self._link_group_guid = link_group_guid

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
        if not isinstance(other, GsaNewLayoutSmartLinkItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
