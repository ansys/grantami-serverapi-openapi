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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaSortCriterion(ModelBase):
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
        "type": "GsaSortCriterionType",
        "sort_direction": "GsaSortDirection",
    }

    attribute_map: dict[str, str] = {
        "type": "type",
        "sort_direction": "sortDirection",
    }

    subtype_mapping: dict[str, str] = {
        "sortDirection": "GsaSortDirection",
        "type": "GsaSortCriterionType",
    }

    discriminator_value_class_map = {
        "attribute".lower(): "#/components/schemas/GsaAttributeSortCriterion",
        "recordProperty".lower(): "#/components/schemas/GsaRecordPropertySortCriterion",
        "relevance".lower(): "#/components/schemas/GsaRelevanceSortCriterion",
    }

    discriminator: Optional[str] = "type"

    def __init__(
        self,
        *,
        type: "GsaSortCriterionType",
        sort_direction: "Union[GsaSortDirection, Unset_Type]" = Unset,
    ) -> None:
        """GsaSortCriterion - a model defined in Swagger

        Parameters
        ----------
        type: GsaSortCriterionType
        sort_direction: GsaSortDirection, optional
        """
        self._sort_direction: Union[GsaSortDirection, Unset_Type] = Unset
        self._type: GsaSortCriterionType

        if sort_direction is not Unset:
            self.sort_direction = sort_direction
        self.type = type

    @property
    def sort_direction(self) -> "Union[GsaSortDirection, Unset_Type]":
        """Gets the sort_direction of this GsaSortCriterion.

        Returns
        -------
        Union[GsaSortDirection, Unset_Type]
            The sort_direction of this GsaSortCriterion.
        """
        return self._sort_direction

    @sort_direction.setter
    def sort_direction(self, sort_direction: "Union[GsaSortDirection, Unset_Type]") -> None:
        """Sets the sort_direction of this GsaSortCriterion.

        Parameters
        ----------
        sort_direction: Union[GsaSortDirection, Unset_Type]
            The sort_direction of this GsaSortCriterion.
        """
        # Field is not nullable
        if sort_direction is None:
            raise ValueError("Invalid value for 'sort_direction', must not be 'None'")
        self._sort_direction = sort_direction

    @property
    def type(self) -> "GsaSortCriterionType":
        """Gets the type of this GsaSortCriterion.

        Returns
        -------
        GsaSortCriterionType
            The type of this GsaSortCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "GsaSortCriterionType") -> None:
        """Sets the type of this GsaSortCriterion.

        Parameters
        ----------
        type: GsaSortCriterionType
            The type of this GsaSortCriterion.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

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
        if not isinstance(other, GsaSortCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
