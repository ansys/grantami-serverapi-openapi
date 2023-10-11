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

from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_layouts_layout_item import (
    GrantaServerApiSchemaLayoutsLayoutItem,
)  # noqa: F401

if TYPE_CHECKING:
    from . import *


class GrantaServerApiSchemaLayoutsLayoutAttributeItem(
    GrantaServerApiSchemaLayoutsLayoutItem
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
        "attribute_type": "GrantaServerApiAttributeType",
        "guid": "str",
        "item_type": "str",
        "meta_attributes": "list[GrantaServerApiSchemaLayoutsLayoutAttributeItem]",
        "name": "str",
        "read_only": "bool",
        "required": "bool",
        "tabular_columns": "list[GrantaServerApiSchemaLayoutsLayoutTabularColumn]",
        "underlying_entity_guid": "str",
    }

    attribute_map = {
        "attribute_type": "attributeType",
        "guid": "guid",
        "item_type": "itemType",
        "meta_attributes": "metaAttributes",
        "name": "name",
        "read_only": "readOnly",
        "required": "required",
        "tabular_columns": "tabularColumns",
        "underlying_entity_guid": "underlyingEntityGuid",
    }

    subtype_mapping = {
        "attributeType": "GrantaServerApiAttributeType",
        "metaAttributes": "GrantaServerApiSchemaLayoutsLayoutAttributeItem",
        "tabularColumns": "GrantaServerApiSchemaLayoutsLayoutTabularColumn",
    }

    def __init__(
        self,
        *,
        attribute_type: "Optional[GrantaServerApiAttributeType]" = None,
        guid: "Optional[str]" = None,
        item_type: "str" = "attribute",
        meta_attributes: "Optional[List[GrantaServerApiSchemaLayoutsLayoutAttributeItem]]" = None,
        name: "Optional[str]" = None,
        read_only: "Optional[bool]" = None,
        required: "Optional[bool]" = None,
        tabular_columns: "Optional[List[GrantaServerApiSchemaLayoutsLayoutTabularColumn]]" = None,
        underlying_entity_guid: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiSchemaLayoutsLayoutAttributeItem - a model defined in Swagger

        Parameters
        ----------
            attribute_type: GrantaServerApiAttributeType, optional
            guid: str, optional
            item_type: str
            meta_attributes: List[GrantaServerApiSchemaLayoutsLayoutAttributeItem], optional
            name: str, optional
            read_only: bool, optional
            required: bool, optional
            tabular_columns: List[GrantaServerApiSchemaLayoutsLayoutTabularColumn], optional
            underlying_entity_guid: str, optional
        """
        super().__init__(
            guid=guid, name=name, underlying_entity_guid=underlying_entity_guid
        )
        self._item_type = None
        self._attribute_type = None
        self._required = None
        self._read_only = None
        self._meta_attributes = None
        self._tabular_columns = None
        self.discriminator = None
        self.item_type = item_type
        if attribute_type is not None:
            self.attribute_type = attribute_type
        if required is not None:
            self.required = required
        if read_only is not None:
            self.read_only = read_only
        if meta_attributes is not None:
            self.meta_attributes = meta_attributes
        if tabular_columns is not None:
            self.tabular_columns = tabular_columns

    @property
    def item_type(self) -> "str":
        """Gets the item_type of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.

        Returns
        -------
        str
            The item_type of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type: "str") -> None:
        """Sets the item_type of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.

        Parameters
        ----------
        item_type: str
            The item_type of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.
        """
        if item_type is None:
            raise ValueError("Invalid value for 'item_type', must not be 'None'")
        self._item_type = item_type

    @property
    def attribute_type(self) -> "GrantaServerApiAttributeType":
        """Gets the attribute_type of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.

        Returns
        -------
        GrantaServerApiAttributeType
            The attribute_type of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.
        """
        return self._attribute_type

    @attribute_type.setter
    def attribute_type(self, attribute_type: "GrantaServerApiAttributeType") -> None:
        """Sets the attribute_type of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.

        Parameters
        ----------
        attribute_type: GrantaServerApiAttributeType
            The attribute_type of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.
        """
        self._attribute_type = attribute_type

    @property
    def required(self) -> "bool":
        """Gets the required of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.

        Returns
        -------
        bool
            The required of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.
        """
        return self._required

    @required.setter
    def required(self, required: "bool") -> None:
        """Sets the required of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.

        Parameters
        ----------
        required: bool
            The required of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.
        """
        self._required = required

    @property
    def read_only(self) -> "bool":
        """Gets the read_only of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.

        Returns
        -------
        bool
            The read_only of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only: "bool") -> None:
        """Sets the read_only of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.

        Parameters
        ----------
        read_only: bool
            The read_only of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.
        """
        self._read_only = read_only

    @property
    def meta_attributes(
        self,
    ) -> "list[GrantaServerApiSchemaLayoutsLayoutAttributeItem]":
        """Gets the meta_attributes of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.

        Returns
        -------
        list[GrantaServerApiSchemaLayoutsLayoutAttributeItem]
            The meta_attributes of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.
        """
        return self._meta_attributes

    @meta_attributes.setter
    def meta_attributes(
        self, meta_attributes: "list[GrantaServerApiSchemaLayoutsLayoutAttributeItem]"
    ) -> None:
        """Sets the meta_attributes of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.

        Parameters
        ----------
        meta_attributes: list[GrantaServerApiSchemaLayoutsLayoutAttributeItem]
            The meta_attributes of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.
        """
        self._meta_attributes = meta_attributes

    @property
    def tabular_columns(
        self,
    ) -> "list[GrantaServerApiSchemaLayoutsLayoutTabularColumn]":
        """Gets the tabular_columns of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.

        Returns
        -------
        list[GrantaServerApiSchemaLayoutsLayoutTabularColumn]
            The tabular_columns of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.
        """
        return self._tabular_columns

    @tabular_columns.setter
    def tabular_columns(
        self, tabular_columns: "list[GrantaServerApiSchemaLayoutsLayoutTabularColumn]"
    ) -> None:
        """Sets the tabular_columns of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.

        Parameters
        ----------
        tabular_columns: list[GrantaServerApiSchemaLayoutsLayoutTabularColumn]
            The tabular_columns of this GrantaServerApiSchemaLayoutsLayoutAttributeItem.
        """
        self._tabular_columns = tabular_columns

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
        if issubclass(GrantaServerApiSchemaLayoutsLayoutAttributeItem, dict):
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
        if not isinstance(other, GrantaServerApiSchemaLayoutsLayoutAttributeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
