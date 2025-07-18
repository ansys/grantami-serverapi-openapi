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

from ansys.grantami.serverapi_openapi.v2025r2.models.gsa_datum_rollup import (  # noqa: F401
    GsaDatumRollup,
)
from ansys.grantami.serverapi_openapi.v2025r2.models.gsa_datum_rollup_type import GsaDatumRollupType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaDatumDoubleRollup(GsaDatumRollup):
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
        "type": "GsaDatumRollupType",
        "value": "float",
        "unit": "GsaSlimUnit",
    }

    attribute_map: dict[str, str] = {
        "type": "type",
        "value": "value",
        "unit": "unit",
    }

    subtype_mapping: dict[str, str] = {
        "unit": "GsaSlimUnit",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        type: "GsaDatumRollupType" = GsaDatumRollupType.DOUBLE,
        value: "float",
        unit: "GsaSlimUnit | Unset_Type" = Unset,
    ) -> None:
        """GsaDatumDoubleRollup - a model defined in Swagger

        Parameters
        ----------
        type: GsaDatumRollupType
        value: float
        unit: GsaSlimUnit, optional
        """
        super().__init__(type=type)
        self._value: float
        self._unit: GsaSlimUnit | Unset_Type = Unset

        self.value = value
        if unit is not Unset:
            self.unit = unit

    @property
    def value(self) -> "float":
        """Gets the value of this GsaDatumDoubleRollup.

        Returns
        -------
        float
            The value of this GsaDatumDoubleRollup.
        """
        return self._value

    @value.setter
    def value(self, value: "float") -> None:
        """Sets the value of this GsaDatumDoubleRollup.

        Parameters
        ----------
        value: float
            The value of this GsaDatumDoubleRollup.
        """
        # Field is not nullable
        if value is None:
            raise ValueError("Invalid value for 'value', must not be 'None'")
        # Field is required
        if value is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'value', must not be 'Unset'")
        self._value = value

    @property
    def unit(self) -> "GsaSlimUnit | Unset_Type":
        """Gets the unit of this GsaDatumDoubleRollup.

        Returns
        -------
        GsaSlimUnit | Unset_Type
            The unit of this GsaDatumDoubleRollup.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "GsaSlimUnit | Unset_Type") -> None:
        """Sets the unit of this GsaDatumDoubleRollup.

        Parameters
        ----------
        unit: GsaSlimUnit | Unset_Type
            The unit of this GsaDatumDoubleRollup.
        """
        # Field is not nullable
        if unit is None:
            raise ValueError("Invalid value for 'unit', must not be 'None'")
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
        if not isinstance(other, GsaDatumDoubleRollup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
