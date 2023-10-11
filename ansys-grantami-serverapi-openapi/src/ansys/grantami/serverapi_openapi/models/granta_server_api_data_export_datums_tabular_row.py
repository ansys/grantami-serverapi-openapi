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


class GrantaServerApiDataExportDatumsTabularRow(ModelBase):
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
        "linked_records": "list[GrantaServerApiIntegrationDataExportRecordReference]",
        "linking_value": "str",
        "local_data": "list[GrantaServerApiDataExportDatumsDatum]",
        "row_guid": "str",
        "row_number": "int",
    }

    attribute_map = {
        "linked_records": "linkedRecords",
        "linking_value": "linkingValue",
        "local_data": "localData",
        "row_guid": "rowGuid",
        "row_number": "rowNumber",
    }

    subtype_mapping = {
        "localData": "GrantaServerApiDataExportDatumsDatum",
        "linkedRecords": "GrantaServerApiIntegrationDataExportRecordReference",
    }

    def __init__(
        self,
        *,
        linked_records: "Optional[List[GrantaServerApiIntegrationDataExportRecordReference]]" = None,
        linking_value: "Optional[str]" = None,
        local_data: "Optional[List[GrantaServerApiDataExportDatumsDatum]]" = None,
        row_guid: "Optional[str]" = None,
        row_number: "Optional[int]" = None,
    ) -> None:
        """GrantaServerApiDataExportDatumsTabularRow - a model defined in Swagger

        Parameters
        ----------
            linked_records: List[GrantaServerApiIntegrationDataExportRecordReference], optional
            linking_value: str, optional
            local_data: List[GrantaServerApiDataExportDatumsDatum], optional
            row_guid: str, optional
            row_number: int, optional
        """
        self._row_guid = None
        self._linking_value = None
        self._row_number = None
        self._local_data = None
        self._linked_records = None
        self.discriminator = None
        if row_guid is not None:
            self.row_guid = row_guid
        if linking_value is not None:
            self.linking_value = linking_value
        if row_number is not None:
            self.row_number = row_number
        if local_data is not None:
            self.local_data = local_data
        if linked_records is not None:
            self.linked_records = linked_records

    @property
    def row_guid(self) -> "str":
        """Gets the row_guid of this GrantaServerApiDataExportDatumsTabularRow.

        Returns
        -------
        str
            The row_guid of this GrantaServerApiDataExportDatumsTabularRow.
        """
        return self._row_guid

    @row_guid.setter
    def row_guid(self, row_guid: "str") -> None:
        """Sets the row_guid of this GrantaServerApiDataExportDatumsTabularRow.

        Parameters
        ----------
        row_guid: str
            The row_guid of this GrantaServerApiDataExportDatumsTabularRow.
        """
        self._row_guid = row_guid

    @property
    def linking_value(self) -> "str":
        """Gets the linking_value of this GrantaServerApiDataExportDatumsTabularRow.

        Returns
        -------
        str
            The linking_value of this GrantaServerApiDataExportDatumsTabularRow.
        """
        return self._linking_value

    @linking_value.setter
    def linking_value(self, linking_value: "str") -> None:
        """Sets the linking_value of this GrantaServerApiDataExportDatumsTabularRow.

        Parameters
        ----------
        linking_value: str
            The linking_value of this GrantaServerApiDataExportDatumsTabularRow.
        """
        self._linking_value = linking_value

    @property
    def row_number(self) -> "int":
        """Gets the row_number of this GrantaServerApiDataExportDatumsTabularRow.

        Returns
        -------
        int
            The row_number of this GrantaServerApiDataExportDatumsTabularRow.
        """
        return self._row_number

    @row_number.setter
    def row_number(self, row_number: "int") -> None:
        """Sets the row_number of this GrantaServerApiDataExportDatumsTabularRow.

        Parameters
        ----------
        row_number: int
            The row_number of this GrantaServerApiDataExportDatumsTabularRow.
        """
        self._row_number = row_number

    @property
    def local_data(self) -> "list[GrantaServerApiDataExportDatumsDatum]":
        """Gets the local_data of this GrantaServerApiDataExportDatumsTabularRow.

        Returns
        -------
        list[GrantaServerApiDataExportDatumsDatum]
            The local_data of this GrantaServerApiDataExportDatumsTabularRow.
        """
        return self._local_data

    @local_data.setter
    def local_data(
        self, local_data: "list[GrantaServerApiDataExportDatumsDatum]"
    ) -> None:
        """Sets the local_data of this GrantaServerApiDataExportDatumsTabularRow.

        Parameters
        ----------
        local_data: list[GrantaServerApiDataExportDatumsDatum]
            The local_data of this GrantaServerApiDataExportDatumsTabularRow.
        """
        self._local_data = local_data

    @property
    def linked_records(
        self,
    ) -> "list[GrantaServerApiIntegrationDataExportRecordReference]":
        """Gets the linked_records of this GrantaServerApiDataExportDatumsTabularRow.

        Returns
        -------
        list[GrantaServerApiIntegrationDataExportRecordReference]
            The linked_records of this GrantaServerApiDataExportDatumsTabularRow.
        """
        return self._linked_records

    @linked_records.setter
    def linked_records(
        self,
        linked_records: "list[GrantaServerApiIntegrationDataExportRecordReference]",
    ) -> None:
        """Sets the linked_records of this GrantaServerApiDataExportDatumsTabularRow.

        Parameters
        ----------
        linked_records: list[GrantaServerApiIntegrationDataExportRecordReference]
            The linked_records of this GrantaServerApiDataExportDatumsTabularRow.
        """
        self._linked_records = linked_records

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
        if issubclass(GrantaServerApiDataExportDatumsTabularRow, dict):
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
        if not isinstance(other, GrantaServerApiDataExportDatumsTabularRow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
