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

from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_layouts_layout_section import GrantaServerApiSchemaLayoutsLayoutSection  # noqa: F401,E501

class GrantaServerApiSchemaLayoutsFullLayoutSection(GrantaServerApiSchemaLayoutsLayoutSection):
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
        'section_detail_type': 'str',
        'section_items': 'list[GrantaServerApiSchemaLayoutsLayoutItem]'
    }
    if hasattr(GrantaServerApiSchemaLayoutsLayoutSection, "swagger_types"):
        swagger_types.update(GrantaServerApiSchemaLayoutsLayoutSection.swagger_types)

    attribute_map = {
        'section_detail_type': 'sectionDetailType',
        'section_items': 'sectionItems'
    }
    if hasattr(GrantaServerApiSchemaLayoutsLayoutSection, "attribute_map"):
        attribute_map.update(GrantaServerApiSchemaLayoutsLayoutSection.attribute_map)

    subtype_mapping = {
        'sectionItems': 'GrantaServerApiSchemaLayoutsLayoutItem'
    }


    def __init__(self, section_detail_type='full', section_items=None, *args, **kwargs):  # noqa: E501
        """GrantaServerApiSchemaLayoutsFullLayoutSection - a model defined in Swagger"""  # noqa: E501
        GrantaServerApiSchemaLayoutsLayoutSection.__init__(self, *args, **kwargs)
        self._section_detail_type = None
        self._section_items = None
        self.discriminator = None
        self.section_detail_type = section_detail_type
        if section_items is not None:
            self.section_items = section_items

    @property
    def section_detail_type(self):
        """Gets the section_detail_type of this GrantaServerApiSchemaLayoutsFullLayoutSection.  # noqa: E501

        :return: The section_detail_type of this GrantaServerApiSchemaLayoutsFullLayoutSection.  # noqa: E501
        :rtype: str
        """
        return self._section_detail_type

    @section_detail_type.setter
    def section_detail_type(self, section_detail_type):
        """Sets the section_detail_type of this GrantaServerApiSchemaLayoutsFullLayoutSection.

        :param section_detail_type: The section_detail_type of this GrantaServerApiSchemaLayoutsFullLayoutSection.  # noqa: E501
        :type: str
        """
        if section_detail_type is None:
            raise ValueError("Invalid value for `section_detail_type`, must not be `None`")  # noqa: E501
        self._section_detail_type = section_detail_type

    @property
    def section_items(self):
        """Gets the section_items of this GrantaServerApiSchemaLayoutsFullLayoutSection.  # noqa: E501

        :return: The section_items of this GrantaServerApiSchemaLayoutsFullLayoutSection.  # noqa: E501
        :rtype: list[GrantaServerApiSchemaLayoutsLayoutItem]
        """
        return self._section_items

    @section_items.setter
    def section_items(self, section_items):
        """Sets the section_items of this GrantaServerApiSchemaLayoutsFullLayoutSection.

        :param section_items: The section_items of this GrantaServerApiSchemaLayoutsFullLayoutSection.  # noqa: E501
        :type: list[GrantaServerApiSchemaLayoutsLayoutItem]
        """
        self._section_items = section_items


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
        if issubclass(GrantaServerApiSchemaLayoutsFullLayoutSection, dict):
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
        if not isinstance(other, GrantaServerApiSchemaLayoutsFullLayoutSection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
