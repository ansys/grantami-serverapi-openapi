"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Dict, IO, List, Optional, Union  # noqa: F401
from . import ApiBase


if TYPE_CHECKING:
    import pathlib
    from ..models import *


class ListManagementApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def api_v1_lists_get(
        self,
    ) -> "Union[GrantaServerApiListsDtoRecordListHeadersInfo, None]":
        """Returns all lists visible to the calling user

        This method makes a synchronous HTTP request.

        Returns
        -------
        Union[GrantaServerApiListsDtoRecordListHeadersInfo, None]
        """
        data = self._api_v1_lists_get_with_http_info(_return_http_data_only=True)
        return data  # type: ignore[return-value]

    def _api_v1_lists_get_with_http_info(self, **kwargs):
        all_params = ["_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method api_v1_lists_get"
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map = {
            200: "GrantaServerApiListsDtoRecordListHeadersInfo",
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

    def api_v1_lists_list_list_identifier_copy_post(
        self, *, list_identifier: "str"
    ) -> "Union[GrantaServerApiListsDtoRecordListHeader, None]":
        """Creates a copy of the list and its items

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        list_identifier: str

        Returns
        -------
        Union[GrantaServerApiListsDtoRecordListHeader, None]
        """
        data = self._api_v1_lists_list_list_identifier_copy_post_with_http_info(
            list_identifier, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _api_v1_lists_list_list_identifier_copy_post_with_http_info(
        self, list_identifier: "str", **kwargs
    ):
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
                    f"Got an unexpected keyword argument '{key}' to method api_v1_lists_list_list_identifier_copy_post"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "list_identifier" is set
        if "list_identifier" not in params or params["list_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'list_identifier' when calling 'api_v1_lists_list_list_identifier_copy_post'"
            )

        collection_formats = {}

        path_params = {}
        if "list_identifier" in params and list_identifier is not None:
            path_params["listIdentifier"] = params["list_identifier"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map = {
            201: "GrantaServerApiListsDtoRecordListHeader",
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

    def api_v1_lists_list_list_identifier_delete(
        self, *, list_identifier: "str"
    ) -> "None":
        """Delete an existing list.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        list_identifier: str

        Returns
        -------
        None
        """
        data = self._api_v1_lists_list_list_identifier_delete_with_http_info(
            list_identifier, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _api_v1_lists_list_list_identifier_delete_with_http_info(
        self, list_identifier: "str", **kwargs
    ):
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
                    f"Got an unexpected keyword argument '{key}' to method api_v1_lists_list_list_identifier_delete"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "list_identifier" is set
        if "list_identifier" not in params or params["list_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'list_identifier' when calling 'api_v1_lists_list_list_identifier_delete'"
            )

        collection_formats = {}

        path_params = {}
        if "list_identifier" in params and list_identifier is not None:
            path_params["listIdentifier"] = params["list_identifier"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        response_type_map = {
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

    def api_v1_lists_list_list_identifier_get(
        self, *, list_identifier: "str"
    ) -> "Union[GrantaServerApiListsDtoRecordListHeader, None]":
        """Returns the given list if it exists and the calling user has read access to it

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        list_identifier: str

        Returns
        -------
        Union[GrantaServerApiListsDtoRecordListHeader, None]
        """
        data = self._api_v1_lists_list_list_identifier_get_with_http_info(
            list_identifier, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _api_v1_lists_list_list_identifier_get_with_http_info(
        self, list_identifier: "str", **kwargs
    ):
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
                    f"Got an unexpected keyword argument '{key}' to method api_v1_lists_list_list_identifier_get"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "list_identifier" is set
        if "list_identifier" not in params or params["list_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'list_identifier' when calling 'api_v1_lists_list_list_identifier_get'"
            )

        collection_formats = {}

        path_params = {}
        if "list_identifier" in params and list_identifier is not None:
            path_params["listIdentifier"] = params["list_identifier"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map = {
            200: "GrantaServerApiListsDtoRecordListHeader",
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

    def api_v1_lists_list_list_identifier_patch(
        self,
        *,
        list_identifier: "str",
        body: "Optional[GrantaServerApiListsDtoUpdateRecordListProperties]" = None,
    ) -> "Union[GrantaServerApiListsDtoRecordListHeader, None]":
        """Performs a partial update on the properties of a list.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        list_identifier: str
        body: GrantaServerApiListsDtoUpdateRecordListProperties

        Returns
        -------
        Union[GrantaServerApiListsDtoRecordListHeader, None]
        """
        data = self._api_v1_lists_list_list_identifier_patch_with_http_info(
            list_identifier, body, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _api_v1_lists_list_list_identifier_patch_with_http_info(
        self,
        list_identifier: "str",
        body: "Optional[GrantaServerApiListsDtoUpdateRecordListProperties]" = None,
        **kwargs,
    ):
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
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method api_v1_lists_list_list_identifier_patch"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "list_identifier" is set
        if "list_identifier" not in params or params["list_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'list_identifier' when calling 'api_v1_lists_list_list_identifier_patch'"
            )

        collection_formats = {}

        path_params = {}
        if "list_identifier" in params and list_identifier is not None:
            path_params["listIdentifier"] = params["list_identifier"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
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
            200: "GrantaServerApiListsDtoRecordListHeader",
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

    def api_v1_lists_list_list_identifier_publish_post(
        self, *, list_identifier: "str"
    ) -> "Union[GrantaServerApiListsDtoRecordListHeader, None]":
        """Update the status of an existing list to \"published\". The list must be awaiting approval, and not already published.  The \"awaiting approval\" flag will be reset to false.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        list_identifier: str

        Returns
        -------
        Union[GrantaServerApiListsDtoRecordListHeader, None]
        """
        data = self._api_v1_lists_list_list_identifier_publish_post_with_http_info(
            list_identifier, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _api_v1_lists_list_list_identifier_publish_post_with_http_info(
        self, list_identifier: "str", **kwargs
    ):
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
                    f"Got an unexpected keyword argument '{key}' to method api_v1_lists_list_list_identifier_publish_post"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "list_identifier" is set
        if "list_identifier" not in params or params["list_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'list_identifier' when calling 'api_v1_lists_list_list_identifier_publish_post'"
            )

        collection_formats = {}

        path_params = {}
        if "list_identifier" in params and list_identifier is not None:
            path_params["listIdentifier"] = params["list_identifier"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map = {
            200: "GrantaServerApiListsDtoRecordListHeader",
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

    def api_v1_lists_list_list_identifier_request_approval_post(
        self, *, list_identifier: "str"
    ) -> "Union[GrantaServerApiListsDtoRecordListHeader, None]":
        """Update the status of an existing list to \"awaiting approval\".

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        list_identifier: str

        Returns
        -------
        Union[GrantaServerApiListsDtoRecordListHeader, None]
        """
        data = self._api_v1_lists_list_list_identifier_request_approval_post_with_http_info(
            list_identifier, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _api_v1_lists_list_list_identifier_request_approval_post_with_http_info(
        self, list_identifier: "str", **kwargs
    ):
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
                    f"Got an unexpected keyword argument '{key}' to method api_v1_lists_list_list_identifier_request_approval_post"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "list_identifier" is set
        if "list_identifier" not in params or params["list_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'list_identifier' when calling 'api_v1_lists_list_list_identifier_request_approval_post'"
            )

        collection_formats = {}

        path_params = {}
        if "list_identifier" in params and list_identifier is not None:
            path_params["listIdentifier"] = params["list_identifier"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map = {
            200: "GrantaServerApiListsDtoRecordListHeader",
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

    def api_v1_lists_list_list_identifier_reset_post(
        self, *, list_identifier: "str"
    ) -> "Union[GrantaServerApiListsDtoRecordListHeader, None]":
        """Update the status of an existing list to not be \"awaiting approval\".

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        list_identifier: str

        Returns
        -------
        Union[GrantaServerApiListsDtoRecordListHeader, None]
        """
        data = self._api_v1_lists_list_list_identifier_reset_post_with_http_info(
            list_identifier, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _api_v1_lists_list_list_identifier_reset_post_with_http_info(
        self, list_identifier: "str", **kwargs
    ):
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
                    f"Got an unexpected keyword argument '{key}' to method api_v1_lists_list_list_identifier_reset_post"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "list_identifier" is set
        if "list_identifier" not in params or params["list_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'list_identifier' when calling 'api_v1_lists_list_list_identifier_reset_post'"
            )

        collection_formats = {}

        path_params = {}
        if "list_identifier" in params and list_identifier is not None:
            path_params["listIdentifier"] = params["list_identifier"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map = {
            200: "GrantaServerApiListsDtoRecordListHeader",
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

    def api_v1_lists_list_list_identifier_revise_post(
        self, *, list_identifier: "str"
    ) -> "Union[GrantaServerApiListsDtoRecordListHeader, None]":
        """Creates a private copy of a list that can be revised.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        list_identifier: str

        Returns
        -------
        Union[GrantaServerApiListsDtoRecordListHeader, None]
        """
        data = self._api_v1_lists_list_list_identifier_revise_post_with_http_info(
            list_identifier, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _api_v1_lists_list_list_identifier_revise_post_with_http_info(
        self, list_identifier: "str", **kwargs
    ):
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
                    f"Got an unexpected keyword argument '{key}' to method api_v1_lists_list_list_identifier_revise_post"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "list_identifier" is set
        if "list_identifier" not in params or params["list_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'list_identifier' when calling 'api_v1_lists_list_list_identifier_revise_post'"
            )

        collection_formats = {}

        path_params = {}
        if "list_identifier" in params and list_identifier is not None:
            path_params["listIdentifier"] = params["list_identifier"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map = {
            201: "GrantaServerApiListsDtoRecordListHeader",
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

    def api_v1_lists_list_list_identifier_unpublish_post(
        self, *, list_identifier: "str"
    ) -> "Union[GrantaServerApiListsDtoRecordListHeader, None]":
        """Update the status of an existing list to \"unpublished\". The list must be published, and awaiting approval.  The \"awaiting approval\" flag will be reset to false.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        list_identifier: str

        Returns
        -------
        Union[GrantaServerApiListsDtoRecordListHeader, None]
        """
        data = self._api_v1_lists_list_list_identifier_unpublish_post_with_http_info(
            list_identifier, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _api_v1_lists_list_list_identifier_unpublish_post_with_http_info(
        self, list_identifier: "str", **kwargs
    ):
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
                    f"Got an unexpected keyword argument '{key}' to method api_v1_lists_list_list_identifier_unpublish_post"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "list_identifier" is set
        if "list_identifier" not in params or params["list_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'list_identifier' when calling 'api_v1_lists_list_list_identifier_unpublish_post'"
            )

        collection_formats = {}

        path_params = {}
        if "list_identifier" in params and list_identifier is not None:
            path_params["listIdentifier"] = params["list_identifier"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map = {
            200: "GrantaServerApiListsDtoRecordListHeader",
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

    def api_v1_lists_post(
        self, *, body: "Optional[GrantaServerApiListsDtoCreateRecordList]" = None
    ) -> "Union[GrantaServerApiListsDtoRecordListHeader, None]":
        """Creates a new list with the specified properties and items.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GrantaServerApiListsDtoCreateRecordList

        Returns
        -------
        Union[GrantaServerApiListsDtoRecordListHeader, None]
        """
        data = self._api_v1_lists_post_with_http_info(body, _return_http_data_only=True)
        return data  # type: ignore[return-value]

    def _api_v1_lists_post_with_http_info(
        self, body: "Optional[GrantaServerApiListsDtoCreateRecordList]" = None, **kwargs
    ):
        all_params = [
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method api_v1_lists_post"
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
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
            201: "GrantaServerApiListsDtoRecordListHeader",
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

    def api_v1_lists_search_post(
        self, *, body: "Optional[GrantaServerApiListsDtoRecordListSearchRequest]" = None
    ) -> "Union[GrantaServerApiListsDtoRecordListSearchInfo, None]":
        """Posts a search request, and returns an object containing search result identifier

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GrantaServerApiListsDtoRecordListSearchRequest

        Returns
        -------
        Union[GrantaServerApiListsDtoRecordListSearchInfo, None]
        """
        data = self._api_v1_lists_search_post_with_http_info(
            body, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _api_v1_lists_search_post_with_http_info(
        self,
        body: "Optional[GrantaServerApiListsDtoRecordListSearchRequest]" = None,
        **kwargs,
    ):
        all_params = [
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method api_v1_lists_search_post"
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
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
            201: "GrantaServerApiListsDtoRecordListSearchInfo",
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

    def api_v1_lists_search_results_result_resource_identifier_get(
        self, *, result_resource_identifier: "str"
    ) -> "Union[GrantaServerApiListsDtoRecordListSearchResultsInfo, None]":
        """Returns the search results found in the specified resource

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        result_resource_identifier: str

        Returns
        -------
        Union[GrantaServerApiListsDtoRecordListSearchResultsInfo, None]
        """
        data = self._api_v1_lists_search_results_result_resource_identifier_get_with_http_info(
            result_resource_identifier, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _api_v1_lists_search_results_result_resource_identifier_get_with_http_info(
        self, result_resource_identifier: "str", **kwargs
    ):
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
                    f"Got an unexpected keyword argument '{key}' to method api_v1_lists_search_results_result_resource_identifier_get"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "result_resource_identifier" is set
        if (
            "result_resource_identifier" not in params
            or params["result_resource_identifier"] is None
        ):
            raise ValueError(
                "Missing the required parameter 'result_resource_identifier' when calling 'api_v1_lists_search_results_result_resource_identifier_get'"
            )

        collection_formats = {}

        path_params = {}
        if (
            "result_resource_identifier" in params
            and result_resource_identifier is not None
        ):
            path_params["resultResourceIdentifier"] = params[
                "result_resource_identifier"
            ]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map = {
            200: "GrantaServerApiListsDtoRecordListSearchResultsInfo",
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
