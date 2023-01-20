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


class GrantaServerApiIntegrationIndexRecordFailure(ModelBase):
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
        'record_history_identity': 'int',
        'record_name': 'str',
        'error': 'str',
        'record_was_oversized': 'bool'
    }

    attribute_map = {
        'record_history_identity': 'recordHistoryIdentity',
        'record_name': 'recordName',
        'error': 'error',
        'record_was_oversized': 'recordWasOversized'
    }

    subtype_mapping = {
    }


    def __init__(self, record_history_identity=None, record_name=None, error=None, record_was_oversized=None):  # noqa: E501
        """GrantaServerApiIntegrationIndexRecordFailure - a model defined in Swagger"""  # noqa: E501
        self._record_history_identity = None
        self._record_name = None
        self._error = None
        self._record_was_oversized = None
        self.discriminator = None
        if record_history_identity is not None:
            self.record_history_identity = record_history_identity
        if record_name is not None:
            self.record_name = record_name
        if error is not None:
            self.error = error
        if record_was_oversized is not None:
            self.record_was_oversized = record_was_oversized

    @property
    def record_history_identity(self):
        """Gets the record_history_identity of this GrantaServerApiIntegrationIndexRecordFailure.  # noqa: E501

        :return: The record_history_identity of this GrantaServerApiIntegrationIndexRecordFailure.  # noqa: E501
        :rtype: int
        """
        return self._record_history_identity

    @record_history_identity.setter
    def record_history_identity(self, record_history_identity):
        """Sets the record_history_identity of this GrantaServerApiIntegrationIndexRecordFailure.

        :param record_history_identity: The record_history_identity of this GrantaServerApiIntegrationIndexRecordFailure.  # noqa: E501
        :type: int
        """
        self._record_history_identity = record_history_identity

    @property
    def record_name(self):
        """Gets the record_name of this GrantaServerApiIntegrationIndexRecordFailure.  # noqa: E501

        :return: The record_name of this GrantaServerApiIntegrationIndexRecordFailure.  # noqa: E501
        :rtype: str
        """
        return self._record_name

    @record_name.setter
    def record_name(self, record_name):
        """Sets the record_name of this GrantaServerApiIntegrationIndexRecordFailure.

        :param record_name: The record_name of this GrantaServerApiIntegrationIndexRecordFailure.  # noqa: E501
        :type: str
        """
        self._record_name = record_name

    @property
    def error(self):
        """Gets the error of this GrantaServerApiIntegrationIndexRecordFailure.  # noqa: E501
        This is the error message from the indexing exception. It may have been returned directly from Elasticsearch.  # noqa: E501

        :return: The error of this GrantaServerApiIntegrationIndexRecordFailure.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this GrantaServerApiIntegrationIndexRecordFailure.
        This is the error message from the indexing exception. It may have been returned directly from Elasticsearch.  # noqa: E501

        :param error: The error of this GrantaServerApiIntegrationIndexRecordFailure.  # noqa: E501
        :type: str
        """
        self._error = error

    @property
    def record_was_oversized(self):
        """Gets the record_was_oversized of this GrantaServerApiIntegrationIndexRecordFailure.  # noqa: E501
        Records that contain a large amount of data are intentionally not sent to the index. This size limit is configurable through  MIServer.exe.config  # noqa: E501

        :return: The record_was_oversized of this GrantaServerApiIntegrationIndexRecordFailure.  # noqa: E501
        :rtype: bool
        """
        return self._record_was_oversized

    @record_was_oversized.setter
    def record_was_oversized(self, record_was_oversized):
        """Sets the record_was_oversized of this GrantaServerApiIntegrationIndexRecordFailure.
        Records that contain a large amount of data are intentionally not sent to the index. This size limit is configurable through  MIServer.exe.config  # noqa: E501

        :param record_was_oversized: The record_was_oversized of this GrantaServerApiIntegrationIndexRecordFailure.  # noqa: E501
        :type: bool
        """
        self._record_was_oversized = record_was_oversized

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
        if issubclass(GrantaServerApiIntegrationIndexRecordFailure, dict):
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
        if not isinstance(other, GrantaServerApiIntegrationIndexRecordFailure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
