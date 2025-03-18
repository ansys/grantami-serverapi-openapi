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

from ansys.grantami.serverapi_openapi.v2024r2.models.granta_server_api_schema_attributes_update_attributes_update_attribute import (  # noqa: F401
    GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute(
    GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute
):
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
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "attribute_parameters": "list[GrantaServerApiSchemaSlimEntitiesSlimEntity]",
        "axis_name": "str",
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "guid": "str",
        "help_path": "str",
        "is_multi_valued": "bool",
        "name": "str",
        "type": "str",
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
    }

    attribute_map: dict[str, str] = {
        "about_attribute": "aboutAttribute",
        "attribute_parameters": "attributeParameters",
        "axis_name": "axisName",
        "default_threshold_type": "defaultThresholdType",
        "guid": "guid",
        "help_path": "helpPath",
        "is_multi_valued": "isMultiValued",
        "name": "name",
        "type": "type",
        "unit": "unit",
    }

    subtype_mapping: dict[str, str] = {
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "attributeParameters": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        about_attribute: "Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]" = Unset,
        attribute_parameters: "Union[list[GrantaServerApiSchemaSlimEntitiesSlimEntity], None, Unset_Type]" = Unset,
        axis_name: "Union[str, None, Unset_Type]" = Unset,
        default_threshold_type: "Union[GrantaServerApiSchemaAttributesAttributeThresholdType, Unset_Type]" = Unset,
        guid: "Union[str, Unset_Type]" = Unset,
        help_path: "Union[str, None, Unset_Type]" = Unset,
        is_multi_valued: "Union[bool, Unset_Type]" = Unset,
        name: "Union[str, Unset_Type]" = Unset,
        type: "str" = "point",
        unit: "Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute - a model defined in Swagger

        Parameters
        ----------
        about_attribute: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
        attribute_parameters: list[GrantaServerApiSchemaSlimEntitiesSlimEntity], optional
        axis_name: str, optional
        default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType, optional
        guid: str, optional
        help_path: str, optional
        is_multi_valued: bool, optional
        name: str, optional
        type: str
        unit: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
        """
        super().__init__(
            about_attribute=about_attribute,
            axis_name=axis_name,
            default_threshold_type=default_threshold_type,
            guid=guid,
            help_path=help_path,
            name=name,
        )
        self._type: str
        self._unit: Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type] = Unset
        self._is_multi_valued: Union[bool, Unset_Type] = Unset
        self._attribute_parameters: Union[
            list[GrantaServerApiSchemaSlimEntitiesSlimEntity], None, Unset_Type
        ] = Unset

        self.type = type
        if unit is not Unset:
            self.unit = unit
        if is_multi_valued is not Unset:
            self.is_multi_valued = is_multi_valued
        if attribute_parameters is not Unset:
            self.attribute_parameters = attribute_parameters

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.
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
        """Gets the unit of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.

        Returns
        -------
        Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]
            The unit of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]") -> None:
        """Sets the unit of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.

        Parameters
        ----------
        unit: Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]
            The unit of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.
        """
        # Field is not nullable
        if unit is None:
            raise ValueError("Invalid value for 'unit', must not be 'None'")
        self._unit = unit

    @property
    def is_multi_valued(self) -> "Union[bool, Unset_Type]":
        """Gets the is_multi_valued of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.

        Returns
        -------
        Union[bool, Unset_Type]
            The is_multi_valued of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.
        """
        return self._is_multi_valued

    @is_multi_valued.setter
    def is_multi_valued(self, is_multi_valued: "Union[bool, Unset_Type]") -> None:
        """Sets the is_multi_valued of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.

        Parameters
        ----------
        is_multi_valued: Union[bool, Unset_Type]
            The is_multi_valued of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.
        """
        # Field is not nullable
        if is_multi_valued is None:
            raise ValueError("Invalid value for 'is_multi_valued', must not be 'None'")
        self._is_multi_valued = is_multi_valued

    @property
    def attribute_parameters(
        self,
    ) -> "Union[list[GrantaServerApiSchemaSlimEntitiesSlimEntity], None, Unset_Type]":
        """Gets the attribute_parameters of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.

        Returns
        -------
        Union[list[GrantaServerApiSchemaSlimEntitiesSlimEntity], None, Unset_Type]
            The attribute_parameters of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.
        """
        return self._attribute_parameters

    @attribute_parameters.setter
    def attribute_parameters(
        self,
        attribute_parameters: "Union[list[GrantaServerApiSchemaSlimEntitiesSlimEntity], None, Unset_Type]",
    ) -> None:
        """Sets the attribute_parameters of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.

        Parameters
        ----------
        attribute_parameters: Union[list[GrantaServerApiSchemaSlimEntitiesSlimEntity], None, Unset_Type]
            The attribute_parameters of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.
        """
        self._attribute_parameters = attribute_parameters

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
        if not isinstance(
            other, GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
