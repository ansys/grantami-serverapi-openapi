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


class GrantaServerApiDataExportLinkedRecordExportBehavior(ModelBase):
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
        "linked_records_criterion": "GrantaServerApiSearchCriterion",
        "summary_roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "tabular_row_behavior": "GrantaServerApiDataExportTabularRowExportBehavior",
    }

    attribute_map: Dict[str, str] = {
        "linked_records_criterion": "linkedRecordsCriterion",
        "summary_roll_up_type": "summaryRollUpType",
        "tabular_row_behavior": "tabularRowBehavior",
    }

    subtype_mapping: Dict[str, str] = {
        "tabularRowBehavior": "GrantaServerApiDataExportTabularRowExportBehavior",
        "summaryRollUpType": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "linkedRecordsCriterion": "GrantaServerApiSearchCriterion",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        linked_records_criterion: "Union[GrantaServerApiSearchCriterion, Unset_Type]" = Unset,
        summary_roll_up_type: "Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]" = Unset,
        tabular_row_behavior: "Union[GrantaServerApiDataExportTabularRowExportBehavior, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiDataExportLinkedRecordExportBehavior - a model defined in Swagger

        Parameters
        ----------
        linked_records_criterion: GrantaServerApiSearchCriterion, optional
        summary_roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, optional
        tabular_row_behavior: GrantaServerApiDataExportTabularRowExportBehavior, optional
        """
        self._tabular_row_behavior: Union[
            GrantaServerApiDataExportTabularRowExportBehavior, Unset_Type
        ] = Unset
        self._summary_roll_up_type: Union[
            GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type
        ] = Unset
        self._linked_records_criterion: Union[
            GrantaServerApiSearchCriterion, Unset_Type
        ] = Unset

        if tabular_row_behavior is not Unset:
            self.tabular_row_behavior = tabular_row_behavior
        if summary_roll_up_type is not Unset:
            self.summary_roll_up_type = summary_roll_up_type
        if linked_records_criterion is not Unset:
            self.linked_records_criterion = linked_records_criterion

    @property
    def tabular_row_behavior(
        self,
    ) -> "Union[GrantaServerApiDataExportTabularRowExportBehavior, Unset_Type]":
        """Gets the tabular_row_behavior of this GrantaServerApiDataExportLinkedRecordExportBehavior.

        Returns
        -------
        Union[GrantaServerApiDataExportTabularRowExportBehavior, Unset_Type]
            The tabular_row_behavior of this GrantaServerApiDataExportLinkedRecordExportBehavior.
        """
        return self._tabular_row_behavior

    @tabular_row_behavior.setter
    def tabular_row_behavior(
        self,
        tabular_row_behavior: "Union[GrantaServerApiDataExportTabularRowExportBehavior, Unset_Type]",
    ) -> None:
        """Sets the tabular_row_behavior of this GrantaServerApiDataExportLinkedRecordExportBehavior.

        Parameters
        ----------
        tabular_row_behavior: Union[GrantaServerApiDataExportTabularRowExportBehavior, Unset_Type]
            The tabular_row_behavior of this GrantaServerApiDataExportLinkedRecordExportBehavior.
        """
        # Field is not nullable
        if tabular_row_behavior is None:
            raise ValueError(
                "Invalid value for 'tabular_row_behavior', must not be 'None'"
            )
        self._tabular_row_behavior = tabular_row_behavior

    @property
    def summary_roll_up_type(
        self,
    ) -> (
        "Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]"
    ):
        """Gets the summary_roll_up_type of this GrantaServerApiDataExportLinkedRecordExportBehavior.

        Returns
        -------
        Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]
            The summary_roll_up_type of this GrantaServerApiDataExportLinkedRecordExportBehavior.
        """
        return self._summary_roll_up_type

    @summary_roll_up_type.setter
    def summary_roll_up_type(
        self,
        summary_roll_up_type: "Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]",
    ) -> None:
        """Sets the summary_roll_up_type of this GrantaServerApiDataExportLinkedRecordExportBehavior.

        Parameters
        ----------
        summary_roll_up_type: Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]
            The summary_roll_up_type of this GrantaServerApiDataExportLinkedRecordExportBehavior.
        """
        # Field is not nullable
        if summary_roll_up_type is None:
            raise ValueError(
                "Invalid value for 'summary_roll_up_type', must not be 'None'"
            )
        self._summary_roll_up_type = summary_roll_up_type

    @property
    def linked_records_criterion(
        self,
    ) -> "Union[GrantaServerApiSearchCriterion, Unset_Type]":
        """Gets the linked_records_criterion of this GrantaServerApiDataExportLinkedRecordExportBehavior.

        Returns
        -------
        Union[GrantaServerApiSearchCriterion, Unset_Type]
            The linked_records_criterion of this GrantaServerApiDataExportLinkedRecordExportBehavior.
        """
        return self._linked_records_criterion

    @linked_records_criterion.setter
    def linked_records_criterion(
        self,
        linked_records_criterion: "Union[GrantaServerApiSearchCriterion, Unset_Type]",
    ) -> None:
        """Sets the linked_records_criterion of this GrantaServerApiDataExportLinkedRecordExportBehavior.

        Parameters
        ----------
        linked_records_criterion: Union[GrantaServerApiSearchCriterion, Unset_Type]
            The linked_records_criterion of this GrantaServerApiDataExportLinkedRecordExportBehavior.
        """
        # Field is not nullable
        if linked_records_criterion is None:
            raise ValueError(
                "Invalid value for 'linked_records_criterion', must not be 'None'"
            )
        self._linked_records_criterion = linked_records_criterion

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
        if not isinstance(other, GrantaServerApiDataExportLinkedRecordExportBehavior):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
