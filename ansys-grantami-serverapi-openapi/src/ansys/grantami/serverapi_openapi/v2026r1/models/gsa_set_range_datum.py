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

from ansys.grantami.serverapi_openapi.v2026r1.models.gsa_set_datum import GsaSetDatum  # noqa: F401
from ansys.grantami.serverapi_openapi.v2026r1.models.gsa_set_datum_type import GsaSetDatumType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaSetRangeDatum(GsaSetDatum):
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
        "high_value": "float",
        "high_value_is_inclusive": "bool",
        "low_value": "float",
        "low_value_is_inclusive": "bool",
        "set_datum_type": "GsaSetDatumType",
    }

    attribute_map: dict[str, str] = {
        "estimated": "estimated",
        "high_value": "highValue",
        "high_value_is_inclusive": "highValueIsInclusive",
        "low_value": "lowValue",
        "low_value_is_inclusive": "lowValueIsInclusive",
        "set_datum_type": "setDatumType",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        estimated: "bool",
        high_value: "float",
        high_value_is_inclusive: "bool",
        low_value: "float",
        low_value_is_inclusive: "bool",
        set_datum_type: "GsaSetDatumType" = GsaSetDatumType.RANGE,
    ) -> None:
        """GsaSetRangeDatum - a model defined in Swagger

        Parameters
        ----------
        estimated: bool
        high_value: float
        high_value_is_inclusive: bool
        low_value: float
        low_value_is_inclusive: bool
        set_datum_type: GsaSetDatumType
        """
        super().__init__(set_datum_type=set_datum_type)
        self._low_value: float
        self._high_value: float
        self._low_value_is_inclusive: bool
        self._high_value_is_inclusive: bool
        self._estimated: bool

        self.low_value = low_value
        self.high_value = high_value
        self.low_value_is_inclusive = low_value_is_inclusive
        self.high_value_is_inclusive = high_value_is_inclusive
        self.estimated = estimated

    @property
    def low_value(self) -> "float":
        """Gets the low_value of this GsaSetRangeDatum.

        Returns
        -------
        float
            The low_value of this GsaSetRangeDatum.
        """
        return self._low_value

    @low_value.setter
    def low_value(self, low_value: "float") -> None:
        """Sets the low_value of this GsaSetRangeDatum.

        Parameters
        ----------
        low_value: float
            The low_value of this GsaSetRangeDatum.
        """
        # Field is not nullable
        if low_value is None:
            raise ValueError("Invalid value for 'low_value', must not be 'None'")
        # Field is required
        if low_value is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'low_value', must not be 'Unset'")
        self._low_value = low_value

    @property
    def high_value(self) -> "float":
        """Gets the high_value of this GsaSetRangeDatum.

        Returns
        -------
        float
            The high_value of this GsaSetRangeDatum.
        """
        return self._high_value

    @high_value.setter
    def high_value(self, high_value: "float") -> None:
        """Sets the high_value of this GsaSetRangeDatum.

        Parameters
        ----------
        high_value: float
            The high_value of this GsaSetRangeDatum.
        """
        # Field is not nullable
        if high_value is None:
            raise ValueError("Invalid value for 'high_value', must not be 'None'")
        # Field is required
        if high_value is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'high_value', must not be 'Unset'")
        self._high_value = high_value

    @property
    def low_value_is_inclusive(self) -> "bool":
        """Gets the low_value_is_inclusive of this GsaSetRangeDatum.

        Returns
        -------
        bool
            The low_value_is_inclusive of this GsaSetRangeDatum.
        """
        return self._low_value_is_inclusive

    @low_value_is_inclusive.setter
    def low_value_is_inclusive(self, low_value_is_inclusive: "bool") -> None:
        """Sets the low_value_is_inclusive of this GsaSetRangeDatum.

        Parameters
        ----------
        low_value_is_inclusive: bool
            The low_value_is_inclusive of this GsaSetRangeDatum.
        """
        # Field is not nullable
        if low_value_is_inclusive is None:
            raise ValueError("Invalid value for 'low_value_is_inclusive', must not be 'None'")
        # Field is required
        if low_value_is_inclusive is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'low_value_is_inclusive', must not be 'Unset'")
        self._low_value_is_inclusive = low_value_is_inclusive

    @property
    def high_value_is_inclusive(self) -> "bool":
        """Gets the high_value_is_inclusive of this GsaSetRangeDatum.

        Returns
        -------
        bool
            The high_value_is_inclusive of this GsaSetRangeDatum.
        """
        return self._high_value_is_inclusive

    @high_value_is_inclusive.setter
    def high_value_is_inclusive(self, high_value_is_inclusive: "bool") -> None:
        """Sets the high_value_is_inclusive of this GsaSetRangeDatum.

        Parameters
        ----------
        high_value_is_inclusive: bool
            The high_value_is_inclusive of this GsaSetRangeDatum.
        """
        # Field is not nullable
        if high_value_is_inclusive is None:
            raise ValueError("Invalid value for 'high_value_is_inclusive', must not be 'None'")
        # Field is required
        if high_value_is_inclusive is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'high_value_is_inclusive', must not be 'Unset'")
        self._high_value_is_inclusive = high_value_is_inclusive

    @property
    def estimated(self) -> "bool":
        """Gets the estimated of this GsaSetRangeDatum.

        Returns
        -------
        bool
            The estimated of this GsaSetRangeDatum.
        """
        return self._estimated

    @estimated.setter
    def estimated(self, estimated: "bool") -> None:
        """Sets the estimated of this GsaSetRangeDatum.

        Parameters
        ----------
        estimated: bool
            The estimated of this GsaSetRangeDatum.
        """
        # Field is not nullable
        if estimated is None:
            raise ValueError("Invalid value for 'estimated', must not be 'None'")
        # Field is required
        if estimated is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'estimated', must not be 'Unset'")
        self._estimated = estimated

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
        if not isinstance(other, GsaSetRangeDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
