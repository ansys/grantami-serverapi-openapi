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

class GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute(GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute):
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
        'display_full_table': 'bool',
        'display_summary_row_inline': 'bool',
        'hide_unlinked_rows': 'bool',
        'tabular_columns': 'list[GrantaServerApiSchemaTabularColumnsTabularColumn]'
    }
    if hasattr(GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute, "swagger_types"):
        swagger_types.update(GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.swagger_types)

    attribute_map = {
        'type': 'type',
        'display_full_table': 'displayFullTable',
        'display_summary_row_inline': 'displaySummaryRowInline',
        'hide_unlinked_rows': 'hideUnlinkedRows',
        'tabular_columns': 'tabularColumns'
    }
    if hasattr(GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute, "attribute_map"):
        attribute_map.update(GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.attribute_map)

    subtype_mapping = {
        'tabularColumns': 'GrantaServerApiSchemaTabularColumnsTabularColumn'
    }


    def __init__(self, type='link', display_full_table=None, display_summary_row_inline=None, hide_unlinked_rows=None, tabular_columns=None, *args, **kwargs):  # noqa: E501
        """GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute - a model defined in Swagger"""  # noqa: E501
        GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.__init__(self, *args, **kwargs)
        self._type = None
        self._display_full_table = None
        self._display_summary_row_inline = None
        self._hide_unlinked_rows = None
        self._tabular_columns = None
        self.discriminator = None
        self.type = type
        if display_full_table is not None:
            self.display_full_table = display_full_table
        if display_summary_row_inline is not None:
            self.display_summary_row_inline = display_summary_row_inline
        if hide_unlinked_rows is not None:
            self.hide_unlinked_rows = hide_unlinked_rows
        if tabular_columns is not None:
            self.tabular_columns = tabular_columns

    @property
    def type(self):
        """Gets the type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.  # noqa: E501

        :return: The type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.

        :param type: The type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type

    @property
    def display_full_table(self):
        """Gets the display_full_table of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.  # noqa: E501

        :return: The display_full_table of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._display_full_table

    @display_full_table.setter
    def display_full_table(self, display_full_table):
        """Sets the display_full_table of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.

        :param display_full_table: The display_full_table of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.  # noqa: E501
        :type: bool
        """
        self._display_full_table = display_full_table

    @property
    def display_summary_row_inline(self):
        """Gets the display_summary_row_inline of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.  # noqa: E501

        :return: The display_summary_row_inline of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._display_summary_row_inline

    @display_summary_row_inline.setter
    def display_summary_row_inline(self, display_summary_row_inline):
        """Sets the display_summary_row_inline of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.

        :param display_summary_row_inline: The display_summary_row_inline of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.  # noqa: E501
        :type: bool
        """
        self._display_summary_row_inline = display_summary_row_inline

    @property
    def hide_unlinked_rows(self):
        """Gets the hide_unlinked_rows of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.  # noqa: E501

        :return: The hide_unlinked_rows of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._hide_unlinked_rows

    @hide_unlinked_rows.setter
    def hide_unlinked_rows(self, hide_unlinked_rows):
        """Sets the hide_unlinked_rows of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.

        :param hide_unlinked_rows: The hide_unlinked_rows of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.  # noqa: E501
        :type: bool
        """
        self._hide_unlinked_rows = hide_unlinked_rows

    @property
    def tabular_columns(self):
        """Gets the tabular_columns of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.  # noqa: E501

        :return: The tabular_columns of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.  # noqa: E501
        :rtype: list[GrantaServerApiSchemaTabularColumnsTabularColumn]
        """
        return self._tabular_columns

    @tabular_columns.setter
    def tabular_columns(self, tabular_columns):
        """Sets the tabular_columns of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.

        :param tabular_columns: The tabular_columns of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.  # noqa: E501
        :type: list[GrantaServerApiSchemaTabularColumnsTabularColumn]
        """
        self._tabular_columns = tabular_columns

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
        if issubclass(GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute, dict):
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
        if not isinstance(other, GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
