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

from . import ApiBase

if TYPE_CHECKING:
    import pathlib

    from ..models import *


class JobQueueApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def create_job(self, *, body: "Optional[GsaCreateJobRequest]" = None) -> "GsaJob":
        """Create a new job.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GsaCreateJobRequest

        Returns
        -------
        GsaJob
        """
        data = self._create_job_with_http_info(body, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _create_job_with_http_info(
        self, body: "Optional[GsaCreateJobRequest]" = None, **kwargs: Any
    ) -> Any:
        all_params = ["body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method create_job")
            params[key] = val
        del params["kwargs"]

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json-patch+json", "application/json", "text/json", "application/*+json"]
        )

        response_type_map: dict[int, Optional[str]] = {
            201: "GsaJob",
        }

        return self.api_client.call_api(
            "/v1alpha/job-queue/jobs",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
            response_type_map=response_type_map,
        )

    def delete_job(self, *, id: "str") -> "None":
        """Delete a job.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        id: str

        Returns
        -------
        None
        """
        data = self._delete_job_with_http_info(id, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _delete_job_with_http_info(self, id: "str", **kwargs: Any) -> Any:
        all_params = ["id", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method delete_job")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "id" is set
        if "id" not in params or params["id"] is None:
            raise ValueError("Missing the required parameter 'id' when calling 'delete_job'")

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "id" in params and id is not None:
            path_params["id"] = params["id"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None

        response_type_map: dict[int, Optional[str]] = {
            200: None,
            204: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/job-queue/jobs/{id}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
            response_type_map=response_type_map,
        )

    def delete_jobs(self, *, body: "Optional[list[str]]" = None) -> "None | list[str]":
        """Delete specified jobs.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: list[str]

        Returns
        -------
        None | list[str]
        """
        data = self._delete_jobs_with_http_info(body, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _delete_jobs_with_http_info(self, body: "Optional[list[str]]" = None, **kwargs: Any) -> Any:
        all_params = ["body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method delete_jobs")
            params[key] = val
        del params["kwargs"]

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json-patch+json", "application/json", "text/json", "application/*+json"]
        )

        response_type_map: dict[int, Optional[str]] = {
            200: "list[str]",
            422: None,
            500: None,
        }

        return self.api_client.call_api(
            "/v1alpha/job-queue/jobs",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
            response_type_map=response_type_map,
        )

    def get_current_user(self) -> "GsaCurrentUser":
        """Get the current user.

        This method makes a synchronous HTTP request.

        Returns
        -------
        GsaCurrentUser
        """
        data = self._get_current_user_with_http_info(_return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _get_current_user_with_http_info(self, **kwargs: Any) -> Any:
        all_params = ["_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_current_user"
                )
            params[key] = val
        del params["kwargs"]

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: dict[int, Optional[str]] = {
            200: "GsaCurrentUser",
        }

        return self.api_client.call_api(
            "/v1alpha/job-queue/current-user",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
            response_type_map=response_type_map,
        )

    def get_job(self, *, id: "str") -> "GsaJob | None":
        """Get job by ID.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        id: str

        Returns
        -------
        GsaJob | None
        """
        data = self._get_job_with_http_info(id, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _get_job_with_http_info(self, id: "str", **kwargs: Any) -> Any:
        all_params = ["id", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method get_job")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "id" is set
        if "id" not in params or params["id"] is None:
            raise ValueError("Missing the required parameter 'id' when calling 'get_job'")

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "id" in params and id is not None:
            path_params["id"] = params["id"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: dict[int, Optional[str]] = {
            200: "GsaJob",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/job-queue/jobs/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
            response_type_map=response_type_map,
        )

    def get_job_output_file(self, *, id: "str", file_name: "str") -> "None | str":
        """Retrieve a job output file.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        id: str
        file_name: str

        Returns
        -------
        None | str
        """
        data = self._get_job_output_file_with_http_info(id, file_name, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _get_job_output_file_with_http_info(
        self, id: "str", file_name: "str", **kwargs: Any
    ) -> Any:
        all_params = [
            "id",
            "file_name",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_job_output_file"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "id" is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter 'id' when calling 'get_job_output_file'"
            )
        # verify the required parameter "file_name" is set
        if "file_name" not in params or params["file_name"] is None:
            raise ValueError(
                "Missing the required parameter 'file_name' when calling 'get_job_output_file'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "id" in params and id is not None:
            path_params["id"] = params["id"]

        query_params: list[Any] = []
        if "file_name" in params and file_name is not None:
            query_params.append(("fileName", params["file_name"]))

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/octet-stream"])

        response_type_map: dict[int, Optional[str]] = {
            200: "file",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/job-queue/jobs/{id}/outputs:export",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
            response_type_map=response_type_map,
        )

    def get_jobs(
        self,
        *,
        job_type: "Optional[str]" = None,
        status: "Optional[str]" = None,
        name_filter: "Optional[str]" = None,
        description_filter: "Optional[str]" = None,
        submitter_name_filter: "Optional[str]" = None,
        page_size: "Optional[int]" = None,
        page_number: "Optional[int]" = None,
    ) -> "GsaGetJobsResponse":
        """Get a list of jobs.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        job_type: str
        status: str
        name_filter: str
        description_filter: str
        submitter_name_filter: str
        page_size: int
        page_number: int

        Returns
        -------
        GsaGetJobsResponse
        """
        data = self._get_jobs_with_http_info(
            job_type,
            status,
            name_filter,
            description_filter,
            submitter_name_filter,
            page_size,
            page_number,
            _return_http_data_only=True,
        )
        return data  # type: ignore[no-any-return]

    def _get_jobs_with_http_info(
        self,
        job_type: "Optional[str]" = None,
        status: "Optional[str]" = None,
        name_filter: "Optional[str]" = None,
        description_filter: "Optional[str]" = None,
        submitter_name_filter: "Optional[str]" = None,
        page_size: "Optional[int]" = None,
        page_number: "Optional[int]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "job_type",
            "status",
            "name_filter",
            "description_filter",
            "submitter_name_filter",
            "page_size",
            "page_number",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method get_jobs")
            params[key] = val
        del params["kwargs"]

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}

        query_params: list[Any] = []
        if "job_type" in params and job_type is not None:
            query_params.append(("jobType", params["job_type"]))
        if "status" in params and status is not None:
            query_params.append(("status", params["status"]))
        if "name_filter" in params and name_filter is not None:
            query_params.append(("nameFilter", params["name_filter"]))
        if "description_filter" in params and description_filter is not None:
            query_params.append(("descriptionFilter", params["description_filter"]))
        if "submitter_name_filter" in params and submitter_name_filter is not None:
            query_params.append(("submitterNameFilter", params["submitter_name_filter"]))
        if "page_size" in params and page_size is not None:
            query_params.append(("pageSize", params["page_size"]))
        if "page_number" in params and page_number is not None:
            query_params.append(("pageNumber", params["page_number"]))

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: dict[int, Optional[str]] = {
            200: "GsaGetJobsResponse",
        }

        return self.api_client.call_api(
            "/v1alpha/job-queue/jobs",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
            response_type_map=response_type_map,
        )

    def get_output_filenames(self, *, id: "str") -> "None | list[str]":
        """Get a job's output filenames.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        id: str

        Returns
        -------
        None | list[str]
        """
        data = self._get_output_filenames_with_http_info(id, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _get_output_filenames_with_http_info(self, id: "str", **kwargs: Any) -> Any:
        all_params = ["id", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_output_filenames"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "id" is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter 'id' when calling 'get_output_filenames'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "id" in params and id is not None:
            path_params["id"] = params["id"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: dict[int, Optional[str]] = {
            200: "list[str]",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/job-queue/jobs/{id}/outputs",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
            response_type_map=response_type_map,
        )

    def get_processing_config(self) -> "GsaProcessingConfig":
        """Get the processing configuration.

        This method makes a synchronous HTTP request.

        Returns
        -------
        GsaProcessingConfig
        """
        data = self._get_processing_config_with_http_info(_return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _get_processing_config_with_http_info(self, **kwargs: Any) -> Any:
        all_params = ["_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_processing_config"
                )
            params[key] = val
        del params["kwargs"]

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: dict[int, Optional[str]] = {
            200: "GsaProcessingConfig",
        }

        return self.api_client.call_api(
            "/v1alpha/job-queue/processing-configuration",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
            response_type_map=response_type_map,
        )

    def move_to_top(self, *, id: "str") -> "None":
        """Move a job to the top of the queue (actually sets the scheduled execution date to now, could be done with patch method).

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        id: str

        Returns
        -------
        None
        """
        data = self._move_to_top_with_http_info(id, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _move_to_top_with_http_info(self, id: "str", **kwargs: Any) -> Any:
        all_params = ["id", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method move_to_top")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "id" is set
        if "id" not in params or params["id"] is None:
            raise ValueError("Missing the required parameter 'id' when calling 'move_to_top'")

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "id" in params and id is not None:
            path_params["id"] = params["id"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None

        response_type_map: dict[int, Optional[str]] = {
            200: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/job-queue/jobs/{id}:move-to-top",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
            response_type_map=response_type_map,
        )

    def restore_job(self, *, id: "str") -> "GsaCreateJobRequest | None":
        """Get a job creation object based on an existing job.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        id: str

        Returns
        -------
        GsaCreateJobRequest | None
        """
        data = self._restore_job_with_http_info(id, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _restore_job_with_http_info(self, id: "str", **kwargs: Any) -> Any:
        all_params = ["id", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method restore_job")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "id" is set
        if "id" not in params or params["id"] is None:
            raise ValueError("Missing the required parameter 'id' when calling 'restore_job'")

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "id" in params and id is not None:
            path_params["id"] = params["id"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: dict[int, Optional[str]] = {
            200: "GsaCreateJobRequest",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/job-queue/jobs/{id}:retrieve-definition",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
            response_type_map=response_type_map,
        )

    def resubmit(
        self, *, id: "str", body: "Optional[GsaResubmitJobRequest]" = None
    ) -> "GsaJob | None":
        """Resubmit a job.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        id: str
        body: GsaResubmitJobRequest

        Returns
        -------
        GsaJob | None
        """
        data = self._resubmit_with_http_info(id, body, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _resubmit_with_http_info(
        self, id: "str", body: "Optional[GsaResubmitJobRequest]" = None, **kwargs: Any
    ) -> Any:
        all_params = [
            "id",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method resubmit")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "id" is set
        if "id" not in params or params["id"] is None:
            raise ValueError("Missing the required parameter 'id' when calling 'resubmit'")

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "id" in params and id is not None:
            path_params["id"] = params["id"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json-patch+json", "application/json", "text/json", "application/*+json"]
        )

        response_type_map: dict[int, Optional[str]] = {
            200: "GsaJob",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/job-queue/jobs/{id}:resubmit",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
            response_type_map=response_type_map,
        )

    def update_job(
        self, *, id: "str", body: "Optional[GsaUpdateJobRequest]" = None
    ) -> "GsaJob | None":
        """Update a job.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        id: str
        body: GsaUpdateJobRequest

        Returns
        -------
        GsaJob | None
        """
        data = self._update_job_with_http_info(id, body, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _update_job_with_http_info(
        self, id: "str", body: "Optional[GsaUpdateJobRequest]" = None, **kwargs: Any
    ) -> Any:
        all_params = [
            "id",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method update_job")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "id" is set
        if "id" not in params or params["id"] is None:
            raise ValueError("Missing the required parameter 'id' when calling 'update_job'")

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "id" in params and id is not None:
            path_params["id"] = params["id"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json-patch+json", "application/json", "text/json", "application/*+json"]
        )

        response_type_map: dict[int, Optional[str]] = {
            200: "GsaJob",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/job-queue/jobs/{id}",
            "PATCH",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
            response_type_map=response_type_map,
        )

    def upload_file(self, *, file: "Optional[BinaryIO | pathlib.Path]" = None) -> "str":
        """Uploads an ephemeral file and returns an ID which can subsequently be used to refer to that file in a job creation request. Ephemeral files have a short lifespan  and should be used to provide file data to jobs only. They should not be used as file storage.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        file: BinaryIO | pathlib.Path

        Returns
        -------
        str
        """
        data = self._upload_file_with_http_info(file, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _upload_file_with_http_info(
        self, file: "Optional[BinaryIO | pathlib.Path]" = None, **kwargs: Any
    ) -> Any:
        all_params = ["file", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method upload_file")
            params[key] = val
        del params["kwargs"]

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}
        if "file" in params and file is not None:
            local_var_files["file"] = params["file"]

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        # multipart/form-data request detected. Content-Type header will be
        # populated by openapi-common based on request content.

        response_type_map: dict[int, Optional[str]] = {
            200: "str",
        }

        return self.api_client.call_api(
            "/v1alpha/job-queue/files",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
            response_type_map=response_type_map,
        )
