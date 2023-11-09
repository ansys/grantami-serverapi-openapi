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


if TYPE_CHECKING:
    from . import *


class GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroupsInfo(ModelBase):
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
        "record_link_groups": "list[GrantaServerApiSchemaSlimEntitiesSlimRecordLinkGroup]",
    }

    attribute_map = {
        "record_link_groups": "recordLinkGroups",
    }

    subtype_mapping = {
        "recordLinkGroups": "GrantaServerApiSchemaSlimEntitiesSlimRecordLinkGroup",
    }

    discriminator = None

    def __init__(
        self,
        *,
        record_link_groups: "Optional[List[GrantaServerApiSchemaSlimEntitiesSlimRecordLinkGroup]]" = None,
    ) -> None:
        """GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroupsInfo - a model defined in Swagger

        Parameters
        ----------
            record_link_groups: List[GrantaServerApiSchemaSlimEntitiesSlimRecordLinkGroup], optional
        """
        self._record_link_groups = None

        if record_link_groups is not None:
            self.record_link_groups = record_link_groups

    @property
    def record_link_groups(
        self,
    ) -> "list[GrantaServerApiSchemaSlimEntitiesSlimRecordLinkGroup]":
        """Gets the record_link_groups of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroupsInfo.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimRecordLinkGroup]
            The record_link_groups of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroupsInfo.
        """
        return self._record_link_groups

    @record_link_groups.setter
    def record_link_groups(
        self,
        record_link_groups: "list[GrantaServerApiSchemaSlimEntitiesSlimRecordLinkGroup]",
    ) -> None:
        """Sets the record_link_groups of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroupsInfo.

        Parameters
        ----------
        record_link_groups: list[GrantaServerApiSchemaSlimEntitiesSlimRecordLinkGroup]
            The record_link_groups of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroupsInfo.
        """
        self._record_link_groups = record_link_groups

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
        if issubclass(GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroupsInfo, dict):
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
        if not isinstance(
            other, GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroupsInfo
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
