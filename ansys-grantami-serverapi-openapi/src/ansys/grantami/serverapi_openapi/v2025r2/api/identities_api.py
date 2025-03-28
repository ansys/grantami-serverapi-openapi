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


class IdentitiesApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def translate_guids_to_identities(
        self,
        *,
        body: "Optional[GsaTranslateGuidsToIdentitiesRequest]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
        mode: "Optional[str]" = None,
    ) -> "Union[GsaTranslateGuidsToIdentitiesResponse, None]":
        """For internal use only.  Translates guids to identities.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GsaTranslateGuidsToIdentitiesRequest
        x_ansys_vc_mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the query string.
        mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the header.

        Returns
        -------
        Union[GsaTranslateGuidsToIdentitiesResponse, None]
        """
        data = self._translate_guids_to_identities_with_http_info(
            body, x_ansys_vc_mode, mode, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _translate_guids_to_identities_with_http_info(
        self,
        body: "Optional[GsaTranslateGuidsToIdentitiesRequest]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
        mode: "Optional[str]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "body",
            "x_ansys_vc_mode",
            "mode",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method translate_guids_to_identities"
                )
            params[key] = val
        del params["kwargs"]

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}

        query_params: list[Any] = []
        if "mode" in params and mode is not None:
            query_params.append(("mode", params["mode"]))

        header_params: dict[str, Any] = {}
        if "x_ansys_vc_mode" in params and x_ansys_vc_mode is not None:
            header_params["X-Ansys-VC-Mode"] = params["x_ansys_vc_mode"]

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
            200: "GsaTranslateGuidsToIdentitiesResponse",
            400: None,
        }

        return self.api_client.call_api(
            "/v1alpha/identities",
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
