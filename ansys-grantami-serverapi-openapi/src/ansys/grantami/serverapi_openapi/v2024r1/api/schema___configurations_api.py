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


class SchemaConfigurationsApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def v1alpha_databases_database_key_configurations_configuration_type_configuration_guid_delete(
        self, *, database_key: "str", configuration_type: "str", configuration_guid: "str"
    ) -> "None":
        """Delete a configuration

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        configuration_type: str
            The configuration type.
        configuration_guid: str

        Returns
        -------
        None
        """
        data = self._v1alpha_databases_database_key_configurations_configuration_type_configuration_guid_delete_with_http_info(
            database_key, configuration_type, configuration_guid, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _v1alpha_databases_database_key_configurations_configuration_type_configuration_guid_delete_with_http_info(
        self,
        database_key: "str",
        configuration_type: "str",
        configuration_guid: "str",
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "configuration_type",
            "configuration_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_configurations_configuration_type_configuration_guid_delete"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_configurations_configuration_type_configuration_guid_delete'"
            )
        # verify the required parameter "configuration_type" is set
        if "configuration_type" not in params or params["configuration_type"] is None:
            raise ValueError(
                "Missing the required parameter 'configuration_type' when calling 'v1alpha_databases_database_key_configurations_configuration_type_configuration_guid_delete'"
            )
        # verify the required parameter "configuration_guid" is set
        if "configuration_guid" not in params or params["configuration_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'configuration_guid' when calling 'v1alpha_databases_database_key_configurations_configuration_type_configuration_guid_delete'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "configuration_type" in params and configuration_type is not None:
            path_params["configuration-type"] = params["configuration_type"]
        if "configuration_guid" in params and configuration_guid is not None:
            path_params["configuration-guid"] = params["configuration_guid"]

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
            "/v1alpha/databases/{database-key}/configurations/{configuration-type}/{configuration-guid}",
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

    def v1alpha_databases_database_key_configurations_configuration_type_configuration_guid_get(
        self, *, database_key: "str", configuration_type: "str", configuration_guid: "str"
    ) -> "Union[GrantaServerApiSchemaConfigurationsConfiguration, None]":
        """Get individual configuration

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        configuration_type: str
            The configuration type.
        configuration_guid: str

        Returns
        -------
        Union[GrantaServerApiSchemaConfigurationsConfiguration, None]
        """
        data = self._v1alpha_databases_database_key_configurations_configuration_type_configuration_guid_get_with_http_info(
            database_key, configuration_type, configuration_guid, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _v1alpha_databases_database_key_configurations_configuration_type_configuration_guid_get_with_http_info(
        self,
        database_key: "str",
        configuration_type: "str",
        configuration_guid: "str",
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "configuration_type",
            "configuration_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_configurations_configuration_type_configuration_guid_get"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_configurations_configuration_type_configuration_guid_get'"
            )
        # verify the required parameter "configuration_type" is set
        if "configuration_type" not in params or params["configuration_type"] is None:
            raise ValueError(
                "Missing the required parameter 'configuration_type' when calling 'v1alpha_databases_database_key_configurations_configuration_type_configuration_guid_get'"
            )
        # verify the required parameter "configuration_guid" is set
        if "configuration_guid" not in params or params["configuration_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'configuration_guid' when calling 'v1alpha_databases_database_key_configurations_configuration_type_configuration_guid_get'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "configuration_type" in params and configuration_type is not None:
            path_params["configuration-type"] = params["configuration_type"]
        if "configuration_guid" in params and configuration_guid is not None:
            path_params["configuration-guid"] = params["configuration_guid"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: dict[int, Optional[str]] = {
            200: "GrantaServerApiSchemaConfigurationsConfiguration",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/configurations/{configuration-type}/{configuration-guid}",
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

    def v1alpha_databases_database_key_configurations_configuration_type_configuration_guid_patch(
        self,
        *,
        database_key: "str",
        configuration_type: "str",
        configuration_guid: "str",
        body: "Optional[GrantaServerApiSchemaConfigurationsUpdateConfiguration]" = None,
    ) -> "Union[GrantaServerApiSchemaConfigurationsConfiguration, None]":
        """Update a configuration.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        configuration_type: str
            The configuration type.
        configuration_guid: str
        body: GrantaServerApiSchemaConfigurationsUpdateConfiguration

        Returns
        -------
        Union[GrantaServerApiSchemaConfigurationsConfiguration, None]
        """
        data = self._v1alpha_databases_database_key_configurations_configuration_type_configuration_guid_patch_with_http_info(
            database_key, configuration_type, configuration_guid, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _v1alpha_databases_database_key_configurations_configuration_type_configuration_guid_patch_with_http_info(
        self,
        database_key: "str",
        configuration_type: "str",
        configuration_guid: "str",
        body: "Optional[GrantaServerApiSchemaConfigurationsUpdateConfiguration]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "configuration_type",
            "configuration_guid",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_configurations_configuration_type_configuration_guid_patch"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_configurations_configuration_type_configuration_guid_patch'"
            )
        # verify the required parameter "configuration_type" is set
        if "configuration_type" not in params or params["configuration_type"] is None:
            raise ValueError(
                "Missing the required parameter 'configuration_type' when calling 'v1alpha_databases_database_key_configurations_configuration_type_configuration_guid_patch'"
            )
        # verify the required parameter "configuration_guid" is set
        if "configuration_guid" not in params or params["configuration_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'configuration_guid' when calling 'v1alpha_databases_database_key_configurations_configuration_type_configuration_guid_patch'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "configuration_type" in params and configuration_type is not None:
            path_params["configuration-type"] = params["configuration_type"]
        if "configuration_guid" in params and configuration_guid is not None:
            path_params["configuration-guid"] = params["configuration_guid"]

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
            200: "GrantaServerApiSchemaConfigurationsConfiguration",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/configurations/{configuration-type}/{configuration-guid}",
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

    def v1alpha_databases_database_key_configurations_configuration_type_configuration_guidexport_get(
        self, *, database_key: "str", configuration_type: "str", configuration_guid: "str"
    ) -> "None":
        """Get individual configuration as a file

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        configuration_type: str
            The configuration type.
        configuration_guid: str

        Returns
        -------
        None
        """
        data = self._v1alpha_databases_database_key_configurations_configuration_type_configuration_guidexport_get_with_http_info(
            database_key, configuration_type, configuration_guid, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _v1alpha_databases_database_key_configurations_configuration_type_configuration_guidexport_get_with_http_info(
        self,
        database_key: "str",
        configuration_type: "str",
        configuration_guid: "str",
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "configuration_type",
            "configuration_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_configurations_configuration_type_configuration_guidexport_get"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_configurations_configuration_type_configuration_guidexport_get'"
            )
        # verify the required parameter "configuration_type" is set
        if "configuration_type" not in params or params["configuration_type"] is None:
            raise ValueError(
                "Missing the required parameter 'configuration_type' when calling 'v1alpha_databases_database_key_configurations_configuration_type_configuration_guidexport_get'"
            )
        # verify the required parameter "configuration_guid" is set
        if "configuration_guid" not in params or params["configuration_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'configuration_guid' when calling 'v1alpha_databases_database_key_configurations_configuration_type_configuration_guidexport_get'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "configuration_type" in params and configuration_type is not None:
            path_params["configuration-type"] = params["configuration_type"]
        if "configuration_guid" in params and configuration_guid is not None:
            path_params["configuration-guid"] = params["configuration_guid"]

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
            "/v1alpha/databases/{database-key}/configurations/{configuration-type}/{configuration-guid}:export",
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

    def v1alpha_databases_database_key_configurations_configuration_type_get(
        self, *, database_key: "str", configuration_type: "str"
    ) -> "Union[GrantaServerApiSchemaConfigurationsConfigurationsInfo, None]":
        """Get all configurations of given type

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        configuration_type: str
            The configuration type.

        Returns
        -------
        Union[GrantaServerApiSchemaConfigurationsConfigurationsInfo, None]
        """
        data = self._v1alpha_databases_database_key_configurations_configuration_type_get_with_http_info(
            database_key, configuration_type, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _v1alpha_databases_database_key_configurations_configuration_type_get_with_http_info(
        self, database_key: "str", configuration_type: "str", **kwargs: Any
    ) -> Any:
        all_params = [
            "database_key",
            "configuration_type",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_configurations_configuration_type_get"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_configurations_configuration_type_get'"
            )
        # verify the required parameter "configuration_type" is set
        if "configuration_type" not in params or params["configuration_type"] is None:
            raise ValueError(
                "Missing the required parameter 'configuration_type' when calling 'v1alpha_databases_database_key_configurations_configuration_type_get'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "configuration_type" in params and configuration_type is not None:
            path_params["configuration-type"] = params["configuration_type"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: dict[int, Optional[str]] = {
            200: "GrantaServerApiSchemaConfigurationsConfigurationsInfo",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/configurations/{configuration-type}",
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

    def v1alpha_databases_database_key_configurations_configuration_type_post(
        self,
        *,
        database_key: "str",
        configuration_type: "str",
        body: "Optional[GrantaServerApiSchemaConfigurationsCreateConfiguration]" = None,
    ) -> "Union[GrantaServerApiSchemaConfigurationsConfiguration, None]":
        """Create a new configuration.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        configuration_type: str
            The configuration type.
        body: GrantaServerApiSchemaConfigurationsCreateConfiguration

        Returns
        -------
        Union[GrantaServerApiSchemaConfigurationsConfiguration, None]
        """
        data = self._v1alpha_databases_database_key_configurations_configuration_type_post_with_http_info(
            database_key, configuration_type, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _v1alpha_databases_database_key_configurations_configuration_type_post_with_http_info(
        self,
        database_key: "str",
        configuration_type: "str",
        body: "Optional[GrantaServerApiSchemaConfigurationsCreateConfiguration]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "configuration_type",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_configurations_configuration_type_post"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_configurations_configuration_type_post'"
            )
        # verify the required parameter "configuration_type" is set
        if "configuration_type" not in params or params["configuration_type"] is None:
            raise ValueError(
                "Missing the required parameter 'configuration_type' when calling 'v1alpha_databases_database_key_configurations_configuration_type_post'"
            )

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "configuration_type" in params and configuration_type is not None:
            path_params["configuration-type"] = params["configuration_type"]

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
            201: "GrantaServerApiSchemaConfigurationsConfiguration",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/configurations/{configuration-type}",
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
