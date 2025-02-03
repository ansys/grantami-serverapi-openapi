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

from ansys.grantami.serverapi_openapi.models.gsa_applicable_datum import (  # noqa: F401
    GsaApplicableDatum,
)
from ansys.grantami.serverapi_openapi.models.gsa_datum_type import GsaDatumType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaTabularDatum(GsaApplicableDatum):
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
        "datum_type": "GsaDatumType",
        "not_applicable": "str",
        "rows": "list[GsaTabularDatumRow]",
        "summary_row": "GsaTabularDatumSummaryRow",
    }

    attribute_map: dict[str, str] = {
        "datum_type": "datumType",
        "not_applicable": "notApplicable",
        "rows": "rows",
        "summary_row": "summaryRow",
    }

    subtype_mapping: dict[str, str] = {
        "rows": "GsaTabularDatumRow",
        "summaryRow": "GsaTabularDatumSummaryRow",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        datum_type: "GsaDatumType" = GsaDatumType.TABULAR,
        not_applicable: "str" = "applicable",
        rows: "list[GsaTabularDatumRow]",
        summary_row: "Union[GsaTabularDatumSummaryRow, Unset_Type]" = Unset,
    ) -> None:
        """GsaTabularDatum - a model defined in Swagger

        Parameters
        ----------
        datum_type: GsaDatumType
        not_applicable: str
        rows: list[GsaTabularDatumRow]
        summary_row: GsaTabularDatumSummaryRow, optional
        """
        super().__init__(datum_type=datum_type, not_applicable=not_applicable)
        self._rows: list[GsaTabularDatumRow]
        self._summary_row: Union[GsaTabularDatumSummaryRow, Unset_Type] = Unset

        self.rows = rows
        if summary_row is not Unset:
            self.summary_row = summary_row

    @property
    def rows(self) -> "list[GsaTabularDatumRow]":
        """Gets the rows of this GsaTabularDatum.

        Returns
        -------
        list[GsaTabularDatumRow]
            The rows of this GsaTabularDatum.
        """
        return self._rows

    @rows.setter
    def rows(self, rows: "list[GsaTabularDatumRow]") -> None:
        """Sets the rows of this GsaTabularDatum.

        Parameters
        ----------
        rows: list[GsaTabularDatumRow]
            The rows of this GsaTabularDatum.
        """
        # Field is not nullable
        if rows is None:
            raise ValueError("Invalid value for 'rows', must not be 'None'")
        # Field is required
        if rows is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'rows', must not be 'Unset'")
        self._rows = rows

    @property
    def summary_row(self) -> "Union[GsaTabularDatumSummaryRow, Unset_Type]":
        """Gets the summary_row of this GsaTabularDatum.

        Returns
        -------
        Union[GsaTabularDatumSummaryRow, Unset_Type]
            The summary_row of this GsaTabularDatum.
        """
        return self._summary_row

    @summary_row.setter
    def summary_row(self, summary_row: "Union[GsaTabularDatumSummaryRow, Unset_Type]") -> None:
        """Sets the summary_row of this GsaTabularDatum.

        Parameters
        ----------
        summary_row: Union[GsaTabularDatumSummaryRow, Unset_Type]
            The summary_row of this GsaTabularDatum.
        """
        # Field is not nullable
        if summary_row is None:
            raise ValueError("Invalid value for 'summary_row', must not be 'None'")
        self._summary_row = summary_row

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
        if not isinstance(other, GsaTabularDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
