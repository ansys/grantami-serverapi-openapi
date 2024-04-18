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


class GrantaServerApiSchemaLayoutsLayoutSection(ModelBase):
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
    swagger_types: Dict[str, str] = {
        "display_names": "dict(str, str)",
        "guid": "str",
        "name": "str",
    }

    attribute_map: Dict[str, str] = {
        "display_names": "displayNames",
        "guid": "guid",
        "name": "name",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator_value_class_map = {
        "slim".lower(): "#/components/schemas/GrantaServerApiSchemaSlimEntitiesSlimLayoutSection",
        "full".lower(): "#/components/schemas/GrantaServerApiSchemaLayoutsFullLayoutSection",
    }

    discriminator: Optional[str] = "section_detail_type"

    def __init__(
        self,
        *,
        display_names: "Dict[str, str]",
        guid: "str",
        name: "str",
    ) -> None:
        """GrantaServerApiSchemaLayoutsLayoutSection - a model defined in Swagger

        Parameters
        ----------
        display_names: Dict[str, str]
        guid: str
        name: str
        """
        self._display_names: Dict[str, str]
        self._name: str
        self._guid: str

        self.display_names = display_names
        self.name = name
        self.guid = guid

    @property
    def display_names(self) -> "Dict[str, str]":
        """Gets the display_names of this GrantaServerApiSchemaLayoutsLayoutSection.

        Returns
        -------
        Dict[str, str]
            The display_names of this GrantaServerApiSchemaLayoutsLayoutSection.
        """
        return self._display_names

    @display_names.setter
    def display_names(self, display_names: "Dict[str, str]") -> None:
        """Sets the display_names of this GrantaServerApiSchemaLayoutsLayoutSection.

        Parameters
        ----------
        display_names: Dict[str, str]
            The display_names of this GrantaServerApiSchemaLayoutsLayoutSection.
        """
        # Field is not nullable
        if display_names is None:
            raise ValueError("Invalid value for 'display_names', must not be 'None'")
        # Field is required
        if display_names is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'display_names', must not be 'Unset'")
        self._display_names = display_names

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaLayoutsLayoutSection.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaLayoutsLayoutSection.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaLayoutsLayoutSection.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaLayoutsLayoutSection.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        # Field is required
        if name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'name', must not be 'Unset'")
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaLayoutsLayoutSection.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaLayoutsLayoutSection.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaLayoutsLayoutSection.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaLayoutsLayoutSection.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        # Field is required
        if guid is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'guid', must not be 'Unset'")
        self._guid = guid

    @classmethod
    def get_real_child_model(cls, data: Dict[str, str]) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[cls._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen,
        # so we have to extract it from the JSON reference
        return cls.discriminator_value_class_map[discriminator_value].rsplit("/", 1)[-1]

    @classmethod
    def _get_discriminator_field_name(cls) -> str:
        assert cls.discriminator
        name_tokens = cls.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiSchemaLayoutsLayoutSection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
