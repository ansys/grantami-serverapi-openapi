"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase
from ansys.grantami.serverapi_openapi.models.granta_server_api_aggregations_aggregation_datum_criterion import (
    GrantaServerApiAggregationsAggregationDatumCriterion,
)  # noqa: F401


if TYPE_CHECKING:
    from . import *


class GrantaServerApiAggregationsFloatFunctionalAggregationDatumCriterion(
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
    swagger_types = {
        "number_of_parameter_values": "int",
        "type": "str",
    }

    attribute_map = {
        "number_of_parameter_values": "numberOfParameterValues",
        "type": "type",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        number_of_parameter_values: "Optional[int]" = None,
        type: "str" = "floatFunctionalGraph",
    ) -> None:
        """GrantaServerApiAggregationsFloatFunctionalAggregationDatumCriterion - a model defined in Swagger

        Parameters
        ----------
            number_of_parameter_values: int, optional
            type: str
        """
        super().__init__()
        self._number_of_parameter_values = None
        self._type = None

        if number_of_parameter_values is not None:
            self.number_of_parameter_values = number_of_parameter_values
        self.type = type

    @property
    def number_of_parameter_values(self) -> "int":
        """Gets the number_of_parameter_values of this GrantaServerApiAggregationsFloatFunctionalAggregationDatumCriterion.
        The maximum number of values to return in this aggregation.

        Returns
        -------
        int
            The number_of_parameter_values of this GrantaServerApiAggregationsFloatFunctionalAggregationDatumCriterion.
        """
        return self._number_of_parameter_values

    @number_of_parameter_values.setter
    def number_of_parameter_values(self, number_of_parameter_values: "int") -> None:
        """Sets the number_of_parameter_values of this GrantaServerApiAggregationsFloatFunctionalAggregationDatumCriterion.
        The maximum number of values to return in this aggregation.

        Parameters
        ----------
        number_of_parameter_values: int
            The number_of_parameter_values of this GrantaServerApiAggregationsFloatFunctionalAggregationDatumCriterion.
        """
        self._number_of_parameter_values = number_of_parameter_values

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiAggregationsFloatFunctionalAggregationDatumCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiAggregationsFloatFunctionalAggregationDatumCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiAggregationsFloatFunctionalAggregationDatumCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiAggregationsFloatFunctionalAggregationDatumCriterion.
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
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(
            other, GrantaServerApiAggregationsFloatFunctionalAggregationDatumCriterion
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
