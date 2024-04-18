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
from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_layouts_layout_section import (
    GrantaServerApiSchemaLayoutsLayoutSection,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaLayoutsFullLayoutSection(
    GrantaServerApiSchemaLayoutsLayoutSection
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
        "display_names": "dict(str, str)",
        "guid": "str",
        "name": "str",
        "section_items": "list[GrantaServerApiSchemaLayoutsLayoutItem]",
        "section_detail_type": "str",
    }

    attribute_map: Dict[str, str] = {
        "display_names": "displayNames",
        "guid": "guid",
        "name": "name",
        "section_items": "sectionItems",
        "section_detail_type": "sectionDetailType",
    }

    subtype_mapping: Dict[str, str] = {
        "sectionItems": "GrantaServerApiSchemaLayoutsLayoutItem",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        display_names: "Dict[str, str]",
        guid: "str",
        name: "str",
        section_items: "List[GrantaServerApiSchemaLayoutsLayoutItem]",
        section_detail_type: "str" = "full",
    ) -> None:
        """GrantaServerApiSchemaLayoutsFullLayoutSection - a model defined in Swagger

        Parameters
        ----------
        display_names: Dict[str, str]
        guid: str
        name: str
        section_items: List[GrantaServerApiSchemaLayoutsLayoutItem]
        section_detail_type: str
        """
        super().__init__(display_names=display_names, guid=guid, name=name)
        self._section_detail_type: str
        self._section_items: List[GrantaServerApiSchemaLayoutsLayoutItem]

        self.section_detail_type = section_detail_type
        self.section_items = section_items

    @property
    def section_detail_type(self) -> "str":
        """Gets the section_detail_type of this GrantaServerApiSchemaLayoutsFullLayoutSection.

        Returns
        -------
        str
            The section_detail_type of this GrantaServerApiSchemaLayoutsFullLayoutSection.
        """
        return self._section_detail_type

    @section_detail_type.setter
    def section_detail_type(self, section_detail_type: "str") -> None:
        """Sets the section_detail_type of this GrantaServerApiSchemaLayoutsFullLayoutSection.

        Parameters
        ----------
        section_detail_type: str
            The section_detail_type of this GrantaServerApiSchemaLayoutsFullLayoutSection.
        """
        # Field is not nullable
        if section_detail_type is None:
            raise ValueError(
                "Invalid value for 'section_detail_type', must not be 'None'"
            )
        # Field is required
        if section_detail_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'section_detail_type', must not be 'Unset'"
            )
        self._section_detail_type = section_detail_type

    @property
    def section_items(self) -> "List[GrantaServerApiSchemaLayoutsLayoutItem]":
        """Gets the section_items of this GrantaServerApiSchemaLayoutsFullLayoutSection.

        Returns
        -------
        List[GrantaServerApiSchemaLayoutsLayoutItem]
            The section_items of this GrantaServerApiSchemaLayoutsFullLayoutSection.
        """
        return self._section_items

    @section_items.setter
    def section_items(
        self, section_items: "List[GrantaServerApiSchemaLayoutsLayoutItem]"
    ) -> None:
        """Sets the section_items of this GrantaServerApiSchemaLayoutsFullLayoutSection.

        Parameters
        ----------
        section_items: List[GrantaServerApiSchemaLayoutsLayoutItem]
            The section_items of this GrantaServerApiSchemaLayoutsFullLayoutSection.
        """
        # Field is not nullable
        if section_items is None:
            raise ValueError("Invalid value for 'section_items', must not be 'None'")
        # Field is required
        if section_items is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'section_items', must not be 'Unset'")
        self._section_items = section_items

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
        if not isinstance(other, GrantaServerApiSchemaLayoutsFullLayoutSection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
