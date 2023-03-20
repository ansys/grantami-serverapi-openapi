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

class GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute(GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute):
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
        'unit': 'GrantaServerApiSchemaSlimEntitiesSlimUnit',
        'is_multi_valued': 'bool',
        'attribute_parameters': 'list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]'
    }
    if hasattr(GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute, "swagger_types"):
        swagger_types.update(GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.swagger_types)

    attribute_map = {
        'type': 'type',
        'unit': 'unit',
        'is_multi_valued': 'isMultiValued',
        'attribute_parameters': 'attributeParameters'
    }
    if hasattr(GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute, "attribute_map"):
        attribute_map.update(GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.attribute_map)

    subtype_mapping = {
        'unit': 'GrantaServerApiSchemaSlimEntitiesSlimUnit',
        'attributeParameters': 'GrantaServerApiSchemaSlimEntitiesSlimNamedEntity'
    }


    def __init__(self, type='point', unit=None, is_multi_valued=None, attribute_parameters=None, *args, **kwargs):  # noqa: E501
        """GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute - a model defined in Swagger"""  # noqa: E501
        GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.__init__(self, *args, **kwargs)
        self._type = None
        self._unit = None
        self._is_multi_valued = None
        self._attribute_parameters = None
        self.discriminator = None
        self.type = type
        if unit is not None:
            self.unit = unit
        if is_multi_valued is not None:
            self.is_multi_valued = is_multi_valued
        if attribute_parameters is not None:
            self.attribute_parameters = attribute_parameters

    @property
    def type(self):
        """Gets the type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.  # noqa: E501

        :return: The type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.

        :param type: The type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type

    @property
    def unit(self):
        """Gets the unit of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.  # noqa: E501

        :return: The unit of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.  # noqa: E501
        :rtype: GrantaServerApiSchemaSlimEntitiesSlimUnit
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.

        :param unit: The unit of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.  # noqa: E501
        :type: GrantaServerApiSchemaSlimEntitiesSlimUnit
        """
        self._unit = unit

    @property
    def is_multi_valued(self):
        """Gets the is_multi_valued of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.  # noqa: E501

        :return: The is_multi_valued of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._is_multi_valued

    @is_multi_valued.setter
    def is_multi_valued(self, is_multi_valued):
        """Sets the is_multi_valued of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.

        :param is_multi_valued: The is_multi_valued of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.  # noqa: E501
        :type: bool
        """
        self._is_multi_valued = is_multi_valued

    @property
    def attribute_parameters(self):
        """Gets the attribute_parameters of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.  # noqa: E501

        :return: The attribute_parameters of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.  # noqa: E501
        :rtype: list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
        """
        return self._attribute_parameters

    @attribute_parameters.setter
    def attribute_parameters(self, attribute_parameters):
        """Sets the attribute_parameters of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.

        :param attribute_parameters: The attribute_parameters of this GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute.  # noqa: E501
        :type: list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
        """
        self._attribute_parameters = attribute_parameters

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
        if issubclass(GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute, dict):
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
        if not isinstance(other, GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
