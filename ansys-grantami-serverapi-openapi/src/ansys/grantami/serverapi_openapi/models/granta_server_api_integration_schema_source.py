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


class GrantaServerApiIntegrationSchemaSource(ModelBase):
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
        'database': 'GrantaServerApiObjectIdentifier',
        'database_key': 'str',
        'table': 'GrantaServerApiObjectIdentifier',
        'mappings': 'list[GrantaServerApiIntegrationSchemaMapping]'
    }

    attribute_map = {
        'database': 'database',
        'database_key': 'databaseKey',
        'table': 'table',
        'mappings': 'mappings'
    }

    subtype_mapping = {
        'database': 'GrantaServerApiObjectIdentifier',
        'table': 'GrantaServerApiObjectIdentifier',
        'mappings': 'GrantaServerApiIntegrationSchemaMapping'
    }


    def __init__(self, database=None, database_key=None, table=None, mappings=None):  # noqa: E501
        """GrantaServerApiIntegrationSchemaSource - a model defined in Swagger"""  # noqa: E501
        self._database = None
        self._database_key = None
        self._table = None
        self._mappings = None
        self.discriminator = None
        if database is not None:
            self.database = database
        if database_key is not None:
            self.database_key = database_key
        if table is not None:
            self.table = table
        if mappings is not None:
            self.mappings = mappings

    @property
    def database(self):
        """Gets the database of this GrantaServerApiIntegrationSchemaSource.  # noqa: E501

        :return: The database of this GrantaServerApiIntegrationSchemaSource.  # noqa: E501
        :rtype: GrantaServerApiObjectIdentifier
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this GrantaServerApiIntegrationSchemaSource.

        :param database: The database of this GrantaServerApiIntegrationSchemaSource.  # noqa: E501
        :type: GrantaServerApiObjectIdentifier
        """
        self._database = database

    @property
    def database_key(self):
        """Gets the database_key of this GrantaServerApiIntegrationSchemaSource.  # noqa: E501

        :return: The database_key of this GrantaServerApiIntegrationSchemaSource.  # noqa: E501
        :rtype: str
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key):
        """Sets the database_key of this GrantaServerApiIntegrationSchemaSource.

        :param database_key: The database_key of this GrantaServerApiIntegrationSchemaSource.  # noqa: E501
        :type: str
        """
        self._database_key = database_key

    @property
    def table(self):
        """Gets the table of this GrantaServerApiIntegrationSchemaSource.  # noqa: E501

        :return: The table of this GrantaServerApiIntegrationSchemaSource.  # noqa: E501
        :rtype: GrantaServerApiObjectIdentifier
        """
        return self._table

    @table.setter
    def table(self, table):
        """Sets the table of this GrantaServerApiIntegrationSchemaSource.

        :param table: The table of this GrantaServerApiIntegrationSchemaSource.  # noqa: E501
        :type: GrantaServerApiObjectIdentifier
        """
        self._table = table

    @property
    def mappings(self):
        """Gets the mappings of this GrantaServerApiIntegrationSchemaSource.  # noqa: E501
        Mappings for items from this table to the integration schema attributes.  # noqa: E501

        :return: The mappings of this GrantaServerApiIntegrationSchemaSource.  # noqa: E501
        :rtype: list[GrantaServerApiIntegrationSchemaMapping]
        """
        return self._mappings

    @mappings.setter
    def mappings(self, mappings):
        """Sets the mappings of this GrantaServerApiIntegrationSchemaSource.
        Mappings for items from this table to the integration schema attributes.  # noqa: E501

        :param mappings: The mappings of this GrantaServerApiIntegrationSchemaSource.  # noqa: E501
        :type: list[GrantaServerApiIntegrationSchemaMapping]
        """
        self._mappings = mappings


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
        if issubclass(GrantaServerApiIntegrationSchemaSource, dict):
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
        if not isinstance(other, GrantaServerApiIntegrationSchemaSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
