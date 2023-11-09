"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Dict, List, Optional, Union  # noqa: F401
from . import ApiBase


if TYPE_CHECKING:
    from ..models import *


class SchemaSubsetsApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def v1alpha_databases_database_key_tables_table_guid_subsets_get(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        mode: "Optional[str]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
    ) -> "Union[GrantaServerApiSchemaSubsetsSubsetsInfo, None]":
        """Get all subsets for table

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the header.
        x_ansys_vc_mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the query string.

        Returns
        -------
        Union[GrantaServerApiSchemaSubsetsSubsetsInfo, None]
        """
        data = self._v1alpha_databases_database_key_tables_table_guid_subsets_get_with_http_info(
            database_key, table_guid, mode, x_ansys_vc_mode, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _v1alpha_databases_database_key_tables_table_guid_subsets_get_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        mode: "Optional[str]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
        **kwargs,
    ):
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
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_tables_table_guid_subsets_get"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_tables_table_guid_subsets_get'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'v1alpha_databases_database_key_tables_table_guid_subsets_get'"
            )

        collection_formats = {}

        path_params = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]

        query_params = []
        if "mode" in params and mode is not None:
            query_params.append(("mode", params["mode"]))

        header_params = {}
        if "x_ansys_vc_mode" in params and x_ansys_vc_mode is not None:
            header_params["X-Ansys-VC-Mode"] = params["x_ansys_vc_mode"]

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        response_type_map = {
            200: "GrantaServerApiSchemaSubsetsSubsetsInfo",
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

    def v1alpha_databases_database_key_tables_table_guid_subsets_post(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        body: "Optional[GrantaServerApiSchemaSubsetsCreateSubset]" = None,
    ) -> "Union[GrantaServerApiSchemaSubsetsSubset, None]":
        """Create a new subset.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        body: GrantaServerApiSchemaSubsetsCreateSubset

        Returns
        -------
        Union[GrantaServerApiSchemaSubsetsSubset, None]
        """
        data = self._v1alpha_databases_database_key_tables_table_guid_subsets_post_with_http_info(
            database_key, table_guid, body, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _v1alpha_databases_database_key_tables_table_guid_subsets_post_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        body: "Optional[GrantaServerApiSchemaSubsetsCreateSubset]" = None,
        **kwargs,
    ):
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
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_tables_table_guid_subsets_post"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_tables_table_guid_subsets_post'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'v1alpha_databases_database_key_tables_table_guid_subsets_post'"
            )

        collection_formats = {}

        path_params = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            [
                "application/json-patch+json",
                "application/json",
                "text/json",
                "application/*+json",
            ]
        )

        response_type_map = {
            201: "GrantaServerApiSchemaSubsetsSubset",
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

    def v1alpha_databases_database_key_tables_table_guid_subsets_subset_guid_delete(
        self, *, database_key: "str", table_guid: "str", subset_guid: "str"
    ) -> "None":
        """Delete a subset.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        subset_guid: str

        Returns
        -------
        None
        """
        data = self._v1alpha_databases_database_key_tables_table_guid_subsets_subset_guid_delete_with_http_info(
            database_key, table_guid, subset_guid, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _v1alpha_databases_database_key_tables_table_guid_subsets_subset_guid_delete_with_http_info(
        self, database_key: "str", table_guid: "str", subset_guid: "str", **kwargs
    ):
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
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_tables_table_guid_subsets_subset_guid_delete"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_tables_table_guid_subsets_subset_guid_delete'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'v1alpha_databases_database_key_tables_table_guid_subsets_subset_guid_delete'"
            )
        # verify the required parameter "subset_guid" is set
        if "subset_guid" not in params or params["subset_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'subset_guid' when calling 'v1alpha_databases_database_key_tables_table_guid_subsets_subset_guid_delete'"
            )

        collection_formats = {}

        path_params = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "subset_guid" in params and subset_guid is not None:
            path_params["subset-guid"] = params["subset_guid"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        response_type_map = {
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

    def v1alpha_databases_database_key_tables_table_guid_subsets_subset_guid_get(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        subset_guid: "str",
        mode: "Optional[str]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
    ) -> "Union[GrantaServerApiSchemaSubsetsSubset, None]":
        """Get a subset with a specified guid for a given database and table.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        subset_guid: str
        mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the header.
        x_ansys_vc_mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the query string.

        Returns
        -------
        Union[GrantaServerApiSchemaSubsetsSubset, None]
        """
        data = self._v1alpha_databases_database_key_tables_table_guid_subsets_subset_guid_get_with_http_info(
            database_key,
            table_guid,
            subset_guid,
            mode,
            x_ansys_vc_mode,
            _return_http_data_only=True,
        )
        return data  # type: ignore[return-value]

    def _v1alpha_databases_database_key_tables_table_guid_subsets_subset_guid_get_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        subset_guid: "str",
        mode: "Optional[str]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
        **kwargs,
    ):
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
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_tables_table_guid_subsets_subset_guid_get"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_tables_table_guid_subsets_subset_guid_get'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'v1alpha_databases_database_key_tables_table_guid_subsets_subset_guid_get'"
            )
        # verify the required parameter "subset_guid" is set
        if "subset_guid" not in params or params["subset_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'subset_guid' when calling 'v1alpha_databases_database_key_tables_table_guid_subsets_subset_guid_get'"
            )

        collection_formats = {}

        path_params = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "subset_guid" in params and subset_guid is not None:
            path_params["subset-guid"] = params["subset_guid"]

        query_params = []
        if "mode" in params and mode is not None:
            query_params.append(("mode", params["mode"]))

        header_params = {}
        if "x_ansys_vc_mode" in params and x_ansys_vc_mode is not None:
            header_params["X-Ansys-VC-Mode"] = params["x_ansys_vc_mode"]

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        response_type_map = {
            200: "GrantaServerApiSchemaSubsetsSubset",
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

    def v1alpha_databases_database_key_tables_table_guid_subsets_subset_guid_patch(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        subset_guid: "str",
        body: "Optional[GrantaServerApiSchemaSubsetsUpdateSubset]" = None,
    ) -> "Union[GrantaServerApiSchemaSubsetsSubset, None]":
        """Update a subset.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        subset_guid: str
        body: GrantaServerApiSchemaSubsetsUpdateSubset

        Returns
        -------
        Union[GrantaServerApiSchemaSubsetsSubset, None]
        """
        data = self._v1alpha_databases_database_key_tables_table_guid_subsets_subset_guid_patch_with_http_info(
            database_key, table_guid, subset_guid, body, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _v1alpha_databases_database_key_tables_table_guid_subsets_subset_guid_patch_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        subset_guid: "str",
        body: "Optional[GrantaServerApiSchemaSubsetsUpdateSubset]" = None,
        **kwargs,
    ):
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
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_tables_table_guid_subsets_subset_guid_patch"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_tables_table_guid_subsets_subset_guid_patch'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'v1alpha_databases_database_key_tables_table_guid_subsets_subset_guid_patch'"
            )
        # verify the required parameter "subset_guid" is set
        if "subset_guid" not in params or params["subset_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'subset_guid' when calling 'v1alpha_databases_database_key_tables_table_guid_subsets_subset_guid_patch'"
            )

        collection_formats = {}

        path_params = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "subset_guid" in params and subset_guid is not None:
            path_params["subset-guid"] = params["subset_guid"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            [
                "application/json-patch+json",
                "application/json",
                "text/json",
                "application/*+json",
            ]
        )

        response_type_map = {
            200: "GrantaServerApiSchemaSubsetsSubset",
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
