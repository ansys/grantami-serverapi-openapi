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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ApiBase

if TYPE_CHECKING:
    import pathlib

    from ..models import *


class SchemaProfileTablesApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def create_profile_table(
        self, *, profile_guid: "str", body: "Optional[GsaCreateProfileTable]" = None
    ) -> "Union[GsaProfileTable, None]":
        """Create a new profile table

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        profile_guid: str
        body: GsaCreateProfileTable

        Returns
        -------
        Union[GsaProfileTable, None]
        """
        data = self._create_profile_table_with_http_info(
            profile_guid, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _create_profile_table_with_http_info(
        self, profile_guid: "str", body: "Optional[GsaCreateProfileTable]" = None, **kwargs: Any
    ) -> Any:
        all_params = [
            "profile_guid",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method create_profile_table"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "profile_guid" is set
        if "profile_guid" not in params or params["profile_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'profile_guid' when calling 'create_profile_table'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "profile_guid" in params and profile_guid is not None:
            path_params["profile-guid"] = params["profile_guid"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json-patch+json", "application/json", "text/json", "application/*+json"]
        )

        response_type_map: dict[int, Optional[str]] = {
            201: "GsaProfileTable",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/profiles/{profile-guid}/profile-tables",
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

    def delete_profile_table(self, *, profile_guid: "str", profile_table_guid: "str") -> "None":
        """Delete a profile table

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        profile_guid: str
        profile_table_guid: str

        Returns
        -------
        None
        """
        data = self._delete_profile_table_with_http_info(
            profile_guid, profile_table_guid, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _delete_profile_table_with_http_info(
        self, profile_guid: "str", profile_table_guid: "str", **kwargs: Any
    ) -> Any:
        all_params = [
            "profile_guid",
            "profile_table_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method delete_profile_table"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "profile_guid" is set
        if "profile_guid" not in params or params["profile_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'profile_guid' when calling 'delete_profile_table'"
            )
        # verify the required parameter "profile_table_guid" is set
        if "profile_table_guid" not in params or params["profile_table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'profile_table_guid' when calling 'delete_profile_table'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "profile_guid" in params and profile_guid is not None:
            path_params["profile-guid"] = params["profile_guid"]
        if "profile_table_guid" in params and profile_table_guid is not None:
            path_params["profile-table-guid"] = params["profile_table_guid"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None

        response_type_map: dict[int, Optional[str]] = {
            200: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/profiles/{profile-guid}/profile-tables/{profile-table-guid}",
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

    def get_profile_table(
        self, *, profile_guid: "str", profile_table_guid: "str"
    ) -> "Union[GsaProfileTable, None]":
        """Get individual profile table

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        profile_guid: str
        profile_table_guid: str

        Returns
        -------
        Union[GsaProfileTable, None]
        """
        data = self._get_profile_table_with_http_info(
            profile_guid, profile_table_guid, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _get_profile_table_with_http_info(
        self, profile_guid: "str", profile_table_guid: "str", **kwargs: Any
    ) -> Any:
        all_params = [
            "profile_guid",
            "profile_table_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_profile_table"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "profile_guid" is set
        if "profile_guid" not in params or params["profile_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'profile_guid' when calling 'get_profile_table'"
            )
        # verify the required parameter "profile_table_guid" is set
        if "profile_table_guid" not in params or params["profile_table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'profile_table_guid' when calling 'get_profile_table'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "profile_guid" in params and profile_guid is not None:
            path_params["profile-guid"] = params["profile_guid"]
        if "profile_table_guid" in params and profile_table_guid is not None:
            path_params["profile-table-guid"] = params["profile_table_guid"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: dict[int, Optional[str]] = {
            200: "GsaProfileTable",
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/profiles/{profile-guid}/profile-tables/{profile-table-guid}",
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

    def get_profile_tables(self, *, profile_guid: "str") -> "Union[GsaProfileTablesInfo, None]":
        """Get all profile tables of given profile

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        profile_guid: str

        Returns
        -------
        Union[GsaProfileTablesInfo, None]
        """
        data = self._get_profile_tables_with_http_info(profile_guid, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _get_profile_tables_with_http_info(self, profile_guid: "str", **kwargs: Any) -> Any:
        all_params = [
            "profile_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_profile_tables"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "profile_guid" is set
        if "profile_guid" not in params or params["profile_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'profile_guid' when calling 'get_profile_tables'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "profile_guid" in params and profile_guid is not None:
            path_params["profile-guid"] = params["profile_guid"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: dict[int, Optional[str]] = {
            200: "GsaProfileTablesInfo",
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/profiles/{profile-guid}/profile-tables",
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

    def update_profile_table(
        self,
        *,
        profile_guid: "str",
        profile_table_guid: "str",
        body: "Optional[GsaUpdateProfileTable]" = None,
    ) -> "Union[GsaProfileTable, None]":
        """Update a profile table

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        profile_guid: str
        profile_table_guid: str
        body: GsaUpdateProfileTable

        Returns
        -------
        Union[GsaProfileTable, None]
        """
        data = self._update_profile_table_with_http_info(
            profile_guid, profile_table_guid, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _update_profile_table_with_http_info(
        self,
        profile_guid: "str",
        profile_table_guid: "str",
        body: "Optional[GsaUpdateProfileTable]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "profile_guid",
            "profile_table_guid",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method update_profile_table"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "profile_guid" is set
        if "profile_guid" not in params or params["profile_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'profile_guid' when calling 'update_profile_table'"
            )
        # verify the required parameter "profile_table_guid" is set
        if "profile_table_guid" not in params or params["profile_table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'profile_table_guid' when calling 'update_profile_table'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "profile_guid" in params and profile_guid is not None:
            path_params["profile-guid"] = params["profile_guid"]
        if "profile_table_guid" in params and profile_table_guid is not None:
            path_params["profile-table-guid"] = params["profile_table_guid"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json-patch+json", "application/json", "text/json", "application/*+json"]
        )

        response_type_map: dict[int, Optional[str]] = {
            200: "GsaProfileTable",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/profiles/{profile-guid}/profile-tables/{profile-table-guid}",
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
