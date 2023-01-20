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

from ansys.grantami.serverapi_openapi.models.granta_server_api_aggregations_attribute_value_aggregation import GrantaServerApiAggregationsAttributeValueAggregation  # noqa: F401,E501

class GrantaServerApiAggregationsIntegerAttributeAggregation(GrantaServerApiAggregationsAttributeValueAggregation):
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
        'minimum': 'int',
        'maximum': 'int',
        'datum_type': 'str'
    }
    if hasattr(GrantaServerApiAggregationsAttributeValueAggregation, "swagger_types"):
        swagger_types.update(GrantaServerApiAggregationsAttributeValueAggregation.swagger_types)

    attribute_map = {
        'minimum': 'minimum',
        'maximum': 'maximum',
        'datum_type': 'datumType'
    }
    if hasattr(GrantaServerApiAggregationsAttributeValueAggregation, "attribute_map"):
        attribute_map.update(GrantaServerApiAggregationsAttributeValueAggregation.attribute_map)

    subtype_mapping = {
    }


    def __init__(self, minimum=None, maximum=None, datum_type='integer', *args, **kwargs):  # noqa: E501
        """GrantaServerApiAggregationsIntegerAttributeAggregation - a model defined in Swagger"""  # noqa: E501
        GrantaServerApiAggregationsAttributeValueAggregation.__init__(self, *args, **kwargs)
        self._minimum = None
        self._maximum = None
        self._datum_type = None
        self.discriminator = None
        if minimum is not None:
            self.minimum = minimum
        if maximum is not None:
            self.maximum = maximum
        self.datum_type = datum_type

    @property
    def minimum(self):
        """Gets the minimum of this GrantaServerApiAggregationsIntegerAttributeAggregation.  # noqa: E501

        :return: The minimum of this GrantaServerApiAggregationsIntegerAttributeAggregation.  # noqa: E501
        :rtype: int
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """Sets the minimum of this GrantaServerApiAggregationsIntegerAttributeAggregation.

        :param minimum: The minimum of this GrantaServerApiAggregationsIntegerAttributeAggregation.  # noqa: E501
        :type: int
        """
        self._minimum = minimum

    @property
    def maximum(self):
        """Gets the maximum of this GrantaServerApiAggregationsIntegerAttributeAggregation.  # noqa: E501

        :return: The maximum of this GrantaServerApiAggregationsIntegerAttributeAggregation.  # noqa: E501
        :rtype: int
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this GrantaServerApiAggregationsIntegerAttributeAggregation.

        :param maximum: The maximum of this GrantaServerApiAggregationsIntegerAttributeAggregation.  # noqa: E501
        :type: int
        """
        self._maximum = maximum

    @property
    def datum_type(self):
        """Gets the datum_type of this GrantaServerApiAggregationsIntegerAttributeAggregation.  # noqa: E501

        :return: The datum_type of this GrantaServerApiAggregationsIntegerAttributeAggregation.  # noqa: E501
        :rtype: str
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type):
        """Sets the datum_type of this GrantaServerApiAggregationsIntegerAttributeAggregation.

        :param datum_type: The datum_type of this GrantaServerApiAggregationsIntegerAttributeAggregation.  # noqa: E501
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
        if issubclass(GrantaServerApiAggregationsIntegerAttributeAggregation, dict):
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
        if not isinstance(other, GrantaServerApiAggregationsIntegerAttributeAggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
