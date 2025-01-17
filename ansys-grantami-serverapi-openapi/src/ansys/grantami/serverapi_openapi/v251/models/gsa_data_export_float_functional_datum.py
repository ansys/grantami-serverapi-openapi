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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from ansys.grantami.serverapi_openapi.v251.models.gsa_attribute_type import GsaAttributeType
from ansys.grantami.serverapi_openapi.v251.models.gsa_data_export_applicable_datum import (  # noqa: F401
    GsaDataExportApplicableDatum,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaDataExportFloatFunctionalDatum(GsaDataExportApplicableDatum):
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
        "datum_type": "GsaAttributeType",
        "graph_type": "str",
        "not_applicable": "str",
        "attribute_guid": "str",
        "attribute_identity": "int",
        "is_estimated": "bool",
        "is_logarithmic": "bool",
        "is_range": "bool",
        "meta_datums": "list[GsaDataExportDatum]",
        "parameters": "list[GsaFunctionalDatumParameterInfo]",
        "unit_symbol": "str",
        "x_axis_parameter": "GsaFunctionalDatumParameterInfo",
    }

    attribute_map: dict[str, str] = {
        "datum_type": "datumType",
        "graph_type": "graphType",
        "not_applicable": "notApplicable",
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "is_estimated": "isEstimated",
        "is_logarithmic": "isLogarithmic",
        "is_range": "isRange",
        "meta_datums": "metaDatums",
        "parameters": "parameters",
        "unit_symbol": "unitSymbol",
        "x_axis_parameter": "xAxisParameter",
    }

    subtype_mapping: dict[str, str] = {
        "xAxisParameter": "GsaFunctionalDatumParameterInfo",
        "parameters": "GsaFunctionalDatumParameterInfo",
    }

    discriminator_value_class_map = {
        "grid".lower(): "#/components/schemas/GsaDataExportFunctionalGridDatum",
        "series".lower(): "#/components/schemas/GsaDataExportFunctionalSeriesDatum",
    }

    discriminator: Optional[str] = "graph_type"

    def __init__(
        self,
        *,
        datum_type: "GsaAttributeType" = GsaAttributeType.FLOATFUNCTIONAL,
        graph_type: "str",
        not_applicable: "str" = "applicable",
        attribute_guid: "Union[str, Unset_Type]" = Unset,
        attribute_identity: "Union[int, Unset_Type]" = Unset,
        is_estimated: "Union[bool, Unset_Type]" = Unset,
        is_logarithmic: "Union[bool, Unset_Type]" = Unset,
        is_range: "Union[bool, Unset_Type]" = Unset,
        meta_datums: "Union[list[GsaDataExportDatum], None, Unset_Type]" = Unset,
        parameters: "Union[list[GsaFunctionalDatumParameterInfo], None, Unset_Type]" = Unset,
        unit_symbol: "Union[str, None, Unset_Type]" = Unset,
        x_axis_parameter: "Union[GsaFunctionalDatumParameterInfo, Unset_Type]" = Unset,
    ) -> None:
        """GsaDataExportFloatFunctionalDatum - a model defined in Swagger

        Parameters
        ----------
        datum_type: GsaAttributeType
        graph_type: str
        not_applicable: str
        attribute_guid: str, optional
        attribute_identity: int, optional
        is_estimated: bool, optional
        is_logarithmic: bool, optional
        is_range: bool, optional
        meta_datums: list[GsaDataExportDatum], optional
        parameters: list[GsaFunctionalDatumParameterInfo], optional
        unit_symbol: str, optional
        x_axis_parameter: GsaFunctionalDatumParameterInfo, optional
        """
        super().__init__(
            datum_type=datum_type,
            not_applicable=not_applicable,
            attribute_guid=attribute_guid,
            attribute_identity=attribute_identity,
            meta_datums=meta_datums,
        )
        self._graph_type: str
        self._unit_symbol: Union[str, None, Unset_Type] = Unset
        self._x_axis_parameter: Union[GsaFunctionalDatumParameterInfo, Unset_Type] = Unset
        self._parameters: Union[list[GsaFunctionalDatumParameterInfo], None, Unset_Type] = Unset
        self._is_estimated: Union[bool, Unset_Type] = Unset
        self._is_range: Union[bool, Unset_Type] = Unset
        self._is_logarithmic: Union[bool, Unset_Type] = Unset

        self.graph_type = graph_type
        if unit_symbol is not Unset:
            self.unit_symbol = unit_symbol
        if x_axis_parameter is not Unset:
            self.x_axis_parameter = x_axis_parameter
        if parameters is not Unset:
            self.parameters = parameters
        if is_estimated is not Unset:
            self.is_estimated = is_estimated
        if is_range is not Unset:
            self.is_range = is_range
        if is_logarithmic is not Unset:
            self.is_logarithmic = is_logarithmic

    @property
    def graph_type(self) -> "str":
        """Gets the graph_type of this GsaDataExportFloatFunctionalDatum.

        Returns
        -------
        str
            The graph_type of this GsaDataExportFloatFunctionalDatum.
        """
        return self._graph_type

    @graph_type.setter
    def graph_type(self, graph_type: "str") -> None:
        """Sets the graph_type of this GsaDataExportFloatFunctionalDatum.

        Parameters
        ----------
        graph_type: str
            The graph_type of this GsaDataExportFloatFunctionalDatum.
        """
        # Field is required
        if graph_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'graph_type', must not be 'Unset'")
        self._graph_type = graph_type

    @property
    def unit_symbol(self) -> "Union[str, None, Unset_Type]":
        """Gets the unit_symbol of this GsaDataExportFloatFunctionalDatum.

        Returns
        -------
        Union[str, None, Unset_Type]
            The unit_symbol of this GsaDataExportFloatFunctionalDatum.
        """
        return self._unit_symbol

    @unit_symbol.setter
    def unit_symbol(self, unit_symbol: "Union[str, None, Unset_Type]") -> None:
        """Sets the unit_symbol of this GsaDataExportFloatFunctionalDatum.

        Parameters
        ----------
        unit_symbol: Union[str, None, Unset_Type]
            The unit_symbol of this GsaDataExportFloatFunctionalDatum.
        """
        self._unit_symbol = unit_symbol

    @property
    def x_axis_parameter(self) -> "Union[GsaFunctionalDatumParameterInfo, Unset_Type]":
        """Gets the x_axis_parameter of this GsaDataExportFloatFunctionalDatum.

        Returns
        -------
        Union[GsaFunctionalDatumParameterInfo, Unset_Type]
            The x_axis_parameter of this GsaDataExportFloatFunctionalDatum.
        """
        return self._x_axis_parameter

    @x_axis_parameter.setter
    def x_axis_parameter(
        self, x_axis_parameter: "Union[GsaFunctionalDatumParameterInfo, Unset_Type]"
    ) -> None:
        """Sets the x_axis_parameter of this GsaDataExportFloatFunctionalDatum.

        Parameters
        ----------
        x_axis_parameter: Union[GsaFunctionalDatumParameterInfo, Unset_Type]
            The x_axis_parameter of this GsaDataExportFloatFunctionalDatum.
        """
        # Field is not nullable
        if x_axis_parameter is None:
            raise ValueError("Invalid value for 'x_axis_parameter', must not be 'None'")
        self._x_axis_parameter = x_axis_parameter

    @property
    def parameters(self) -> "Union[list[GsaFunctionalDatumParameterInfo], None, Unset_Type]":
        """Gets the parameters of this GsaDataExportFloatFunctionalDatum.

        Returns
        -------
        Union[list[GsaFunctionalDatumParameterInfo], None, Unset_Type]
            The parameters of this GsaDataExportFloatFunctionalDatum.
        """
        return self._parameters

    @parameters.setter
    def parameters(
        self, parameters: "Union[list[GsaFunctionalDatumParameterInfo], None, Unset_Type]"
    ) -> None:
        """Sets the parameters of this GsaDataExportFloatFunctionalDatum.

        Parameters
        ----------
        parameters: Union[list[GsaFunctionalDatumParameterInfo], None, Unset_Type]
            The parameters of this GsaDataExportFloatFunctionalDatum.
        """
        self._parameters = parameters

    @property
    def is_estimated(self) -> "Union[bool, Unset_Type]":
        """Gets the is_estimated of this GsaDataExportFloatFunctionalDatum.

        Returns
        -------
        Union[bool, Unset_Type]
            The is_estimated of this GsaDataExportFloatFunctionalDatum.
        """
        return self._is_estimated

    @is_estimated.setter
    def is_estimated(self, is_estimated: "Union[bool, Unset_Type]") -> None:
        """Sets the is_estimated of this GsaDataExportFloatFunctionalDatum.

        Parameters
        ----------
        is_estimated: Union[bool, Unset_Type]
            The is_estimated of this GsaDataExportFloatFunctionalDatum.
        """
        # Field is not nullable
        if is_estimated is None:
            raise ValueError("Invalid value for 'is_estimated', must not be 'None'")
        self._is_estimated = is_estimated

    @property
    def is_range(self) -> "Union[bool, Unset_Type]":
        """Gets the is_range of this GsaDataExportFloatFunctionalDatum.

        Returns
        -------
        Union[bool, Unset_Type]
            The is_range of this GsaDataExportFloatFunctionalDatum.
        """
        return self._is_range

    @is_range.setter
    def is_range(self, is_range: "Union[bool, Unset_Type]") -> None:
        """Sets the is_range of this GsaDataExportFloatFunctionalDatum.

        Parameters
        ----------
        is_range: Union[bool, Unset_Type]
            The is_range of this GsaDataExportFloatFunctionalDatum.
        """
        # Field is not nullable
        if is_range is None:
            raise ValueError("Invalid value for 'is_range', must not be 'None'")
        self._is_range = is_range

    @property
    def is_logarithmic(self) -> "Union[bool, Unset_Type]":
        """Gets the is_logarithmic of this GsaDataExportFloatFunctionalDatum.

        Returns
        -------
        Union[bool, Unset_Type]
            The is_logarithmic of this GsaDataExportFloatFunctionalDatum.
        """
        return self._is_logarithmic

    @is_logarithmic.setter
    def is_logarithmic(self, is_logarithmic: "Union[bool, Unset_Type]") -> None:
        """Sets the is_logarithmic of this GsaDataExportFloatFunctionalDatum.

        Parameters
        ----------
        is_logarithmic: Union[bool, Unset_Type]
            The is_logarithmic of this GsaDataExportFloatFunctionalDatum.
        """
        # Field is not nullable
        if is_logarithmic is None:
            raise ValueError("Invalid value for 'is_logarithmic', must not be 'None'")
        self._is_logarithmic = is_logarithmic

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
        if not isinstance(other, GsaDataExportFloatFunctionalDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
