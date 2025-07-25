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


class GrantaServerApiSchemaConstantsConstant(ModelBase):
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
        "guid": "str",
        "name": "str",
        "value": "float",
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimUnit",
    }

    attribute_map: dict[str, str] = {
        "guid": "guid",
        "name": "name",
        "value": "value",
        "unit": "unit",
    }

    subtype_mapping: dict[str, str] = {
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimUnit",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        guid: "str",
        name: "str",
        value: "float",
        unit: "GrantaServerApiSchemaSlimEntitiesSlimUnit | Unset_Type" = Unset,
    ) -> None:
        """GrantaServerApiSchemaConstantsConstant - a model defined in Swagger

        Parameters
        ----------
        guid: str
        name: str
        value: float
        unit: GrantaServerApiSchemaSlimEntitiesSlimUnit, optional
        """
        self._unit: GrantaServerApiSchemaSlimEntitiesSlimUnit | Unset_Type = Unset
        self._value: float
        self._name: str
        self._guid: str

        if unit is not Unset:
            self.unit = unit
        self.value = value
        self.name = name
        self.guid = guid

    @property
    def unit(self) -> "GrantaServerApiSchemaSlimEntitiesSlimUnit | Unset_Type":
        """Gets the unit of this GrantaServerApiSchemaConstantsConstant.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimUnit | Unset_Type
            The unit of this GrantaServerApiSchemaConstantsConstant.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "GrantaServerApiSchemaSlimEntitiesSlimUnit | Unset_Type") -> None:
        """Sets the unit of this GrantaServerApiSchemaConstantsConstant.

        Parameters
        ----------
        unit: GrantaServerApiSchemaSlimEntitiesSlimUnit | Unset_Type
            The unit of this GrantaServerApiSchemaConstantsConstant.
        """
        # Field is not nullable
        if unit is None:
            raise ValueError("Invalid value for 'unit', must not be 'None'")
        self._unit = unit

    @property
    def value(self) -> "float":
        """Gets the value of this GrantaServerApiSchemaConstantsConstant.

        Returns
        -------
        float
            The value of this GrantaServerApiSchemaConstantsConstant.
        """
        return self._value

    @value.setter
    def value(self, value: "float") -> None:
        """Sets the value of this GrantaServerApiSchemaConstantsConstant.

        Parameters
        ----------
        value: float
            The value of this GrantaServerApiSchemaConstantsConstant.
        """
        # Field is not nullable
        if value is None:
            raise ValueError("Invalid value for 'value', must not be 'None'")
        # Field is required
        if value is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'value', must not be 'Unset'")
        self._value = value

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaConstantsConstant.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaConstantsConstant.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaConstantsConstant.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaConstantsConstant.
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
        """Gets the guid of this GrantaServerApiSchemaConstantsConstant.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaConstantsConstant.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaConstantsConstant.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaConstantsConstant.
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
        if not isinstance(other, GrantaServerApiSchemaConstantsConstant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
