# Copyright (C) 2021 - 2024 ANSYS, Inc. and/or its affiliates.
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

from ansys.grantami.serverapi_openapi.models.granta_server_api_exceptions_version_control_version_control_error_detail import (  # noqa: F401
    GrantaServerApiExceptionsVersionControlVersionControlErrorDetail,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiExceptionsVersionControlNotTheLatestVersionErrorDetail(
    GrantaServerApiExceptionsVersionControlVersionControlErrorDetail
):
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
        "message": "str",
        "newer_version": "GrantaServerApiRecordsRecordVersionsSlimRecordVersion",
        "reason": "str",
    }

    attribute_map: Dict[str, str] = {
        "message": "message",
        "newer_version": "newerVersion",
        "reason": "reason",
    }

    subtype_mapping: Dict[str, str] = {
        "newerVersion": "GrantaServerApiRecordsRecordVersionsSlimRecordVersion",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        message: "str",
        newer_version: "Union[GrantaServerApiRecordsRecordVersionsSlimRecordVersion, Unset_Type]" = Unset,
        reason: "str" = "notTheLatestVersion",
    ) -> None:
        """GrantaServerApiExceptionsVersionControlNotTheLatestVersionErrorDetail - a model defined in Swagger

        Parameters
        ----------
        message: str
        newer_version: GrantaServerApiRecordsRecordVersionsSlimRecordVersion, optional
        reason: str
        """
        super().__init__(message=message)
        self._newer_version: Union[
            GrantaServerApiRecordsRecordVersionsSlimRecordVersion, Unset_Type
        ] = Unset
        self._reason: str

        if newer_version is not Unset:
            self.newer_version = newer_version
        self.reason = reason

    @property
    def newer_version(
        self,
    ) -> "Union[GrantaServerApiRecordsRecordVersionsSlimRecordVersion, Unset_Type]":
        """Gets the newer_version of this GrantaServerApiExceptionsVersionControlNotTheLatestVersionErrorDetail.

        Returns
        -------
        Union[GrantaServerApiRecordsRecordVersionsSlimRecordVersion, Unset_Type]
            The newer_version of this GrantaServerApiExceptionsVersionControlNotTheLatestVersionErrorDetail.
        """
        return self._newer_version

    @newer_version.setter
    def newer_version(
        self,
        newer_version: "Union[GrantaServerApiRecordsRecordVersionsSlimRecordVersion, Unset_Type]",
    ) -> None:
        """Sets the newer_version of this GrantaServerApiExceptionsVersionControlNotTheLatestVersionErrorDetail.

        Parameters
        ----------
        newer_version: Union[GrantaServerApiRecordsRecordVersionsSlimRecordVersion, Unset_Type]
            The newer_version of this GrantaServerApiExceptionsVersionControlNotTheLatestVersionErrorDetail.
        """
        # Field is not nullable
        if newer_version is None:
            raise ValueError("Invalid value for 'newer_version', must not be 'None'")
        self._newer_version = newer_version

    @property
    def reason(self) -> "str":
        """Gets the reason of this GrantaServerApiExceptionsVersionControlNotTheLatestVersionErrorDetail.

        Returns
        -------
        str
            The reason of this GrantaServerApiExceptionsVersionControlNotTheLatestVersionErrorDetail.
        """
        return self._reason

    @reason.setter
    def reason(self, reason: "str") -> None:
        """Sets the reason of this GrantaServerApiExceptionsVersionControlNotTheLatestVersionErrorDetail.

        Parameters
        ----------
        reason: str
            The reason of this GrantaServerApiExceptionsVersionControlNotTheLatestVersionErrorDetail.
        """
        # Field is not nullable
        if reason is None:
            raise ValueError("Invalid value for 'reason', must not be 'None'")
        # Field is required
        if reason is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'reason', must not be 'Unset'")
        self._reason = reason

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
        if not isinstance(
            other, GrantaServerApiExceptionsVersionControlNotTheLatestVersionErrorDetail
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
