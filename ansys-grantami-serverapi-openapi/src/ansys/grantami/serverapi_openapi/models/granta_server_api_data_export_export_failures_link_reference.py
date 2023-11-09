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


class GrantaServerApiDataExportExportFailuresLinkReference(ModelBase):
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
        "link_type": "GrantaServerApiLinkAttributeType",
        "link_guid": "str",
        "link_identity": "int",
        "target_database_guid": "str",
    }

    attribute_map = {
        "link_type": "linkType",
        "link_guid": "linkGuid",
        "link_identity": "linkIdentity",
        "target_database_guid": "targetDatabaseGuid",
    }

    subtype_mapping = {
        "linkType": "GrantaServerApiLinkAttributeType",
    }

    discriminator = None

    def __init__(
        self,
        *,
        link_type: "GrantaServerApiLinkAttributeType",
        link_guid: "Optional[str]" = None,
        link_identity: "Optional[int]" = None,
        target_database_guid: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiDataExportExportFailuresLinkReference - a model defined in Swagger

        Parameters
        ----------
            link_type: GrantaServerApiLinkAttributeType
            link_guid: str, optional
            link_identity: int, optional
            target_database_guid: str, optional
        """
        self._target_database_guid = None
        self._link_identity = None
        self._link_guid = None
        self._link_type = None

        if target_database_guid is not None:
            self.target_database_guid = target_database_guid
        if link_identity is not None:
            self.link_identity = link_identity
        if link_guid is not None:
            self.link_guid = link_guid
        self.link_type = link_type

    @property
    def target_database_guid(self) -> "str":
        """Gets the target_database_guid of this GrantaServerApiDataExportExportFailuresLinkReference.

        Returns
        -------
        str
            The target_database_guid of this GrantaServerApiDataExportExportFailuresLinkReference.
        """
        return self._target_database_guid

    @target_database_guid.setter
    def target_database_guid(self, target_database_guid: "str") -> None:
        """Sets the target_database_guid of this GrantaServerApiDataExportExportFailuresLinkReference.

        Parameters
        ----------
        target_database_guid: str
            The target_database_guid of this GrantaServerApiDataExportExportFailuresLinkReference.
        """
        self._target_database_guid = target_database_guid

    @property
    def link_identity(self) -> "int":
        """Gets the link_identity of this GrantaServerApiDataExportExportFailuresLinkReference.

        Returns
        -------
        int
            The link_identity of this GrantaServerApiDataExportExportFailuresLinkReference.
        """
        return self._link_identity

    @link_identity.setter
    def link_identity(self, link_identity: "int") -> None:
        """Sets the link_identity of this GrantaServerApiDataExportExportFailuresLinkReference.

        Parameters
        ----------
        link_identity: int
            The link_identity of this GrantaServerApiDataExportExportFailuresLinkReference.
        """
        self._link_identity = link_identity

    @property
    def link_guid(self) -> "str":
        """Gets the link_guid of this GrantaServerApiDataExportExportFailuresLinkReference.

        Returns
        -------
        str
            The link_guid of this GrantaServerApiDataExportExportFailuresLinkReference.
        """
        return self._link_guid

    @link_guid.setter
    def link_guid(self, link_guid: "str") -> None:
        """Sets the link_guid of this GrantaServerApiDataExportExportFailuresLinkReference.

        Parameters
        ----------
        link_guid: str
            The link_guid of this GrantaServerApiDataExportExportFailuresLinkReference.
        """
        self._link_guid = link_guid

    @property
    def link_type(self) -> "GrantaServerApiLinkAttributeType":
        """Gets the link_type of this GrantaServerApiDataExportExportFailuresLinkReference.

        Returns
        -------
        GrantaServerApiLinkAttributeType
            The link_type of this GrantaServerApiDataExportExportFailuresLinkReference.
        """
        return self._link_type

    @link_type.setter
    def link_type(self, link_type: "GrantaServerApiLinkAttributeType") -> None:
        """Sets the link_type of this GrantaServerApiDataExportExportFailuresLinkReference.

        Parameters
        ----------
        link_type: GrantaServerApiLinkAttributeType
            The link_type of this GrantaServerApiDataExportExportFailuresLinkReference.
        """
        if link_type is None:
            raise ValueError("Invalid value for 'link_type', must not be 'None'")
        self._link_type = link_type

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
        if issubclass(GrantaServerApiDataExportExportFailuresLinkReference, dict):
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
        if not isinstance(other, GrantaServerApiDataExportExportFailuresLinkReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
