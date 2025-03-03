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

from ansys.grantami.serverapi_openapi.2024r2.models.granta_server_api_aggregations_aggregation_datum_criterion import (  # noqa: F401
    GrantaServerApiAggregationsAggregationDatumCriterion,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion(GrantaServerApiAggregationsAggregationDatumCriterion):
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
        "interval": "GrantaServerApiAggregationsCalendarInterval",
        "offset": "str",
        "type": "str",
    }

    attribute_map: dict[str, str] = {
        "interval": "interval",
        "offset": "offset",
        "type": "type",
    }

    subtype_mapping: dict[str, str] = {
        "interval": "GrantaServerApiAggregationsCalendarInterval",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, interval: "Union[GrantaServerApiAggregationsCalendarInterval, Unset_Type]" = Unset, offset: "Union[str, None, Unset_Type]" = Unset, type: "str" = 'dateTimeFixedCalendarWidthHistogram',) -> None:
        """GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion - a model defined in Swagger

        Parameters
        ----------
        interval: GrantaServerApiAggregationsCalendarInterval, optional
        offset: str, optional
        type: str
        """
        super().__init__()
        self._interval: Union[GrantaServerApiAggregationsCalendarInterval, Unset_Type] = Unset
        self._offset: Union[str, None, Unset_Type] = Unset
        self._type: str

        if interval is not Unset:
            self.interval = interval
        if offset is not Unset:
            self.offset = offset
        self.type = type

    @property
    def interval(self) -> "Union[GrantaServerApiAggregationsCalendarInterval, Unset_Type]":
        """Gets the interval of this GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion.

        Returns
        -------
        Union[GrantaServerApiAggregationsCalendarInterval, Unset_Type]
            The interval of this GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion.
        """
        return self._interval

    @interval.setter
    def interval(self, interval: "Union[GrantaServerApiAggregationsCalendarInterval, Unset_Type]") -> None:
        """Sets the interval of this GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion.

        Parameters
        ----------
        interval: Union[GrantaServerApiAggregationsCalendarInterval, Unset_Type]
            The interval of this GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion.
        """
        # Field is not nullable
        if interval is None:
            raise ValueError("Invalid value for 'interval', must not be 'None'")
        self._interval = interval

    @property
    def offset(self) -> "Union[str, None, Unset_Type]":
        """Gets the offset of this GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion.
        Optional offset of the lowest bucket boundary, in SI time units. Must be an integer followed by one of the following units: ms (milliseconds), s (seconds), m (minutes), h (hours), d (days). Defaults to 0. Must be less than the interval. Negative offsets (e.g. \"-6h\") are supported

        Returns
        -------
        Union[str, None, Unset_Type]
            The offset of this GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion.
        """
        return self._offset

    @offset.setter
    def offset(self, offset: "Union[str, None, Unset_Type]") -> None:
        """Sets the offset of this GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion.
        Optional offset of the lowest bucket boundary, in SI time units. Must be an integer followed by one of the following units: ms (milliseconds), s (seconds), m (minutes), h (hours), d (days). Defaults to 0. Must be less than the interval. Negative offsets (e.g. \"-6h\") are supported

        Parameters
        ----------
        offset: Union[str, None, Unset_Type]
            The offset of this GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion.
        """
        self._offset = offset

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion.
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
        if not isinstance(other, GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

