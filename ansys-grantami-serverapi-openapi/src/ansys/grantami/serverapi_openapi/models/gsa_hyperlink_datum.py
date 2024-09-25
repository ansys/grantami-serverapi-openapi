# Copyright (C) 2023 - 2024 ANSYS, Inc. and/or its affiliates.
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
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, Union  # noqa: F401

from ansys.grantami.serverapi_openapi.models.gsa_applicable_datum import (  # noqa: F401
    GsaApplicableDatum,
)
from ansys.grantami.serverapi_openapi.models.gsa_datum_type import GsaDatumType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaHyperlinkDatum(GsaApplicableDatum):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes
    ----------
    swagger_types: Dict[str, str]
        The key is attribute name and the value is attribute type.
    attribute_map: Dict[str, str]
        The key is attribute name and the value is json key in definition.
    subtype_mapping: Dict[str, str]
        The key is the unmangled property name and the value is the corresponding type.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: Dict[str, str] = {
        "address": "str",
        "datum_type": "GsaDatumType",
        "description": "str",
        "not_applicable": "str",
        "target": "GsaHyperlinkTarget",
    }

    attribute_map: Dict[str, str] = {
        "address": "address",
        "datum_type": "datumType",
        "description": "description",
        "not_applicable": "notApplicable",
        "target": "target",
    }

    subtype_mapping: Dict[str, str] = {
        "target": "GsaHyperlinkTarget",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        address: "str",
        datum_type: "GsaDatumType" = GsaDatumType.HYPERLINK,
        description: "str",
        not_applicable: "str" = "applicable",
        target: "GsaHyperlinkTarget",
    ) -> None:
        """GsaHyperlinkDatum - a model defined in Swagger

        Parameters
        ----------
        address: str
        datum_type: GsaDatumType
        description: str
        not_applicable: str
        target: GsaHyperlinkTarget
        """
        super().__init__(datum_type=datum_type, not_applicable=not_applicable)
        self._address: str
        self._description: str
        self._target: GsaHyperlinkTarget

        self.address = address
        self.description = description
        self.target = target

    @property
    def address(self) -> "str":
        """Gets the address of this GsaHyperlinkDatum.

        Returns
        -------
        str
            The address of this GsaHyperlinkDatum.
        """
        return self._address

    @address.setter
    def address(self, address: "str") -> None:
        """Sets the address of this GsaHyperlinkDatum.

        Parameters
        ----------
        address: str
            The address of this GsaHyperlinkDatum.
        """
        # Field is not nullable
        if address is None:
            raise ValueError("Invalid value for 'address', must not be 'None'")
        # Field is required
        if address is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'address', must not be 'Unset'")
        self._address = address

    @property
    def description(self) -> "str":
        """Gets the description of this GsaHyperlinkDatum.

        Returns
        -------
        str
            The description of this GsaHyperlinkDatum.
        """
        return self._description

    @description.setter
    def description(self, description: "str") -> None:
        """Sets the description of this GsaHyperlinkDatum.

        Parameters
        ----------
        description: str
            The description of this GsaHyperlinkDatum.
        """
        # Field is not nullable
        if description is None:
            raise ValueError("Invalid value for 'description', must not be 'None'")
        # Field is required
        if description is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'description', must not be 'Unset'")
        self._description = description

    @property
    def target(self) -> "GsaHyperlinkTarget":
        """Gets the target of this GsaHyperlinkDatum.

        Returns
        -------
        GsaHyperlinkTarget
            The target of this GsaHyperlinkDatum.
        """
        return self._target

    @target.setter
    def target(self, target: "GsaHyperlinkTarget") -> None:
        """Sets the target of this GsaHyperlinkDatum.

        Parameters
        ----------
        target: GsaHyperlinkTarget
            The target of this GsaHyperlinkDatum.
        """
        # Field is not nullable
        if target is None:
            raise ValueError("Invalid value for 'target', must not be 'None'")
        # Field is required
        if target is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'target', must not be 'Unset'")
        self._target = target

    @classmethod
    def get_real_child_model(cls, data: Dict[str, str]) -> str:
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
        if not isinstance(other, GsaHyperlinkDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other