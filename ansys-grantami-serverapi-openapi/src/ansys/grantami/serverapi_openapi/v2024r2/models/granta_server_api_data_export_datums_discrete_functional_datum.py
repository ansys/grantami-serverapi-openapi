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

from ansys.grantami.serverapi_openapi.v2024r2.models.granta_server_api_data_export_datums_applicable_datum import (  # noqa: F401
    GrantaServerApiDataExportDatumsApplicableDatum,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiDataExportDatumsDiscreteFunctionalDatum(
    GrantaServerApiDataExportDatumsApplicableDatum
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
    discriminator_class_map: dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "attribute_guid": "str",
        "attribute_identity": "int",
        "datum_type": "str",
        "meta_datums": "list[GrantaServerApiDataExportDatumsDatum]",
        "not_applicable": "str",
        "parameters": "list[GrantaServerApiFunctionalDatumParameterInfo]",
        "x_axis_parameter": "GrantaServerApiFunctionalDatumParameterInfo",
    }

    attribute_map: dict[str, str] = {
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "datum_type": "datumType",
        "meta_datums": "metaDatums",
        "not_applicable": "notApplicable",
        "parameters": "parameters",
        "x_axis_parameter": "xAxisParameter",
    }

    subtype_mapping: dict[str, str] = {
        "xAxisParameter": "GrantaServerApiFunctionalDatumParameterInfo",
        "parameters": "GrantaServerApiFunctionalDatumParameterInfo",
    }

    discriminator_value_class_map = {
        "grid".lower(): "#/components/schemas/GrantaServerApiDataExportDatumsDiscreteFunctionalGridDatum",
        "series".lower(): "#/components/schemas/GrantaServerApiDataExportDatumsDiscreteFunctionalSeriesDatum",
    }

    discriminator: Optional[str] = "graph_type"

    def __init__(
        self,
        *,
        attribute_guid: "str | Unset_Type" = Unset,
        attribute_identity: "int | Unset_Type" = Unset,
        datum_type: "str" = "discreteFunctional",
        meta_datums: "list[GrantaServerApiDataExportDatumsDatum] | None | Unset_Type" = Unset,
        not_applicable: "str" = "applicable",
        parameters: "list[GrantaServerApiFunctionalDatumParameterInfo] | None | Unset_Type" = Unset,
        x_axis_parameter: "GrantaServerApiFunctionalDatumParameterInfo | Unset_Type" = Unset,
    ) -> None:
        """GrantaServerApiDataExportDatumsDiscreteFunctionalDatum - a model defined in Swagger

        Parameters
        ----------
        attribute_guid: str, optional
        attribute_identity: int, optional
        datum_type: str
        meta_datums: list[GrantaServerApiDataExportDatumsDatum] | None, optional
        not_applicable: str
        parameters: list[GrantaServerApiFunctionalDatumParameterInfo] | None, optional
        x_axis_parameter: GrantaServerApiFunctionalDatumParameterInfo, optional
        """
        super().__init__(
            attribute_guid=attribute_guid,
            attribute_identity=attribute_identity,
            meta_datums=meta_datums,
            not_applicable=not_applicable,
        )
        self._datum_type: str
        self._x_axis_parameter: GrantaServerApiFunctionalDatumParameterInfo | Unset_Type = Unset
        self._parameters: list[GrantaServerApiFunctionalDatumParameterInfo] | None | Unset_Type = (
            Unset
        )

        self.datum_type = datum_type
        if x_axis_parameter is not Unset:
            self.x_axis_parameter = x_axis_parameter
        if parameters is not Unset:
            self.parameters = parameters

    @property
    def datum_type(self) -> "str":
        """Gets the datum_type of this GrantaServerApiDataExportDatumsDiscreteFunctionalDatum.

        Returns
        -------
        str
            The datum_type of this GrantaServerApiDataExportDatumsDiscreteFunctionalDatum.
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type: "str") -> None:
        """Sets the datum_type of this GrantaServerApiDataExportDatumsDiscreteFunctionalDatum.

        Parameters
        ----------
        datum_type: str
            The datum_type of this GrantaServerApiDataExportDatumsDiscreteFunctionalDatum.
        """
        # Field is not nullable
        if datum_type is None:
            raise ValueError("Invalid value for 'datum_type', must not be 'None'")
        # Field is required
        if datum_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'datum_type', must not be 'Unset'")
        self._datum_type = datum_type

    @property
    def x_axis_parameter(self) -> "GrantaServerApiFunctionalDatumParameterInfo | Unset_Type":
        """Gets the x_axis_parameter of this GrantaServerApiDataExportDatumsDiscreteFunctionalDatum.

        Returns
        -------
        GrantaServerApiFunctionalDatumParameterInfo | Unset_Type
            The x_axis_parameter of this GrantaServerApiDataExportDatumsDiscreteFunctionalDatum.
        """
        return self._x_axis_parameter

    @x_axis_parameter.setter
    def x_axis_parameter(
        self, x_axis_parameter: "GrantaServerApiFunctionalDatumParameterInfo | Unset_Type"
    ) -> None:
        """Sets the x_axis_parameter of this GrantaServerApiDataExportDatumsDiscreteFunctionalDatum.

        Parameters
        ----------
        x_axis_parameter: GrantaServerApiFunctionalDatumParameterInfo | Unset_Type
            The x_axis_parameter of this GrantaServerApiDataExportDatumsDiscreteFunctionalDatum.
        """
        # Field is not nullable
        if x_axis_parameter is None:
            raise ValueError("Invalid value for 'x_axis_parameter', must not be 'None'")
        self._x_axis_parameter = x_axis_parameter

    @property
    def parameters(self) -> "list[GrantaServerApiFunctionalDatumParameterInfo] | None | Unset_Type":
        """Gets the parameters of this GrantaServerApiDataExportDatumsDiscreteFunctionalDatum.

        Returns
        -------
        list[GrantaServerApiFunctionalDatumParameterInfo] | None | Unset_Type
            The parameters of this GrantaServerApiDataExportDatumsDiscreteFunctionalDatum.
        """
        return self._parameters

    @parameters.setter
    def parameters(
        self, parameters: "list[GrantaServerApiFunctionalDatumParameterInfo] | None | Unset_Type"
    ) -> None:
        """Sets the parameters of this GrantaServerApiDataExportDatumsDiscreteFunctionalDatum.

        Parameters
        ----------
        parameters: list[GrantaServerApiFunctionalDatumParameterInfo] | None | Unset_Type
            The parameters of this GrantaServerApiDataExportDatumsDiscreteFunctionalDatum.
        """
        self._parameters = parameters

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
        if not isinstance(other, GrantaServerApiDataExportDatumsDiscreteFunctionalDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
