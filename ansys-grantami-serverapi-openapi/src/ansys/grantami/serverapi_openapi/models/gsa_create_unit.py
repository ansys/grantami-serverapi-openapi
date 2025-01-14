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


class GsaCreateUnit(ModelBase):
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
        "name": "str",
        "symbol": "str",
        "equation": "str",
        "guid": "str",
    }

    attribute_map: dict[str, str] = {
        "name": "name",
        "symbol": "symbol",
        "equation": "equation",
        "guid": "guid",
    }

    subtype_mapping: dict[str, str] = {
    }

    discriminator: Optional[str] = None

    def __init__(self, *, name: "str", symbol: "str", equation: "Union[str, None, Unset_Type]" = Unset, guid: "Union[str, Unset_Type]" = Unset,) -> None:
        """GsaCreateUnit - a model defined in Swagger

        Parameters
        ----------
        name: str
        symbol: str
        equation: str, optional
        guid: str, optional
        """
        self._symbol: str
        self._equation: Union[str, None, Unset_Type] = Unset
        self._name: str
        self._guid: Union[str, Unset_Type] = Unset

        self.symbol = symbol
        if equation is not Unset:
            self.equation = equation
        self.name = name
        if guid is not Unset:
            self.guid = guid

    @property
    def symbol(self) -> "str":
        """Gets the symbol of this GsaCreateUnit.

        Returns
        -------
        str
            The symbol of this GsaCreateUnit.
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol: "str") -> None:
        """Sets the symbol of this GsaCreateUnit.

        Parameters
        ----------
        symbol: str
            The symbol of this GsaCreateUnit.
        """
        # Field is not nullable
        if symbol is None:
            raise ValueError("Invalid value for 'symbol', must not be 'None'")
        # Field is required
        if symbol is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'symbol', must not be 'Unset'")
        self._symbol = symbol

    @property
    def equation(self) -> "Union[str, None, Unset_Type]":
        """Gets the equation of this GsaCreateUnit.

        Returns
        -------
        Union[str, None, Unset_Type]
            The equation of this GsaCreateUnit.
        """
        return self._equation

    @equation.setter
    def equation(self, equation: "Union[str, None, Unset_Type]") -> None:
        """Sets the equation of this GsaCreateUnit.

        Parameters
        ----------
        equation: Union[str, None, Unset_Type]
            The equation of this GsaCreateUnit.
        """
        self._equation = equation

    @property
    def name(self) -> "str":
        """Gets the name of this GsaCreateUnit.

        Returns
        -------
        str
            The name of this GsaCreateUnit.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GsaCreateUnit.

        Parameters
        ----------
        name: str
            The name of this GsaCreateUnit.
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
        """Gets the guid of this GsaCreateUnit.

        Returns
        -------
        Union[str, Unset_Type]
            The guid of this GsaCreateUnit.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, Unset_Type]") -> None:
        """Sets the guid of this GsaCreateUnit.

        Parameters
        ----------
        guid: Union[str, Unset_Type]
            The guid of this GsaCreateUnit.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        self._guid = guid

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
        if not isinstance(other, GsaCreateUnit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

