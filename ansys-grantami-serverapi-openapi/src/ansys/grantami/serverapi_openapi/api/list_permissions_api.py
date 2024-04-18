"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    BinaryIO,
    List,
    Optional,
    Union,
)  # noqa: F401
from . import ApiBase


if TYPE_CHECKING:
    import pathlib
    from ..models import *


class ListPermissionsApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def get_permissions(
        self, *, list_identifier: "str"
    ) -> "Union[GrantaServerApiListsDtoUserPermissionsInfo, None]":
        """Gets all permissions associated with the specified list.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        list_identifier: str

        Returns
        -------
        Union[GrantaServerApiListsDtoUserPermissionsInfo, None]
        """
        data = self._get_permissions_with_http_info(
            list_identifier, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _get_permissions_with_http_info(
        self, list_identifier: "str", **kwargs: Any
    ) -> Any:
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
                    f"Got an unexpected keyword argument '{key}' to method get_permissions"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "list_identifier" is set
        if "list_identifier" not in params or params["list_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'list_identifier' when calling 'get_permissions'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "list_identifier" in params and list_identifier is not None:
            path_params["listIdentifier"] = params["list_identifier"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiListsDtoUserPermissionsInfo",
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/api/v1/lists/list/{listIdentifier}/permissions",
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

    def get_permissions_for_user(
        self, *, list_identifier: "str", user_identifier: "str"
    ) -> "Union[GrantaServerApiListsDtoRecordListPermissionFlags, None]":
        """Gets the permission flags of the permission associating the specified list with the specified user.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        list_identifier: str
        user_identifier: str

        Returns
        -------
        Union[GrantaServerApiListsDtoRecordListPermissionFlags, None]
        """
        data = self._get_permissions_for_user_with_http_info(
            list_identifier, user_identifier, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _get_permissions_for_user_with_http_info(
        self, list_identifier: "str", user_identifier: "str", **kwargs: Any
    ) -> Any:
        all_params = [
            "list_identifier",
            "user_identifier",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_permissions_for_user"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "list_identifier" is set
        if "list_identifier" not in params or params["list_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'list_identifier' when calling 'get_permissions_for_user'"
            )
        # verify the required parameter "user_identifier" is set
        if "user_identifier" not in params or params["user_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'user_identifier' when calling 'get_permissions_for_user'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "list_identifier" in params and list_identifier is not None:
            path_params["listIdentifier"] = params["list_identifier"]
        if "user_identifier" in params and user_identifier is not None:
            path_params["userIdentifier"] = params["user_identifier"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiListsDtoRecordListPermissionFlags",
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/api/v1/lists/list/{listIdentifier}/permissions/user/{userIdentifier}",
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

    def set_permissions(
        self,
        *,
        list_identifier: "str",
        body: "Optional[GrantaServerApiListsDtoUpdateUserPermissionsInfo]" = None,
    ) -> "Union[GrantaServerApiListsDtoUserPermissionsInfo, None]":
        """Sets permissions for the specified list. Returns a collection of the created/updated permissions.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        list_identifier: str
        body: GrantaServerApiListsDtoUpdateUserPermissionsInfo

        Returns
        -------
        Union[GrantaServerApiListsDtoUserPermissionsInfo, None]
        """
        data = self._set_permissions_with_http_info(
            list_identifier, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _set_permissions_with_http_info(
        self,
        list_identifier: "str",
        body: "Optional[GrantaServerApiListsDtoUpdateUserPermissionsInfo]" = None,
        **kwargs: Any,
    ) -> Any:
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
                    f"Got an unexpected keyword argument '{key}' to method set_permissions"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "list_identifier" is set
        if "list_identifier" not in params or params["list_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'list_identifier' when calling 'set_permissions'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "list_identifier" in params and list_identifier is not None:
            path_params["listIdentifier"] = params["list_identifier"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

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

        response_type_map: Dict[int, Optional[str]] = {
            202: "GrantaServerApiListsDtoUserPermissionsInfo",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/api/v1/lists/list/{listIdentifier}/permissions",
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

    def set_permissions_for_user(
        self,
        *,
        list_identifier: "str",
        user_identifier: "str",
        body: "Optional[GrantaServerApiListsDtoUpdateRecordListPermissionFlags]" = None,
    ) -> "Union[GrantaServerApiListsDtoRecordListPermissionFlags, None]":
        """Sets the permission flags of the permission associating the specified list with the specified user.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        list_identifier: str
        user_identifier: str
        body: GrantaServerApiListsDtoUpdateRecordListPermissionFlags

        Returns
        -------
        Union[GrantaServerApiListsDtoRecordListPermissionFlags, None]
        """
        data = self._set_permissions_for_user_with_http_info(
            list_identifier, user_identifier, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _set_permissions_for_user_with_http_info(
        self,
        list_identifier: "str",
        user_identifier: "str",
        body: "Optional[GrantaServerApiListsDtoUpdateRecordListPermissionFlags]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "list_identifier",
            "user_identifier",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method set_permissions_for_user"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "list_identifier" is set
        if "list_identifier" not in params or params["list_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'list_identifier' when calling 'set_permissions_for_user'"
            )
        # verify the required parameter "user_identifier" is set
        if "user_identifier" not in params or params["user_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'user_identifier' when calling 'set_permissions_for_user'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "list_identifier" in params and list_identifier is not None:
            path_params["listIdentifier"] = params["list_identifier"]
        if "user_identifier" in params and user_identifier is not None:
            path_params["userIdentifier"] = params["user_identifier"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

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

        response_type_map: Dict[int, Optional[str]] = {
            201: "GrantaServerApiListsDtoRecordListPermissionFlags",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/api/v1/lists/list/{listIdentifier}/permissions/user/{userIdentifier}",
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

    def subscribe(
        self, *, list_identifier: "str"
    ) -> "Union[GrantaServerApiListsDtoUserPermission, None]":
        """Subscribes the calling user to the specified list.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        list_identifier: str

        Returns
        -------
        Union[GrantaServerApiListsDtoUserPermission, None]
        """
        data = self._subscribe_with_http_info(
            list_identifier, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _subscribe_with_http_info(self, list_identifier: "str", **kwargs: Any) -> Any:
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
                    f"Got an unexpected keyword argument '{key}' to method subscribe"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "list_identifier" is set
        if "list_identifier" not in params or params["list_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'list_identifier' when calling 'subscribe'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "list_identifier" in params and list_identifier is not None:
            path_params["listIdentifier"] = params["list_identifier"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            202: "GrantaServerApiListsDtoUserPermission",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/api/v1/lists/list/{listIdentifier}/permissions/subscribe",
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

    def unsubscribe(
        self, *, list_identifier: "str"
    ) -> "Union[GrantaServerApiListsDtoUserPermission, None]":
        """Unsubscribes the calling user from the specified list.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        list_identifier: str

        Returns
        -------
        Union[GrantaServerApiListsDtoUserPermission, None]
        """
        data = self._unsubscribe_with_http_info(
            list_identifier, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _unsubscribe_with_http_info(self, list_identifier: "str", **kwargs: Any) -> Any:
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
                    f"Got an unexpected keyword argument '{key}' to method unsubscribe"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "list_identifier" is set
        if "list_identifier" not in params or params["list_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'list_identifier' when calling 'unsubscribe'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "list_identifier" in params and list_identifier is not None:
            path_params["listIdentifier"] = params["list_identifier"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            202: "GrantaServerApiListsDtoUserPermission",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/api/v1/lists/list/{listIdentifier}/permissions/unsubscribe",
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
