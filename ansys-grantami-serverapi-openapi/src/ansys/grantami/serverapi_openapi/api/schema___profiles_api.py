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


class SchemaProfilesApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def create_profile(
        self, *, body: "Optional[GrantaServerApiSchemaProfilesCreateProfile]" = None
    ) -> "Union[GrantaServerApiSchemaProfilesProfile, None]":
        """Create a new profile

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GrantaServerApiSchemaProfilesCreateProfile

        Returns
        -------
        Union[GrantaServerApiSchemaProfilesProfile, None]
        """
        data = self._create_profile_with_http_info(body, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _create_profile_with_http_info(
        self,
        body: "Optional[GrantaServerApiSchemaProfilesCreateProfile]" = None,
        **kwargs: Any,
    ) -> Any:
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
                    f"Got an unexpected keyword argument '{key}' to method create_profile"
                )
            params[key] = val
        del params["kwargs"]

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}

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
            [
                "application/json-patch+json",
                "application/json",
                "text/json",
                "application/*+json",
            ]
        )

        response_type_map: Dict[int, Optional[str]] = {
            201: "GrantaServerApiSchemaProfilesProfile",
            400: None,
            403: None,
        }

        return self.api_client.call_api(
            "/v1alpha/profiles",
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

    def delete_profile(self, *, profile_guid: "str") -> "None":
        """Delete a profile

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        profile_guid: str

        Returns
        -------
        None
        """
        data = self._delete_profile_with_http_info(profile_guid, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _delete_profile_with_http_info(self, profile_guid: "str", **kwargs: Any) -> Any:
        all_params = [
            "profile_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method delete_profile"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "profile_guid" is set
        if "profile_guid" not in params or params["profile_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'profile_guid' when calling 'delete_profile'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "profile_guid" in params and profile_guid is not None:
            path_params["profile-guid"] = params["profile_guid"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None

        response_type_map: Dict[int, Optional[str]] = {
            200: None,
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/profiles/{profile-guid}",
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

    def get_profile(
        self, *, profile_guid: "str"
    ) -> "Union[GrantaServerApiSchemaProfilesProfile, None]":
        """Get individual profile

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        profile_guid: str

        Returns
        -------
        Union[GrantaServerApiSchemaProfilesProfile, None]
        """
        data = self._get_profile_with_http_info(profile_guid, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _get_profile_with_http_info(self, profile_guid: "str", **kwargs: Any) -> Any:
        all_params = [
            "profile_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method get_profile")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "profile_guid" is set
        if "profile_guid" not in params or params["profile_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'profile_guid' when calling 'get_profile'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "profile_guid" in params and profile_guid is not None:
            path_params["profile-guid"] = params["profile_guid"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiSchemaProfilesProfile",
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/profiles/{profile-guid}",
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

    def get_profiles(
        self,
    ) -> "Union[GrantaServerApiSchemaProfilesAllProfilesInfo, None]":
        """Get AllProfilesInfo

        This method makes a synchronous HTTP request.

        Returns
        -------
        Union[GrantaServerApiSchemaProfilesAllProfilesInfo, None]
        """
        data = self._get_profiles_with_http_info(_return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _get_profiles_with_http_info(self, **kwargs: Any) -> Any:
        all_params = ["_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_profiles"
                )
            params[key] = val
        del params["kwargs"]

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiSchemaProfilesAllProfilesInfo",
            403: None,
        }

        return self.api_client.call_api(
            "/v1alpha/profiles",
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

    def update_all_profiles_info(
        self,
        *,
        body: "Optional[GrantaServerApiSchemaProfilesUpdateAllProfilesInfo]" = None,
    ) -> "Union[GrantaServerApiSchemaProfilesAllProfilesInfo, None]":
        """Update AllProfilesInfo

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GrantaServerApiSchemaProfilesUpdateAllProfilesInfo

        Returns
        -------
        Union[GrantaServerApiSchemaProfilesAllProfilesInfo, None]
        """
        data = self._update_all_profiles_info_with_http_info(body, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _update_all_profiles_info_with_http_info(
        self,
        body: "Optional[GrantaServerApiSchemaProfilesUpdateAllProfilesInfo]" = None,
        **kwargs: Any,
    ) -> Any:
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
                    f"Got an unexpected keyword argument '{key}' to method update_all_profiles_info"
                )
            params[key] = val
        del params["kwargs"]

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}

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
            [
                "application/json-patch+json",
                "application/json",
                "text/json",
                "application/*+json",
            ]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiSchemaProfilesAllProfilesInfo",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/profiles",
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

    def update_profile(
        self,
        *,
        profile_guid: "str",
        body: "Optional[GrantaServerApiSchemaProfilesUpdateProfile]" = None,
    ) -> "Union[GrantaServerApiSchemaProfilesProfile, None]":
        """Update a profile

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        profile_guid: str
        body: GrantaServerApiSchemaProfilesUpdateProfile

        Returns
        -------
        Union[GrantaServerApiSchemaProfilesProfile, None]
        """
        data = self._update_profile_with_http_info(profile_guid, body, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _update_profile_with_http_info(
        self,
        profile_guid: "str",
        body: "Optional[GrantaServerApiSchemaProfilesUpdateProfile]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "profile_guid",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method update_profile"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "profile_guid" is set
        if "profile_guid" not in params or params["profile_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'profile_guid' when calling 'update_profile'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "profile_guid" in params and profile_guid is not None:
            path_params["profile-guid"] = params["profile_guid"]

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
            [
                "application/json-patch+json",
                "application/json",
                "text/json",
                "application/*+json",
            ]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiSchemaProfilesProfile",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/profiles/{profile-guid}",
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
