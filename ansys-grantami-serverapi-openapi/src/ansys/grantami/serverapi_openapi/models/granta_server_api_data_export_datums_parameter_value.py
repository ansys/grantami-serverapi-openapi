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


class GrantaServerApiDataExportDatumsParameterValue(ModelBase):
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
        'parameter': 'GrantaServerApiParameterInfo',
        'value_name': 'str',
        'value': 'float'
    }

    attribute_map = {
        'parameter': 'parameter',
        'value_name': 'valueName',
        'value': 'value'
    }

    subtype_mapping = {
        'parameter': 'GrantaServerApiParameterInfo',
    }


    def __init__(self, parameter=None, value_name=None, value=None):  # noqa: E501
        """GrantaServerApiDataExportDatumsParameterValue - a model defined in Swagger"""  # noqa: E501
        self._parameter = None
        self._value_name = None
        self._value = None
        self.discriminator = None
        if parameter is not None:
            self.parameter = parameter
        if value_name is not None:
            self.value_name = value_name
        if value is not None:
            self.value = value

    @property
    def parameter(self):
        """Gets the parameter of this GrantaServerApiDataExportDatumsParameterValue.  # noqa: E501

        :return: The parameter of this GrantaServerApiDataExportDatumsParameterValue.  # noqa: E501
        :rtype: GrantaServerApiParameterInfo
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        """Sets the parameter of this GrantaServerApiDataExportDatumsParameterValue.

        :param parameter: The parameter of this GrantaServerApiDataExportDatumsParameterValue.  # noqa: E501
        :type: GrantaServerApiParameterInfo
        """
        self._parameter = parameter

    @property
    def value_name(self):
        """Gets the value_name of this GrantaServerApiDataExportDatumsParameterValue.  # noqa: E501

        :return: The value_name of this GrantaServerApiDataExportDatumsParameterValue.  # noqa: E501
        :rtype: str
        """
        return self._value_name

    @value_name.setter
    def value_name(self, value_name):
        """Sets the value_name of this GrantaServerApiDataExportDatumsParameterValue.

        :param value_name: The value_name of this GrantaServerApiDataExportDatumsParameterValue.  # noqa: E501
        :type: str
        """
        self._value_name = value_name

    @property
    def value(self):
        """Gets the value of this GrantaServerApiDataExportDatumsParameterValue.  # noqa: E501

        :return: The value of this GrantaServerApiDataExportDatumsParameterValue.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GrantaServerApiDataExportDatumsParameterValue.

        :param value: The value of this GrantaServerApiDataExportDatumsParameterValue.  # noqa: E501
        :type: float
        """
        self._value = value


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
        if issubclass(GrantaServerApiDataExportDatumsParameterValue, dict):
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
        if not isinstance(other, GrantaServerApiDataExportDatumsParameterValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
