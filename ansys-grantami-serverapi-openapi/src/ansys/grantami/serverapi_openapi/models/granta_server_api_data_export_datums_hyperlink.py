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


class GrantaServerApiDataExportDatumsHyperlink(ModelBase):
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

    """
    swagger_types = {
        "address": "str",
        "description": "str",
        "formatted_address": "str",
    }

    attribute_map = {
        "address": "address",
        "description": "description",
        "formatted_address": "formattedAddress",
    }

    subtype_mapping = {}

    def __init__(
        self,
        *,
        address: "Optional[str]" = None,
        description: "Optional[str]" = None,
        formatted_address: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiDataExportDatumsHyperlink - a model defined in Swagger

        Parameters
        ----------
            address: str, optional
            description: str, optional
            formatted_address: str, optional
        """
        self._address = None
        self._formatted_address = None
        self._description = None
        self.discriminator = None
        if address is not None:
            self.address = address
        if formatted_address is not None:
            self.formatted_address = formatted_address
        if description is not None:
            self.description = description

    @property
    def address(self) -> "str":
        """Gets the address of this GrantaServerApiDataExportDatumsHyperlink.

        Returns
        -------
        str
            The address of this GrantaServerApiDataExportDatumsHyperlink.
        """
        return self._address

    @address.setter
    def address(self, address: "str") -> None:
        """Sets the address of this GrantaServerApiDataExportDatumsHyperlink.

        Parameters
        ----------
        address: str
            The address of this GrantaServerApiDataExportDatumsHyperlink.
        """
        self._address = address

    @property
    def formatted_address(self) -> "str":
        """Gets the formatted_address of this GrantaServerApiDataExportDatumsHyperlink.

        Returns
        -------
        str
            The formatted_address of this GrantaServerApiDataExportDatumsHyperlink.
        """
        return self._formatted_address

    @formatted_address.setter
    def formatted_address(self, formatted_address: "str") -> None:
        """Sets the formatted_address of this GrantaServerApiDataExportDatumsHyperlink.

        Parameters
        ----------
        formatted_address: str
            The formatted_address of this GrantaServerApiDataExportDatumsHyperlink.
        """
        self._formatted_address = formatted_address

    @property
    def description(self) -> "str":
        """Gets the description of this GrantaServerApiDataExportDatumsHyperlink.

        Returns
        -------
        str
            The description of this GrantaServerApiDataExportDatumsHyperlink.
        """
        return self._description

    @description.setter
    def description(self, description: "str") -> None:
        """Sets the description of this GrantaServerApiDataExportDatumsHyperlink.

        Parameters
        ----------
        description: str
            The description of this GrantaServerApiDataExportDatumsHyperlink.
        """
        self._description = description

    def get_real_child_model(self, data: ModelBase) -> str:
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
        if issubclass(GrantaServerApiDataExportDatumsHyperlink, dict):
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
        if not isinstance(other, GrantaServerApiDataExportDatumsHyperlink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
