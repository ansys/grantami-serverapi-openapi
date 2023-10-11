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

from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_record_link_groups_update_record_link_group import (
    GrantaServerApiSchemaRecordLinkGroupsUpdateRecordLinkGroup,
)  # noqa: F401

if TYPE_CHECKING:
    from . import *


class GrantaServerApiSchemaRecordLinkGroupsUpdateStaticRecordLinkGroup(
    GrantaServerApiSchemaRecordLinkGroupsUpdateRecordLinkGroup
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

    """
    swagger_types = {
        "guid": "str",
        "include_indirect_links": "bool",
        "name": "str",
        "reverse_name": "str",
        "type": "str",
    }

    attribute_map = {
        "guid": "guid",
        "include_indirect_links": "includeIndirectLinks",
        "name": "name",
        "reverse_name": "reverseName",
        "type": "type",
    }

    subtype_mapping = {}

    def __init__(
        self,
        *,
        guid: "Optional[str]" = None,
        include_indirect_links: "Optional[bool]" = None,
        name: "Optional[str]" = None,
        reverse_name: "Optional[str]" = None,
        type: "str" = "static",
    ) -> None:
        """GrantaServerApiSchemaRecordLinkGroupsUpdateStaticRecordLinkGroup - a model defined in Swagger

        Parameters
        ----------
            guid: str, optional
            include_indirect_links: bool, optional
            name: str, optional
            reverse_name: str, optional
            type: str
        """
        super().__init__(guid=guid, name=name, reverse_name=reverse_name)
        self._include_indirect_links = None
        self._type = None
        self.discriminator = None
        if include_indirect_links is not None:
            self.include_indirect_links = include_indirect_links
        self.type = type

    @property
    def include_indirect_links(self) -> "bool":
        """Gets the include_indirect_links of this GrantaServerApiSchemaRecordLinkGroupsUpdateStaticRecordLinkGroup.

        Returns
        -------
        bool
            The include_indirect_links of this GrantaServerApiSchemaRecordLinkGroupsUpdateStaticRecordLinkGroup.
        """
        return self._include_indirect_links

    @include_indirect_links.setter
    def include_indirect_links(self, include_indirect_links: "bool") -> None:
        """Sets the include_indirect_links of this GrantaServerApiSchemaRecordLinkGroupsUpdateStaticRecordLinkGroup.

        Parameters
        ----------
        include_indirect_links: bool
            The include_indirect_links of this GrantaServerApiSchemaRecordLinkGroupsUpdateStaticRecordLinkGroup.
        """
        self._include_indirect_links = include_indirect_links

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaRecordLinkGroupsUpdateStaticRecordLinkGroup.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaRecordLinkGroupsUpdateStaticRecordLinkGroup.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaRecordLinkGroupsUpdateStaticRecordLinkGroup.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaRecordLinkGroupsUpdateStaticRecordLinkGroup.
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
        if issubclass(
            GrantaServerApiSchemaRecordLinkGroupsUpdateStaticRecordLinkGroup, dict
        ):
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
            other, GrantaServerApiSchemaRecordLinkGroupsUpdateStaticRecordLinkGroup
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
