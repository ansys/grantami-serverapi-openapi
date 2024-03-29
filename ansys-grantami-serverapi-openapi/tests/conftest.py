# coding: utf-8

"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pytest
import requests_mock
import ansys.openapi.common as auth
import ansys.grantami.serverapi_openapi.models as models


@pytest.fixture(scope="session")
def api_client():
    test_url = "/"
    with requests_mock.Mocker() as m:
        m.get(test_url, status_code=200)
        api_client = auth.ApiClientFactory(test_url).with_anonymous().connect()
        api_client.setup_client(models)
    return api_client
