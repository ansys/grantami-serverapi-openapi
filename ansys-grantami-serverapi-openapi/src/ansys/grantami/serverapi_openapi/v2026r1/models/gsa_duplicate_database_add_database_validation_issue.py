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

from ansys.grantami.serverapi_openapi.v2026r1.models.gsa_add_database_issue_type import (
    GsaAddDatabaseIssueType,
)
from ansys.grantami.serverapi_openapi.v2026r1.models.gsa_add_database_validation_issue import (  # noqa: F401
    GsaAddDatabaseValidationIssue,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaDuplicateDatabaseAddDatabaseValidationIssue(GsaAddDatabaseValidationIssue):
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
        "database_key": "str",
        "database_name": "str",
        "issue_type": "GsaAddDatabaseIssueType",
        "additional_information": "str",
    }

    attribute_map: dict[str, str] = {
        "database_key": "databaseKey",
        "database_name": "databaseName",
        "issue_type": "IssueType",
        "additional_information": "additionalInformation",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        database_key: "str",
        database_name: "str",
        issue_type: "GsaAddDatabaseIssueType" = GsaAddDatabaseIssueType.DUPLICATEDATABASE,
        additional_information: "str | None | Unset_Type" = Unset,
    ) -> None:
        """GsaDuplicateDatabaseAddDatabaseValidationIssue - a model defined in Swagger

        Parameters
        ----------
        database_key: str
        database_name: str
        issue_type: GsaAddDatabaseIssueType
        additional_information: str | None, optional
        """
        super().__init__(issue_type=issue_type, additional_information=additional_information)
        self._database_key: str
        self._database_name: str

        self.database_key = database_key
        self.database_name = database_name

    @property
    def database_key(self) -> "str":
        """Gets the database_key of this GsaDuplicateDatabaseAddDatabaseValidationIssue.

        Returns
        -------
        str
            The database_key of this GsaDuplicateDatabaseAddDatabaseValidationIssue.
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key: "str") -> None:
        """Sets the database_key of this GsaDuplicateDatabaseAddDatabaseValidationIssue.

        Parameters
        ----------
        database_key: str
            The database_key of this GsaDuplicateDatabaseAddDatabaseValidationIssue.
        """
        # Field is not nullable
        if database_key is None:
            raise ValueError("Invalid value for 'database_key', must not be 'None'")
        # Field is required
        if database_key is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'database_key', must not be 'Unset'")
        self._database_key = database_key

    @property
    def database_name(self) -> "str":
        """Gets the database_name of this GsaDuplicateDatabaseAddDatabaseValidationIssue.

        Returns
        -------
        str
            The database_name of this GsaDuplicateDatabaseAddDatabaseValidationIssue.
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name: "str") -> None:
        """Sets the database_name of this GsaDuplicateDatabaseAddDatabaseValidationIssue.

        Parameters
        ----------
        database_name: str
            The database_name of this GsaDuplicateDatabaseAddDatabaseValidationIssue.
        """
        # Field is not nullable
        if database_name is None:
            raise ValueError("Invalid value for 'database_name', must not be 'None'")
        # Field is required
        if database_name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'database_name', must not be 'Unset'")
        self._database_name = database_name

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
        if not isinstance(other, GsaDuplicateDatabaseAddDatabaseValidationIssue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
