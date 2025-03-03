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

from ansys.grantami.serverapi_openapi.2024r2.models.granta_server_api_search_criterion import (  # noqa: F401
    GrantaServerApiSearchCriterion,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiSearchRecordReferenceCriterion(GrantaServerApiSearchCriterion):
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
        "record_guid": "str",
        "record_history_guid": "str",
        "record_history_identity": "int",
        "record_identity": "int",
        "type": "str",
    }

    attribute_map: dict[str, str] = {
        "database_key": "databaseKey",
        "record_guid": "recordGuid",
        "record_history_guid": "recordHistoryGuid",
        "record_history_identity": "recordHistoryIdentity",
        "record_identity": "recordIdentity",
        "type": "type",
    }

    subtype_mapping: dict[str, str] = {
    }

    discriminator: Optional[str] = None

    def __init__(self, *, database_key: "Union[str, None, Unset_Type]" = Unset, record_guid: "Union[str, None, Unset_Type]" = Unset, record_history_guid: "Union[str, None, Unset_Type]" = Unset, record_history_identity: "Union[int, None, Unset_Type]" = Unset, record_identity: "Union[int, None, Unset_Type]" = Unset, type: "str" = 'reference',) -> None:
        """GrantaServerApiSearchRecordReferenceCriterion - a model defined in Swagger

        Parameters
        ----------
        database_key: str, optional
        record_guid: str, optional
        record_history_guid: str, optional
        record_history_identity: int, optional
        record_identity: int, optional
        type: str
        """
        super().__init__()
        self._database_key: Union[str, None, Unset_Type] = Unset
        self._record_identity: Union[int, None, Unset_Type] = Unset
        self._record_history_identity: Union[int, None, Unset_Type] = Unset
        self._record_history_guid: Union[str, None, Unset_Type] = Unset
        self._record_guid: Union[str, None, Unset_Type] = Unset
        self._type: str

        if database_key is not Unset:
            self.database_key = database_key
        if record_identity is not Unset:
            self.record_identity = record_identity
        if record_history_identity is not Unset:
            self.record_history_identity = record_history_identity
        if record_history_guid is not Unset:
            self.record_history_guid = record_history_guid
        if record_guid is not Unset:
            self.record_guid = record_guid
        self.type = type

    @property
    def database_key(self) -> "Union[str, None, Unset_Type]":
        """Gets the database_key of this GrantaServerApiSearchRecordReferenceCriterion.

        Returns
        -------
        Union[str, None, Unset_Type]
            The database_key of this GrantaServerApiSearchRecordReferenceCriterion.
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key: "Union[str, None, Unset_Type]") -> None:
        """Sets the database_key of this GrantaServerApiSearchRecordReferenceCriterion.

        Parameters
        ----------
        database_key: Union[str, None, Unset_Type]
            The database_key of this GrantaServerApiSearchRecordReferenceCriterion.
        """
        self._database_key = database_key

    @property
    def record_identity(self) -> "Union[int, None, Unset_Type]":
        """Gets the record_identity of this GrantaServerApiSearchRecordReferenceCriterion.

        Returns
        -------
        Union[int, None, Unset_Type]
            The record_identity of this GrantaServerApiSearchRecordReferenceCriterion.
        """
        return self._record_identity

    @record_identity.setter
    def record_identity(self, record_identity: "Union[int, None, Unset_Type]") -> None:
        """Sets the record_identity of this GrantaServerApiSearchRecordReferenceCriterion.

        Parameters
        ----------
        record_identity: Union[int, None, Unset_Type]
            The record_identity of this GrantaServerApiSearchRecordReferenceCriterion.
        """
        self._record_identity = record_identity

    @property
    def record_history_identity(self) -> "Union[int, None, Unset_Type]":
        """Gets the record_history_identity of this GrantaServerApiSearchRecordReferenceCriterion.

        Returns
        -------
        Union[int, None, Unset_Type]
            The record_history_identity of this GrantaServerApiSearchRecordReferenceCriterion.
        """
        return self._record_history_identity

    @record_history_identity.setter
    def record_history_identity(self, record_history_identity: "Union[int, None, Unset_Type]") -> None:
        """Sets the record_history_identity of this GrantaServerApiSearchRecordReferenceCriterion.

        Parameters
        ----------
        record_history_identity: Union[int, None, Unset_Type]
            The record_history_identity of this GrantaServerApiSearchRecordReferenceCriterion.
        """
        self._record_history_identity = record_history_identity

    @property
    def record_history_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the record_history_guid of this GrantaServerApiSearchRecordReferenceCriterion.

        Returns
        -------
        Union[str, None, Unset_Type]
            The record_history_guid of this GrantaServerApiSearchRecordReferenceCriterion.
        """
        return self._record_history_guid

    @record_history_guid.setter
    def record_history_guid(self, record_history_guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the record_history_guid of this GrantaServerApiSearchRecordReferenceCriterion.

        Parameters
        ----------
        record_history_guid: Union[str, None, Unset_Type]
            The record_history_guid of this GrantaServerApiSearchRecordReferenceCriterion.
        """
        self._record_history_guid = record_history_guid

    @property
    def record_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the record_guid of this GrantaServerApiSearchRecordReferenceCriterion.

        Returns
        -------
        Union[str, None, Unset_Type]
            The record_guid of this GrantaServerApiSearchRecordReferenceCriterion.
        """
        return self._record_guid

    @record_guid.setter
    def record_guid(self, record_guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the record_guid of this GrantaServerApiSearchRecordReferenceCriterion.

        Parameters
        ----------
        record_guid: Union[str, None, Unset_Type]
            The record_guid of this GrantaServerApiSearchRecordReferenceCriterion.
        """
        self._record_guid = record_guid

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchRecordReferenceCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchRecordReferenceCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchRecordReferenceCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchRecordReferenceCriterion.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

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
        if not isinstance(other, GrantaServerApiSearchRecordReferenceCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

