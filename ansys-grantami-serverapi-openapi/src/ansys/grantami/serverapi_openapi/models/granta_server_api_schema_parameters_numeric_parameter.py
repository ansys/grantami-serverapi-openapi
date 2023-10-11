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

from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_parameters_parameter import (
    GrantaServerApiSchemaParametersParameter,
)  # noqa: F401

if TYPE_CHECKING:
    from . import *


class GrantaServerApiSchemaParametersNumericParameter(
    GrantaServerApiSchemaParametersParameter
):
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
        "display_names": "dict(str, str)",
        "guid": "str",
        "help_path": "str",
        "interpolation_type": "GrantaServerApiSchemaParametersParameterInterpolationType",
        "is_restricted": "bool",
        "name": "str",
        "scale_type": "GrantaServerApiSchemaParametersParameterScaleType",
        "type": "str",
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimUnit",
        "values": "list[GrantaServerApiSchemaParametersNumericParameterValue]",
    }

    attribute_map = {
        "display_names": "displayNames",
        "guid": "guid",
        "help_path": "helpPath",
        "interpolation_type": "interpolationType",
        "is_restricted": "isRestricted",
        "name": "name",
        "scale_type": "scaleType",
        "type": "type",
        "unit": "unit",
        "values": "values",
    }

    subtype_mapping = {
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimUnit",
        "values": "GrantaServerApiSchemaParametersNumericParameterValue",
        "interpolationType": "GrantaServerApiSchemaParametersParameterInterpolationType",
        "scaleType": "GrantaServerApiSchemaParametersParameterScaleType",
    }

    def __init__(
        self,
        *,
        display_names: "Optional[Dict[str, str]]" = None,
        guid: "Optional[str]" = None,
        help_path: "Optional[str]" = None,
        interpolation_type: "Optional[GrantaServerApiSchemaParametersParameterInterpolationType]" = None,
        is_restricted: "Optional[bool]" = None,
        name: "Optional[str]" = None,
        scale_type: "Optional[GrantaServerApiSchemaParametersParameterScaleType]" = None,
        type: "str" = "numeric",
        unit: "Optional[GrantaServerApiSchemaSlimEntitiesSlimUnit]" = None,
        values: "Optional[List[GrantaServerApiSchemaParametersNumericParameterValue]]" = None,
    ) -> None:
        """GrantaServerApiSchemaParametersNumericParameter - a model defined in Swagger

        Parameters
        ----------
            display_names: Dict[str, str], optional
            guid: str, optional
            help_path: str, optional
            interpolation_type: GrantaServerApiSchemaParametersParameterInterpolationType, optional
            is_restricted: bool, optional
            name: str, optional
            scale_type: GrantaServerApiSchemaParametersParameterScaleType, optional
            type: str
            unit: GrantaServerApiSchemaSlimEntitiesSlimUnit, optional
            values: List[GrantaServerApiSchemaParametersNumericParameterValue], optional
        """
        super().__init__(
            display_names=display_names, guid=guid, help_path=help_path, name=name
        )
        self._type = None
        self._is_restricted = None
        self._unit = None
        self._values = None
        self._interpolation_type = None
        self._scale_type = None
        self.discriminator = None
        self.type = type
        if is_restricted is not None:
            self.is_restricted = is_restricted
        if unit is not None:
            self.unit = unit
        if values is not None:
            self.values = values
        if interpolation_type is not None:
            self.interpolation_type = interpolation_type
        if scale_type is not None:
            self.scale_type = scale_type

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaParametersNumericParameter.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaParametersNumericParameter.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaParametersNumericParameter.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaParametersNumericParameter.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @property
    def is_restricted(self) -> "bool":
        """Gets the is_restricted of this GrantaServerApiSchemaParametersNumericParameter.

        Returns
        -------
        bool
            The is_restricted of this GrantaServerApiSchemaParametersNumericParameter.
        """
        return self._is_restricted

    @is_restricted.setter
    def is_restricted(self, is_restricted: "bool") -> None:
        """Sets the is_restricted of this GrantaServerApiSchemaParametersNumericParameter.

        Parameters
        ----------
        is_restricted: bool
            The is_restricted of this GrantaServerApiSchemaParametersNumericParameter.
        """
        self._is_restricted = is_restricted

    @property
    def unit(self) -> "GrantaServerApiSchemaSlimEntitiesSlimUnit":
        """Gets the unit of this GrantaServerApiSchemaParametersNumericParameter.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimUnit
            The unit of this GrantaServerApiSchemaParametersNumericParameter.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "GrantaServerApiSchemaSlimEntitiesSlimUnit") -> None:
        """Sets the unit of this GrantaServerApiSchemaParametersNumericParameter.

        Parameters
        ----------
        unit: GrantaServerApiSchemaSlimEntitiesSlimUnit
            The unit of this GrantaServerApiSchemaParametersNumericParameter.
        """
        self._unit = unit

    @property
    def values(self) -> "list[GrantaServerApiSchemaParametersNumericParameterValue]":
        """Gets the values of this GrantaServerApiSchemaParametersNumericParameter.

        Returns
        -------
        list[GrantaServerApiSchemaParametersNumericParameterValue]
            The values of this GrantaServerApiSchemaParametersNumericParameter.
        """
        return self._values

    @values.setter
    def values(
        self, values: "list[GrantaServerApiSchemaParametersNumericParameterValue]"
    ) -> None:
        """Sets the values of this GrantaServerApiSchemaParametersNumericParameter.

        Parameters
        ----------
        values: list[GrantaServerApiSchemaParametersNumericParameterValue]
            The values of this GrantaServerApiSchemaParametersNumericParameter.
        """
        self._values = values

    @property
    def interpolation_type(
        self,
    ) -> "GrantaServerApiSchemaParametersParameterInterpolationType":
        """Gets the interpolation_type of this GrantaServerApiSchemaParametersNumericParameter.

        Returns
        -------
        GrantaServerApiSchemaParametersParameterInterpolationType
            The interpolation_type of this GrantaServerApiSchemaParametersNumericParameter.
        """
        return self._interpolation_type

    @interpolation_type.setter
    def interpolation_type(
        self,
        interpolation_type: "GrantaServerApiSchemaParametersParameterInterpolationType",
    ) -> None:
        """Sets the interpolation_type of this GrantaServerApiSchemaParametersNumericParameter.

        Parameters
        ----------
        interpolation_type: GrantaServerApiSchemaParametersParameterInterpolationType
            The interpolation_type of this GrantaServerApiSchemaParametersNumericParameter.
        """
        self._interpolation_type = interpolation_type

    @property
    def scale_type(self) -> "GrantaServerApiSchemaParametersParameterScaleType":
        """Gets the scale_type of this GrantaServerApiSchemaParametersNumericParameter.

        Returns
        -------
        GrantaServerApiSchemaParametersParameterScaleType
            The scale_type of this GrantaServerApiSchemaParametersNumericParameter.
        """
        return self._scale_type

    @scale_type.setter
    def scale_type(
        self, scale_type: "GrantaServerApiSchemaParametersParameterScaleType"
    ) -> None:
        """Sets the scale_type of this GrantaServerApiSchemaParametersNumericParameter.

        Parameters
        ----------
        scale_type: GrantaServerApiSchemaParametersParameterScaleType
            The scale_type of this GrantaServerApiSchemaParametersNumericParameter.
        """
        self._scale_type = scale_type

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
        if issubclass(GrantaServerApiSchemaParametersNumericParameter, dict):
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
        if not isinstance(other, GrantaServerApiSchemaParametersNumericParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
