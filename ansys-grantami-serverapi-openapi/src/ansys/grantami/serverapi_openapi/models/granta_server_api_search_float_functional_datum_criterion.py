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

from ansys.grantami.serverapi_openapi.models.granta_server_api_search_datum_criterion import GrantaServerApiSearchDatumCriterion  # noqa: F401,E501

class GrantaServerApiSearchFloatFunctionalDatumCriterion(GrantaServerApiSearchDatumCriterion):
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
        'gte': 'float',
        'lte': 'float',
        'unit': 'str',
        'constraints': 'list[GrantaServerApiSearchParameterConstraint]'
    }
    if hasattr(GrantaServerApiSearchDatumCriterion, "swagger_types"):
        swagger_types.update(GrantaServerApiSearchDatumCriterion.swagger_types)

    attribute_map = {
        'type': 'type',
        'gte': 'gte',
        'lte': 'lte',
        'unit': 'unit',
        'constraints': 'constraints'
    }
    if hasattr(GrantaServerApiSearchDatumCriterion, "attribute_map"):
        attribute_map.update(GrantaServerApiSearchDatumCriterion.attribute_map)

    subtype_mapping = {
        'constraints': 'GrantaServerApiSearchParameterConstraint'
    }


    def __init__(self, type='floatFunctional', gte=None, lte=None, unit=None, constraints=None, *args, **kwargs):  # noqa: E501
        """GrantaServerApiSearchFloatFunctionalDatumCriterion - a model defined in Swagger"""  # noqa: E501
        GrantaServerApiSearchDatumCriterion.__init__(self, *args, **kwargs)
        self._type = None
        self._gte = None
        self._lte = None
        self._unit = None
        self._constraints = None
        self.discriminator = None
        self.type = type
        if gte is not None:
            self.gte = gte
        if lte is not None:
            self.lte = lte
        if unit is not None:
            self.unit = unit
        if constraints is not None:
            self.constraints = constraints

    @property
    def type(self):
        """Gets the type of this GrantaServerApiSearchFloatFunctionalDatumCriterion.  # noqa: E501

        :return: The type of this GrantaServerApiSearchFloatFunctionalDatumCriterion.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GrantaServerApiSearchFloatFunctionalDatumCriterion.

        :param type: The type of this GrantaServerApiSearchFloatFunctionalDatumCriterion.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type

    @property
    def gte(self):
        """Gets the gte of this GrantaServerApiSearchFloatFunctionalDatumCriterion.  # noqa: E501
        Greater than or equal to  # noqa: E501

        :return: The gte of this GrantaServerApiSearchFloatFunctionalDatumCriterion.  # noqa: E501
        :rtype: float
        """
        return self._gte

    @gte.setter
    def gte(self, gte):
        """Sets the gte of this GrantaServerApiSearchFloatFunctionalDatumCriterion.
        Greater than or equal to  # noqa: E501

        :param gte: The gte of this GrantaServerApiSearchFloatFunctionalDatumCriterion.  # noqa: E501
        :type: float
        """
        self._gte = gte

    @property
    def lte(self):
        """Gets the lte of this GrantaServerApiSearchFloatFunctionalDatumCriterion.  # noqa: E501
        Less than or equal to  # noqa: E501

        :return: The lte of this GrantaServerApiSearchFloatFunctionalDatumCriterion.  # noqa: E501
        :rtype: float
        """
        return self._lte

    @lte.setter
    def lte(self, lte):
        """Sets the lte of this GrantaServerApiSearchFloatFunctionalDatumCriterion.
        Less than or equal to  # noqa: E501

        :param lte: The lte of this GrantaServerApiSearchFloatFunctionalDatumCriterion.  # noqa: E501
        :type: float
        """
        self._lte = lte

    @property
    def unit(self):
        """Gets the unit of this GrantaServerApiSearchFloatFunctionalDatumCriterion.  # noqa: E501
        Optional unit string. If not included, the gte and lte values are assumed to be in database units.  # noqa: E501

        :return: The unit of this GrantaServerApiSearchFloatFunctionalDatumCriterion.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this GrantaServerApiSearchFloatFunctionalDatumCriterion.
        Optional unit string. If not included, the gte and lte values are assumed to be in database units.  # noqa: E501

        :param unit: The unit of this GrantaServerApiSearchFloatFunctionalDatumCriterion.  # noqa: E501
        :type: str
        """
        self._unit = unit

    @property
    def constraints(self):
        """Gets the constraints of this GrantaServerApiSearchFloatFunctionalDatumCriterion.  # noqa: E501
        Constraints on the parameters of the attribute. Unspecified parameters will be assumed to be unconstrained.  # noqa: E501

        :return: The constraints of this GrantaServerApiSearchFloatFunctionalDatumCriterion.  # noqa: E501
        :rtype: list[GrantaServerApiSearchParameterConstraint]
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        """Sets the constraints of this GrantaServerApiSearchFloatFunctionalDatumCriterion.
        Constraints on the parameters of the attribute. Unspecified parameters will be assumed to be unconstrained.  # noqa: E501

        :param constraints: The constraints of this GrantaServerApiSearchFloatFunctionalDatumCriterion.  # noqa: E501
        :type: list[GrantaServerApiSearchParameterConstraint]
        """
        self._constraints = constraints


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
        if issubclass(GrantaServerApiSearchFloatFunctionalDatumCriterion, dict):
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
        if not isinstance(other, GrantaServerApiSearchFloatFunctionalDatumCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
