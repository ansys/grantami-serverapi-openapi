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

from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_attributes_update_attributes_update_attribute import GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute  # noqa: F401,E501

class GrantaServerApiSchemaAttributesUpdateAttributesUpdateShortTextAttribute(GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute):
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
        'type': 'str',
        'is_unique': 'bool',
        'data_rule': 'GrantaServerApiSchemaSlimEntitiesSlimNamedEntity'
    }
    if hasattr(GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute, "swagger_types"):
        swagger_types.update(GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.swagger_types)

    attribute_map = {
        'type': 'type',
        'is_unique': 'isUnique',
        'data_rule': 'dataRule'
    }
    if hasattr(GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute, "attribute_map"):
        attribute_map.update(GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.attribute_map)

    subtype_mapping = {
        'dataRule': 'GrantaServerApiSchemaSlimEntitiesSlimNamedEntity'
    }


    def __init__(self, type='shortText', is_unique=None, data_rule=None, *args, **kwargs):  # noqa: E501
        """GrantaServerApiSchemaAttributesUpdateAttributesUpdateShortTextAttribute - a model defined in Swagger"""  # noqa: E501
        GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.__init__(self, *args, **kwargs)
        self._type = None
        self._is_unique = None
        self._data_rule = None
        self.discriminator = None
        self.type = type
        if is_unique is not None:
            self.is_unique = is_unique
        if data_rule is not None:
            self.data_rule = data_rule

    @property
    def type(self):
        """Gets the type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateShortTextAttribute.  # noqa: E501

        :return: The type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateShortTextAttribute.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateShortTextAttribute.

        :param type: The type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateShortTextAttribute.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type

    @property
    def is_unique(self):
        """Gets the is_unique of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateShortTextAttribute.  # noqa: E501

        :return: The is_unique of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateShortTextAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._is_unique

    @is_unique.setter
    def is_unique(self, is_unique):
        """Sets the is_unique of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateShortTextAttribute.

        :param is_unique: The is_unique of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateShortTextAttribute.  # noqa: E501
        :type: bool
        """
        self._is_unique = is_unique

    @property
    def data_rule(self):
        """Gets the data_rule of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateShortTextAttribute.  # noqa: E501

        :return: The data_rule of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateShortTextAttribute.  # noqa: E501
        :rtype: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
        """
        return self._data_rule

    @data_rule.setter
    def data_rule(self, data_rule):
        """Sets the data_rule of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateShortTextAttribute.

        :param data_rule: The data_rule of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateShortTextAttribute.  # noqa: E501
        :type: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
        """
        self._data_rule = data_rule

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
        if issubclass(GrantaServerApiSchemaAttributesUpdateAttributesUpdateShortTextAttribute, dict):
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
        if not isinstance(other, GrantaServerApiSchemaAttributesUpdateAttributesUpdateShortTextAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
