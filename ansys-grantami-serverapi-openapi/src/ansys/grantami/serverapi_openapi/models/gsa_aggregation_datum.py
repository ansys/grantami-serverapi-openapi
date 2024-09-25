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

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaAggregationDatum(ModelBase):
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
        "datum_type": "GsaAggregationDatumType",
    }

    attribute_map: Dict[str, str] = {
        "datum_type": "datumType",
    }

    subtype_mapping: Dict[str, str] = {
        "datumType": "GsaAggregationDatumType",
    }

    discriminator_value_class_map = {
        "integer".lower(): "#/components/schemas/GsaIntegerAggregation",
        "point".lower(): "#/components/schemas/GsaPointAggregation",
        "range".lower(): "#/components/schemas/GsaRangeAggregation",
        "integerHistogram".lower(): "#/components/schemas/GsaIntegerHistogramAggregation",
        "pointHistogram".lower(): "#/components/schemas/GsaPointHistogramAggregation",
        "rangeHistogram".lower(): "#/components/schemas/GsaRangeHistogramAggregation",
        "dateTime".lower(): "#/components/schemas/GsaDateTimeAggregation",
        "dateTimeHistogram".lower(): "#/components/schemas/GsaDateTimeHistogramAggregation",
        "shortText".lower(): "#/components/schemas/GsaShortTextAggregation",
        "discreteText".lower(): "#/components/schemas/GsaDiscreteTextAggregation",
        "link".lower(): "#/components/schemas/GsaLinkAggregation",
        "logical".lower(): "#/components/schemas/GsaLogicalAggregation",
        "floatFunctionalGraph".lower(): "#/components/schemas/GsaFloatFunctionalAggregation",
    }

    discriminator: Optional[str] = "datumType"

    def __init__(
        self,
        *,
        datum_type: "GsaAggregationDatumType",
    ) -> None:
        """GsaAggregationDatum - a model defined in Swagger

        Parameters
        ----------
        datum_type: GsaAggregationDatumType
        """
        self._datum_type: GsaAggregationDatumType

        self.datum_type = datum_type

    @property
    def datum_type(self) -> "GsaAggregationDatumType":
        """Gets the datum_type of this GsaAggregationDatum.

        Returns
        -------
        GsaAggregationDatumType
            The datum_type of this GsaAggregationDatum.
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type: "GsaAggregationDatumType") -> None:
        """Sets the datum_type of this GsaAggregationDatum.

        Parameters
        ----------
        datum_type: GsaAggregationDatumType
            The datum_type of this GsaAggregationDatum.
        """
        # Field is not nullable
        if datum_type is None:
            raise ValueError("Invalid value for 'datum_type', must not be 'None'")
        # Field is required
        if datum_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'datum_type', must not be 'Unset'")
        self._datum_type = datum_type

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
        if not isinstance(other, GsaAggregationDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other