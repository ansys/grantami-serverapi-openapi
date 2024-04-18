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
from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_tabular_columns_tabular_column import (
    GrantaServerApiSchemaTabularColumnsTabularColumn,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn(
    GrantaServerApiSchemaTabularColumnsTabularColumn
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
        "discrete_type": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "display_names": "dict(str, str)",
        "guid": "str",
        "name": "str",
        "roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "show_as_link": "bool",
        "summary_row_enabled": "bool",
        "summary_row_roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "summary_row_text": "str",
        "column_type": "str",
    }

    attribute_map: Dict[str, str] = {
        "default_threshold_type": "defaultThresholdType",
        "discrete_type": "discreteType",
        "display_names": "displayNames",
        "guid": "guid",
        "name": "name",
        "roll_up_type": "rollUpType",
        "show_as_link": "showAsLink",
        "summary_row_enabled": "summaryRowEnabled",
        "summary_row_roll_up_type": "summaryRowRollUpType",
        "summary_row_text": "summaryRowText",
        "column_type": "columnType",
    }

    subtype_mapping: Dict[str, str] = {
        "defaultThresholdType": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "discreteType": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        default_threshold_type: "GrantaServerApiSchemaAttributesAttributeThresholdType",
        discrete_type: "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        display_names: "Dict[str, str]",
        guid: "str",
        name: "str",
        roll_up_type: "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        show_as_link: "bool",
        summary_row_enabled: "bool",
        summary_row_roll_up_type: "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        summary_row_text: "str",
        column_type: "str" = "localDiscrete",
    ) -> None:
        """GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn - a model defined in Swagger

        Parameters
        ----------
        default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType
        discrete_type: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
        display_names: Dict[str, str]
        guid: str
        name: str
        roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
        show_as_link: bool
        summary_row_enabled: bool
        summary_row_roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
        summary_row_text: str
        column_type: str
        """
        super().__init__(
            display_names=display_names,
            guid=guid,
            name=name,
            roll_up_type=roll_up_type,
            show_as_link=show_as_link,
            summary_row_enabled=summary_row_enabled,
            summary_row_roll_up_type=summary_row_roll_up_type,
            summary_row_text=summary_row_text,
        )
        self._column_type: str
        self._default_threshold_type: (
            GrantaServerApiSchemaAttributesAttributeThresholdType
        )
        self._discrete_type: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity

        self.column_type = column_type
        self.default_threshold_type = default_threshold_type
        self.discrete_type = discrete_type

    @property
    def column_type(self) -> "str":
        """Gets the column_type of this GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn.

        Returns
        -------
        str
            The column_type of this GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn.
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type: "str") -> None:
        """Sets the column_type of this GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn.

        Parameters
        ----------
        column_type: str
            The column_type of this GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn.
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
    ) -> "GrantaServerApiSchemaAttributesAttributeThresholdType":
        """Gets the default_threshold_type of this GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn.

        Returns
        -------
        GrantaServerApiSchemaAttributesAttributeThresholdType
            The default_threshold_type of this GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn.
        """
        return self._default_threshold_type

    @default_threshold_type.setter
    def default_threshold_type(
        self,
        default_threshold_type: "GrantaServerApiSchemaAttributesAttributeThresholdType",
    ) -> None:
        """Sets the default_threshold_type of this GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn.

        Parameters
        ----------
        default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType
            The default_threshold_type of this GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn.
        """
        # Field is not nullable
        if default_threshold_type is None:
            raise ValueError(
                "Invalid value for 'default_threshold_type', must not be 'None'"
            )
        # Field is required
        if default_threshold_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'default_threshold_type', must not be 'Unset'"
            )
        self._default_threshold_type = default_threshold_type

    @property
    def discrete_type(self) -> "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity":
        """Gets the discrete_type of this GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
            The discrete_type of this GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn.
        """
        return self._discrete_type

    @discrete_type.setter
    def discrete_type(
        self, discrete_type: "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity"
    ) -> None:
        """Sets the discrete_type of this GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn.

        Parameters
        ----------
        discrete_type: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
            The discrete_type of this GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn.
        """
        # Field is not nullable
        if discrete_type is None:
            raise ValueError("Invalid value for 'discrete_type', must not be 'None'")
        # Field is required
        if discrete_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'discrete_type', must not be 'Unset'")
        self._discrete_type = discrete_type

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
            other, GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
