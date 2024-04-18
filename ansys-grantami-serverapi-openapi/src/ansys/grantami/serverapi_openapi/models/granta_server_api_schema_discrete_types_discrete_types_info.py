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


class GrantaServerApiSchemaDiscreteTypesDiscreteTypesInfo(ModelBase):
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
        "discrete_types": "list[GrantaServerApiSchemaDiscreteTypesDiscreteType]",
    }

    attribute_map: Dict[str, str] = {
        "discrete_types": "discreteTypes",
    }

    subtype_mapping: Dict[str, str] = {
        "discreteTypes": "GrantaServerApiSchemaDiscreteTypesDiscreteType",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        discrete_types: "Union[List[GrantaServerApiSchemaDiscreteTypesDiscreteType], None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaDiscreteTypesDiscreteTypesInfo - a model defined in Swagger

        Parameters
        ----------
        discrete_types: List[GrantaServerApiSchemaDiscreteTypesDiscreteType], optional
        """
        self._discrete_types: Union[
            List[GrantaServerApiSchemaDiscreteTypesDiscreteType], None, Unset_Type
        ] = Unset

        if discrete_types is not Unset:
            self.discrete_types = discrete_types

    @property
    def discrete_types(
        self,
    ) -> (
        "Union[List[GrantaServerApiSchemaDiscreteTypesDiscreteType], None, Unset_Type]"
    ):
        """Gets the discrete_types of this GrantaServerApiSchemaDiscreteTypesDiscreteTypesInfo.

        Returns
        -------
        Union[List[GrantaServerApiSchemaDiscreteTypesDiscreteType], None, Unset_Type]
            The discrete_types of this GrantaServerApiSchemaDiscreteTypesDiscreteTypesInfo.
        """
        return self._discrete_types

    @discrete_types.setter
    def discrete_types(
        self,
        discrete_types: "Union[List[GrantaServerApiSchemaDiscreteTypesDiscreteType], None, Unset_Type]",
    ) -> None:
        """Sets the discrete_types of this GrantaServerApiSchemaDiscreteTypesDiscreteTypesInfo.

        Parameters
        ----------
        discrete_types: Union[List[GrantaServerApiSchemaDiscreteTypesDiscreteType], None, Unset_Type]
            The discrete_types of this GrantaServerApiSchemaDiscreteTypesDiscreteTypesInfo.
        """
        self._discrete_types = discrete_types

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
        if not isinstance(other, GrantaServerApiSchemaDiscreteTypesDiscreteTypesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
