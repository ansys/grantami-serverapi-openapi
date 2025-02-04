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

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaUpdateAttribute(ModelBase):
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
        "type": "GsaAttributeType",
        "about_attribute": "GsaSlimEntity",
        "axis_name": "GsaUpdateAxisName",
        "default_threshold_type": "GsaAttributeThresholdType",
        "guid": "str",
        "help_path": "str",
        "is_hidden_from_search_criteria": "bool",
        "name": "str",
    }

    attribute_map: dict[str, str] = {
        "type": "type",
        "about_attribute": "aboutAttribute",
        "axis_name": "axisName",
        "default_threshold_type": "defaultThresholdType",
        "guid": "guid",
        "help_path": "helpPath",
        "is_hidden_from_search_criteria": "isHiddenFromSearchCriteria",
        "name": "name",
    }

    subtype_mapping: dict[str, str] = {
        "type": "GsaAttributeType",
        "defaultThresholdType": "GsaAttributeThresholdType",
        "axisName": "GsaUpdateAxisName",
        "aboutAttribute": "GsaSlimEntity",
    }

    discriminator_value_class_map = {
        "point".lower(): "#/components/schemas/GsaUpdatePointAttribute",
        "integer".lower(): "#/components/schemas/GsaUpdateIntegerAttribute",
        "range".lower(): "#/components/schemas/GsaUpdateRangeAttribute",
        "logical".lower(): "#/components/schemas/GsaUpdateLogicalAttribute",
        "shortText".lower(): "#/components/schemas/GsaUpdateShortTextAttribute",
        "longText".lower(): "#/components/schemas/GsaUpdateLongTextAttribute",
        "dateTime".lower(): "#/components/schemas/GsaUpdateDateTimeAttribute",
        "discrete".lower(): "#/components/schemas/GsaUpdateDiscreteAttribute",
        "hyperlink".lower(): "#/components/schemas/GsaUpdateHyperlinkAttribute",
        "file".lower(): "#/components/schemas/GsaUpdateFileAttribute",
        "picture".lower(): "#/components/schemas/GsaUpdatePictureAttribute",
        "link".lower(): "#/components/schemas/GsaUpdateTabularAttribute",
        "floatFunctional".lower(): "#/components/schemas/GsaUpdateFloatFunctionalAttribute",
        "discreteFunctional".lower(): "#/components/schemas/GsaUpdateDiscreteFunctionalAttribute",
        "mathsFunctional".lower(): "#/components/schemas/GsaUpdateMathsFunctionalAttribute",
    }

    discriminator: Optional[str] = "type"

    def __init__(
        self,
        *,
        type: "GsaAttributeType",
        about_attribute: "Union[GsaSlimEntity, Unset_Type]" = Unset,
        axis_name: "Union[GsaUpdateAxisName, Unset_Type]" = Unset,
        default_threshold_type: "Union[GsaAttributeThresholdType, Unset_Type]" = Unset,
        guid: "Union[str, Unset_Type]" = Unset,
        help_path: "Union[str, None, Unset_Type]" = Unset,
        is_hidden_from_search_criteria: "Union[bool, None, Unset_Type]" = Unset,
        name: "Union[str, Unset_Type]" = Unset,
    ) -> None:
        """GsaUpdateAttribute - a model defined in Swagger

        Parameters
        ----------
        type: GsaAttributeType
        about_attribute: GsaSlimEntity, optional
        axis_name: GsaUpdateAxisName, optional
        default_threshold_type: GsaAttributeThresholdType, optional
        guid: str, optional
        help_path: str, optional
        is_hidden_from_search_criteria: bool, optional
        name: str, optional
        """
        self._type: GsaAttributeType
        self._default_threshold_type: Union[GsaAttributeThresholdType, Unset_Type] = Unset
        self._axis_name: Union[GsaUpdateAxisName, Unset_Type] = Unset
        self._help_path: Union[str, None, Unset_Type] = Unset
        self._about_attribute: Union[GsaSlimEntity, Unset_Type] = Unset
        self._is_hidden_from_search_criteria: Union[bool, None, Unset_Type] = Unset
        self._name: Union[str, Unset_Type] = Unset
        self._guid: Union[str, Unset_Type] = Unset

        self.type = type
        if default_threshold_type is not Unset:
            self.default_threshold_type = default_threshold_type
        if axis_name is not Unset:
            self.axis_name = axis_name
        if help_path is not Unset:
            self.help_path = help_path
        if about_attribute is not Unset:
            self.about_attribute = about_attribute
        if is_hidden_from_search_criteria is not Unset:
            self.is_hidden_from_search_criteria = is_hidden_from_search_criteria
        if name is not Unset:
            self.name = name
        if guid is not Unset:
            self.guid = guid

    @property
    def type(self) -> "GsaAttributeType":
        """Gets the type of this GsaUpdateAttribute.

        Returns
        -------
        GsaAttributeType
            The type of this GsaUpdateAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "GsaAttributeType") -> None:
        """Sets the type of this GsaUpdateAttribute.

        Parameters
        ----------
        type: GsaAttributeType
            The type of this GsaUpdateAttribute.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

    @property
    def default_threshold_type(self) -> "Union[GsaAttributeThresholdType, Unset_Type]":
        """Gets the default_threshold_type of this GsaUpdateAttribute.

        Returns
        -------
        Union[GsaAttributeThresholdType, Unset_Type]
            The default_threshold_type of this GsaUpdateAttribute.
        """
        return self._default_threshold_type

    @default_threshold_type.setter
    def default_threshold_type(
        self, default_threshold_type: "Union[GsaAttributeThresholdType, Unset_Type]"
    ) -> None:
        """Sets the default_threshold_type of this GsaUpdateAttribute.

        Parameters
        ----------
        default_threshold_type: Union[GsaAttributeThresholdType, Unset_Type]
            The default_threshold_type of this GsaUpdateAttribute.
        """
        # Field is not nullable
        if default_threshold_type is None:
            raise ValueError("Invalid value for 'default_threshold_type', must not be 'None'")
        self._default_threshold_type = default_threshold_type

    @property
    def axis_name(self) -> "Union[GsaUpdateAxisName, Unset_Type]":
        """Gets the axis_name of this GsaUpdateAttribute.

        Returns
        -------
        Union[GsaUpdateAxisName, Unset_Type]
            The axis_name of this GsaUpdateAttribute.
        """
        return self._axis_name

    @axis_name.setter
    def axis_name(self, axis_name: "Union[GsaUpdateAxisName, Unset_Type]") -> None:
        """Sets the axis_name of this GsaUpdateAttribute.

        Parameters
        ----------
        axis_name: Union[GsaUpdateAxisName, Unset_Type]
            The axis_name of this GsaUpdateAttribute.
        """
        # Field is not nullable
        if axis_name is None:
            raise ValueError("Invalid value for 'axis_name', must not be 'None'")
        self._axis_name = axis_name

    @property
    def help_path(self) -> "Union[str, None, Unset_Type]":
        """Gets the help_path of this GsaUpdateAttribute.

        Returns
        -------
        Union[str, None, Unset_Type]
            The help_path of this GsaUpdateAttribute.
        """
        return self._help_path

    @help_path.setter
    def help_path(self, help_path: "Union[str, None, Unset_Type]") -> None:
        """Sets the help_path of this GsaUpdateAttribute.

        Parameters
        ----------
        help_path: Union[str, None, Unset_Type]
            The help_path of this GsaUpdateAttribute.
        """
        self._help_path = help_path

    @property
    def about_attribute(self) -> "Union[GsaSlimEntity, Unset_Type]":
        """Gets the about_attribute of this GsaUpdateAttribute.

        Returns
        -------
        Union[GsaSlimEntity, Unset_Type]
            The about_attribute of this GsaUpdateAttribute.
        """
        return self._about_attribute

    @about_attribute.setter
    def about_attribute(self, about_attribute: "Union[GsaSlimEntity, Unset_Type]") -> None:
        """Sets the about_attribute of this GsaUpdateAttribute.

        Parameters
        ----------
        about_attribute: Union[GsaSlimEntity, Unset_Type]
            The about_attribute of this GsaUpdateAttribute.
        """
        # Field is not nullable
        if about_attribute is None:
            raise ValueError("Invalid value for 'about_attribute', must not be 'None'")
        self._about_attribute = about_attribute

    @property
    def is_hidden_from_search_criteria(self) -> "Union[bool, None, Unset_Type]":
        """Gets the is_hidden_from_search_criteria of this GsaUpdateAttribute.
        If true, the attribute should not be shown in search UIs.  It will still be included in text searches.  If not specified, it will be set to the default value for the attribute type.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The is_hidden_from_search_criteria of this GsaUpdateAttribute.
        """
        return self._is_hidden_from_search_criteria

    @is_hidden_from_search_criteria.setter
    def is_hidden_from_search_criteria(
        self, is_hidden_from_search_criteria: "Union[bool, None, Unset_Type]"
    ) -> None:
        """Sets the is_hidden_from_search_criteria of this GsaUpdateAttribute.
        If true, the attribute should not be shown in search UIs.  It will still be included in text searches.  If not specified, it will be set to the default value for the attribute type.

        Parameters
        ----------
        is_hidden_from_search_criteria: Union[bool, None, Unset_Type]
            The is_hidden_from_search_criteria of this GsaUpdateAttribute.
        """
        self._is_hidden_from_search_criteria = is_hidden_from_search_criteria

    @property
    def name(self) -> "Union[str, Unset_Type]":
        """Gets the name of this GsaUpdateAttribute.

        Returns
        -------
        Union[str, Unset_Type]
            The name of this GsaUpdateAttribute.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, Unset_Type]") -> None:
        """Sets the name of this GsaUpdateAttribute.

        Parameters
        ----------
        name: Union[str, Unset_Type]
            The name of this GsaUpdateAttribute.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

    @property
    def guid(self) -> "Union[str, Unset_Type]":
        """Gets the guid of this GsaUpdateAttribute.

        Returns
        -------
        Union[str, Unset_Type]
            The guid of this GsaUpdateAttribute.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, Unset_Type]") -> None:
        """Sets the guid of this GsaUpdateAttribute.

        Parameters
        ----------
        guid: Union[str, Unset_Type]
            The guid of this GsaUpdateAttribute.
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
        if not isinstance(other, GsaUpdateAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
