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


class GsaTablesInfo(ModelBase):
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
        "tables": "list[GsaSlimTable]",
    }

    attribute_map: dict[str, str] = {
        "tables": "tables",
    }

    subtype_mapping: dict[str, str] = {
        "tables": "GsaSlimTable",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, tables: "Union[list[GsaSlimTable], None, Unset_Type]" = Unset,) -> None:
        """GsaTablesInfo - a model defined in Swagger

        Parameters
        ----------
        tables: list[GsaSlimTable], optional
        """
        self._tables: Union[list[GsaSlimTable], None, Unset_Type] = Unset

        if tables is not Unset:
            self.tables = tables

    @property
    def tables(self) -> "Union[list[GsaSlimTable], None, Unset_Type]":
        """Gets the tables of this GsaTablesInfo.

        Returns
        -------
        Union[list[GsaSlimTable], None, Unset_Type]
            The tables of this GsaTablesInfo.
        """
        return self._tables

    @tables.setter
    def tables(self, tables: "Union[list[GsaSlimTable], None, Unset_Type]") -> None:
        """Sets the tables of this GsaTablesInfo.

        Parameters
        ----------
        tables: Union[list[GsaSlimTable], None, Unset_Type]
            The tables of this GsaTablesInfo.
        """
        self._tables = tables

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
        if not isinstance(other, GsaTablesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

