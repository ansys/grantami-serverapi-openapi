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
    BinaryIO,
    Dict,
    List,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase, Unset, Unset_Type


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiListsDtoRecordListSearchResult(ModelBase):
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
        "header": "GrantaServerApiListsDtoRecordListHeader",
        "items": "list[GrantaServerApiListsDtoListItem]",
    }

    attribute_map: Dict[str, str] = {
        "header": "header",
        "items": "items",
    }

    subtype_mapping: Dict[str, str] = {
        "header": "GrantaServerApiListsDtoRecordListHeader",
        "items": "GrantaServerApiListsDtoListItem",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        header: "GrantaServerApiListsDtoRecordListHeader",
        items: "List[GrantaServerApiListsDtoListItem]",
    ) -> None:
        """GrantaServerApiListsDtoRecordListSearchResult - a model defined in Swagger

        Parameters
        ----------
        header: GrantaServerApiListsDtoRecordListHeader
        items: List[GrantaServerApiListsDtoListItem]
        """
        self._header: GrantaServerApiListsDtoRecordListHeader
        self._items: List[GrantaServerApiListsDtoListItem]

        self.header = header
        self.items = items

    @property
    def header(self) -> "GrantaServerApiListsDtoRecordListHeader":
        """Gets the header of this GrantaServerApiListsDtoRecordListSearchResult.

        Returns
        -------
        GrantaServerApiListsDtoRecordListHeader
            The header of this GrantaServerApiListsDtoRecordListSearchResult.
        """
        return self._header

    @header.setter
    def header(self, header: "GrantaServerApiListsDtoRecordListHeader") -> None:
        """Sets the header of this GrantaServerApiListsDtoRecordListSearchResult.

        Parameters
        ----------
        header: GrantaServerApiListsDtoRecordListHeader
            The header of this GrantaServerApiListsDtoRecordListSearchResult.
        """
        # Field is not nullable
        if header is None:
            raise ValueError("Invalid value for 'header', must not be 'None'")
        # Field is required
        if header is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'header', must not be 'Unset'")
        self._header = header

    @property
    def items(self) -> "List[GrantaServerApiListsDtoListItem]":
        """Gets the items of this GrantaServerApiListsDtoRecordListSearchResult.

        Returns
        -------
        List[GrantaServerApiListsDtoListItem]
            The items of this GrantaServerApiListsDtoRecordListSearchResult.
        """
        return self._items

    @items.setter
    def items(self, items: "List[GrantaServerApiListsDtoListItem]") -> None:
        """Sets the items of this GrantaServerApiListsDtoRecordListSearchResult.

        Parameters
        ----------
        items: List[GrantaServerApiListsDtoListItem]
            The items of this GrantaServerApiListsDtoRecordListSearchResult.
        """
        # Field is not nullable
        if items is None:
            raise ValueError("Invalid value for 'items', must not be 'None'")
        # Field is required
        if items is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'items', must not be 'Unset'")
        self._items = items

    @classmethod
    def get_real_child_model(cls, data: Dict[str, str]) -> str:
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
        if not isinstance(other, GrantaServerApiListsDtoRecordListSearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
