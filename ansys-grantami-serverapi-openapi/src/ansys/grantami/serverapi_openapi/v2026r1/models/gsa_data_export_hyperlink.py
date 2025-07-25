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


class GsaDataExportHyperlink(ModelBase):
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
        "address": "str",
        "description": "str",
        "formatted_address": "str",
        "target": "GsaHyperlinkTarget",
    }

    attribute_map: dict[str, str] = {
        "address": "address",
        "description": "description",
        "formatted_address": "formattedAddress",
        "target": "target",
    }

    subtype_mapping: dict[str, str] = {
        "target": "GsaHyperlinkTarget",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        address: "str | None | Unset_Type" = Unset,
        description: "str | None | Unset_Type" = Unset,
        formatted_address: "str | None | Unset_Type" = Unset,
        target: "GsaHyperlinkTarget | Unset_Type" = Unset,
    ) -> None:
        """GsaDataExportHyperlink - a model defined in Swagger

        Parameters
        ----------
        address: str | None, optional
        description: str | None, optional
        formatted_address: str | None, optional
        target: GsaHyperlinkTarget, optional
        """
        self._address: str | None | Unset_Type = Unset
        self._formatted_address: str | None | Unset_Type = Unset
        self._description: str | None | Unset_Type = Unset
        self._target: GsaHyperlinkTarget | Unset_Type = Unset

        if address is not Unset:
            self.address = address
        if formatted_address is not Unset:
            self.formatted_address = formatted_address
        if description is not Unset:
            self.description = description
        if target is not Unset:
            self.target = target

    @property
    def address(self) -> "str | None | Unset_Type":
        """Gets the address of this GsaDataExportHyperlink.

        Returns
        -------
        str | None | Unset_Type
            The address of this GsaDataExportHyperlink.
        """
        return self._address

    @address.setter
    def address(self, address: "str | None | Unset_Type") -> None:
        """Sets the address of this GsaDataExportHyperlink.

        Parameters
        ----------
        address: str | None | Unset_Type
            The address of this GsaDataExportHyperlink.
        """
        self._address = address

    @property
    def formatted_address(self) -> "str | None | Unset_Type":
        """Gets the formatted_address of this GsaDataExportHyperlink.

        Returns
        -------
        str | None | Unset_Type
            The formatted_address of this GsaDataExportHyperlink.
        """
        return self._formatted_address

    @formatted_address.setter
    def formatted_address(self, formatted_address: "str | None | Unset_Type") -> None:
        """Sets the formatted_address of this GsaDataExportHyperlink.

        Parameters
        ----------
        formatted_address: str | None | Unset_Type
            The formatted_address of this GsaDataExportHyperlink.
        """
        self._formatted_address = formatted_address

    @property
    def description(self) -> "str | None | Unset_Type":
        """Gets the description of this GsaDataExportHyperlink.

        Returns
        -------
        str | None | Unset_Type
            The description of this GsaDataExportHyperlink.
        """
        return self._description

    @description.setter
    def description(self, description: "str | None | Unset_Type") -> None:
        """Sets the description of this GsaDataExportHyperlink.

        Parameters
        ----------
        description: str | None | Unset_Type
            The description of this GsaDataExportHyperlink.
        """
        self._description = description

    @property
    def target(self) -> "GsaHyperlinkTarget | Unset_Type":
        """Gets the target of this GsaDataExportHyperlink.

        Returns
        -------
        GsaHyperlinkTarget | Unset_Type
            The target of this GsaDataExportHyperlink.
        """
        return self._target

    @target.setter
    def target(self, target: "GsaHyperlinkTarget | Unset_Type") -> None:
        """Sets the target of this GsaDataExportHyperlink.

        Parameters
        ----------
        target: GsaHyperlinkTarget | Unset_Type
            The target of this GsaDataExportHyperlink.
        """
        # Field is not nullable
        if target is None:
            raise ValueError("Invalid value for 'target', must not be 'None'")
        self._target = target

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
        if not isinstance(other, GsaDataExportHyperlink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
