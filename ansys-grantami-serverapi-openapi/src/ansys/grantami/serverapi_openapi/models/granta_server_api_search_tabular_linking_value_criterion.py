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

class GrantaServerApiSearchTabularLinkingValueCriterion(GrantaServerApiSearchCriterion):
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
        'values': 'list[str]',
        'linking_value_match_behaviour': 'GrantaServerApiSearchLinkingValueMatchBehaviour',
        'type': 'str'
    }
    if hasattr(GrantaServerApiSearchCriterion, "swagger_types"):
        swagger_types.update(GrantaServerApiSearchCriterion.swagger_types)

    attribute_map = {
        'values': 'values',
        'linking_value_match_behaviour': 'linkingValueMatchBehaviour',
        'type': 'type'
    }
    if hasattr(GrantaServerApiSearchCriterion, "attribute_map"):
        attribute_map.update(GrantaServerApiSearchCriterion.attribute_map)

    subtype_mapping = {
        'linkingValueMatchBehaviour': 'GrantaServerApiSearchLinkingValueMatchBehaviour',
    }


    def __init__(self, values=None, linking_value_match_behaviour=None, type='tabularLinkingValue', *args, **kwargs):  # noqa: E501
        """GrantaServerApiSearchTabularLinkingValueCriterion - a model defined in Swagger"""  # noqa: E501
        GrantaServerApiSearchCriterion.__init__(self, *args, **kwargs)
        self._values = None
        self._linking_value_match_behaviour = None
        self._type = None
        self.discriminator = None
        if values is not None:
            self.values = values
        if linking_value_match_behaviour is not None:
            self.linking_value_match_behaviour = linking_value_match_behaviour
        self.type = type

    @property
    def values(self):
        """Gets the values of this GrantaServerApiSearchTabularLinkingValueCriterion.  # noqa: E501

        :return: The values of this GrantaServerApiSearchTabularLinkingValueCriterion.  # noqa: E501
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this GrantaServerApiSearchTabularLinkingValueCriterion.

        :param values: The values of this GrantaServerApiSearchTabularLinkingValueCriterion.  # noqa: E501
        :type: list[str]
        """
        self._values = values

    @property
    def linking_value_match_behaviour(self):
        """Gets the linking_value_match_behaviour of this GrantaServerApiSearchTabularLinkingValueCriterion.  # noqa: E501

        :return: The linking_value_match_behaviour of this GrantaServerApiSearchTabularLinkingValueCriterion.  # noqa: E501
        :rtype: GrantaServerApiSearchLinkingValueMatchBehaviour
        """
        return self._linking_value_match_behaviour

    @linking_value_match_behaviour.setter
    def linking_value_match_behaviour(self, linking_value_match_behaviour):
        """Sets the linking_value_match_behaviour of this GrantaServerApiSearchTabularLinkingValueCriterion.

        :param linking_value_match_behaviour: The linking_value_match_behaviour of this GrantaServerApiSearchTabularLinkingValueCriterion.  # noqa: E501
        :type: GrantaServerApiSearchLinkingValueMatchBehaviour
        """
        self._linking_value_match_behaviour = linking_value_match_behaviour

    @property
    def type(self):
        """Gets the type of this GrantaServerApiSearchTabularLinkingValueCriterion.  # noqa: E501

        :return: The type of this GrantaServerApiSearchTabularLinkingValueCriterion.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GrantaServerApiSearchTabularLinkingValueCriterion.

        :param type: The type of this GrantaServerApiSearchTabularLinkingValueCriterion.  # noqa: E501
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
        if issubclass(GrantaServerApiSearchTabularLinkingValueCriterion, dict):
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
        if not isinstance(other, GrantaServerApiSearchTabularLinkingValueCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
