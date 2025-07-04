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

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaUnitUsage(ModelBase):
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
        "attributes": "list[GsaSlimNamedEntity]",
        "constants": "list[GsaSlimNamedEntity]",
        "expressions": "list[GsaSlimNamedEntity]",
        "parameters": "list[GsaSlimNamedEntity]",
        "units": "list[GsaSlimUnit]",
    }

    attribute_map: dict[str, str] = {
        "attributes": "attributes",
        "constants": "constants",
        "expressions": "expressions",
        "parameters": "parameters",
        "units": "units",
    }

    subtype_mapping: dict[str, str] = {
        "attributes": "GsaSlimNamedEntity",
        "parameters": "GsaSlimNamedEntity",
        "constants": "GsaSlimNamedEntity",
        "expressions": "GsaSlimNamedEntity",
        "units": "GsaSlimUnit",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attributes: "list[GsaSlimNamedEntity]",
        constants: "list[GsaSlimNamedEntity]",
        expressions: "list[GsaSlimNamedEntity]",
        parameters: "list[GsaSlimNamedEntity]",
        units: "list[GsaSlimUnit]",
    ) -> None:
        """GsaUnitUsage - a model defined in Swagger

        Parameters
        ----------
        attributes: list[GsaSlimNamedEntity]
        constants: list[GsaSlimNamedEntity]
        expressions: list[GsaSlimNamedEntity]
        parameters: list[GsaSlimNamedEntity]
        units: list[GsaSlimUnit]
        """
        self._attributes: list[GsaSlimNamedEntity]
        self._parameters: list[GsaSlimNamedEntity]
        self._constants: list[GsaSlimNamedEntity]
        self._expressions: list[GsaSlimNamedEntity]
        self._units: list[GsaSlimUnit]

        self.attributes = attributes
        self.parameters = parameters
        self.constants = constants
        self.expressions = expressions
        self.units = units

    @property
    def attributes(self) -> "list[GsaSlimNamedEntity]":
        """Gets the attributes of this GsaUnitUsage.

        Returns
        -------
        list[GsaSlimNamedEntity]
            The attributes of this GsaUnitUsage.
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes: "list[GsaSlimNamedEntity]") -> None:
        """Sets the attributes of this GsaUnitUsage.

        Parameters
        ----------
        attributes: list[GsaSlimNamedEntity]
            The attributes of this GsaUnitUsage.
        """
        # Field is not nullable
        if attributes is None:
            raise ValueError("Invalid value for 'attributes', must not be 'None'")
        # Field is required
        if attributes is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'attributes', must not be 'Unset'")
        self._attributes = attributes

    @property
    def parameters(self) -> "list[GsaSlimNamedEntity]":
        """Gets the parameters of this GsaUnitUsage.

        Returns
        -------
        list[GsaSlimNamedEntity]
            The parameters of this GsaUnitUsage.
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters: "list[GsaSlimNamedEntity]") -> None:
        """Sets the parameters of this GsaUnitUsage.

        Parameters
        ----------
        parameters: list[GsaSlimNamedEntity]
            The parameters of this GsaUnitUsage.
        """
        # Field is not nullable
        if parameters is None:
            raise ValueError("Invalid value for 'parameters', must not be 'None'")
        # Field is required
        if parameters is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'parameters', must not be 'Unset'")
        self._parameters = parameters

    @property
    def constants(self) -> "list[GsaSlimNamedEntity]":
        """Gets the constants of this GsaUnitUsage.

        Returns
        -------
        list[GsaSlimNamedEntity]
            The constants of this GsaUnitUsage.
        """
        return self._constants

    @constants.setter
    def constants(self, constants: "list[GsaSlimNamedEntity]") -> None:
        """Sets the constants of this GsaUnitUsage.

        Parameters
        ----------
        constants: list[GsaSlimNamedEntity]
            The constants of this GsaUnitUsage.
        """
        # Field is not nullable
        if constants is None:
            raise ValueError("Invalid value for 'constants', must not be 'None'")
        # Field is required
        if constants is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'constants', must not be 'Unset'")
        self._constants = constants

    @property
    def expressions(self) -> "list[GsaSlimNamedEntity]":
        """Gets the expressions of this GsaUnitUsage.

        Returns
        -------
        list[GsaSlimNamedEntity]
            The expressions of this GsaUnitUsage.
        """
        return self._expressions

    @expressions.setter
    def expressions(self, expressions: "list[GsaSlimNamedEntity]") -> None:
        """Sets the expressions of this GsaUnitUsage.

        Parameters
        ----------
        expressions: list[GsaSlimNamedEntity]
            The expressions of this GsaUnitUsage.
        """
        # Field is not nullable
        if expressions is None:
            raise ValueError("Invalid value for 'expressions', must not be 'None'")
        # Field is required
        if expressions is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'expressions', must not be 'Unset'")
        self._expressions = expressions

    @property
    def units(self) -> "list[GsaSlimUnit]":
        """Gets the units of this GsaUnitUsage.

        Returns
        -------
        list[GsaSlimUnit]
            The units of this GsaUnitUsage.
        """
        return self._units

    @units.setter
    def units(self, units: "list[GsaSlimUnit]") -> None:
        """Sets the units of this GsaUnitUsage.

        Parameters
        ----------
        units: list[GsaSlimUnit]
            The units of this GsaUnitUsage.
        """
        # Field is not nullable
        if units is None:
            raise ValueError("Invalid value for 'units', must not be 'None'")
        # Field is required
        if units is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'units', must not be 'Unset'")
        self._units = units

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
        if not isinstance(other, GsaUnitUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
