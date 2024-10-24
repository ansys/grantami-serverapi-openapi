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

from ansys.grantami.serverapi_openapi.models.gsa_criterion import GsaCriterion  # noqa: F401
from ansys.grantami.serverapi_openapi.models.gsa_criterion_type import GsaCriterionType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaBooleanCriterion(GsaCriterion):
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
        "type": "GsaCriterionType",
        "_none": "list[GsaCriterion]",
        "all": "list[GsaCriterion]",
        "any": "list[GsaCriterion]",
    }

    attribute_map: dict[str, str] = {
        "type": "type",
        "_none": "none",
        "all": "all",
        "any": "any",
    }

    subtype_mapping: dict[str, str] = {
        "all": "GsaCriterion",
        "any": "GsaCriterion",
        "none": "GsaCriterion",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        type: "GsaCriterionType" = GsaCriterionType.BOOLEAN,
        _none: "Union[list[GsaCriterion], None, Unset_Type]" = Unset,
        all: "Union[list[GsaCriterion], None, Unset_Type]" = Unset,
        any: "Union[list[GsaCriterion], None, Unset_Type]" = Unset,
    ) -> None:
        """GsaBooleanCriterion - a model defined in Swagger

        Parameters
        ----------
        type: GsaCriterionType
        _none: list[GsaCriterion], optional
        all: list[GsaCriterion], optional
        any: list[GsaCriterion], optional
        """
        super().__init__(type=type)
        self._all: Union[list[GsaCriterion], None, Unset_Type] = Unset
        self._any: Union[list[GsaCriterion], None, Unset_Type] = Unset
        self.__none: Union[list[GsaCriterion], None, Unset_Type] = Unset

        if all is not Unset:
            self.all = all
        if any is not Unset:
            self.any = any
        if _none is not Unset:
            self._none = _none

    @property
    def all(self) -> "Union[list[GsaCriterion], None, Unset_Type]":
        """Gets the all of this GsaBooleanCriterion.
        Only records that match all of these criteria are returned.

        Returns
        -------
        Union[list[GsaCriterion], None, Unset_Type]
            The all of this GsaBooleanCriterion.
        """
        return self._all

    @all.setter
    def all(self, all: "Union[list[GsaCriterion], None, Unset_Type]") -> None:
        """Sets the all of this GsaBooleanCriterion.
        Only records that match all of these criteria are returned.

        Parameters
        ----------
        all: Union[list[GsaCriterion], None, Unset_Type]
            The all of this GsaBooleanCriterion.
        """
        self._all = all

    @property
    def any(self) -> "Union[list[GsaCriterion], None, Unset_Type]":
        """Gets the any of this GsaBooleanCriterion.
        Only results that match any of these criteria are returned.

        Returns
        -------
        Union[list[GsaCriterion], None, Unset_Type]
            The any of this GsaBooleanCriterion.
        """
        return self._any

    @any.setter
    def any(self, any: "Union[list[GsaCriterion], None, Unset_Type]") -> None:
        """Sets the any of this GsaBooleanCriterion.
        Only results that match any of these criteria are returned.

        Parameters
        ----------
        any: Union[list[GsaCriterion], None, Unset_Type]
            The any of this GsaBooleanCriterion.
        """
        self._any = any

    @property
    def _none(self) -> "Union[list[GsaCriterion], None, Unset_Type]":
        """Gets the _none of this GsaBooleanCriterion.
        Only results that match none of these criteria are returned.

        Returns
        -------
        Union[list[GsaCriterion], None, Unset_Type]
            The _none of this GsaBooleanCriterion.
        """
        return self.__none

    @_none.setter
    def _none(self, _none: "Union[list[GsaCriterion], None, Unset_Type]") -> None:
        """Sets the _none of this GsaBooleanCriterion.
        Only results that match none of these criteria are returned.

        Parameters
        ----------
        _none: Union[list[GsaCriterion], None, Unset_Type]
            The _none of this GsaBooleanCriterion.
        """
        self.__none = _none

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
        if not isinstance(other, GsaBooleanCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
