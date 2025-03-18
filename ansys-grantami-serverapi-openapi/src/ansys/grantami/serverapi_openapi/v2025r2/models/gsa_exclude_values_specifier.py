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

from ansys.grantami.serverapi_openapi.v2025r2.models.gsa_value_specifier import (  # noqa: F401
    GsaValueSpecifier,
)
from ansys.grantami.serverapi_openapi.v2025r2.models.gsa_value_specifier_type import (
    GsaValueSpecifierType,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaExcludeValuesSpecifier(GsaValueSpecifier):
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
        "filter_on": "GsaValueSpecifierType",
        "excluded_guids": "list[str]",
        "excluded_identities": "list[int]",
    }

    attribute_map: dict[str, str] = {
        "filter_on": "filterOn",
        "excluded_guids": "excludedGuids",
        "excluded_identities": "excludedIdentities",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        filter_on: "GsaValueSpecifierType" = GsaValueSpecifierType.EXCLUDE,
        excluded_guids: "Union[list[str], None, Unset_Type]" = Unset,
        excluded_identities: "Union[list[int], None, Unset_Type]" = Unset,
    ) -> None:
        """GsaExcludeValuesSpecifier - a model defined in Swagger

        Parameters
        ----------
        filter_on: GsaValueSpecifierType
        excluded_guids: list[str], optional
        excluded_identities: list[int], optional
        """
        super().__init__(filter_on=filter_on)
        self._excluded_identities: Union[list[int], None, Unset_Type] = Unset
        self._excluded_guids: Union[list[str], None, Unset_Type] = Unset

        if excluded_identities is not Unset:
            self.excluded_identities = excluded_identities
        if excluded_guids is not Unset:
            self.excluded_guids = excluded_guids

    @property
    def excluded_identities(self) -> "Union[list[int], None, Unset_Type]":
        """Gets the excluded_identities of this GsaExcludeValuesSpecifier.

        Returns
        -------
        Union[list[int], None, Unset_Type]
            The excluded_identities of this GsaExcludeValuesSpecifier.
        """
        return self._excluded_identities

    @excluded_identities.setter
    def excluded_identities(
        self, excluded_identities: "Union[list[int], None, Unset_Type]"
    ) -> None:
        """Sets the excluded_identities of this GsaExcludeValuesSpecifier.

        Parameters
        ----------
        excluded_identities: Union[list[int], None, Unset_Type]
            The excluded_identities of this GsaExcludeValuesSpecifier.
        """
        self._excluded_identities = excluded_identities

    @property
    def excluded_guids(self) -> "Union[list[str], None, Unset_Type]":
        """Gets the excluded_guids of this GsaExcludeValuesSpecifier.

        Returns
        -------
        Union[list[str], None, Unset_Type]
            The excluded_guids of this GsaExcludeValuesSpecifier.
        """
        return self._excluded_guids

    @excluded_guids.setter
    def excluded_guids(self, excluded_guids: "Union[list[str], None, Unset_Type]") -> None:
        """Sets the excluded_guids of this GsaExcludeValuesSpecifier.

        Parameters
        ----------
        excluded_guids: Union[list[str], None, Unset_Type]
            The excluded_guids of this GsaExcludeValuesSpecifier.
        """
        self._excluded_guids = excluded_guids

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
        if not isinstance(other, GsaExcludeValuesSpecifier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
