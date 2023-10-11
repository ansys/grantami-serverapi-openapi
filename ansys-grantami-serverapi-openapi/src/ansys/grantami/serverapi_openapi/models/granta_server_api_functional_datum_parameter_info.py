"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase


if TYPE_CHECKING:
    from . import *


class GrantaServerApiFunctionalDatumParameterInfo(ModelBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes
    ----------
    swagger_types: Dict[str, str]
        The key is attribute name and the value is attribute type.
    attribute_map: Dict[str, str]
        The key is attribute name and the value is json key in definition.
    subtype_mapping: Dict[str, str]
        The key is the unmangled property name and the value is the corresponding type.

    """
    swagger_types = {
        "default_value": "GrantaServerApiDataExportDatumsParameterValue",
        "default_value_defined_at": "GrantaServerApiDataExportParameterSettingDefinedAt",
        "identity": "int",
        "interpolation_method_defined_at": "GrantaServerApiDataExportParameterSettingDefinedAt",
        "interpolation_type": "str",
        "name": "str",
        "parameter_type": "str",
        "scale_type": "str",
        "scale_type_defined_at": "GrantaServerApiDataExportParameterSettingDefinedAt",
        "unit_symbol": "str",
    }

    attribute_map = {
        "default_value": "defaultValue",
        "default_value_defined_at": "defaultValueDefinedAt",
        "identity": "identity",
        "interpolation_method_defined_at": "interpolationMethodDefinedAt",
        "interpolation_type": "interpolationType",
        "name": "name",
        "parameter_type": "parameterType",
        "scale_type": "scaleType",
        "scale_type_defined_at": "scaleTypeDefinedAt",
        "unit_symbol": "unitSymbol",
    }

    subtype_mapping = {
        "scaleTypeDefinedAt": "GrantaServerApiDataExportParameterSettingDefinedAt",
        "interpolationMethodDefinedAt": "GrantaServerApiDataExportParameterSettingDefinedAt",
        "defaultValueDefinedAt": "GrantaServerApiDataExportParameterSettingDefinedAt",
        "defaultValue": "GrantaServerApiDataExportDatumsParameterValue",
    }

    def __init__(
        self,
        *,
        default_value: "Optional[GrantaServerApiDataExportDatumsParameterValue]" = None,
        default_value_defined_at: "Optional[GrantaServerApiDataExportParameterSettingDefinedAt]" = None,
        identity: "Optional[int]" = None,
        interpolation_method_defined_at: "Optional[GrantaServerApiDataExportParameterSettingDefinedAt]" = None,
        interpolation_type: "Optional[str]" = None,
        name: "Optional[str]" = None,
        parameter_type: "Optional[str]" = None,
        scale_type: "Optional[str]" = None,
        scale_type_defined_at: "Optional[GrantaServerApiDataExportParameterSettingDefinedAt]" = None,
        unit_symbol: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiFunctionalDatumParameterInfo - a model defined in Swagger

        Parameters
        ----------
            default_value: GrantaServerApiDataExportDatumsParameterValue, optional
            default_value_defined_at: GrantaServerApiDataExportParameterSettingDefinedAt, optional
            identity: int, optional
            interpolation_method_defined_at: GrantaServerApiDataExportParameterSettingDefinedAt, optional
            interpolation_type: str, optional
            name: str, optional
            parameter_type: str, optional
            scale_type: str, optional
            scale_type_defined_at: GrantaServerApiDataExportParameterSettingDefinedAt, optional
            unit_symbol: str, optional
        """
        self._scale_type_defined_at = None
        self._interpolation_method_defined_at = None
        self._default_value_defined_at = None
        self._name = None
        self._identity = None
        self._unit_symbol = None
        self._scale_type = None
        self._interpolation_type = None
        self._parameter_type = None
        self._default_value = None
        self.discriminator = None
        if scale_type_defined_at is not None:
            self.scale_type_defined_at = scale_type_defined_at
        if interpolation_method_defined_at is not None:
            self.interpolation_method_defined_at = interpolation_method_defined_at
        if default_value_defined_at is not None:
            self.default_value_defined_at = default_value_defined_at
        if name is not None:
            self.name = name
        if identity is not None:
            self.identity = identity
        if unit_symbol is not None:
            self.unit_symbol = unit_symbol
        if scale_type is not None:
            self.scale_type = scale_type
        if interpolation_type is not None:
            self.interpolation_type = interpolation_type
        if parameter_type is not None:
            self.parameter_type = parameter_type
        if default_value is not None:
            self.default_value = default_value

    @property
    def scale_type_defined_at(
        self,
    ) -> "GrantaServerApiDataExportParameterSettingDefinedAt":
        """Gets the scale_type_defined_at of this GrantaServerApiFunctionalDatumParameterInfo.

        Returns
        -------
        GrantaServerApiDataExportParameterSettingDefinedAt
            The scale_type_defined_at of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        return self._scale_type_defined_at

    @scale_type_defined_at.setter
    def scale_type_defined_at(
        self,
        scale_type_defined_at: "GrantaServerApiDataExportParameterSettingDefinedAt",
    ) -> None:
        """Sets the scale_type_defined_at of this GrantaServerApiFunctionalDatumParameterInfo.

        Parameters
        ----------
        scale_type_defined_at: GrantaServerApiDataExportParameterSettingDefinedAt
            The scale_type_defined_at of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        self._scale_type_defined_at = scale_type_defined_at

    @property
    def interpolation_method_defined_at(
        self,
    ) -> "GrantaServerApiDataExportParameterSettingDefinedAt":
        """Gets the interpolation_method_defined_at of this GrantaServerApiFunctionalDatumParameterInfo.

        Returns
        -------
        GrantaServerApiDataExportParameterSettingDefinedAt
            The interpolation_method_defined_at of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        return self._interpolation_method_defined_at

    @interpolation_method_defined_at.setter
    def interpolation_method_defined_at(
        self,
        interpolation_method_defined_at: "GrantaServerApiDataExportParameterSettingDefinedAt",
    ) -> None:
        """Sets the interpolation_method_defined_at of this GrantaServerApiFunctionalDatumParameterInfo.

        Parameters
        ----------
        interpolation_method_defined_at: GrantaServerApiDataExportParameterSettingDefinedAt
            The interpolation_method_defined_at of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        self._interpolation_method_defined_at = interpolation_method_defined_at

    @property
    def default_value_defined_at(
        self,
    ) -> "GrantaServerApiDataExportParameterSettingDefinedAt":
        """Gets the default_value_defined_at of this GrantaServerApiFunctionalDatumParameterInfo.

        Returns
        -------
        GrantaServerApiDataExportParameterSettingDefinedAt
            The default_value_defined_at of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        return self._default_value_defined_at

    @default_value_defined_at.setter
    def default_value_defined_at(
        self,
        default_value_defined_at: "GrantaServerApiDataExportParameterSettingDefinedAt",
    ) -> None:
        """Sets the default_value_defined_at of this GrantaServerApiFunctionalDatumParameterInfo.

        Parameters
        ----------
        default_value_defined_at: GrantaServerApiDataExportParameterSettingDefinedAt
            The default_value_defined_at of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        self._default_value_defined_at = default_value_defined_at

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiFunctionalDatumParameterInfo.

        Returns
        -------
        str
            The name of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiFunctionalDatumParameterInfo.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        self._name = name

    @property
    def identity(self) -> "int":
        """Gets the identity of this GrantaServerApiFunctionalDatumParameterInfo.

        Returns
        -------
        int
            The identity of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        return self._identity

    @identity.setter
    def identity(self, identity: "int") -> None:
        """Sets the identity of this GrantaServerApiFunctionalDatumParameterInfo.

        Parameters
        ----------
        identity: int
            The identity of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        self._identity = identity

    @property
    def unit_symbol(self) -> "str":
        """Gets the unit_symbol of this GrantaServerApiFunctionalDatumParameterInfo.

        Returns
        -------
        str
            The unit_symbol of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        return self._unit_symbol

    @unit_symbol.setter
    def unit_symbol(self, unit_symbol: "str") -> None:
        """Sets the unit_symbol of this GrantaServerApiFunctionalDatumParameterInfo.

        Parameters
        ----------
        unit_symbol: str
            The unit_symbol of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        self._unit_symbol = unit_symbol

    @property
    def scale_type(self) -> "str":
        """Gets the scale_type of this GrantaServerApiFunctionalDatumParameterInfo.
        Linear or Log

        Returns
        -------
        str
            The scale_type of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        return self._scale_type

    @scale_type.setter
    def scale_type(self, scale_type: "str") -> None:
        """Sets the scale_type of this GrantaServerApiFunctionalDatumParameterInfo.
        Linear or Log

        Parameters
        ----------
        scale_type: str
            The scale_type of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        self._scale_type = scale_type

    @property
    def interpolation_type(self) -> "str":
        """Gets the interpolation_type of this GrantaServerApiFunctionalDatumParameterInfo.
        Auto, None, Linear or CubicSpline

        Returns
        -------
        str
            The interpolation_type of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        return self._interpolation_type

    @interpolation_type.setter
    def interpolation_type(self, interpolation_type: "str") -> None:
        """Sets the interpolation_type of this GrantaServerApiFunctionalDatumParameterInfo.
        Auto, None, Linear or CubicSpline

        Parameters
        ----------
        interpolation_type: str
            The interpolation_type of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        self._interpolation_type = interpolation_type

    @property
    def parameter_type(self) -> "str":
        """Gets the parameter_type of this GrantaServerApiFunctionalDatumParameterInfo.

        Returns
        -------
        str
            The parameter_type of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        return self._parameter_type

    @parameter_type.setter
    def parameter_type(self, parameter_type: "str") -> None:
        """Sets the parameter_type of this GrantaServerApiFunctionalDatumParameterInfo.

        Parameters
        ----------
        parameter_type: str
            The parameter_type of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        self._parameter_type = parameter_type

    @property
    def default_value(self) -> "GrantaServerApiDataExportDatumsParameterValue":
        """Gets the default_value of this GrantaServerApiFunctionalDatumParameterInfo.

        Returns
        -------
        GrantaServerApiDataExportDatumsParameterValue
            The default_value of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        return self._default_value

    @default_value.setter
    def default_value(
        self, default_value: "GrantaServerApiDataExportDatumsParameterValue"
    ) -> None:
        """Sets the default_value of this GrantaServerApiFunctionalDatumParameterInfo.

        Parameters
        ----------
        default_value: GrantaServerApiDataExportDatumsParameterValue
            The default_value of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        self._default_value = default_value

    def get_real_child_model(self, data: ModelBase) -> str:
        """Raises a NotImplementedError for a type without a discriminator defined.

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class

        Raises
        ------
        NotImplementedError
            This class has no discriminator, and hence no subclasses
        """
        raise NotImplementedError()

    def to_dict(self) -> Dict:
        """Returns the model properties as a dict

        Returns
        -------
        Dict
            Dictionary indexed by property name containing all the model properties
        """
        result = {}

        for attr in self.swagger_types.keys():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(GrantaServerApiFunctionalDatumParameterInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model

        Returns
        -------
        str
            String representation of the model as a dictionary
        """
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiFunctionalDatumParameterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
