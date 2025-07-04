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


class GsaResolvedLinkTarget(ModelBase):
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
        "database_guid": "str",
        "database_version_guid": "str",
        "table_guid": "str",
    }

    attribute_map: dict[str, str] = {
        "database_guid": "databaseGuid",
        "database_version_guid": "databaseVersionGuid",
        "table_guid": "tableGuid",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        database_guid: "str",
        database_version_guid: "str",
        table_guid: "str",
    ) -> None:
        """GsaResolvedLinkTarget - a model defined in Swagger

        Parameters
        ----------
        database_guid: str
        database_version_guid: str
        table_guid: str
        """
        self._database_guid: str
        self._database_version_guid: str
        self._table_guid: str

        self.database_guid = database_guid
        self.database_version_guid = database_version_guid
        self.table_guid = table_guid

    @property
    def database_guid(self) -> "str":
        """Gets the database_guid of this GsaResolvedLinkTarget.

        Returns
        -------
        str
            The database_guid of this GsaResolvedLinkTarget.
        """
        return self._database_guid

    @database_guid.setter
    def database_guid(self, database_guid: "str") -> None:
        """Sets the database_guid of this GsaResolvedLinkTarget.

        Parameters
        ----------
        database_guid: str
            The database_guid of this GsaResolvedLinkTarget.
        """
        # Field is not nullable
        if database_guid is None:
            raise ValueError("Invalid value for 'database_guid', must not be 'None'")
        # Field is required
        if database_guid is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'database_guid', must not be 'Unset'")
        self._database_guid = database_guid

    @property
    def database_version_guid(self) -> "str":
        """Gets the database_version_guid of this GsaResolvedLinkTarget.

        Returns
        -------
        str
            The database_version_guid of this GsaResolvedLinkTarget.
        """
        return self._database_version_guid

    @database_version_guid.setter
    def database_version_guid(self, database_version_guid: "str") -> None:
        """Sets the database_version_guid of this GsaResolvedLinkTarget.

        Parameters
        ----------
        database_version_guid: str
            The database_version_guid of this GsaResolvedLinkTarget.
        """
        # Field is not nullable
        if database_version_guid is None:
            raise ValueError("Invalid value for 'database_version_guid', must not be 'None'")
        # Field is required
        if database_version_guid is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'database_version_guid', must not be 'Unset'")
        self._database_version_guid = database_version_guid

    @property
    def table_guid(self) -> "str":
        """Gets the table_guid of this GsaResolvedLinkTarget.

        Returns
        -------
        str
            The table_guid of this GsaResolvedLinkTarget.
        """
        return self._table_guid

    @table_guid.setter
    def table_guid(self, table_guid: "str") -> None:
        """Sets the table_guid of this GsaResolvedLinkTarget.

        Parameters
        ----------
        table_guid: str
            The table_guid of this GsaResolvedLinkTarget.
        """
        # Field is not nullable
        if table_guid is None:
            raise ValueError("Invalid value for 'table_guid', must not be 'None'")
        # Field is required
        if table_guid is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'table_guid', must not be 'Unset'")
        self._table_guid = table_guid

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
        if not isinstance(other, GsaResolvedLinkTarget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
