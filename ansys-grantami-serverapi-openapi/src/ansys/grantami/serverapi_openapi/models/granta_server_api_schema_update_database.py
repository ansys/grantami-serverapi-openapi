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


class GrantaServerApiSchemaUpdateDatabase(ModelBase):
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
        'author': 'str',
        'company': 'str',
        'notes': 'str',
        'currency_code': 'str',
        'version_guid': 'str',
        'name': 'str',
        'guid': 'str'
    }

    attribute_map = {
        'author': 'author',
        'company': 'company',
        'notes': 'notes',
        'currency_code': 'currencyCode',
        'version_guid': 'versionGuid',
        'name': 'name',
        'guid': 'guid'
    }

    subtype_mapping = {
    }


    def __init__(self, author=None, company=None, notes=None, currency_code=None, version_guid=None, name=None, guid=None):  # noqa: E501
        """GrantaServerApiSchemaUpdateDatabase - a model defined in Swagger"""  # noqa: E501
        self._author = None
        self._company = None
        self._notes = None
        self._currency_code = None
        self._version_guid = None
        self._name = None
        self._guid = None
        self.discriminator = None
        if author is not None:
            self.author = author
        if company is not None:
            self.company = company
        if notes is not None:
            self.notes = notes
        if currency_code is not None:
            self.currency_code = currency_code
        if version_guid is not None:
            self.version_guid = version_guid
        if name is not None:
            self.name = name
        if guid is not None:
            self.guid = guid

    @property
    def author(self):
        """Gets the author of this GrantaServerApiSchemaUpdateDatabase.  # noqa: E501

        :return: The author of this GrantaServerApiSchemaUpdateDatabase.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this GrantaServerApiSchemaUpdateDatabase.

        :param author: The author of this GrantaServerApiSchemaUpdateDatabase.  # noqa: E501
        :type: str
        """
        self._author = author

    @property
    def company(self):
        """Gets the company of this GrantaServerApiSchemaUpdateDatabase.  # noqa: E501

        :return: The company of this GrantaServerApiSchemaUpdateDatabase.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this GrantaServerApiSchemaUpdateDatabase.

        :param company: The company of this GrantaServerApiSchemaUpdateDatabase.  # noqa: E501
        :type: str
        """
        self._company = company

    @property
    def notes(self):
        """Gets the notes of this GrantaServerApiSchemaUpdateDatabase.  # noqa: E501

        :return: The notes of this GrantaServerApiSchemaUpdateDatabase.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this GrantaServerApiSchemaUpdateDatabase.

        :param notes: The notes of this GrantaServerApiSchemaUpdateDatabase.  # noqa: E501
        :type: str
        """
        self._notes = notes

    @property
    def currency_code(self):
        """Gets the currency_code of this GrantaServerApiSchemaUpdateDatabase.  # noqa: E501

        :return: The currency_code of this GrantaServerApiSchemaUpdateDatabase.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this GrantaServerApiSchemaUpdateDatabase.

        :param currency_code: The currency_code of this GrantaServerApiSchemaUpdateDatabase.  # noqa: E501
        :type: str
        """
        self._currency_code = currency_code

    @property
    def version_guid(self):
        """Gets the version_guid of this GrantaServerApiSchemaUpdateDatabase.  # noqa: E501

        :return: The version_guid of this GrantaServerApiSchemaUpdateDatabase.  # noqa: E501
        :rtype: str
        """
        return self._version_guid

    @version_guid.setter
    def version_guid(self, version_guid):
        """Sets the version_guid of this GrantaServerApiSchemaUpdateDatabase.

        :param version_guid: The version_guid of this GrantaServerApiSchemaUpdateDatabase.  # noqa: E501
        :type: str
        """
        self._version_guid = version_guid

    @property
    def name(self):
        """Gets the name of this GrantaServerApiSchemaUpdateDatabase.  # noqa: E501

        :return: The name of this GrantaServerApiSchemaUpdateDatabase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GrantaServerApiSchemaUpdateDatabase.

        :param name: The name of this GrantaServerApiSchemaUpdateDatabase.  # noqa: E501
        :type: str
        """
        self._name = name

    @property
    def guid(self):
        """Gets the guid of this GrantaServerApiSchemaUpdateDatabase.  # noqa: E501

        :return: The guid of this GrantaServerApiSchemaUpdateDatabase.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this GrantaServerApiSchemaUpdateDatabase.

        :param guid: The guid of this GrantaServerApiSchemaUpdateDatabase.  # noqa: E501
        :type: str
        """
        self._guid = guid

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
        if issubclass(GrantaServerApiSchemaUpdateDatabase, dict):
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
        if not isinstance(other, GrantaServerApiSchemaUpdateDatabase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other