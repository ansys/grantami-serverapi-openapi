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

from ansys.grantami.serverapi_openapi.models.granta_server_api_data_export_datums_float_functional_datum import GrantaServerApiDataExportDatumsFloatFunctionalDatum  # noqa: F401,E501

class GrantaServerApiDataExportDatumsFunctionalSeriesDatum(GrantaServerApiDataExportDatumsFloatFunctionalDatum):
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
        'graph_type': 'str',
        'series': 'list[GrantaServerApiDataExportDatumsSeries]',
        'is_logarithmic': 'bool',
        'is_range': 'bool',
        'show_as_table': 'bool'
    }
    if hasattr(GrantaServerApiDataExportDatumsFloatFunctionalDatum, "swagger_types"):
        swagger_types.update(GrantaServerApiDataExportDatumsFloatFunctionalDatum.swagger_types)

    attribute_map = {
        'graph_type': 'graphType',
        'series': 'series',
        'is_logarithmic': 'isLogarithmic',
        'is_range': 'isRange',
        'show_as_table': 'showAsTable'
    }
    if hasattr(GrantaServerApiDataExportDatumsFloatFunctionalDatum, "attribute_map"):
        attribute_map.update(GrantaServerApiDataExportDatumsFloatFunctionalDatum.attribute_map)

    subtype_mapping = {
        'series': 'GrantaServerApiDataExportDatumsSeries',
    }


    def __init__(self, graph_type='series', series=None, is_logarithmic=None, is_range=None, show_as_table=None, *args, **kwargs):  # noqa: E501
        """GrantaServerApiDataExportDatumsFunctionalSeriesDatum - a model defined in Swagger"""  # noqa: E501
        GrantaServerApiDataExportDatumsFloatFunctionalDatum.__init__(self, *args, **kwargs)
        self._graph_type = None
        self._series = None
        self._is_logarithmic = None
        self._is_range = None
        self._show_as_table = None
        self.discriminator = None
        self.graph_type = graph_type
        if series is not None:
            self.series = series
        if is_logarithmic is not None:
            self.is_logarithmic = is_logarithmic
        if is_range is not None:
            self.is_range = is_range
        if show_as_table is not None:
            self.show_as_table = show_as_table

    @property
    def graph_type(self):
        """Gets the graph_type of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.  # noqa: E501

        :return: The graph_type of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.  # noqa: E501
        :rtype: str
        """
        return self._graph_type

    @graph_type.setter
    def graph_type(self, graph_type):
        """Sets the graph_type of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.

        :param graph_type: The graph_type of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.  # noqa: E501
        :type: str
        """
        if graph_type is None:
            raise ValueError("Invalid value for `graph_type`, must not be `None`")  # noqa: E501
        self._graph_type = graph_type

    @property
    def series(self):
        """Gets the series of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.  # noqa: E501

        :return: The series of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.  # noqa: E501
        :rtype: list[GrantaServerApiDataExportDatumsSeries]
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.

        :param series: The series of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.  # noqa: E501
        :type: list[GrantaServerApiDataExportDatumsSeries]
        """
        self._series = series

    @property
    def is_logarithmic(self):
        """Gets the is_logarithmic of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.  # noqa: E501

        :return: The is_logarithmic of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.  # noqa: E501
        :rtype: bool
        """
        return self._is_logarithmic

    @is_logarithmic.setter
    def is_logarithmic(self, is_logarithmic):
        """Sets the is_logarithmic of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.

        :param is_logarithmic: The is_logarithmic of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.  # noqa: E501
        :type: bool
        """
        self._is_logarithmic = is_logarithmic

    @property
    def is_range(self):
        """Gets the is_range of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.  # noqa: E501

        :return: The is_range of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.  # noqa: E501
        :rtype: bool
        """
        return self._is_range

    @is_range.setter
    def is_range(self, is_range):
        """Sets the is_range of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.

        :param is_range: The is_range of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.  # noqa: E501
        :type: bool
        """
        self._is_range = is_range

    @property
    def show_as_table(self):
        """Gets the show_as_table of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.  # noqa: E501

        :return: The show_as_table of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.  # noqa: E501
        :rtype: bool
        """
        return self._show_as_table

    @show_as_table.setter
    def show_as_table(self, show_as_table):
        """Sets the show_as_table of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.

        :param show_as_table: The show_as_table of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.  # noqa: E501
        :type: bool
        """
        self._show_as_table = show_as_table

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
        if issubclass(GrantaServerApiDataExportDatumsFunctionalSeriesDatum, dict):
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
        if not isinstance(other, GrantaServerApiDataExportDatumsFunctionalSeriesDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
