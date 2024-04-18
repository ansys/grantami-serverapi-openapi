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
    BinaryIO,
    Dict,
    List,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase, Unset, Unset_Type


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSelectionSearchesUserOrGroup(ModelBase):
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
    swagger_types: Dict[str, str] = {
        "display_name": "str",
        "identifier": "str",
        "name": "str",
    }

    attribute_map: Dict[str, str] = {
        "display_name": "displayName",
        "identifier": "identifier",
        "name": "name",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        display_name: "Union[str, None, Unset_Type]" = Unset,
        identifier: "Union[str, Unset_Type]" = Unset,
        name: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSelectionSearchesUserOrGroup - a model defined in Swagger

        Parameters
        ----------
        display_name: str, optional
        identifier: str, optional
        name: str, optional
        """
        self._identifier: Union[str, Unset_Type] = Unset
        self._display_name: Union[str, None, Unset_Type] = Unset
        self._name: Union[str, None, Unset_Type] = Unset

        if identifier is not Unset:
            self.identifier = identifier
        if display_name is not Unset:
            self.display_name = display_name
        if name is not Unset:
            self.name = name

    @property
    def identifier(self) -> "Union[str, Unset_Type]":
        """Gets the identifier of this GrantaServerApiSelectionSearchesUserOrGroup.

        Returns
        -------
        Union[str, Unset_Type]
            The identifier of this GrantaServerApiSelectionSearchesUserOrGroup.
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier: "Union[str, Unset_Type]") -> None:
        """Sets the identifier of this GrantaServerApiSelectionSearchesUserOrGroup.

        Parameters
        ----------
        identifier: Union[str, Unset_Type]
            The identifier of this GrantaServerApiSelectionSearchesUserOrGroup.
        """
        # Field is not nullable
        if identifier is None:
            raise ValueError("Invalid value for 'identifier', must not be 'None'")
        self._identifier = identifier

    @property
    def display_name(self) -> "Union[str, None, Unset_Type]":
        """Gets the display_name of this GrantaServerApiSelectionSearchesUserOrGroup.

        Returns
        -------
        Union[str, None, Unset_Type]
            The display_name of this GrantaServerApiSelectionSearchesUserOrGroup.
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: "Union[str, None, Unset_Type]") -> None:
        """Sets the display_name of this GrantaServerApiSelectionSearchesUserOrGroup.

        Parameters
        ----------
        display_name: Union[str, None, Unset_Type]
            The display_name of this GrantaServerApiSelectionSearchesUserOrGroup.
        """
        self._display_name = display_name

    @property
    def name(self) -> "Union[str, None, Unset_Type]":
        """Gets the name of this GrantaServerApiSelectionSearchesUserOrGroup.

        Returns
        -------
        Union[str, None, Unset_Type]
            The name of this GrantaServerApiSelectionSearchesUserOrGroup.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, None, Unset_Type]") -> None:
        """Sets the name of this GrantaServerApiSelectionSearchesUserOrGroup.

        Parameters
        ----------
        name: Union[str, None, Unset_Type]
            The name of this GrantaServerApiSelectionSearchesUserOrGroup.
        """
        self._name = name

    @classmethod
    def get_real_child_model(cls, data: Dict[str, str]) -> str:
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
        if not isinstance(other, GrantaServerApiSelectionSearchesUserOrGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
