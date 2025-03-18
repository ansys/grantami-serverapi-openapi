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

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaUpdateProfileTable(ModelBase):
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
        "guid": "str",
        "layout_guid": "str",
        "subset_guid": "str",
    }

    attribute_map: dict[str, str] = {
        "guid": "guid",
        "layout_guid": "layoutGuid",
        "subset_guid": "subsetGuid",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        guid: "Union[str, Unset_Type]" = Unset,
        layout_guid: "Union[str, None, Unset_Type]" = Unset,
        subset_guid: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaUpdateProfileTable - a model defined in Swagger

        Parameters
        ----------
        guid: str, optional
        layout_guid: str, optional
        subset_guid: str, optional
        """
        self._subset_guid: Union[str, None, Unset_Type] = Unset
        self._layout_guid: Union[str, None, Unset_Type] = Unset
        self._guid: Union[str, Unset_Type] = Unset

        if subset_guid is not Unset:
            self.subset_guid = subset_guid
        if layout_guid is not Unset:
            self.layout_guid = layout_guid
        if guid is not Unset:
            self.guid = guid

    @property
    def subset_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the subset_guid of this GsaUpdateProfileTable.

        Returns
        -------
        Union[str, None, Unset_Type]
            The subset_guid of this GsaUpdateProfileTable.
        """
        return self._subset_guid

    @subset_guid.setter
    def subset_guid(self, subset_guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the subset_guid of this GsaUpdateProfileTable.

        Parameters
        ----------
        subset_guid: Union[str, None, Unset_Type]
            The subset_guid of this GsaUpdateProfileTable.
        """
        self._subset_guid = subset_guid

    @property
    def layout_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the layout_guid of this GsaUpdateProfileTable.

        Returns
        -------
        Union[str, None, Unset_Type]
            The layout_guid of this GsaUpdateProfileTable.
        """
        return self._layout_guid

    @layout_guid.setter
    def layout_guid(self, layout_guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the layout_guid of this GsaUpdateProfileTable.

        Parameters
        ----------
        layout_guid: Union[str, None, Unset_Type]
            The layout_guid of this GsaUpdateProfileTable.
        """
        self._layout_guid = layout_guid

    @property
    def guid(self) -> "Union[str, Unset_Type]":
        """Gets the guid of this GsaUpdateProfileTable.

        Returns
        -------
        Union[str, Unset_Type]
            The guid of this GsaUpdateProfileTable.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, Unset_Type]") -> None:
        """Sets the guid of this GsaUpdateProfileTable.

        Parameters
        ----------
        guid: Union[str, Unset_Type]
            The guid of this GsaUpdateProfileTable.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        self._guid = guid

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
        if not isinstance(other, GsaUpdateProfileTable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
