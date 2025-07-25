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


class GsaJob(ModelBase):
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
        "completion_date": "datetime",
        "description": "str",
        "execution_date": "datetime",
        "id": "str",
        "input_file_ids": "list[str]",
        "job_specific_outputs": "dict(str, object)",
        "name": "str",
        "output_file_names": "list[str]",
        "position": "int",
        "scheduled_execution_date": "datetime",
        "status": "GsaJobStatus",
        "submission_date": "datetime",
        "submitter_name": "str",
        "submitter_roles": "list[str]",
        "type": "str",
    }

    attribute_map: dict[str, str] = {
        "completion_date": "completionDate",
        "description": "description",
        "execution_date": "executionDate",
        "id": "id",
        "input_file_ids": "inputFileIds",
        "job_specific_outputs": "jobSpecificOutputs",
        "name": "name",
        "output_file_names": "outputFileNames",
        "position": "position",
        "scheduled_execution_date": "scheduledExecutionDate",
        "status": "status",
        "submission_date": "submissionDate",
        "submitter_name": "submitterName",
        "submitter_roles": "submitterRoles",
        "type": "type",
    }

    subtype_mapping: dict[str, str] = {
        "status": "GsaJobStatus",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        completion_date: "datetime | None | Unset_Type" = Unset,
        description: "str | None | Unset_Type" = Unset,
        execution_date: "datetime | None | Unset_Type" = Unset,
        id: "str | Unset_Type" = Unset,
        input_file_ids: "list[str] | None | Unset_Type" = Unset,
        job_specific_outputs: "dict[str, object] | None | Unset_Type" = Unset,
        name: "str | None | Unset_Type" = Unset,
        output_file_names: "list[str] | None | Unset_Type" = Unset,
        position: "int | None | Unset_Type" = Unset,
        scheduled_execution_date: "datetime | None | Unset_Type" = Unset,
        status: "GsaJobStatus | Unset_Type" = Unset,
        submission_date: "datetime | None | Unset_Type" = Unset,
        submitter_name: "str | None | Unset_Type" = Unset,
        submitter_roles: "list[str] | None | Unset_Type" = Unset,
        type: "str | None | Unset_Type" = Unset,
    ) -> None:
        """GsaJob - a model defined in Swagger

        Parameters
        ----------
        completion_date: datetime | None, optional
        description: str | None, optional
        execution_date: datetime | None, optional
        id: str, optional
        input_file_ids: list[str] | None, optional
        job_specific_outputs: dict[str, object] | None, optional
        name: str | None, optional
        output_file_names: list[str] | None, optional
        position: int | None, optional
        scheduled_execution_date: datetime | None, optional
        status: GsaJobStatus, optional
        submission_date: datetime | None, optional
        submitter_name: str | None, optional
        submitter_roles: list[str] | None, optional
        type: str | None, optional
        """
        self._id: str | Unset_Type = Unset
        self._name: str | None | Unset_Type = Unset
        self._description: str | None | Unset_Type = Unset
        self._type: str | None | Unset_Type = Unset
        self._submitter_name: str | None | Unset_Type = Unset
        self._submitter_roles: list[str] | None | Unset_Type = Unset
        self._submission_date: datetime | None | Unset_Type = Unset
        self._scheduled_execution_date: datetime | None | Unset_Type = Unset
        self._execution_date: datetime | None | Unset_Type = Unset
        self._completion_date: datetime | None | Unset_Type = Unset
        self._status: GsaJobStatus | Unset_Type = Unset
        self._input_file_ids: list[str] | None | Unset_Type = Unset
        self._output_file_names: list[str] | None | Unset_Type = Unset
        self._position: int | None | Unset_Type = Unset
        self._job_specific_outputs: dict[str, object] | None | Unset_Type = Unset

        if id is not Unset:
            self.id = id
        if name is not Unset:
            self.name = name
        if description is not Unset:
            self.description = description
        if type is not Unset:
            self.type = type
        if submitter_name is not Unset:
            self.submitter_name = submitter_name
        if submitter_roles is not Unset:
            self.submitter_roles = submitter_roles
        if submission_date is not Unset:
            self.submission_date = submission_date
        if scheduled_execution_date is not Unset:
            self.scheduled_execution_date = scheduled_execution_date
        if execution_date is not Unset:
            self.execution_date = execution_date
        if completion_date is not Unset:
            self.completion_date = completion_date
        if status is not Unset:
            self.status = status
        if input_file_ids is not Unset:
            self.input_file_ids = input_file_ids
        if output_file_names is not Unset:
            self.output_file_names = output_file_names
        if position is not Unset:
            self.position = position
        if job_specific_outputs is not Unset:
            self.job_specific_outputs = job_specific_outputs

    @property
    def id(self) -> "str | Unset_Type":
        """Gets the id of this GsaJob.

        Returns
        -------
        str | Unset_Type
            The id of this GsaJob.
        """
        return self._id

    @id.setter
    def id(self, id: "str | Unset_Type") -> None:
        """Sets the id of this GsaJob.

        Parameters
        ----------
        id: str | Unset_Type
            The id of this GsaJob.
        """
        # Field is not nullable
        if id is None:
            raise ValueError("Invalid value for 'id', must not be 'None'")
        self._id = id

    @property
    def name(self) -> "str | None | Unset_Type":
        """Gets the name of this GsaJob.

        Returns
        -------
        str | None | Unset_Type
            The name of this GsaJob.
        """
        return self._name

    @name.setter
    def name(self, name: "str | None | Unset_Type") -> None:
        """Sets the name of this GsaJob.

        Parameters
        ----------
        name: str | None | Unset_Type
            The name of this GsaJob.
        """
        self._name = name

    @property
    def description(self) -> "str | None | Unset_Type":
        """Gets the description of this GsaJob.

        Returns
        -------
        str | None | Unset_Type
            The description of this GsaJob.
        """
        return self._description

    @description.setter
    def description(self, description: "str | None | Unset_Type") -> None:
        """Sets the description of this GsaJob.

        Parameters
        ----------
        description: str | None | Unset_Type
            The description of this GsaJob.
        """
        self._description = description

    @property
    def type(self) -> "str | None | Unset_Type":
        """Gets the type of this GsaJob.

        Returns
        -------
        str | None | Unset_Type
            The type of this GsaJob.
        """
        return self._type

    @type.setter
    def type(self, type: "str | None | Unset_Type") -> None:
        """Sets the type of this GsaJob.

        Parameters
        ----------
        type: str | None | Unset_Type
            The type of this GsaJob.
        """
        self._type = type

    @property
    def submitter_name(self) -> "str | None | Unset_Type":
        """Gets the submitter_name of this GsaJob.

        Returns
        -------
        str | None | Unset_Type
            The submitter_name of this GsaJob.
        """
        return self._submitter_name

    @submitter_name.setter
    def submitter_name(self, submitter_name: "str | None | Unset_Type") -> None:
        """Sets the submitter_name of this GsaJob.

        Parameters
        ----------
        submitter_name: str | None | Unset_Type
            The submitter_name of this GsaJob.
        """
        self._submitter_name = submitter_name

    @property
    def submitter_roles(self) -> "list[str] | None | Unset_Type":
        """Gets the submitter_roles of this GsaJob.

        Returns
        -------
        list[str] | None | Unset_Type
            The submitter_roles of this GsaJob.
        """
        return self._submitter_roles

    @submitter_roles.setter
    def submitter_roles(self, submitter_roles: "list[str] | None | Unset_Type") -> None:
        """Sets the submitter_roles of this GsaJob.

        Parameters
        ----------
        submitter_roles: list[str] | None | Unset_Type
            The submitter_roles of this GsaJob.
        """
        self._submitter_roles = submitter_roles

    @property
    def submission_date(self) -> "datetime | None | Unset_Type":
        """Gets the submission_date of this GsaJob.

        Returns
        -------
        datetime | None | Unset_Type
            The submission_date of this GsaJob.
        """
        return self._submission_date

    @submission_date.setter
    def submission_date(self, submission_date: "datetime | None | Unset_Type") -> None:
        """Sets the submission_date of this GsaJob.

        Parameters
        ----------
        submission_date: datetime | None | Unset_Type
            The submission_date of this GsaJob.
        """
        self._submission_date = submission_date

    @property
    def scheduled_execution_date(self) -> "datetime | None | Unset_Type":
        """Gets the scheduled_execution_date of this GsaJob.

        Returns
        -------
        datetime | None | Unset_Type
            The scheduled_execution_date of this GsaJob.
        """
        return self._scheduled_execution_date

    @scheduled_execution_date.setter
    def scheduled_execution_date(
        self, scheduled_execution_date: "datetime | None | Unset_Type"
    ) -> None:
        """Sets the scheduled_execution_date of this GsaJob.

        Parameters
        ----------
        scheduled_execution_date: datetime | None | Unset_Type
            The scheduled_execution_date of this GsaJob.
        """
        self._scheduled_execution_date = scheduled_execution_date

    @property
    def execution_date(self) -> "datetime | None | Unset_Type":
        """Gets the execution_date of this GsaJob.

        Returns
        -------
        datetime | None | Unset_Type
            The execution_date of this GsaJob.
        """
        return self._execution_date

    @execution_date.setter
    def execution_date(self, execution_date: "datetime | None | Unset_Type") -> None:
        """Sets the execution_date of this GsaJob.

        Parameters
        ----------
        execution_date: datetime | None | Unset_Type
            The execution_date of this GsaJob.
        """
        self._execution_date = execution_date

    @property
    def completion_date(self) -> "datetime | None | Unset_Type":
        """Gets the completion_date of this GsaJob.

        Returns
        -------
        datetime | None | Unset_Type
            The completion_date of this GsaJob.
        """
        return self._completion_date

    @completion_date.setter
    def completion_date(self, completion_date: "datetime | None | Unset_Type") -> None:
        """Sets the completion_date of this GsaJob.

        Parameters
        ----------
        completion_date: datetime | None | Unset_Type
            The completion_date of this GsaJob.
        """
        self._completion_date = completion_date

    @property
    def status(self) -> "GsaJobStatus | Unset_Type":
        """Gets the status of this GsaJob.

        Returns
        -------
        GsaJobStatus | Unset_Type
            The status of this GsaJob.
        """
        return self._status

    @status.setter
    def status(self, status: "GsaJobStatus | Unset_Type") -> None:
        """Sets the status of this GsaJob.

        Parameters
        ----------
        status: GsaJobStatus | Unset_Type
            The status of this GsaJob.
        """
        # Field is not nullable
        if status is None:
            raise ValueError("Invalid value for 'status', must not be 'None'")
        self._status = status

    @property
    def input_file_ids(self) -> "list[str] | None | Unset_Type":
        """Gets the input_file_ids of this GsaJob.

        Returns
        -------
        list[str] | None | Unset_Type
            The input_file_ids of this GsaJob.
        """
        return self._input_file_ids

    @input_file_ids.setter
    def input_file_ids(self, input_file_ids: "list[str] | None | Unset_Type") -> None:
        """Sets the input_file_ids of this GsaJob.

        Parameters
        ----------
        input_file_ids: list[str] | None | Unset_Type
            The input_file_ids of this GsaJob.
        """
        self._input_file_ids = input_file_ids

    @property
    def output_file_names(self) -> "list[str] | None | Unset_Type":
        """Gets the output_file_names of this GsaJob.

        Returns
        -------
        list[str] | None | Unset_Type
            The output_file_names of this GsaJob.
        """
        return self._output_file_names

    @output_file_names.setter
    def output_file_names(self, output_file_names: "list[str] | None | Unset_Type") -> None:
        """Sets the output_file_names of this GsaJob.

        Parameters
        ----------
        output_file_names: list[str] | None | Unset_Type
            The output_file_names of this GsaJob.
        """
        self._output_file_names = output_file_names

    @property
    def position(self) -> "int | None | Unset_Type":
        """Gets the position of this GsaJob.

        Returns
        -------
        int | None | Unset_Type
            The position of this GsaJob.
        """
        return self._position

    @position.setter
    def position(self, position: "int | None | Unset_Type") -> None:
        """Sets the position of this GsaJob.

        Parameters
        ----------
        position: int | None | Unset_Type
            The position of this GsaJob.
        """
        self._position = position

    @property
    def job_specific_outputs(self) -> "dict[str, object] | None | Unset_Type":
        """Gets the job_specific_outputs of this GsaJob.

        Returns
        -------
        dict[str, object] | None | Unset_Type
            The job_specific_outputs of this GsaJob.
        """
        return self._job_specific_outputs

    @job_specific_outputs.setter
    def job_specific_outputs(
        self, job_specific_outputs: "dict[str, object] | None | Unset_Type"
    ) -> None:
        """Sets the job_specific_outputs of this GsaJob.

        Parameters
        ----------
        job_specific_outputs: dict[str, object] | None | Unset_Type
            The job_specific_outputs of this GsaJob.
        """
        self._job_specific_outputs = job_specific_outputs

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
        if not isinstance(other, GsaJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
