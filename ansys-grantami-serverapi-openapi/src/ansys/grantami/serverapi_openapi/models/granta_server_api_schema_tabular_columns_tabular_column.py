# Copyright (C) 2023 - 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiSchemaTabularColumnsTabularColumn(ModelBase):
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
        "roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "show_as_link": "bool",
        "summary_row_enabled": "bool",
        "summary_row_roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "summary_row_text": "str",
    }

    attribute_map: Dict[str, str] = {
        "display_names": "displayNames",
        "guid": "guid",
        "name": "name",
        "roll_up_type": "rollUpType",
        "show_as_link": "showAsLink",
        "summary_row_enabled": "summaryRowEnabled",
        "summary_row_roll_up_type": "summaryRowRollUpType",
        "summary_row_text": "summaryRowText",
    }

    subtype_mapping: Dict[str, str] = {
        "rollUpType": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "summaryRowRollUpType": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
    }

    discriminator_value_class_map = {
        "linkedAttribute".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsLinkedAttributeTabularColumn",
        "linkedColumn".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsLinkedColumnTabularColumn",
        "linkedRecord".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsLinkedRecordTabularColumn",
        "localPoint".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsLocalPointTabularColumn",
        "localRange".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsLocalRangeTabularColumn",
        "localInteger".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsLocalIntegerTabularColumn",
        "localLogical".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsLocalLogicalTabularColumn",
        "localShortText".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsLocalShortTextTabularColumn",
        "localLongText".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsLocalLongTextTabularColumn",
        "localDateTime".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsLocalDateTimeTabularColumn",
        "localDiscrete".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn",
        "localHyperlink".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsLocalHyperlinkTabularColumn",
        "localFile".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsLocalFileTabularColumn",
        "localPicture".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsLocalPictureTabularColumn",
        "unavailable".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsUnavailableTabularColumn",
    }

    discriminator: Optional[str] = "columnType"

    def __init__(
        self,
        *,
        display_names: "Dict[str, str]",
        guid: "str",
        name: "str",
        roll_up_type: "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        show_as_link: "bool",
        summary_row_enabled: "bool",
        summary_row_roll_up_type: "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        summary_row_text: "str",
    ) -> None:
        """GrantaServerApiSchemaTabularColumnsTabularColumn - a model defined in Swagger

        Parameters
        ----------
        display_names: Dict[str, str]
        guid: str
        name: str
        roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
        show_as_link: bool
        summary_row_enabled: bool
        summary_row_roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
        summary_row_text: str
        """
        self._show_as_link: bool
        self._summary_row_enabled: bool
        self._summary_row_text: str
        self._roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
        self._summary_row_roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
        self._display_names: Dict[str, str]
        self._name: str
        self._guid: str

        self.show_as_link = show_as_link
        self.summary_row_enabled = summary_row_enabled
        self.summary_row_text = summary_row_text
        self.roll_up_type = roll_up_type
        self.summary_row_roll_up_type = summary_row_roll_up_type
        self.display_names = display_names
        self.name = name
        self.guid = guid

    @property
    def show_as_link(self) -> "bool":
        """Gets the show_as_link of this GrantaServerApiSchemaTabularColumnsTabularColumn.

        Returns
        -------
        bool
            The show_as_link of this GrantaServerApiSchemaTabularColumnsTabularColumn.
        """
        return self._show_as_link

    @show_as_link.setter
    def show_as_link(self, show_as_link: "bool") -> None:
        """Sets the show_as_link of this GrantaServerApiSchemaTabularColumnsTabularColumn.

        Parameters
        ----------
        show_as_link: bool
            The show_as_link of this GrantaServerApiSchemaTabularColumnsTabularColumn.
        """
        # Field is not nullable
        if show_as_link is None:
            raise ValueError("Invalid value for 'show_as_link', must not be 'None'")
        # Field is required
        if show_as_link is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'show_as_link', must not be 'Unset'")
        self._show_as_link = show_as_link

    @property
    def summary_row_enabled(self) -> "bool":
        """Gets the summary_row_enabled of this GrantaServerApiSchemaTabularColumnsTabularColumn.

        Returns
        -------
        bool
            The summary_row_enabled of this GrantaServerApiSchemaTabularColumnsTabularColumn.
        """
        return self._summary_row_enabled

    @summary_row_enabled.setter
    def summary_row_enabled(self, summary_row_enabled: "bool") -> None:
        """Sets the summary_row_enabled of this GrantaServerApiSchemaTabularColumnsTabularColumn.

        Parameters
        ----------
        summary_row_enabled: bool
            The summary_row_enabled of this GrantaServerApiSchemaTabularColumnsTabularColumn.
        """
        # Field is not nullable
        if summary_row_enabled is None:
            raise ValueError("Invalid value for 'summary_row_enabled', must not be 'None'")
        # Field is required
        if summary_row_enabled is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'summary_row_enabled', must not be 'Unset'")
        self._summary_row_enabled = summary_row_enabled

    @property
    def summary_row_text(self) -> "str":
        """Gets the summary_row_text of this GrantaServerApiSchemaTabularColumnsTabularColumn.

        Returns
        -------
        str
            The summary_row_text of this GrantaServerApiSchemaTabularColumnsTabularColumn.
        """
        return self._summary_row_text

    @summary_row_text.setter
    def summary_row_text(self, summary_row_text: "str") -> None:
        """Sets the summary_row_text of this GrantaServerApiSchemaTabularColumnsTabularColumn.

        Parameters
        ----------
        summary_row_text: str
            The summary_row_text of this GrantaServerApiSchemaTabularColumnsTabularColumn.
        """
        # Field is not nullable
        if summary_row_text is None:
            raise ValueError("Invalid value for 'summary_row_text', must not be 'None'")
        # Field is required
        if summary_row_text is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'summary_row_text', must not be 'Unset'")
        self._summary_row_text = summary_row_text

    @property
    def roll_up_type(self) -> "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType":
        """Gets the roll_up_type of this GrantaServerApiSchemaTabularColumnsTabularColumn.

        Returns
        -------
        GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
            The roll_up_type of this GrantaServerApiSchemaTabularColumnsTabularColumn.
        """
        return self._roll_up_type

    @roll_up_type.setter
    def roll_up_type(
        self, roll_up_type: "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType"
    ) -> None:
        """Sets the roll_up_type of this GrantaServerApiSchemaTabularColumnsTabularColumn.

        Parameters
        ----------
        roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
            The roll_up_type of this GrantaServerApiSchemaTabularColumnsTabularColumn.
        """
        # Field is not nullable
        if roll_up_type is None:
            raise ValueError("Invalid value for 'roll_up_type', must not be 'None'")
        # Field is required
        if roll_up_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'roll_up_type', must not be 'Unset'")
        self._roll_up_type = roll_up_type

    @property
    def summary_row_roll_up_type(
        self,
    ) -> "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType":
        """Gets the summary_row_roll_up_type of this GrantaServerApiSchemaTabularColumnsTabularColumn.

        Returns
        -------
        GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
            The summary_row_roll_up_type of this GrantaServerApiSchemaTabularColumnsTabularColumn.
        """
        return self._summary_row_roll_up_type

    @summary_row_roll_up_type.setter
    def summary_row_roll_up_type(
        self, summary_row_roll_up_type: "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType"
    ) -> None:
        """Sets the summary_row_roll_up_type of this GrantaServerApiSchemaTabularColumnsTabularColumn.

        Parameters
        ----------
        summary_row_roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
            The summary_row_roll_up_type of this GrantaServerApiSchemaTabularColumnsTabularColumn.
        """
        # Field is not nullable
        if summary_row_roll_up_type is None:
            raise ValueError("Invalid value for 'summary_row_roll_up_type', must not be 'None'")
        # Field is required
        if summary_row_roll_up_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'summary_row_roll_up_type', must not be 'Unset'")
        self._summary_row_roll_up_type = summary_row_roll_up_type

    @property
    def display_names(self) -> "Dict[str, str]":
        """Gets the display_names of this GrantaServerApiSchemaTabularColumnsTabularColumn.

        Returns
        -------
        Dict[str, str]
            The display_names of this GrantaServerApiSchemaTabularColumnsTabularColumn.
        """
        return self._display_names

    @display_names.setter
    def display_names(self, display_names: "Dict[str, str]") -> None:
        """Sets the display_names of this GrantaServerApiSchemaTabularColumnsTabularColumn.

        Parameters
        ----------
        display_names: Dict[str, str]
            The display_names of this GrantaServerApiSchemaTabularColumnsTabularColumn.
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
        """Gets the name of this GrantaServerApiSchemaTabularColumnsTabularColumn.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaTabularColumnsTabularColumn.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaTabularColumnsTabularColumn.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaTabularColumnsTabularColumn.
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
        """Gets the guid of this GrantaServerApiSchemaTabularColumnsTabularColumn.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaTabularColumnsTabularColumn.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaTabularColumnsTabularColumn.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaTabularColumnsTabularColumn.
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
        discriminator_value = str(data[cls.discriminator]).lower()  # type: ignore[index]
        # The actual class name is not available in swagger-codegen,
        # so we have to extract it from the JSON reference
        return cls.discriminator_value_class_map[discriminator_value].rsplit("/", 1)[-1]

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiSchemaTabularColumnsTabularColumn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
