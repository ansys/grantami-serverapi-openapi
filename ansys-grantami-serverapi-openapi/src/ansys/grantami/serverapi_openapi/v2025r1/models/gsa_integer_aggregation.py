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

from ansys.grantami.serverapi_openapi.v2025r1.models.gsa_aggregation_datum import (  # noqa: F401
    GsaAggregationDatum,
)
from ansys.grantami.serverapi_openapi.v2025r1.models.gsa_aggregation_datum_type import (
    GsaAggregationDatumType,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaIntegerAggregation(GsaAggregationDatum):
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
        "datum_type": "GsaAggregationDatumType",
        "maximum": "int",
        "minimum": "int",
    }

    attribute_map: dict[str, str] = {
        "datum_type": "datumType",
        "maximum": "maximum",
        "minimum": "minimum",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        datum_type: "GsaAggregationDatumType" = GsaAggregationDatumType.INTEGER,
        maximum: "Union[int, None, Unset_Type]" = Unset,
        minimum: "Union[int, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaIntegerAggregation - a model defined in Swagger

        Parameters
        ----------
        datum_type: GsaAggregationDatumType
        maximum: int, optional
        minimum: int, optional
        """
        super().__init__(datum_type=datum_type)
        self._minimum: Union[int, None, Unset_Type] = Unset
        self._maximum: Union[int, None, Unset_Type] = Unset

        if minimum is not Unset:
            self.minimum = minimum
        if maximum is not Unset:
            self.maximum = maximum

    @property
    def minimum(self) -> "Union[int, None, Unset_Type]":
        """Gets the minimum of this GsaIntegerAggregation.

        Returns
        -------
        Union[int, None, Unset_Type]
            The minimum of this GsaIntegerAggregation.
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum: "Union[int, None, Unset_Type]") -> None:
        """Sets the minimum of this GsaIntegerAggregation.

        Parameters
        ----------
        minimum: Union[int, None, Unset_Type]
            The minimum of this GsaIntegerAggregation.
        """
        self._minimum = minimum

    @property
    def maximum(self) -> "Union[int, None, Unset_Type]":
        """Gets the maximum of this GsaIntegerAggregation.

        Returns
        -------
        Union[int, None, Unset_Type]
            The maximum of this GsaIntegerAggregation.
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum: "Union[int, None, Unset_Type]") -> None:
        """Sets the maximum of this GsaIntegerAggregation.

        Parameters
        ----------
        maximum: Union[int, None, Unset_Type]
            The maximum of this GsaIntegerAggregation.
        """
        self._maximum = maximum

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
        if not isinstance(other, GsaIntegerAggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
