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
    BinaryIO,
    Dict,
    List,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.models.granta_server_api_aggregations_aggregation_datum_criterion import (
    GrantaServerApiAggregationsAggregationDatumCriterion,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion(
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
        "interval": "float",
        "offset": "float",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "interval": "interval",
        "offset": "offset",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        interval: "Union[float, Unset_Type]" = Unset,
        offset: "Union[float, Unset_Type]" = Unset,
        type: "str" = "pointFixedWidthHistogram",
    ) -> None:
        """GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion - a model defined in Swagger

        Parameters
        ----------
        interval: float, optional
        offset: float, optional
        type: str
        """
        super().__init__()
        self._interval: Union[float, Unset_Type] = Unset
        self._offset: Union[float, Unset_Type] = Unset
        self._type: str

        if interval is not Unset:
            self.interval = interval
        if offset is not Unset:
            self.offset = offset
        self.type = type

    @property
    def interval(self) -> "Union[float, Unset_Type]":
        """Gets the interval of this GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion.
        Fixed size of the resulting histogram buckets

        Returns
        -------
        Union[float, Unset_Type]
            The interval of this GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion.
        """
        return self._interval

    @interval.setter
    def interval(self, interval: "Union[float, Unset_Type]") -> None:
        """Sets the interval of this GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion.
        Fixed size of the resulting histogram buckets

        Parameters
        ----------
        interval: Union[float, Unset_Type]
            The interval of this GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion.
        """
        # Field is not nullable
        if interval is None:
            raise ValueError("Invalid value for 'interval', must not be 'None'")
        self._interval = interval

    @property
    def offset(self) -> "Union[float, Unset_Type]":
        """Gets the offset of this GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion.
        Offset of the lowest bucket boundary. Defaults to 0. Must be less than the interval.

        Returns
        -------
        Union[float, Unset_Type]
            The offset of this GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion.
        """
        return self._offset

    @offset.setter
    def offset(self, offset: "Union[float, Unset_Type]") -> None:
        """Sets the offset of this GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion.
        Offset of the lowest bucket boundary. Defaults to 0. Must be less than the interval.

        Parameters
        ----------
        offset: Union[float, Unset_Type]
            The offset of this GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion.
        """
        # Field is not nullable
        if offset is None:
            raise ValueError("Invalid value for 'offset', must not be 'None'")
        self._offset = offset

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

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
        if not isinstance(
            other,
            GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
