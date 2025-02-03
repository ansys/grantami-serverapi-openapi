# Copyright (C) 2023 - 2025 ANSYS, Inc. and/or its affiliates.
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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaLinkedRecordExportBehavior(ModelBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes
    ----------
    swagger_types: dict[str, str]
        The key is attribute name and the value is attribute type.
    attribute_map: dict[str, str]
        The key is attribute name and the value is json key in definition.
    subtype_mapping: dict[str, str]
        The key is the unmangled property name and the value is the corresponding type.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "linked_records_criterion": "GsaCriterion",
        "summary_roll_up_type": "GsaTabularColumnRollUpType",
        "tabular_row_behavior": "GsaTabularRowExportBehavior",
    }

    attribute_map: dict[str, str] = {
        "linked_records_criterion": "linkedRecordsCriterion",
        "summary_roll_up_type": "summaryRollUpType",
        "tabular_row_behavior": "tabularRowBehavior",
    }

    subtype_mapping: dict[str, str] = {
        "tabularRowBehavior": "GsaTabularRowExportBehavior",
        "summaryRollUpType": "GsaTabularColumnRollUpType",
        "linkedRecordsCriterion": "GsaCriterion",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        linked_records_criterion: "Union[GsaCriterion, Unset_Type]" = Unset,
        summary_roll_up_type: "Union[GsaTabularColumnRollUpType, Unset_Type]" = Unset,
        tabular_row_behavior: "Union[GsaTabularRowExportBehavior, Unset_Type]" = Unset,
    ) -> None:
        """GsaLinkedRecordExportBehavior - a model defined in Swagger

        Parameters
        ----------
        linked_records_criterion: GsaCriterion, optional
        summary_roll_up_type: GsaTabularColumnRollUpType, optional
        tabular_row_behavior: GsaTabularRowExportBehavior, optional
        """
        self._tabular_row_behavior: Union[GsaTabularRowExportBehavior, Unset_Type] = Unset
        self._summary_roll_up_type: Union[GsaTabularColumnRollUpType, Unset_Type] = Unset
        self._linked_records_criterion: Union[GsaCriterion, Unset_Type] = Unset

        if tabular_row_behavior is not Unset:
            self.tabular_row_behavior = tabular_row_behavior
        if summary_roll_up_type is not Unset:
            self.summary_roll_up_type = summary_roll_up_type
        if linked_records_criterion is not Unset:
            self.linked_records_criterion = linked_records_criterion

    @property
    def tabular_row_behavior(self) -> "Union[GsaTabularRowExportBehavior, Unset_Type]":
        """Gets the tabular_row_behavior of this GsaLinkedRecordExportBehavior.

        Returns
        -------
        Union[GsaTabularRowExportBehavior, Unset_Type]
            The tabular_row_behavior of this GsaLinkedRecordExportBehavior.
        """
        return self._tabular_row_behavior

    @tabular_row_behavior.setter
    def tabular_row_behavior(
        self, tabular_row_behavior: "Union[GsaTabularRowExportBehavior, Unset_Type]"
    ) -> None:
        """Sets the tabular_row_behavior of this GsaLinkedRecordExportBehavior.

        Parameters
        ----------
        tabular_row_behavior: Union[GsaTabularRowExportBehavior, Unset_Type]
            The tabular_row_behavior of this GsaLinkedRecordExportBehavior.
        """
        # Field is not nullable
        if tabular_row_behavior is None:
            raise ValueError("Invalid value for 'tabular_row_behavior', must not be 'None'")
        self._tabular_row_behavior = tabular_row_behavior

    @property
    def summary_roll_up_type(self) -> "Union[GsaTabularColumnRollUpType, Unset_Type]":
        """Gets the summary_roll_up_type of this GsaLinkedRecordExportBehavior.

        Returns
        -------
        Union[GsaTabularColumnRollUpType, Unset_Type]
            The summary_roll_up_type of this GsaLinkedRecordExportBehavior.
        """
        return self._summary_roll_up_type

    @summary_roll_up_type.setter
    def summary_roll_up_type(
        self, summary_roll_up_type: "Union[GsaTabularColumnRollUpType, Unset_Type]"
    ) -> None:
        """Sets the summary_roll_up_type of this GsaLinkedRecordExportBehavior.

        Parameters
        ----------
        summary_roll_up_type: Union[GsaTabularColumnRollUpType, Unset_Type]
            The summary_roll_up_type of this GsaLinkedRecordExportBehavior.
        """
        # Field is not nullable
        if summary_roll_up_type is None:
            raise ValueError("Invalid value for 'summary_roll_up_type', must not be 'None'")
        self._summary_roll_up_type = summary_roll_up_type

    @property
    def linked_records_criterion(self) -> "Union[GsaCriterion, Unset_Type]":
        """Gets the linked_records_criterion of this GsaLinkedRecordExportBehavior.

        Returns
        -------
        Union[GsaCriterion, Unset_Type]
            The linked_records_criterion of this GsaLinkedRecordExportBehavior.
        """
        return self._linked_records_criterion

    @linked_records_criterion.setter
    def linked_records_criterion(
        self, linked_records_criterion: "Union[GsaCriterion, Unset_Type]"
    ) -> None:
        """Sets the linked_records_criterion of this GsaLinkedRecordExportBehavior.

        Parameters
        ----------
        linked_records_criterion: Union[GsaCriterion, Unset_Type]
            The linked_records_criterion of this GsaLinkedRecordExportBehavior.
        """
        # Field is not nullable
        if linked_records_criterion is None:
            raise ValueError("Invalid value for 'linked_records_criterion', must not be 'None'")
        self._linked_records_criterion = linked_records_criterion

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
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
        if not isinstance(other, GsaLinkedRecordExportBehavior):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
