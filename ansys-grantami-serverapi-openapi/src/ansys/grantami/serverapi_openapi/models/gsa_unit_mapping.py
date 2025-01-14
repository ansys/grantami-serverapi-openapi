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


class GsaUnitMapping(ModelBase):
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
        "equivalent_unit": "GsaSlimUnit",
        "unit": "GsaSlimUnit",
    }

    attribute_map: dict[str, str] = {
        "equivalent_unit": "equivalentUnit",
        "unit": "unit",
    }

    subtype_mapping: dict[str, str] = {
        "unit": "GsaSlimUnit",
        "equivalentUnit": "GsaSlimUnit",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, equivalent_unit: "GsaSlimUnit", unit: "GsaSlimUnit",) -> None:
        """GsaUnitMapping - a model defined in Swagger

        Parameters
        ----------
        equivalent_unit: GsaSlimUnit
        unit: GsaSlimUnit
        """
        self._unit: GsaSlimUnit
        self._equivalent_unit: GsaSlimUnit

        self.unit = unit
        self.equivalent_unit = equivalent_unit

    @property
    def unit(self) -> "GsaSlimUnit":
        """Gets the unit of this GsaUnitMapping.

        Returns
        -------
        GsaSlimUnit
            The unit of this GsaUnitMapping.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "GsaSlimUnit") -> None:
        """Sets the unit of this GsaUnitMapping.

        Parameters
        ----------
        unit: GsaSlimUnit
            The unit of this GsaUnitMapping.
        """
        # Field is not nullable
        if unit is None:
            raise ValueError("Invalid value for 'unit', must not be 'None'")
        # Field is required
        if unit is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'unit', must not be 'Unset'")
        self._unit = unit

    @property
    def equivalent_unit(self) -> "GsaSlimUnit":
        """Gets the equivalent_unit of this GsaUnitMapping.

        Returns
        -------
        GsaSlimUnit
            The equivalent_unit of this GsaUnitMapping.
        """
        return self._equivalent_unit

    @equivalent_unit.setter
    def equivalent_unit(self, equivalent_unit: "GsaSlimUnit") -> None:
        """Sets the equivalent_unit of this GsaUnitMapping.

        Parameters
        ----------
        equivalent_unit: GsaSlimUnit
            The equivalent_unit of this GsaUnitMapping.
        """
        # Field is not nullable
        if equivalent_unit is None:
            raise ValueError("Invalid value for 'equivalent_unit', must not be 'None'")
        # Field is required
        if equivalent_unit is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'equivalent_unit', must not be 'Unset'")
        self._equivalent_unit = equivalent_unit

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
        if not isinstance(other, GsaUnitMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

