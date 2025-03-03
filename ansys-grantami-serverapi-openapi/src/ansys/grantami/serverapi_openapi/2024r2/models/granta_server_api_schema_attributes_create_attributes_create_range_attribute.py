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

from ansys.grantami.serverapi_openapi.2024r2.models.granta_server_api_schema_attributes_create_attributes_create_attribute import (  # noqa: F401
    GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiSchemaAttributesCreateAttributesCreateRangeAttribute(GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute):
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
        "name": "str",
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "axis_name": "str",
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "guid": "str",
        "help_path": "str",
        "type": "str",
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
    }

    attribute_map: dict[str, str] = {
        "name": "name",
        "about_attribute": "aboutAttribute",
        "axis_name": "axisName",
        "default_threshold_type": "defaultThresholdType",
        "guid": "guid",
        "help_path": "helpPath",
        "type": "type",
        "unit": "unit",
    }

    subtype_mapping: dict[str, str] = {
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, name: "str", about_attribute: "Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]" = Unset, axis_name: "Union[str, None, Unset_Type]" = Unset, default_threshold_type: "Union[GrantaServerApiSchemaAttributesAttributeThresholdType, Unset_Type]" = Unset, guid: "Union[str, Unset_Type]" = Unset, help_path: "Union[str, None, Unset_Type]" = Unset, type: "str" = 'range', unit: "Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]" = Unset,) -> None:
        """GrantaServerApiSchemaAttributesCreateAttributesCreateRangeAttribute - a model defined in Swagger

        Parameters
        ----------
        name: str
        about_attribute: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
        axis_name: str, optional
        default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType, optional
        guid: str, optional
        help_path: str, optional
        type: str
        unit: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
        """
        super().__init__(name=name, about_attribute=about_attribute, default_threshold_type=default_threshold_type, guid=guid, help_path=help_path)
        self._type: str
        self._unit: Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type] = Unset
        self._axis_name: Union[str, None, Unset_Type] = Unset

        self.type = type
        if unit is not Unset:
            self.unit = unit
        if axis_name is not Unset:
            self.axis_name = axis_name

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaAttributesCreateAttributesCreateRangeAttribute.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaAttributesCreateAttributesCreateRangeAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaAttributesCreateAttributesCreateRangeAttribute.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaAttributesCreateAttributesCreateRangeAttribute.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

    @property
    def unit(self) -> "Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]":
        """Gets the unit of this GrantaServerApiSchemaAttributesCreateAttributesCreateRangeAttribute.

        Returns
        -------
        Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]
            The unit of this GrantaServerApiSchemaAttributesCreateAttributesCreateRangeAttribute.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]") -> None:
        """Sets the unit of this GrantaServerApiSchemaAttributesCreateAttributesCreateRangeAttribute.

        Parameters
        ----------
        unit: Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]
            The unit of this GrantaServerApiSchemaAttributesCreateAttributesCreateRangeAttribute.
        """
        # Field is not nullable
        if unit is None:
            raise ValueError("Invalid value for 'unit', must not be 'None'")
        self._unit = unit

    @property
    def axis_name(self) -> "Union[str, None, Unset_Type]":
        """Gets the axis_name of this GrantaServerApiSchemaAttributesCreateAttributesCreateRangeAttribute.

        Returns
        -------
        Union[str, None, Unset_Type]
            The axis_name of this GrantaServerApiSchemaAttributesCreateAttributesCreateRangeAttribute.
        """
        return self._axis_name

    @axis_name.setter
    def axis_name(self, axis_name: "Union[str, None, Unset_Type]") -> None:
        """Sets the axis_name of this GrantaServerApiSchemaAttributesCreateAttributesCreateRangeAttribute.

        Parameters
        ----------
        axis_name: Union[str, None, Unset_Type]
            The axis_name of this GrantaServerApiSchemaAttributesCreateAttributesCreateRangeAttribute.
        """
        self._axis_name = axis_name

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
        if not isinstance(other, GrantaServerApiSchemaAttributesCreateAttributesCreateRangeAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

