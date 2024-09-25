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

from ansys.grantami.serverapi_openapi.models.gsa_sort_criterion import (  # noqa: F401
    GsaSortCriterion,
)
from ansys.grantami.serverapi_openapi.models.gsa_sort_criterion_type import GsaSortCriterionType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaRecordPropertySortCriterion(GsaSortCriterion):
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
        "type": "GsaSortCriterionType",
        "_property": "GsaSearchableRecordProperty",
        "sort_direction": "GsaSortDirection",
        "sort_type": "GsaSortType",
    }

    attribute_map: Dict[str, str] = {
        "type": "type",
        "_property": "property",
        "sort_direction": "sortDirection",
        "sort_type": "sortType",
    }

    subtype_mapping: Dict[str, str] = {
        "property": "GsaSearchableRecordProperty",
        "sortType": "GsaSortType",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        type: "GsaSortCriterionType" = GsaSortCriterionType.RECORDPROPERTY,
        _property: "Union[GsaSearchableRecordProperty, Unset_Type]" = Unset,
        sort_direction: "Union[GsaSortDirection, Unset_Type]" = Unset,
        sort_type: "Union[GsaSortType, Unset_Type]" = Unset,
    ) -> None:
        """GsaRecordPropertySortCriterion - a model defined in Swagger

        Parameters
        ----------
        type: GsaSortCriterionType
        _property: GsaSearchableRecordProperty, optional
        sort_direction: GsaSortDirection, optional
        sort_type: GsaSortType, optional
        """
        super().__init__(type=type, sort_direction=sort_direction)
        self.__property: Union[GsaSearchableRecordProperty, Unset_Type] = Unset
        self._sort_type: Union[GsaSortType, Unset_Type] = Unset

        if _property is not Unset:
            self._property = _property
        if sort_type is not Unset:
            self.sort_type = sort_type

    @property
    def _property(self) -> "Union[GsaSearchableRecordProperty, Unset_Type]":
        """Gets the _property of this GsaRecordPropertySortCriterion.

        Returns
        -------
        Union[GsaSearchableRecordProperty, Unset_Type]
            The _property of this GsaRecordPropertySortCriterion.
        """
        return self.__property

    @_property.setter
    def _property(self, _property: "Union[GsaSearchableRecordProperty, Unset_Type]") -> None:
        """Sets the _property of this GsaRecordPropertySortCriterion.

        Parameters
        ----------
        _property: Union[GsaSearchableRecordProperty, Unset_Type]
            The _property of this GsaRecordPropertySortCriterion.
        """
        # Field is not nullable
        if _property is None:
            raise ValueError("Invalid value for '_property', must not be 'None'")
        self.__property = _property

    @property
    def sort_type(self) -> "Union[GsaSortType, Unset_Type]":
        """Gets the sort_type of this GsaRecordPropertySortCriterion.

        Returns
        -------
        Union[GsaSortType, Unset_Type]
            The sort_type of this GsaRecordPropertySortCriterion.
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type: "Union[GsaSortType, Unset_Type]") -> None:
        """Sets the sort_type of this GsaRecordPropertySortCriterion.

        Parameters
        ----------
        sort_type: Union[GsaSortType, Unset_Type]
            The sort_type of this GsaRecordPropertySortCriterion.
        """
        # Field is not nullable
        if sort_type is None:
            raise ValueError("Invalid value for 'sort_type', must not be 'None'")
        self._sort_type = sort_type

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
        if not isinstance(other, GsaRecordPropertySortCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other