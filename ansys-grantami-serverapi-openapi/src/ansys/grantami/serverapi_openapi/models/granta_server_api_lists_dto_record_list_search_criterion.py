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

from ansys.grantami.serverapi_openapi.models.granta_server_api_lists_dto_list_criterion import GrantaServerApiListsDtoListCriterion  # noqa: F401,E501

class GrantaServerApiListsDtoRecordListSearchCriterion(GrantaServerApiListsDtoListCriterion):
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
        'name_contains': 'str',
        'user_role': 'GrantaServerApiListsDtoUserRole',
        'is_published': 'bool',
        'is_awaiting_approval': 'bool',
        'is_internal_use': 'bool',
        'is_revision': 'bool',
        'contains_records_in_databases': 'list[str]',
        'contains_records_in_integration_schemas': 'list[str]',
        'contains_records_in_tables': 'list[str]',
        'contains_records': 'list[str]',
        'user_can_add_or_remove_items': 'bool',
        'type': 'str'
    }
    if hasattr(GrantaServerApiListsDtoListCriterion, "swagger_types"):
        swagger_types.update(GrantaServerApiListsDtoListCriterion.swagger_types)

    attribute_map = {
        'name_contains': 'nameContains',
        'user_role': 'userRole',
        'is_published': 'isPublished',
        'is_awaiting_approval': 'isAwaitingApproval',
        'is_internal_use': 'isInternalUse',
        'is_revision': 'isRevision',
        'contains_records_in_databases': 'containsRecordsInDatabases',
        'contains_records_in_integration_schemas': 'containsRecordsInIntegrationSchemas',
        'contains_records_in_tables': 'containsRecordsInTables',
        'contains_records': 'containsRecords',
        'user_can_add_or_remove_items': 'userCanAddOrRemoveItems',
        'type': 'type'
    }
    if hasattr(GrantaServerApiListsDtoListCriterion, "attribute_map"):
        attribute_map.update(GrantaServerApiListsDtoListCriterion.attribute_map)

    subtype_mapping = {
        'userRole': 'GrantaServerApiListsDtoUserRole',
    }


    def __init__(self, name_contains=None, user_role=None, is_published=None, is_awaiting_approval=None, is_internal_use=None, is_revision=None, contains_records_in_databases=None, contains_records_in_integration_schemas=None, contains_records_in_tables=None, contains_records=None, user_can_add_or_remove_items=None, type='recordList', *args, **kwargs):  # noqa: E501
        """GrantaServerApiListsDtoRecordListSearchCriterion - a model defined in Swagger"""  # noqa: E501
        GrantaServerApiListsDtoListCriterion.__init__(self, *args, **kwargs)
        self._name_contains = None
        self._user_role = None
        self._is_published = None
        self._is_awaiting_approval = None
        self._is_internal_use = None
        self._is_revision = None
        self._contains_records_in_databases = None
        self._contains_records_in_integration_schemas = None
        self._contains_records_in_tables = None
        self._contains_records = None
        self._user_can_add_or_remove_items = None
        self._type = None
        self.discriminator = None
        if name_contains is not None:
            self.name_contains = name_contains
        if user_role is not None:
            self.user_role = user_role
        if is_published is not None:
            self.is_published = is_published
        if is_awaiting_approval is not None:
            self.is_awaiting_approval = is_awaiting_approval
        if is_internal_use is not None:
            self.is_internal_use = is_internal_use
        if is_revision is not None:
            self.is_revision = is_revision
        if contains_records_in_databases is not None:
            self.contains_records_in_databases = contains_records_in_databases
        if contains_records_in_integration_schemas is not None:
            self.contains_records_in_integration_schemas = contains_records_in_integration_schemas
        if contains_records_in_tables is not None:
            self.contains_records_in_tables = contains_records_in_tables
        if contains_records is not None:
            self.contains_records = contains_records
        if user_can_add_or_remove_items is not None:
            self.user_can_add_or_remove_items = user_can_add_or_remove_items
        self.type = type

    @property
    def name_contains(self):
        """Gets the name_contains of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501

        :return: The name_contains of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        :rtype: str
        """
        return self._name_contains

    @name_contains.setter
    def name_contains(self, name_contains):
        """Sets the name_contains of this GrantaServerApiListsDtoRecordListSearchCriterion.

        :param name_contains: The name_contains of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        :type: str
        """
        self._name_contains = name_contains

    @property
    def user_role(self):
        """Gets the user_role of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501

        :return: The user_role of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        :rtype: GrantaServerApiListsDtoUserRole
        """
        return self._user_role

    @user_role.setter
    def user_role(self, user_role):
        """Sets the user_role of this GrantaServerApiListsDtoRecordListSearchCriterion.

        :param user_role: The user_role of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        :type: GrantaServerApiListsDtoUserRole
        """
        self._user_role = user_role

    @property
    def is_published(self):
        """Gets the is_published of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501

        :return: The is_published of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        :rtype: bool
        """
        return self._is_published

    @is_published.setter
    def is_published(self, is_published):
        """Sets the is_published of this GrantaServerApiListsDtoRecordListSearchCriterion.

        :param is_published: The is_published of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        :type: bool
        """
        self._is_published = is_published

    @property
    def is_awaiting_approval(self):
        """Gets the is_awaiting_approval of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501

        :return: The is_awaiting_approval of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        :rtype: bool
        """
        return self._is_awaiting_approval

    @is_awaiting_approval.setter
    def is_awaiting_approval(self, is_awaiting_approval):
        """Sets the is_awaiting_approval of this GrantaServerApiListsDtoRecordListSearchCriterion.

        :param is_awaiting_approval: The is_awaiting_approval of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        :type: bool
        """
        self._is_awaiting_approval = is_awaiting_approval

    @property
    def is_internal_use(self):
        """Gets the is_internal_use of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501

        :return: The is_internal_use of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        :rtype: bool
        """
        return self._is_internal_use

    @is_internal_use.setter
    def is_internal_use(self, is_internal_use):
        """Sets the is_internal_use of this GrantaServerApiListsDtoRecordListSearchCriterion.

        :param is_internal_use: The is_internal_use of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        :type: bool
        """
        self._is_internal_use = is_internal_use

    @property
    def is_revision(self):
        """Gets the is_revision of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        Restrict to record lists that are (non discarded) revisions.  # noqa: E501

        :return: The is_revision of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        :rtype: bool
        """
        return self._is_revision

    @is_revision.setter
    def is_revision(self, is_revision):
        """Sets the is_revision of this GrantaServerApiListsDtoRecordListSearchCriterion.
        Restrict to record lists that are (non discarded) revisions.  # noqa: E501

        :param is_revision: The is_revision of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        :type: bool
        """
        self._is_revision = is_revision

    @property
    def contains_records_in_databases(self):
        """Gets the contains_records_in_databases of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        Limits results to lists containing records in any of of the specified databases  # noqa: E501

        :return: The contains_records_in_databases of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        :rtype: list[str]
        """
        return self._contains_records_in_databases

    @contains_records_in_databases.setter
    def contains_records_in_databases(self, contains_records_in_databases):
        """Sets the contains_records_in_databases of this GrantaServerApiListsDtoRecordListSearchCriterion.
        Limits results to lists containing records in any of of the specified databases  # noqa: E501

        :param contains_records_in_databases: The contains_records_in_databases of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        :type: list[str]
        """
        self._contains_records_in_databases = contains_records_in_databases

    @property
    def contains_records_in_integration_schemas(self):
        """Gets the contains_records_in_integration_schemas of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        Limits results to lists containing records in any of the specified integration schemas  # noqa: E501

        :return: The contains_records_in_integration_schemas of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        :rtype: list[str]
        """
        return self._contains_records_in_integration_schemas

    @contains_records_in_integration_schemas.setter
    def contains_records_in_integration_schemas(self, contains_records_in_integration_schemas):
        """Sets the contains_records_in_integration_schemas of this GrantaServerApiListsDtoRecordListSearchCriterion.
        Limits results to lists containing records in any of the specified integration schemas  # noqa: E501

        :param contains_records_in_integration_schemas: The contains_records_in_integration_schemas of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        :type: list[str]
        """
        self._contains_records_in_integration_schemas = contains_records_in_integration_schemas

    @property
    def contains_records_in_tables(self):
        """Gets the contains_records_in_tables of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        Limits results to lists containing records in any of the specified tables  # noqa: E501

        :return: The contains_records_in_tables of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        :rtype: list[str]
        """
        return self._contains_records_in_tables

    @contains_records_in_tables.setter
    def contains_records_in_tables(self, contains_records_in_tables):
        """Sets the contains_records_in_tables of this GrantaServerApiListsDtoRecordListSearchCriterion.
        Limits results to lists containing records in any of the specified tables  # noqa: E501

        :param contains_records_in_tables: The contains_records_in_tables of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        :type: list[str]
        """
        self._contains_records_in_tables = contains_records_in_tables

    @property
    def contains_records(self):
        """Gets the contains_records of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        Limits results to lists containing any of the given records  # noqa: E501

        :return: The contains_records of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        :rtype: list[str]
        """
        return self._contains_records

    @contains_records.setter
    def contains_records(self, contains_records):
        """Sets the contains_records of this GrantaServerApiListsDtoRecordListSearchCriterion.
        Limits results to lists containing any of the given records  # noqa: E501

        :param contains_records: The contains_records of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        :type: list[str]
        """
        self._contains_records = contains_records

    @property
    def user_can_add_or_remove_items(self):
        """Gets the user_can_add_or_remove_items of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        Limits results to lists where the current user can add or remove items.  # noqa: E501

        :return: The user_can_add_or_remove_items of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        :rtype: bool
        """
        return self._user_can_add_or_remove_items

    @user_can_add_or_remove_items.setter
    def user_can_add_or_remove_items(self, user_can_add_or_remove_items):
        """Sets the user_can_add_or_remove_items of this GrantaServerApiListsDtoRecordListSearchCriterion.
        Limits results to lists where the current user can add or remove items.  # noqa: E501

        :param user_can_add_or_remove_items: The user_can_add_or_remove_items of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        :type: bool
        """
        self._user_can_add_or_remove_items = user_can_add_or_remove_items

    @property
    def type(self):
        """Gets the type of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501

        :return: The type of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GrantaServerApiListsDtoRecordListSearchCriterion.

        :param type: The type of this GrantaServerApiListsDtoRecordListSearchCriterion.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type


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
        if issubclass(GrantaServerApiListsDtoRecordListSearchCriterion, dict):
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
        if not isinstance(other, GrantaServerApiListsDtoRecordListSearchCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
