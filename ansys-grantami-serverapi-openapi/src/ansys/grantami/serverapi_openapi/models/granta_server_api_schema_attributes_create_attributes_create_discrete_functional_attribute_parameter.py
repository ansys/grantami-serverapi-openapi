"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase


if TYPE_CHECKING:
    from . import *


class GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteFunctionalAttributeParameter(
    ModelBase
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
        "parameter": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "default_value": "float",
    }

    attribute_map = {
        "parameter": "parameter",
        "default_value": "defaultValue",
    }

    subtype_mapping = {
        "parameter": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
    }

    discriminator = None

    def __init__(
        self,
        *,
        parameter: "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        default_value: "Optional[float]" = None,
    ) -> None:
        """GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteFunctionalAttributeParameter - a model defined in Swagger

        Parameters
        ----------
            parameter: GrantaServerApiSchemaSlimEntitiesSlimEntity
            default_value: float, optional
        """
        self._parameter = None
        self._default_value = None

        self.parameter = parameter
        if default_value is not None:
            self.default_value = default_value

    @property
    def parameter(self) -> "GrantaServerApiSchemaSlimEntitiesSlimEntity":
        """Gets the parameter of this GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteFunctionalAttributeParameter.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimEntity
            The parameter of this GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteFunctionalAttributeParameter.
        """
        return self._parameter

    @parameter.setter
    def parameter(
        self, parameter: "GrantaServerApiSchemaSlimEntitiesSlimEntity"
    ) -> None:
        """Sets the parameter of this GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteFunctionalAttributeParameter.

        Parameters
        ----------
        parameter: GrantaServerApiSchemaSlimEntitiesSlimEntity
            The parameter of this GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteFunctionalAttributeParameter.
        """
        if parameter is None:
            raise ValueError("Invalid value for 'parameter', must not be 'None'")
        self._parameter = parameter

    @property
    def default_value(self) -> "float":
        """Gets the default_value of this GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteFunctionalAttributeParameter.

        Returns
        -------
        float
            The default_value of this GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteFunctionalAttributeParameter.
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value: "float") -> None:
        """Sets the default_value of this GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteFunctionalAttributeParameter.

        Parameters
        ----------
        default_value: float
            The default_value of this GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteFunctionalAttributeParameter.
        """
        self._default_value = default_value

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
            other,
            GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteFunctionalAttributeParameter,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
