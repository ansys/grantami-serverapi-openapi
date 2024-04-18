# Copyright (C) 2023 - 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, Union  # noqa: F401

from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_parameters_parameter import (  # noqa: F401
    GrantaServerApiSchemaParametersParameter,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiSchemaParametersNumericParameter(GrantaServerApiSchemaParametersParameter):
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
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: Dict[str, str] = {
        "default_parameter_value_guid": "str",
        "display_names": "dict(str, str)",
        "guid": "str",
        "interpolation_type": "GrantaServerApiSchemaParametersParameterInterpolationType",
        "is_restricted": "bool",
        "name": "str",
        "scale_type": "GrantaServerApiSchemaParametersParameterScaleType",
        "values": "list[GrantaServerApiSchemaParametersNumericParameterValue]",
        "help_path": "str",
        "type": "str",
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimUnit",
    }

    attribute_map: Dict[str, str] = {
        "default_parameter_value_guid": "defaultParameterValueGuid",
        "display_names": "displayNames",
        "guid": "guid",
        "interpolation_type": "interpolationType",
        "is_restricted": "isRestricted",
        "name": "name",
        "scale_type": "scaleType",
        "values": "values",
        "help_path": "helpPath",
        "type": "type",
        "unit": "unit",
    }

    subtype_mapping: Dict[str, str] = {
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimUnit",
        "values": "GrantaServerApiSchemaParametersNumericParameterValue",
        "interpolationType": "GrantaServerApiSchemaParametersParameterInterpolationType",
        "scaleType": "GrantaServerApiSchemaParametersParameterScaleType",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        default_parameter_value_guid: "str",
        display_names: "Dict[str, str]",
        guid: "str",
        interpolation_type: "GrantaServerApiSchemaParametersParameterInterpolationType",
        is_restricted: "bool",
        name: "str",
        scale_type: "GrantaServerApiSchemaParametersParameterScaleType",
        values: "List[GrantaServerApiSchemaParametersNumericParameterValue]",
        help_path: "Union[str, None, Unset_Type]" = Unset,
        type: "str" = "numeric",
        unit: "Union[GrantaServerApiSchemaSlimEntitiesSlimUnit, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaParametersNumericParameter - a model defined in Swagger

        Parameters
        ----------
        default_parameter_value_guid: str
        display_names: Dict[str, str]
        guid: str
        interpolation_type: GrantaServerApiSchemaParametersParameterInterpolationType
        is_restricted: bool
        name: str
        scale_type: GrantaServerApiSchemaParametersParameterScaleType
        values: List[GrantaServerApiSchemaParametersNumericParameterValue]
        help_path: str, optional
        type: str
        unit: GrantaServerApiSchemaSlimEntitiesSlimUnit, optional
        """
        super().__init__(
            default_parameter_value_guid=default_parameter_value_guid,
            display_names=display_names,
            guid=guid,
            name=name,
            help_path=help_path,
        )
        self._type: str
        self._is_restricted: bool
        self._unit: Union[GrantaServerApiSchemaSlimEntitiesSlimUnit, Unset_Type] = Unset
        self._values: List[GrantaServerApiSchemaParametersNumericParameterValue]
        self._interpolation_type: GrantaServerApiSchemaParametersParameterInterpolationType
        self._scale_type: GrantaServerApiSchemaParametersParameterScaleType

        self.type = type
        self.is_restricted = is_restricted
        if unit is not Unset:
            self.unit = unit
        self.values = values
        self.interpolation_type = interpolation_type
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
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
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
        # Field is not nullable
        if is_restricted is None:
            raise ValueError("Invalid value for 'is_restricted', must not be 'None'")
        # Field is required
        if is_restricted is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'is_restricted', must not be 'Unset'")
        self._is_restricted = is_restricted

    @property
    def unit(self) -> "Union[GrantaServerApiSchemaSlimEntitiesSlimUnit, Unset_Type]":
        """Gets the unit of this GrantaServerApiSchemaParametersNumericParameter.

        Returns
        -------
        Union[GrantaServerApiSchemaSlimEntitiesSlimUnit, Unset_Type]
            The unit of this GrantaServerApiSchemaParametersNumericParameter.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "Union[GrantaServerApiSchemaSlimEntitiesSlimUnit, Unset_Type]") -> None:
        """Sets the unit of this GrantaServerApiSchemaParametersNumericParameter.

        Parameters
        ----------
        unit: Union[GrantaServerApiSchemaSlimEntitiesSlimUnit, Unset_Type]
            The unit of this GrantaServerApiSchemaParametersNumericParameter.
        """
        # Field is not nullable
        if unit is None:
            raise ValueError("Invalid value for 'unit', must not be 'None'")
        self._unit = unit

    @property
    def values(self) -> "List[GrantaServerApiSchemaParametersNumericParameterValue]":
        """Gets the values of this GrantaServerApiSchemaParametersNumericParameter.

        Returns
        -------
        List[GrantaServerApiSchemaParametersNumericParameterValue]
            The values of this GrantaServerApiSchemaParametersNumericParameter.
        """
        return self._values

    @values.setter
    def values(self, values: "List[GrantaServerApiSchemaParametersNumericParameterValue]") -> None:
        """Sets the values of this GrantaServerApiSchemaParametersNumericParameter.

        Parameters
        ----------
        values: List[GrantaServerApiSchemaParametersNumericParameterValue]
            The values of this GrantaServerApiSchemaParametersNumericParameter.
        """
        # Field is not nullable
        if values is None:
            raise ValueError("Invalid value for 'values', must not be 'None'")
        # Field is required
        if values is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'values', must not be 'Unset'")
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
        # Field is not nullable
        if interpolation_type is None:
            raise ValueError("Invalid value for 'interpolation_type', must not be 'None'")
        # Field is required
        if interpolation_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'interpolation_type', must not be 'Unset'")
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
    def scale_type(self, scale_type: "GrantaServerApiSchemaParametersParameterScaleType") -> None:
        """Sets the scale_type of this GrantaServerApiSchemaParametersNumericParameter.

        Parameters
        ----------
        scale_type: GrantaServerApiSchemaParametersParameterScaleType
            The scale_type of this GrantaServerApiSchemaParametersNumericParameter.
        """
        # Field is not nullable
        if scale_type is None:
            raise ValueError("Invalid value for 'scale_type', must not be 'None'")
        # Field is required
        if scale_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'scale_type', must not be 'Unset'")
        self._scale_type = scale_type

    @classmethod
    def get_real_child_model(cls, data: Dict[str, str]) -> str:
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
