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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from ansys.grantami.serverapi_openapi.models.gsa_datum_rollup import GsaDatumRollup  # noqa: F401
from ansys.grantami.serverapi_openapi.models.gsa_datum_rollup_type import GsaDatumRollupType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaDatumListRollup(GsaDatumRollup):
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
        "list_rollup_datums": "list[GsaListRollupDatum]",
        "type": "GsaDatumRollupType",
    }

    attribute_map: dict[str, str] = {
        "list_rollup_datums": "listRollupDatums",
        "type": "type",
    }

    subtype_mapping: dict[str, str] = {
        "listRollupDatums": "GsaListRollupDatum",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        list_rollup_datums: "list[GsaListRollupDatum]",
        type: "GsaDatumRollupType" = GsaDatumRollupType.LIST,
    ) -> None:
        """GsaDatumListRollup - a model defined in Swagger

        Parameters
        ----------
        list_rollup_datums: list[GsaListRollupDatum]
        type: GsaDatumRollupType
        """
        super().__init__(type=type)
        self._list_rollup_datums: list[GsaListRollupDatum]

        self.list_rollup_datums = list_rollup_datums

    @property
    def list_rollup_datums(self) -> "list[GsaListRollupDatum]":
        """Gets the list_rollup_datums of this GsaDatumListRollup.

        Returns
        -------
        list[GsaListRollupDatum]
            The list_rollup_datums of this GsaDatumListRollup.
        """
        return self._list_rollup_datums

    @list_rollup_datums.setter
    def list_rollup_datums(self, list_rollup_datums: "list[GsaListRollupDatum]") -> None:
        """Sets the list_rollup_datums of this GsaDatumListRollup.

        Parameters
        ----------
        list_rollup_datums: list[GsaListRollupDatum]
            The list_rollup_datums of this GsaDatumListRollup.
        """
        # Field is not nullable
        if list_rollup_datums is None:
            raise ValueError("Invalid value for 'list_rollup_datums', must not be 'None'")
        # Field is required
        if list_rollup_datums is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'list_rollup_datums', must not be 'Unset'")
        self._list_rollup_datums = list_rollup_datums

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
        if not isinstance(other, GsaDatumListRollup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
