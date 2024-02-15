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
from ansys.grantami.serverapi_openapi.models.granta_server_api_aggregations_aggregation_datum import (
    GrantaServerApiAggregationsAggregationDatum,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiAggregationsDateTimeHistogramAggregation(
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
        "histogram": "GrantaServerApiAggregationsDateTimeHistogram",
    }

    attribute_map: Dict[str, str] = {
        "datum_type": "datumType",
        "histogram": "histogram",
    }

    subtype_mapping: Dict[str, str] = {
        "histogram": "GrantaServerApiAggregationsDateTimeHistogram",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        datum_type: "str" = "dateTimeHistogram",
        histogram: "Optional[GrantaServerApiAggregationsDateTimeHistogram]" = None,
    ) -> None:
        """GrantaServerApiAggregationsDateTimeHistogramAggregation - a model defined in Swagger

        Parameters
        ----------
            datum_type: str
            histogram: GrantaServerApiAggregationsDateTimeHistogram, optional
        """
        super().__init__()
        self._histogram = None
        self._datum_type: str = None  # type: ignore[assignment]

        if histogram is not None:
            self.histogram = histogram
        self.datum_type = datum_type

    @property
    def histogram(self) -> "Optional[GrantaServerApiAggregationsDateTimeHistogram]":
        """Gets the histogram of this GrantaServerApiAggregationsDateTimeHistogramAggregation.

        Returns
        -------
        GrantaServerApiAggregationsDateTimeHistogram
            The histogram of this GrantaServerApiAggregationsDateTimeHistogramAggregation.
        """
        return self._histogram

    @histogram.setter
    def histogram(
        self, histogram: "Optional[GrantaServerApiAggregationsDateTimeHistogram]"
    ) -> None:
        """Sets the histogram of this GrantaServerApiAggregationsDateTimeHistogramAggregation.

        Parameters
        ----------
        histogram: GrantaServerApiAggregationsDateTimeHistogram
            The histogram of this GrantaServerApiAggregationsDateTimeHistogramAggregation.
        """
        self._histogram = histogram

    @property
    def datum_type(self) -> "str":
        """Gets the datum_type of this GrantaServerApiAggregationsDateTimeHistogramAggregation.

        Returns
        -------
        str
            The datum_type of this GrantaServerApiAggregationsDateTimeHistogramAggregation.
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type: "str") -> None:
        """Sets the datum_type of this GrantaServerApiAggregationsDateTimeHistogramAggregation.

        Parameters
        ----------
        datum_type: str
            The datum_type of this GrantaServerApiAggregationsDateTimeHistogramAggregation.
        """
        if datum_type is None:
            raise ValueError("Invalid value for 'datum_type', must not be 'None'")
        self._datum_type = datum_type

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
            other, GrantaServerApiAggregationsDateTimeHistogramAggregation
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
