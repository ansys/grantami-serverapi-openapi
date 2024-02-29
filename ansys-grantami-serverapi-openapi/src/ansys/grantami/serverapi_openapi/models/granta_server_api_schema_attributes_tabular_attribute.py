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
from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_attributes_attribute import (
    GrantaServerApiSchemaAttributesAttribute,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaAttributesTabularAttribute(
    GrantaServerApiSchemaAttributesAttribute
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
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "display_full_table": "bool",
        "display_names": "dict(str, str)",
        "display_summary_row_inline": "bool",
        "guid": "str",
        "hide_unlinked_rows": "bool",
        "info": "GrantaServerApiSchemaAttributesAttributeAttributeInfo",
        "name": "str",
        "tabular_columns": "list[GrantaServerApiSchemaTabularColumnsTabularColumn]",
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "axis_name": "str",
        "help_path": "str",
        "target": "GrantaServerApiSchemaAttributesTabularAttributeTarget",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "default_threshold_type": "defaultThresholdType",
        "display_full_table": "displayFullTable",
        "display_names": "displayNames",
        "display_summary_row_inline": "displaySummaryRowInline",
        "guid": "guid",
        "hide_unlinked_rows": "hideUnlinkedRows",
        "info": "info",
        "name": "name",
        "tabular_columns": "tabularColumns",
        "about_attribute": "aboutAttribute",
        "axis_name": "axisName",
        "help_path": "helpPath",
        "target": "target",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {
        "target": "GrantaServerApiSchemaAttributesTabularAttributeTarget",
        "tabularColumns": "GrantaServerApiSchemaTabularColumnsTabularColumn",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        default_threshold_type: "GrantaServerApiSchemaAttributesAttributeThresholdType",
        display_full_table: "bool",
        display_names: "Dict[str, str]",
        display_summary_row_inline: "bool",
        guid: "str",
        hide_unlinked_rows: "bool",
        info: "GrantaServerApiSchemaAttributesAttributeAttributeInfo",
        name: "str",
        tabular_columns: "List[GrantaServerApiSchemaTabularColumnsTabularColumn]",
        about_attribute: "Union[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, Unset_Type]" = Unset,
        axis_name: "Union[str, None, Unset_Type]" = Unset,
        help_path: "Union[str, None, Unset_Type]" = Unset,
        target: "Union[GrantaServerApiSchemaAttributesTabularAttributeTarget, Unset_Type]" = Unset,
        type: "str" = "link",
    ) -> None:
        """GrantaServerApiSchemaAttributesTabularAttribute - a model defined in Swagger

        Parameters
        ----------
        default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType
        display_full_table: bool
        display_names: Dict[str, str]
        display_summary_row_inline: bool
        guid: str
        hide_unlinked_rows: bool
        info: GrantaServerApiSchemaAttributesAttributeAttributeInfo
        name: str
        tabular_columns: List[GrantaServerApiSchemaTabularColumnsTabularColumn]
        about_attribute: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, optional
        axis_name: str, optional
        help_path: str, optional
        target: GrantaServerApiSchemaAttributesTabularAttributeTarget, optional
        type: str
        """
        super().__init__(
            default_threshold_type=default_threshold_type,
            display_names=display_names,
            guid=guid,
            info=info,
            name=name,
            about_attribute=about_attribute,
            axis_name=axis_name,
            help_path=help_path,
        )
        self._type: str
        self._display_full_table: bool
        self._display_summary_row_inline: bool
        self._hide_unlinked_rows: bool
        self._target: Union[
            GrantaServerApiSchemaAttributesTabularAttributeTarget, Unset_Type
        ] = Unset
        self._tabular_columns: List[GrantaServerApiSchemaTabularColumnsTabularColumn]

        self.type = type
        self.display_full_table = display_full_table
        self.display_summary_row_inline = display_summary_row_inline
        self.hide_unlinked_rows = hide_unlinked_rows
        if target is not Unset:
            self.target = target
        self.tabular_columns = tabular_columns

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaAttributesTabularAttribute.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaAttributesTabularAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaAttributesTabularAttribute.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaAttributesTabularAttribute.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

    @property
    def display_full_table(self) -> "bool":
        """Gets the display_full_table of this GrantaServerApiSchemaAttributesTabularAttribute.

        Returns
        -------
        bool
            The display_full_table of this GrantaServerApiSchemaAttributesTabularAttribute.
        """
        return self._display_full_table

    @display_full_table.setter
    def display_full_table(self, display_full_table: "bool") -> None:
        """Sets the display_full_table of this GrantaServerApiSchemaAttributesTabularAttribute.

        Parameters
        ----------
        display_full_table: bool
            The display_full_table of this GrantaServerApiSchemaAttributesTabularAttribute.
        """
        # Field is not nullable
        if display_full_table is None:
            raise ValueError(
                "Invalid value for 'display_full_table', must not be 'None'"
            )
        # Field is required
        if display_full_table is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'display_full_table', must not be 'Unset'"
            )
        self._display_full_table = display_full_table

    @property
    def display_summary_row_inline(self) -> "bool":
        """Gets the display_summary_row_inline of this GrantaServerApiSchemaAttributesTabularAttribute.

        Returns
        -------
        bool
            The display_summary_row_inline of this GrantaServerApiSchemaAttributesTabularAttribute.
        """
        return self._display_summary_row_inline

    @display_summary_row_inline.setter
    def display_summary_row_inline(self, display_summary_row_inline: "bool") -> None:
        """Sets the display_summary_row_inline of this GrantaServerApiSchemaAttributesTabularAttribute.

        Parameters
        ----------
        display_summary_row_inline: bool
            The display_summary_row_inline of this GrantaServerApiSchemaAttributesTabularAttribute.
        """
        # Field is not nullable
        if display_summary_row_inline is None:
            raise ValueError(
                "Invalid value for 'display_summary_row_inline', must not be 'None'"
            )
        # Field is required
        if display_summary_row_inline is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'display_summary_row_inline', must not be 'Unset'"
            )
        self._display_summary_row_inline = display_summary_row_inline

    @property
    def hide_unlinked_rows(self) -> "bool":
        """Gets the hide_unlinked_rows of this GrantaServerApiSchemaAttributesTabularAttribute.

        Returns
        -------
        bool
            The hide_unlinked_rows of this GrantaServerApiSchemaAttributesTabularAttribute.
        """
        return self._hide_unlinked_rows

    @hide_unlinked_rows.setter
    def hide_unlinked_rows(self, hide_unlinked_rows: "bool") -> None:
        """Sets the hide_unlinked_rows of this GrantaServerApiSchemaAttributesTabularAttribute.

        Parameters
        ----------
        hide_unlinked_rows: bool
            The hide_unlinked_rows of this GrantaServerApiSchemaAttributesTabularAttribute.
        """
        # Field is not nullable
        if hide_unlinked_rows is None:
            raise ValueError(
                "Invalid value for 'hide_unlinked_rows', must not be 'None'"
            )
        # Field is required
        if hide_unlinked_rows is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'hide_unlinked_rows', must not be 'Unset'"
            )
        self._hide_unlinked_rows = hide_unlinked_rows

    @property
    def target(
        self,
    ) -> "Union[GrantaServerApiSchemaAttributesTabularAttributeTarget, Unset_Type]":
        """Gets the target of this GrantaServerApiSchemaAttributesTabularAttribute.

        Returns
        -------
        Union[GrantaServerApiSchemaAttributesTabularAttributeTarget, Unset_Type]
            The target of this GrantaServerApiSchemaAttributesTabularAttribute.
        """
        return self._target

    @target.setter
    def target(
        self,
        target: "Union[GrantaServerApiSchemaAttributesTabularAttributeTarget, Unset_Type]",
    ) -> None:
        """Sets the target of this GrantaServerApiSchemaAttributesTabularAttribute.

        Parameters
        ----------
        target: Union[GrantaServerApiSchemaAttributesTabularAttributeTarget, Unset_Type]
            The target of this GrantaServerApiSchemaAttributesTabularAttribute.
        """
        # Field is not nullable
        if target is None:
            raise ValueError("Invalid value for 'target', must not be 'None'")
        self._target = target

    @property
    def tabular_columns(
        self,
    ) -> "List[GrantaServerApiSchemaTabularColumnsTabularColumn]":
        """Gets the tabular_columns of this GrantaServerApiSchemaAttributesTabularAttribute.

        Returns
        -------
        List[GrantaServerApiSchemaTabularColumnsTabularColumn]
            The tabular_columns of this GrantaServerApiSchemaAttributesTabularAttribute.
        """
        return self._tabular_columns

    @tabular_columns.setter
    def tabular_columns(
        self, tabular_columns: "List[GrantaServerApiSchemaTabularColumnsTabularColumn]"
    ) -> None:
        """Sets the tabular_columns of this GrantaServerApiSchemaAttributesTabularAttribute.

        Parameters
        ----------
        tabular_columns: List[GrantaServerApiSchemaTabularColumnsTabularColumn]
            The tabular_columns of this GrantaServerApiSchemaAttributesTabularAttribute.
        """
        # Field is not nullable
        if tabular_columns is None:
            raise ValueError("Invalid value for 'tabular_columns', must not be 'None'")
        # Field is required
        if tabular_columns is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'tabular_columns', must not be 'Unset'")
        self._tabular_columns = tabular_columns

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
        if not isinstance(other, GrantaServerApiSchemaAttributesTabularAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
