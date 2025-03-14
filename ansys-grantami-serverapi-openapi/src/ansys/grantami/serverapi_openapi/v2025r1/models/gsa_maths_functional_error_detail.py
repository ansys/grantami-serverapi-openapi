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


class GsaMathsFunctionalErrorDetail(ModelBase):
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
    discriminator_class_map: dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "message": "str",
        "reason": "GsaMathsFunctionalErrorReason",
    }

    attribute_map: dict[str, str] = {
        "message": "message",
        "reason": "reason",
    }

    subtype_mapping: dict[str, str] = {
        "reason": "GsaMathsFunctionalErrorReason",
    }

    discriminator_value_class_map = {
        "anonymousExpressionsMustAllowAllCompatible".lower(): "#/components/schemas/GsaAnonymousExpressionsMustAllowAllCompatibleMathsFunctionalErrorDetail",
        "defaultExpressionNotFound".lower(): "#/components/schemas/GsaDefaultExpressionNotFoundMathsFunctionalErrorDetail",
        "defaultFreeParameterNotFound".lower(): "#/components/schemas/GsaDefaultFreeParameterNotFoundMathsFunctionalErrorDetail",
        "duplicateExpressionGuids".lower(): "#/components/schemas/GsaDuplicateExpressionGuidsMathsFunctionalErrorDetail",
        "expression".lower(): "#/components/schemas/GsaExpressionMathsFunctionalErrorDetail",
        "expressionsHaveUnknownParameters".lower(): "#/components/schemas/GsaExpressionsHaveUnknownParametersMathsFunctionalErrorDetail",
        "noExpressions".lower(): "#/components/schemas/GsaNoExpressionsMathsFunctionalErrorDetail",
        "noSuchExpressions".lower(): "#/components/schemas/GsaNoSuchExpressionsMathsFunctionalErrorDetail",
        "parameterContent".lower(): "#/components/schemas/GsaParameterContentMathsFunctionalErrorDetail",
        "parameterContentDuplicateGuids".lower(): "#/components/schemas/GsaParameterContentDuplicateGuidsMathsFunctionalErrorDetail",
        "parameterContentUnknownParameters".lower(): "#/components/schemas/GsaParameterContentUnknownParametersMathsFunctionalErrorDetail",
    }

    discriminator: Optional[str] = "reason"

    def __init__(
        self,
        *,
        message: "str",
        reason: "GsaMathsFunctionalErrorReason",
    ) -> None:
        """GsaMathsFunctionalErrorDetail - a model defined in Swagger

        Parameters
        ----------
        message: str
        reason: GsaMathsFunctionalErrorReason
        """
        self._message: str
        self._reason: GsaMathsFunctionalErrorReason

        self.message = message
        self.reason = reason

    @property
    def message(self) -> "str":
        """Gets the message of this GsaMathsFunctionalErrorDetail.

        Returns
        -------
        str
            The message of this GsaMathsFunctionalErrorDetail.
        """
        return self._message

    @message.setter
    def message(self, message: "str") -> None:
        """Sets the message of this GsaMathsFunctionalErrorDetail.

        Parameters
        ----------
        message: str
            The message of this GsaMathsFunctionalErrorDetail.
        """
        # Field is not nullable
        if message is None:
            raise ValueError("Invalid value for 'message', must not be 'None'")
        # Field is required
        if message is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'message', must not be 'Unset'")
        self._message = message

    @property
    def reason(self) -> "GsaMathsFunctionalErrorReason":
        """Gets the reason of this GsaMathsFunctionalErrorDetail.

        Returns
        -------
        GsaMathsFunctionalErrorReason
            The reason of this GsaMathsFunctionalErrorDetail.
        """
        return self._reason

    @reason.setter
    def reason(self, reason: "GsaMathsFunctionalErrorReason") -> None:
        """Sets the reason of this GsaMathsFunctionalErrorDetail.

        Parameters
        ----------
        reason: GsaMathsFunctionalErrorReason
            The reason of this GsaMathsFunctionalErrorDetail.
        """
        # Field is not nullable
        if reason is None:
            raise ValueError("Invalid value for 'reason', must not be 'None'")
        # Field is required
        if reason is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'reason', must not be 'Unset'")
        self._reason = reason

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[cls._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen,
        # so we have to extract it from the JSON reference
        return cls.discriminator_value_class_map[discriminator_value].rsplit("/", 1)[-1]

    @classmethod
    def _get_discriminator_field_name(cls) -> str:
        assert cls.discriminator
        name_tokens = cls.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GsaMathsFunctionalErrorDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
