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

from . import ApiBase

if TYPE_CHECKING:
    import pathlib

    from ..models import *


class SchemaLayoutSectionsApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def create_layout_item(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        layout_guid: "str",
        section_guid: "str",
        body: "Optional[GrantaServerApiSchemaLayoutsNewLayoutItem]" = None,
    ) -> "Union[GrantaServerApiSchemaLayoutsNewLayoutItem, None]":
        """Add a new layout item.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        layout_guid: str
        section_guid: str
        body: GrantaServerApiSchemaLayoutsNewLayoutItem

        Returns
        -------
        Union[GrantaServerApiSchemaLayoutsNewLayoutItem, None]
        """
        data = self._create_layout_item_with_http_info(
            database_key, table_guid, layout_guid, section_guid, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _create_layout_item_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        layout_guid: "str",
        section_guid: "str",
        body: "Optional[GrantaServerApiSchemaLayoutsNewLayoutItem]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "layout_guid",
            "section_guid",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method create_layout_item"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'create_layout_item'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'create_layout_item'"
            )
        # verify the required parameter "layout_guid" is set
        if "layout_guid" not in params or params["layout_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'layout_guid' when calling 'create_layout_item'"
            )
        # verify the required parameter "section_guid" is set
        if "section_guid" not in params or params["section_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'section_guid' when calling 'create_layout_item'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "layout_guid" in params and layout_guid is not None:
            path_params["layout-guid"] = params["layout_guid"]
        if "section_guid" in params and section_guid is not None:
            path_params["section-guid"] = params["section_guid"]

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
            201: "GrantaServerApiSchemaLayoutsNewLayoutItem",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/layouts/{layout-guid}/sections/{section-guid}/items",
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

    def create_section(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        layout_guid: "str",
        body: "Optional[GrantaServerApiSchemaLayoutsCreateLayoutSection]" = None,
    ) -> "Union[GrantaServerApiSchemaSlimEntitiesSlimLayoutSection, None]":
        """Create a new layout section.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        layout_guid: str
        body: GrantaServerApiSchemaLayoutsCreateLayoutSection

        Returns
        -------
        Union[GrantaServerApiSchemaSlimEntitiesSlimLayoutSection, None]
        """
        data = self._create_section_with_http_info(
            database_key, table_guid, layout_guid, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _create_section_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        layout_guid: "str",
        body: "Optional[GrantaServerApiSchemaLayoutsCreateLayoutSection]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "layout_guid",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method create_section"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'create_section'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'create_section'"
            )
        # verify the required parameter "layout_guid" is set
        if "layout_guid" not in params or params["layout_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'layout_guid' when calling 'create_section'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "layout_guid" in params and layout_guid is not None:
            path_params["layout-guid"] = params["layout_guid"]

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
            201: "GrantaServerApiSchemaSlimEntitiesSlimLayoutSection",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/layouts/{layout-guid}/sections",
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

    def delete_item(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        layout_guid: "str",
        section_guid: "str",
        item_guid: "str",
    ) -> "None":
        """Delete a layout item.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        layout_guid: str
        section_guid: str
        item_guid: str

        Returns
        -------
        None
        """
        data = self._delete_item_with_http_info(
            database_key,
            table_guid,
            layout_guid,
            section_guid,
            item_guid,
            _return_http_data_only=True,
        )
        return data  # type: ignore[no-any-return]

    def _delete_item_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        layout_guid: "str",
        section_guid: "str",
        item_guid: "str",
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "layout_guid",
            "section_guid",
            "item_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method delete_item")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'delete_item'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'delete_item'"
            )
        # verify the required parameter "layout_guid" is set
        if "layout_guid" not in params or params["layout_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'layout_guid' when calling 'delete_item'"
            )
        # verify the required parameter "section_guid" is set
        if "section_guid" not in params or params["section_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'section_guid' when calling 'delete_item'"
            )
        # verify the required parameter "item_guid" is set
        if "item_guid" not in params or params["item_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'item_guid' when calling 'delete_item'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "layout_guid" in params and layout_guid is not None:
            path_params["layout-guid"] = params["layout_guid"]
        if "section_guid" in params and section_guid is not None:
            path_params["section-guid"] = params["section_guid"]
        if "item_guid" in params and item_guid is not None:
            path_params["item-guid"] = params["item_guid"]

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
            "/v1alpha/databases/{database-key}/tables/{table-guid}/layouts/{layout-guid}/sections/{section-guid}/items/{item-guid}",
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

    def delete_section(
        self, *, database_key: "str", table_guid: "str", layout_guid: "str", section_guid: "str"
    ) -> "None":
        """Delete a layout section.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        layout_guid: str
        section_guid: str

        Returns
        -------
        None
        """
        data = self._delete_section_with_http_info(
            database_key, table_guid, layout_guid, section_guid, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _delete_section_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        layout_guid: "str",
        section_guid: "str",
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "layout_guid",
            "section_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method delete_section"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'delete_section'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'delete_section'"
            )
        # verify the required parameter "layout_guid" is set
        if "layout_guid" not in params or params["layout_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'layout_guid' when calling 'delete_section'"
            )
        # verify the required parameter "section_guid" is set
        if "section_guid" not in params or params["section_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'section_guid' when calling 'delete_section'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "layout_guid" in params and layout_guid is not None:
            path_params["layout-guid"] = params["layout_guid"]
        if "section_guid" in params and section_guid is not None:
            path_params["section-guid"] = params["section_guid"]

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
            "/v1alpha/databases/{database-key}/tables/{table-guid}/layouts/{layout-guid}/sections/{section-guid}",
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

    def get_layout_section(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        layout_guid: "str",
        section_guid: "str",
        show_full_detail: "Optional[bool]" = None,
        mode: "Optional[str]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
    ) -> "Union[GrantaServerApiSchemaLayoutsLayoutSection, None]":
        """Get a layout section with a specified guid for a given layout.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        layout_guid: str
        section_guid: str
        show_full_detail: bool
        mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the header.
        x_ansys_vc_mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the query string.

        Returns
        -------
        Union[GrantaServerApiSchemaLayoutsLayoutSection, None]
        """
        data = self._get_layout_section_with_http_info(
            database_key,
            table_guid,
            layout_guid,
            section_guid,
            show_full_detail,
            mode,
            x_ansys_vc_mode,
            _return_http_data_only=True,
        )
        return data  # type: ignore[no-any-return]

    def _get_layout_section_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        layout_guid: "str",
        section_guid: "str",
        show_full_detail: "Optional[bool]" = None,
        mode: "Optional[str]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "layout_guid",
            "section_guid",
            "show_full_detail",
            "mode",
            "x_ansys_vc_mode",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_layout_section"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'get_layout_section'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'get_layout_section'"
            )
        # verify the required parameter "layout_guid" is set
        if "layout_guid" not in params or params["layout_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'layout_guid' when calling 'get_layout_section'"
            )
        # verify the required parameter "section_guid" is set
        if "section_guid" not in params or params["section_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'section_guid' when calling 'get_layout_section'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "layout_guid" in params and layout_guid is not None:
            path_params["layout-guid"] = params["layout_guid"]
        if "section_guid" in params and section_guid is not None:
            path_params["section-guid"] = params["section_guid"]

        query_params: list[Any] = []
        if "show_full_detail" in params and show_full_detail is not None:
            query_params.append(("showFullDetail", params["show_full_detail"]))
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
            200: "GrantaServerApiSchemaLayoutsLayoutSection",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/layouts/{layout-guid}/sections/{section-guid}",
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

    def get_layout_sections(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        layout_guid: "str",
        show_full_detail: "Optional[bool]" = None,
        mode: "Optional[str]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
    ) -> "Union[GrantaServerApiSchemaLayoutsLayoutSectionsInfo, None]":
        """Get all sections for a layout

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        layout_guid: str
        show_full_detail: bool
        mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the header.
        x_ansys_vc_mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the query string.

        Returns
        -------
        Union[GrantaServerApiSchemaLayoutsLayoutSectionsInfo, None]
        """
        data = self._get_layout_sections_with_http_info(
            database_key,
            table_guid,
            layout_guid,
            show_full_detail,
            mode,
            x_ansys_vc_mode,
            _return_http_data_only=True,
        )
        return data  # type: ignore[no-any-return]

    def _get_layout_sections_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        layout_guid: "str",
        show_full_detail: "Optional[bool]" = None,
        mode: "Optional[str]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "layout_guid",
            "show_full_detail",
            "mode",
            "x_ansys_vc_mode",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_layout_sections"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'get_layout_sections'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'get_layout_sections'"
            )
        # verify the required parameter "layout_guid" is set
        if "layout_guid" not in params or params["layout_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'layout_guid' when calling 'get_layout_sections'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "layout_guid" in params and layout_guid is not None:
            path_params["layout-guid"] = params["layout_guid"]

        query_params: list[Any] = []
        if "show_full_detail" in params and show_full_detail is not None:
            query_params.append(("showFullDetail", params["show_full_detail"]))
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
            200: "GrantaServerApiSchemaLayoutsLayoutSectionsInfo",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/layouts/{layout-guid}/sections",
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

    def reorder_sections(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        layout_guid: "str",
        body: "Optional[GrantaServerApiSchemaLayoutsReorderSectionsInfo]" = None,
    ) -> "Union[GrantaServerApiSchemaLayoutsLayoutSectionsInfo, None]":
        """Reorder the list of layout sections for a layout.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        layout_guid: str
        body: GrantaServerApiSchemaLayoutsReorderSectionsInfo

        Returns
        -------
        Union[GrantaServerApiSchemaLayoutsLayoutSectionsInfo, None]
        """
        data = self._reorder_sections_with_http_info(
            database_key, table_guid, layout_guid, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _reorder_sections_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        layout_guid: "str",
        body: "Optional[GrantaServerApiSchemaLayoutsReorderSectionsInfo]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "layout_guid",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method reorder_sections"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'reorder_sections'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'reorder_sections'"
            )
        # verify the required parameter "layout_guid" is set
        if "layout_guid" not in params or params["layout_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'layout_guid' when calling 'reorder_sections'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "layout_guid" in params and layout_guid is not None:
            path_params["layout-guid"] = params["layout_guid"]

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
            200: "GrantaServerApiSchemaLayoutsLayoutSectionsInfo",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/layouts/{layout-guid}/sections",
            "PUT",
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
