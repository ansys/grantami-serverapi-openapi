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

from ansys.grantami.serverapi_openapi.v2024r2.models.granta_server_api_data_export_datums_float_functional_datum import (  # noqa: F401
    GrantaServerApiDataExportDatumsFloatFunctionalDatum,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiDataExportDatumsFunctionalGridDatum(
    GrantaServerApiDataExportDatumsFloatFunctionalDatum
):
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
        "attribute_guid": "str",
        "attribute_identity": "int",
        "datum_type": "str",
        "graph_type": "str",
        "is_estimated": "bool",
        "is_range": "bool",
        "meta_datums": "list[GrantaServerApiDataExportDatumsDatum]",
        "not_applicable": "str",
        "parameters": "list[GrantaServerApiFunctionalDatumParameterInfo]",
        "points": "list[GrantaServerApiDataExportDatumsGridPoint]",
        "unit_symbol": "str",
        "x_axis_parameter": "GrantaServerApiFunctionalDatumParameterInfo",
    }

    attribute_map: dict[str, str] = {
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "datum_type": "datumType",
        "graph_type": "graphType",
        "is_estimated": "isEstimated",
        "is_range": "isRange",
        "meta_datums": "metaDatums",
        "not_applicable": "notApplicable",
        "parameters": "parameters",
        "points": "points",
        "unit_symbol": "unitSymbol",
        "x_axis_parameter": "xAxisParameter",
    }

    subtype_mapping: dict[str, str] = {
        "points": "GrantaServerApiDataExportDatumsGridPoint",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_guid: "str | Unset_Type" = Unset,
        attribute_identity: "int | Unset_Type" = Unset,
        datum_type: "str" = "floatFunctional",
        graph_type: "str" = "grid",
        is_estimated: "bool | Unset_Type" = Unset,
        is_range: "bool | Unset_Type" = Unset,
        meta_datums: "list[GrantaServerApiDataExportDatumsDatum] | None | Unset_Type" = Unset,
        not_applicable: "str" = "applicable",
        parameters: "list[GrantaServerApiFunctionalDatumParameterInfo] | None | Unset_Type" = Unset,
        points: "list[GrantaServerApiDataExportDatumsGridPoint] | None | Unset_Type" = Unset,
        unit_symbol: "str | None | Unset_Type" = Unset,
        x_axis_parameter: "GrantaServerApiFunctionalDatumParameterInfo | Unset_Type" = Unset,
    ) -> None:
        """GrantaServerApiDataExportDatumsFunctionalGridDatum - a model defined in Swagger

        Parameters
        ----------
        attribute_guid: str, optional
        attribute_identity: int, optional
        datum_type: str
        graph_type: str
        is_estimated: bool, optional
        is_range: bool, optional
        meta_datums: list[GrantaServerApiDataExportDatumsDatum] | None, optional
        not_applicable: str
        parameters: list[GrantaServerApiFunctionalDatumParameterInfo] | None, optional
        points: list[GrantaServerApiDataExportDatumsGridPoint] | None, optional
        unit_symbol: str | None, optional
        x_axis_parameter: GrantaServerApiFunctionalDatumParameterInfo, optional
        """
        super().__init__(
            attribute_guid=attribute_guid,
            attribute_identity=attribute_identity,
            datum_type=datum_type,
            is_estimated=is_estimated,
            is_range=is_range,
            meta_datums=meta_datums,
            not_applicable=not_applicable,
            parameters=parameters,
            unit_symbol=unit_symbol,
            x_axis_parameter=x_axis_parameter,
        )
        self._graph_type: str
        self._points: list[GrantaServerApiDataExportDatumsGridPoint] | None | Unset_Type = Unset

        self.graph_type = graph_type
        if points is not Unset:
            self.points = points

    @property
    def graph_type(self) -> "str":
        """Gets the graph_type of this GrantaServerApiDataExportDatumsFunctionalGridDatum.

        Returns
        -------
        str
            The graph_type of this GrantaServerApiDataExportDatumsFunctionalGridDatum.
        """
        return self._graph_type

    @graph_type.setter
    def graph_type(self, graph_type: "str") -> None:
        """Sets the graph_type of this GrantaServerApiDataExportDatumsFunctionalGridDatum.

        Parameters
        ----------
        graph_type: str
            The graph_type of this GrantaServerApiDataExportDatumsFunctionalGridDatum.
        """
        # Field is not nullable
        if graph_type is None:
            raise ValueError("Invalid value for 'graph_type', must not be 'None'")
        # Field is required
        if graph_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'graph_type', must not be 'Unset'")
        self._graph_type = graph_type

    @property
    def points(self) -> "list[GrantaServerApiDataExportDatumsGridPoint] | None | Unset_Type":
        """Gets the points of this GrantaServerApiDataExportDatumsFunctionalGridDatum.

        Returns
        -------
        list[GrantaServerApiDataExportDatumsGridPoint] | None | Unset_Type
            The points of this GrantaServerApiDataExportDatumsFunctionalGridDatum.
        """
        return self._points

    @points.setter
    def points(
        self, points: "list[GrantaServerApiDataExportDatumsGridPoint] | None | Unset_Type"
    ) -> None:
        """Sets the points of this GrantaServerApiDataExportDatumsFunctionalGridDatum.

        Parameters
        ----------
        points: list[GrantaServerApiDataExportDatumsGridPoint] | None | Unset_Type
            The points of this GrantaServerApiDataExportDatumsFunctionalGridDatum.
        """
        self._points = points

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
        if not isinstance(other, GrantaServerApiDataExportDatumsFunctionalGridDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
