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


class GsaReleaseRecordVersionControlException(ModelBase):
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
        "code": "SystemNetHttpStatusCode",
        "errors": "list[GsaVersionControlErrorDetail]",
        "message": "str",
    }

    attribute_map: Dict[str, str] = {
        "code": "code",
        "errors": "errors",
        "message": "message",
    }

    subtype_mapping: Dict[str, str] = {
        "code": "SystemNetHttpStatusCode",
        "errors": "GsaVersionControlErrorDetail",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        code: "Union[SystemNetHttpStatusCode, Unset_Type]" = Unset,
        errors: "Union[List[GsaVersionControlErrorDetail], None, Unset_Type]" = Unset,
        message: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaReleaseRecordVersionControlException - a model defined in Swagger

        Parameters
        ----------
        code: SystemNetHttpStatusCode, optional
        errors: List[GsaVersionControlErrorDetail], optional
        message: str, optional
        """
        self._message: Union[str, None, Unset_Type] = Unset
        self._code: Union[SystemNetHttpStatusCode, Unset_Type] = Unset
        self._errors: Union[List[GsaVersionControlErrorDetail], None, Unset_Type] = Unset

        if message is not Unset:
            self.message = message
        if code is not Unset:
            self.code = code
        if errors is not Unset:
            self.errors = errors

    @property
    def message(self) -> "Union[str, None, Unset_Type]":
        """Gets the message of this GsaReleaseRecordVersionControlException.

        Returns
        -------
        Union[str, None, Unset_Type]
            The message of this GsaReleaseRecordVersionControlException.
        """
        return self._message

    @message.setter
    def message(self, message: "Union[str, None, Unset_Type]") -> None:
        """Sets the message of this GsaReleaseRecordVersionControlException.

        Parameters
        ----------
        message: Union[str, None, Unset_Type]
            The message of this GsaReleaseRecordVersionControlException.
        """
        self._message = message

    @property
    def code(self) -> "Union[SystemNetHttpStatusCode, Unset_Type]":
        """Gets the code of this GsaReleaseRecordVersionControlException.

        Returns
        -------
        Union[SystemNetHttpStatusCode, Unset_Type]
            The code of this GsaReleaseRecordVersionControlException.
        """
        return self._code

    @code.setter
    def code(self, code: "Union[SystemNetHttpStatusCode, Unset_Type]") -> None:
        """Sets the code of this GsaReleaseRecordVersionControlException.

        Parameters
        ----------
        code: Union[SystemNetHttpStatusCode, Unset_Type]
            The code of this GsaReleaseRecordVersionControlException.
        """
        # Field is not nullable
        if code is None:
            raise ValueError("Invalid value for 'code', must not be 'None'")
        self._code = code

    @property
    def errors(self) -> "Union[List[GsaVersionControlErrorDetail], None, Unset_Type]":
        """Gets the errors of this GsaReleaseRecordVersionControlException.

        Returns
        -------
        Union[List[GsaVersionControlErrorDetail], None, Unset_Type]
            The errors of this GsaReleaseRecordVersionControlException.
        """
        return self._errors

    @errors.setter
    def errors(self, errors: "Union[List[GsaVersionControlErrorDetail], None, Unset_Type]") -> None:
        """Sets the errors of this GsaReleaseRecordVersionControlException.

        Parameters
        ----------
        errors: Union[List[GsaVersionControlErrorDetail], None, Unset_Type]
            The errors of this GsaReleaseRecordVersionControlException.
        """
        self._errors = errors

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
        if not isinstance(other, GsaReleaseRecordVersionControlException):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
