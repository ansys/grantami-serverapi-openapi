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

from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_tabular_columns_tabular_column import (
    GrantaServerApiSchemaTabularColumnsTabularColumn,
)  # noqa: F401

if TYPE_CHECKING:
    from . import *


class GrantaServerApiSchemaTabularColumnsLocalLongTextTabularColumn(
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

    """
    swagger_types = {
        "column_type": "str",
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "display_names": "dict(str, str)",
        "guid": "str",
        "name": "str",
        "roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "show_as_link": "bool",
        "summary_row_enabled": "bool",
        "summary_row_roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "summary_row_text": "str",
    }

    attribute_map = {
        "column_type": "columnType",
        "default_threshold_type": "defaultThresholdType",
        "display_names": "displayNames",
        "guid": "guid",
        "name": "name",
        "roll_up_type": "rollUpType",
        "show_as_link": "showAsLink",
        "summary_row_enabled": "summaryRowEnabled",
        "summary_row_roll_up_type": "summaryRowRollUpType",
        "summary_row_text": "summaryRowText",
    }

    subtype_mapping = {
        "defaultThresholdType": "GrantaServerApiSchemaAttributesAttributeThresholdType",
    }

    def __init__(
        self,
        *,
        column_type: "str" = "localLongText",
        default_threshold_type: "Optional[GrantaServerApiSchemaAttributesAttributeThresholdType]" = None,
        display_names: "Optional[Dict[str, str]]" = None,
        guid: "Optional[str]" = None,
        name: "Optional[str]" = None,
        roll_up_type: "Optional[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType]" = None,
        show_as_link: "Optional[bool]" = None,
        summary_row_enabled: "Optional[bool]" = None,
        summary_row_roll_up_type: "Optional[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType]" = None,
        summary_row_text: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiSchemaTabularColumnsLocalLongTextTabularColumn - a model defined in Swagger

        Parameters
        ----------
            column_type: str
            default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType, optional
            display_names: Dict[str, str], optional
            guid: str, optional
            name: str, optional
            roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, optional
            show_as_link: bool, optional
            summary_row_enabled: bool, optional
            summary_row_roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, optional
            summary_row_text: str, optional
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
        self._column_type = None
        self._default_threshold_type = None
        self.discriminator = None
        self.column_type = column_type
        if default_threshold_type is not None:
            self.default_threshold_type = default_threshold_type

    @property
    def column_type(self) -> "str":
        """Gets the column_type of this GrantaServerApiSchemaTabularColumnsLocalLongTextTabularColumn.

        Returns
        -------
        str
            The column_type of this GrantaServerApiSchemaTabularColumnsLocalLongTextTabularColumn.
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type: "str") -> None:
        """Sets the column_type of this GrantaServerApiSchemaTabularColumnsLocalLongTextTabularColumn.

        Parameters
        ----------
        column_type: str
            The column_type of this GrantaServerApiSchemaTabularColumnsLocalLongTextTabularColumn.
        """
        if column_type is None:
            raise ValueError("Invalid value for 'column_type', must not be 'None'")
        self._column_type = column_type

    @property
    def default_threshold_type(
        self,
    ) -> "GrantaServerApiSchemaAttributesAttributeThresholdType":
        """Gets the default_threshold_type of this GrantaServerApiSchemaTabularColumnsLocalLongTextTabularColumn.

        Returns
        -------
        GrantaServerApiSchemaAttributesAttributeThresholdType
            The default_threshold_type of this GrantaServerApiSchemaTabularColumnsLocalLongTextTabularColumn.
        """
        return self._default_threshold_type

    @default_threshold_type.setter
    def default_threshold_type(
        self,
        default_threshold_type: "GrantaServerApiSchemaAttributesAttributeThresholdType",
    ) -> None:
        """Sets the default_threshold_type of this GrantaServerApiSchemaTabularColumnsLocalLongTextTabularColumn.

        Parameters
        ----------
        default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType
            The default_threshold_type of this GrantaServerApiSchemaTabularColumnsLocalLongTextTabularColumn.
        """
        self._default_threshold_type = default_threshold_type

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
        if issubclass(
            GrantaServerApiSchemaTabularColumnsLocalLongTextTabularColumn, dict
        ):
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
        if not isinstance(
            other, GrantaServerApiSchemaTabularColumnsLocalLongTextTabularColumn
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
