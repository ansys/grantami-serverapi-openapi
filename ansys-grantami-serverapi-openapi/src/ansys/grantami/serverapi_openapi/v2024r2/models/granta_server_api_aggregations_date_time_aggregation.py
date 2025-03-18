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

from ansys.grantami.serverapi_openapi.v2024r2.models.granta_server_api_aggregations_aggregation_datum import (  # noqa: F401
    GrantaServerApiAggregationsAggregationDatum,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiAggregationsDateTimeAggregation(GrantaServerApiAggregationsAggregationDatum):
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
        "datum_type": "str",
        "maximum": "datetime",
        "minimum": "datetime",
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
        datum_type: "str" = "dateTime",
        maximum: "Union[datetime, None, Unset_Type]" = Unset,
        minimum: "Union[datetime, None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiAggregationsDateTimeAggregation - a model defined in Swagger

        Parameters
        ----------
        datum_type: str
        maximum: datetime, optional
        minimum: datetime, optional
        """
        super().__init__()
        self._minimum: Union[datetime, None, Unset_Type] = Unset
        self._maximum: Union[datetime, None, Unset_Type] = Unset
        self._datum_type: str

        if minimum is not Unset:
            self.minimum = minimum
        if maximum is not Unset:
            self.maximum = maximum
        self.datum_type = datum_type

    @property
    def minimum(self) -> "Union[datetime, None, Unset_Type]":
        """Gets the minimum of this GrantaServerApiAggregationsDateTimeAggregation.

        Returns
        -------
        Union[datetime, None, Unset_Type]
            The minimum of this GrantaServerApiAggregationsDateTimeAggregation.
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum: "Union[datetime, None, Unset_Type]") -> None:
        """Sets the minimum of this GrantaServerApiAggregationsDateTimeAggregation.

        Parameters
        ----------
        minimum: Union[datetime, None, Unset_Type]
            The minimum of this GrantaServerApiAggregationsDateTimeAggregation.
        """
        self._minimum = minimum

    @property
    def maximum(self) -> "Union[datetime, None, Unset_Type]":
        """Gets the maximum of this GrantaServerApiAggregationsDateTimeAggregation.

        Returns
        -------
        Union[datetime, None, Unset_Type]
            The maximum of this GrantaServerApiAggregationsDateTimeAggregation.
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum: "Union[datetime, None, Unset_Type]") -> None:
        """Sets the maximum of this GrantaServerApiAggregationsDateTimeAggregation.

        Parameters
        ----------
        maximum: Union[datetime, None, Unset_Type]
            The maximum of this GrantaServerApiAggregationsDateTimeAggregation.
        """
        self._maximum = maximum

    @property
    def datum_type(self) -> "str":
        """Gets the datum_type of this GrantaServerApiAggregationsDateTimeAggregation.

        Returns
        -------
        str
            The datum_type of this GrantaServerApiAggregationsDateTimeAggregation.
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type: "str") -> None:
        """Sets the datum_type of this GrantaServerApiAggregationsDateTimeAggregation.

        Parameters
        ----------
        datum_type: str
            The datum_type of this GrantaServerApiAggregationsDateTimeAggregation.
        """
        # Field is not nullable
        if datum_type is None:
            raise ValueError("Invalid value for 'datum_type', must not be 'None'")
        # Field is required
        if datum_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'datum_type', must not be 'Unset'")
        self._datum_type = datum_type

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
        if not isinstance(other, GrantaServerApiAggregationsDateTimeAggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
