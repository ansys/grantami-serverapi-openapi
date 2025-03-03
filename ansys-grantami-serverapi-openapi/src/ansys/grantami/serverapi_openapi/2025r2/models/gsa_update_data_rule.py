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


class GsaUpdateDataRule(ModelBase):
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
        "description": "str",
        "guid": "str",
        "name": "str",
        "regular_expression": "str",
    }

    attribute_map: dict[str, str] = {
        "description": "description",
        "guid": "guid",
        "name": "name",
        "regular_expression": "regularExpression",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        description: "Union[str, Unset_Type]" = Unset,
        guid: "Union[str, Unset_Type]" = Unset,
        name: "Union[str, Unset_Type]" = Unset,
        regular_expression: "Union[str, Unset_Type]" = Unset,
    ) -> None:
        """GsaUpdateDataRule - a model defined in Swagger

        Parameters
        ----------
        description: str, optional
        guid: str, optional
        name: str, optional
        regular_expression: str, optional
        """
        self._description: Union[str, Unset_Type] = Unset
        self._regular_expression: Union[str, Unset_Type] = Unset
        self._name: Union[str, Unset_Type] = Unset
        self._guid: Union[str, Unset_Type] = Unset

        if description is not Unset:
            self.description = description
        if regular_expression is not Unset:
            self.regular_expression = regular_expression
        if name is not Unset:
            self.name = name
        if guid is not Unset:
            self.guid = guid

    @property
    def description(self) -> "Union[str, Unset_Type]":
        """Gets the description of this GsaUpdateDataRule.

        Returns
        -------
        Union[str, Unset_Type]
            The description of this GsaUpdateDataRule.
        """
        return self._description

    @description.setter
    def description(self, description: "Union[str, Unset_Type]") -> None:
        """Sets the description of this GsaUpdateDataRule.

        Parameters
        ----------
        description: Union[str, Unset_Type]
            The description of this GsaUpdateDataRule.
        """
        # Field is not nullable
        if description is None:
            raise ValueError("Invalid value for 'description', must not be 'None'")
        self._description = description

    @property
    def regular_expression(self) -> "Union[str, Unset_Type]":
        """Gets the regular_expression of this GsaUpdateDataRule.

        Returns
        -------
        Union[str, Unset_Type]
            The regular_expression of this GsaUpdateDataRule.
        """
        return self._regular_expression

    @regular_expression.setter
    def regular_expression(self, regular_expression: "Union[str, Unset_Type]") -> None:
        """Sets the regular_expression of this GsaUpdateDataRule.

        Parameters
        ----------
        regular_expression: Union[str, Unset_Type]
            The regular_expression of this GsaUpdateDataRule.
        """
        # Field is not nullable
        if regular_expression is None:
            raise ValueError("Invalid value for 'regular_expression', must not be 'None'")
        self._regular_expression = regular_expression

    @property
    def name(self) -> "Union[str, Unset_Type]":
        """Gets the name of this GsaUpdateDataRule.

        Returns
        -------
        Union[str, Unset_Type]
            The name of this GsaUpdateDataRule.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, Unset_Type]") -> None:
        """Sets the name of this GsaUpdateDataRule.

        Parameters
        ----------
        name: Union[str, Unset_Type]
            The name of this GsaUpdateDataRule.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

    @property
    def guid(self) -> "Union[str, Unset_Type]":
        """Gets the guid of this GsaUpdateDataRule.

        Returns
        -------
        Union[str, Unset_Type]
            The guid of this GsaUpdateDataRule.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, Unset_Type]") -> None:
        """Sets the guid of this GsaUpdateDataRule.

        Parameters
        ----------
        guid: Union[str, Unset_Type]
            The guid of this GsaUpdateDataRule.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
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
        if not isinstance(other, GsaUpdateDataRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
