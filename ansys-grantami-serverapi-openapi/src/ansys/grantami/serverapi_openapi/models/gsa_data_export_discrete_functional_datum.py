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

from ansys.grantami.serverapi_openapi.models.gsa_attribute_type import GsaAttributeType
from ansys.grantami.serverapi_openapi.models.gsa_data_export_applicable_datum import (  # noqa: F401
    GsaDataExportApplicableDatum,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaDataExportDiscreteFunctionalDatum(GsaDataExportApplicableDatum):
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
    discriminator_class_map: Dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: Dict[str, str] = {
        "datum_type": "GsaAttributeType",
        "graph_type": "str",
        "not_applicable": "str",
        "attribute_guid": "str",
        "attribute_identity": "int",
        "meta_datums": "list[GsaDataExportDatum]",
        "parameters": "list[GsaFunctionalDatumParameterInfo]",
        "x_axis_parameter": "GsaFunctionalDatumParameterInfo",
    }

    attribute_map: Dict[str, str] = {
        "datum_type": "datumType",
        "graph_type": "graphType",
        "not_applicable": "notApplicable",
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "meta_datums": "metaDatums",
        "parameters": "parameters",
        "x_axis_parameter": "xAxisParameter",
    }

    subtype_mapping: Dict[str, str] = {
        "xAxisParameter": "GsaFunctionalDatumParameterInfo",
        "parameters": "GsaFunctionalDatumParameterInfo",
    }

    discriminator_value_class_map = {
        "grid".lower(): "#/components/schemas/GsaDataExportDiscreteFunctionalGridDatum",
        "series".lower(): "#/components/schemas/GsaDataExportDiscreteFunctionalSeriesDatum",
    }

    discriminator: Optional[str] = "graph_type"

    def __init__(
        self,
        *,
        datum_type: "GsaAttributeType" = GsaAttributeType.DISCRETEFUNCTIONAL,
        graph_type: "str",
        not_applicable: "str" = "applicable",
        attribute_guid: "Union[str, Unset_Type]" = Unset,
        attribute_identity: "Union[int, Unset_Type]" = Unset,
        meta_datums: "Union[List[GsaDataExportDatum], None, Unset_Type]" = Unset,
        parameters: "Union[List[GsaFunctionalDatumParameterInfo], None, Unset_Type]" = Unset,
        x_axis_parameter: "Union[GsaFunctionalDatumParameterInfo, Unset_Type]" = Unset,
    ) -> None:
        """GsaDataExportDiscreteFunctionalDatum - a model defined in Swagger

        Parameters
        ----------
        datum_type: GsaAttributeType
        graph_type: str
        not_applicable: str
        attribute_guid: str, optional
        attribute_identity: int, optional
        meta_datums: List[GsaDataExportDatum], optional
        parameters: List[GsaFunctionalDatumParameterInfo], optional
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
        self._x_axis_parameter: Union[GsaFunctionalDatumParameterInfo, Unset_Type] = Unset
        self._parameters: Union[List[GsaFunctionalDatumParameterInfo], None, Unset_Type] = Unset

        self.graph_type = graph_type
        if x_axis_parameter is not Unset:
            self.x_axis_parameter = x_axis_parameter
        if parameters is not Unset:
            self.parameters = parameters

    @property
    def graph_type(self) -> "str":
        """Gets the graph_type of this GsaDataExportDiscreteFunctionalDatum.

        Returns
        -------
        str
            The graph_type of this GsaDataExportDiscreteFunctionalDatum.
        """
        return self._graph_type

    @graph_type.setter
    def graph_type(self, graph_type: "str") -> None:
        """Sets the graph_type of this GsaDataExportDiscreteFunctionalDatum.

        Parameters
        ----------
        graph_type: str
            The graph_type of this GsaDataExportDiscreteFunctionalDatum.
        """
        # Field is required
        if graph_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'graph_type', must not be 'Unset'")
        self._graph_type = graph_type

    @property
    def x_axis_parameter(self) -> "Union[GsaFunctionalDatumParameterInfo, Unset_Type]":
        """Gets the x_axis_parameter of this GsaDataExportDiscreteFunctionalDatum.

        Returns
        -------
        Union[GsaFunctionalDatumParameterInfo, Unset_Type]
            The x_axis_parameter of this GsaDataExportDiscreteFunctionalDatum.
        """
        return self._x_axis_parameter

    @x_axis_parameter.setter
    def x_axis_parameter(
        self, x_axis_parameter: "Union[GsaFunctionalDatumParameterInfo, Unset_Type]"
    ) -> None:
        """Sets the x_axis_parameter of this GsaDataExportDiscreteFunctionalDatum.

        Parameters
        ----------
        x_axis_parameter: Union[GsaFunctionalDatumParameterInfo, Unset_Type]
            The x_axis_parameter of this GsaDataExportDiscreteFunctionalDatum.
        """
        # Field is not nullable
        if x_axis_parameter is None:
            raise ValueError("Invalid value for 'x_axis_parameter', must not be 'None'")
        self._x_axis_parameter = x_axis_parameter

    @property
    def parameters(self) -> "Union[List[GsaFunctionalDatumParameterInfo], None, Unset_Type]":
        """Gets the parameters of this GsaDataExportDiscreteFunctionalDatum.

        Returns
        -------
        Union[List[GsaFunctionalDatumParameterInfo], None, Unset_Type]
            The parameters of this GsaDataExportDiscreteFunctionalDatum.
        """
        return self._parameters

    @parameters.setter
    def parameters(
        self, parameters: "Union[List[GsaFunctionalDatumParameterInfo], None, Unset_Type]"
    ) -> None:
        """Sets the parameters of this GsaDataExportDiscreteFunctionalDatum.

        Parameters
        ----------
        parameters: Union[List[GsaFunctionalDatumParameterInfo], None, Unset_Type]
            The parameters of this GsaDataExportDiscreteFunctionalDatum.
        """
        self._parameters = parameters

    @classmethod
    def get_real_child_model(cls, data: Dict[str, str]) -> str:
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
        if not isinstance(other, GsaDataExportDiscreteFunctionalDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other