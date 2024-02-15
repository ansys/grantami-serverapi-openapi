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
    Dict,
    List,
    BinaryIO,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase
from ansys.grantami.serverapi_openapi.models.granta_server_api_search_datum_criterion import (
    GrantaServerApiSearchDatumCriterion,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSearchLogicalDatumCriterion(GrantaServerApiSearchDatumCriterion):
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
        "type": "str",
        "value": "bool",
    }

    attribute_map: Dict[str, str] = {
        "type": "type",
        "value": "value",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        type: "str" = "logical",
        value: "Optional[bool]" = None,
    ) -> None:
        """GrantaServerApiSearchLogicalDatumCriterion - a model defined in Swagger

        Parameters
        ----------
            type: str
            value: bool, optional
        """
        super().__init__()
        self._value = None
        self._type: str = None  # type: ignore[assignment]

        if value is not None:
            self.value = value
        self.type = type

    @property
    def value(self) -> "Optional[bool]":
        """Gets the value of this GrantaServerApiSearchLogicalDatumCriterion.
        Logical search value

        Returns
        -------
        bool
            The value of this GrantaServerApiSearchLogicalDatumCriterion.
        """
        return self._value

    @value.setter
    def value(self, value: "Optional[bool]") -> None:
        """Sets the value of this GrantaServerApiSearchLogicalDatumCriterion.
        Logical search value

        Parameters
        ----------
        value: bool
            The value of this GrantaServerApiSearchLogicalDatumCriterion.
        """
        self._value = value

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchLogicalDatumCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchLogicalDatumCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchLogicalDatumCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchLogicalDatumCriterion.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

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

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()  # type: ignore[no-any-return]

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiSearchLogicalDatumCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
