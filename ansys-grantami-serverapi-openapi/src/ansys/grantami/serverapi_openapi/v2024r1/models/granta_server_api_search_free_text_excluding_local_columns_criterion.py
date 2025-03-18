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

from ansys.grantami.serverapi_openapi.v2024r1.models.granta_server_api_search_free_text_criterion import (  # noqa: F401
    GrantaServerApiSearchFreeTextCriterion,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiSearchFreeTextExcludingLocalColumnsCriterion(
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
        "column_guids_to_boost": "list[GrantaServerApiSearchBoostByGuid]",
        "column_guids_to_exclude": "list[str]",
        "column_identities_to_boost": "list[GrantaServerApiSearchBoostByIdentity]",
        "column_identities_to_exclude": "list[int]",
        "free_text_criterion_type": "str",
        "type": "str",
        "value": "str",
    }

    attribute_map: dict[str, str] = {
        "column_guids_to_boost": "columnGuidsToBoost",
        "column_guids_to_exclude": "columnGuidsToExclude",
        "column_identities_to_boost": "columnIdentitiesToBoost",
        "column_identities_to_exclude": "columnIdentitiesToExclude",
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
        column_guids_to_boost: "Union[list[GrantaServerApiSearchBoostByGuid], None, Unset_Type]" = Unset,
        column_guids_to_exclude: "Union[list[str], None, Unset_Type]" = Unset,
        column_identities_to_boost: "Union[list[GrantaServerApiSearchBoostByIdentity], None, Unset_Type]" = Unset,
        column_identities_to_exclude: "Union[list[int], None, Unset_Type]" = Unset,
        free_text_criterion_type: "str" = "excludingLocalColumns",
        type: "str" = "text",
        value: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSearchFreeTextExcludingLocalColumnsCriterion - a model defined in Swagger

        Parameters
        ----------
        column_guids_to_boost: list[GrantaServerApiSearchBoostByGuid], optional
        column_guids_to_exclude: list[str], optional
        column_identities_to_boost: list[GrantaServerApiSearchBoostByIdentity], optional
        column_identities_to_exclude: list[int], optional
        free_text_criterion_type: str
        type: str
        value: str, optional
        """
        super().__init__(type=type, value=value)
        self._column_identities_to_boost: Union[
            list[GrantaServerApiSearchBoostByIdentity], None, Unset_Type
        ] = Unset
        self._column_identities_to_exclude: Union[list[int], None, Unset_Type] = Unset
        self._column_guids_to_boost: Union[
            list[GrantaServerApiSearchBoostByGuid], None, Unset_Type
        ] = Unset
        self._column_guids_to_exclude: Union[list[str], None, Unset_Type] = Unset
        self._free_text_criterion_type: str

        if column_identities_to_boost is not Unset:
            self.column_identities_to_boost = column_identities_to_boost
        if column_identities_to_exclude is not Unset:
            self.column_identities_to_exclude = column_identities_to_exclude
        if column_guids_to_boost is not Unset:
            self.column_guids_to_boost = column_guids_to_boost
        if column_guids_to_exclude is not Unset:
            self.column_guids_to_exclude = column_guids_to_exclude
        self.free_text_criterion_type = free_text_criterion_type

    @property
    def column_identities_to_boost(
        self,
    ) -> "Union[list[GrantaServerApiSearchBoostByIdentity], None, Unset_Type]":
        """Gets the column_identities_to_boost of this GrantaServerApiSearchFreeTextExcludingLocalColumnsCriterion.

        Returns
        -------
        Union[list[GrantaServerApiSearchBoostByIdentity], None, Unset_Type]
            The column_identities_to_boost of this GrantaServerApiSearchFreeTextExcludingLocalColumnsCriterion.
        """
        return self._column_identities_to_boost

    @column_identities_to_boost.setter
    def column_identities_to_boost(
        self,
        column_identities_to_boost: "Union[list[GrantaServerApiSearchBoostByIdentity], None, Unset_Type]",
    ) -> None:
        """Sets the column_identities_to_boost of this GrantaServerApiSearchFreeTextExcludingLocalColumnsCriterion.

        Parameters
        ----------
        column_identities_to_boost: Union[list[GrantaServerApiSearchBoostByIdentity], None, Unset_Type]
            The column_identities_to_boost of this GrantaServerApiSearchFreeTextExcludingLocalColumnsCriterion.
        """
        self._column_identities_to_boost = column_identities_to_boost

    @property
    def column_identities_to_exclude(self) -> "Union[list[int], None, Unset_Type]":
        """Gets the column_identities_to_exclude of this GrantaServerApiSearchFreeTextExcludingLocalColumnsCriterion.

        Returns
        -------
        Union[list[int], None, Unset_Type]
            The column_identities_to_exclude of this GrantaServerApiSearchFreeTextExcludingLocalColumnsCriterion.
        """
        return self._column_identities_to_exclude

    @column_identities_to_exclude.setter
    def column_identities_to_exclude(
        self, column_identities_to_exclude: "Union[list[int], None, Unset_Type]"
    ) -> None:
        """Sets the column_identities_to_exclude of this GrantaServerApiSearchFreeTextExcludingLocalColumnsCriterion.

        Parameters
        ----------
        column_identities_to_exclude: Union[list[int], None, Unset_Type]
            The column_identities_to_exclude of this GrantaServerApiSearchFreeTextExcludingLocalColumnsCriterion.
        """
        self._column_identities_to_exclude = column_identities_to_exclude

    @property
    def column_guids_to_boost(
        self,
    ) -> "Union[list[GrantaServerApiSearchBoostByGuid], None, Unset_Type]":
        """Gets the column_guids_to_boost of this GrantaServerApiSearchFreeTextExcludingLocalColumnsCriterion.

        Returns
        -------
        Union[list[GrantaServerApiSearchBoostByGuid], None, Unset_Type]
            The column_guids_to_boost of this GrantaServerApiSearchFreeTextExcludingLocalColumnsCriterion.
        """
        return self._column_guids_to_boost

    @column_guids_to_boost.setter
    def column_guids_to_boost(
        self,
        column_guids_to_boost: "Union[list[GrantaServerApiSearchBoostByGuid], None, Unset_Type]",
    ) -> None:
        """Sets the column_guids_to_boost of this GrantaServerApiSearchFreeTextExcludingLocalColumnsCriterion.

        Parameters
        ----------
        column_guids_to_boost: Union[list[GrantaServerApiSearchBoostByGuid], None, Unset_Type]
            The column_guids_to_boost of this GrantaServerApiSearchFreeTextExcludingLocalColumnsCriterion.
        """
        self._column_guids_to_boost = column_guids_to_boost

    @property
    def column_guids_to_exclude(self) -> "Union[list[str], None, Unset_Type]":
        """Gets the column_guids_to_exclude of this GrantaServerApiSearchFreeTextExcludingLocalColumnsCriterion.

        Returns
        -------
        Union[list[str], None, Unset_Type]
            The column_guids_to_exclude of this GrantaServerApiSearchFreeTextExcludingLocalColumnsCriterion.
        """
        return self._column_guids_to_exclude

    @column_guids_to_exclude.setter
    def column_guids_to_exclude(
        self, column_guids_to_exclude: "Union[list[str], None, Unset_Type]"
    ) -> None:
        """Sets the column_guids_to_exclude of this GrantaServerApiSearchFreeTextExcludingLocalColumnsCriterion.

        Parameters
        ----------
        column_guids_to_exclude: Union[list[str], None, Unset_Type]
            The column_guids_to_exclude of this GrantaServerApiSearchFreeTextExcludingLocalColumnsCriterion.
        """
        self._column_guids_to_exclude = column_guids_to_exclude

    @property
    def free_text_criterion_type(self) -> "str":
        """Gets the free_text_criterion_type of this GrantaServerApiSearchFreeTextExcludingLocalColumnsCriterion.

        Returns
        -------
        str
            The free_text_criterion_type of this GrantaServerApiSearchFreeTextExcludingLocalColumnsCriterion.
        """
        return self._free_text_criterion_type

    @free_text_criterion_type.setter
    def free_text_criterion_type(self, free_text_criterion_type: "str") -> None:
        """Sets the free_text_criterion_type of this GrantaServerApiSearchFreeTextExcludingLocalColumnsCriterion.

        Parameters
        ----------
        free_text_criterion_type: str
            The free_text_criterion_type of this GrantaServerApiSearchFreeTextExcludingLocalColumnsCriterion.
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
        if not isinstance(other, GrantaServerApiSearchFreeTextExcludingLocalColumnsCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
