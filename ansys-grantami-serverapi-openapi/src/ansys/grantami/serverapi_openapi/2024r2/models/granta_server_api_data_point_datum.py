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

from ansys.grantami.serverapi_openapi.2024r2.models.granta_server_api_data_applicable_datum import (  # noqa: F401
    GrantaServerApiDataApplicableDatum,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiDataPointDatum(GrantaServerApiDataApplicableDatum):
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
        "estimated": "bool",
        "values": "list[GrantaServerApiDataPointDataValue]",
        "datum_type": "str",
        "not_applicable": "str",
    }

    attribute_map: dict[str, str] = {
        "estimated": "estimated",
        "values": "values",
        "datum_type": "datumType",
        "not_applicable": "notApplicable",
    }

    subtype_mapping: dict[str, str] = {
        "values": "GrantaServerApiDataPointDataValue",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, estimated: "bool", values: "list[GrantaServerApiDataPointDataValue]", datum_type: "str" = 'point', not_applicable: "str" = 'applicable',) -> None:
        """GrantaServerApiDataPointDatum - a model defined in Swagger

        Parameters
        ----------
        estimated: bool
        values: list[GrantaServerApiDataPointDataValue]
        datum_type: str
        not_applicable: str
        """
        super().__init__(not_applicable=not_applicable)
        self._datum_type: str
        self._estimated: bool
        self._values: list[GrantaServerApiDataPointDataValue]

        self.datum_type = datum_type
        self.estimated = estimated
        self.values = values

    @property
    def datum_type(self) -> "str":
        """Gets the datum_type of this GrantaServerApiDataPointDatum.

        Returns
        -------
        str
            The datum_type of this GrantaServerApiDataPointDatum.
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type: "str") -> None:
        """Sets the datum_type of this GrantaServerApiDataPointDatum.

        Parameters
        ----------
        datum_type: str
            The datum_type of this GrantaServerApiDataPointDatum.
        """
        # Field is not nullable
        if datum_type is None:
            raise ValueError("Invalid value for 'datum_type', must not be 'None'")
        # Field is required
        if datum_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'datum_type', must not be 'Unset'")
        self._datum_type = datum_type

    @property
    def estimated(self) -> "bool":
        """Gets the estimated of this GrantaServerApiDataPointDatum.

        Returns
        -------
        bool
            The estimated of this GrantaServerApiDataPointDatum.
        """
        return self._estimated

    @estimated.setter
    def estimated(self, estimated: "bool") -> None:
        """Sets the estimated of this GrantaServerApiDataPointDatum.

        Parameters
        ----------
        estimated: bool
            The estimated of this GrantaServerApiDataPointDatum.
        """
        # Field is not nullable
        if estimated is None:
            raise ValueError("Invalid value for 'estimated', must not be 'None'")
        # Field is required
        if estimated is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'estimated', must not be 'Unset'")
        self._estimated = estimated

    @property
    def values(self) -> "list[GrantaServerApiDataPointDataValue]":
        """Gets the values of this GrantaServerApiDataPointDatum.

        Returns
        -------
        list[GrantaServerApiDataPointDataValue]
            The values of this GrantaServerApiDataPointDatum.
        """
        return self._values

    @values.setter
    def values(self, values: "list[GrantaServerApiDataPointDataValue]") -> None:
        """Sets the values of this GrantaServerApiDataPointDatum.

        Parameters
        ----------
        values: list[GrantaServerApiDataPointDataValue]
            The values of this GrantaServerApiDataPointDatum.
        """
        # Field is not nullable
        if values is None:
            raise ValueError("Invalid value for 'values', must not be 'None'")
        # Field is required
        if values is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'values', must not be 'Unset'")
        self._values = values

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
        if not isinstance(other, GrantaServerApiDataPointDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

