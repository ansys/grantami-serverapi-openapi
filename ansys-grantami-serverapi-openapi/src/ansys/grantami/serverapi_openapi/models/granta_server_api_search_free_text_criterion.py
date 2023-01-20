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

from ansys.grantami.serverapi_openapi.models.granta_server_api_search_criterion import GrantaServerApiSearchCriterion  # noqa: F401,E501

class GrantaServerApiSearchFreeTextCriterion(GrantaServerApiSearchCriterion):
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
        'identities': 'list[int]',
        'value': 'str',
        'identities_to_boost': 'list[GrantaServerApiSearchBoost]',
        'type': 'str'
    }
    if hasattr(GrantaServerApiSearchCriterion, "swagger_types"):
        swagger_types.update(GrantaServerApiSearchCriterion.swagger_types)

    attribute_map = {
        'identities': 'identities',
        'value': 'value',
        'identities_to_boost': 'identitiesToBoost',
        'type': 'type'
    }
    if hasattr(GrantaServerApiSearchCriterion, "attribute_map"):
        attribute_map.update(GrantaServerApiSearchCriterion.attribute_map)

    subtype_mapping = {
        'identitiesToBoost': 'GrantaServerApiSearchBoost',
    }


    def __init__(self, identities=None, value=None, identities_to_boost=None, type='text', *args, **kwargs):  # noqa: E501
        """GrantaServerApiSearchFreeTextCriterion - a model defined in Swagger"""  # noqa: E501
        GrantaServerApiSearchCriterion.__init__(self, *args, **kwargs)
        self._identities = None
        self._value = None
        self._identities_to_boost = None
        self._type = None
        self.discriminator = None
        if identities is not None:
            self.identities = identities
        if value is not None:
            self.value = value
        if identities_to_boost is not None:
            self.identities_to_boost = identities_to_boost
        self.type = type

    @property
    def identities(self):
        """Gets the identities of this GrantaServerApiSearchFreeTextCriterion.  # noqa: E501

        :return: The identities of this GrantaServerApiSearchFreeTextCriterion.  # noqa: E501
        :rtype: list[int]
        """
        return self._identities

    @identities.setter
    def identities(self, identities):
        """Sets the identities of this GrantaServerApiSearchFreeTextCriterion.

        :param identities: The identities of this GrantaServerApiSearchFreeTextCriterion.  # noqa: E501
        :type: list[int]
        """
        self._identities = identities

    @property
    def value(self):
        """Gets the value of this GrantaServerApiSearchFreeTextCriterion.  # noqa: E501

        :return: The value of this GrantaServerApiSearchFreeTextCriterion.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GrantaServerApiSearchFreeTextCriterion.

        :param value: The value of this GrantaServerApiSearchFreeTextCriterion.  # noqa: E501
        :type: str
        """
        self._value = value

    @property
    def identities_to_boost(self):
        """Gets the identities_to_boost of this GrantaServerApiSearchFreeTextCriterion.  # noqa: E501

        :return: The identities_to_boost of this GrantaServerApiSearchFreeTextCriterion.  # noqa: E501
        :rtype: list[GrantaServerApiSearchBoost]
        """
        return self._identities_to_boost

    @identities_to_boost.setter
    def identities_to_boost(self, identities_to_boost):
        """Sets the identities_to_boost of this GrantaServerApiSearchFreeTextCriterion.

        :param identities_to_boost: The identities_to_boost of this GrantaServerApiSearchFreeTextCriterion.  # noqa: E501
        :type: list[GrantaServerApiSearchBoost]
        """
        self._identities_to_boost = identities_to_boost

    @property
    def type(self):
        """Gets the type of this GrantaServerApiSearchFreeTextCriterion.  # noqa: E501

        :return: The type of this GrantaServerApiSearchFreeTextCriterion.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GrantaServerApiSearchFreeTextCriterion.

        :param type: The type of this GrantaServerApiSearchFreeTextCriterion.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type


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
        if issubclass(GrantaServerApiSearchFreeTextCriterion, dict):
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
        if not isinstance(other, GrantaServerApiSearchFreeTextCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
