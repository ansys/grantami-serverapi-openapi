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

from ansys.grantami.serverapi_openapi.models.gsa_attribute_type import GsaAttributeType
from ansys.grantami.serverapi_openapi.models.gsa_data_export_applicable_datum import (  # noqa: F401
    GsaDataExportApplicableDatum,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaDataExportRangeDatum(GsaDataExportApplicableDatum):
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
        "datum_type": "GsaAttributeType",
        "not_applicable": "str",
        "datum_value": "GsaDataExportRange",
        "is_estimated": "bool",
        "meta_datums": "list[GsaDataExportDatum]",
        "unit": "str",
    }

    attribute_map: dict[str, str] = {
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "datum_type": "datumType",
        "not_applicable": "notApplicable",
        "datum_value": "datumValue",
        "is_estimated": "isEstimated",
        "meta_datums": "metaDatums",
        "unit": "unit",
    }

    subtype_mapping: dict[str, str] = {
        "datumValue": "GsaDataExportRange",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_guid: "str",
        attribute_identity: "int",
        datum_type: "GsaAttributeType" = GsaAttributeType.RANGE,
        not_applicable: "str" = "applicable",
        datum_value: "Union[GsaDataExportRange, Unset_Type]" = Unset,
        is_estimated: "Union[bool, Unset_Type]" = Unset,
        meta_datums: "Union[list[GsaDataExportDatum], None, Unset_Type]" = Unset,
        unit: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaDataExportRangeDatum - a model defined in Swagger

        Parameters
        ----------
        attribute_guid: str
        attribute_identity: int
        datum_type: GsaAttributeType
        not_applicable: str
        datum_value: GsaDataExportRange, optional
        is_estimated: bool, optional
        meta_datums: list[GsaDataExportDatum], optional
        unit: str, optional
        """
        super().__init__(
            attribute_guid=attribute_guid,
            attribute_identity=attribute_identity,
            datum_type=datum_type,
            not_applicable=not_applicable,
            meta_datums=meta_datums,
        )
        self._datum_value: Union[GsaDataExportRange, Unset_Type] = Unset
        self._is_estimated: Union[bool, Unset_Type] = Unset
        self._unit: Union[str, None, Unset_Type] = Unset

        if datum_value is not Unset:
            self.datum_value = datum_value
        if is_estimated is not Unset:
            self.is_estimated = is_estimated
        if unit is not Unset:
            self.unit = unit

    @property
    def datum_value(self) -> "Union[GsaDataExportRange, Unset_Type]":
        """Gets the datum_value of this GsaDataExportRangeDatum.

        Returns
        -------
        Union[GsaDataExportRange, Unset_Type]
            The datum_value of this GsaDataExportRangeDatum.
        """
        return self._datum_value

    @datum_value.setter
    def datum_value(self, datum_value: "Union[GsaDataExportRange, Unset_Type]") -> None:
        """Sets the datum_value of this GsaDataExportRangeDatum.

        Parameters
        ----------
        datum_value: Union[GsaDataExportRange, Unset_Type]
            The datum_value of this GsaDataExportRangeDatum.
        """
        # Field is not nullable
        if datum_value is None:
            raise ValueError("Invalid value for 'datum_value', must not be 'None'")
        self._datum_value = datum_value

    @property
    def is_estimated(self) -> "Union[bool, Unset_Type]":
        """Gets the is_estimated of this GsaDataExportRangeDatum.

        Returns
        -------
        Union[bool, Unset_Type]
            The is_estimated of this GsaDataExportRangeDatum.
        """
        return self._is_estimated

    @is_estimated.setter
    def is_estimated(self, is_estimated: "Union[bool, Unset_Type]") -> None:
        """Sets the is_estimated of this GsaDataExportRangeDatum.

        Parameters
        ----------
        is_estimated: Union[bool, Unset_Type]
            The is_estimated of this GsaDataExportRangeDatum.
        """
        # Field is not nullable
        if is_estimated is None:
            raise ValueError("Invalid value for 'is_estimated', must not be 'None'")
        self._is_estimated = is_estimated

    @property
    def unit(self) -> "Union[str, None, Unset_Type]":
        """Gets the unit of this GsaDataExportRangeDatum.

        Returns
        -------
        Union[str, None, Unset_Type]
            The unit of this GsaDataExportRangeDatum.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "Union[str, None, Unset_Type]") -> None:
        """Sets the unit of this GsaDataExportRangeDatum.

        Parameters
        ----------
        unit: Union[str, None, Unset_Type]
            The unit of this GsaDataExportRangeDatum.
        """
        self._unit = unit

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
        if not isinstance(other, GsaDataExportRangeDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
