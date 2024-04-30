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

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiAsyncJobsUpdateJobRequest(ModelBase):
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
        "description": "str",
        "name": "str",
        "scheduled_execution_date": "datetime",
        "status": "GrantaServerApiAsyncJobsJobStatus",
    }

    attribute_map: Dict[str, str] = {
        "description": "description",
        "name": "name",
        "scheduled_execution_date": "scheduledExecutionDate",
        "status": "status",
    }

    subtype_mapping: Dict[str, str] = {
        "status": "GrantaServerApiAsyncJobsJobStatus",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        description: "Union[str, None, Unset_Type]" = Unset,
        name: "Union[str, None, Unset_Type]" = Unset,
        scheduled_execution_date: "Union[datetime, None, Unset_Type]" = Unset,
        status: "Union[GrantaServerApiAsyncJobsJobStatus, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiAsyncJobsUpdateJobRequest - a model defined in Swagger

        Parameters
        ----------
        description: str, optional
        name: str, optional
        scheduled_execution_date: datetime, optional
        status: GrantaServerApiAsyncJobsJobStatus, optional
        """
        self._name: Union[str, None, Unset_Type] = Unset
        self._description: Union[str, None, Unset_Type] = Unset
        self._scheduled_execution_date: Union[datetime, None, Unset_Type] = Unset
        self._status: Union[GrantaServerApiAsyncJobsJobStatus, Unset_Type] = Unset

        if name is not Unset:
            self.name = name
        if description is not Unset:
            self.description = description
        if scheduled_execution_date is not Unset:
            self.scheduled_execution_date = scheduled_execution_date
        if status is not Unset:
            self.status = status

    @property
    def name(self) -> "Union[str, None, Unset_Type]":
        """Gets the name of this GrantaServerApiAsyncJobsUpdateJobRequest.

        Returns
        -------
        Union[str, None, Unset_Type]
            The name of this GrantaServerApiAsyncJobsUpdateJobRequest.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, None, Unset_Type]") -> None:
        """Sets the name of this GrantaServerApiAsyncJobsUpdateJobRequest.

        Parameters
        ----------
        name: Union[str, None, Unset_Type]
            The name of this GrantaServerApiAsyncJobsUpdateJobRequest.
        """
        self._name = name

    @property
    def description(self) -> "Union[str, None, Unset_Type]":
        """Gets the description of this GrantaServerApiAsyncJobsUpdateJobRequest.

        Returns
        -------
        Union[str, None, Unset_Type]
            The description of this GrantaServerApiAsyncJobsUpdateJobRequest.
        """
        return self._description

    @description.setter
    def description(self, description: "Union[str, None, Unset_Type]") -> None:
        """Sets the description of this GrantaServerApiAsyncJobsUpdateJobRequest.

        Parameters
        ----------
        description: Union[str, None, Unset_Type]
            The description of this GrantaServerApiAsyncJobsUpdateJobRequest.
        """
        self._description = description

    @property
    def scheduled_execution_date(self) -> "Union[datetime, None, Unset_Type]":
        """Gets the scheduled_execution_date of this GrantaServerApiAsyncJobsUpdateJobRequest.

        Returns
        -------
        Union[datetime, None, Unset_Type]
            The scheduled_execution_date of this GrantaServerApiAsyncJobsUpdateJobRequest.
        """
        return self._scheduled_execution_date

    @scheduled_execution_date.setter
    def scheduled_execution_date(
        self, scheduled_execution_date: "Union[datetime, None, Unset_Type]"
    ) -> None:
        """Sets the scheduled_execution_date of this GrantaServerApiAsyncJobsUpdateJobRequest.

        Parameters
        ----------
        scheduled_execution_date: Union[datetime, None, Unset_Type]
            The scheduled_execution_date of this GrantaServerApiAsyncJobsUpdateJobRequest.
        """
        self._scheduled_execution_date = scheduled_execution_date

    @property
    def status(self) -> "Union[GrantaServerApiAsyncJobsJobStatus, Unset_Type]":
        """Gets the status of this GrantaServerApiAsyncJobsUpdateJobRequest.

        Returns
        -------
        Union[GrantaServerApiAsyncJobsJobStatus, Unset_Type]
            The status of this GrantaServerApiAsyncJobsUpdateJobRequest.
        """
        return self._status

    @status.setter
    def status(self, status: "Union[GrantaServerApiAsyncJobsJobStatus, Unset_Type]") -> None:
        """Sets the status of this GrantaServerApiAsyncJobsUpdateJobRequest.

        Parameters
        ----------
        status: Union[GrantaServerApiAsyncJobsJobStatus, Unset_Type]
            The status of this GrantaServerApiAsyncJobsUpdateJobRequest.
        """
        # Field is not nullable
        if status is None:
            raise ValueError("Invalid value for 'status', must not be 'None'")
        self._status = status

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
        if not isinstance(other, GrantaServerApiAsyncJobsUpdateJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
