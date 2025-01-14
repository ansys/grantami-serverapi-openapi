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


class GsaExpression(ModelBase):
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
        "attribute_dependencies": "list[GsaSlimAttribute]",
        "constant_dependencies": "list[GsaSlimNamedEntity]",
        "guid": "str",
        "name": "str",
        "parameter_dependencies": "list[GsaSlimNamedEntity]",
        "value": "str",
        "unit": "GsaSlimUnit",
    }

    attribute_map: dict[str, str] = {
        "attribute_dependencies": "attributeDependencies",
        "constant_dependencies": "constantDependencies",
        "guid": "guid",
        "name": "name",
        "parameter_dependencies": "parameterDependencies",
        "value": "value",
        "unit": "unit",
    }

    subtype_mapping: dict[str, str] = {
        "unit": "GsaSlimUnit",
        "attributeDependencies": "GsaSlimAttribute",
        "constantDependencies": "GsaSlimNamedEntity",
        "parameterDependencies": "GsaSlimNamedEntity",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_dependencies: "list[GsaSlimAttribute]",
        constant_dependencies: "list[GsaSlimNamedEntity]",
        guid: "str",
        name: "str",
        parameter_dependencies: "list[GsaSlimNamedEntity]",
        value: "str",
        unit: "Union[GsaSlimUnit, Unset_Type]" = Unset,
    ) -> None:
        """GsaExpression - a model defined in Swagger

        Parameters
        ----------
        attribute_dependencies: list[GsaSlimAttribute]
        constant_dependencies: list[GsaSlimNamedEntity]
        guid: str
        name: str
        parameter_dependencies: list[GsaSlimNamedEntity]
        value: str
        unit: GsaSlimUnit, optional
        """
        self._value: str
        self._unit: Union[GsaSlimUnit, Unset_Type] = Unset
        self._attribute_dependencies: list[GsaSlimAttribute]
        self._constant_dependencies: list[GsaSlimNamedEntity]
        self._parameter_dependencies: list[GsaSlimNamedEntity]
        self._name: str
        self._guid: str

        self.value = value
        if unit is not Unset:
            self.unit = unit
        self.attribute_dependencies = attribute_dependencies
        self.constant_dependencies = constant_dependencies
        self.parameter_dependencies = parameter_dependencies
        self.name = name
        self.guid = guid

    @property
    def value(self) -> "str":
        """Gets the value of this GsaExpression.

        Returns
        -------
        str
            The value of this GsaExpression.
        """
        return self._value

    @value.setter
    def value(self, value: "str") -> None:
        """Sets the value of this GsaExpression.

        Parameters
        ----------
        value: str
            The value of this GsaExpression.
        """
        # Field is not nullable
        if value is None:
            raise ValueError("Invalid value for 'value', must not be 'None'")
        # Field is required
        if value is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'value', must not be 'Unset'")
        self._value = value

    @property
    def unit(self) -> "Union[GsaSlimUnit, Unset_Type]":
        """Gets the unit of this GsaExpression.

        Returns
        -------
        Union[GsaSlimUnit, Unset_Type]
            The unit of this GsaExpression.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "Union[GsaSlimUnit, Unset_Type]") -> None:
        """Sets the unit of this GsaExpression.

        Parameters
        ----------
        unit: Union[GsaSlimUnit, Unset_Type]
            The unit of this GsaExpression.
        """
        # Field is not nullable
        if unit is None:
            raise ValueError("Invalid value for 'unit', must not be 'None'")
        self._unit = unit

    @property
    def attribute_dependencies(self) -> "list[GsaSlimAttribute]":
        """Gets the attribute_dependencies of this GsaExpression.

        Returns
        -------
        list[GsaSlimAttribute]
            The attribute_dependencies of this GsaExpression.
        """
        return self._attribute_dependencies

    @attribute_dependencies.setter
    def attribute_dependencies(self, attribute_dependencies: "list[GsaSlimAttribute]") -> None:
        """Sets the attribute_dependencies of this GsaExpression.

        Parameters
        ----------
        attribute_dependencies: list[GsaSlimAttribute]
            The attribute_dependencies of this GsaExpression.
        """
        # Field is not nullable
        if attribute_dependencies is None:
            raise ValueError("Invalid value for 'attribute_dependencies', must not be 'None'")
        # Field is required
        if attribute_dependencies is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'attribute_dependencies', must not be 'Unset'")
        self._attribute_dependencies = attribute_dependencies

    @property
    def constant_dependencies(self) -> "list[GsaSlimNamedEntity]":
        """Gets the constant_dependencies of this GsaExpression.

        Returns
        -------
        list[GsaSlimNamedEntity]
            The constant_dependencies of this GsaExpression.
        """
        return self._constant_dependencies

    @constant_dependencies.setter
    def constant_dependencies(self, constant_dependencies: "list[GsaSlimNamedEntity]") -> None:
        """Sets the constant_dependencies of this GsaExpression.

        Parameters
        ----------
        constant_dependencies: list[GsaSlimNamedEntity]
            The constant_dependencies of this GsaExpression.
        """
        # Field is not nullable
        if constant_dependencies is None:
            raise ValueError("Invalid value for 'constant_dependencies', must not be 'None'")
        # Field is required
        if constant_dependencies is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'constant_dependencies', must not be 'Unset'")
        self._constant_dependencies = constant_dependencies

    @property
    def parameter_dependencies(self) -> "list[GsaSlimNamedEntity]":
        """Gets the parameter_dependencies of this GsaExpression.

        Returns
        -------
        list[GsaSlimNamedEntity]
            The parameter_dependencies of this GsaExpression.
        """
        return self._parameter_dependencies

    @parameter_dependencies.setter
    def parameter_dependencies(self, parameter_dependencies: "list[GsaSlimNamedEntity]") -> None:
        """Sets the parameter_dependencies of this GsaExpression.

        Parameters
        ----------
        parameter_dependencies: list[GsaSlimNamedEntity]
            The parameter_dependencies of this GsaExpression.
        """
        # Field is not nullable
        if parameter_dependencies is None:
            raise ValueError("Invalid value for 'parameter_dependencies', must not be 'None'")
        # Field is required
        if parameter_dependencies is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'parameter_dependencies', must not be 'Unset'")
        self._parameter_dependencies = parameter_dependencies

    @property
    def name(self) -> "str":
        """Gets the name of this GsaExpression.

        Returns
        -------
        str
            The name of this GsaExpression.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GsaExpression.

        Parameters
        ----------
        name: str
            The name of this GsaExpression.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        # Field is required
        if name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'name', must not be 'Unset'")
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GsaExpression.

        Returns
        -------
        str
            The guid of this GsaExpression.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GsaExpression.

        Parameters
        ----------
        guid: str
            The guid of this GsaExpression.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        # Field is required
        if guid is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'guid', must not be 'Unset'")
        self._guid = guid

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
        if not isinstance(other, GsaExpression):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
