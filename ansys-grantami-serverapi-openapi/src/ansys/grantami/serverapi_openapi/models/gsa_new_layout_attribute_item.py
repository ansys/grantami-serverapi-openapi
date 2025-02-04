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

from ansys.grantami.serverapi_openapi.models.gsa_new_layout_item import (  # noqa: F401
    GsaNewLayoutItem,
)
from ansys.grantami.serverapi_openapi.models.gsa_new_layout_item_type import GsaNewLayoutItemType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaNewLayoutAttributeItem(GsaNewLayoutItem):
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
        "attribute_guid": "str",
        "item_type": "GsaNewLayoutItemType",
        "guid": "str",
        "meta_attributes": "list[GsaNewLayoutAttributeItem]",
        "read_only": "bool",
        "required": "bool",
        "tabular_column_guids": "list[str]",
    }

    attribute_map: dict[str, str] = {
        "attribute_guid": "attributeGuid",
        "item_type": "itemType",
        "guid": "guid",
        "meta_attributes": "metaAttributes",
        "read_only": "readOnly",
        "required": "required",
        "tabular_column_guids": "tabularColumnGuids",
    }

    subtype_mapping: dict[str, str] = {
        "metaAttributes": "GsaNewLayoutAttributeItem",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_guid: "str",
        item_type: "GsaNewLayoutItemType" = GsaNewLayoutItemType.ATTRIBUTE,
        guid: "Union[str, Unset_Type]" = Unset,
        meta_attributes: "Union[list[GsaNewLayoutAttributeItem], None, Unset_Type]" = Unset,
        read_only: "Union[bool, Unset_Type]" = Unset,
        required: "Union[bool, Unset_Type]" = Unset,
        tabular_column_guids: "Union[list[str], None, Unset_Type]" = Unset,
    ) -> None:
        """GsaNewLayoutAttributeItem - a model defined in Swagger

        Parameters
        ----------
        attribute_guid: str
        item_type: GsaNewLayoutItemType
        guid: str, optional
        meta_attributes: list[GsaNewLayoutAttributeItem], optional
        read_only: bool, optional
        required: bool, optional
        tabular_column_guids: list[str], optional
        """
        super().__init__(item_type=item_type, guid=guid)
        self._attribute_guid: str
        self._required: Union[bool, Unset_Type] = Unset
        self._read_only: Union[bool, Unset_Type] = Unset
        self._meta_attributes: Union[list[GsaNewLayoutAttributeItem], None, Unset_Type] = Unset
        self._tabular_column_guids: Union[list[str], None, Unset_Type] = Unset

        self.attribute_guid = attribute_guid
        if required is not Unset:
            self.required = required
        if read_only is not Unset:
            self.read_only = read_only
        if meta_attributes is not Unset:
            self.meta_attributes = meta_attributes
        if tabular_column_guids is not Unset:
            self.tabular_column_guids = tabular_column_guids

    @property
    def attribute_guid(self) -> "str":
        """Gets the attribute_guid of this GsaNewLayoutAttributeItem.

        Returns
        -------
        str
            The attribute_guid of this GsaNewLayoutAttributeItem.
        """
        return self._attribute_guid

    @attribute_guid.setter
    def attribute_guid(self, attribute_guid: "str") -> None:
        """Sets the attribute_guid of this GsaNewLayoutAttributeItem.

        Parameters
        ----------
        attribute_guid: str
            The attribute_guid of this GsaNewLayoutAttributeItem.
        """
        # Field is not nullable
        if attribute_guid is None:
            raise ValueError("Invalid value for 'attribute_guid', must not be 'None'")
        # Field is required
        if attribute_guid is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'attribute_guid', must not be 'Unset'")
        self._attribute_guid = attribute_guid

    @property
    def required(self) -> "Union[bool, Unset_Type]":
        """Gets the required of this GsaNewLayoutAttributeItem.

        Returns
        -------
        Union[bool, Unset_Type]
            The required of this GsaNewLayoutAttributeItem.
        """
        return self._required

    @required.setter
    def required(self, required: "Union[bool, Unset_Type]") -> None:
        """Sets the required of this GsaNewLayoutAttributeItem.

        Parameters
        ----------
        required: Union[bool, Unset_Type]
            The required of this GsaNewLayoutAttributeItem.
        """
        # Field is not nullable
        if required is None:
            raise ValueError("Invalid value for 'required', must not be 'None'")
        self._required = required

    @property
    def read_only(self) -> "Union[bool, Unset_Type]":
        """Gets the read_only of this GsaNewLayoutAttributeItem.

        Returns
        -------
        Union[bool, Unset_Type]
            The read_only of this GsaNewLayoutAttributeItem.
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only: "Union[bool, Unset_Type]") -> None:
        """Sets the read_only of this GsaNewLayoutAttributeItem.

        Parameters
        ----------
        read_only: Union[bool, Unset_Type]
            The read_only of this GsaNewLayoutAttributeItem.
        """
        # Field is not nullable
        if read_only is None:
            raise ValueError("Invalid value for 'read_only', must not be 'None'")
        self._read_only = read_only

    @property
    def meta_attributes(self) -> "Union[list[GsaNewLayoutAttributeItem], None, Unset_Type]":
        """Gets the meta_attributes of this GsaNewLayoutAttributeItem.

        Returns
        -------
        Union[list[GsaNewLayoutAttributeItem], None, Unset_Type]
            The meta_attributes of this GsaNewLayoutAttributeItem.
        """
        return self._meta_attributes

    @meta_attributes.setter
    def meta_attributes(
        self, meta_attributes: "Union[list[GsaNewLayoutAttributeItem], None, Unset_Type]"
    ) -> None:
        """Sets the meta_attributes of this GsaNewLayoutAttributeItem.

        Parameters
        ----------
        meta_attributes: Union[list[GsaNewLayoutAttributeItem], None, Unset_Type]
            The meta_attributes of this GsaNewLayoutAttributeItem.
        """
        self._meta_attributes = meta_attributes

    @property
    def tabular_column_guids(self) -> "Union[list[str], None, Unset_Type]":
        """Gets the tabular_column_guids of this GsaNewLayoutAttributeItem.

        Returns
        -------
        Union[list[str], None, Unset_Type]
            The tabular_column_guids of this GsaNewLayoutAttributeItem.
        """
        return self._tabular_column_guids

    @tabular_column_guids.setter
    def tabular_column_guids(
        self, tabular_column_guids: "Union[list[str], None, Unset_Type]"
    ) -> None:
        """Sets the tabular_column_guids of this GsaNewLayoutAttributeItem.

        Parameters
        ----------
        tabular_column_guids: Union[list[str], None, Unset_Type]
            The tabular_column_guids of this GsaNewLayoutAttributeItem.
        """
        self._tabular_column_guids = tabular_column_guids

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
        if not isinstance(other, GsaNewLayoutAttributeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
