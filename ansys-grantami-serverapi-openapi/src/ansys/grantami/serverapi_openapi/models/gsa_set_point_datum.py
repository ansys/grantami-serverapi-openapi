"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.models.gsa_set_datum import GsaSetDatum  # noqa: F401
from ansys.grantami.serverapi_openapi.models.gsa_set_datum_type import GsaSetDatumType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaSetPointDatum(GsaSetDatum):
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
        "estimated": "bool",
        "set_datum_type": "GsaSetDatumType",
        "values": "list[GsaSetPointDatumValue]",
    }

    attribute_map: dict[str, str] = {
        "estimated": "estimated",
        "set_datum_type": "setDatumType",
        "values": "values",
    }

    subtype_mapping: dict[str, str] = {
        "values": "GsaSetPointDatumValue",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, estimated: "bool", set_datum_type: "GsaSetDatumType" = GsaSetDatumType.POINT, values: "list[GsaSetPointDatumValue]",) -> None:
        """GsaSetPointDatum - a model defined in Swagger

        Parameters
        ----------
        estimated: bool
        set_datum_type: GsaSetDatumType
        values: list[GsaSetPointDatumValue]
        """
        super().__init__(set_datum_type=set_datum_type)
        self._estimated: bool
        self._values: list[GsaSetPointDatumValue]

        self.estimated = estimated
        self.values = values

    @property
    def estimated(self) -> "bool":
        """Gets the estimated of this GsaSetPointDatum.

        Returns
        -------
        bool
            The estimated of this GsaSetPointDatum.
        """
        return self._estimated

    @estimated.setter
    def estimated(self, estimated: "bool") -> None:
        """Sets the estimated of this GsaSetPointDatum.

        Parameters
        ----------
        estimated: bool
            The estimated of this GsaSetPointDatum.
        """
        # Field is not nullable
        if estimated is None:
            raise ValueError("Invalid value for 'estimated', must not be 'None'")
        # Field is required
        if estimated is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'estimated', must not be 'Unset'")
        self._estimated = estimated

    @property
    def values(self) -> "list[GsaSetPointDatumValue]":
        """Gets the values of this GsaSetPointDatum.

        Returns
        -------
        list[GsaSetPointDatumValue]
            The values of this GsaSetPointDatum.
        """
        return self._values

    @values.setter
    def values(self, values: "list[GsaSetPointDatumValue]") -> None:
        """Sets the values of this GsaSetPointDatum.

        Parameters
        ----------
        values: list[GsaSetPointDatumValue]
            The values of this GsaSetPointDatum.
        """
        # Field is not nullable
        if values is None:
            raise ValueError("Invalid value for 'values', must not be 'None'")
        # Field is required
        if values is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'values', must not be 'Unset'")
        self._values = values

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
        if not isinstance(other, GsaSetPointDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

