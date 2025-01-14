"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.models.gsa_aggregation_datum_criterion import GsaAggregationDatumCriterion  # noqa: F401
from ansys.grantami.serverapi_openapi.models.gsa_aggregation_datum_criterion_type import GsaAggregationDatumCriterionType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaRangeFixedWidthHistogramAggregationDatumCriterion(GsaAggregationDatumCriterion):
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
        "type": "GsaAggregationDatumCriterionType",
        "interval": "float",
        "offset": "float",
    }

    attribute_map: dict[str, str] = {
        "type": "type",
        "interval": "interval",
        "offset": "offset",
    }

    subtype_mapping: dict[str, str] = {
    }

    discriminator: Optional[str] = None

    def __init__(self, *, type: "GsaAggregationDatumCriterionType" = GsaAggregationDatumCriterionType.RANGEFIXEDWIDTHHISTOGRAM, interval: "Union[float, Unset_Type]" = Unset, offset: "Union[float, Unset_Type]" = Unset,) -> None:
        """GsaRangeFixedWidthHistogramAggregationDatumCriterion - a model defined in Swagger

        Parameters
        ----------
        type: GsaAggregationDatumCriterionType
        interval: float, optional
        offset: float, optional
        """
        super().__init__(type=type)
        self._interval: Union[float, Unset_Type] = Unset
        self._offset: Union[float, Unset_Type] = Unset

        if interval is not Unset:
            self.interval = interval
        if offset is not Unset:
            self.offset = offset

    @property
    def interval(self) -> "Union[float, Unset_Type]":
        """Gets the interval of this GsaRangeFixedWidthHistogramAggregationDatumCriterion.
        Fixed size of the resulting histogram buckets

        Returns
        -------
        Union[float, Unset_Type]
            The interval of this GsaRangeFixedWidthHistogramAggregationDatumCriterion.
        """
        return self._interval

    @interval.setter
    def interval(self, interval: "Union[float, Unset_Type]") -> None:
        """Sets the interval of this GsaRangeFixedWidthHistogramAggregationDatumCriterion.
        Fixed size of the resulting histogram buckets

        Parameters
        ----------
        interval: Union[float, Unset_Type]
            The interval of this GsaRangeFixedWidthHistogramAggregationDatumCriterion.
        """
        # Field is not nullable
        if interval is None:
            raise ValueError("Invalid value for 'interval', must not be 'None'")
        self._interval = interval

    @property
    def offset(self) -> "Union[float, Unset_Type]":
        """Gets the offset of this GsaRangeFixedWidthHistogramAggregationDatumCriterion.
        Offset of the lowest bucket boundary. Defaults to 0. Must be less than the interval.

        Returns
        -------
        Union[float, Unset_Type]
            The offset of this GsaRangeFixedWidthHistogramAggregationDatumCriterion.
        """
        return self._offset

    @offset.setter
    def offset(self, offset: "Union[float, Unset_Type]") -> None:
        """Sets the offset of this GsaRangeFixedWidthHistogramAggregationDatumCriterion.
        Offset of the lowest bucket boundary. Defaults to 0. Must be less than the interval.

        Parameters
        ----------
        offset: Union[float, Unset_Type]
            The offset of this GsaRangeFixedWidthHistogramAggregationDatumCriterion.
        """
        # Field is not nullable
        if offset is None:
            raise ValueError("Invalid value for 'offset', must not be 'None'")
        self._offset = offset

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
        if not isinstance(other, GsaRangeFixedWidthHistogramAggregationDatumCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

