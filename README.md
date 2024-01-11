# PyGranta Server API

[![PyAnsys](https://img.shields.io/badge/Py-Ansys-ffc107.svg?labelColor=black&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABDklEQVQ4jWNgoDfg5mD8vE7q/3bpVyskbW0sMRUwofHD7Dh5OBkZGBgW7/3W2tZpa2tLQEOyOzeEsfumlK2tbVpaGj4N6jIs1lpsDAwMJ278sveMY2BgCA0NFRISwqkhyQ1q/Nyd3zg4OBgYGNjZ2ePi4rB5loGBhZnhxTLJ/9ulv26Q4uVk1NXV/f///////69du4Zdg78lx//t0v+3S88rFISInD59GqIH2esIJ8G9O2/XVwhjzpw5EAam1xkkBJn/bJX+v1365hxxuCAfH9+3b9/+////48cPuNehNsS7cDEzMTAwMMzb+Q2u4dOnT2vWrMHu9ZtzxP9vl/69RVpCkBlZ3N7enoDXBwEAAA+YYitOilMVAAAAAElFTkSuQmCC)](https://docs.pyansys.com/)
[![python](https://img.shields.io/pypi/pyversions/ansys-grantami-serverapi-openapi?logo=pypi)](https://pypi.org/project/ansys-grantami-serverapi-openapi/)
[![pypi](https://img.shields.io/pypi/v/ansys-grantami-serverapi-openapi.svg?logo=python&logoColor=white)](https://pypi.org/project/ansys-grantami-serverapi-openapi/)
[![GH-CI](https://github.com/pyansys/grantami-serverapi-openapi/actions/workflows/build_and_test_library.yml/badge.svg)](https://github.com/pyansys/grantami-serverapi-openapi/actions/workflows/build_and_test_library.yml)
[![MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Project Overview

Autogenerated client library for the Granta MI Server API Services. Direct use
of this package is unsupported. Use [ansys-grantami-recordlists](https://github.com/pyansys/grantami-recordlists)
instead.

Commits should generally only be made to this repository to update the OpenAPI
YAML definition (stored in ``yaml/``). Changes to the Python code will be made
automatically when the YAML is modified.


## Contributing

This repository is not under active development. It is only for storing the code generated from the API
definition. All development is done in the following repositories:

- [ansys-grantami-recordlists](https://github.com/pyansys/grantami-recordlists)


## Releasing

This package follows [Semantic Versioning](https://semver.org/). Release candidates are versioned as ``MAJOR.MINOR.0rc<ITERATION>``.

The release process follows the standard [PyAnsys release guidelines](https://dev.docs.pyansys.com/how-to/releasing.html).

1. Ensure the ``main`` branch build status is green, which indicates that the most recent run of the ``CI`` workflow was successful.
2. Create a new branch from the ``main`` branch with the name ``release/MAJOR.MINOR`` and push the branch to GitHub.
3. Do one of the following two steps to generate a 'release' `pyproject.toml` file:
   * To change the version number, modify the ``<version>`` XML element in the ``pom.xml`` file and open a Pull Request.
   * If the version number is correct, manually run the 'Generate client library' GitHub action on the release branch.
5. Pull the branch and check that the most recent commit includes the 'release' `pyproject.toml` file.
4. Tag the release:
   ```console
   git tag v<MAJOR.MINOR.0rc0>
   git push origin --tags
   ```

Once the tag is pushed to GitHub, a workflow will build and publish the release.


## Using this package directly

As stated above, direct use of this package is unsupported. The recommended approach is to use the idiomatic
libraries written for specific API areas.

We do understand that internal or external users might want to experiment with Granta MI Server API functionality that 
is not exposed via an idiomatic python library. To that extent, the following sections demonstrate how to install and
get started with the library.

### Requirements
The `ansys-grantami-serverapi-openapi` package requires Granta MI. The following table details compatibility between 
Granta MI releases and versions of the Python package.

| Granta MI | ansys-grantami-serverapi-openapi |
|-----------|----------------------------------|
| 2024R1    | v2.0.0                           |
| 2023R2    | v1.0.0                           |



### Installation

During active development phases of Granta MI, this repository is kept up to date with new versions of the API 
documentation. To use the most up-to-date version of this package in another project, add a dependency on the 
repository's main branch, e.g. with poetry:

```console
   poetry add git+https://github.com/pyansys/grantami-serverapi-openapi#subdirectory=ansys-grantami-serverapi-openapi
```

Or with pip:

```console
   pip install git+https://github.com/pyansys/grantami-serverapi-openapi.git#subdirectory=ansys-grantami-serverapi-openapi
```

### Minimal setup
The following code snippet demonstrates how to perform the minimal setup required to interact with the API using this 
library.

```python
from typing import Optional
from importlib.metadata import version

from ansys.openapi.common import (
    ApiClientFactory,
    ApiClient,
    generate_user_agent,
    SessionConfiguration,
)
from ansys.grantami.serverapi_openapi import models

SERVICE_PATH = "/proxy/v1.svc"
MI_AUTH_PATH = "/v1alpha/schema/mi-version"
GRANTA_APPLICATION_NAME_HEADER = "PyGranta ServerAPI"


class Connection(ApiClientFactory):
    def __init__(self, api_url: str, session_configuration: Optional[SessionConfiguration] = None) -> None:
        package_name = "ansys-grantami-serverapi-openapi"
        ver = version(package_name)

        self._full_api_url = api_url.strip("/") + SERVICE_PATH
        auth_url = self._full_api_url + MI_AUTH_PATH

        super().__init__(auth_url, session_configuration)
        session_configuration = self._session_configuration
        session_configuration.headers["X-Granta-ApplicationName"] = GRANTA_APPLICATION_NAME_HEADER
        session_configuration.headers["User-Agent"] = generate_user_agent(package_name, ver)

    def connect(self) -> ApiClient:
        self._validate_builder()
        client = ApiClient(
            session=self._session,
            api_url=self._full_api_url,
            configuration=self._session_configuration,
        )
        client.setup_client(models)
        return client


if __name__ == '__main__':
    from ansys.grantami.serverapi_openapi import api
    
    # Update URL and connection method for your system
    URL = "http://my_server_name/mi_servicelayer"
    api_client = Connection(api_url=URL).with_autologon().connect()
    
    schema_api = api.SchemaApi(api_client)
    server_version = schema_api.v1alpha_schema_mi_version_get()
    print(server_version.version)
```
