"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase


if TYPE_CHECKING:
    from . import *


class GrantaServerApiAppNameLicenseCheckoutResult(ModelBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes
    ----------
    swagger_types: Dict[str, str]
        The key is attribute name and the value is attribute type.
    attribute_map: Dict[str, str]
        The key is attribute name and the value is json key in definition.
    subtype_mapping: Dict[str, str]
        The key is the unmangled property name and the value is the corresponding type.

    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types = {
        "app_name": "str",
        "license_state_ok": "bool",
    }

    attribute_map = {
        "app_name": "appName",
        "license_state_ok": "licenseStateOk",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        app_name: "Optional[str]" = None,
        license_state_ok: "Optional[bool]" = None,
    ) -> None:
        """GrantaServerApiAppNameLicenseCheckoutResult - a model defined in Swagger

        Parameters
        ----------
            app_name: str, optional
            license_state_ok: bool, optional
        """
        self._app_name = None
        self._license_state_ok = None

        if app_name is not None:
            self.app_name = app_name
        if license_state_ok is not None:
            self.license_state_ok = license_state_ok

    @property
    def app_name(self) -> "str":
        """Gets the app_name of this GrantaServerApiAppNameLicenseCheckoutResult.

        Returns
        -------
        str
            The app_name of this GrantaServerApiAppNameLicenseCheckoutResult.
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name: "str") -> None:
        """Sets the app_name of this GrantaServerApiAppNameLicenseCheckoutResult.

        Parameters
        ----------
        app_name: str
            The app_name of this GrantaServerApiAppNameLicenseCheckoutResult.
        """
        self._app_name = app_name

    @property
    def license_state_ok(self) -> "bool":
        """Gets the license_state_ok of this GrantaServerApiAppNameLicenseCheckoutResult.

        Returns
        -------
        bool
            The license_state_ok of this GrantaServerApiAppNameLicenseCheckoutResult.
        """
        return self._license_state_ok

    @license_state_ok.setter
    def license_state_ok(self, license_state_ok: "bool") -> None:
        """Sets the license_state_ok of this GrantaServerApiAppNameLicenseCheckoutResult.

        Parameters
        ----------
        license_state_ok: bool
            The license_state_ok of this GrantaServerApiAppNameLicenseCheckoutResult.
        """
        self._license_state_ok = license_state_ok

    @classmethod
    def get_real_child_model(cls, data: ModelBase) -> str:
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

    def to_dict(self) -> Dict:
        """Returns the model properties as a dict

        Returns
        -------
        Dict
            Dictionary indexed by property name containing all the model properties
        """
        result = {}

        for attr in self.swagger_types.keys():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(GrantaServerApiAppNameLicenseCheckoutResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model

        Returns
        -------
        str
            String representation of the model as a dictionary
        """
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiAppNameLicenseCheckoutResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other