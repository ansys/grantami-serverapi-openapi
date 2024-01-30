"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase


if TYPE_CHECKING:
    from . import *


class GrantaServerApiListsDtoCreateRecordListItemsInfo(ModelBase):
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
        "items": "list[GrantaServerApiListsDtoCreateListItem]",
    }

    attribute_map = {
        "items": "items",
    }

    subtype_mapping = {
        "items": "GrantaServerApiListsDtoCreateListItem",
    }

    discriminator = None

    def __init__(
        self,
        *,
        items: "List[GrantaServerApiListsDtoCreateListItem]",
    ) -> None:
        """GrantaServerApiListsDtoCreateRecordListItemsInfo - a model defined in Swagger

        Parameters
        ----------
            items: List[GrantaServerApiListsDtoCreateListItem]
        """
        self._items = None

        self.items = items

    @property
    def items(self) -> "list[GrantaServerApiListsDtoCreateListItem]":
        """Gets the items of this GrantaServerApiListsDtoCreateRecordListItemsInfo.

        Returns
        -------
        list[GrantaServerApiListsDtoCreateListItem]
            The items of this GrantaServerApiListsDtoCreateRecordListItemsInfo.
        """
        return self._items

    @items.setter
    def items(self, items: "list[GrantaServerApiListsDtoCreateListItem]") -> None:
        """Sets the items of this GrantaServerApiListsDtoCreateRecordListItemsInfo.

        Parameters
        ----------
        items: list[GrantaServerApiListsDtoCreateListItem]
            The items of this GrantaServerApiListsDtoCreateRecordListItemsInfo.
        """
        if items is None:
            raise ValueError("Invalid value for 'items', must not be 'None'")
        self._items = items

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
        if not isinstance(other, GrantaServerApiListsDtoCreateRecordListItemsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
