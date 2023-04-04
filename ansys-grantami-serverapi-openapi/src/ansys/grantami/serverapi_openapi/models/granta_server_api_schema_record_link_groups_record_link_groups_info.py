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


class GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroupsInfo(ModelBase):
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
        'record_link_groups': 'list[GrantaServerApiSchemaSlimEntitiesSlimRecordLinkGroup]'
    }

    attribute_map = {
        'record_link_groups': 'recordLinkGroups'
    }

    subtype_mapping = {
        'recordLinkGroups': 'GrantaServerApiSchemaSlimEntitiesSlimRecordLinkGroup'
    }


    def __init__(self, record_link_groups=None):  # noqa: E501
        """GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroupsInfo - a model defined in Swagger"""  # noqa: E501
        self._record_link_groups = None
        self.discriminator = None
        if record_link_groups is not None:
            self.record_link_groups = record_link_groups

    @property
    def record_link_groups(self):
        """Gets the record_link_groups of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroupsInfo.  # noqa: E501

        :return: The record_link_groups of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroupsInfo.  # noqa: E501
        :rtype: list[GrantaServerApiSchemaSlimEntitiesSlimRecordLinkGroup]
        """
        return self._record_link_groups

    @record_link_groups.setter
    def record_link_groups(self, record_link_groups):
        """Sets the record_link_groups of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroupsInfo.

        :param record_link_groups: The record_link_groups of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroupsInfo.  # noqa: E501
        :type: list[GrantaServerApiSchemaSlimEntitiesSlimRecordLinkGroup]
        """
        self._record_link_groups = record_link_groups

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
        if issubclass(GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroupsInfo, dict):
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
        if not isinstance(other, GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroupsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other