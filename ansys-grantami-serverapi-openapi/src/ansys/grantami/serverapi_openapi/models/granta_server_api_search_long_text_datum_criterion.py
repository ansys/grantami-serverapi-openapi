"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase
from ansys.grantami.serverapi_openapi.models.granta_server_api_search_datum_criterion import (
    GrantaServerApiSearchDatumCriterion,
)  # noqa: F401


if TYPE_CHECKING:
    from . import *


class GrantaServerApiSearchLongTextDatumCriterion(GrantaServerApiSearchDatumCriterion):
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
        "type": "str",
        "value": "str",
    }

    attribute_map = {
        "type": "type",
        "value": "value",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        type: "str" = "longText",
        value: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiSearchLongTextDatumCriterion - a model defined in Swagger

        Parameters
        ----------
            type: str
            value: str, optional
        """
        super().__init__()
        self._value = None
        self._type = None

        if value is not None:
            self.value = value
        self.type = type

    @property
    def value(self) -> "str":
        """Gets the value of this GrantaServerApiSearchLongTextDatumCriterion.
        Long text search value

        Returns
        -------
        str
            The value of this GrantaServerApiSearchLongTextDatumCriterion.
        """
        return self._value

    @value.setter
    def value(self, value: "str") -> None:
        """Sets the value of this GrantaServerApiSearchLongTextDatumCriterion.
        Long text search value

        Parameters
        ----------
        value: str
            The value of this GrantaServerApiSearchLongTextDatumCriterion.
        """
        self._value = value

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchLongTextDatumCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchLongTextDatumCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchLongTextDatumCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchLongTextDatumCriterion.
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
        if not isinstance(other, GrantaServerApiSearchLongTextDatumCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
