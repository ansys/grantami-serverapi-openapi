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

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaListRollupDatum(ModelBase):
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
        "datum": "GsaDatum",
        "source_row": "GsaSlimEntity",
    }

    attribute_map: dict[str, str] = {
        "datum": "datum",
        "source_row": "sourceRow",
    }

    subtype_mapping: dict[str, str] = {
        "sourceRow": "GsaSlimEntity",
        "datum": "GsaDatum",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        datum: "GsaDatum",
        source_row: "GsaSlimEntity",
    ) -> None:
        """GsaListRollupDatum - a model defined in Swagger

        Parameters
        ----------
        datum: GsaDatum
        source_row: GsaSlimEntity
        """
        self._source_row: GsaSlimEntity
        self._datum: GsaDatum

        self.source_row = source_row
        self.datum = datum

    @property
    def source_row(self) -> "GsaSlimEntity":
        """Gets the source_row of this GsaListRollupDatum.

        Returns
        -------
        GsaSlimEntity
            The source_row of this GsaListRollupDatum.
        """
        return self._source_row

    @source_row.setter
    def source_row(self, source_row: "GsaSlimEntity") -> None:
        """Sets the source_row of this GsaListRollupDatum.

        Parameters
        ----------
        source_row: GsaSlimEntity
            The source_row of this GsaListRollupDatum.
        """
        # Field is not nullable
        if source_row is None:
            raise ValueError("Invalid value for 'source_row', must not be 'None'")
        # Field is required
        if source_row is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'source_row', must not be 'Unset'")
        self._source_row = source_row

    @property
    def datum(self) -> "GsaDatum":
        """Gets the datum of this GsaListRollupDatum.

        Returns
        -------
        GsaDatum
            The datum of this GsaListRollupDatum.
        """
        return self._datum

    @datum.setter
    def datum(self, datum: "GsaDatum") -> None:
        """Sets the datum of this GsaListRollupDatum.

        Parameters
        ----------
        datum: GsaDatum
            The datum of this GsaListRollupDatum.
        """
        # Field is not nullable
        if datum is None:
            raise ValueError("Invalid value for 'datum', must not be 'None'")
        # Field is required
        if datum is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'datum', must not be 'Unset'")
        self._datum = datum

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
        if not isinstance(other, GsaListRollupDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
