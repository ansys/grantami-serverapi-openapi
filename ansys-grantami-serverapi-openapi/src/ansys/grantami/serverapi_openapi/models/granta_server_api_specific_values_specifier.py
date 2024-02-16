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
from ansys.grantami.serverapi_openapi.models.granta_server_api_value_specifier import (
    GrantaServerApiValueSpecifier,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSpecificValuesSpecifier(GrantaServerApiValueSpecifier):
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
        "filter_on": "str",
        "guids": "list[str]",
        "identities": "list[int]",
    }

    attribute_map: Dict[str, str] = {
        "filter_on": "filterOn",
        "guids": "guids",
        "identities": "identities",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        filter_on: "str" = "specific",
        guids: "Optional[List[str]]" = None,
        identities: "Optional[List[int]]" = None,
    ) -> None:
        """GrantaServerApiSpecificValuesSpecifier - a model defined in Swagger

        Parameters
        ----------
            filter_on: str
            guids: List[str], optional
            identities: List[int], optional
        """
        super().__init__()
        self._identities = None
        self._guids = None
        self._filter_on: str = None  # type: ignore[assignment]

        if identities is not None:
            self.identities = identities
        if guids is not None:
            self.guids = guids
        self.filter_on = filter_on

    @property
    def identities(self) -> "Optional[List[int]]":
        """Gets the identities of this GrantaServerApiSpecificValuesSpecifier.

        Returns
        -------
        list[int]
            The identities of this GrantaServerApiSpecificValuesSpecifier.
        """
        return self._identities

    @identities.setter
    def identities(self, identities: "Optional[List[int]]") -> None:
        """Sets the identities of this GrantaServerApiSpecificValuesSpecifier.

        Parameters
        ----------
        identities: List[int]
            The identities of this GrantaServerApiSpecificValuesSpecifier.
        """
        self._identities = identities

    @property
    def guids(self) -> "Optional[List[str]]":
        """Gets the guids of this GrantaServerApiSpecificValuesSpecifier.

        Returns
        -------
        list[str]
            The guids of this GrantaServerApiSpecificValuesSpecifier.
        """
        return self._guids

    @guids.setter
    def guids(self, guids: "Optional[List[str]]") -> None:
        """Sets the guids of this GrantaServerApiSpecificValuesSpecifier.

        Parameters
        ----------
        guids: List[str]
            The guids of this GrantaServerApiSpecificValuesSpecifier.
        """
        self._guids = guids

    @property
    def filter_on(self) -> "str":
        """Gets the filter_on of this GrantaServerApiSpecificValuesSpecifier.

        Returns
        -------
        str
            The filter_on of this GrantaServerApiSpecificValuesSpecifier.
        """
        return self._filter_on

    @filter_on.setter
    def filter_on(self, filter_on: "str") -> None:
        """Sets the filter_on of this GrantaServerApiSpecificValuesSpecifier.

        Parameters
        ----------
        filter_on: str
            The filter_on of this GrantaServerApiSpecificValuesSpecifier.
        """
        if filter_on is None:
            raise ValueError("Invalid value for 'filter_on', must not be 'None'")
        self._filter_on = filter_on

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
        if not isinstance(other, GrantaServerApiSpecificValuesSpecifier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
