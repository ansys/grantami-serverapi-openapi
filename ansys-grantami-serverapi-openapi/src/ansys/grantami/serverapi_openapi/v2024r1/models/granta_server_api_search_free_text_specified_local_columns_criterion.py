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

from ansys.grantami.serverapi_openapi.v2024r1.models.granta_server_api_search_free_text_criterion import (  # noqa: F401
    GrantaServerApiSearchFreeTextCriterion,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion(
    GrantaServerApiSearchFreeTextCriterion
):
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
        "column_guids": "list[str]",
        "column_guids_to_boost": "list[GrantaServerApiSearchBoostByGuid]",
        "column_identities": "list[int]",
        "column_identities_to_boost": "list[GrantaServerApiSearchBoostByIdentity]",
        "free_text_criterion_type": "str",
        "type": "str",
        "value": "str",
    }

    attribute_map: dict[str, str] = {
        "column_guids": "columnGuids",
        "column_guids_to_boost": "columnGuidsToBoost",
        "column_identities": "columnIdentities",
        "column_identities_to_boost": "columnIdentitiesToBoost",
        "free_text_criterion_type": "freeTextCriterionType",
        "type": "type",
        "value": "value",
    }

    subtype_mapping: dict[str, str] = {
        "columnIdentitiesToBoost": "GrantaServerApiSearchBoostByIdentity",
        "columnGuidsToBoost": "GrantaServerApiSearchBoostByGuid",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        column_guids: "list[str] | None | Unset_Type" = Unset,
        column_guids_to_boost: "list[GrantaServerApiSearchBoostByGuid] | None | Unset_Type" = Unset,
        column_identities: "list[int] | None | Unset_Type" = Unset,
        column_identities_to_boost: "list[GrantaServerApiSearchBoostByIdentity] | None | Unset_Type" = Unset,
        free_text_criterion_type: "str" = "specifiedLocalColumns",
        type: "str" = "text",
        value: "str | None | Unset_Type" = Unset,
    ) -> None:
        """GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion - a model defined in Swagger

        Parameters
        ----------
        column_guids: list[str] | None, optional
        column_guids_to_boost: list[GrantaServerApiSearchBoostByGuid] | None, optional
        column_identities: list[int] | None, optional
        column_identities_to_boost: list[GrantaServerApiSearchBoostByIdentity] | None, optional
        free_text_criterion_type: str
        type: str
        value: str | None, optional
        """
        super().__init__(type=type, value=value)
        self._column_identities: list[int] | None | Unset_Type = Unset
        self._column_identities_to_boost: (
            list[GrantaServerApiSearchBoostByIdentity] | None | Unset_Type
        ) = Unset
        self._column_guids: list[str] | None | Unset_Type = Unset
        self._column_guids_to_boost: list[GrantaServerApiSearchBoostByGuid] | None | Unset_Type = (
            Unset
        )
        self._free_text_criterion_type: str

        if column_identities is not Unset:
            self.column_identities = column_identities
        if column_identities_to_boost is not Unset:
            self.column_identities_to_boost = column_identities_to_boost
        if column_guids is not Unset:
            self.column_guids = column_guids
        if column_guids_to_boost is not Unset:
            self.column_guids_to_boost = column_guids_to_boost
        self.free_text_criterion_type = free_text_criterion_type

    @property
    def column_identities(self) -> "list[int] | None | Unset_Type":
        """Gets the column_identities of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.

        Returns
        -------
        list[int] | None | Unset_Type
            The column_identities of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.
        """
        return self._column_identities

    @column_identities.setter
    def column_identities(self, column_identities: "list[int] | None | Unset_Type") -> None:
        """Sets the column_identities of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.

        Parameters
        ----------
        column_identities: list[int] | None | Unset_Type
            The column_identities of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.
        """
        self._column_identities = column_identities

    @property
    def column_identities_to_boost(
        self,
    ) -> "list[GrantaServerApiSearchBoostByIdentity] | None | Unset_Type":
        """Gets the column_identities_to_boost of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.

        Returns
        -------
        list[GrantaServerApiSearchBoostByIdentity] | None | Unset_Type
            The column_identities_to_boost of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.
        """
        return self._column_identities_to_boost

    @column_identities_to_boost.setter
    def column_identities_to_boost(
        self,
        column_identities_to_boost: "list[GrantaServerApiSearchBoostByIdentity] | None | Unset_Type",
    ) -> None:
        """Sets the column_identities_to_boost of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.

        Parameters
        ----------
        column_identities_to_boost: list[GrantaServerApiSearchBoostByIdentity] | None | Unset_Type
            The column_identities_to_boost of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.
        """
        self._column_identities_to_boost = column_identities_to_boost

    @property
    def column_guids(self) -> "list[str] | None | Unset_Type":
        """Gets the column_guids of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.

        Returns
        -------
        list[str] | None | Unset_Type
            The column_guids of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.
        """
        return self._column_guids

    @column_guids.setter
    def column_guids(self, column_guids: "list[str] | None | Unset_Type") -> None:
        """Sets the column_guids of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.

        Parameters
        ----------
        column_guids: list[str] | None | Unset_Type
            The column_guids of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.
        """
        self._column_guids = column_guids

    @property
    def column_guids_to_boost(self) -> "list[GrantaServerApiSearchBoostByGuid] | None | Unset_Type":
        """Gets the column_guids_to_boost of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.

        Returns
        -------
        list[GrantaServerApiSearchBoostByGuid] | None | Unset_Type
            The column_guids_to_boost of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.
        """
        return self._column_guids_to_boost

    @column_guids_to_boost.setter
    def column_guids_to_boost(
        self, column_guids_to_boost: "list[GrantaServerApiSearchBoostByGuid] | None | Unset_Type"
    ) -> None:
        """Sets the column_guids_to_boost of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.

        Parameters
        ----------
        column_guids_to_boost: list[GrantaServerApiSearchBoostByGuid] | None | Unset_Type
            The column_guids_to_boost of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.
        """
        self._column_guids_to_boost = column_guids_to_boost

    @property
    def free_text_criterion_type(self) -> "str":
        """Gets the free_text_criterion_type of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.

        Returns
        -------
        str
            The free_text_criterion_type of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.
        """
        return self._free_text_criterion_type

    @free_text_criterion_type.setter
    def free_text_criterion_type(self, free_text_criterion_type: "str") -> None:
        """Sets the free_text_criterion_type of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.

        Parameters
        ----------
        free_text_criterion_type: str
            The free_text_criterion_type of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.
        """
        # Field is not nullable
        if free_text_criterion_type is None:
            raise ValueError("Invalid value for 'free_text_criterion_type', must not be 'None'")
        # Field is required
        if free_text_criterion_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'free_text_criterion_type', must not be 'Unset'")
        self._free_text_criterion_type = free_text_criterion_type

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
        if not isinstance(other, GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
