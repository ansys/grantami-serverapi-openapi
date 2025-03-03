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

from ansys.grantami.serverapi_openapi.v2025r2.models.gsa_applicable_datum import (  # noqa: F401
    GsaApplicableDatum,
)
from ansys.grantami.serverapi_openapi.v2025r2.models.gsa_datum_type import GsaDatumType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaPictureDatum(GsaApplicableDatum):
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
        "datum_type": "GsaDatumType",
        "not_applicable": "str",
        "relative_export_url": "str",
    }

    attribute_map: dict[str, str] = {
        "datum_type": "datumType",
        "not_applicable": "notApplicable",
        "relative_export_url": "relativeExportUrl",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        datum_type: "GsaDatumType" = GsaDatumType.PICTURE,
        not_applicable: "str" = "applicable",
        relative_export_url: "str",
    ) -> None:
        """GsaPictureDatum - a model defined in Swagger

        Parameters
        ----------
        datum_type: GsaDatumType
        not_applicable: str
        relative_export_url: str
        """
        super().__init__(datum_type=datum_type, not_applicable=not_applicable)
        self._relative_export_url: str

        self.relative_export_url = relative_export_url

    @property
    def relative_export_url(self) -> "str":
        """Gets the relative_export_url of this GsaPictureDatum.

        Returns
        -------
        str
            The relative_export_url of this GsaPictureDatum.
        """
        return self._relative_export_url

    @relative_export_url.setter
    def relative_export_url(self, relative_export_url: "str") -> None:
        """Sets the relative_export_url of this GsaPictureDatum.

        Parameters
        ----------
        relative_export_url: str
            The relative_export_url of this GsaPictureDatum.
        """
        # Field is not nullable
        if relative_export_url is None:
            raise ValueError("Invalid value for 'relative_export_url', must not be 'None'")
        # Field is required
        if relative_export_url is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'relative_export_url', must not be 'Unset'")
        self._relative_export_url = relative_export_url

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
        if not isinstance(other, GsaPictureDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
