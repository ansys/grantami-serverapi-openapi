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


class GsaDatabaseIssues(ModelBase):
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
        "database_revision_identity_has_decreased": "bool",
        "loading_exception_info": "GsaExceptionInformation",
    }

    attribute_map: dict[str, str] = {
        "database_revision_identity_has_decreased": "databaseRevisionIdentityHasDecreased",
        "loading_exception_info": "loadingExceptionInfo",
    }

    subtype_mapping: dict[str, str] = {
        "loadingExceptionInfo": "GsaExceptionInformation",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        database_revision_identity_has_decreased: "bool",
        loading_exception_info: "GsaExceptionInformation | Unset_Type" = Unset,
    ) -> None:
        """GsaDatabaseIssues - a model defined in Swagger

        Parameters
        ----------
        database_revision_identity_has_decreased: bool
        loading_exception_info: GsaExceptionInformation, optional
        """
        self._database_revision_identity_has_decreased: bool
        self._loading_exception_info: GsaExceptionInformation | Unset_Type = Unset

        self.database_revision_identity_has_decreased = database_revision_identity_has_decreased
        if loading_exception_info is not Unset:
            self.loading_exception_info = loading_exception_info

    @property
    def database_revision_identity_has_decreased(self) -> "bool":
        """Gets the database_revision_identity_has_decreased of this GsaDatabaseIssues.

        Returns
        -------
        bool
            The database_revision_identity_has_decreased of this GsaDatabaseIssues.
        """
        return self._database_revision_identity_has_decreased

    @database_revision_identity_has_decreased.setter
    def database_revision_identity_has_decreased(
        self, database_revision_identity_has_decreased: "bool"
    ) -> None:
        """Sets the database_revision_identity_has_decreased of this GsaDatabaseIssues.

        Parameters
        ----------
        database_revision_identity_has_decreased: bool
            The database_revision_identity_has_decreased of this GsaDatabaseIssues.
        """
        # Field is not nullable
        if database_revision_identity_has_decreased is None:
            raise ValueError(
                "Invalid value for 'database_revision_identity_has_decreased', must not be 'None'"
            )
        # Field is required
        if database_revision_identity_has_decreased is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'database_revision_identity_has_decreased', must not be 'Unset'"
            )
        self._database_revision_identity_has_decreased = database_revision_identity_has_decreased

    @property
    def loading_exception_info(self) -> "GsaExceptionInformation | Unset_Type":
        """Gets the loading_exception_info of this GsaDatabaseIssues.

        Returns
        -------
        GsaExceptionInformation | Unset_Type
            The loading_exception_info of this GsaDatabaseIssues.
        """
        return self._loading_exception_info

    @loading_exception_info.setter
    def loading_exception_info(
        self, loading_exception_info: "GsaExceptionInformation | Unset_Type"
    ) -> None:
        """Sets the loading_exception_info of this GsaDatabaseIssues.

        Parameters
        ----------
        loading_exception_info: GsaExceptionInformation | Unset_Type
            The loading_exception_info of this GsaDatabaseIssues.
        """
        # Field is not nullable
        if loading_exception_info is None:
            raise ValueError("Invalid value for 'loading_exception_info', must not be 'None'")
        self._loading_exception_info = loading_exception_info

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
        if not isinstance(other, GsaDatabaseIssues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
