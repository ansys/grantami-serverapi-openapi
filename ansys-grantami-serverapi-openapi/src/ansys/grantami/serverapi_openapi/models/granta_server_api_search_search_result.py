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


class GrantaServerApiSearchSearchResult(ModelBase):
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
        'record_history_identity': 'int',
        'record_identity': 'int',
        'record_history_guid': 'str',
        'record_guid': 'str',
        'record_name': 'str',
        'record_color': 'str',
        'table_identity': 'int',
        'cubic_spline_status': 'str',
        'version_control_state': 'str',
        'version_number': 'int',
        'parent_identity': 'int',
        'type': 'GrantaServerApiRecordType',
        'score': 'float',
        'sorting_value': 'GrantaServerApiSearchSortingValue'
    }

    attribute_map = {
        'database_key': 'databaseKey',
        'record_history_identity': 'recordHistoryIdentity',
        'record_identity': 'recordIdentity',
        'record_history_guid': 'recordHistoryGuid',
        'record_guid': 'recordGuid',
        'record_name': 'recordName',
        'record_color': 'recordColor',
        'table_identity': 'tableIdentity',
        'cubic_spline_status': 'cubicSplineStatus',
        'version_control_state': 'versionControlState',
        'version_number': 'versionNumber',
        'parent_identity': 'parentIdentity',
        'type': 'type',
        'score': 'score',
        'sorting_value': 'sortingValue'
    }

    subtype_mapping = {
        'type': 'GrantaServerApiRecordType',
        'sortingValue': 'GrantaServerApiSearchSortingValue'
    }


    def __init__(self, database_key=None, record_history_identity=None, record_identity=None, record_history_guid=None, record_guid=None, record_name=None, record_color=None, table_identity=None, cubic_spline_status=None, version_control_state=None, version_number=None, parent_identity=None, type=None, score=None, sorting_value=None):  # noqa: E501
        """GrantaServerApiSearchSearchResult - a model defined in Swagger"""  # noqa: E501
        self._database_key = None
        self._record_history_identity = None
        self._record_identity = None
        self._record_history_guid = None
        self._record_guid = None
        self._record_name = None
        self._record_color = None
        self._table_identity = None
        self._cubic_spline_status = None
        self._version_control_state = None
        self._version_number = None
        self._parent_identity = None
        self._type = None
        self._score = None
        self._sorting_value = None
        self.discriminator = None
        if database_key is not None:
            self.database_key = database_key
        if record_history_identity is not None:
            self.record_history_identity = record_history_identity
        if record_identity is not None:
            self.record_identity = record_identity
        if record_history_guid is not None:
            self.record_history_guid = record_history_guid
        if record_guid is not None:
            self.record_guid = record_guid
        if record_name is not None:
            self.record_name = record_name
        if record_color is not None:
            self.record_color = record_color
        if table_identity is not None:
            self.table_identity = table_identity
        if cubic_spline_status is not None:
            self.cubic_spline_status = cubic_spline_status
        if version_control_state is not None:
            self.version_control_state = version_control_state
        if version_number is not None:
            self.version_number = version_number
        if parent_identity is not None:
            self.parent_identity = parent_identity
        if type is not None:
            self.type = type
        if score is not None:
            self.score = score
        if sorting_value is not None:
            self.sorting_value = sorting_value

    @property
    def database_key(self):
        """Gets the database_key of this GrantaServerApiSearchSearchResult.  # noqa: E501

        :return: The database_key of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key):
        """Sets the database_key of this GrantaServerApiSearchSearchResult.

        :param database_key: The database_key of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :type: str
        """
        self._database_key = database_key

    @property
    def record_history_identity(self):
        """Gets the record_history_identity of this GrantaServerApiSearchSearchResult.  # noqa: E501

        :return: The record_history_identity of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._record_history_identity

    @record_history_identity.setter
    def record_history_identity(self, record_history_identity):
        """Sets the record_history_identity of this GrantaServerApiSearchSearchResult.

        :param record_history_identity: The record_history_identity of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :type: int
        """
        self._record_history_identity = record_history_identity

    @property
    def record_identity(self):
        """Gets the record_identity of this GrantaServerApiSearchSearchResult.  # noqa: E501

        :return: The record_identity of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._record_identity

    @record_identity.setter
    def record_identity(self, record_identity):
        """Sets the record_identity of this GrantaServerApiSearchSearchResult.

        :param record_identity: The record_identity of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :type: int
        """
        self._record_identity = record_identity

    @property
    def record_history_guid(self):
        """Gets the record_history_guid of this GrantaServerApiSearchSearchResult.  # noqa: E501

        :return: The record_history_guid of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._record_history_guid

    @record_history_guid.setter
    def record_history_guid(self, record_history_guid):
        """Sets the record_history_guid of this GrantaServerApiSearchSearchResult.

        :param record_history_guid: The record_history_guid of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :type: str
        """
        self._record_history_guid = record_history_guid

    @property
    def record_guid(self):
        """Gets the record_guid of this GrantaServerApiSearchSearchResult.  # noqa: E501

        :return: The record_guid of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._record_guid

    @record_guid.setter
    def record_guid(self, record_guid):
        """Sets the record_guid of this GrantaServerApiSearchSearchResult.

        :param record_guid: The record_guid of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :type: str
        """
        self._record_guid = record_guid

    @property
    def record_name(self):
        """Gets the record_name of this GrantaServerApiSearchSearchResult.  # noqa: E501

        :return: The record_name of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._record_name

    @record_name.setter
    def record_name(self, record_name):
        """Sets the record_name of this GrantaServerApiSearchSearchResult.

        :param record_name: The record_name of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :type: str
        """
        self._record_name = record_name

    @property
    def record_color(self):
        """Gets the record_color of this GrantaServerApiSearchSearchResult.  # noqa: E501

        :return: The record_color of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._record_color

    @record_color.setter
    def record_color(self, record_color):
        """Sets the record_color of this GrantaServerApiSearchSearchResult.

        :param record_color: The record_color of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :type: str
        """
        self._record_color = record_color

    @property
    def table_identity(self):
        """Gets the table_identity of this GrantaServerApiSearchSearchResult.  # noqa: E501

        :return: The table_identity of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._table_identity

    @table_identity.setter
    def table_identity(self, table_identity):
        """Sets the table_identity of this GrantaServerApiSearchSearchResult.

        :param table_identity: The table_identity of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :type: int
        """
        self._table_identity = table_identity

    @property
    def cubic_spline_status(self):
        """Gets the cubic_spline_status of this GrantaServerApiSearchSearchResult.  # noqa: E501

        :return: The cubic_spline_status of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._cubic_spline_status

    @cubic_spline_status.setter
    def cubic_spline_status(self, cubic_spline_status):
        """Sets the cubic_spline_status of this GrantaServerApiSearchSearchResult.

        :param cubic_spline_status: The cubic_spline_status of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :type: str
        """
        self._cubic_spline_status = cubic_spline_status

    @property
    def version_control_state(self):
        """Gets the version_control_state of this GrantaServerApiSearchSearchResult.  # noqa: E501

        :return: The version_control_state of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._version_control_state

    @version_control_state.setter
    def version_control_state(self, version_control_state):
        """Sets the version_control_state of this GrantaServerApiSearchSearchResult.

        :param version_control_state: The version_control_state of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :type: str
        """
        self._version_control_state = version_control_state

    @property
    def version_number(self):
        """Gets the version_number of this GrantaServerApiSearchSearchResult.  # noqa: E501

        :return: The version_number of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """Sets the version_number of this GrantaServerApiSearchSearchResult.

        :param version_number: The version_number of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :type: int
        """
        self._version_number = version_number

    @property
    def parent_identity(self):
        """Gets the parent_identity of this GrantaServerApiSearchSearchResult.  # noqa: E501

        :return: The parent_identity of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._parent_identity

    @parent_identity.setter
    def parent_identity(self, parent_identity):
        """Sets the parent_identity of this GrantaServerApiSearchSearchResult.

        :param parent_identity: The parent_identity of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :type: int
        """
        self._parent_identity = parent_identity

    @property
    def type(self):
        """Gets the type of this GrantaServerApiSearchSearchResult.  # noqa: E501

        :return: The type of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :rtype: GrantaServerApiRecordType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GrantaServerApiSearchSearchResult.

        :param type: The type of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :type: GrantaServerApiRecordType
        """
        self._type = type

    @property
    def score(self):
        """Gets the score of this GrantaServerApiSearchSearchResult.  # noqa: E501

        :return: The score of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this GrantaServerApiSearchSearchResult.

        :param score: The score of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :type: float
        """
        self._score = score

    @property
    def sorting_value(self):
        """Gets the sorting_value of this GrantaServerApiSearchSearchResult.  # noqa: E501

        :return: The sorting_value of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :rtype: GrantaServerApiSearchSortingValue
        """
        return self._sorting_value

    @sorting_value.setter
    def sorting_value(self, sorting_value):
        """Sets the sorting_value of this GrantaServerApiSearchSearchResult.

        :param sorting_value: The sorting_value of this GrantaServerApiSearchSearchResult.  # noqa: E501
        :type: GrantaServerApiSearchSortingValue
        """
        self._sorting_value = sorting_value

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
        if issubclass(GrantaServerApiSearchSearchResult, dict):
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
        if not isinstance(other, GrantaServerApiSearchSearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
