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

from ansys.grantami.serverapi_openapi.models.granta_server_api_data_export_datums_applicable_datum import GrantaServerApiDataExportDatumsApplicableDatum  # noqa: F401,E501

class GrantaServerApiDataExportDatumsLinkedRecordsDatum(GrantaServerApiDataExportDatumsApplicableDatum):
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
        'link_group_name': 'str',
        'linked_records': 'list[GrantaServerApiIntegrationDataExportRecordReference]',
        'datum_type': 'str'
    }
    if hasattr(GrantaServerApiDataExportDatumsApplicableDatum, "swagger_types"):
        swagger_types.update(GrantaServerApiDataExportDatumsApplicableDatum.swagger_types)

    attribute_map = {
        'link_group_name': 'linkGroupName',
        'linked_records': 'linkedRecords',
        'datum_type': 'datumType'
    }
    if hasattr(GrantaServerApiDataExportDatumsApplicableDatum, "attribute_map"):
        attribute_map.update(GrantaServerApiDataExportDatumsApplicableDatum.attribute_map)

    subtype_mapping = {
        'linkedRecords': 'GrantaServerApiIntegrationDataExportRecordReference',
    }


    def __init__(self, link_group_name=None, linked_records=None, datum_type='link', *args, **kwargs):  # noqa: E501
        """GrantaServerApiDataExportDatumsLinkedRecordsDatum - a model defined in Swagger"""  # noqa: E501
        GrantaServerApiDataExportDatumsApplicableDatum.__init__(self, *args, **kwargs)
        self._link_group_name = None
        self._linked_records = None
        self._datum_type = None
        self.discriminator = None
        if link_group_name is not None:
            self.link_group_name = link_group_name
        if linked_records is not None:
            self.linked_records = linked_records
        self.datum_type = datum_type

    @property
    def link_group_name(self):
        """Gets the link_group_name of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.  # noqa: E501

        :return: The link_group_name of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.  # noqa: E501
        :rtype: str
        """
        return self._link_group_name

    @link_group_name.setter
    def link_group_name(self, link_group_name):
        """Sets the link_group_name of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.

        :param link_group_name: The link_group_name of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.  # noqa: E501
        :type: str
        """
        self._link_group_name = link_group_name

    @property
    def linked_records(self):
        """Gets the linked_records of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.  # noqa: E501

        :return: The linked_records of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.  # noqa: E501
        :rtype: list[GrantaServerApiIntegrationDataExportRecordReference]
        """
        return self._linked_records

    @linked_records.setter
    def linked_records(self, linked_records):
        """Sets the linked_records of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.

        :param linked_records: The linked_records of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.  # noqa: E501
        :type: list[GrantaServerApiIntegrationDataExportRecordReference]
        """
        self._linked_records = linked_records

    @property
    def datum_type(self):
        """Gets the datum_type of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.  # noqa: E501

        :return: The datum_type of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.  # noqa: E501
        :rtype: str
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type):
        """Sets the datum_type of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.

        :param datum_type: The datum_type of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.  # noqa: E501
        :type: str
        """
        if datum_type is None:
            raise ValueError("Invalid value for `datum_type`, must not be `None`")  # noqa: E501
        self._datum_type = datum_type


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
        if issubclass(GrantaServerApiDataExportDatumsLinkedRecordsDatum, dict):
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
        if not isinstance(other, GrantaServerApiDataExportDatumsLinkedRecordsDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
