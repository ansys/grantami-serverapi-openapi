"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase

from ansys.grantami.serverapi_openapi.models.granta_server_api_search_criterion import (
    GrantaServerApiSearchCriterion,
)  # noqa: F401

if TYPE_CHECKING:
    from . import *


class GrantaServerApiSearchFreeTextCriterion(GrantaServerApiSearchCriterion):
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

    """
    swagger_types = {
        "guids": "list[str]",
        "guids_to_boost": "list[GrantaServerApiSearchBoostByGuid]",
        "guids_to_exclude": "list[str]",
        "identities": "list[int]",
        "identities_to_boost": "list[GrantaServerApiSearchBoostByIdentity]",
        "identities_to_exclude": "list[int]",
        "type": "str",
        "value": "str",
    }

    attribute_map = {
        "guids": "guids",
        "guids_to_boost": "guidsToBoost",
        "guids_to_exclude": "guidsToExclude",
        "identities": "identities",
        "identities_to_boost": "identitiesToBoost",
        "identities_to_exclude": "identitiesToExclude",
        "type": "type",
        "value": "value",
    }

    subtype_mapping = {
        "identitiesToBoost": "GrantaServerApiSearchBoostByIdentity",
        "guidsToBoost": "GrantaServerApiSearchBoostByGuid",
    }

    def __init__(
        self,
        *,
        guids: "Optional[List[str]]" = None,
        guids_to_boost: "Optional[List[GrantaServerApiSearchBoostByGuid]]" = None,
        guids_to_exclude: "Optional[List[str]]" = None,
        identities: "Optional[List[int]]" = None,
        identities_to_boost: "Optional[List[GrantaServerApiSearchBoostByIdentity]]" = None,
        identities_to_exclude: "Optional[List[int]]" = None,
        type: "str" = "text",
        value: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiSearchFreeTextCriterion - a model defined in Swagger

        Parameters
        ----------
            guids: List[str], optional
            guids_to_boost: List[GrantaServerApiSearchBoostByGuid], optional
            guids_to_exclude: List[str], optional
            identities: List[int], optional
            identities_to_boost: List[GrantaServerApiSearchBoostByIdentity], optional
            identities_to_exclude: List[int], optional
            type: str
            value: str, optional
        """
        super().__init__()
        self._identities = None
        self._value = None
        self._identities_to_boost = None
        self._identities_to_exclude = None
        self._guids = None
        self._guids_to_boost = None
        self._guids_to_exclude = None
        self._type = None
        self.discriminator = None
        if identities is not None:
            self.identities = identities
        if value is not None:
            self.value = value
        if identities_to_boost is not None:
            self.identities_to_boost = identities_to_boost
        if identities_to_exclude is not None:
            self.identities_to_exclude = identities_to_exclude
        if guids is not None:
            self.guids = guids
        if guids_to_boost is not None:
            self.guids_to_boost = guids_to_boost
        if guids_to_exclude is not None:
            self.guids_to_exclude = guids_to_exclude
        self.type = type

    @property
    def identities(self) -> "list[int]":
        """Gets the identities of this GrantaServerApiSearchFreeTextCriterion.

        Returns
        -------
        list[int]
            The identities of this GrantaServerApiSearchFreeTextCriterion.
        """
        return self._identities

    @identities.setter
    def identities(self, identities: "list[int]") -> None:
        """Sets the identities of this GrantaServerApiSearchFreeTextCriterion.

        Parameters
        ----------
        identities: list[int]
            The identities of this GrantaServerApiSearchFreeTextCriterion.
        """
        self._identities = identities

    @property
    def value(self) -> "str":
        """Gets the value of this GrantaServerApiSearchFreeTextCriterion.

        Returns
        -------
        str
            The value of this GrantaServerApiSearchFreeTextCriterion.
        """
        return self._value

    @value.setter
    def value(self, value: "str") -> None:
        """Sets the value of this GrantaServerApiSearchFreeTextCriterion.

        Parameters
        ----------
        value: str
            The value of this GrantaServerApiSearchFreeTextCriterion.
        """
        self._value = value

    @property
    def identities_to_boost(self) -> "list[GrantaServerApiSearchBoostByIdentity]":
        """Gets the identities_to_boost of this GrantaServerApiSearchFreeTextCriterion.

        Returns
        -------
        list[GrantaServerApiSearchBoostByIdentity]
            The identities_to_boost of this GrantaServerApiSearchFreeTextCriterion.
        """
        return self._identities_to_boost

    @identities_to_boost.setter
    def identities_to_boost(
        self, identities_to_boost: "list[GrantaServerApiSearchBoostByIdentity]"
    ) -> None:
        """Sets the identities_to_boost of this GrantaServerApiSearchFreeTextCriterion.

        Parameters
        ----------
        identities_to_boost: list[GrantaServerApiSearchBoostByIdentity]
            The identities_to_boost of this GrantaServerApiSearchFreeTextCriterion.
        """
        self._identities_to_boost = identities_to_boost

    @property
    def identities_to_exclude(self) -> "list[int]":
        """Gets the identities_to_exclude of this GrantaServerApiSearchFreeTextCriterion.

        Returns
        -------
        list[int]
            The identities_to_exclude of this GrantaServerApiSearchFreeTextCriterion.
        """
        return self._identities_to_exclude

    @identities_to_exclude.setter
    def identities_to_exclude(self, identities_to_exclude: "list[int]") -> None:
        """Sets the identities_to_exclude of this GrantaServerApiSearchFreeTextCriterion.

        Parameters
        ----------
        identities_to_exclude: list[int]
            The identities_to_exclude of this GrantaServerApiSearchFreeTextCriterion.
        """
        self._identities_to_exclude = identities_to_exclude

    @property
    def guids(self) -> "list[str]":
        """Gets the guids of this GrantaServerApiSearchFreeTextCriterion.

        Returns
        -------
        list[str]
            The guids of this GrantaServerApiSearchFreeTextCriterion.
        """
        return self._guids

    @guids.setter
    def guids(self, guids: "list[str]") -> None:
        """Sets the guids of this GrantaServerApiSearchFreeTextCriterion.

        Parameters
        ----------
        guids: list[str]
            The guids of this GrantaServerApiSearchFreeTextCriterion.
        """
        self._guids = guids

    @property
    def guids_to_boost(self) -> "list[GrantaServerApiSearchBoostByGuid]":
        """Gets the guids_to_boost of this GrantaServerApiSearchFreeTextCriterion.

        Returns
        -------
        list[GrantaServerApiSearchBoostByGuid]
            The guids_to_boost of this GrantaServerApiSearchFreeTextCriterion.
        """
        return self._guids_to_boost

    @guids_to_boost.setter
    def guids_to_boost(
        self, guids_to_boost: "list[GrantaServerApiSearchBoostByGuid]"
    ) -> None:
        """Sets the guids_to_boost of this GrantaServerApiSearchFreeTextCriterion.

        Parameters
        ----------
        guids_to_boost: list[GrantaServerApiSearchBoostByGuid]
            The guids_to_boost of this GrantaServerApiSearchFreeTextCriterion.
        """
        self._guids_to_boost = guids_to_boost

    @property
    def guids_to_exclude(self) -> "list[str]":
        """Gets the guids_to_exclude of this GrantaServerApiSearchFreeTextCriterion.

        Returns
        -------
        list[str]
            The guids_to_exclude of this GrantaServerApiSearchFreeTextCriterion.
        """
        return self._guids_to_exclude

    @guids_to_exclude.setter
    def guids_to_exclude(self, guids_to_exclude: "list[str]") -> None:
        """Sets the guids_to_exclude of this GrantaServerApiSearchFreeTextCriterion.

        Parameters
        ----------
        guids_to_exclude: list[str]
            The guids_to_exclude of this GrantaServerApiSearchFreeTextCriterion.
        """
        self._guids_to_exclude = guids_to_exclude

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchFreeTextCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchFreeTextCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchFreeTextCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchFreeTextCriterion.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    def get_real_child_model(self, data: ModelBase) -> str:
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

    def to_dict(self) -> Dict:
        """Returns the model properties as a dict

        Returns
        -------
        Dict
            Dictionary indexed by property name containing all the model properties
        """
        result = {}

        for attr in self.swagger_types.keys():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(GrantaServerApiSearchFreeTextCriterion, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model

        Returns
        -------
        str
            String representation of the model as a dictionary
        """
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiSearchFreeTextCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
