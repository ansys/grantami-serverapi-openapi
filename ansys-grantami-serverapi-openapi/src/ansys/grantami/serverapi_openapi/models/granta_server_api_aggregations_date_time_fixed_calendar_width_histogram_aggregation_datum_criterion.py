"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    BinaryIO,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase
from ansys.grantami.serverapi_openapi.models.granta_server_api_aggregations_aggregation_datum_criterion import (
    GrantaServerApiAggregationsAggregationDatumCriterion,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion(
    GrantaServerApiAggregationsAggregationDatumCriterion
):
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
        "interval": "GrantaServerApiAggregationsCalendarInterval",
        "offset": "str",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "interval": "interval",
        "offset": "offset",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {
        "interval": "GrantaServerApiAggregationsCalendarInterval",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        interval: "Optional[GrantaServerApiAggregationsCalendarInterval]" = None,
        offset: "Optional[str]" = None,
        type: "str" = "dateTimeFixedCalendarWidthHistogram",
    ) -> None:
        """GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion - a model defined in Swagger

        Parameters
        ----------
            interval: GrantaServerApiAggregationsCalendarInterval, optional
            offset: str, optional
            type: str
        """
        super().__init__()
        self._interval = None
        self._offset = None
        self._type: str = None  # type: ignore[assignment]

        if interval is not None:
            self.interval = interval
        if offset is not None:
            self.offset = offset
        self.type = type

    @property
    def interval(self) -> "Optional[GrantaServerApiAggregationsCalendarInterval]":
        """Gets the interval of this GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion.

        Returns
        -------
        GrantaServerApiAggregationsCalendarInterval
            The interval of this GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion.
        """
        return self._interval

    @interval.setter
    def interval(
        self, interval: "Optional[GrantaServerApiAggregationsCalendarInterval]"
    ) -> None:
        """Sets the interval of this GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion.

        Parameters
        ----------
        interval: GrantaServerApiAggregationsCalendarInterval
            The interval of this GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion.
        """
        self._interval = interval

    @property
    def offset(self) -> "Optional[str]":
        """Gets the offset of this GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion.
        Optional offset of the lowest bucket boundary, in SI time units. Must be an integer followed by one of the following units: ms (milliseconds), s (seconds), m (minutes), h (hours), d (days). Defaults to 0. Must be less than the interval. Negative offsets (e.g. \"-6h\") are supported

        Returns
        -------
        str
            The offset of this GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion.
        """
        return self._offset

    @offset.setter
    def offset(self, offset: "Optional[str]") -> None:
        """Sets the offset of this GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion.
        Optional offset of the lowest bucket boundary, in SI time units. Must be an integer followed by one of the following units: ms (milliseconds), s (seconds), m (minutes), h (hours), d (days). Defaults to 0. Must be less than the interval. Negative offsets (e.g. \"-6h\") are supported

        Parameters
        ----------
        offset: str
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
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @classmethod
    def get_real_child_model(cls, data: ModelBase) -> str:
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
        return self.to_str()  # type: ignore[no-any-return]

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(
            other,
            GrantaServerApiAggregationsDateTimeFixedCalendarWidthHistogramAggregationDatumCriterion,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
