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


class GsaResolvedLinkInfo(ModelBase):
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
        "link_source": "GsaResolvedLinkTarget",
        "link_target": "GsaResolvedLinkTarget",
    }

    attribute_map: dict[str, str] = {
        "link_source": "linkSource",
        "link_target": "linkTarget",
    }

    subtype_mapping: dict[str, str] = {
        "linkSource": "GsaResolvedLinkTarget",
        "linkTarget": "GsaResolvedLinkTarget",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        link_source: "GsaResolvedLinkTarget",
        link_target: "GsaResolvedLinkTarget",
    ) -> None:
        """GsaResolvedLinkInfo - a model defined in Swagger

        Parameters
        ----------
        link_source: GsaResolvedLinkTarget
        link_target: GsaResolvedLinkTarget
        """
        self._link_source: GsaResolvedLinkTarget
        self._link_target: GsaResolvedLinkTarget

        self.link_source = link_source
        self.link_target = link_target

    @property
    def link_source(self) -> "GsaResolvedLinkTarget":
        """Gets the link_source of this GsaResolvedLinkInfo.

        Returns
        -------
        GsaResolvedLinkTarget
            The link_source of this GsaResolvedLinkInfo.
        """
        return self._link_source

    @link_source.setter
    def link_source(self, link_source: "GsaResolvedLinkTarget") -> None:
        """Sets the link_source of this GsaResolvedLinkInfo.

        Parameters
        ----------
        link_source: GsaResolvedLinkTarget
            The link_source of this GsaResolvedLinkInfo.
        """
        # Field is not nullable
        if link_source is None:
            raise ValueError("Invalid value for 'link_source', must not be 'None'")
        # Field is required
        if link_source is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'link_source', must not be 'Unset'")
        self._link_source = link_source

    @property
    def link_target(self) -> "GsaResolvedLinkTarget":
        """Gets the link_target of this GsaResolvedLinkInfo.

        Returns
        -------
        GsaResolvedLinkTarget
            The link_target of this GsaResolvedLinkInfo.
        """
        return self._link_target

    @link_target.setter
    def link_target(self, link_target: "GsaResolvedLinkTarget") -> None:
        """Sets the link_target of this GsaResolvedLinkInfo.

        Parameters
        ----------
        link_target: GsaResolvedLinkTarget
            The link_target of this GsaResolvedLinkInfo.
        """
        # Field is not nullable
        if link_target is None:
            raise ValueError("Invalid value for 'link_target', must not be 'None'")
        # Field is required
        if link_target is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'link_target', must not be 'Unset'")
        self._link_target = link_target

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
        if not isinstance(other, GsaResolvedLinkInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
