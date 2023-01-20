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


class GrantaServerApiListsDtoPagingOptions(ModelBase):
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
        'start_index': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'start_index': 'startIndex',
        'page_size': 'pageSize'
    }

    subtype_mapping = {
    }


    def __init__(self, start_index=None, page_size=None):  # noqa: E501
        """GrantaServerApiListsDtoPagingOptions - a model defined in Swagger"""  # noqa: E501
        self._start_index = None
        self._page_size = None
        self.discriminator = None
        if start_index is not None:
            self.start_index = start_index
        if page_size is not None:
            self.page_size = page_size

    @property
    def start_index(self):
        """Gets the start_index of this GrantaServerApiListsDtoPagingOptions.  # noqa: E501
        The index of the first list in the collection to be returned. If not provided it will start at index 0.  # noqa: E501

        :return: The start_index of this GrantaServerApiListsDtoPagingOptions.  # noqa: E501
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        """Sets the start_index of this GrantaServerApiListsDtoPagingOptions.
        The index of the first list in the collection to be returned. If not provided it will start at index 0.  # noqa: E501

        :param start_index: The start_index of this GrantaServerApiListsDtoPagingOptions.  # noqa: E501
        :type: int
        """
        self._start_index = start_index

    @property
    def page_size(self):
        """Gets the page_size of this GrantaServerApiListsDtoPagingOptions.  # noqa: E501
        The number of lists to be returned per page. If not provided the number of returned lists will be unlimited.  # noqa: E501

        :return: The page_size of this GrantaServerApiListsDtoPagingOptions.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this GrantaServerApiListsDtoPagingOptions.
        The number of lists to be returned per page. If not provided the number of returned lists will be unlimited.  # noqa: E501

        :param page_size: The page_size of this GrantaServerApiListsDtoPagingOptions.  # noqa: E501
        :type: int
        """
        self._page_size = page_size


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
        if issubclass(GrantaServerApiListsDtoPagingOptions, dict):
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
        if not isinstance(other, GrantaServerApiListsDtoPagingOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
