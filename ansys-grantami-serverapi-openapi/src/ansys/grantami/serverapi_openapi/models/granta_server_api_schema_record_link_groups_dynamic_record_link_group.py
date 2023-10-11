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

from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_record_link_groups_record_link_group import (
    GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup,
)  # noqa: F401

if TYPE_CHECKING:
    from . import *


class GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup(
    GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup
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
        "attribute_pairs": "list[GrantaServerApiSchemaRecordLinkGroupsAttributeLinkPair]",
        "display_names": "dict(str, str)",
        "forbid_orphans": "bool",
        "guid": "str",
        "identity": "int",
        "link_info": "GrantaServerApiSchemaRecordLinkGroupsLinkInfo",
        "name": "str",
        "referential_integrity_model": "GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel",
        "reverse_display_names": "dict(str, str)",
        "reverse_name": "str",
        "type": "str",
    }

    attribute_map = {
        "attribute_pairs": "attributePairs",
        "display_names": "displayNames",
        "forbid_orphans": "forbidOrphans",
        "guid": "guid",
        "identity": "identity",
        "link_info": "linkInfo",
        "name": "name",
        "referential_integrity_model": "referentialIntegrityModel",
        "reverse_display_names": "reverseDisplayNames",
        "reverse_name": "reverseName",
        "type": "type",
    }

    subtype_mapping = {
        "referentialIntegrityModel": "GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel",
        "attributePairs": "GrantaServerApiSchemaRecordLinkGroupsAttributeLinkPair",
    }

    def __init__(
        self,
        *,
        attribute_pairs: "Optional[List[GrantaServerApiSchemaRecordLinkGroupsAttributeLinkPair]]" = None,
        display_names: "Optional[Dict[str, str]]" = None,
        forbid_orphans: "Optional[bool]" = None,
        guid: "Optional[str]" = None,
        identity: "Optional[int]" = None,
        link_info: "Optional[GrantaServerApiSchemaRecordLinkGroupsLinkInfo]" = None,
        name: "Optional[str]" = None,
        referential_integrity_model: "Optional[GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel]" = None,
        reverse_display_names: "Optional[Dict[str, str]]" = None,
        reverse_name: "Optional[str]" = None,
        type: "str" = "dynamic",
    ) -> None:
        """GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup - a model defined in Swagger

        Parameters
        ----------
            attribute_pairs: List[GrantaServerApiSchemaRecordLinkGroupsAttributeLinkPair], optional
            display_names: Dict[str, str], optional
            forbid_orphans: bool, optional
            guid: str, optional
            identity: int, optional
            link_info: GrantaServerApiSchemaRecordLinkGroupsLinkInfo, optional
            name: str, optional
            referential_integrity_model: GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel, optional
            reverse_display_names: Dict[str, str], optional
            reverse_name: str, optional
            type: str
        """
        super().__init__(
            display_names=display_names,
            guid=guid,
            identity=identity,
            link_info=link_info,
            name=name,
            reverse_display_names=reverse_display_names,
            reverse_name=reverse_name,
        )
        self._forbid_orphans = None
        self._referential_integrity_model = None
        self._attribute_pairs = None
        self._type = None
        self.discriminator = None
        if forbid_orphans is not None:
            self.forbid_orphans = forbid_orphans
        if referential_integrity_model is not None:
            self.referential_integrity_model = referential_integrity_model
        if attribute_pairs is not None:
            self.attribute_pairs = attribute_pairs
        self.type = type

    @property
    def forbid_orphans(self) -> "bool":
        """Gets the forbid_orphans of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.

        Returns
        -------
        bool
            The forbid_orphans of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.
        """
        return self._forbid_orphans

    @forbid_orphans.setter
    def forbid_orphans(self, forbid_orphans: "bool") -> None:
        """Sets the forbid_orphans of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.

        Parameters
        ----------
        forbid_orphans: bool
            The forbid_orphans of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.
        """
        self._forbid_orphans = forbid_orphans

    @property
    def referential_integrity_model(
        self,
    ) -> "GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel":
        """Gets the referential_integrity_model of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.

        Returns
        -------
        GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel
            The referential_integrity_model of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.
        """
        return self._referential_integrity_model

    @referential_integrity_model.setter
    def referential_integrity_model(
        self,
        referential_integrity_model: "GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel",
    ) -> None:
        """Sets the referential_integrity_model of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.

        Parameters
        ----------
        referential_integrity_model: GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel
            The referential_integrity_model of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.
        """
        self._referential_integrity_model = referential_integrity_model

    @property
    def attribute_pairs(
        self,
    ) -> "list[GrantaServerApiSchemaRecordLinkGroupsAttributeLinkPair]":
        """Gets the attribute_pairs of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.

        Returns
        -------
        list[GrantaServerApiSchemaRecordLinkGroupsAttributeLinkPair]
            The attribute_pairs of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.
        """
        return self._attribute_pairs

    @attribute_pairs.setter
    def attribute_pairs(
        self,
        attribute_pairs: "list[GrantaServerApiSchemaRecordLinkGroupsAttributeLinkPair]",
    ) -> None:
        """Sets the attribute_pairs of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.

        Parameters
        ----------
        attribute_pairs: list[GrantaServerApiSchemaRecordLinkGroupsAttributeLinkPair]
            The attribute_pairs of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.
        """
        self._attribute_pairs = attribute_pairs

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.
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
            GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup, dict
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
            other, GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
