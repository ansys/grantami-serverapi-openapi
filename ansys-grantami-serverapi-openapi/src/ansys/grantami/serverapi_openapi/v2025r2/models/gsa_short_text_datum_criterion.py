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

from ansys.grantami.serverapi_openapi.v2025r2.models.gsa_datum_criterion import (  # noqa: F401
    GsaDatumCriterion,
)
from ansys.grantami.serverapi_openapi.v2025r2.models.gsa_datum_criterion_type import (
    GsaDatumCriterionType,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaShortTextDatumCriterion(GsaDatumCriterion):
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
        "type": "GsaDatumCriterionType",
        "value": "str",
        "text_match_behavior": "GsaTextMatchBehavior",
    }

    attribute_map: dict[str, str] = {
        "type": "type",
        "value": "value",
        "text_match_behavior": "textMatchBehavior",
    }

    subtype_mapping: dict[str, str] = {
        "textMatchBehavior": "GsaTextMatchBehavior",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        type: "GsaDatumCriterionType" = GsaDatumCriterionType.SHORTTEXT,
        value: "str",
        text_match_behavior: "Union[GsaTextMatchBehavior, Unset_Type]" = Unset,
    ) -> None:
        """GsaShortTextDatumCriterion - a model defined in Swagger

        Parameters
        ----------
        type: GsaDatumCriterionType
        value: str
        text_match_behavior: GsaTextMatchBehavior, optional
        """
        super().__init__(type=type)
        self._value: str
        self._text_match_behavior: Union[GsaTextMatchBehavior, Unset_Type] = Unset

        self.value = value
        if text_match_behavior is not Unset:
            self.text_match_behavior = text_match_behavior

    @property
    def value(self) -> "str":
        """Gets the value of this GsaShortTextDatumCriterion.

        Returns
        -------
        str
            The value of this GsaShortTextDatumCriterion.
        """
        return self._value

    @value.setter
    def value(self, value: "str") -> None:
        """Sets the value of this GsaShortTextDatumCriterion.

        Parameters
        ----------
        value: str
            The value of this GsaShortTextDatumCriterion.
        """
        # Field is not nullable
        if value is None:
            raise ValueError("Invalid value for 'value', must not be 'None'")
        # Field is required
        if value is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'value', must not be 'Unset'")
        self._value = value

    @property
    def text_match_behavior(self) -> "Union[GsaTextMatchBehavior, Unset_Type]":
        """Gets the text_match_behavior of this GsaShortTextDatumCriterion.

        Returns
        -------
        Union[GsaTextMatchBehavior, Unset_Type]
            The text_match_behavior of this GsaShortTextDatumCriterion.
        """
        return self._text_match_behavior

    @text_match_behavior.setter
    def text_match_behavior(
        self, text_match_behavior: "Union[GsaTextMatchBehavior, Unset_Type]"
    ) -> None:
        """Sets the text_match_behavior of this GsaShortTextDatumCriterion.

        Parameters
        ----------
        text_match_behavior: Union[GsaTextMatchBehavior, Unset_Type]
            The text_match_behavior of this GsaShortTextDatumCriterion.
        """
        # Field is not nullable
        if text_match_behavior is None:
            raise ValueError("Invalid value for 'text_match_behavior', must not be 'None'")
        self._text_match_behavior = text_match_behavior

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
        if not isinstance(other, GsaShortTextDatumCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
