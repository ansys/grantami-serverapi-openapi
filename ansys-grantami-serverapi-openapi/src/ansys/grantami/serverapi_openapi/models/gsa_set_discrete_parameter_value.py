"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.models.gsa_set_parameter_value import GsaSetParameterValue  # noqa: F401
from ansys.grantami.serverapi_openapi.models.gsa_parameter_type import GsaParameterType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaSetDiscreteParameterValue(GsaSetParameterValue):
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
        "parameter_type": "GsaParameterType",
        "parameter_value": "GsaSlimEntity",
    }

    attribute_map: dict[str, str] = {
        "parameter_type": "parameterType",
        "parameter_value": "parameterValue",
    }

    subtype_mapping: dict[str, str] = {
        "parameterValue": "GsaSlimEntity",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, parameter_type: "GsaParameterType" = GsaParameterType.DISCRETE, parameter_value: "GsaSlimEntity",) -> None:
        """GsaSetDiscreteParameterValue - a model defined in Swagger

        Parameters
        ----------
        parameter_type: GsaParameterType
        parameter_value: GsaSlimEntity
        """
        super().__init__(parameter_type=parameter_type)
        self._parameter_value: GsaSlimEntity

        self.parameter_value = parameter_value

    @property
    def parameter_value(self) -> "GsaSlimEntity":
        """Gets the parameter_value of this GsaSetDiscreteParameterValue.

        Returns
        -------
        GsaSlimEntity
            The parameter_value of this GsaSetDiscreteParameterValue.
        """
        return self._parameter_value

    @parameter_value.setter
    def parameter_value(self, parameter_value: "GsaSlimEntity") -> None:
        """Sets the parameter_value of this GsaSetDiscreteParameterValue.

        Parameters
        ----------
        parameter_value: GsaSlimEntity
            The parameter_value of this GsaSetDiscreteParameterValue.
        """
        # Field is not nullable
        if parameter_value is None:
            raise ValueError("Invalid value for 'parameter_value', must not be 'None'")
        # Field is required
        if parameter_value is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'parameter_value', must not be 'Unset'")
        self._parameter_value = parameter_value

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
        if not isinstance(other, GsaSetDiscreteParameterValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

