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
from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_tabular_columns_create_tabular_columns_create_tabular_column import (
    GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalPointTabularColumn(
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
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
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
        "unit": "unit",
    }

    subtype_mapping: Dict[str, str] = {
        "defaultThresholdType": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        name: "str",
        column_type: "str" = "localPoint",
        default_threshold_type: "Optional[GrantaServerApiSchemaAttributesAttributeThresholdType]" = None,
        guid: "Optional[str]" = None,
        roll_up_type: "Optional[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType]" = None,
        show_as_link: "Optional[bool]" = None,
        summary_row_enabled: "Optional[bool]" = None,
        summary_row_roll_up_type: "Optional[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType]" = None,
        summary_row_text: "Optional[str]" = None,
        unit: "Optional[GrantaServerApiSchemaSlimEntitiesSlimEntity]" = None,
    ) -> None:
        """GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalPointTabularColumn - a model defined in Swagger

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
            unit: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
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
        self._column_type: str = None  # type: ignore[assignment]
        self._default_threshold_type = None
        self._unit = None

        self.column_type = column_type
        if default_threshold_type is not None:
            self.default_threshold_type = default_threshold_type
        if unit is not None:
            self.unit = unit

    @property
    def column_type(self) -> "str":
        """Gets the column_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalPointTabularColumn.

        Returns
        -------
        str
            The column_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalPointTabularColumn.
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type: "str") -> None:
        """Sets the column_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalPointTabularColumn.

        Parameters
        ----------
        column_type: str
            The column_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalPointTabularColumn.
        """
        if column_type is None:
            raise ValueError("Invalid value for 'column_type', must not be 'None'")
        self._column_type = column_type

    @property
    def default_threshold_type(
        self,
    ) -> "Optional[GrantaServerApiSchemaAttributesAttributeThresholdType]":
        """Gets the default_threshold_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalPointTabularColumn.

        Returns
        -------
        GrantaServerApiSchemaAttributesAttributeThresholdType
            The default_threshold_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalPointTabularColumn.
        """
        return self._default_threshold_type

    @default_threshold_type.setter
    def default_threshold_type(
        self,
        default_threshold_type: "Optional[GrantaServerApiSchemaAttributesAttributeThresholdType]",
    ) -> None:
        """Sets the default_threshold_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalPointTabularColumn.

        Parameters
        ----------
        default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType
            The default_threshold_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalPointTabularColumn.
        """
        self._default_threshold_type = default_threshold_type

    @property
    def unit(self) -> "Optional[GrantaServerApiSchemaSlimEntitiesSlimEntity]":
        """Gets the unit of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalPointTabularColumn.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimEntity
            The unit of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalPointTabularColumn.
        """
        return self._unit

    @unit.setter
    def unit(
        self, unit: "Optional[GrantaServerApiSchemaSlimEntitiesSlimEntity]"
    ) -> None:
        """Sets the unit of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalPointTabularColumn.

        Parameters
        ----------
        unit: GrantaServerApiSchemaSlimEntitiesSlimEntity
            The unit of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalPointTabularColumn.
        """
        self._unit = unit

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
        if not isinstance(
            other,
            GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalPointTabularColumn,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
