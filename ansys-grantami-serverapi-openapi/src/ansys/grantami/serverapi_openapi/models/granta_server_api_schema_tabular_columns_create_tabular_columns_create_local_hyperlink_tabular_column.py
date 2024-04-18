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
from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_tabular_columns_create_tabular_columns_create_tabular_column import (
    GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalHyperlinkTabularColumn(
    GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn
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
        "name": "str",
        "column_type": "str",
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "guid": "str",
        "roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "show_as_link": "bool",
        "summary_row_enabled": "bool",
        "summary_row_roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "summary_row_text": "str",
    }

    attribute_map: Dict[str, str] = {
        "name": "name",
        "column_type": "columnType",
        "default_threshold_type": "defaultThresholdType",
        "guid": "guid",
        "roll_up_type": "rollUpType",
        "show_as_link": "showAsLink",
        "summary_row_enabled": "summaryRowEnabled",
        "summary_row_roll_up_type": "summaryRowRollUpType",
        "summary_row_text": "summaryRowText",
    }

    subtype_mapping: Dict[str, str] = {
        "defaultThresholdType": "GrantaServerApiSchemaAttributesAttributeThresholdType",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        name: "str",
        column_type: "str" = "localHyperlink",
        default_threshold_type: "Union[GrantaServerApiSchemaAttributesAttributeThresholdType, Unset_Type]" = Unset,
        guid: "Union[str, Unset_Type]" = Unset,
        roll_up_type: "Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]" = Unset,
        show_as_link: "Union[bool, Unset_Type]" = Unset,
        summary_row_enabled: "Union[bool, Unset_Type]" = Unset,
        summary_row_roll_up_type: "Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]" = Unset,
        summary_row_text: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalHyperlinkTabularColumn - a model defined in Swagger

        Parameters
        ----------
        name: str
        column_type: str
        default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType, optional
        guid: str, optional
        roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, optional
        show_as_link: bool, optional
        summary_row_enabled: bool, optional
        summary_row_roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, optional
        summary_row_text: str, optional
        """
        super().__init__(
            name=name,
            guid=guid,
            roll_up_type=roll_up_type,
            show_as_link=show_as_link,
            summary_row_enabled=summary_row_enabled,
            summary_row_roll_up_type=summary_row_roll_up_type,
            summary_row_text=summary_row_text,
        )
        self._column_type: str
        self._default_threshold_type: Union[
            GrantaServerApiSchemaAttributesAttributeThresholdType, Unset_Type
        ] = Unset

        self.column_type = column_type
        if default_threshold_type is not Unset:
            self.default_threshold_type = default_threshold_type

    @property
    def column_type(self) -> "str":
        """Gets the column_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalHyperlinkTabularColumn.

        Returns
        -------
        str
            The column_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalHyperlinkTabularColumn.
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type: "str") -> None:
        """Sets the column_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalHyperlinkTabularColumn.

        Parameters
        ----------
        column_type: str
            The column_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalHyperlinkTabularColumn.
        """
        # Field is not nullable
        if column_type is None:
            raise ValueError("Invalid value for 'column_type', must not be 'None'")
        # Field is required
        if column_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'column_type', must not be 'Unset'")
        self._column_type = column_type

    @property
    def default_threshold_type(
        self,
    ) -> "Union[GrantaServerApiSchemaAttributesAttributeThresholdType, Unset_Type]":
        """Gets the default_threshold_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalHyperlinkTabularColumn.

        Returns
        -------
        Union[GrantaServerApiSchemaAttributesAttributeThresholdType, Unset_Type]
            The default_threshold_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalHyperlinkTabularColumn.
        """
        return self._default_threshold_type

    @default_threshold_type.setter
    def default_threshold_type(
        self,
        default_threshold_type: "Union[GrantaServerApiSchemaAttributesAttributeThresholdType, Unset_Type]",
    ) -> None:
        """Sets the default_threshold_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalHyperlinkTabularColumn.

        Parameters
        ----------
        default_threshold_type: Union[GrantaServerApiSchemaAttributesAttributeThresholdType, Unset_Type]
            The default_threshold_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalHyperlinkTabularColumn.
        """
        # Field is not nullable
        if default_threshold_type is None:
            raise ValueError(
                "Invalid value for 'default_threshold_type', must not be 'None'"
            )
        self._default_threshold_type = default_threshold_type

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
        if not isinstance(
            other,
            GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalHyperlinkTabularColumn,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
