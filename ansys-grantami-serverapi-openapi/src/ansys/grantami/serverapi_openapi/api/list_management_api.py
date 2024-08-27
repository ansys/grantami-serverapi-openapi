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

from . import ApiBase

if TYPE_CHECKING:
    import pathlib

    from ..models import *


class ListManagementApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def copy_list(self, *, list_identifier: "str") -> "Union[GsaRecordListHeader, None]":
        """Creates a copy of the list and its items

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        list_identifier: str

        Returns
        -------
        Union[GsaRecordListHeader, None]
        """
        data = self._copy_list_with_http_info(list_identifier, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _copy_list_with_http_info(self, list_identifier: "str", **kwargs: Any) -> Any:
        all_params = [
            "list_identifier",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method copy_list")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "list_identifier" is set
        if "list_identifier" not in params or params["list_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'list_identifier' when calling 'copy_list'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "list_identifier" in params and list_identifier is not None:
            path_params["listIdentifier"] = params["list_identifier"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            201: "GsaRecordListHeader",
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/api/v1/lists/list/{listIdentifier}/copy",
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

    def create_list(
        self, *, body: "Optional[GsaCreateRecordList]" = None
    ) -> "Union[GsaRecordListHeader, None]":
        """Creates a new list with the specified properties and items.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GsaCreateRecordList

        Returns
        -------
        Union[GsaRecordListHeader, None]
        """
        data = self._create_list_with_http_info(body, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _create_list_with_http_info(
        self, body: "Optional[GsaCreateRecordList]" = None, **kwargs: Any
    ) -> Any:
        all_params = ["body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method create_list")
            params[key] = val
        del params["kwargs"]

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

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

        response_type_map: Dict[int, Optional[str]] = {
            201: "GsaRecordListHeader",
            400: None,
            403: None,
        }

        return self.api_client.call_api(
            "/api/v1/lists",
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

    def delete_list(self, *, list_identifier: "str") -> "None":
        """Delete an existing list.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        list_identifier: str

        Returns
        -------
        None
        """
        data = self._delete_list_with_http_info(list_identifier, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _delete_list_with_http_info(self, list_identifier: "str", **kwargs: Any) -> Any:
        all_params = [
            "list_identifier",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method delete_list")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "list_identifier" is set
        if "list_identifier" not in params or params["list_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'list_identifier' when calling 'delete_list'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "list_identifier" in params and list_identifier is not None:
            path_params["listIdentifier"] = params["list_identifier"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None

        response_type_map: Dict[int, Optional[str]] = {
            200: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/api/v1/lists/list/{listIdentifier}",
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

    def get_all_lists(self) -> "Union[GsaRecordListHeadersInfo, None]":
        """Returns all lists visible to the calling user

        This method makes a synchronous HTTP request.

        Returns
        -------
        Union[GsaRecordListHeadersInfo, None]
        """
        data = self._get_all_lists_with_http_info(_return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _get_all_lists_with_http_info(self, **kwargs: Any) -> Any:
        all_params = ["_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_all_lists"
                )
            params[key] = val
        del params["kwargs"]

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GsaRecordListHeadersInfo",
            403: None,
        }

        return self.api_client.call_api(
            "/api/v1/lists",
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

    def get_list(self, *, list_identifier: "str") -> "Union[GsaRecordListHeader, None]":
        """Returns the given list if it exists and the calling user has read access to it

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        list_identifier: str

        Returns
        -------
        Union[GsaRecordListHeader, None]
        """
        data = self._get_list_with_http_info(list_identifier, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _get_list_with_http_info(self, list_identifier: "str", **kwargs: Any) -> Any:
        all_params = [
            "list_identifier",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method get_list")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "list_identifier" is set
        if "list_identifier" not in params or params["list_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'list_identifier' when calling 'get_list'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "list_identifier" in params and list_identifier is not None:
            path_params["listIdentifier"] = params["list_identifier"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GsaRecordListHeader",
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/api/v1/lists/list/{listIdentifier}",
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

    def get_record_list_search_results(
        self, *, result_resource_identifier: "str"
    ) -> "Union[GsaRecordListSearchResultsInfo, None]":
        """Returns the search results found in the specified resource

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        result_resource_identifier: str

        Returns
        -------
        Union[GsaRecordListSearchResultsInfo, None]
        """
        data = self._get_record_list_search_results_with_http_info(
            result_resource_identifier, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _get_record_list_search_results_with_http_info(
        self, result_resource_identifier: "str", **kwargs: Any
    ) -> Any:
        all_params = [
            "result_resource_identifier",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_record_list_search_results"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "result_resource_identifier" is set
        if (
            "result_resource_identifier" not in params
            or params["result_resource_identifier"] is None
        ):
            raise ValueError(
                "Missing the required parameter 'result_resource_identifier' when calling 'get_record_list_search_results'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "result_resource_identifier" in params and result_resource_identifier is not None:
            path_params["resultResourceIdentifier"] = params["result_resource_identifier"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GsaRecordListSearchResultsInfo",
            403: None,
            404: None,
            410: None,
        }

        return self.api_client.call_api(
            "/api/v1/lists/search/results/{resultResourceIdentifier}",
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

    def publish_list(self, *, list_identifier: "str") -> "Union[GsaRecordListHeader, None]":
        """Update the status of an existing list to \"published\". The list must be awaiting approval, and not already published.  The \"awaiting approval\" flag will be reset to false.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        list_identifier: str

        Returns
        -------
        Union[GsaRecordListHeader, None]
        """
        data = self._publish_list_with_http_info(list_identifier, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _publish_list_with_http_info(self, list_identifier: "str", **kwargs: Any) -> Any:
        all_params = [
            "list_identifier",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method publish_list"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "list_identifier" is set
        if "list_identifier" not in params or params["list_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'list_identifier' when calling 'publish_list'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "list_identifier" in params and list_identifier is not None:
            path_params["listIdentifier"] = params["list_identifier"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GsaRecordListHeader",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/api/v1/lists/list/{listIdentifier}/publish",
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

    def request_approval(self, *, list_identifier: "str") -> "Union[GsaRecordListHeader, None]":
        """Update the status of an existing list to \"awaiting approval\".

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        list_identifier: str

        Returns
        -------
        Union[GsaRecordListHeader, None]
        """
        data = self._request_approval_with_http_info(list_identifier, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _request_approval_with_http_info(self, list_identifier: "str", **kwargs: Any) -> Any:
        all_params = [
            "list_identifier",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method request_approval"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "list_identifier" is set
        if "list_identifier" not in params or params["list_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'list_identifier' when calling 'request_approval'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "list_identifier" in params and list_identifier is not None:
            path_params["listIdentifier"] = params["list_identifier"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GsaRecordListHeader",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/api/v1/lists/list/{listIdentifier}/request-approval",
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

    def reset_awaiting_approval(
        self, *, list_identifier: "str"
    ) -> "Union[GsaRecordListHeader, None]":
        """Update the status of an existing list to not be \"awaiting approval\".

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        list_identifier: str

        Returns
        -------
        Union[GsaRecordListHeader, None]
        """
        data = self._reset_awaiting_approval_with_http_info(
            list_identifier, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _reset_awaiting_approval_with_http_info(self, list_identifier: "str", **kwargs: Any) -> Any:
        all_params = [
            "list_identifier",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method reset_awaiting_approval"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "list_identifier" is set
        if "list_identifier" not in params or params["list_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'list_identifier' when calling 'reset_awaiting_approval'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "list_identifier" in params and list_identifier is not None:
            path_params["listIdentifier"] = params["list_identifier"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GsaRecordListHeader",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/api/v1/lists/list/{listIdentifier}/reset",
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

    def revise_list(self, *, list_identifier: "str") -> "Union[GsaRecordListHeader, None]":
        """Creates a private copy of a list that can be revised.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        list_identifier: str

        Returns
        -------
        Union[GsaRecordListHeader, None]
        """
        data = self._revise_list_with_http_info(list_identifier, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _revise_list_with_http_info(self, list_identifier: "str", **kwargs: Any) -> Any:
        all_params = [
            "list_identifier",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method revise_list")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "list_identifier" is set
        if "list_identifier" not in params or params["list_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'list_identifier' when calling 'revise_list'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "list_identifier" in params and list_identifier is not None:
            path_params["listIdentifier"] = params["list_identifier"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            201: "GsaRecordListHeader",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/api/v1/lists/list/{listIdentifier}/revise",
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

    def run_record_lists_search(
        self, *, body: "Optional[GsaRecordListSearchRequest]" = None
    ) -> "Union[GsaRecordListSearchInfo, None]":
        """Posts a search request, and returns an object containing search result identifier

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GsaRecordListSearchRequest

        Returns
        -------
        Union[GsaRecordListSearchInfo, None]
        """
        data = self._run_record_lists_search_with_http_info(body, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _run_record_lists_search_with_http_info(
        self, body: "Optional[GsaRecordListSearchRequest]" = None, **kwargs: Any
    ) -> Any:
        all_params = ["body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method run_record_lists_search"
                )
            params[key] = val
        del params["kwargs"]

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

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

        response_type_map: Dict[int, Optional[str]] = {
            201: "GsaRecordListSearchInfo",
            400: None,
            403: None,
        }

        return self.api_client.call_api(
            "/api/v1/lists/search",
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

    def unpublish_list(self, *, list_identifier: "str") -> "Union[GsaRecordListHeader, None]":
        """Update the status of an existing list to \"unpublished\". The list must be published, and awaiting approval.  The \"awaiting approval\" flag will be reset to false.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        list_identifier: str

        Returns
        -------
        Union[GsaRecordListHeader, None]
        """
        data = self._unpublish_list_with_http_info(list_identifier, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _unpublish_list_with_http_info(self, list_identifier: "str", **kwargs: Any) -> Any:
        all_params = [
            "list_identifier",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method unpublish_list"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "list_identifier" is set
        if "list_identifier" not in params or params["list_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'list_identifier' when calling 'unpublish_list'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "list_identifier" in params and list_identifier is not None:
            path_params["listIdentifier"] = params["list_identifier"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GsaRecordListHeader",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/api/v1/lists/list/{listIdentifier}/unpublish",
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

    def update_list(
        self, *, list_identifier: "str", body: "Optional[GsaUpdateRecordListProperties]" = None
    ) -> "Union[GsaRecordListHeader, None]":
        """Performs a partial update on the properties of a list.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        list_identifier: str
        body: GsaUpdateRecordListProperties

        Returns
        -------
        Union[GsaRecordListHeader, None]
        """
        data = self._update_list_with_http_info(list_identifier, body, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _update_list_with_http_info(
        self,
        list_identifier: "str",
        body: "Optional[GsaUpdateRecordListProperties]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "list_identifier",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method update_list")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "list_identifier" is set
        if "list_identifier" not in params or params["list_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'list_identifier' when calling 'update_list'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "list_identifier" in params and list_identifier is not None:
            path_params["listIdentifier"] = params["list_identifier"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

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

        response_type_map: Dict[int, Optional[str]] = {
            200: "GsaRecordListHeader",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/api/v1/lists/list/{listIdentifier}",
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
