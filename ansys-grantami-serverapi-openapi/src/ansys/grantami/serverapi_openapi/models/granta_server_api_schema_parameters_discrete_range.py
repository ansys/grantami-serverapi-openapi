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


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaParametersDiscreteRange(ModelBase):
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
        "parameter_values": "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
    }

    attribute_map: Dict[str, str] = {
        "parameter_values": "parameterValues",
    }

    subtype_mapping: Dict[str, str] = {
        "parameterValues": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        parameter_values: "List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
    ) -> None:
        """GrantaServerApiSchemaParametersDiscreteRange - a model defined in Swagger

        Parameters
        ----------
        parameter_values: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
        """
        self._parameter_values: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]

        self.parameter_values = parameter_values

    @property
    def parameter_values(
        self,
    ) -> "List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]":
        """Gets the parameter_values of this GrantaServerApiSchemaParametersDiscreteRange.

        Returns
        -------
        List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The parameter_values of this GrantaServerApiSchemaParametersDiscreteRange.
        """
        return self._parameter_values

    @parameter_values.setter
    def parameter_values(
        self, parameter_values: "List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]"
    ) -> None:
        """Sets the parameter_values of this GrantaServerApiSchemaParametersDiscreteRange.

        Parameters
        ----------
        parameter_values: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The parameter_values of this GrantaServerApiSchemaParametersDiscreteRange.
        """
        # Field is not nullable
        if parameter_values is None:
            raise ValueError("Invalid value for 'parameter_values', must not be 'None'")
        # Field is required
        if parameter_values is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'parameter_values', must not be 'Unset'"
            )
        self._parameter_values = parameter_values

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
        if not isinstance(other, GrantaServerApiSchemaParametersDiscreteRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
