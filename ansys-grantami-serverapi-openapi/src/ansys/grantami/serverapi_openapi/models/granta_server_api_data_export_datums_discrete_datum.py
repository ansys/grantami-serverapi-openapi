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

from ansys.grantami.serverapi_openapi.models.granta_server_api_data_export_datums_applicable_datum import GrantaServerApiDataExportDatumsApplicableDatum  # noqa: F401,E501

class GrantaServerApiDataExportDatumsDiscreteDatum(GrantaServerApiDataExportDatumsApplicableDatum):
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
        'datum_type': 'str',
        'datum_value': 'list[GrantaServerApiDiscreteValue]'
    }
    if hasattr(GrantaServerApiDataExportDatumsApplicableDatum, "swagger_types"):
        swagger_types.update(GrantaServerApiDataExportDatumsApplicableDatum.swagger_types)

    attribute_map = {
        'datum_type': 'datumType',
        'datum_value': 'datumValue'
    }
    if hasattr(GrantaServerApiDataExportDatumsApplicableDatum, "attribute_map"):
        attribute_map.update(GrantaServerApiDataExportDatumsApplicableDatum.attribute_map)

    subtype_mapping = {
        'datumValue': 'GrantaServerApiDiscreteValue'
    }


    def __init__(self, datum_type='discrete', datum_value=None, *args, **kwargs):  # noqa: E501
        """GrantaServerApiDataExportDatumsDiscreteDatum - a model defined in Swagger"""  # noqa: E501
        GrantaServerApiDataExportDatumsApplicableDatum.__init__(self, *args, **kwargs)
        self._datum_type = None
        self._datum_value = None
        self.discriminator = None
        self.datum_type = datum_type
        if datum_value is not None:
            self.datum_value = datum_value

    @property
    def datum_type(self):
        """Gets the datum_type of this GrantaServerApiDataExportDatumsDiscreteDatum.  # noqa: E501

        :return: The datum_type of this GrantaServerApiDataExportDatumsDiscreteDatum.  # noqa: E501
        :rtype: str
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type):
        """Sets the datum_type of this GrantaServerApiDataExportDatumsDiscreteDatum.

        :param datum_type: The datum_type of this GrantaServerApiDataExportDatumsDiscreteDatum.  # noqa: E501
        :type: str
        """
        if datum_type is None:
            raise ValueError("Invalid value for `datum_type`, must not be `None`")  # noqa: E501
        self._datum_type = datum_type

    @property
    def datum_value(self):
        """Gets the datum_value of this GrantaServerApiDataExportDatumsDiscreteDatum.  # noqa: E501

        :return: The datum_value of this GrantaServerApiDataExportDatumsDiscreteDatum.  # noqa: E501
        :rtype: list[GrantaServerApiDiscreteValue]
        """
        return self._datum_value

    @datum_value.setter
    def datum_value(self, datum_value):
        """Sets the datum_value of this GrantaServerApiDataExportDatumsDiscreteDatum.

        :param datum_value: The datum_value of this GrantaServerApiDataExportDatumsDiscreteDatum.  # noqa: E501
        :type: list[GrantaServerApiDiscreteValue]
        """
        self._datum_value = datum_value

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
        if issubclass(GrantaServerApiDataExportDatumsDiscreteDatum, dict):
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
        if not isinstance(other, GrantaServerApiDataExportDatumsDiscreteDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
