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


class SchemaParametersApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def create_parameter(
        self,
        *,
        database_key: "str",
        body: "Optional[GrantaServerApiSchemaParametersCreateParameter]" = None,
    ) -> "Union[GrantaServerApiSchemaParametersParameter, None]":
        """Create a new parameter.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        body: GrantaServerApiSchemaParametersCreateParameter

        Returns
        -------
        Union[GrantaServerApiSchemaParametersParameter, None]
        """
        data = self._create_parameter_with_http_info(
            database_key, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _create_parameter_with_http_info(
        self,
        database_key: "str",
        body: "Optional[GrantaServerApiSchemaParametersCreateParameter]" = None,
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
                    f"Got an unexpected keyword argument '{key}' to method create_parameter"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'create_parameter'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json-patch+json", "application/json", "text/json", "application/*+json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            201: "GrantaServerApiSchemaParametersParameter",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/parameters",
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

    def create_parameter_value(
        self,
        *,
        database_key: "str",
        parameter_guid: "str",
        body: "Optional[GrantaServerApiSchemaParametersCreateParameterValue]" = None,
    ) -> "Union[GrantaServerApiSchemaParametersParameterValue, None]":
        """Create a new parameter value.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        parameter_guid: str
        body: GrantaServerApiSchemaParametersCreateParameterValue

        Returns
        -------
        Union[GrantaServerApiSchemaParametersParameterValue, None]
        """
        data = self._create_parameter_value_with_http_info(
            database_key, parameter_guid, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _create_parameter_value_with_http_info(
        self,
        database_key: "str",
        parameter_guid: "str",
        body: "Optional[GrantaServerApiSchemaParametersCreateParameterValue]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "parameter_guid",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method create_parameter_value"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'create_parameter_value'"
            )
        # verify the required parameter "parameter_guid" is set
        if "parameter_guid" not in params or params["parameter_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'parameter_guid' when calling 'create_parameter_value'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "parameter_guid" in params and parameter_guid is not None:
            path_params["parameter-guid"] = params["parameter_guid"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json-patch+json", "application/json", "text/json", "application/*+json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            201: "GrantaServerApiSchemaParametersParameterValue",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/parameters/{parameter-guid}/parameter-values",
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

    def delete_parameter(
        self, *, database_key: "str", parameter_guid: "str"
    ) -> "Union[GrantaServerApiExceptionsDeletionParameterDeletionException, None]":
        """Delete a parameter.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        parameter_guid: str

        Returns
        -------
        Union[GrantaServerApiExceptionsDeletionParameterDeletionException, None]
        """
        data = self._delete_parameter_with_http_info(
            database_key, parameter_guid, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _delete_parameter_with_http_info(
        self, database_key: "str", parameter_guid: "str", **kwargs: Any
    ) -> Any:
        all_params = [
            "database_key",
            "parameter_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method delete_parameter"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'delete_parameter'"
            )
        # verify the required parameter "parameter_guid" is set
        if "parameter_guid" not in params or params["parameter_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'parameter_guid' when calling 'delete_parameter'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "parameter_guid" in params and parameter_guid is not None:
            path_params["parameter-guid"] = params["parameter_guid"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: Dict[int, Optional[str]] = {
            400: "GrantaServerApiExceptionsDeletionParameterDeletionException",
            200: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/parameters/{parameter-guid}",
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

    def delete_parameter_value(
        self, *, database_key: "str", parameter_guid: "str", parameter_value_guid: "str"
    ) -> "Union[GrantaServerApiExceptionsDeletionParameterValueDeletionException, None]":
        """Delete a parameter value.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        parameter_guid: str
        parameter_value_guid: str

        Returns
        -------
        Union[GrantaServerApiExceptionsDeletionParameterValueDeletionException, None]
        """
        data = self._delete_parameter_value_with_http_info(
            database_key, parameter_guid, parameter_value_guid, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _delete_parameter_value_with_http_info(
        self, database_key: "str", parameter_guid: "str", parameter_value_guid: "str", **kwargs: Any
    ) -> Any:
        all_params = [
            "database_key",
            "parameter_guid",
            "parameter_value_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method delete_parameter_value"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'delete_parameter_value'"
            )
        # verify the required parameter "parameter_guid" is set
        if "parameter_guid" not in params or params["parameter_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'parameter_guid' when calling 'delete_parameter_value'"
            )
        # verify the required parameter "parameter_value_guid" is set
        if "parameter_value_guid" not in params or params["parameter_value_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'parameter_value_guid' when calling 'delete_parameter_value'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "parameter_guid" in params and parameter_guid is not None:
            path_params["parameter-guid"] = params["parameter_guid"]
        if "parameter_value_guid" in params and parameter_value_guid is not None:
            path_params["parameter-value-guid"] = params["parameter_value_guid"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: Dict[int, Optional[str]] = {
            400: "GrantaServerApiExceptionsDeletionParameterValueDeletionException",
            200: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/parameters/{parameter-guid}/parameter-values/{parameter-value-guid}",
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

    def get_objects_using_parameter(
        self, *, database_key: "str", parameter_guid: "str"
    ) -> "Union[GrantaServerApiSchemaSlimEntitiesSlimObjects, None]":
        """Get attributes which currently use the given parameter.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        parameter_guid: str

        Returns
        -------
        Union[GrantaServerApiSchemaSlimEntitiesSlimObjects, None]
        """
        data = self._get_objects_using_parameter_with_http_info(
            database_key, parameter_guid, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _get_objects_using_parameter_with_http_info(
        self, database_key: "str", parameter_guid: "str", **kwargs: Any
    ) -> Any:
        all_params = [
            "database_key",
            "parameter_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_objects_using_parameter"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'get_objects_using_parameter'"
            )
        # verify the required parameter "parameter_guid" is set
        if "parameter_guid" not in params or params["parameter_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'parameter_guid' when calling 'get_objects_using_parameter'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "parameter_guid" in params and parameter_guid is not None:
            path_params["parameter-guid"] = params["parameter_guid"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiSchemaSlimEntitiesSlimObjects",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/parameters/{parameter-guid}:usages",
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

    def get_parameter(
        self, *, database_key: "str", parameter_guid: "str"
    ) -> "Union[GrantaServerApiSchemaParametersParameter, None]":
        """Get a parameter with a specified guid for a given database.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        parameter_guid: str

        Returns
        -------
        Union[GrantaServerApiSchemaParametersParameter, None]
        """
        data = self._get_parameter_with_http_info(
            database_key, parameter_guid, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _get_parameter_with_http_info(
        self, database_key: "str", parameter_guid: "str", **kwargs: Any
    ) -> Any:
        all_params = [
            "database_key",
            "parameter_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_parameter"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'get_parameter'"
            )
        # verify the required parameter "parameter_guid" is set
        if "parameter_guid" not in params or params["parameter_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'parameter_guid' when calling 'get_parameter'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "parameter_guid" in params and parameter_guid is not None:
            path_params["parameter-guid"] = params["parameter_guid"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiSchemaParametersParameter",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/parameters/{parameter-guid}",
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

    def get_parameter_value(
        self, *, database_key: "str", parameter_guid: "str", parameter_value_guid: "str"
    ) -> "Union[GrantaServerApiSchemaParametersParameterValue, None]":
        """Get a parameter value with a specified guid for a given database for a given parameter.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        parameter_guid: str
        parameter_value_guid: str

        Returns
        -------
        Union[GrantaServerApiSchemaParametersParameterValue, None]
        """
        data = self._get_parameter_value_with_http_info(
            database_key, parameter_guid, parameter_value_guid, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _get_parameter_value_with_http_info(
        self, database_key: "str", parameter_guid: "str", parameter_value_guid: "str", **kwargs: Any
    ) -> Any:
        all_params = [
            "database_key",
            "parameter_guid",
            "parameter_value_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_parameter_value"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'get_parameter_value'"
            )
        # verify the required parameter "parameter_guid" is set
        if "parameter_guid" not in params or params["parameter_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'parameter_guid' when calling 'get_parameter_value'"
            )
        # verify the required parameter "parameter_value_guid" is set
        if "parameter_value_guid" not in params or params["parameter_value_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'parameter_value_guid' when calling 'get_parameter_value'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "parameter_guid" in params and parameter_guid is not None:
            path_params["parameter-guid"] = params["parameter_guid"]
        if "parameter_value_guid" in params and parameter_value_guid is not None:
            path_params["parameter-value-guid"] = params["parameter_value_guid"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiSchemaParametersParameterValue",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/parameters/{parameter-guid}/parameter-values/{parameter-value-guid}",
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

    def get_parameters(
        self, *, database_key: "str"
    ) -> "Union[GrantaServerApiSchemaParametersParametersInfo, None]":
        """Get all parameters for a given database.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str

        Returns
        -------
        Union[GrantaServerApiSchemaParametersParametersInfo, None]
        """
        data = self._get_parameters_with_http_info(database_key, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _get_parameters_with_http_info(self, database_key: "str", **kwargs: Any) -> Any:
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
                    f"Got an unexpected keyword argument '{key}' to method get_parameters"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'get_parameters'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiSchemaParametersParametersInfo",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/parameters",
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

    def update_parameter(
        self,
        *,
        database_key: "str",
        parameter_guid: "str",
        body: "Optional[GrantaServerApiSchemaParametersUpdateParameter]" = None,
    ) -> "Union[GrantaServerApiSchemaParametersParameter, None]":
        """Update a parameter.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        parameter_guid: str
        body: GrantaServerApiSchemaParametersUpdateParameter

        Returns
        -------
        Union[GrantaServerApiSchemaParametersParameter, None]
        """
        data = self._update_parameter_with_http_info(
            database_key, parameter_guid, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _update_parameter_with_http_info(
        self,
        database_key: "str",
        parameter_guid: "str",
        body: "Optional[GrantaServerApiSchemaParametersUpdateParameter]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "parameter_guid",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method update_parameter"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'update_parameter'"
            )
        # verify the required parameter "parameter_guid" is set
        if "parameter_guid" not in params or params["parameter_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'parameter_guid' when calling 'update_parameter'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "parameter_guid" in params and parameter_guid is not None:
            path_params["parameter-guid"] = params["parameter_guid"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json-patch+json", "application/json", "text/json", "application/*+json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiSchemaParametersParameter",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/parameters/{parameter-guid}",
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

    def update_parameter_value(
        self,
        *,
        database_key: "str",
        parameter_guid: "str",
        parameter_value_guid: "str",
        body: "Optional[GrantaServerApiSchemaParametersUpdateParameterValue]" = None,
    ) -> "Union[GrantaServerApiSchemaParametersParameterValue, None]":
        """Update a parameter value.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        parameter_guid: str
        parameter_value_guid: str
        body: GrantaServerApiSchemaParametersUpdateParameterValue

        Returns
        -------
        Union[GrantaServerApiSchemaParametersParameterValue, None]
        """
        data = self._update_parameter_value_with_http_info(
            database_key, parameter_guid, parameter_value_guid, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _update_parameter_value_with_http_info(
        self,
        database_key: "str",
        parameter_guid: "str",
        parameter_value_guid: "str",
        body: "Optional[GrantaServerApiSchemaParametersUpdateParameterValue]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "parameter_guid",
            "parameter_value_guid",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method update_parameter_value"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'update_parameter_value'"
            )
        # verify the required parameter "parameter_guid" is set
        if "parameter_guid" not in params or params["parameter_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'parameter_guid' when calling 'update_parameter_value'"
            )
        # verify the required parameter "parameter_value_guid" is set
        if "parameter_value_guid" not in params or params["parameter_value_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'parameter_value_guid' when calling 'update_parameter_value'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "parameter_guid" in params and parameter_guid is not None:
            path_params["parameter-guid"] = params["parameter_guid"]
        if "parameter_value_guid" in params and parameter_value_guid is not None:
            path_params["parameter-value-guid"] = params["parameter_value_guid"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json-patch+json", "application/json", "text/json", "application/*+json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiSchemaParametersParameterValue",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/parameters/{parameter-guid}/parameter-values/{parameter-value-guid}",
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
