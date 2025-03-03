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


class SchemaDataRulesApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def create_data_rule(
        self,
        *,
        database_key: "str",
        body: "Optional[GrantaServerApiSchemaDataRulesCreateDataRule]" = None,
    ) -> "Union[GrantaServerApiSchemaDataRulesDataRule, None]":
        """Create a new data rule

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        body: GrantaServerApiSchemaDataRulesCreateDataRule

        Returns
        -------
        Union[GrantaServerApiSchemaDataRulesDataRule, None]
        """
        data = self._create_data_rule_with_http_info(
            database_key, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _create_data_rule_with_http_info(
        self,
        database_key: "str",
        body: "Optional[GrantaServerApiSchemaDataRulesCreateDataRule]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method create_data_rule"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'create_data_rule'"
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
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json-patch+json", "application/json", "text/json", "application/*+json"]
        )

        response_type_map: dict[int, Optional[str]] = {
            201: "GrantaServerApiSchemaDataRulesDataRule",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/data-rules",
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

    def delete_data_rule(self, *, database_key: "str", data_rule_guid: "str") -> "None":
        """Delete a data rule.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        data_rule_guid: str

        Returns
        -------
        None
        """
        data = self._delete_data_rule_with_http_info(
            database_key, data_rule_guid, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _delete_data_rule_with_http_info(
        self, database_key: "str", data_rule_guid: "str", **kwargs: Any
    ) -> Any:
        all_params = [
            "database_key",
            "data_rule_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method delete_data_rule"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'delete_data_rule'"
            )
        # verify the required parameter "data_rule_guid" is set
        if "data_rule_guid" not in params or params["data_rule_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'data_rule_guid' when calling 'delete_data_rule'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "data_rule_guid" in params and data_rule_guid is not None:
            path_params["data-rule-guid"] = params["data_rule_guid"]

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
            "/v1alpha/databases/{database-key}/data-rules/{data-rule-guid}",
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

    def get_data_rule(
        self, *, database_key: "str", data_rule_guid: "str"
    ) -> "Union[GrantaServerApiSchemaDataRulesDataRule, None]":
        """Gets a data rule for a given database and guid.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        data_rule_guid: str

        Returns
        -------
        Union[GrantaServerApiSchemaDataRulesDataRule, None]
        """
        data = self._get_data_rule_with_http_info(
            database_key, data_rule_guid, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _get_data_rule_with_http_info(
        self, database_key: "str", data_rule_guid: "str", **kwargs: Any
    ) -> Any:
        all_params = [
            "database_key",
            "data_rule_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_data_rule"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'get_data_rule'"
            )
        # verify the required parameter "data_rule_guid" is set
        if "data_rule_guid" not in params or params["data_rule_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'data_rule_guid' when calling 'get_data_rule'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "data_rule_guid" in params and data_rule_guid is not None:
            path_params["data-rule-guid"] = params["data_rule_guid"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: dict[int, Optional[str]] = {
            200: "GrantaServerApiSchemaDataRulesDataRule",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/data-rules/{data-rule-guid}",
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

    def get_data_rules(
        self, *, database_key: "str"
    ) -> "Union[GrantaServerApiSchemaDataRulesDataRulesInfo, None]":
        """Gets all data rules for a given database.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str

        Returns
        -------
        Union[GrantaServerApiSchemaDataRulesDataRulesInfo, None]
        """
        data = self._get_data_rules_with_http_info(database_key, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _get_data_rules_with_http_info(self, database_key: "str", **kwargs: Any) -> Any:
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
                    f"Got an unexpected keyword argument '{key}' to method get_data_rules"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'get_data_rules'"
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
            200: "GrantaServerApiSchemaDataRulesDataRulesInfo",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/data-rules",
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

    def update_data_rule(
        self,
        *,
        database_key: "str",
        data_rule_guid: "str",
        body: "Optional[GrantaServerApiSchemaDataRulesUpdateDataRule]" = None,
    ) -> "Union[GrantaServerApiSchemaDataRulesDataRule, None]":
        """Edit a data rule

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        data_rule_guid: str
        body: GrantaServerApiSchemaDataRulesUpdateDataRule

        Returns
        -------
        Union[GrantaServerApiSchemaDataRulesDataRule, None]
        """
        data = self._update_data_rule_with_http_info(
            database_key, data_rule_guid, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _update_data_rule_with_http_info(
        self,
        database_key: "str",
        data_rule_guid: "str",
        body: "Optional[GrantaServerApiSchemaDataRulesUpdateDataRule]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "data_rule_guid",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method update_data_rule"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'update_data_rule'"
            )
        # verify the required parameter "data_rule_guid" is set
        if "data_rule_guid" not in params or params["data_rule_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'data_rule_guid' when calling 'update_data_rule'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "data_rule_guid" in params and data_rule_guid is not None:
            path_params["data-rule-guid"] = params["data_rule_guid"]

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
            200: "GrantaServerApiSchemaDataRulesDataRule",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/data-rules/{data-rule-guid}",
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
