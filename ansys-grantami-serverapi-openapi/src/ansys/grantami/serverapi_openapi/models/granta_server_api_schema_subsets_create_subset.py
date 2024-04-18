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


class GrantaServerApiSchemaSubsetsCreateSubset(ModelBase):
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
        "name": "str",
        "associated_layout": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "guid": "str",
    }

    attribute_map: Dict[str, str] = {
        "name": "name",
        "associated_layout": "associatedLayout",
        "guid": "guid",
    }

    subtype_mapping: Dict[str, str] = {
        "associatedLayout": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        name: "str",
        associated_layout: "Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]" = Unset,
        guid: "Union[str, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaSubsetsCreateSubset - a model defined in Swagger

        Parameters
        ----------
        name: str
        associated_layout: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
        guid: str, optional
        """
        self._associated_layout: Union[
            GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type
        ] = Unset
        self._name: str
        self._guid: Union[str, Unset_Type] = Unset

        if associated_layout is not Unset:
            self.associated_layout = associated_layout
        self.name = name
        if guid is not Unset:
            self.guid = guid

    @property
    def associated_layout(
        self,
    ) -> "Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]":
        """Gets the associated_layout of this GrantaServerApiSchemaSubsetsCreateSubset.

        Returns
        -------
        Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]
            The associated_layout of this GrantaServerApiSchemaSubsetsCreateSubset.
        """
        return self._associated_layout

    @associated_layout.setter
    def associated_layout(
        self,
        associated_layout: "Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]",
    ) -> None:
        """Sets the associated_layout of this GrantaServerApiSchemaSubsetsCreateSubset.

        Parameters
        ----------
        associated_layout: Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]
            The associated_layout of this GrantaServerApiSchemaSubsetsCreateSubset.
        """
        # Field is not nullable
        if associated_layout is None:
            raise ValueError(
                "Invalid value for 'associated_layout', must not be 'None'"
            )
        self._associated_layout = associated_layout

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaSubsetsCreateSubset.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaSubsetsCreateSubset.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaSubsetsCreateSubset.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaSubsetsCreateSubset.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        # Field is required
        if name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'name', must not be 'Unset'")
        self._name = name

    @property
    def guid(self) -> "Union[str, Unset_Type]":
        """Gets the guid of this GrantaServerApiSchemaSubsetsCreateSubset.

        Returns
        -------
        Union[str, Unset_Type]
            The guid of this GrantaServerApiSchemaSubsetsCreateSubset.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, Unset_Type]") -> None:
        """Sets the guid of this GrantaServerApiSchemaSubsetsCreateSubset.

        Parameters
        ----------
        guid: Union[str, Unset_Type]
            The guid of this GrantaServerApiSchemaSubsetsCreateSubset.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        self._guid = guid

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
        if not isinstance(other, GrantaServerApiSchemaSubsetsCreateSubset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
