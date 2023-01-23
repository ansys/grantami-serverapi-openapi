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

from ansys.grantami.serverapi_openapi.models.granta_server_api_aggregations_attribute_aggregation import GrantaServerApiAggregationsAttributeAggregation  # noqa: F401,E501

class GrantaServerApiAggregationsAttributeValueAggregation(GrantaServerApiAggregationsAttributeAggregation):
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
        'attribute_aggregation_type': 'str'
    }
    if hasattr(GrantaServerApiAggregationsAttributeAggregation, "swagger_types"):
        swagger_types.update(GrantaServerApiAggregationsAttributeAggregation.swagger_types)

    attribute_map = {
        'attribute_aggregation_type': 'attributeAggregationType'
    }
    if hasattr(GrantaServerApiAggregationsAttributeAggregation, "attribute_map"):
        attribute_map.update(GrantaServerApiAggregationsAttributeAggregation.attribute_map)

    subtype_mapping = {
    }

    discriminator_value_class_map = {
        'integer'.lower(): '#/components/schemas/GrantaServerApiAggregationsIntegerAttributeAggregation',
        'point'.lower(): '#/components/schemas/GrantaServerApiAggregationsPointAttributeAggregation',
        'range'.lower(): '#/components/schemas/GrantaServerApiAggregationsRangeAttributeAggregation',
        'dateTime'.lower(): '#/components/schemas/GrantaServerApiAggregationsDateTimeAttributeAggregation',
        'shortText'.lower(): '#/components/schemas/GrantaServerApiAggregationsShortTextAttributeAggregation',
        'discreteText'.lower(): '#/components/schemas/GrantaServerApiAggregationsDiscreteTextAttributeAggregation',
        'link'.lower(): '#/components/schemas/GrantaServerApiAggregationsLinkAttributeAggregation',
        'logical'.lower(): '#/components/schemas/GrantaServerApiAggregationsLogicalAttributeAggregation',
    }

    def __init__(self, attribute_aggregation_type='value', *args, **kwargs):  # noqa: E501
        """GrantaServerApiAggregationsAttributeValueAggregation - a model defined in Swagger"""  # noqa: E501
        GrantaServerApiAggregationsAttributeAggregation.__init__(self, *args, **kwargs)
        self._attribute_aggregation_type = None
        self.discriminator = 'datum_type'
        self.attribute_aggregation_type = attribute_aggregation_type

    @property
    def attribute_aggregation_type(self):
        """Gets the attribute_aggregation_type of this GrantaServerApiAggregationsAttributeValueAggregation.  # noqa: E501

        :return: The attribute_aggregation_type of this GrantaServerApiAggregationsAttributeValueAggregation.  # noqa: E501
        :rtype: str
        """
        return self._attribute_aggregation_type

    @attribute_aggregation_type.setter
    def attribute_aggregation_type(self, attribute_aggregation_type):
        """Sets the attribute_aggregation_type of this GrantaServerApiAggregationsAttributeValueAggregation.

        :param attribute_aggregation_type: The attribute_aggregation_type of this GrantaServerApiAggregationsAttributeValueAggregation.  # noqa: E501
        :type: str
        """
        if attribute_aggregation_type is None:
            raise ValueError("Invalid value for `attribute_aggregation_type`, must not be `None`")  # noqa: E501
        self._attribute_aggregation_type = attribute_aggregation_type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = str(data[self._get_discriminator_field_name()]).lower()
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
        if issubclass(GrantaServerApiAggregationsAttributeValueAggregation, dict):
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
        if not isinstance(other, GrantaServerApiAggregationsAttributeValueAggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
