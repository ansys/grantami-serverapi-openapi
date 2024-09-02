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

from ansys.grantami.serverapi_openapi.models.gsa_export_failure import (  # noqa: F401
    GsaExportFailure,
)
from ansys.grantami.serverapi_openapi.models.gsa_export_failure_type import GsaExportFailureType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaLinkExportFailure(GsaExportFailure):
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
        "failed_link": "GsaLinkReference",
        "failure_details": "str",
        "failure_reason": "str",
        "type": "GsaExportFailureType",
    }

    attribute_map: Dict[str, str] = {
        "failed_link": "failedLink",
        "failure_details": "failureDetails",
        "failure_reason": "failureReason",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {
        "failedLink": "GsaLinkReference",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        failed_link: "GsaLinkReference",
        failure_details: "str",
        failure_reason: "str",
        type: "GsaExportFailureType" = GsaExportFailureType.LINK,
    ) -> None:
        """GsaLinkExportFailure - a model defined in Swagger

        Parameters
        ----------
        failed_link: GsaLinkReference
        failure_details: str
        failure_reason: str
        type: GsaExportFailureType
        """
        super().__init__(failure_details=failure_details, failure_reason=failure_reason, type=type)
        self._failed_link: GsaLinkReference

        self.failed_link = failed_link

    @property
    def failed_link(self) -> "GsaLinkReference":
        """Gets the failed_link of this GsaLinkExportFailure.

        Returns
        -------
        GsaLinkReference
            The failed_link of this GsaLinkExportFailure.
        """
        return self._failed_link

    @failed_link.setter
    def failed_link(self, failed_link: "GsaLinkReference") -> None:
        """Sets the failed_link of this GsaLinkExportFailure.

        Parameters
        ----------
        failed_link: GsaLinkReference
            The failed_link of this GsaLinkExportFailure.
        """
        # Field is not nullable
        if failed_link is None:
            raise ValueError("Invalid value for 'failed_link', must not be 'None'")
        # Field is required
        if failed_link is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'failed_link', must not be 'Unset'")
        self._failed_link = failed_link

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
        if not isinstance(other, GsaLinkExportFailure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
