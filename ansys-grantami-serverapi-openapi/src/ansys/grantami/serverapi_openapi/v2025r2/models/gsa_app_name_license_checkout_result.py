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

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaAppNameLicenseCheckoutResult(ModelBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes
    ----------
    swagger_types: dict[str, str]
        The key is attribute name and the value is attribute type.
    attribute_map: dict[str, str]
        The key is attribute name and the value is json key in definition.
    subtype_mapping: dict[str, str]
        The key is the unmangled property name and the value is the corresponding type.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "app_name": "str",
        "license_state_ok": "bool",
    }

    attribute_map: dict[str, str] = {
        "app_name": "appName",
        "license_state_ok": "licenseStateOk",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        app_name: "Union[str, None, Unset_Type]" = Unset,
        license_state_ok: "Union[bool, Unset_Type]" = Unset,
    ) -> None:
        """GsaAppNameLicenseCheckoutResult - a model defined in Swagger

        Parameters
        ----------
        app_name: str, optional
        license_state_ok: bool, optional
        """
        self._app_name: Union[str, None, Unset_Type] = Unset
        self._license_state_ok: Union[bool, Unset_Type] = Unset

        if app_name is not Unset:
            self.app_name = app_name
        if license_state_ok is not Unset:
            self.license_state_ok = license_state_ok

    @property
    def app_name(self) -> "Union[str, None, Unset_Type]":
        """Gets the app_name of this GsaAppNameLicenseCheckoutResult.

        Returns
        -------
        Union[str, None, Unset_Type]
            The app_name of this GsaAppNameLicenseCheckoutResult.
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name: "Union[str, None, Unset_Type]") -> None:
        """Sets the app_name of this GsaAppNameLicenseCheckoutResult.

        Parameters
        ----------
        app_name: Union[str, None, Unset_Type]
            The app_name of this GsaAppNameLicenseCheckoutResult.
        """
        self._app_name = app_name

    @property
    def license_state_ok(self) -> "Union[bool, Unset_Type]":
        """Gets the license_state_ok of this GsaAppNameLicenseCheckoutResult.

        Returns
        -------
        Union[bool, Unset_Type]
            The license_state_ok of this GsaAppNameLicenseCheckoutResult.
        """
        return self._license_state_ok

    @license_state_ok.setter
    def license_state_ok(self, license_state_ok: "Union[bool, Unset_Type]") -> None:
        """Sets the license_state_ok of this GsaAppNameLicenseCheckoutResult.

        Parameters
        ----------
        license_state_ok: Union[bool, Unset_Type]
            The license_state_ok of this GsaAppNameLicenseCheckoutResult.
        """
        # Field is not nullable
        if license_state_ok is None:
            raise ValueError("Invalid value for 'license_state_ok', must not be 'None'")
        self._license_state_ok = license_state_ok

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
        """Raises a NotImplementedError for a type without a discriminator defined.

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class

        Raises
        ------
        NotImplementedError
            This class has no discriminator, and hence no subclasses
        """
        raise NotImplementedError()

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GsaAppNameLicenseCheckoutResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
