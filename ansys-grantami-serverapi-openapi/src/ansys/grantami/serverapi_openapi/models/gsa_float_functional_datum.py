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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from ansys.grantami.serverapi_openapi.models.gsa_applicable_datum import (  # noqa: F401
    GsaApplicableDatum,
)
from ansys.grantami.serverapi_openapi.models.gsa_datum_type import GsaDatumType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaFloatFunctionalDatum(GsaApplicableDatum):
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
    discriminator_class_map: dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "datum_type": "GsaDatumType",
        "estimated": "bool",
        "graph_type": "GsaGraphType",
        "is_range": "bool",
        "log_scale_on_y_axis": "bool",
        "not_applicable": "str",
        "parameter_settings": "list[GsaFunctionalParameterSetting]",
        "show_as_table": "bool",
        "unit": "GsaSlimUnit",
    }

    attribute_map: dict[str, str] = {
        "datum_type": "datumType",
        "estimated": "estimated",
        "graph_type": "graphType",
        "is_range": "isRange",
        "log_scale_on_y_axis": "logScaleOnYAxis",
        "not_applicable": "notApplicable",
        "parameter_settings": "parameterSettings",
        "show_as_table": "showAsTable",
        "unit": "unit",
    }

    subtype_mapping: dict[str, str] = {
        "graphType": "GsaGraphType",
        "unit": "GsaSlimUnit",
        "parameterSettings": "GsaFunctionalParameterSetting",
    }

    discriminator_value_class_map = {
        "series".lower(): "#/components/schemas/GsaFloatFunctionalSeriesDatum",
        "grid".lower(): "#/components/schemas/GsaFloatFunctionalGridDatum",
    }

    discriminator: Optional[str] = "graph_type"

    def __init__(
        self,
        *,
        datum_type: "GsaDatumType" = GsaDatumType.FLOATFUNCTIONAL,
        estimated: "bool",
        graph_type: "GsaGraphType",
        is_range: "bool",
        log_scale_on_y_axis: "bool",
        not_applicable: "str" = "applicable",
        parameter_settings: "list[GsaFunctionalParameterSetting]",
        show_as_table: "bool",
        unit: "Union[GsaSlimUnit, Unset_Type]" = Unset,
    ) -> None:
        """GsaFloatFunctionalDatum - a model defined in Swagger

        Parameters
        ----------
        datum_type: GsaDatumType
        estimated: bool
        graph_type: GsaGraphType
        is_range: bool
        log_scale_on_y_axis: bool
        not_applicable: str
        parameter_settings: list[GsaFunctionalParameterSetting]
        show_as_table: bool
        unit: GsaSlimUnit, optional
        """
        super().__init__(datum_type=datum_type, not_applicable=not_applicable)
        self._graph_type: GsaGraphType
        self._log_scale_on_y_axis: bool
        self._estimated: bool
        self._show_as_table: bool
        self._is_range: bool
        self._unit: Union[GsaSlimUnit, Unset_Type] = Unset
        self._parameter_settings: list[GsaFunctionalParameterSetting]

        self.graph_type = graph_type
        self.log_scale_on_y_axis = log_scale_on_y_axis
        self.estimated = estimated
        self.show_as_table = show_as_table
        self.is_range = is_range
        if unit is not Unset:
            self.unit = unit
        self.parameter_settings = parameter_settings

    @property
    def graph_type(self) -> "GsaGraphType":
        """Gets the graph_type of this GsaFloatFunctionalDatum.

        Returns
        -------
        GsaGraphType
            The graph_type of this GsaFloatFunctionalDatum.
        """
        return self._graph_type

    @graph_type.setter
    def graph_type(self, graph_type: "GsaGraphType") -> None:
        """Sets the graph_type of this GsaFloatFunctionalDatum.

        Parameters
        ----------
        graph_type: GsaGraphType
            The graph_type of this GsaFloatFunctionalDatum.
        """
        # Field is not nullable
        if graph_type is None:
            raise ValueError("Invalid value for 'graph_type', must not be 'None'")
        # Field is required
        if graph_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'graph_type', must not be 'Unset'")
        self._graph_type = graph_type

    @property
    def log_scale_on_y_axis(self) -> "bool":
        """Gets the log_scale_on_y_axis of this GsaFloatFunctionalDatum.

        Returns
        -------
        bool
            The log_scale_on_y_axis of this GsaFloatFunctionalDatum.
        """
        return self._log_scale_on_y_axis

    @log_scale_on_y_axis.setter
    def log_scale_on_y_axis(self, log_scale_on_y_axis: "bool") -> None:
        """Sets the log_scale_on_y_axis of this GsaFloatFunctionalDatum.

        Parameters
        ----------
        log_scale_on_y_axis: bool
            The log_scale_on_y_axis of this GsaFloatFunctionalDatum.
        """
        # Field is not nullable
        if log_scale_on_y_axis is None:
            raise ValueError("Invalid value for 'log_scale_on_y_axis', must not be 'None'")
        # Field is required
        if log_scale_on_y_axis is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'log_scale_on_y_axis', must not be 'Unset'")
        self._log_scale_on_y_axis = log_scale_on_y_axis

    @property
    def estimated(self) -> "bool":
        """Gets the estimated of this GsaFloatFunctionalDatum.

        Returns
        -------
        bool
            The estimated of this GsaFloatFunctionalDatum.
        """
        return self._estimated

    @estimated.setter
    def estimated(self, estimated: "bool") -> None:
        """Sets the estimated of this GsaFloatFunctionalDatum.

        Parameters
        ----------
        estimated: bool
            The estimated of this GsaFloatFunctionalDatum.
        """
        # Field is not nullable
        if estimated is None:
            raise ValueError("Invalid value for 'estimated', must not be 'None'")
        # Field is required
        if estimated is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'estimated', must not be 'Unset'")
        self._estimated = estimated

    @property
    def show_as_table(self) -> "bool":
        """Gets the show_as_table of this GsaFloatFunctionalDatum.

        Returns
        -------
        bool
            The show_as_table of this GsaFloatFunctionalDatum.
        """
        return self._show_as_table

    @show_as_table.setter
    def show_as_table(self, show_as_table: "bool") -> None:
        """Sets the show_as_table of this GsaFloatFunctionalDatum.

        Parameters
        ----------
        show_as_table: bool
            The show_as_table of this GsaFloatFunctionalDatum.
        """
        # Field is not nullable
        if show_as_table is None:
            raise ValueError("Invalid value for 'show_as_table', must not be 'None'")
        # Field is required
        if show_as_table is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'show_as_table', must not be 'Unset'")
        self._show_as_table = show_as_table

    @property
    def is_range(self) -> "bool":
        """Gets the is_range of this GsaFloatFunctionalDatum.

        Returns
        -------
        bool
            The is_range of this GsaFloatFunctionalDatum.
        """
        return self._is_range

    @is_range.setter
    def is_range(self, is_range: "bool") -> None:
        """Sets the is_range of this GsaFloatFunctionalDatum.

        Parameters
        ----------
        is_range: bool
            The is_range of this GsaFloatFunctionalDatum.
        """
        # Field is not nullable
        if is_range is None:
            raise ValueError("Invalid value for 'is_range', must not be 'None'")
        # Field is required
        if is_range is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'is_range', must not be 'Unset'")
        self._is_range = is_range

    @property
    def unit(self) -> "Union[GsaSlimUnit, Unset_Type]":
        """Gets the unit of this GsaFloatFunctionalDatum.

        Returns
        -------
        Union[GsaSlimUnit, Unset_Type]
            The unit of this GsaFloatFunctionalDatum.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "Union[GsaSlimUnit, Unset_Type]") -> None:
        """Sets the unit of this GsaFloatFunctionalDatum.

        Parameters
        ----------
        unit: Union[GsaSlimUnit, Unset_Type]
            The unit of this GsaFloatFunctionalDatum.
        """
        # Field is not nullable
        if unit is None:
            raise ValueError("Invalid value for 'unit', must not be 'None'")
        self._unit = unit

    @property
    def parameter_settings(self) -> "list[GsaFunctionalParameterSetting]":
        """Gets the parameter_settings of this GsaFloatFunctionalDatum.

        Returns
        -------
        list[GsaFunctionalParameterSetting]
            The parameter_settings of this GsaFloatFunctionalDatum.
        """
        return self._parameter_settings

    @parameter_settings.setter
    def parameter_settings(self, parameter_settings: "list[GsaFunctionalParameterSetting]") -> None:
        """Sets the parameter_settings of this GsaFloatFunctionalDatum.

        Parameters
        ----------
        parameter_settings: list[GsaFunctionalParameterSetting]
            The parameter_settings of this GsaFloatFunctionalDatum.
        """
        # Field is not nullable
        if parameter_settings is None:
            raise ValueError("Invalid value for 'parameter_settings', must not be 'None'")
        # Field is required
        if parameter_settings is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'parameter_settings', must not be 'Unset'")
        self._parameter_settings = parameter_settings

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[cls._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen,
        # so we have to extract it from the JSON reference
        return cls.discriminator_value_class_map[discriminator_value].rsplit("/", 1)[-1]

    @classmethod
    def _get_discriminator_field_name(cls) -> str:
        assert cls.discriminator
        name_tokens = cls.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GsaFloatFunctionalDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
