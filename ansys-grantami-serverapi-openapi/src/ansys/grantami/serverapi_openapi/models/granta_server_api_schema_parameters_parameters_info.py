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


class GrantaServerApiSchemaParametersParametersInfo(ModelBase):
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
        "parameters": "list[GrantaServerApiSchemaParametersParameter]",
    }

    attribute_map: Dict[str, str] = {
        "parameters": "parameters",
    }

    subtype_mapping: Dict[str, str] = {
        "parameters": "GrantaServerApiSchemaParametersParameter",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        parameters: "Union[List[GrantaServerApiSchemaParametersParameter], None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaParametersParametersInfo - a model defined in Swagger

        Parameters
        ----------
        parameters: List[GrantaServerApiSchemaParametersParameter], optional
        """
        self._parameters: Union[
            List[GrantaServerApiSchemaParametersParameter], None, Unset_Type
        ] = Unset

        if parameters is not Unset:
            self.parameters = parameters

    @property
    def parameters(
        self,
    ) -> "Union[List[GrantaServerApiSchemaParametersParameter], None, Unset_Type]":
        """Gets the parameters of this GrantaServerApiSchemaParametersParametersInfo.

        Returns
        -------
        Union[List[GrantaServerApiSchemaParametersParameter], None, Unset_Type]
            The parameters of this GrantaServerApiSchemaParametersParametersInfo.
        """
        return self._parameters

    @parameters.setter
    def parameters(
        self,
        parameters: "Union[List[GrantaServerApiSchemaParametersParameter], None, Unset_Type]",
    ) -> None:
        """Sets the parameters of this GrantaServerApiSchemaParametersParametersInfo.

        Parameters
        ----------
        parameters: Union[List[GrantaServerApiSchemaParametersParameter], None, Unset_Type]
            The parameters of this GrantaServerApiSchemaParametersParametersInfo.
        """
        self._parameters = parameters

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
        if not isinstance(other, GrantaServerApiSchemaParametersParametersInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
