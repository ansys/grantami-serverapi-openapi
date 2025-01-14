"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.models.gsa_record_link_group import GsaRecordLinkGroup  # noqa: F401
from ansys.grantami.serverapi_openapi.models.gsa_record_link_group_type import GsaRecordLinkGroupType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaCrossDatabaseRecordLinkGroup(GsaRecordLinkGroup):
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
        "display_names": "dict(str, str)",
        "guid": "str",
        "include_indirect_links": "bool",
        "link_info": "GsaLinkInfo",
        "name": "str",
        "reverse_name": "str",
        "type": "GsaRecordLinkGroupType",
        "identity": "int",
        "reverse_display_names": "dict(str, str)",
    }

    attribute_map: dict[str, str] = {
        "display_names": "displayNames",
        "guid": "guid",
        "include_indirect_links": "includeIndirectLinks",
        "link_info": "linkInfo",
        "name": "name",
        "reverse_name": "reverseName",
        "type": "type",
        "identity": "identity",
        "reverse_display_names": "reverseDisplayNames",
    }

    subtype_mapping: dict[str, str] = {
    }

    discriminator: Optional[str] = None

    def __init__(self, *, display_names: "dict[str, str]", guid: "str", include_indirect_links: "bool", link_info: "GsaLinkInfo", name: "str", reverse_name: "str", type: "GsaRecordLinkGroupType" = GsaRecordLinkGroupType.CROSSDATABASE, identity: "Union[int, None, Unset_Type]" = Unset, reverse_display_names: "Union[dict[str, str], None, Unset_Type]" = Unset,) -> None:
        """GsaCrossDatabaseRecordLinkGroup - a model defined in Swagger

        Parameters
        ----------
        display_names: dict[str, str]
        guid: str
        include_indirect_links: bool
        link_info: GsaLinkInfo
        name: str
        reverse_name: str
        type: GsaRecordLinkGroupType
        identity: int, optional
        reverse_display_names: dict[str, str], optional
        """
        super().__init__(display_names=display_names, guid=guid, link_info=link_info, name=name, reverse_name=reverse_name, type=type, identity=identity, reverse_display_names=reverse_display_names)
        self._include_indirect_links: bool

        self.include_indirect_links = include_indirect_links

    @property
    def include_indirect_links(self) -> "bool":
        """Gets the include_indirect_links of this GsaCrossDatabaseRecordLinkGroup.

        Returns
        -------
        bool
            The include_indirect_links of this GsaCrossDatabaseRecordLinkGroup.
        """
        return self._include_indirect_links

    @include_indirect_links.setter
    def include_indirect_links(self, include_indirect_links: "bool") -> None:
        """Sets the include_indirect_links of this GsaCrossDatabaseRecordLinkGroup.

        Parameters
        ----------
        include_indirect_links: bool
            The include_indirect_links of this GsaCrossDatabaseRecordLinkGroup.
        """
        # Field is not nullable
        if include_indirect_links is None:
            raise ValueError("Invalid value for 'include_indirect_links', must not be 'None'")
        # Field is required
        if include_indirect_links is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'include_indirect_links', must not be 'Unset'")
        self._include_indirect_links = include_indirect_links

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
        if not isinstance(other, GsaCrossDatabaseRecordLinkGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

