# Copyright (C) 2023 - 2025 ANSYS, Inc. and/or its affiliates.
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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiFunctionalDatumParameterInfo(ModelBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes
    ----------
    swagger_types: dict[str, str]
        The key is attribute name and the value is attribute type.
    attribute_map: dict[str, str]
        The key is attribute name and the value is json key in definition.
    subtype_mapping: dict[str, str]
        The key is the unmangled property name and the value is the corresponding type.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "default_value": "GrantaServerApiDataExportDatumsParameterValue",
        "default_value_defined_at": "GrantaServerApiDataExportParameterSettingDefinedAt",
        "identity": "int",
        "interpolation_method_defined_at": "GrantaServerApiDataExportParameterSettingDefinedAt",
        "interpolation_type": "GrantaServerApiParameterInfoInterpolationType",
        "name": "str",
        "parameter_type": "GrantaServerApiParameterInfoParameterType",
        "scale_type": "GrantaServerApiParameterInfoScaleType",
        "scale_type_defined_at": "GrantaServerApiDataExportParameterSettingDefinedAt",
        "unit_symbol": "str",
    }

    attribute_map: dict[str, str] = {
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

    subtype_mapping: dict[str, str] = {
        "scaleTypeDefinedAt": "GrantaServerApiDataExportParameterSettingDefinedAt",
        "interpolationMethodDefinedAt": "GrantaServerApiDataExportParameterSettingDefinedAt",
        "defaultValueDefinedAt": "GrantaServerApiDataExportParameterSettingDefinedAt",
        "scaleType": "GrantaServerApiParameterInfoScaleType",
        "interpolationType": "GrantaServerApiParameterInfoInterpolationType",
        "parameterType": "GrantaServerApiParameterInfoParameterType",
        "defaultValue": "GrantaServerApiDataExportDatumsParameterValue",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        default_value: "GrantaServerApiDataExportDatumsParameterValue | Unset_Type" = Unset,
        default_value_defined_at: "GrantaServerApiDataExportParameterSettingDefinedAt | Unset_Type" = Unset,
        identity: "int | Unset_Type" = Unset,
        interpolation_method_defined_at: "GrantaServerApiDataExportParameterSettingDefinedAt | Unset_Type" = Unset,
        interpolation_type: "GrantaServerApiParameterInfoInterpolationType | Unset_Type" = Unset,
        name: "str | None | Unset_Type" = Unset,
        parameter_type: "GrantaServerApiParameterInfoParameterType | Unset_Type" = Unset,
        scale_type: "GrantaServerApiParameterInfoScaleType | Unset_Type" = Unset,
        scale_type_defined_at: "GrantaServerApiDataExportParameterSettingDefinedAt | Unset_Type" = Unset,
        unit_symbol: "str | None | Unset_Type" = Unset,
    ) -> None:
        """GrantaServerApiFunctionalDatumParameterInfo - a model defined in Swagger

        Parameters
        ----------
        default_value: GrantaServerApiDataExportDatumsParameterValue, optional
        default_value_defined_at: GrantaServerApiDataExportParameterSettingDefinedAt, optional
        identity: int, optional
        interpolation_method_defined_at: GrantaServerApiDataExportParameterSettingDefinedAt, optional
        interpolation_type: GrantaServerApiParameterInfoInterpolationType, optional
        name: str | None, optional
        parameter_type: GrantaServerApiParameterInfoParameterType, optional
        scale_type: GrantaServerApiParameterInfoScaleType, optional
        scale_type_defined_at: GrantaServerApiDataExportParameterSettingDefinedAt, optional
        unit_symbol: str | None, optional
        """
        self._scale_type_defined_at: (
            GrantaServerApiDataExportParameterSettingDefinedAt | Unset_Type
        ) = Unset
        self._interpolation_method_defined_at: (
            GrantaServerApiDataExportParameterSettingDefinedAt | Unset_Type
        ) = Unset
        self._default_value_defined_at: (
            GrantaServerApiDataExportParameterSettingDefinedAt | Unset_Type
        ) = Unset
        self._name: str | None | Unset_Type = Unset
        self._identity: int | Unset_Type = Unset
        self._unit_symbol: str | None | Unset_Type = Unset
        self._scale_type: GrantaServerApiParameterInfoScaleType | Unset_Type = Unset
        self._interpolation_type: GrantaServerApiParameterInfoInterpolationType | Unset_Type = Unset
        self._parameter_type: GrantaServerApiParameterInfoParameterType | Unset_Type = Unset
        self._default_value: GrantaServerApiDataExportDatumsParameterValue | Unset_Type = Unset

        if scale_type_defined_at is not Unset:
            self.scale_type_defined_at = scale_type_defined_at
        if interpolation_method_defined_at is not Unset:
            self.interpolation_method_defined_at = interpolation_method_defined_at
        if default_value_defined_at is not Unset:
            self.default_value_defined_at = default_value_defined_at
        if name is not Unset:
            self.name = name
        if identity is not Unset:
            self.identity = identity
        if unit_symbol is not Unset:
            self.unit_symbol = unit_symbol
        if scale_type is not Unset:
            self.scale_type = scale_type
        if interpolation_type is not Unset:
            self.interpolation_type = interpolation_type
        if parameter_type is not Unset:
            self.parameter_type = parameter_type
        if default_value is not Unset:
            self.default_value = default_value

    @property
    def scale_type_defined_at(
        self,
    ) -> "GrantaServerApiDataExportParameterSettingDefinedAt | Unset_Type":
        """Gets the scale_type_defined_at of this GrantaServerApiFunctionalDatumParameterInfo.

        Returns
        -------
        GrantaServerApiDataExportParameterSettingDefinedAt | Unset_Type
            The scale_type_defined_at of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        return self._scale_type_defined_at

    @scale_type_defined_at.setter
    def scale_type_defined_at(
        self,
        scale_type_defined_at: "GrantaServerApiDataExportParameterSettingDefinedAt | Unset_Type",
    ) -> None:
        """Sets the scale_type_defined_at of this GrantaServerApiFunctionalDatumParameterInfo.

        Parameters
        ----------
        scale_type_defined_at: GrantaServerApiDataExportParameterSettingDefinedAt | Unset_Type
            The scale_type_defined_at of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        # Field is not nullable
        if scale_type_defined_at is None:
            raise ValueError("Invalid value for 'scale_type_defined_at', must not be 'None'")
        self._scale_type_defined_at = scale_type_defined_at

    @property
    def interpolation_method_defined_at(
        self,
    ) -> "GrantaServerApiDataExportParameterSettingDefinedAt | Unset_Type":
        """Gets the interpolation_method_defined_at of this GrantaServerApiFunctionalDatumParameterInfo.

        Returns
        -------
        GrantaServerApiDataExportParameterSettingDefinedAt | Unset_Type
            The interpolation_method_defined_at of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        return self._interpolation_method_defined_at

    @interpolation_method_defined_at.setter
    def interpolation_method_defined_at(
        self,
        interpolation_method_defined_at: "GrantaServerApiDataExportParameterSettingDefinedAt | Unset_Type",
    ) -> None:
        """Sets the interpolation_method_defined_at of this GrantaServerApiFunctionalDatumParameterInfo.

        Parameters
        ----------
        interpolation_method_defined_at: GrantaServerApiDataExportParameterSettingDefinedAt | Unset_Type
            The interpolation_method_defined_at of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        # Field is not nullable
        if interpolation_method_defined_at is None:
            raise ValueError(
                "Invalid value for 'interpolation_method_defined_at', must not be 'None'"
            )
        self._interpolation_method_defined_at = interpolation_method_defined_at

    @property
    def default_value_defined_at(
        self,
    ) -> "GrantaServerApiDataExportParameterSettingDefinedAt | Unset_Type":
        """Gets the default_value_defined_at of this GrantaServerApiFunctionalDatumParameterInfo.

        Returns
        -------
        GrantaServerApiDataExportParameterSettingDefinedAt | Unset_Type
            The default_value_defined_at of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        return self._default_value_defined_at

    @default_value_defined_at.setter
    def default_value_defined_at(
        self,
        default_value_defined_at: "GrantaServerApiDataExportParameterSettingDefinedAt | Unset_Type",
    ) -> None:
        """Sets the default_value_defined_at of this GrantaServerApiFunctionalDatumParameterInfo.

        Parameters
        ----------
        default_value_defined_at: GrantaServerApiDataExportParameterSettingDefinedAt | Unset_Type
            The default_value_defined_at of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        # Field is not nullable
        if default_value_defined_at is None:
            raise ValueError("Invalid value for 'default_value_defined_at', must not be 'None'")
        self._default_value_defined_at = default_value_defined_at

    @property
    def name(self) -> "str | None | Unset_Type":
        """Gets the name of this GrantaServerApiFunctionalDatumParameterInfo.

        Returns
        -------
        str | None | Unset_Type
            The name of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        return self._name

    @name.setter
    def name(self, name: "str | None | Unset_Type") -> None:
        """Sets the name of this GrantaServerApiFunctionalDatumParameterInfo.

        Parameters
        ----------
        name: str | None | Unset_Type
            The name of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        self._name = name

    @property
    def identity(self) -> "int | Unset_Type":
        """Gets the identity of this GrantaServerApiFunctionalDatumParameterInfo.

        Returns
        -------
        int | Unset_Type
            The identity of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        return self._identity

    @identity.setter
    def identity(self, identity: "int | Unset_Type") -> None:
        """Sets the identity of this GrantaServerApiFunctionalDatumParameterInfo.

        Parameters
        ----------
        identity: int | Unset_Type
            The identity of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        # Field is not nullable
        if identity is None:
            raise ValueError("Invalid value for 'identity', must not be 'None'")
        self._identity = identity

    @property
    def unit_symbol(self) -> "str | None | Unset_Type":
        """Gets the unit_symbol of this GrantaServerApiFunctionalDatumParameterInfo.

        Returns
        -------
        str | None | Unset_Type
            The unit_symbol of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        return self._unit_symbol

    @unit_symbol.setter
    def unit_symbol(self, unit_symbol: "str | None | Unset_Type") -> None:
        """Sets the unit_symbol of this GrantaServerApiFunctionalDatumParameterInfo.

        Parameters
        ----------
        unit_symbol: str | None | Unset_Type
            The unit_symbol of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        self._unit_symbol = unit_symbol

    @property
    def scale_type(self) -> "GrantaServerApiParameterInfoScaleType | Unset_Type":
        """Gets the scale_type of this GrantaServerApiFunctionalDatumParameterInfo.

        Returns
        -------
        GrantaServerApiParameterInfoScaleType | Unset_Type
            The scale_type of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        return self._scale_type

    @scale_type.setter
    def scale_type(self, scale_type: "GrantaServerApiParameterInfoScaleType | Unset_Type") -> None:
        """Sets the scale_type of this GrantaServerApiFunctionalDatumParameterInfo.

        Parameters
        ----------
        scale_type: GrantaServerApiParameterInfoScaleType | Unset_Type
            The scale_type of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        # Field is not nullable
        if scale_type is None:
            raise ValueError("Invalid value for 'scale_type', must not be 'None'")
        self._scale_type = scale_type

    @property
    def interpolation_type(self) -> "GrantaServerApiParameterInfoInterpolationType | Unset_Type":
        """Gets the interpolation_type of this GrantaServerApiFunctionalDatumParameterInfo.

        Returns
        -------
        GrantaServerApiParameterInfoInterpolationType | Unset_Type
            The interpolation_type of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        return self._interpolation_type

    @interpolation_type.setter
    def interpolation_type(
        self, interpolation_type: "GrantaServerApiParameterInfoInterpolationType | Unset_Type"
    ) -> None:
        """Sets the interpolation_type of this GrantaServerApiFunctionalDatumParameterInfo.

        Parameters
        ----------
        interpolation_type: GrantaServerApiParameterInfoInterpolationType | Unset_Type
            The interpolation_type of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        # Field is not nullable
        if interpolation_type is None:
            raise ValueError("Invalid value for 'interpolation_type', must not be 'None'")
        self._interpolation_type = interpolation_type

    @property
    def parameter_type(self) -> "GrantaServerApiParameterInfoParameterType | Unset_Type":
        """Gets the parameter_type of this GrantaServerApiFunctionalDatumParameterInfo.

        Returns
        -------
        GrantaServerApiParameterInfoParameterType | Unset_Type
            The parameter_type of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        return self._parameter_type

    @parameter_type.setter
    def parameter_type(
        self, parameter_type: "GrantaServerApiParameterInfoParameterType | Unset_Type"
    ) -> None:
        """Sets the parameter_type of this GrantaServerApiFunctionalDatumParameterInfo.

        Parameters
        ----------
        parameter_type: GrantaServerApiParameterInfoParameterType | Unset_Type
            The parameter_type of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        # Field is not nullable
        if parameter_type is None:
            raise ValueError("Invalid value for 'parameter_type', must not be 'None'")
        self._parameter_type = parameter_type

    @property
    def default_value(self) -> "GrantaServerApiDataExportDatumsParameterValue | Unset_Type":
        """Gets the default_value of this GrantaServerApiFunctionalDatumParameterInfo.

        Returns
        -------
        GrantaServerApiDataExportDatumsParameterValue | Unset_Type
            The default_value of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        return self._default_value

    @default_value.setter
    def default_value(
        self, default_value: "GrantaServerApiDataExportDatumsParameterValue | Unset_Type"
    ) -> None:
        """Sets the default_value of this GrantaServerApiFunctionalDatumParameterInfo.

        Parameters
        ----------
        default_value: GrantaServerApiDataExportDatumsParameterValue | Unset_Type
            The default_value of this GrantaServerApiFunctionalDatumParameterInfo.
        """
        # Field is not nullable
        if default_value is None:
            raise ValueError("Invalid value for 'default_value', must not be 'None'")
        self._default_value = default_value

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
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
        if not isinstance(other, GrantaServerApiFunctionalDatumParameterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
