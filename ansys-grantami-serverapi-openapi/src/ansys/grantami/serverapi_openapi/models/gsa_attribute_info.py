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


class GsaAttributeInfo(ModelBase):
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
        "chartable": "bool",
        "expressionable": "bool",
        "extended_name": "str",
        "foreign_data_link_groups": "list[GsaSlimNamedEntity]",
        "is_meta_attribute": "bool",
        "linkable": "bool",
        "primary_data_link_groups": "list[GsaSlimNamedEntity]",
        "standard_names": "list[GsaSlimNamedEntity]",
        "type_code": "str",
        "foreign_dynamic_link_groups": "list[GsaSlimNamedEntity]",
        "ordered_meta_attributes": "list[GsaSlimNamedEntity]",
        "primary_dynamic_link_groups": "list[GsaSlimNamedEntity]",
    }

    attribute_map: Dict[str, str] = {
        "chartable": "chartable",
        "expressionable": "expressionable",
        "extended_name": "extendedName",
        "foreign_data_link_groups": "foreignDataLinkGroups",
        "is_meta_attribute": "isMetaAttribute",
        "linkable": "linkable",
        "primary_data_link_groups": "primaryDataLinkGroups",
        "standard_names": "standardNames",
        "type_code": "typeCode",
        "foreign_dynamic_link_groups": "foreignDynamicLinkGroups",
        "ordered_meta_attributes": "orderedMetaAttributes",
        "primary_dynamic_link_groups": "primaryDynamicLinkGroups",
    }

    subtype_mapping: Dict[str, str] = {
        "orderedMetaAttributes": "GsaSlimNamedEntity",
        "standardNames": "GsaSlimNamedEntity",
        "primaryDataLinkGroups": "GsaSlimNamedEntity",
        "foreignDataLinkGroups": "GsaSlimNamedEntity",
        "primaryDynamicLinkGroups": "GsaSlimNamedEntity",
        "foreignDynamicLinkGroups": "GsaSlimNamedEntity",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        chartable: "bool",
        expressionable: "bool",
        extended_name: "str",
        foreign_data_link_groups: "List[GsaSlimNamedEntity]",
        is_meta_attribute: "bool",
        linkable: "bool",
        primary_data_link_groups: "List[GsaSlimNamedEntity]",
        standard_names: "List[GsaSlimNamedEntity]",
        type_code: "str",
        foreign_dynamic_link_groups: "Union[List[GsaSlimNamedEntity], None, Unset_Type]" = Unset,
        ordered_meta_attributes: "Union[List[GsaSlimNamedEntity], None, Unset_Type]" = Unset,
        primary_dynamic_link_groups: "Union[List[GsaSlimNamedEntity], None, Unset_Type]" = Unset,
    ) -> None:
        """GsaAttributeInfo - a model defined in Swagger

        Parameters
        ----------
        chartable: bool
        expressionable: bool
        extended_name: str
        foreign_data_link_groups: List[GsaSlimNamedEntity]
        is_meta_attribute: bool
        linkable: bool
        primary_data_link_groups: List[GsaSlimNamedEntity]
        standard_names: List[GsaSlimNamedEntity]
        type_code: str
        foreign_dynamic_link_groups: List[GsaSlimNamedEntity], optional
        ordered_meta_attributes: List[GsaSlimNamedEntity], optional
        primary_dynamic_link_groups: List[GsaSlimNamedEntity], optional
        """
        self._type_code: str
        self._chartable: bool
        self._expressionable: bool
        self._linkable: bool
        self._extended_name: str
        self._is_meta_attribute: bool
        self._ordered_meta_attributes: Union[List[GsaSlimNamedEntity], None, Unset_Type] = Unset
        self._standard_names: List[GsaSlimNamedEntity]
        self._primary_data_link_groups: List[GsaSlimNamedEntity]
        self._foreign_data_link_groups: List[GsaSlimNamedEntity]
        self._primary_dynamic_link_groups: Union[List[GsaSlimNamedEntity], None, Unset_Type] = Unset
        self._foreign_dynamic_link_groups: Union[List[GsaSlimNamedEntity], None, Unset_Type] = Unset

        self.type_code = type_code
        self.chartable = chartable
        self.expressionable = expressionable
        self.linkable = linkable
        self.extended_name = extended_name
        self.is_meta_attribute = is_meta_attribute
        if ordered_meta_attributes is not Unset:
            self.ordered_meta_attributes = ordered_meta_attributes
        self.standard_names = standard_names
        self.primary_data_link_groups = primary_data_link_groups
        self.foreign_data_link_groups = foreign_data_link_groups
        if primary_dynamic_link_groups is not Unset:
            self.primary_dynamic_link_groups = primary_dynamic_link_groups
        if foreign_dynamic_link_groups is not Unset:
            self.foreign_dynamic_link_groups = foreign_dynamic_link_groups

    @property
    def type_code(self) -> "str":
        """Gets the type_code of this GsaAttributeInfo.

        Returns
        -------
        str
            The type_code of this GsaAttributeInfo.
        """
        return self._type_code

    @type_code.setter
    def type_code(self, type_code: "str") -> None:
        """Sets the type_code of this GsaAttributeInfo.

        Parameters
        ----------
        type_code: str
            The type_code of this GsaAttributeInfo.
        """
        # Field is not nullable
        if type_code is None:
            raise ValueError("Invalid value for 'type_code', must not be 'None'")
        # Field is required
        if type_code is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type_code', must not be 'Unset'")
        self._type_code = type_code

    @property
    def chartable(self) -> "bool":
        """Gets the chartable of this GsaAttributeInfo.

        Returns
        -------
        bool
            The chartable of this GsaAttributeInfo.
        """
        return self._chartable

    @chartable.setter
    def chartable(self, chartable: "bool") -> None:
        """Sets the chartable of this GsaAttributeInfo.

        Parameters
        ----------
        chartable: bool
            The chartable of this GsaAttributeInfo.
        """
        # Field is not nullable
        if chartable is None:
            raise ValueError("Invalid value for 'chartable', must not be 'None'")
        # Field is required
        if chartable is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'chartable', must not be 'Unset'")
        self._chartable = chartable

    @property
    def expressionable(self) -> "bool":
        """Gets the expressionable of this GsaAttributeInfo.

        Returns
        -------
        bool
            The expressionable of this GsaAttributeInfo.
        """
        return self._expressionable

    @expressionable.setter
    def expressionable(self, expressionable: "bool") -> None:
        """Sets the expressionable of this GsaAttributeInfo.

        Parameters
        ----------
        expressionable: bool
            The expressionable of this GsaAttributeInfo.
        """
        # Field is not nullable
        if expressionable is None:
            raise ValueError("Invalid value for 'expressionable', must not be 'None'")
        # Field is required
        if expressionable is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'expressionable', must not be 'Unset'")
        self._expressionable = expressionable

    @property
    def linkable(self) -> "bool":
        """Gets the linkable of this GsaAttributeInfo.

        Returns
        -------
        bool
            The linkable of this GsaAttributeInfo.
        """
        return self._linkable

    @linkable.setter
    def linkable(self, linkable: "bool") -> None:
        """Sets the linkable of this GsaAttributeInfo.

        Parameters
        ----------
        linkable: bool
            The linkable of this GsaAttributeInfo.
        """
        # Field is not nullable
        if linkable is None:
            raise ValueError("Invalid value for 'linkable', must not be 'None'")
        # Field is required
        if linkable is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'linkable', must not be 'Unset'")
        self._linkable = linkable

    @property
    def extended_name(self) -> "str":
        """Gets the extended_name of this GsaAttributeInfo.

        Returns
        -------
        str
            The extended_name of this GsaAttributeInfo.
        """
        return self._extended_name

    @extended_name.setter
    def extended_name(self, extended_name: "str") -> None:
        """Sets the extended_name of this GsaAttributeInfo.

        Parameters
        ----------
        extended_name: str
            The extended_name of this GsaAttributeInfo.
        """
        # Field is not nullable
        if extended_name is None:
            raise ValueError("Invalid value for 'extended_name', must not be 'None'")
        # Field is required
        if extended_name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'extended_name', must not be 'Unset'")
        self._extended_name = extended_name

    @property
    def is_meta_attribute(self) -> "bool":
        """Gets the is_meta_attribute of this GsaAttributeInfo.

        Returns
        -------
        bool
            The is_meta_attribute of this GsaAttributeInfo.
        """
        return self._is_meta_attribute

    @is_meta_attribute.setter
    def is_meta_attribute(self, is_meta_attribute: "bool") -> None:
        """Sets the is_meta_attribute of this GsaAttributeInfo.

        Parameters
        ----------
        is_meta_attribute: bool
            The is_meta_attribute of this GsaAttributeInfo.
        """
        # Field is not nullable
        if is_meta_attribute is None:
            raise ValueError("Invalid value for 'is_meta_attribute', must not be 'None'")
        # Field is required
        if is_meta_attribute is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'is_meta_attribute', must not be 'Unset'")
        self._is_meta_attribute = is_meta_attribute

    @property
    def ordered_meta_attributes(self) -> "Union[List[GsaSlimNamedEntity], None, Unset_Type]":
        """Gets the ordered_meta_attributes of this GsaAttributeInfo.

        Returns
        -------
        Union[List[GsaSlimNamedEntity], None, Unset_Type]
            The ordered_meta_attributes of this GsaAttributeInfo.
        """
        return self._ordered_meta_attributes

    @ordered_meta_attributes.setter
    def ordered_meta_attributes(
        self, ordered_meta_attributes: "Union[List[GsaSlimNamedEntity], None, Unset_Type]"
    ) -> None:
        """Sets the ordered_meta_attributes of this GsaAttributeInfo.

        Parameters
        ----------
        ordered_meta_attributes: Union[List[GsaSlimNamedEntity], None, Unset_Type]
            The ordered_meta_attributes of this GsaAttributeInfo.
        """
        self._ordered_meta_attributes = ordered_meta_attributes

    @property
    def standard_names(self) -> "List[GsaSlimNamedEntity]":
        """Gets the standard_names of this GsaAttributeInfo.

        Returns
        -------
        List[GsaSlimNamedEntity]
            The standard_names of this GsaAttributeInfo.
        """
        return self._standard_names

    @standard_names.setter
    def standard_names(self, standard_names: "List[GsaSlimNamedEntity]") -> None:
        """Sets the standard_names of this GsaAttributeInfo.

        Parameters
        ----------
        standard_names: List[GsaSlimNamedEntity]
            The standard_names of this GsaAttributeInfo.
        """
        # Field is not nullable
        if standard_names is None:
            raise ValueError("Invalid value for 'standard_names', must not be 'None'")
        # Field is required
        if standard_names is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'standard_names', must not be 'Unset'")
        self._standard_names = standard_names

    @property
    def primary_data_link_groups(self) -> "List[GsaSlimNamedEntity]":
        """Gets the primary_data_link_groups of this GsaAttributeInfo.

        Returns
        -------
        List[GsaSlimNamedEntity]
            The primary_data_link_groups of this GsaAttributeInfo.
        """
        return self._primary_data_link_groups

    @primary_data_link_groups.setter
    def primary_data_link_groups(
        self, primary_data_link_groups: "List[GsaSlimNamedEntity]"
    ) -> None:
        """Sets the primary_data_link_groups of this GsaAttributeInfo.

        Parameters
        ----------
        primary_data_link_groups: List[GsaSlimNamedEntity]
            The primary_data_link_groups of this GsaAttributeInfo.
        """
        # Field is not nullable
        if primary_data_link_groups is None:
            raise ValueError("Invalid value for 'primary_data_link_groups', must not be 'None'")
        # Field is required
        if primary_data_link_groups is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'primary_data_link_groups', must not be 'Unset'")
        self._primary_data_link_groups = primary_data_link_groups

    @property
    def foreign_data_link_groups(self) -> "List[GsaSlimNamedEntity]":
        """Gets the foreign_data_link_groups of this GsaAttributeInfo.

        Returns
        -------
        List[GsaSlimNamedEntity]
            The foreign_data_link_groups of this GsaAttributeInfo.
        """
        return self._foreign_data_link_groups

    @foreign_data_link_groups.setter
    def foreign_data_link_groups(
        self, foreign_data_link_groups: "List[GsaSlimNamedEntity]"
    ) -> None:
        """Sets the foreign_data_link_groups of this GsaAttributeInfo.

        Parameters
        ----------
        foreign_data_link_groups: List[GsaSlimNamedEntity]
            The foreign_data_link_groups of this GsaAttributeInfo.
        """
        # Field is not nullable
        if foreign_data_link_groups is None:
            raise ValueError("Invalid value for 'foreign_data_link_groups', must not be 'None'")
        # Field is required
        if foreign_data_link_groups is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'foreign_data_link_groups', must not be 'Unset'")
        self._foreign_data_link_groups = foreign_data_link_groups

    @property
    def primary_dynamic_link_groups(self) -> "Union[List[GsaSlimNamedEntity], None, Unset_Type]":
        """Gets the primary_dynamic_link_groups of this GsaAttributeInfo.

        Returns
        -------
        Union[List[GsaSlimNamedEntity], None, Unset_Type]
            The primary_dynamic_link_groups of this GsaAttributeInfo.
        """
        return self._primary_dynamic_link_groups

    @primary_dynamic_link_groups.setter
    def primary_dynamic_link_groups(
        self, primary_dynamic_link_groups: "Union[List[GsaSlimNamedEntity], None, Unset_Type]"
    ) -> None:
        """Sets the primary_dynamic_link_groups of this GsaAttributeInfo.

        Parameters
        ----------
        primary_dynamic_link_groups: Union[List[GsaSlimNamedEntity], None, Unset_Type]
            The primary_dynamic_link_groups of this GsaAttributeInfo.
        """
        self._primary_dynamic_link_groups = primary_dynamic_link_groups

    @property
    def foreign_dynamic_link_groups(self) -> "Union[List[GsaSlimNamedEntity], None, Unset_Type]":
        """Gets the foreign_dynamic_link_groups of this GsaAttributeInfo.

        Returns
        -------
        Union[List[GsaSlimNamedEntity], None, Unset_Type]
            The foreign_dynamic_link_groups of this GsaAttributeInfo.
        """
        return self._foreign_dynamic_link_groups

    @foreign_dynamic_link_groups.setter
    def foreign_dynamic_link_groups(
        self, foreign_dynamic_link_groups: "Union[List[GsaSlimNamedEntity], None, Unset_Type]"
    ) -> None:
        """Sets the foreign_dynamic_link_groups of this GsaAttributeInfo.

        Parameters
        ----------
        foreign_dynamic_link_groups: Union[List[GsaSlimNamedEntity], None, Unset_Type]
            The foreign_dynamic_link_groups of this GsaAttributeInfo.
        """
        self._foreign_dynamic_link_groups = foreign_dynamic_link_groups

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
        if not isinstance(other, GsaAttributeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other