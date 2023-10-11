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


class GrantaServerApiSearchRecordListMemberCriterion(GrantaServerApiSearchCriterion):
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
        "record_list_identifiers": "list[str]",
        "type": "str",
    }

    attribute_map = {
        "record_list_identifiers": "recordListIdentifiers",
        "type": "type",
    }

    subtype_mapping = {}

    def __init__(
        self,
        *,
        record_list_identifiers: "Optional[List[str]]" = None,
        type: "str" = "recordListMember",
    ) -> None:
        """GrantaServerApiSearchRecordListMemberCriterion - a model defined in Swagger

        Parameters
        ----------
            record_list_identifiers: List[str], optional
            type: str
        """
        super().__init__()
        self._record_list_identifiers = None
        self._type = None
        self.discriminator = None
        if record_list_identifiers is not None:
            self.record_list_identifiers = record_list_identifiers
        self.type = type

    @property
    def record_list_identifiers(self) -> "list[str]":
        """Gets the record_list_identifiers of this GrantaServerApiSearchRecordListMemberCriterion.

        Returns
        -------
        list[str]
            The record_list_identifiers of this GrantaServerApiSearchRecordListMemberCriterion.
        """
        return self._record_list_identifiers

    @record_list_identifiers.setter
    def record_list_identifiers(self, record_list_identifiers: "list[str]") -> None:
        """Sets the record_list_identifiers of this GrantaServerApiSearchRecordListMemberCriterion.

        Parameters
        ----------
        record_list_identifiers: list[str]
            The record_list_identifiers of this GrantaServerApiSearchRecordListMemberCriterion.
        """
        self._record_list_identifiers = record_list_identifiers

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchRecordListMemberCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchRecordListMemberCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchRecordListMemberCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchRecordListMemberCriterion.
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
        if issubclass(GrantaServerApiSearchRecordListMemberCriterion, dict):
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
        if not isinstance(other, GrantaServerApiSearchRecordListMemberCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
