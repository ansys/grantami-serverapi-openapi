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


class SchemaDataRulesApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def v1alpha_databases_database_key_data_rules_data_rule_guid_delete(
        self, *, database_key: "str", data_rule_guid: "str"
    ) -> "None":
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
        data = self._v1alpha_databases_database_key_data_rules_data_rule_guid_delete_with_http_info(
            database_key, data_rule_guid, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _v1alpha_databases_database_key_data_rules_data_rule_guid_delete_with_http_info(
        self, database_key: "str", data_rule_guid: "str", **kwargs
    ):
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
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_data_rules_data_rule_guid_delete"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_data_rules_data_rule_guid_delete'"
            )
        # verify the required parameter "data_rule_guid" is set
        if "data_rule_guid" not in params or params["data_rule_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'data_rule_guid' when calling 'v1alpha_databases_database_key_data_rules_data_rule_guid_delete'"
            )

        collection_formats = {}

        path_params = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "data_rule_guid" in params and data_rule_guid is not None:
            path_params["data-rule-guid"] = params["data_rule_guid"]

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

    def v1alpha_databases_database_key_data_rules_data_rule_guid_get(
        self, *, database_key: "str", data_rule_guid: "str"
    ) -> "Union[GrantaServerApiSchemaDataRule, None]":
        """Gets a data rule for a given database and guid.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        data_rule_guid: str

        Returns
        -------
        Union[GrantaServerApiSchemaDataRule, None]
        """
        data = self._v1alpha_databases_database_key_data_rules_data_rule_guid_get_with_http_info(
            database_key, data_rule_guid, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _v1alpha_databases_database_key_data_rules_data_rule_guid_get_with_http_info(
        self, database_key: "str", data_rule_guid: "str", **kwargs
    ):
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
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_data_rules_data_rule_guid_get"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_data_rules_data_rule_guid_get'"
            )
        # verify the required parameter "data_rule_guid" is set
        if "data_rule_guid" not in params or params["data_rule_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'data_rule_guid' when calling 'v1alpha_databases_database_key_data_rules_data_rule_guid_get'"
            )

        collection_formats = {}

        path_params = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "data_rule_guid" in params and data_rule_guid is not None:
            path_params["data-rule-guid"] = params["data_rule_guid"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        response_type_map = {
            200: "GrantaServerApiSchemaDataRule",
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

    def v1alpha_databases_database_key_data_rules_data_rule_guid_patch(
        self,
        *,
        database_key: "str",
        data_rule_guid: "str",
        body: "Optional[GrantaServerApiSchemaUpdateDataRule]" = None,
    ) -> "Union[GrantaServerApiSchemaDataRule, None]":
        """Edit a data rule

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        data_rule_guid: str
        body: GrantaServerApiSchemaUpdateDataRule

        Returns
        -------
        Union[GrantaServerApiSchemaDataRule, None]
        """
        data = self._v1alpha_databases_database_key_data_rules_data_rule_guid_patch_with_http_info(
            database_key, data_rule_guid, body, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _v1alpha_databases_database_key_data_rules_data_rule_guid_patch_with_http_info(
        self,
        database_key: "str",
        data_rule_guid: "str",
        body: "Optional[GrantaServerApiSchemaUpdateDataRule]" = None,
        **kwargs,
    ):
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
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_data_rules_data_rule_guid_patch"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_data_rules_data_rule_guid_patch'"
            )
        # verify the required parameter "data_rule_guid" is set
        if "data_rule_guid" not in params or params["data_rule_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'data_rule_guid' when calling 'v1alpha_databases_database_key_data_rules_data_rule_guid_patch'"
            )

        collection_formats = {}

        path_params = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "data_rule_guid" in params and data_rule_guid is not None:
            path_params["data-rule-guid"] = params["data_rule_guid"]

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
            200: "GrantaServerApiSchemaDataRule",
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

    def v1alpha_databases_database_key_data_rules_get(
        self, *, database_key: "str"
    ) -> "Union[GrantaServerApiSchemaDataRulesInfo, None]":
        """Gets all data rules for a given database.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str

        Returns
        -------
        Union[GrantaServerApiSchemaDataRulesInfo, None]
        """
        data = self._v1alpha_databases_database_key_data_rules_get_with_http_info(
            database_key, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _v1alpha_databases_database_key_data_rules_get_with_http_info(
        self, database_key: "str", **kwargs
    ):
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
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_data_rules_get"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_data_rules_get'"
            )

        collection_formats = {}

        path_params = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        response_type_map = {
            200: "GrantaServerApiSchemaDataRulesInfo",
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

    def v1alpha_databases_database_key_data_rules_post(
        self,
        *,
        database_key: "str",
        body: "Optional[GrantaServerApiSchemaDataRule]" = None,
    ) -> "Union[GrantaServerApiSchemaDataRule, None]":
        """Create a new data rule

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        body: GrantaServerApiSchemaDataRule

        Returns
        -------
        Union[GrantaServerApiSchemaDataRule, None]
        """
        data = self._v1alpha_databases_database_key_data_rules_post_with_http_info(
            database_key, body, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _v1alpha_databases_database_key_data_rules_post_with_http_info(
        self,
        database_key: "str",
        body: "Optional[GrantaServerApiSchemaDataRule]" = None,
        **kwargs,
    ):
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
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_data_rules_post"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_data_rules_post'"
            )

        collection_formats = {}

        path_params = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]

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
            200: "GrantaServerApiSchemaDataRule",
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
