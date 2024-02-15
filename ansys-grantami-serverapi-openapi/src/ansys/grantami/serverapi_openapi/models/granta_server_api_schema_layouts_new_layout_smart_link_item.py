"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    BinaryIO,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase
from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_layouts_new_layout_item import (
    GrantaServerApiSchemaLayoutsNewLayoutItem,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem(
    GrantaServerApiSchemaLayoutsNewLayoutItem
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
    swagger_types: Dict[str, str] = {
        "link_group_guid": "str",
        "forwards": "bool",
        "guid": "str",
        "item_type": "str",
    }

    attribute_map: Dict[str, str] = {
        "link_group_guid": "linkGroupGuid",
        "forwards": "forwards",
        "guid": "guid",
        "item_type": "itemType",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        link_group_guid: "str",
        forwards: "Optional[bool]" = None,
        guid: "Optional[str]" = None,
        item_type: "str" = "smartLink",
    ) -> None:
        """GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem - a model defined in Swagger

        Parameters
        ----------
            link_group_guid: str
            forwards: bool, optional
            guid: str, optional
            item_type: str
        """
        super().__init__(guid=guid)
        self._item_type: str = None  # type: ignore[assignment]
        self._forwards = None
        self._link_group_guid: str = None  # type: ignore[assignment]

        self.item_type = item_type
        if forwards is not None:
            self.forwards = forwards
        self.link_group_guid = link_group_guid

    @property
    def item_type(self) -> "str":
        """Gets the item_type of this GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem.

        Returns
        -------
        str
            The item_type of this GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem.
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type: "str") -> None:
        """Sets the item_type of this GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem.

        Parameters
        ----------
        item_type: str
            The item_type of this GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem.
        """
        if item_type is None:
            raise ValueError("Invalid value for 'item_type', must not be 'None'")
        self._item_type = item_type

    @property
    def forwards(self) -> "Optional[bool]":
        """Gets the forwards of this GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem.

        Returns
        -------
        bool
            The forwards of this GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem.
        """
        return self._forwards

    @forwards.setter
    def forwards(self, forwards: "Optional[bool]") -> None:
        """Sets the forwards of this GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem.

        Parameters
        ----------
        forwards: bool
            The forwards of this GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem.
        """
        self._forwards = forwards

    @property
    def link_group_guid(self) -> "str":
        """Gets the link_group_guid of this GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem.

        Returns
        -------
        str
            The link_group_guid of this GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem.
        """
        return self._link_group_guid

    @link_group_guid.setter
    def link_group_guid(self, link_group_guid: "str") -> None:
        """Sets the link_group_guid of this GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem.

        Parameters
        ----------
        link_group_guid: str
            The link_group_guid of this GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem.
        """
        if link_group_guid is None:
            raise ValueError("Invalid value for 'link_group_guid', must not be 'None'")
        self._link_group_guid = link_group_guid

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
        return self.to_str()  # type: ignore[no-any-return]

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
