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


class SchemaSubsetsApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def add_to_subset(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        subset_guid: "str",
        body: "Optional[GsaAddRecordHistoryToSubset]" = None,
    ) -> "None":
        """Add a record history to a subset.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
            See [Schema - Databases/GetAllDatabases](#/Schema%20-%20Databases/GetAllDatabases)
        table_guid: str
            See [Schema - Tables/GetTables](#/Schema%20-%20Tables/GetTables) or [Schema - Tables/QueryTables](#/Schema%20-%20Tables/QueryTables)
        subset_guid: str
        body: GsaAddRecordHistoryToSubset

        Returns
        -------
        None
        """
        data = self._add_to_subset_with_http_info(
            database_key, table_guid, subset_guid, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _add_to_subset_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        subset_guid: "str",
        body: "Optional[GsaAddRecordHistoryToSubset]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "subset_guid",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method add_to_subset"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'add_to_subset'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'add_to_subset'"
            )
        # verify the required parameter "subset_guid" is set
        if "subset_guid" not in params or params["subset_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'subset_guid' when calling 'add_to_subset'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "subset_guid" in params and subset_guid is not None:
            path_params["subset-guid"] = params["subset_guid"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json-patch+json", "application/json", "text/json", "application/*+json"]
        )

        response_type_map: dict[int, Optional[str]] = {
            200: None,
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/subsets/{subset-guid}:add-to-subset",
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

    def create_subset(
        self, *, database_key: "str", table_guid: "str", body: "Optional[GsaCreateSubset]" = None
    ) -> "GsaSubset | None":
        """Create a new subset.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
            See [Schema - Databases/GetAllDatabases](#/Schema%20-%20Databases/GetAllDatabases)
        table_guid: str
            See [Schema - Tables/GetTables](#/Schema%20-%20Tables/GetTables) or [Schema - Tables/QueryTables](#/Schema%20-%20Tables/QueryTables)
        body: GsaCreateSubset

        Returns
        -------
        GsaSubset | None
        """
        data = self._create_subset_with_http_info(
            database_key, table_guid, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _create_subset_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        body: "Optional[GsaCreateSubset]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method create_subset"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'create_subset'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'create_subset'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]

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
            201: "GsaSubset",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/subsets",
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

    def delete_subset(
        self, *, database_key: "str", table_guid: "str", subset_guid: "str"
    ) -> "None":
        """Delete a subset.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
            See [Schema - Databases/GetAllDatabases](#/Schema%20-%20Databases/GetAllDatabases)
        table_guid: str
            See [Schema - Tables/GetTables](#/Schema%20-%20Tables/GetTables) or [Schema - Tables/QueryTables](#/Schema%20-%20Tables/QueryTables)
        subset_guid: str

        Returns
        -------
        None
        """
        data = self._delete_subset_with_http_info(
            database_key, table_guid, subset_guid, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _delete_subset_with_http_info(
        self, database_key: "str", table_guid: "str", subset_guid: "str", **kwargs: Any
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "subset_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method delete_subset"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'delete_subset'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'delete_subset'"
            )
        # verify the required parameter "subset_guid" is set
        if "subset_guid" not in params or params["subset_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'subset_guid' when calling 'delete_subset'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "subset_guid" in params and subset_guid is not None:
            path_params["subset-guid"] = params["subset_guid"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None

        response_type_map: dict[int, Optional[str]] = {
            200: None,
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/subsets/{subset-guid}",
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

    def get_subset(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        subset_guid: "str",
        mode: "Optional[str]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
    ) -> "GsaSubset | None":
        """Get a subset with a specified guid for a given database and table.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
            See [Schema - Databases/GetAllDatabases](#/Schema%20-%20Databases/GetAllDatabases)
        table_guid: str
            See [Schema - Tables/GetTables](#/Schema%20-%20Tables/GetTables) or [Schema - Tables/QueryTables](#/Schema%20-%20Tables/QueryTables)
        subset_guid: str
        mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the header.
        x_ansys_vc_mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the query string.

        Returns
        -------
        GsaSubset | None
        """
        data = self._get_subset_with_http_info(
            database_key,
            table_guid,
            subset_guid,
            mode,
            x_ansys_vc_mode,
            _return_http_data_only=True,
        )
        return data  # type: ignore[no-any-return]

    def _get_subset_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        subset_guid: "str",
        mode: "Optional[str]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "subset_guid",
            "mode",
            "x_ansys_vc_mode",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method get_subset")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'get_subset'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'get_subset'"
            )
        # verify the required parameter "subset_guid" is set
        if "subset_guid" not in params or params["subset_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'subset_guid' when calling 'get_subset'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "subset_guid" in params and subset_guid is not None:
            path_params["subset-guid"] = params["subset_guid"]

        query_params: list[Any] = []
        if "mode" in params and mode is not None:
            query_params.append(("mode", params["mode"]))

        header_params: dict[str, Any] = {}
        if "x_ansys_vc_mode" in params and x_ansys_vc_mode is not None:
            header_params["X-Ansys-VC-Mode"] = params["x_ansys_vc_mode"]

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: dict[int, Optional[str]] = {
            200: "GsaSubset",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/subsets/{subset-guid}",
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

    def get_subsets(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        mode: "Optional[str]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
    ) -> "GsaSubsetsInfo | None":
        """Get all subsets for table

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
            See [Schema - Databases/GetAllDatabases](#/Schema%20-%20Databases/GetAllDatabases)
        table_guid: str
            See [Schema - Tables/GetTables](#/Schema%20-%20Tables/GetTables) or [Schema - Tables/QueryTables](#/Schema%20-%20Tables/QueryTables)
        mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the header.
        x_ansys_vc_mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the query string.

        Returns
        -------
        GsaSubsetsInfo | None
        """
        data = self._get_subsets_with_http_info(
            database_key, table_guid, mode, x_ansys_vc_mode, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _get_subsets_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        mode: "Optional[str]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "mode",
            "x_ansys_vc_mode",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method get_subsets")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'get_subsets'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'get_subsets'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]

        query_params: list[Any] = []
        if "mode" in params and mode is not None:
            query_params.append(("mode", params["mode"]))

        header_params: dict[str, Any] = {}
        if "x_ansys_vc_mode" in params and x_ansys_vc_mode is not None:
            header_params["X-Ansys-VC-Mode"] = params["x_ansys_vc_mode"]

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: dict[int, Optional[str]] = {
            200: "GsaSubsetsInfo",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/subsets",
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

    def remove_from_subset(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        subset_guid: "str",
        body: "Optional[GsaRemoveRecordHistoryFromSubset]" = None,
    ) -> "None":
        """Remove a record history, and all of its descendants, from a subset.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
            See [Schema - Databases/GetAllDatabases](#/Schema%20-%20Databases/GetAllDatabases)
        table_guid: str
            See [Schema - Tables/GetTables](#/Schema%20-%20Tables/GetTables) or [Schema - Tables/QueryTables](#/Schema%20-%20Tables/QueryTables)
        subset_guid: str
        body: GsaRemoveRecordHistoryFromSubset

        Returns
        -------
        None
        """
        data = self._remove_from_subset_with_http_info(
            database_key, table_guid, subset_guid, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _remove_from_subset_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        subset_guid: "str",
        body: "Optional[GsaRemoveRecordHistoryFromSubset]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "subset_guid",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method remove_from_subset"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'remove_from_subset'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'remove_from_subset'"
            )
        # verify the required parameter "subset_guid" is set
        if "subset_guid" not in params or params["subset_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'subset_guid' when calling 'remove_from_subset'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "subset_guid" in params and subset_guid is not None:
            path_params["subset-guid"] = params["subset_guid"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json-patch+json", "application/json", "text/json", "application/*+json"]
        )

        response_type_map: dict[int, Optional[str]] = {
            200: None,
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/subsets/{subset-guid}:remove-from-subset",
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

    def update_subset(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        subset_guid: "str",
        body: "Optional[GsaUpdateSubset]" = None,
    ) -> "GsaSubset | None":
        """Update a subset.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
            See [Schema - Databases/GetAllDatabases](#/Schema%20-%20Databases/GetAllDatabases)
        table_guid: str
            See [Schema - Tables/GetTables](#/Schema%20-%20Tables/GetTables) or [Schema - Tables/QueryTables](#/Schema%20-%20Tables/QueryTables)
        subset_guid: str
        body: GsaUpdateSubset

        Returns
        -------
        GsaSubset | None
        """
        data = self._update_subset_with_http_info(
            database_key, table_guid, subset_guid, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _update_subset_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        subset_guid: "str",
        body: "Optional[GsaUpdateSubset]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "subset_guid",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method update_subset"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'update_subset'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'update_subset'"
            )
        # verify the required parameter "subset_guid" is set
        if "subset_guid" not in params or params["subset_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'subset_guid' when calling 'update_subset'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "subset_guid" in params and subset_guid is not None:
            path_params["subset-guid"] = params["subset_guid"]

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
            200: "GsaSubset",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/subsets/{subset-guid}",
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
