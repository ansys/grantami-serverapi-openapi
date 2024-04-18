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
from ansys.grantami.serverapi_openapi.models.granta_server_api_aggregations_aggregation_datum import (
    GrantaServerApiAggregationsAggregationDatum,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiAggregationsIntegerHistogramAggregation(
    GrantaServerApiAggregationsAggregationDatum
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
        "datum_type": "str",
        "histogram": "GrantaServerApiAggregationsHistogram",
    }

    attribute_map: Dict[str, str] = {
        "datum_type": "datumType",
        "histogram": "histogram",
    }

    subtype_mapping: Dict[str, str] = {
        "histogram": "GrantaServerApiAggregationsHistogram",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        datum_type: "str" = "integerHistogram",
        histogram: "Union[GrantaServerApiAggregationsHistogram, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiAggregationsIntegerHistogramAggregation - a model defined in Swagger

        Parameters
        ----------
        datum_type: str
        histogram: GrantaServerApiAggregationsHistogram, optional
        """
        super().__init__()
        self._histogram: Union[GrantaServerApiAggregationsHistogram, Unset_Type] = Unset
        self._datum_type: str

        if histogram is not Unset:
            self.histogram = histogram
        self.datum_type = datum_type

    @property
    def histogram(self) -> "Union[GrantaServerApiAggregationsHistogram, Unset_Type]":
        """Gets the histogram of this GrantaServerApiAggregationsIntegerHistogramAggregation.

        Returns
        -------
        Union[GrantaServerApiAggregationsHistogram, Unset_Type]
            The histogram of this GrantaServerApiAggregationsIntegerHistogramAggregation.
        """
        return self._histogram

    @histogram.setter
    def histogram(
        self, histogram: "Union[GrantaServerApiAggregationsHistogram, Unset_Type]"
    ) -> None:
        """Sets the histogram of this GrantaServerApiAggregationsIntegerHistogramAggregation.

        Parameters
        ----------
        histogram: Union[GrantaServerApiAggregationsHistogram, Unset_Type]
            The histogram of this GrantaServerApiAggregationsIntegerHistogramAggregation.
        """
        # Field is not nullable
        if histogram is None:
            raise ValueError("Invalid value for 'histogram', must not be 'None'")
        self._histogram = histogram

    @property
    def datum_type(self) -> "str":
        """Gets the datum_type of this GrantaServerApiAggregationsIntegerHistogramAggregation.

        Returns
        -------
        str
            The datum_type of this GrantaServerApiAggregationsIntegerHistogramAggregation.
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type: "str") -> None:
        """Sets the datum_type of this GrantaServerApiAggregationsIntegerHistogramAggregation.

        Parameters
        ----------
        datum_type: str
            The datum_type of this GrantaServerApiAggregationsIntegerHistogramAggregation.
        """
        # Field is not nullable
        if datum_type is None:
            raise ValueError("Invalid value for 'datum_type', must not be 'None'")
        # Field is required
        if datum_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'datum_type', must not be 'Unset'")
        self._datum_type = datum_type

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
            other, GrantaServerApiAggregationsIntegerHistogramAggregation
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
