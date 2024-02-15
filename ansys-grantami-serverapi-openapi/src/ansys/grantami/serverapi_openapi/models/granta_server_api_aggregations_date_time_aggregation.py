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


class GrantaServerApiAggregationsDateTimeAggregation(
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
        "maximum": "datetime",
        "minimum": "datetime",
    }

    attribute_map: Dict[str, str] = {
        "datum_type": "datumType",
        "maximum": "maximum",
        "minimum": "minimum",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        datum_type: "str" = "dateTime",
        maximum: "Optional[datetime]" = None,
        minimum: "Optional[datetime]" = None,
    ) -> None:
        """GrantaServerApiAggregationsDateTimeAggregation - a model defined in Swagger

        Parameters
        ----------
            datum_type: str
            maximum: datetime, optional
            minimum: datetime, optional
        """
        super().__init__()
        self._minimum = None
        self._maximum = None
        self._datum_type: str = None  # type: ignore[assignment]

        if minimum is not None:
            self.minimum = minimum
        if maximum is not None:
            self.maximum = maximum
        self.datum_type = datum_type

    @property
    def minimum(self) -> "Optional[datetime]":
        """Gets the minimum of this GrantaServerApiAggregationsDateTimeAggregation.

        Returns
        -------
        datetime
            The minimum of this GrantaServerApiAggregationsDateTimeAggregation.
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum: "Optional[datetime]") -> None:
        """Sets the minimum of this GrantaServerApiAggregationsDateTimeAggregation.

        Parameters
        ----------
        minimum: datetime
            The minimum of this GrantaServerApiAggregationsDateTimeAggregation.
        """
        self._minimum = minimum

    @property
    def maximum(self) -> "Optional[datetime]":
        """Gets the maximum of this GrantaServerApiAggregationsDateTimeAggregation.

        Returns
        -------
        datetime
            The maximum of this GrantaServerApiAggregationsDateTimeAggregation.
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum: "Optional[datetime]") -> None:
        """Sets the maximum of this GrantaServerApiAggregationsDateTimeAggregation.

        Parameters
        ----------
        maximum: datetime
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
        if not isinstance(other, GrantaServerApiAggregationsDateTimeAggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
