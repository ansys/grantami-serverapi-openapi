# Copyright (C) 2023 - 2024 ANSYS, Inc. and/or its affiliates.
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
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaQueryAttributeInfoProperties(ModelBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes
    ----------
    swagger_types: Dict[str, str]
        The key is attribute name and the value is attribute type.
    attribute_map: Dict[str, str]
        The key is attribute name and the value is json key in definition.
    subtype_mapping: Dict[str, str]
        The key is the unmangled property name and the value is the corresponding type.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: Dict[str, str] = {
        "chartable": "bool",
        "ordered_meta_attributes": "GsaQuerySlimNamedEntityProperties",
    }

    attribute_map: Dict[str, str] = {
        "chartable": "chartable",
        "ordered_meta_attributes": "orderedMetaAttributes",
    }

    subtype_mapping: Dict[str, str] = {
        "orderedMetaAttributes": "GsaQuerySlimNamedEntityProperties",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        chartable: "Union[bool, None, Unset_Type]" = Unset,
        ordered_meta_attributes: "Union[GsaQuerySlimNamedEntityProperties, Unset_Type]" = Unset,
    ) -> None:
        """GsaQueryAttributeInfoProperties - a model defined in Swagger

        Parameters
        ----------
        chartable: bool, optional
        ordered_meta_attributes: GsaQuerySlimNamedEntityProperties, optional
        """
        self._chartable: Union[bool, None, Unset_Type] = Unset
        self._ordered_meta_attributes: Union[GsaQuerySlimNamedEntityProperties, Unset_Type] = Unset

        if chartable is not Unset:
            self.chartable = chartable
        if ordered_meta_attributes is not Unset:
            self.ordered_meta_attributes = ordered_meta_attributes

    @property
    def chartable(self) -> "Union[bool, None, Unset_Type]":
        """Gets the chartable of this GsaQueryAttributeInfoProperties.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The chartable of this GsaQueryAttributeInfoProperties.
        """
        return self._chartable

    @chartable.setter
    def chartable(self, chartable: "Union[bool, None, Unset_Type]") -> None:
        """Sets the chartable of this GsaQueryAttributeInfoProperties.

        Parameters
        ----------
        chartable: Union[bool, None, Unset_Type]
            The chartable of this GsaQueryAttributeInfoProperties.
        """
        self._chartable = chartable

    @property
    def ordered_meta_attributes(self) -> "Union[GsaQuerySlimNamedEntityProperties, Unset_Type]":
        """Gets the ordered_meta_attributes of this GsaQueryAttributeInfoProperties.

        Returns
        -------
        Union[GsaQuerySlimNamedEntityProperties, Unset_Type]
            The ordered_meta_attributes of this GsaQueryAttributeInfoProperties.
        """
        return self._ordered_meta_attributes

    @ordered_meta_attributes.setter
    def ordered_meta_attributes(
        self, ordered_meta_attributes: "Union[GsaQuerySlimNamedEntityProperties, Unset_Type]"
    ) -> None:
        """Sets the ordered_meta_attributes of this GsaQueryAttributeInfoProperties.

        Parameters
        ----------
        ordered_meta_attributes: Union[GsaQuerySlimNamedEntityProperties, Unset_Type]
            The ordered_meta_attributes of this GsaQueryAttributeInfoProperties.
        """
        # Field is not nullable
        if ordered_meta_attributes is None:
            raise ValueError("Invalid value for 'ordered_meta_attributes', must not be 'None'")
        self._ordered_meta_attributes = ordered_meta_attributes

    @classmethod
    def get_real_child_model(cls, data: Dict[str, str]) -> str:
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
        if not isinstance(other, GsaQueryAttributeInfoProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
