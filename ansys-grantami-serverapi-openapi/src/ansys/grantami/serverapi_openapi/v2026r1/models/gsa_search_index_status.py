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


class GsaSearchIndexStatus(ModelBase):
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
        "records_that_failed_to_index": "list[GsaIndexRecordFailure]",
        "search_index_in_sync": "bool",
        "search_index_is_read_only": "bool",
        "search_index_location": "str",
        "search_index_out_of_date_duration": "str",
        "search_index_unavailable": "bool",
        "search_index_up_to_date": "bool",
    }

    attribute_map: dict[str, str] = {
        "records_that_failed_to_index": "recordsThatFailedToIndex",
        "search_index_in_sync": "searchIndexInSync",
        "search_index_is_read_only": "searchIndexIsReadOnly",
        "search_index_location": "searchIndexLocation",
        "search_index_out_of_date_duration": "searchIndexOutOfDateDuration",
        "search_index_unavailable": "searchIndexUnavailable",
        "search_index_up_to_date": "searchIndexUpToDate",
    }

    subtype_mapping: dict[str, str] = {
        "recordsThatFailedToIndex": "GsaIndexRecordFailure",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        records_that_failed_to_index: "list[GsaIndexRecordFailure] | None | Unset_Type" = Unset,
        search_index_in_sync: "bool | Unset_Type" = Unset,
        search_index_is_read_only: "bool | None | Unset_Type" = Unset,
        search_index_location: "str | None | Unset_Type" = Unset,
        search_index_out_of_date_duration: "str | None | Unset_Type" = Unset,
        search_index_unavailable: "bool | None | Unset_Type" = Unset,
        search_index_up_to_date: "bool | Unset_Type" = Unset,
    ) -> None:
        """GsaSearchIndexStatus - a model defined in Swagger

        Parameters
        ----------
        records_that_failed_to_index: list[GsaIndexRecordFailure] | None, optional
        search_index_in_sync: bool, optional
        search_index_is_read_only: bool | None, optional
        search_index_location: str | None, optional
        search_index_out_of_date_duration: str | None, optional
        search_index_unavailable: bool | None, optional
        search_index_up_to_date: bool, optional
        """
        self._search_index_up_to_date: bool | Unset_Type = Unset
        self._search_index_out_of_date_duration: str | None | Unset_Type = Unset
        self._search_index_in_sync: bool | Unset_Type = Unset
        self._search_index_location: str | None | Unset_Type = Unset
        self._search_index_is_read_only: bool | None | Unset_Type = Unset
        self._search_index_unavailable: bool | None | Unset_Type = Unset
        self._records_that_failed_to_index: list[GsaIndexRecordFailure] | None | Unset_Type = Unset

        if search_index_up_to_date is not Unset:
            self.search_index_up_to_date = search_index_up_to_date
        if search_index_out_of_date_duration is not Unset:
            self.search_index_out_of_date_duration = search_index_out_of_date_duration
        if search_index_in_sync is not Unset:
            self.search_index_in_sync = search_index_in_sync
        if search_index_location is not Unset:
            self.search_index_location = search_index_location
        if search_index_is_read_only is not Unset:
            self.search_index_is_read_only = search_index_is_read_only
        if search_index_unavailable is not Unset:
            self.search_index_unavailable = search_index_unavailable
        if records_that_failed_to_index is not Unset:
            self.records_that_failed_to_index = records_that_failed_to_index

    @property
    def search_index_up_to_date(self) -> "bool | Unset_Type":
        """Gets the search_index_up_to_date of this GsaSearchIndexStatus.
        Whether all changes up to and including the most recent database revision have been sent to the search index. This will return true  even if some of those revisions could not be indexed

        Returns
        -------
        bool | Unset_Type
            The search_index_up_to_date of this GsaSearchIndexStatus.
        """
        return self._search_index_up_to_date

    @search_index_up_to_date.setter
    def search_index_up_to_date(self, search_index_up_to_date: "bool | Unset_Type") -> None:
        """Sets the search_index_up_to_date of this GsaSearchIndexStatus.
        Whether all changes up to and including the most recent database revision have been sent to the search index. This will return true  even if some of those revisions could not be indexed

        Parameters
        ----------
        search_index_up_to_date: bool | Unset_Type
            The search_index_up_to_date of this GsaSearchIndexStatus.
        """
        # Field is not nullable
        if search_index_up_to_date is None:
            raise ValueError("Invalid value for 'search_index_up_to_date', must not be 'None'")
        self._search_index_up_to_date = search_index_up_to_date

    @property
    def search_index_out_of_date_duration(self) -> "str | None | Unset_Type":
        """Gets the search_index_out_of_date_duration of this GsaSearchIndexStatus.
        How long has the index been out of date.  Specifically the duration between the first non-indexed revision and the current time.

        Returns
        -------
        str | None | Unset_Type
            The search_index_out_of_date_duration of this GsaSearchIndexStatus.
        """
        return self._search_index_out_of_date_duration

    @search_index_out_of_date_duration.setter
    def search_index_out_of_date_duration(
        self, search_index_out_of_date_duration: "str | None | Unset_Type"
    ) -> None:
        """Sets the search_index_out_of_date_duration of this GsaSearchIndexStatus.
        How long has the index been out of date.  Specifically the duration between the first non-indexed revision and the current time.

        Parameters
        ----------
        search_index_out_of_date_duration: str | None | Unset_Type
            The search_index_out_of_date_duration of this GsaSearchIndexStatus.
        """
        self._search_index_out_of_date_duration = search_index_out_of_date_duration

    @property
    def search_index_in_sync(self) -> "bool | Unset_Type":
        """Gets the search_index_in_sync of this GsaSearchIndexStatus.
        Returns false if the search index is out of sync with the database (i.e. because changes were made that could not be indexed)

        Returns
        -------
        bool | Unset_Type
            The search_index_in_sync of this GsaSearchIndexStatus.
        """
        return self._search_index_in_sync

    @search_index_in_sync.setter
    def search_index_in_sync(self, search_index_in_sync: "bool | Unset_Type") -> None:
        """Sets the search_index_in_sync of this GsaSearchIndexStatus.
        Returns false if the search index is out of sync with the database (i.e. because changes were made that could not be indexed)

        Parameters
        ----------
        search_index_in_sync: bool | Unset_Type
            The search_index_in_sync of this GsaSearchIndexStatus.
        """
        # Field is not nullable
        if search_index_in_sync is None:
            raise ValueError("Invalid value for 'search_index_in_sync', must not be 'None'")
        self._search_index_in_sync = search_index_in_sync

    @property
    def search_index_location(self) -> "str | None | Unset_Type":
        """Gets the search_index_location of this GsaSearchIndexStatus.
        The location of the index.

        Returns
        -------
        str | None | Unset_Type
            The search_index_location of this GsaSearchIndexStatus.
        """
        return self._search_index_location

    @search_index_location.setter
    def search_index_location(self, search_index_location: "str | None | Unset_Type") -> None:
        """Sets the search_index_location of this GsaSearchIndexStatus.
        The location of the index.

        Parameters
        ----------
        search_index_location: str | None | Unset_Type
            The search_index_location of this GsaSearchIndexStatus.
        """
        self._search_index_location = search_index_location

    @property
    def search_index_is_read_only(self) -> "bool | None | Unset_Type":
        """Gets the search_index_is_read_only of this GsaSearchIndexStatus.
        True if the index is read only.

        Returns
        -------
        bool | None | Unset_Type
            The search_index_is_read_only of this GsaSearchIndexStatus.
        """
        return self._search_index_is_read_only

    @search_index_is_read_only.setter
    def search_index_is_read_only(
        self, search_index_is_read_only: "bool | None | Unset_Type"
    ) -> None:
        """Sets the search_index_is_read_only of this GsaSearchIndexStatus.
        True if the index is read only.

        Parameters
        ----------
        search_index_is_read_only: bool | None | Unset_Type
            The search_index_is_read_only of this GsaSearchIndexStatus.
        """
        self._search_index_is_read_only = search_index_is_read_only

    @property
    def search_index_unavailable(self) -> "bool | None | Unset_Type":
        """Gets the search_index_unavailable of this GsaSearchIndexStatus.
        True if the index could not be contacted.

        Returns
        -------
        bool | None | Unset_Type
            The search_index_unavailable of this GsaSearchIndexStatus.
        """
        return self._search_index_unavailable

    @search_index_unavailable.setter
    def search_index_unavailable(
        self, search_index_unavailable: "bool | None | Unset_Type"
    ) -> None:
        """Sets the search_index_unavailable of this GsaSearchIndexStatus.
        True if the index could not be contacted.

        Parameters
        ----------
        search_index_unavailable: bool | None | Unset_Type
            The search_index_unavailable of this GsaSearchIndexStatus.
        """
        self._search_index_unavailable = search_index_unavailable

    @property
    def records_that_failed_to_index(self) -> "list[GsaIndexRecordFailure] | None | Unset_Type":
        """Gets the records_that_failed_to_index of this GsaSearchIndexStatus.
        Details of any records that failed to index.

        Returns
        -------
        list[GsaIndexRecordFailure] | None | Unset_Type
            The records_that_failed_to_index of this GsaSearchIndexStatus.
        """
        return self._records_that_failed_to_index

    @records_that_failed_to_index.setter
    def records_that_failed_to_index(
        self, records_that_failed_to_index: "list[GsaIndexRecordFailure] | None | Unset_Type"
    ) -> None:
        """Sets the records_that_failed_to_index of this GsaSearchIndexStatus.
        Details of any records that failed to index.

        Parameters
        ----------
        records_that_failed_to_index: list[GsaIndexRecordFailure] | None | Unset_Type
            The records_that_failed_to_index of this GsaSearchIndexStatus.
        """
        self._records_that_failed_to_index = records_that_failed_to_index

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
        if not isinstance(other, GsaSearchIndexStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
