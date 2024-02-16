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


class GrantaServerApiAggregationsDiscreteTextAggregationDatumCriterion(
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
        "number_of_terms": "int",
        "prefix": "str",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "number_of_terms": "numberOfTerms",
        "prefix": "prefix",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        number_of_terms: "Optional[int]" = None,
        prefix: "Optional[str]" = None,
        type: "str" = "discreteText",
    ) -> None:
        """GrantaServerApiAggregationsDiscreteTextAggregationDatumCriterion - a model defined in Swagger

        Parameters
        ----------
            number_of_terms: int, optional
            prefix: str, optional
            type: str
        """
        super().__init__()
        self._number_of_terms = None
        self._prefix = None
        self._type: str = None  # type: ignore[assignment]

        if number_of_terms is not None:
            self.number_of_terms = number_of_terms
        if prefix is not None:
            self.prefix = prefix
        self.type = type

    @property
    def number_of_terms(self) -> "Optional[int]":
        """Gets the number_of_terms of this GrantaServerApiAggregationsDiscreteTextAggregationDatumCriterion.
        The maximum number of terms to return in this aggregation.

        Returns
        -------
        int
            The number_of_terms of this GrantaServerApiAggregationsDiscreteTextAggregationDatumCriterion.
        """
        return self._number_of_terms

    @number_of_terms.setter
    def number_of_terms(self, number_of_terms: "Optional[int]") -> None:
        """Sets the number_of_terms of this GrantaServerApiAggregationsDiscreteTextAggregationDatumCriterion.
        The maximum number of terms to return in this aggregation.

        Parameters
        ----------
        number_of_terms: int
            The number_of_terms of this GrantaServerApiAggregationsDiscreteTextAggregationDatumCriterion.
        """
        self._number_of_terms = number_of_terms

    @property
    def prefix(self) -> "Optional[str]":
        """Gets the prefix of this GrantaServerApiAggregationsDiscreteTextAggregationDatumCriterion.
        An optional textual prefix. If provided, only terms that start with this prefix will be  considered in the aggregation.

        Returns
        -------
        str
            The prefix of this GrantaServerApiAggregationsDiscreteTextAggregationDatumCriterion.
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix: "Optional[str]") -> None:
        """Sets the prefix of this GrantaServerApiAggregationsDiscreteTextAggregationDatumCriterion.
        An optional textual prefix. If provided, only terms that start with this prefix will be  considered in the aggregation.

        Parameters
        ----------
        prefix: str
            The prefix of this GrantaServerApiAggregationsDiscreteTextAggregationDatumCriterion.
        """
        self._prefix = prefix

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiAggregationsDiscreteTextAggregationDatumCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiAggregationsDiscreteTextAggregationDatumCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiAggregationsDiscreteTextAggregationDatumCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiAggregationsDiscreteTextAggregationDatumCriterion.
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
            other, GrantaServerApiAggregationsDiscreteTextAggregationDatumCriterion
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
