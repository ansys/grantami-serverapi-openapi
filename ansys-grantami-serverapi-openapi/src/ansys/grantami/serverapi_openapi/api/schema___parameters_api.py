# coding: utf-8

"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from . import ApiBase


class SchemaParametersApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def v1alpha_databases_database_key_parameters_get(self, database_key, **kwargs):  # noqa: E501
        """Get all parameters for a given database.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :return: GrantaServerApiSchemaParametersParametersInfo
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_databases_database_key_parameters_get_with_http_info(database_key, **kwargs)  # noqa: E501
        return data

    def v1alpha_databases_database_key_parameters_get_with_http_info(self, database_key, **kwargs):  # noqa: E501
        """Get all parameters for a given database.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :return: GrantaServerApiSchemaParametersParametersInfo
        """

        all_params = ['database_key']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_databases_database_key_parameters_get".format(key)
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_key' is set
        if ('database_key' not in params or
                params['database_key'] is None):
            raise ValueError("Missing the required parameter `database_key` when calling `v1alpha_databases_database_key_parameters_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_key' in params:
            path_params['database-key'] = params['database_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/databases/{database-key}/parameters', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GrantaServerApiSchemaParametersParametersInfo',  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1alpha_databases_database_key_parameters_parameter_guid_delete(self, database_key, parameter_guid, **kwargs):  # noqa: E501
        """Delete a parameter.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str parameter_guid: (required)
        :return: None
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_databases_database_key_parameters_parameter_guid_delete_with_http_info(database_key, parameter_guid, **kwargs)  # noqa: E501
        return data

    def v1alpha_databases_database_key_parameters_parameter_guid_delete_with_http_info(self, database_key, parameter_guid, **kwargs):  # noqa: E501
        """Delete a parameter.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str parameter_guid: (required)
        :return: None
        """

        all_params = ['database_key', 'parameter_guid']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_databases_database_key_parameters_parameter_guid_delete".format(key)
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_key' is set
        if ('database_key' not in params or
                params['database_key'] is None):
            raise ValueError("Missing the required parameter `database_key` when calling `v1alpha_databases_database_key_parameters_parameter_guid_delete`")  # noqa: E501
        # verify the required parameter 'parameter_guid' is set
        if ('parameter_guid' not in params or
                params['parameter_guid'] is None):
            raise ValueError("Missing the required parameter `parameter_guid` when calling `v1alpha_databases_database_key_parameters_parameter_guid_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_key' in params:
            path_params['database-key'] = params['database_key']  # noqa: E501
        if 'parameter_guid' in params:
            path_params['parameter-guid'] = params['parameter_guid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/databases/{database-key}/parameters/{parameter-guid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1alpha_databases_database_key_parameters_parameter_guid_get(self, database_key, parameter_guid, **kwargs):  # noqa: E501
        """Get a parameter with a specified guid for a given database.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str parameter_guid: (required)
        :return: GrantaServerApiSchemaParametersParameter
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_databases_database_key_parameters_parameter_guid_get_with_http_info(database_key, parameter_guid, **kwargs)  # noqa: E501
        return data

    def v1alpha_databases_database_key_parameters_parameter_guid_get_with_http_info(self, database_key, parameter_guid, **kwargs):  # noqa: E501
        """Get a parameter with a specified guid for a given database.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str parameter_guid: (required)
        :return: GrantaServerApiSchemaParametersParameter
        """

        all_params = ['database_key', 'parameter_guid']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_databases_database_key_parameters_parameter_guid_get".format(key)
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_key' is set
        if ('database_key' not in params or
                params['database_key'] is None):
            raise ValueError("Missing the required parameter `database_key` when calling `v1alpha_databases_database_key_parameters_parameter_guid_get`")  # noqa: E501
        # verify the required parameter 'parameter_guid' is set
        if ('parameter_guid' not in params or
                params['parameter_guid'] is None):
            raise ValueError("Missing the required parameter `parameter_guid` when calling `v1alpha_databases_database_key_parameters_parameter_guid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_key' in params:
            path_params['database-key'] = params['database_key']  # noqa: E501
        if 'parameter_guid' in params:
            path_params['parameter-guid'] = params['parameter_guid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/databases/{database-key}/parameters/{parameter-guid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GrantaServerApiSchemaParametersParameter',  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_parameter_value_guid_delete(self, database_key, parameter_guid, parameter_value_guid, **kwargs):  # noqa: E501
        """Delete a parameter value.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str parameter_guid: (required)
        :param str parameter_value_guid: (required)
        :return: None
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_parameter_value_guid_delete_with_http_info(database_key, parameter_guid, parameter_value_guid, **kwargs)  # noqa: E501
        return data

    def v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_parameter_value_guid_delete_with_http_info(self, database_key, parameter_guid, parameter_value_guid, **kwargs):  # noqa: E501
        """Delete a parameter value.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str parameter_guid: (required)
        :param str parameter_value_guid: (required)
        :return: None
        """

        all_params = ['database_key', 'parameter_guid', 'parameter_value_guid']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_parameter_value_guid_delete".format(key)
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_key' is set
        if ('database_key' not in params or
                params['database_key'] is None):
            raise ValueError("Missing the required parameter `database_key` when calling `v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_parameter_value_guid_delete`")  # noqa: E501
        # verify the required parameter 'parameter_guid' is set
        if ('parameter_guid' not in params or
                params['parameter_guid'] is None):
            raise ValueError("Missing the required parameter `parameter_guid` when calling `v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_parameter_value_guid_delete`")  # noqa: E501
        # verify the required parameter 'parameter_value_guid' is set
        if ('parameter_value_guid' not in params or
                params['parameter_value_guid'] is None):
            raise ValueError("Missing the required parameter `parameter_value_guid` when calling `v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_parameter_value_guid_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_key' in params:
            path_params['database-key'] = params['database_key']  # noqa: E501
        if 'parameter_guid' in params:
            path_params['parameter-guid'] = params['parameter_guid']  # noqa: E501
        if 'parameter_value_guid' in params:
            path_params['parameter-value-guid'] = params['parameter_value_guid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/databases/{database-key}/parameters/{parameter-guid}/parameter-values/{parameter-value-guid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_parameter_value_guid_patch(self, database_key, parameter_guid, parameter_value_guid, **kwargs):  # noqa: E501
        """Update a parameter value.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str parameter_guid: (required)
        :param str parameter_value_guid: (required)
        :param GrantaServerApiSchemaParametersParameterValue body:
        :return: GrantaServerApiSchemaParametersParameterValue
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_parameter_value_guid_patch_with_http_info(database_key, parameter_guid, parameter_value_guid, **kwargs)  # noqa: E501
        return data

    def v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_parameter_value_guid_patch_with_http_info(self, database_key, parameter_guid, parameter_value_guid, **kwargs):  # noqa: E501
        """Update a parameter value.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str parameter_guid: (required)
        :param str parameter_value_guid: (required)
        :param GrantaServerApiSchemaParametersParameterValue body:
        :return: GrantaServerApiSchemaParametersParameterValue
        """

        all_params = ['database_key', 'parameter_guid', 'parameter_value_guid', 'body']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_parameter_value_guid_patch".format(key)
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_key' is set
        if ('database_key' not in params or
                params['database_key'] is None):
            raise ValueError("Missing the required parameter `database_key` when calling `v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_parameter_value_guid_patch`")  # noqa: E501
        # verify the required parameter 'parameter_guid' is set
        if ('parameter_guid' not in params or
                params['parameter_guid'] is None):
            raise ValueError("Missing the required parameter `parameter_guid` when calling `v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_parameter_value_guid_patch`")  # noqa: E501
        # verify the required parameter 'parameter_value_guid' is set
        if ('parameter_value_guid' not in params or
                params['parameter_value_guid'] is None):
            raise ValueError("Missing the required parameter `parameter_value_guid` when calling `v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_parameter_value_guid_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_key' in params:
            path_params['database-key'] = params['database_key']  # noqa: E501
        if 'parameter_guid' in params:
            path_params['parameter-guid'] = params['parameter_guid']  # noqa: E501
        if 'parameter_value_guid' in params:
            path_params['parameter-value-guid'] = params['parameter_value_guid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/databases/{database-key}/parameters/{parameter-guid}/parameter-values/{parameter-value-guid}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GrantaServerApiSchemaParametersParameterValue',  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_post(self, database_key, parameter_guid, **kwargs):  # noqa: E501
        """Create a new parameter value.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str parameter_guid: (required)
        :param GrantaServerApiSchemaParametersParameterValue body:
        :return: None
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_post_with_http_info(database_key, parameter_guid, **kwargs)  # noqa: E501
        return data

    def v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_post_with_http_info(self, database_key, parameter_guid, **kwargs):  # noqa: E501
        """Create a new parameter value.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str parameter_guid: (required)
        :param GrantaServerApiSchemaParametersParameterValue body:
        :return: None
        """

        all_params = ['database_key', 'parameter_guid', 'body']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_post".format(key)
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_key' is set
        if ('database_key' not in params or
                params['database_key'] is None):
            raise ValueError("Missing the required parameter `database_key` when calling `v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_post`")  # noqa: E501
        # verify the required parameter 'parameter_guid' is set
        if ('parameter_guid' not in params or
                params['parameter_guid'] is None):
            raise ValueError("Missing the required parameter `parameter_guid` when calling `v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_key' in params:
            path_params['database-key'] = params['database_key']  # noqa: E501
        if 'parameter_guid' in params:
            path_params['parameter-guid'] = params['parameter_guid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/databases/{database-key}/parameters/{parameter-guid}/parameter-values', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_put(self, database_key, parameter_guid, **kwargs):  # noqa: E501
        """Replace the whole parameter value collection for a given parameter.  This will result in adding, modifying and deleting parameter values. If any of those operations fail, the whole operation fails.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str parameter_guid: (required)
        :param GrantaServerApiSchemaParametersParameterValuesInfo body:
        :return: GrantaServerApiSchemaParametersParameterValuesInfo
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_put_with_http_info(database_key, parameter_guid, **kwargs)  # noqa: E501
        return data

    def v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_put_with_http_info(self, database_key, parameter_guid, **kwargs):  # noqa: E501
        """Replace the whole parameter value collection for a given parameter.  This will result in adding, modifying and deleting parameter values. If any of those operations fail, the whole operation fails.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str parameter_guid: (required)
        :param GrantaServerApiSchemaParametersParameterValuesInfo body:
        :return: GrantaServerApiSchemaParametersParameterValuesInfo
        """

        all_params = ['database_key', 'parameter_guid', 'body']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_put".format(key)
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_key' is set
        if ('database_key' not in params or
                params['database_key'] is None):
            raise ValueError("Missing the required parameter `database_key` when calling `v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_put`")  # noqa: E501
        # verify the required parameter 'parameter_guid' is set
        if ('parameter_guid' not in params or
                params['parameter_guid'] is None):
            raise ValueError("Missing the required parameter `parameter_guid` when calling `v1alpha_databases_database_key_parameters_parameter_guid_parameter_values_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_key' in params:
            path_params['database-key'] = params['database_key']  # noqa: E501
        if 'parameter_guid' in params:
            path_params['parameter-guid'] = params['parameter_guid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/databases/{database-key}/parameters/{parameter-guid}/parameter-values', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GrantaServerApiSchemaParametersParameterValuesInfo',  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1alpha_databases_database_key_parameters_parameter_guid_patch(self, database_key, parameter_guid, **kwargs):  # noqa: E501
        """Update a parameter.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str parameter_guid: (required)
        :param GrantaServerApiSchemaParametersParameter body:
        :return: GrantaServerApiSchemaParametersParameter
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_databases_database_key_parameters_parameter_guid_patch_with_http_info(database_key, parameter_guid, **kwargs)  # noqa: E501
        return data

    def v1alpha_databases_database_key_parameters_parameter_guid_patch_with_http_info(self, database_key, parameter_guid, **kwargs):  # noqa: E501
        """Update a parameter.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str parameter_guid: (required)
        :param GrantaServerApiSchemaParametersParameter body:
        :return: GrantaServerApiSchemaParametersParameter
        """

        all_params = ['database_key', 'parameter_guid', 'body']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_databases_database_key_parameters_parameter_guid_patch".format(key)
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_key' is set
        if ('database_key' not in params or
                params['database_key'] is None):
            raise ValueError("Missing the required parameter `database_key` when calling `v1alpha_databases_database_key_parameters_parameter_guid_patch`")  # noqa: E501
        # verify the required parameter 'parameter_guid' is set
        if ('parameter_guid' not in params or
                params['parameter_guid'] is None):
            raise ValueError("Missing the required parameter `parameter_guid` when calling `v1alpha_databases_database_key_parameters_parameter_guid_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_key' in params:
            path_params['database-key'] = params['database_key']  # noqa: E501
        if 'parameter_guid' in params:
            path_params['parameter-guid'] = params['parameter_guid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/databases/{database-key}/parameters/{parameter-guid}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GrantaServerApiSchemaParametersParameter',  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1alpha_databases_database_key_parameters_parameter_guidusages_get(self, database_key, parameter_guid, **kwargs):  # noqa: E501
        """Get attributes which currently use the given parameter.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str parameter_guid: (required)
        :return: GrantaServerApiSchemaSlimEntitiesSlimObjects
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_databases_database_key_parameters_parameter_guidusages_get_with_http_info(database_key, parameter_guid, **kwargs)  # noqa: E501
        return data

    def v1alpha_databases_database_key_parameters_parameter_guidusages_get_with_http_info(self, database_key, parameter_guid, **kwargs):  # noqa: E501
        """Get attributes which currently use the given parameter.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str parameter_guid: (required)
        :return: GrantaServerApiSchemaSlimEntitiesSlimObjects
        """

        all_params = ['database_key', 'parameter_guid']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_databases_database_key_parameters_parameter_guidusages_get".format(key)
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_key' is set
        if ('database_key' not in params or
                params['database_key'] is None):
            raise ValueError("Missing the required parameter `database_key` when calling `v1alpha_databases_database_key_parameters_parameter_guidusages_get`")  # noqa: E501
        # verify the required parameter 'parameter_guid' is set
        if ('parameter_guid' not in params or
                params['parameter_guid'] is None):
            raise ValueError("Missing the required parameter `parameter_guid` when calling `v1alpha_databases_database_key_parameters_parameter_guidusages_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_key' in params:
            path_params['database-key'] = params['database_key']  # noqa: E501
        if 'parameter_guid' in params:
            path_params['parameter-guid'] = params['parameter_guid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/databases/{database-key}/parameters/{parameter-guid}:usages', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GrantaServerApiSchemaSlimEntitiesSlimObjects',  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1alpha_databases_database_key_parameters_post(self, database_key, **kwargs):  # noqa: E501
        """Create a new parameter.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param GrantaServerApiSchemaParametersParameter body:
        :return: None
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_databases_database_key_parameters_post_with_http_info(database_key, **kwargs)  # noqa: E501
        return data

    def v1alpha_databases_database_key_parameters_post_with_http_info(self, database_key, **kwargs):  # noqa: E501
        """Create a new parameter.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param GrantaServerApiSchemaParametersParameter body:
        :return: None
        """

        all_params = ['database_key', 'body']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_databases_database_key_parameters_post".format(key)
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_key' is set
        if ('database_key' not in params or
                params['database_key'] is None):
            raise ValueError("Missing the required parameter `database_key` when calling `v1alpha_databases_database_key_parameters_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_key' in params:
            path_params['database-key'] = params['database_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/databases/{database-key}/parameters', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
