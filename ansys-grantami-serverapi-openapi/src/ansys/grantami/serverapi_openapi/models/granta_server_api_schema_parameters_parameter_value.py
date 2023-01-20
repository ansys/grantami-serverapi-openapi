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


class GrantaServerApiSchemaParametersParameterValue(ModelBase):
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
        'is_default': 'bool',
        'name': 'str',
        'guid': 'str'
    }

    attribute_map = {
        'is_default': 'isDefault',
        'name': 'name',
        'guid': 'guid'
    }

    subtype_mapping = {
    }

    discriminator_value_class_map = {
        'discrete'.lower(): '#/components/schemas/GrantaServerApiSchemaParametersDiscreteParameterValue',
        'numeric'.lower(): '#/components/schemas/GrantaServerApiSchemaParametersNumericParameterValue',
    }

    def __init__(self, is_default=None, name=None, guid=None):  # noqa: E501
        """GrantaServerApiSchemaParametersParameterValue - a model defined in Swagger"""  # noqa: E501
        self._is_default = None
        self._name = None
        self._guid = None
        self.discriminator = 'type'
        if is_default is not None:
            self.is_default = is_default
        if name is not None:
            self.name = name
        if guid is not None:
            self.guid = guid

    @property
    def is_default(self):
        """Gets the is_default of this GrantaServerApiSchemaParametersParameterValue.  # noqa: E501

        :return: The is_default of this GrantaServerApiSchemaParametersParameterValue.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this GrantaServerApiSchemaParametersParameterValue.

        :param is_default: The is_default of this GrantaServerApiSchemaParametersParameterValue.  # noqa: E501
        :type: bool
        """
        self._is_default = is_default

    @property
    def name(self):
        """Gets the name of this GrantaServerApiSchemaParametersParameterValue.  # noqa: E501

        :return: The name of this GrantaServerApiSchemaParametersParameterValue.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GrantaServerApiSchemaParametersParameterValue.

        :param name: The name of this GrantaServerApiSchemaParametersParameterValue.  # noqa: E501
        :type: str
        """
        self._name = name

    @property
    def guid(self):
        """Gets the guid of this GrantaServerApiSchemaParametersParameterValue.  # noqa: E501

        :return: The guid of this GrantaServerApiSchemaParametersParameterValue.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this GrantaServerApiSchemaParametersParameterValue.

        :param guid: The guid of this GrantaServerApiSchemaParametersParameterValue.  # noqa: E501
        :type: str
        """
        self._guid = guid


    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self._get_discriminator_field_name()].lower()
        # The actual class name is not available in swagger-codegen, 
        # so we have to extract it from the JSON reference
        return self.discriminator_value_class_map.get(discriminator_value).rsplit("/", 1)[-1]

    def _get_discriminator_field_name(self):
        name_tokens = self.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

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
        if issubclass(GrantaServerApiSchemaParametersParameterValue, dict):
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
        if not isinstance(other, GrantaServerApiSchemaParametersParameterValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
