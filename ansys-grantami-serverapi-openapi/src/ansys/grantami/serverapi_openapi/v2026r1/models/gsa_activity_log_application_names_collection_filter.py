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


class GsaActivityLogApplicationNamesCollectionFilter(ModelBase):
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
        "application_names_to_match": "list[str]",
        "collection_match_type": "GsaActivityLogCollectionMatchType",
    }

    attribute_map: dict[str, str] = {
        "application_names_to_match": "applicationNamesToMatch",
        "collection_match_type": "collectionMatchType",
    }

    subtype_mapping: dict[str, str] = {
        "collectionMatchType": "GsaActivityLogCollectionMatchType",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        application_names_to_match: "list[str]",
        collection_match_type: "GsaActivityLogCollectionMatchType | Unset_Type" = Unset,
    ) -> None:
        """GsaActivityLogApplicationNamesCollectionFilter - a model defined in Swagger

        Parameters
        ----------
        application_names_to_match: list[str]
        collection_match_type: GsaActivityLogCollectionMatchType, optional
        """
        self._application_names_to_match: list[str]
        self._collection_match_type: GsaActivityLogCollectionMatchType | Unset_Type = Unset

        self.application_names_to_match = application_names_to_match
        if collection_match_type is not Unset:
            self.collection_match_type = collection_match_type

    @property
    def application_names_to_match(self) -> "list[str]":
        """Gets the application_names_to_match of this GsaActivityLogApplicationNamesCollectionFilter.

        Returns
        -------
        list[str]
            The application_names_to_match of this GsaActivityLogApplicationNamesCollectionFilter.
        """
        return self._application_names_to_match

    @application_names_to_match.setter
    def application_names_to_match(self, application_names_to_match: "list[str]") -> None:
        """Sets the application_names_to_match of this GsaActivityLogApplicationNamesCollectionFilter.

        Parameters
        ----------
        application_names_to_match: list[str]
            The application_names_to_match of this GsaActivityLogApplicationNamesCollectionFilter.
        """
        # Field is not nullable
        if application_names_to_match is None:
            raise ValueError("Invalid value for 'application_names_to_match', must not be 'None'")
        # Field is required
        if application_names_to_match is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'application_names_to_match', must not be 'Unset'")
        self._application_names_to_match = application_names_to_match

    @property
    def collection_match_type(self) -> "GsaActivityLogCollectionMatchType | Unset_Type":
        """Gets the collection_match_type of this GsaActivityLogApplicationNamesCollectionFilter.

        Returns
        -------
        GsaActivityLogCollectionMatchType | Unset_Type
            The collection_match_type of this GsaActivityLogApplicationNamesCollectionFilter.
        """
        return self._collection_match_type

    @collection_match_type.setter
    def collection_match_type(
        self, collection_match_type: "GsaActivityLogCollectionMatchType | Unset_Type"
    ) -> None:
        """Sets the collection_match_type of this GsaActivityLogApplicationNamesCollectionFilter.

        Parameters
        ----------
        collection_match_type: GsaActivityLogCollectionMatchType | Unset_Type
            The collection_match_type of this GsaActivityLogApplicationNamesCollectionFilter.
        """
        # Field is not nullable
        if collection_match_type is None:
            raise ValueError("Invalid value for 'collection_match_type', must not be 'None'")
        self._collection_match_type = collection_match_type

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
        if not isinstance(other, GsaActivityLogApplicationNamesCollectionFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
