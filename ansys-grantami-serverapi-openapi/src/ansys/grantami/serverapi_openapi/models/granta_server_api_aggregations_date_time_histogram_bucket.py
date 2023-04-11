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


class GrantaServerApiAggregationsDateTimeHistogramBucket(ModelBase):
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
        'lower': 'datetime',
        'count': 'int'
    }

    attribute_map = {
        'lower': 'lower',
        'count': 'count'
    }

    subtype_mapping = {
    }


    def __init__(self, lower=None, count=None):  # noqa: E501
        """GrantaServerApiAggregationsDateTimeHistogramBucket - a model defined in Swagger"""  # noqa: E501
        self._lower = None
        self._count = None
        self.discriminator = None
        if lower is not None:
            self.lower = lower
        if count is not None:
            self.count = count

    @property
    def lower(self):
        """Gets the lower of this GrantaServerApiAggregationsDateTimeHistogramBucket.  # noqa: E501

        :return: The lower of this GrantaServerApiAggregationsDateTimeHistogramBucket.  # noqa: E501
        :rtype: datetime
        """
        return self._lower

    @lower.setter
    def lower(self, lower):
        """Sets the lower of this GrantaServerApiAggregationsDateTimeHistogramBucket.

        :param lower: The lower of this GrantaServerApiAggregationsDateTimeHistogramBucket.  # noqa: E501
        :type: datetime
        """
        self._lower = lower

    @property
    def count(self):
        """Gets the count of this GrantaServerApiAggregationsDateTimeHistogramBucket.  # noqa: E501

        :return: The count of this GrantaServerApiAggregationsDateTimeHistogramBucket.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this GrantaServerApiAggregationsDateTimeHistogramBucket.

        :param count: The count of this GrantaServerApiAggregationsDateTimeHistogramBucket.  # noqa: E501
        :type: int
        """
        self._count = count

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
        if issubclass(GrantaServerApiAggregationsDateTimeHistogramBucket, dict):
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
        if not isinstance(other, GrantaServerApiAggregationsDateTimeHistogramBucket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other