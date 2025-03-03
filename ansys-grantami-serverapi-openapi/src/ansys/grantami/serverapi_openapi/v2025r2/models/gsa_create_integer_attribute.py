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

from ansys.grantami.serverapi_openapi.v2025r2.models.gsa_attribute_type import GsaAttributeType
from ansys.grantami.serverapi_openapi.v2025r2.models.gsa_create_attribute import (  # noqa: F401
    GsaCreateAttribute,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaCreateIntegerAttribute(GsaCreateAttribute):
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
        "type": "GsaAttributeType",
        "axis_name": "GsaCreateAxisName",
        "default_threshold_type": "GsaAttributeThresholdType",
        "guid": "str",
        "help_path": "str",
        "is_hidden_from_search_criteria": "bool",
        "is_unique": "bool",
    }

    attribute_map: dict[str, str] = {
        "name": "name",
        "type": "type",
        "axis_name": "axisName",
        "default_threshold_type": "defaultThresholdType",
        "guid": "guid",
        "help_path": "helpPath",
        "is_hidden_from_search_criteria": "isHiddenFromSearchCriteria",
        "is_unique": "isUnique",
    }

    subtype_mapping: dict[str, str] = {
        "axisName": "GsaCreateAxisName",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        name: "str",
        type: "GsaAttributeType" = GsaAttributeType.INTEGER,
        axis_name: "Union[GsaCreateAxisName, Unset_Type]" = Unset,
        default_threshold_type: "Union[GsaAttributeThresholdType, Unset_Type]" = Unset,
        guid: "Union[str, Unset_Type]" = Unset,
        help_path: "Union[str, None, Unset_Type]" = Unset,
        is_hidden_from_search_criteria: "Union[bool, None, Unset_Type]" = Unset,
        is_unique: "Union[bool, Unset_Type]" = Unset,
    ) -> None:
        """GsaCreateIntegerAttribute - a model defined in Swagger

        Parameters
        ----------
        name: str
        type: GsaAttributeType
        axis_name: GsaCreateAxisName, optional
        default_threshold_type: GsaAttributeThresholdType, optional
        guid: str, optional
        help_path: str, optional
        is_hidden_from_search_criteria: bool, optional
        is_unique: bool, optional
        """
        super().__init__(
            name=name,
            type=type,
            default_threshold_type=default_threshold_type,
            guid=guid,
            help_path=help_path,
            is_hidden_from_search_criteria=is_hidden_from_search_criteria,
        )
        self._is_unique: Union[bool, Unset_Type] = Unset
        self._axis_name: Union[GsaCreateAxisName, Unset_Type] = Unset

        if is_unique is not Unset:
            self.is_unique = is_unique
        if axis_name is not Unset:
            self.axis_name = axis_name

    @property
    def is_unique(self) -> "Union[bool, Unset_Type]":
        """Gets the is_unique of this GsaCreateIntegerAttribute.
        Whether or not the attribute is constrained to contain a unique value

        Returns
        -------
        Union[bool, Unset_Type]
            The is_unique of this GsaCreateIntegerAttribute.
        """
        return self._is_unique

    @is_unique.setter
    def is_unique(self, is_unique: "Union[bool, Unset_Type]") -> None:
        """Sets the is_unique of this GsaCreateIntegerAttribute.
        Whether or not the attribute is constrained to contain a unique value

        Parameters
        ----------
        is_unique: Union[bool, Unset_Type]
            The is_unique of this GsaCreateIntegerAttribute.
        """
        # Field is not nullable
        if is_unique is None:
            raise ValueError("Invalid value for 'is_unique', must not be 'None'")
        self._is_unique = is_unique

    @property
    def axis_name(self) -> "Union[GsaCreateAxisName, Unset_Type]":
        """Gets the axis_name of this GsaCreateIntegerAttribute.

        Returns
        -------
        Union[GsaCreateAxisName, Unset_Type]
            The axis_name of this GsaCreateIntegerAttribute.
        """
        return self._axis_name

    @axis_name.setter
    def axis_name(self, axis_name: "Union[GsaCreateAxisName, Unset_Type]") -> None:
        """Sets the axis_name of this GsaCreateIntegerAttribute.

        Parameters
        ----------
        axis_name: Union[GsaCreateAxisName, Unset_Type]
            The axis_name of this GsaCreateIntegerAttribute.
        """
        # Field is not nullable
        if axis_name is None:
            raise ValueError("Invalid value for 'axis_name', must not be 'None'")
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
        if not isinstance(other, GsaCreateIntegerAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
