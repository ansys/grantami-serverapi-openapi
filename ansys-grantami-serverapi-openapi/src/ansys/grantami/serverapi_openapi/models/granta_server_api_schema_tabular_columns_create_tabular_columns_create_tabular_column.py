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


class GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn(
    ModelBase
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
    discriminator_class_map: Dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types = {
        "name": "str",
        "guid": "str",
        "roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "show_as_link": "bool",
        "summary_row_enabled": "bool",
        "summary_row_roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "summary_row_text": "str",
    }

    attribute_map = {
        "name": "name",
        "guid": "guid",
        "roll_up_type": "rollUpType",
        "show_as_link": "showAsLink",
        "summary_row_enabled": "summaryRowEnabled",
        "summary_row_roll_up_type": "summaryRowRollUpType",
        "summary_row_text": "summaryRowText",
    }

    subtype_mapping = {
        "rollUpType": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "summaryRowRollUpType": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
    }

    discriminator_value_class_map = {
        "linkedAttribute".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLinkedAttributeTabularColumn",
        "linkedColumn".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLinkedColumnTabularColumn",
        "linkedRecord".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLinkedRecordTabularColumn",
        "localPoint".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalPointTabularColumn",
        "localRange".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalRangeTabularColumn",
        "localInteger".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalIntegerTabularColumn",
        "localLogical".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalLogicalTabularColumn",
        "localShortText".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalShortTextTabularColumn",
        "localLongText".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalLongTextTabularColumn",
        "localDateTime".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalDateTimeTabularColumn",
        "localDiscrete".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalDiscreteTabularColumn",
        "localHyperlink".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalHyperlinkTabularColumn",
        "localFile".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalFileTabularColumn",
        "localPicture".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalPictureTabularColumn",
    }

    discriminator = "columnType"

    def __init__(
        self,
        *,
        name: "str",
        guid: "Optional[str]" = None,
        roll_up_type: "Optional[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType]" = None,
        show_as_link: "Optional[bool]" = None,
        summary_row_enabled: "Optional[bool]" = None,
        summary_row_roll_up_type: "Optional[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType]" = None,
        summary_row_text: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn - a model defined in Swagger

        Parameters
        ----------
            name: str
            guid: str, optional
            roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, optional
            show_as_link: bool, optional
            summary_row_enabled: bool, optional
            summary_row_roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, optional
            summary_row_text: str, optional
        """
        self._show_as_link = None
        self._summary_row_enabled = None
        self._summary_row_text = None
        self._roll_up_type = None
        self._summary_row_roll_up_type = None
        self._name = None
        self._guid = None

        if show_as_link is not None:
            self.show_as_link = show_as_link
        if summary_row_enabled is not None:
            self.summary_row_enabled = summary_row_enabled
        if summary_row_text is not None:
            self.summary_row_text = summary_row_text
        if roll_up_type is not None:
            self.roll_up_type = roll_up_type
        if summary_row_roll_up_type is not None:
            self.summary_row_roll_up_type = summary_row_roll_up_type
        self.name = name
        if guid is not None:
            self.guid = guid

    @property
    def show_as_link(self) -> "bool":
        """Gets the show_as_link of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Returns
        -------
        bool
            The show_as_link of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        return self._show_as_link

    @show_as_link.setter
    def show_as_link(self, show_as_link: "bool") -> None:
        """Sets the show_as_link of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Parameters
        ----------
        show_as_link: bool
            The show_as_link of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        self._show_as_link = show_as_link

    @property
    def summary_row_enabled(self) -> "bool":
        """Gets the summary_row_enabled of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Returns
        -------
        bool
            The summary_row_enabled of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        return self._summary_row_enabled

    @summary_row_enabled.setter
    def summary_row_enabled(self, summary_row_enabled: "bool") -> None:
        """Sets the summary_row_enabled of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Parameters
        ----------
        summary_row_enabled: bool
            The summary_row_enabled of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        self._summary_row_enabled = summary_row_enabled

    @property
    def summary_row_text(self) -> "str":
        """Gets the summary_row_text of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Returns
        -------
        str
            The summary_row_text of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        return self._summary_row_text

    @summary_row_text.setter
    def summary_row_text(self, summary_row_text: "str") -> None:
        """Sets the summary_row_text of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Parameters
        ----------
        summary_row_text: str
            The summary_row_text of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        self._summary_row_text = summary_row_text

    @property
    def roll_up_type(
        self,
    ) -> "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType":
        """Gets the roll_up_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Returns
        -------
        GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
            The roll_up_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        return self._roll_up_type

    @roll_up_type.setter
    def roll_up_type(
        self, roll_up_type: "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType"
    ) -> None:
        """Sets the roll_up_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Parameters
        ----------
        roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
            The roll_up_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        self._roll_up_type = roll_up_type

    @property
    def summary_row_roll_up_type(
        self,
    ) -> "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType":
        """Gets the summary_row_roll_up_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Returns
        -------
        GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
            The summary_row_roll_up_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        return self._summary_row_roll_up_type

    @summary_row_roll_up_type.setter
    def summary_row_roll_up_type(
        self,
        summary_row_roll_up_type: "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
    ) -> None:
        """Sets the summary_row_roll_up_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Parameters
        ----------
        summary_row_roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
            The summary_row_roll_up_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        self._summary_row_roll_up_type = summary_row_roll_up_type

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
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
        if issubclass(
            GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn,
            dict,
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
            other,
            GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
