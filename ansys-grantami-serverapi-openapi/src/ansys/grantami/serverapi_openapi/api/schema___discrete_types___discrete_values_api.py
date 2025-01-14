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


class SchemaDiscreteTypesDiscreteValuesApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def create_discrete_value(self, *, database_key: "str", discrete_type_guid: "str", body: "Optional[GsaDiscreteValuesCreateDiscreteValue]" = None) -> "Union[GsaDiscreteValuesDiscreteValue, None]":
        """Create new discrete value. It will be added at the end.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        discrete_type_guid: str
        body: GsaDiscreteValuesCreateDiscreteValue

        Returns
        -------
        Union[GsaDiscreteValuesDiscreteValue, None]
        """
        data = self._create_discrete_value_with_http_info(database_key, discrete_type_guid, body, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _create_discrete_value_with_http_info(self, database_key: "str", discrete_type_guid: "str", body: "Optional[GsaDiscreteValuesCreateDiscreteValue]" = None, **kwargs: Any) -> Any:
        all_params = ["database_key", "discrete_type_guid", "body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method create_discrete_value")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError("Missing the required parameter 'database_key' when calling 'create_discrete_value'")
        # verify the required parameter "discrete_type_guid" is set
        if "discrete_type_guid" not in params or params["discrete_type_guid"] is None:
            raise ValueError("Missing the required parameter 'discrete_type_guid' when calling 'create_discrete_value'")

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "discrete_type_guid" in params and discrete_type_guid is not None:
            path_params["discrete-type-guid"] = params["discrete_type_guid"]

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
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json-patch+json", "application/json", "text/json", "application/*+json"])

        response_type_map: dict[int, Optional[str]] = {
            201: "GsaDiscreteValuesDiscreteValue",
            400: None,
            403: None,
            404: None,
        }
        
        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/discrete-types/{discrete-type-guid}/discrete-values", "POST",
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

    def delete_discrete_value(self, *, database_key: "str", discrete_type_guid: "str", discrete_value_guid: "str") -> "Union[GsaDiscreteValueAggregateException, None]":
        """Delete a single discrete value. It must not be used by any data, or the operation will fail.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        discrete_type_guid: str
        discrete_value_guid: str

        Returns
        -------
        Union[GsaDiscreteValueAggregateException, None]
        """
        data = self._delete_discrete_value_with_http_info(database_key, discrete_type_guid, discrete_value_guid, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _delete_discrete_value_with_http_info(self, database_key: "str", discrete_type_guid: "str", discrete_value_guid: "str", **kwargs: Any) -> Any:
        all_params = ["database_key", "discrete_type_guid", "discrete_value_guid", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method delete_discrete_value")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError("Missing the required parameter 'database_key' when calling 'delete_discrete_value'")
        # verify the required parameter "discrete_type_guid" is set
        if "discrete_type_guid" not in params or params["discrete_type_guid"] is None:
            raise ValueError("Missing the required parameter 'discrete_type_guid' when calling 'delete_discrete_value'")
        # verify the required parameter "discrete_value_guid" is set
        if "discrete_value_guid" not in params or params["discrete_value_guid"] is None:
            raise ValueError("Missing the required parameter 'discrete_value_guid' when calling 'delete_discrete_value'")

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "discrete_type_guid" in params and discrete_type_guid is not None:
            path_params["discrete-type-guid"] = params["discrete_type_guid"]
        if "discrete_value_guid" in params and discrete_value_guid is not None:
            path_params["discrete-value-guid"] = params["discrete_value_guid"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])


        response_type_map: dict[int, Optional[str]] = {
            400: "GsaDiscreteValueAggregateException",
            200: None,
            403: None,
            404: None,
        }
        
        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/discrete-types/{discrete-type-guid}/discrete-values/{discrete-value-guid}", "DELETE",
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

    def find_unused_discrete_values(self, *, database_key: "str", discrete_type_guid: "str") -> "Union[GsaDiscreteValuesDiscreteValuesInfo, None]":
        """Find discrete values that are not in use by any data

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        discrete_type_guid: str

        Returns
        -------
        Union[GsaDiscreteValuesDiscreteValuesInfo, None]
        """
        data = self._find_unused_discrete_values_with_http_info(database_key, discrete_type_guid, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _find_unused_discrete_values_with_http_info(self, database_key: "str", discrete_type_guid: "str", **kwargs: Any) -> Any:
        all_params = ["database_key", "discrete_type_guid", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method find_unused_discrete_values")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError("Missing the required parameter 'database_key' when calling 'find_unused_discrete_values'")
        # verify the required parameter "discrete_type_guid" is set
        if "discrete_type_guid" not in params or params["discrete_type_guid"] is None:
            raise ValueError("Missing the required parameter 'discrete_type_guid' when calling 'find_unused_discrete_values'")

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "discrete_type_guid" in params and discrete_type_guid is not None:
            path_params["discrete-type-guid"] = params["discrete_type_guid"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])


        response_type_map: dict[int, Optional[str]] = {
            200: "GsaDiscreteValuesDiscreteValuesInfo",
            400: None,
            404: None,
        }
        
        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/discrete-types/{discrete-type-guid}/discrete-values:find-unused", "GET",
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

    def get_discrete_value(self, *, database_key: "str", discrete_type_guid: "str", discrete_value_guid: "str") -> "Union[GsaDiscreteValuesDiscreteValue, None]":
        """Gets specific discrete value for a given discreteType within a given database.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        discrete_type_guid: str
        discrete_value_guid: str

        Returns
        -------
        Union[GsaDiscreteValuesDiscreteValue, None]
        """
        data = self._get_discrete_value_with_http_info(database_key, discrete_type_guid, discrete_value_guid, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _get_discrete_value_with_http_info(self, database_key: "str", discrete_type_guid: "str", discrete_value_guid: "str", **kwargs: Any) -> Any:
        all_params = ["database_key", "discrete_type_guid", "discrete_value_guid", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method get_discrete_value")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError("Missing the required parameter 'database_key' when calling 'get_discrete_value'")
        # verify the required parameter "discrete_type_guid" is set
        if "discrete_type_guid" not in params or params["discrete_type_guid"] is None:
            raise ValueError("Missing the required parameter 'discrete_type_guid' when calling 'get_discrete_value'")
        # verify the required parameter "discrete_value_guid" is set
        if "discrete_value_guid" not in params or params["discrete_value_guid"] is None:
            raise ValueError("Missing the required parameter 'discrete_value_guid' when calling 'get_discrete_value'")

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "discrete_type_guid" in params and discrete_type_guid is not None:
            path_params["discrete-type-guid"] = params["discrete_type_guid"]
        if "discrete_value_guid" in params and discrete_value_guid is not None:
            path_params["discrete-value-guid"] = params["discrete_value_guid"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])


        response_type_map: dict[int, Optional[str]] = {
            200: "GsaDiscreteValuesDiscreteValue",
            404: None,
        }
        
        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/discrete-types/{discrete-type-guid}/discrete-values/{discrete-value-guid}", "GET",
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

    def get_discrete_values(self, *, database_key: "str", discrete_type_guid: "str") -> "Union[GsaDiscreteValuesDiscreteValuesInfo, None]":
        """Gets all discrete values for a given discreteType, returned in order.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        discrete_type_guid: str

        Returns
        -------
        Union[GsaDiscreteValuesDiscreteValuesInfo, None]
        """
        data = self._get_discrete_values_with_http_info(database_key, discrete_type_guid, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _get_discrete_values_with_http_info(self, database_key: "str", discrete_type_guid: "str", **kwargs: Any) -> Any:
        all_params = ["database_key", "discrete_type_guid", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method get_discrete_values")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError("Missing the required parameter 'database_key' when calling 'get_discrete_values'")
        # verify the required parameter "discrete_type_guid" is set
        if "discrete_type_guid" not in params or params["discrete_type_guid"] is None:
            raise ValueError("Missing the required parameter 'discrete_type_guid' when calling 'get_discrete_values'")

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "discrete_type_guid" in params and discrete_type_guid is not None:
            path_params["discrete-type-guid"] = params["discrete_type_guid"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])


        response_type_map: dict[int, Optional[str]] = {
            200: "GsaDiscreteValuesDiscreteValuesInfo",
            404: None,
        }
        
        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/discrete-types/{discrete-type-guid}/discrete-values", "GET",
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

    def replace_discrete_values(self, *, database_key: "str", discrete_type_guid: "str", body: "Optional[GsaDiscreteValuesReplaceDiscreteValuesInfo]" = None) -> "Union[GsaDiscreteValuesDiscreteValuesInfo, None]":
        """Replace the whole discrete value collection for a given discrete type.  This will result in adding, modifying, deleting and reordering discrete values. If any of those operations fail, the whole operation fails.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        discrete_type_guid: str
        body: GsaDiscreteValuesReplaceDiscreteValuesInfo

        Returns
        -------
        Union[GsaDiscreteValuesDiscreteValuesInfo, None]
        """
        data = self._replace_discrete_values_with_http_info(database_key, discrete_type_guid, body, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _replace_discrete_values_with_http_info(self, database_key: "str", discrete_type_guid: "str", body: "Optional[GsaDiscreteValuesReplaceDiscreteValuesInfo]" = None, **kwargs: Any) -> Any:
        all_params = ["database_key", "discrete_type_guid", "body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method replace_discrete_values")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError("Missing the required parameter 'database_key' when calling 'replace_discrete_values'")
        # verify the required parameter "discrete_type_guid" is set
        if "discrete_type_guid" not in params or params["discrete_type_guid"] is None:
            raise ValueError("Missing the required parameter 'discrete_type_guid' when calling 'replace_discrete_values'")

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "discrete_type_guid" in params and discrete_type_guid is not None:
            path_params["discrete-type-guid"] = params["discrete_type_guid"]

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
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json-patch+json", "application/json", "text/json", "application/*+json"])

        response_type_map: dict[int, Optional[str]] = {
            200: "GsaDiscreteValuesDiscreteValuesInfo",
            400: None,
            403: None,
            404: None,
        }
        
        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/discrete-types/{discrete-type-guid}/discrete-values", "PUT",
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

    def update_discrete_value(self, *, database_key: "str", discrete_type_guid: "str", discrete_value_guid: "str", body: "Optional[GsaDiscreteValuesUpdateDiscreteValue]" = None) -> "Union[GsaDiscreteValuesDiscreteValue, None]":
        """Update discrete value.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        discrete_type_guid: str
        discrete_value_guid: str
        body: GsaDiscreteValuesUpdateDiscreteValue

        Returns
        -------
        Union[GsaDiscreteValuesDiscreteValue, None]
        """
        data = self._update_discrete_value_with_http_info(database_key, discrete_type_guid, discrete_value_guid, body, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _update_discrete_value_with_http_info(self, database_key: "str", discrete_type_guid: "str", discrete_value_guid: "str", body: "Optional[GsaDiscreteValuesUpdateDiscreteValue]" = None, **kwargs: Any) -> Any:
        all_params = ["database_key", "discrete_type_guid", "discrete_value_guid", "body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method update_discrete_value")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError("Missing the required parameter 'database_key' when calling 'update_discrete_value'")
        # verify the required parameter "discrete_type_guid" is set
        if "discrete_type_guid" not in params or params["discrete_type_guid"] is None:
            raise ValueError("Missing the required parameter 'discrete_type_guid' when calling 'update_discrete_value'")
        # verify the required parameter "discrete_value_guid" is set
        if "discrete_value_guid" not in params or params["discrete_value_guid"] is None:
            raise ValueError("Missing the required parameter 'discrete_value_guid' when calling 'update_discrete_value'")

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "discrete_type_guid" in params and discrete_type_guid is not None:
            path_params["discrete-type-guid"] = params["discrete_type_guid"]
        if "discrete_value_guid" in params and discrete_value_guid is not None:
            path_params["discrete-value-guid"] = params["discrete_value_guid"]

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
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json-patch+json", "application/json", "text/json", "application/*+json"])

        response_type_map: dict[int, Optional[str]] = {
            200: "GsaDiscreteValuesDiscreteValue",
            400: None,
            403: None,
            404: None,
        }
        
        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/discrete-types/{discrete-type-guid}/discrete-values/{discrete-value-guid}", "PATCH",
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
