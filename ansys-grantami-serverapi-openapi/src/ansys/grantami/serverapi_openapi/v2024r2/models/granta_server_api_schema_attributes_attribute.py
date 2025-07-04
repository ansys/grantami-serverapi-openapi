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


class GrantaServerApiSchemaAttributesAttribute(ModelBase):
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
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "display_names": "dict(str, str)",
        "guid": "str",
        "info": "GrantaServerApiSchemaAttributesAttributeAttributeInfo",
        "name": "str",
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "axis_name": "str",
        "help_path": "str",
    }

    attribute_map: dict[str, str] = {
        "default_threshold_type": "defaultThresholdType",
        "display_names": "displayNames",
        "guid": "guid",
        "info": "info",
        "name": "name",
        "about_attribute": "aboutAttribute",
        "axis_name": "axisName",
        "help_path": "helpPath",
    }

    subtype_mapping: dict[str, str] = {
        "defaultThresholdType": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "aboutAttribute": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "info": "GrantaServerApiSchemaAttributesAttributeAttributeInfo",
    }

    discriminator_value_class_map = {
        "point".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesPointAttribute",
        "integer".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesIntegerAttribute",
        "range".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesRangeAttribute",
        "logical".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesLogicalAttribute",
        "shortText".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesShortTextAttribute",
        "longText".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesLongTextAttribute",
        "dateTime".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesDateTimeAttribute",
        "discrete".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesDiscreteAttribute",
        "hyperlink".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesHyperlinkAttribute",
        "file".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesFileAttribute",
        "picture".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesPictureAttribute",
        "link".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesTabularAttribute",
        "floatFunctional".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesFloatFunctionalAttribute",
        "discreteFunctional".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute",
        "mathsFunctional".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesMathsFunctionalAttribute",
    }

    discriminator: Optional[str] = "type"

    def __init__(
        self,
        *,
        default_threshold_type: "GrantaServerApiSchemaAttributesAttributeThresholdType",
        display_names: "dict[str, str]",
        guid: "str",
        info: "GrantaServerApiSchemaAttributesAttributeAttributeInfo",
        name: "str",
        about_attribute: "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity | Unset_Type" = Unset,
        axis_name: "str | None | Unset_Type" = Unset,
        help_path: "str | None | Unset_Type" = Unset,
    ) -> None:
        """GrantaServerApiSchemaAttributesAttribute - a model defined in Swagger

        Parameters
        ----------
        default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType
        display_names: dict[str, str]
        guid: str
        info: GrantaServerApiSchemaAttributesAttributeAttributeInfo
        name: str
        about_attribute: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, optional
        axis_name: str | None, optional
        help_path: str | None, optional
        """
        self._default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType
        self._axis_name: str | None | Unset_Type = Unset
        self._help_path: str | None | Unset_Type = Unset
        self._about_attribute: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity | Unset_Type = Unset
        self._info: GrantaServerApiSchemaAttributesAttributeAttributeInfo
        self._display_names: dict[str, str]
        self._name: str
        self._guid: str

        self.default_threshold_type = default_threshold_type
        if axis_name is not Unset:
            self.axis_name = axis_name
        if help_path is not Unset:
            self.help_path = help_path
        if about_attribute is not Unset:
            self.about_attribute = about_attribute
        self.info = info
        self.display_names = display_names
        self.name = name
        self.guid = guid

    @property
    def default_threshold_type(self) -> "GrantaServerApiSchemaAttributesAttributeThresholdType":
        """Gets the default_threshold_type of this GrantaServerApiSchemaAttributesAttribute.

        Returns
        -------
        GrantaServerApiSchemaAttributesAttributeThresholdType
            The default_threshold_type of this GrantaServerApiSchemaAttributesAttribute.
        """
        return self._default_threshold_type

    @default_threshold_type.setter
    def default_threshold_type(
        self, default_threshold_type: "GrantaServerApiSchemaAttributesAttributeThresholdType"
    ) -> None:
        """Sets the default_threshold_type of this GrantaServerApiSchemaAttributesAttribute.

        Parameters
        ----------
        default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType
            The default_threshold_type of this GrantaServerApiSchemaAttributesAttribute.
        """
        # Field is not nullable
        if default_threshold_type is None:
            raise ValueError("Invalid value for 'default_threshold_type', must not be 'None'")
        # Field is required
        if default_threshold_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'default_threshold_type', must not be 'Unset'")
        self._default_threshold_type = default_threshold_type

    @property
    def axis_name(self) -> "str | None | Unset_Type":
        """Gets the axis_name of this GrantaServerApiSchemaAttributesAttribute.

        Returns
        -------
        str | None | Unset_Type
            The axis_name of this GrantaServerApiSchemaAttributesAttribute.
        """
        return self._axis_name

    @axis_name.setter
    def axis_name(self, axis_name: "str | None | Unset_Type") -> None:
        """Sets the axis_name of this GrantaServerApiSchemaAttributesAttribute.

        Parameters
        ----------
        axis_name: str | None | Unset_Type
            The axis_name of this GrantaServerApiSchemaAttributesAttribute.
        """
        self._axis_name = axis_name

    @property
    def help_path(self) -> "str | None | Unset_Type":
        """Gets the help_path of this GrantaServerApiSchemaAttributesAttribute.

        Returns
        -------
        str | None | Unset_Type
            The help_path of this GrantaServerApiSchemaAttributesAttribute.
        """
        return self._help_path

    @help_path.setter
    def help_path(self, help_path: "str | None | Unset_Type") -> None:
        """Sets the help_path of this GrantaServerApiSchemaAttributesAttribute.

        Parameters
        ----------
        help_path: str | None | Unset_Type
            The help_path of this GrantaServerApiSchemaAttributesAttribute.
        """
        self._help_path = help_path

    @property
    def about_attribute(self) -> "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity | Unset_Type":
        """Gets the about_attribute of this GrantaServerApiSchemaAttributesAttribute.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimNamedEntity | Unset_Type
            The about_attribute of this GrantaServerApiSchemaAttributesAttribute.
        """
        return self._about_attribute

    @about_attribute.setter
    def about_attribute(
        self, about_attribute: "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity | Unset_Type"
    ) -> None:
        """Sets the about_attribute of this GrantaServerApiSchemaAttributesAttribute.

        Parameters
        ----------
        about_attribute: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity | Unset_Type
            The about_attribute of this GrantaServerApiSchemaAttributesAttribute.
        """
        # Field is not nullable
        if about_attribute is None:
            raise ValueError("Invalid value for 'about_attribute', must not be 'None'")
        self._about_attribute = about_attribute

    @property
    def info(self) -> "GrantaServerApiSchemaAttributesAttributeAttributeInfo":
        """Gets the info of this GrantaServerApiSchemaAttributesAttribute.

        Returns
        -------
        GrantaServerApiSchemaAttributesAttributeAttributeInfo
            The info of this GrantaServerApiSchemaAttributesAttribute.
        """
        return self._info

    @info.setter
    def info(self, info: "GrantaServerApiSchemaAttributesAttributeAttributeInfo") -> None:
        """Sets the info of this GrantaServerApiSchemaAttributesAttribute.

        Parameters
        ----------
        info: GrantaServerApiSchemaAttributesAttributeAttributeInfo
            The info of this GrantaServerApiSchemaAttributesAttribute.
        """
        # Field is not nullable
        if info is None:
            raise ValueError("Invalid value for 'info', must not be 'None'")
        # Field is required
        if info is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'info', must not be 'Unset'")
        self._info = info

    @property
    def display_names(self) -> "dict[str, str]":
        """Gets the display_names of this GrantaServerApiSchemaAttributesAttribute.

        Returns
        -------
        dict[str, str]
            The display_names of this GrantaServerApiSchemaAttributesAttribute.
        """
        return self._display_names

    @display_names.setter
    def display_names(self, display_names: "dict[str, str]") -> None:
        """Sets the display_names of this GrantaServerApiSchemaAttributesAttribute.

        Parameters
        ----------
        display_names: dict[str, str]
            The display_names of this GrantaServerApiSchemaAttributesAttribute.
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
        """Gets the name of this GrantaServerApiSchemaAttributesAttribute.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaAttributesAttribute.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaAttributesAttribute.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaAttributesAttribute.
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
        """Gets the guid of this GrantaServerApiSchemaAttributesAttribute.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaAttributesAttribute.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaAttributesAttribute.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaAttributesAttribute.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        # Field is required
        if guid is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'guid', must not be 'Unset'")
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
        if not isinstance(other, GrantaServerApiSchemaAttributesAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
