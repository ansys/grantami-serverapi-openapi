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


class PermissionBasedAccessControlApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def get_permission_categories(
        self, *, database_key: "str"
    ) -> "Union[GsaPermissionCategoriesInfo, None]":
        """Get all permission-based access control categories for the specified database.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str

        Returns
        -------
        Union[GsaPermissionCategoriesInfo, None]
        """
        data = self._get_permission_categories_with_http_info(
            database_key, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _get_permission_categories_with_http_info(self, database_key: "str", **kwargs: Any) -> Any:
        all_params = [
            "database_key",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_permission_categories"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'get_permission_categories'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: dict[int, Optional[str]] = {
            200: "GsaPermissionCategoriesInfo",
            403: None,
            404: None,
            422: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/permission-categories",
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

    def get_permission_category(
        self, *, database_key: "str", category_guid: "str"
    ) -> "Union[GsaPermissionCategory, None]":
        """Get a permission-based access control category with a specified guid.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        category_guid: str

        Returns
        -------
        Union[GsaPermissionCategory, None]
        """
        data = self._get_permission_category_with_http_info(
            database_key, category_guid, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _get_permission_category_with_http_info(
        self, database_key: "str", category_guid: "str", **kwargs: Any
    ) -> Any:
        all_params = [
            "database_key",
            "category_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_permission_category"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'get_permission_category'"
            )
        # verify the required parameter "category_guid" is set
        if "category_guid" not in params or params["category_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'category_guid' when calling 'get_permission_category'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "category_guid" in params and category_guid is not None:
            path_params["category-guid"] = params["category_guid"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: dict[int, Optional[str]] = {
            200: "GsaPermissionCategory",
            403: None,
            404: None,
            422: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/permission-categories/{category-guid}",
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

    def get_permission_in_category(
        self, *, database_key: "str", category_guid: "str", permission_guid: "str"
    ) -> "Union[GsaPermission, None]":
        """Get a permission-based access control permission with a given guid in the specified category.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        category_guid: str
        permission_guid: str

        Returns
        -------
        Union[GsaPermission, None]
        """
        data = self._get_permission_in_category_with_http_info(
            database_key, category_guid, permission_guid, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _get_permission_in_category_with_http_info(
        self, database_key: "str", category_guid: "str", permission_guid: "str", **kwargs: Any
    ) -> Any:
        all_params = [
            "database_key",
            "category_guid",
            "permission_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_permission_in_category"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'get_permission_in_category'"
            )
        # verify the required parameter "category_guid" is set
        if "category_guid" not in params or params["category_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'category_guid' when calling 'get_permission_in_category'"
            )
        # verify the required parameter "permission_guid" is set
        if "permission_guid" not in params or params["permission_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'permission_guid' when calling 'get_permission_in_category'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "category_guid" in params and category_guid is not None:
            path_params["category-guid"] = params["category_guid"]
        if "permission_guid" in params and permission_guid is not None:
            path_params["permission-guid"] = params["permission_guid"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: dict[int, Optional[str]] = {
            200: "GsaPermission",
            403: None,
            404: None,
            422: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/permission-categories/{category-guid}/permissions/{permission-guid}",
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

    def get_permissions_in_category(
        self, *, database_key: "str", category_guid: "str"
    ) -> "Union[GsaPermissionsInfo, None]":
        """Get all permission-based access control permissions for the specified category.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        category_guid: str

        Returns
        -------
        Union[GsaPermissionsInfo, None]
        """
        data = self._get_permissions_in_category_with_http_info(
            database_key, category_guid, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _get_permissions_in_category_with_http_info(
        self, database_key: "str", category_guid: "str", **kwargs: Any
    ) -> Any:
        all_params = [
            "database_key",
            "category_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_permissions_in_category"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'get_permissions_in_category'"
            )
        # verify the required parameter "category_guid" is set
        if "category_guid" not in params or params["category_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'category_guid' when calling 'get_permissions_in_category'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "category_guid" in params and category_guid is not None:
            path_params["category-guid"] = params["category_guid"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: dict[int, Optional[str]] = {
            200: "GsaPermissionsInfo",
            403: None,
            404: None,
            422: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/permission-categories/{category-guid}/permissions",
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
