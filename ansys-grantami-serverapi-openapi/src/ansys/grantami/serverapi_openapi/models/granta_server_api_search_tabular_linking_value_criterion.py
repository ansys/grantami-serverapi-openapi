"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase
from ansys.grantami.serverapi_openapi.models.granta_server_api_search_criterion import (
    GrantaServerApiSearchCriterion,
)  # noqa: F401


if TYPE_CHECKING:
    from . import *


class GrantaServerApiSearchTabularLinkingValueCriterion(GrantaServerApiSearchCriterion):
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
        "linking_value_match_behaviour": "GrantaServerApiSearchLinkingValueMatchBehaviour",
        "type": "str",
        "values": "list[str]",
    }

    attribute_map = {
        "linking_value_match_behaviour": "linkingValueMatchBehaviour",
        "type": "type",
        "values": "values",
    }

    subtype_mapping = {
        "linkingValueMatchBehaviour": "GrantaServerApiSearchLinkingValueMatchBehaviour",
    }

    discriminator = None

    def __init__(
        self,
        *,
        linking_value_match_behaviour: "Optional[GrantaServerApiSearchLinkingValueMatchBehaviour]" = None,
        type: "str" = "tabularLinkingValue",
        values: "Optional[List[str]]" = None,
    ) -> None:
        """GrantaServerApiSearchTabularLinkingValueCriterion - a model defined in Swagger

        Parameters
        ----------
            linking_value_match_behaviour: GrantaServerApiSearchLinkingValueMatchBehaviour, optional
            type: str
            values: List[str], optional
        """
        super().__init__()
        self._values = None
        self._linking_value_match_behaviour = None
        self._type = None

        if values is not None:
            self.values = values
        if linking_value_match_behaviour is not None:
            self.linking_value_match_behaviour = linking_value_match_behaviour
        self.type = type

    @property
    def values(self) -> "list[str]":
        """Gets the values of this GrantaServerApiSearchTabularLinkingValueCriterion.

        Returns
        -------
        list[str]
            The values of this GrantaServerApiSearchTabularLinkingValueCriterion.
        """
        return self._values

    @values.setter
    def values(self, values: "list[str]") -> None:
        """Sets the values of this GrantaServerApiSearchTabularLinkingValueCriterion.

        Parameters
        ----------
        values: list[str]
            The values of this GrantaServerApiSearchTabularLinkingValueCriterion.
        """
        self._values = values

    @property
    def linking_value_match_behaviour(
        self,
    ) -> "GrantaServerApiSearchLinkingValueMatchBehaviour":
        """Gets the linking_value_match_behaviour of this GrantaServerApiSearchTabularLinkingValueCriterion.

        Returns
        -------
        GrantaServerApiSearchLinkingValueMatchBehaviour
            The linking_value_match_behaviour of this GrantaServerApiSearchTabularLinkingValueCriterion.
        """
        return self._linking_value_match_behaviour

    @linking_value_match_behaviour.setter
    def linking_value_match_behaviour(
        self,
        linking_value_match_behaviour: "GrantaServerApiSearchLinkingValueMatchBehaviour",
    ) -> None:
        """Sets the linking_value_match_behaviour of this GrantaServerApiSearchTabularLinkingValueCriterion.

        Parameters
        ----------
        linking_value_match_behaviour: GrantaServerApiSearchLinkingValueMatchBehaviour
            The linking_value_match_behaviour of this GrantaServerApiSearchTabularLinkingValueCriterion.
        """
        self._linking_value_match_behaviour = linking_value_match_behaviour

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchTabularLinkingValueCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchTabularLinkingValueCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchTabularLinkingValueCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchTabularLinkingValueCriterion.
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
        if not isinstance(other, GrantaServerApiSearchTabularLinkingValueCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
