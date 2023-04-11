# coding: utf-8

"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
from . import ModelBase


class GrantaServerApiDataExportDatumsTabularRow(ModelBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'row_guid': 'str',
        'linking_value': 'str',
        'row_number': 'int',
        'local_data': 'list[GrantaServerApiDataExportDatumsDatum]',
        'linked_records': 'list[GrantaServerApiIntegrationDataExportRecordReference]'
    }

    attribute_map = {
        'row_guid': 'rowGuid',
        'linking_value': 'linkingValue',
        'row_number': 'rowNumber',
        'local_data': 'localData',
        'linked_records': 'linkedRecords'
    }

    subtype_mapping = {
        'localData': 'GrantaServerApiDataExportDatumsDatum',
        'linkedRecords': 'GrantaServerApiIntegrationDataExportRecordReference'
    }


    def __init__(self, row_guid=None, linking_value=None, row_number=None, local_data=None, linked_records=None):  # noqa: E501
        """GrantaServerApiDataExportDatumsTabularRow - a model defined in Swagger"""  # noqa: E501
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
    def row_guid(self):
        """Gets the row_guid of this GrantaServerApiDataExportDatumsTabularRow.  # noqa: E501

        :return: The row_guid of this GrantaServerApiDataExportDatumsTabularRow.  # noqa: E501
        :rtype: str
        """
        return self._row_guid

    @row_guid.setter
    def row_guid(self, row_guid):
        """Sets the row_guid of this GrantaServerApiDataExportDatumsTabularRow.

        :param row_guid: The row_guid of this GrantaServerApiDataExportDatumsTabularRow.  # noqa: E501
        :type: str
        """
        self._row_guid = row_guid

    @property
    def linking_value(self):
        """Gets the linking_value of this GrantaServerApiDataExportDatumsTabularRow.  # noqa: E501

        :return: The linking_value of this GrantaServerApiDataExportDatumsTabularRow.  # noqa: E501
        :rtype: str
        """
        return self._linking_value

    @linking_value.setter
    def linking_value(self, linking_value):
        """Sets the linking_value of this GrantaServerApiDataExportDatumsTabularRow.

        :param linking_value: The linking_value of this GrantaServerApiDataExportDatumsTabularRow.  # noqa: E501
        :type: str
        """
        self._linking_value = linking_value

    @property
    def row_number(self):
        """Gets the row_number of this GrantaServerApiDataExportDatumsTabularRow.  # noqa: E501

        :return: The row_number of this GrantaServerApiDataExportDatumsTabularRow.  # noqa: E501
        :rtype: int
        """
        return self._row_number

    @row_number.setter
    def row_number(self, row_number):
        """Sets the row_number of this GrantaServerApiDataExportDatumsTabularRow.

        :param row_number: The row_number of this GrantaServerApiDataExportDatumsTabularRow.  # noqa: E501
        :type: int
        """
        self._row_number = row_number

    @property
    def local_data(self):
        """Gets the local_data of this GrantaServerApiDataExportDatumsTabularRow.  # noqa: E501

        :return: The local_data of this GrantaServerApiDataExportDatumsTabularRow.  # noqa: E501
        :rtype: list[GrantaServerApiDataExportDatumsDatum]
        """
        return self._local_data

    @local_data.setter
    def local_data(self, local_data):
        """Sets the local_data of this GrantaServerApiDataExportDatumsTabularRow.

        :param local_data: The local_data of this GrantaServerApiDataExportDatumsTabularRow.  # noqa: E501
        :type: list[GrantaServerApiDataExportDatumsDatum]
        """
        self._local_data = local_data

    @property
    def linked_records(self):
        """Gets the linked_records of this GrantaServerApiDataExportDatumsTabularRow.  # noqa: E501

        :return: The linked_records of this GrantaServerApiDataExportDatumsTabularRow.  # noqa: E501
        :rtype: list[GrantaServerApiIntegrationDataExportRecordReference]
        """
        return self._linked_records

    @linked_records.setter
    def linked_records(self, linked_records):
        """Sets the linked_records of this GrantaServerApiDataExportDatumsTabularRow.

        :param linked_records: The linked_records of this GrantaServerApiDataExportDatumsTabularRow.  # noqa: E501
        :type: list[GrantaServerApiIntegrationDataExportRecordReference]
        """
        self._linked_records = linked_records

    def get_real_child_model(self, data):
        """Raises a NotImplementedError for a type without a discriminator defined."""
        raise NotImplementedError()

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr in self.swagger_types.keys():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GrantaServerApiDataExportDatumsTabularRow, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiDataExportDatumsTabularRow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other