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

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaUnitEquivalent(ModelBase):
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
        "equivalent_unit": "GsaUnit",
        "unit": "GsaUnit",
        "unit_system": "GsaUnitSystem",
    }

    attribute_map: dict[str, str] = {
        "equivalent_unit": "equivalentUnit",
        "unit": "unit",
        "unit_system": "unitSystem",
    }

    subtype_mapping: dict[str, str] = {
        "unit": "GsaUnit",
        "unitSystem": "GsaUnitSystem",
        "equivalentUnit": "GsaUnit",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        equivalent_unit: "GsaUnit",
        unit: "GsaUnit",
        unit_system: "GsaUnitSystem",
    ) -> None:
        """GsaUnitEquivalent - a model defined in Swagger

        Parameters
        ----------
        equivalent_unit: GsaUnit
        unit: GsaUnit
        unit_system: GsaUnitSystem
        """
        self._unit: GsaUnit
        self._unit_system: GsaUnitSystem
        self._equivalent_unit: GsaUnit

        self.unit = unit
        self.unit_system = unit_system
        self.equivalent_unit = equivalent_unit

    @property
    def unit(self) -> "GsaUnit":
        """Gets the unit of this GsaUnitEquivalent.

        Returns
        -------
        GsaUnit
            The unit of this GsaUnitEquivalent.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "GsaUnit") -> None:
        """Sets the unit of this GsaUnitEquivalent.

        Parameters
        ----------
        unit: GsaUnit
            The unit of this GsaUnitEquivalent.
        """
        # Field is not nullable
        if unit is None:
            raise ValueError("Invalid value for 'unit', must not be 'None'")
        # Field is required
        if unit is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'unit', must not be 'Unset'")
        self._unit = unit

    @property
    def unit_system(self) -> "GsaUnitSystem":
        """Gets the unit_system of this GsaUnitEquivalent.

        Returns
        -------
        GsaUnitSystem
            The unit_system of this GsaUnitEquivalent.
        """
        return self._unit_system

    @unit_system.setter
    def unit_system(self, unit_system: "GsaUnitSystem") -> None:
        """Sets the unit_system of this GsaUnitEquivalent.

        Parameters
        ----------
        unit_system: GsaUnitSystem
            The unit_system of this GsaUnitEquivalent.
        """
        # Field is not nullable
        if unit_system is None:
            raise ValueError("Invalid value for 'unit_system', must not be 'None'")
        # Field is required
        if unit_system is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'unit_system', must not be 'Unset'")
        self._unit_system = unit_system

    @property
    def equivalent_unit(self) -> "GsaUnit":
        """Gets the equivalent_unit of this GsaUnitEquivalent.

        Returns
        -------
        GsaUnit
            The equivalent_unit of this GsaUnitEquivalent.
        """
        return self._equivalent_unit

    @equivalent_unit.setter
    def equivalent_unit(self, equivalent_unit: "GsaUnit") -> None:
        """Sets the equivalent_unit of this GsaUnitEquivalent.

        Parameters
        ----------
        equivalent_unit: GsaUnit
            The equivalent_unit of this GsaUnitEquivalent.
        """
        # Field is not nullable
        if equivalent_unit is None:
            raise ValueError("Invalid value for 'equivalent_unit', must not be 'None'")
        # Field is required
        if equivalent_unit is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'equivalent_unit', must not be 'Unset'")
        self._equivalent_unit = equivalent_unit

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
        if not isinstance(other, GsaUnitEquivalent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
