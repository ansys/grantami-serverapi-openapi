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


class GrantaServerApiSchemaLayoutsLayoutItem(ModelBase):
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
    discriminator_class_map: Dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types = {
        "guid": "str",
        "name": "str",
        "underlying_entity_guid": "str",
    }

    attribute_map = {
        "guid": "guid",
        "name": "name",
        "underlying_entity_guid": "underlyingEntityGuid",
    }

    subtype_mapping = {}

    discriminator_value_class_map = {
        "attribute".lower(): "#/components/schemas/GrantaServerApiSchemaLayoutsLayoutAttributeItem",
        "link".lower(): "#/components/schemas/GrantaServerApiSchemaLayoutsLayoutLinkItem",
    }

    discriminator = "item_type"

    def __init__(
        self,
        *,
        guid: "str",
        name: "str",
        underlying_entity_guid: "str",
    ) -> None:
        """GrantaServerApiSchemaLayoutsLayoutItem - a model defined in Swagger

        Parameters
        ----------
            guid: str
            name: str
            underlying_entity_guid: str
        """
        self._underlying_entity_guid = None
        self._name = None
        self._guid = None

        self.underlying_entity_guid = underlying_entity_guid
        self.name = name
        self.guid = guid

    @property
    def underlying_entity_guid(self) -> "str":
        """Gets the underlying_entity_guid of this GrantaServerApiSchemaLayoutsLayoutItem.

        Returns
        -------
        str
            The underlying_entity_guid of this GrantaServerApiSchemaLayoutsLayoutItem.
        """
        return self._underlying_entity_guid

    @underlying_entity_guid.setter
    def underlying_entity_guid(self, underlying_entity_guid: "str") -> None:
        """Sets the underlying_entity_guid of this GrantaServerApiSchemaLayoutsLayoutItem.

        Parameters
        ----------
        underlying_entity_guid: str
            The underlying_entity_guid of this GrantaServerApiSchemaLayoutsLayoutItem.
        """
        if underlying_entity_guid is None:
            raise ValueError(
                "Invalid value for 'underlying_entity_guid', must not be 'None'"
            )
        self._underlying_entity_guid = underlying_entity_guid

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaLayoutsLayoutItem.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaLayoutsLayoutItem.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaLayoutsLayoutItem.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaLayoutsLayoutItem.
        """
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaLayoutsLayoutItem.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaLayoutsLayoutItem.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaLayoutsLayoutItem.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaLayoutsLayoutItem.
        """
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        self._guid = guid

    @classmethod
    def get_real_child_model(cls, data: ModelBase) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[cls._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen,
        # so we have to extract it from the JSON reference
        return cls.discriminator_value_class_map.get(discriminator_value).rsplit(
            "/", 1
        )[-1]

    @classmethod
    def _get_discriminator_field_name(cls) -> str:
        name_tokens = cls.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

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
        if issubclass(GrantaServerApiSchemaLayoutsLayoutItem, dict):
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
        if not isinstance(other, GrantaServerApiSchemaLayoutsLayoutItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
