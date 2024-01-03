"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase
from ansys.grantami.serverapi_openapi.models.granta_server_api_search_parameter_constraint import (
    GrantaServerApiSearchParameterConstraint,
)  # noqa: F401


if TYPE_CHECKING:
    from . import *


class GrantaServerApiSearchDiscreteParameterValueConstraint(
    GrantaServerApiSearchParameterConstraint
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
        "_none": "list[float]",
        "any": "list[float]",
        "parameter": "GrantaServerApiObjectIdentifier",
        "type": "str",
    }

    attribute_map = {
        "_none": "none",
        "any": "any",
        "parameter": "parameter",
        "type": "type",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        _none: "Optional[List[float]]" = None,
        any: "Optional[List[float]]" = None,
        parameter: "Optional[GrantaServerApiObjectIdentifier]" = None,
        type: "str" = "discreteValue",
    ) -> None:
        """GrantaServerApiSearchDiscreteParameterValueConstraint - a model defined in Swagger

        Parameters
        ----------
            _none: List[float], optional
            any: List[float], optional
            parameter: GrantaServerApiObjectIdentifier, optional
            type: str
        """
        super().__init__(parameter=parameter)
        self._any = None
        self.__none = None
        self._type = None

        if any is not None:
            self.any = any
        if _none is not None:
            self._none = _none
        self.type = type

    @property
    def any(self) -> "list[float]":
        """Gets the any of this GrantaServerApiSearchDiscreteParameterValueConstraint.

        Returns
        -------
        list[float]
            The any of this GrantaServerApiSearchDiscreteParameterValueConstraint.
        """
        return self._any

    @any.setter
    def any(self, any: "list[float]") -> None:
        """Sets the any of this GrantaServerApiSearchDiscreteParameterValueConstraint.

        Parameters
        ----------
        any: list[float]
            The any of this GrantaServerApiSearchDiscreteParameterValueConstraint.
        """
        self._any = any

    @property
    def _none(self) -> "list[float]":
        """Gets the _none of this GrantaServerApiSearchDiscreteParameterValueConstraint.

        Returns
        -------
        list[float]
            The _none of this GrantaServerApiSearchDiscreteParameterValueConstraint.
        """
        return self.__none

    @_none.setter
    def _none(self, _none: "list[float]") -> None:
        """Sets the _none of this GrantaServerApiSearchDiscreteParameterValueConstraint.

        Parameters
        ----------
        _none: list[float]
            The _none of this GrantaServerApiSearchDiscreteParameterValueConstraint.
        """
        self.__none = _none

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchDiscreteParameterValueConstraint.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchDiscreteParameterValueConstraint.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchDiscreteParameterValueConstraint.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchDiscreteParameterValueConstraint.
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
        if not isinstance(other, GrantaServerApiSearchDiscreteParameterValueConstraint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
