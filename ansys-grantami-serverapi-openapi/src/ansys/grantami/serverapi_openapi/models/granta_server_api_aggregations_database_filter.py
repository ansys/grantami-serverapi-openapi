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


class GrantaServerApiAggregationsDatabaseFilter(ModelBase):
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
        'database_key': 'str',
        'tables': 'list[GrantaServerApiAggregationsTableFilter]'
    }

    attribute_map = {
        'database_key': 'databaseKey',
        'tables': 'tables'
    }

    subtype_mapping = {
        'tables': 'GrantaServerApiAggregationsTableFilter'
    }


    def __init__(self, database_key=None, tables=None):  # noqa: E501
        """GrantaServerApiAggregationsDatabaseFilter - a model defined in Swagger"""  # noqa: E501
        self._database_key = None
        self._tables = None
        self.discriminator = None
        if database_key is not None:
            self.database_key = database_key
        if tables is not None:
            self.tables = tables

    @property
    def database_key(self):
        """Gets the database_key of this GrantaServerApiAggregationsDatabaseFilter.  # noqa: E501

        :return: The database_key of this GrantaServerApiAggregationsDatabaseFilter.  # noqa: E501
        :rtype: str
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key):
        """Sets the database_key of this GrantaServerApiAggregationsDatabaseFilter.

        :param database_key: The database_key of this GrantaServerApiAggregationsDatabaseFilter.  # noqa: E501
        :type: str
        """
        self._database_key = database_key

    @property
    def tables(self):
        """Gets the tables of this GrantaServerApiAggregationsDatabaseFilter.  # noqa: E501
        Results are only returned from the table and attributes specified in the filters.  # noqa: E501

        :return: The tables of this GrantaServerApiAggregationsDatabaseFilter.  # noqa: E501
        :rtype: list[GrantaServerApiAggregationsTableFilter]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        """Sets the tables of this GrantaServerApiAggregationsDatabaseFilter.
        Results are only returned from the table and attributes specified in the filters.  # noqa: E501

        :param tables: The tables of this GrantaServerApiAggregationsDatabaseFilter.  # noqa: E501
        :type: list[GrantaServerApiAggregationsTableFilter]
        """
        self._tables = tables


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
        if issubclass(GrantaServerApiAggregationsDatabaseFilter, dict):
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
        if not isinstance(other, GrantaServerApiAggregationsDatabaseFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
