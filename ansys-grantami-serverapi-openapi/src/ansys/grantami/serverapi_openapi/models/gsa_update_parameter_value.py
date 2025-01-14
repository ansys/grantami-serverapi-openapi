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


class GsaUpdateParameterValue(ModelBase):
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
    discriminator_class_map: dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "type": "GsaParameterValueType",
        "guid": "str",
    }

    attribute_map: dict[str, str] = {
        "type": "type",
        "guid": "guid",
    }

    subtype_mapping: dict[str, str] = {
        "type": "GsaParameterValueType",
    }

    discriminator_value_class_map = {
        "discrete".lower(): "#/components/schemas/GsaUpdateDiscreteParameterValue",
        "numeric".lower(): "#/components/schemas/GsaUpdateNumericParameterValue",
    }

    discriminator: Optional[str] = "type"

    def __init__(self, *, type: "GsaParameterValueType", guid: "Union[str, Unset_Type]" = Unset,) -> None:
        """GsaUpdateParameterValue - a model defined in Swagger

        Parameters
        ----------
        type: GsaParameterValueType
        guid: str, optional
        """
        self._type: GsaParameterValueType
        self._guid: Union[str, Unset_Type] = Unset

        self.type = type
        if guid is not Unset:
            self.guid = guid

    @property
    def type(self) -> "GsaParameterValueType":
        """Gets the type of this GsaUpdateParameterValue.

        Returns
        -------
        GsaParameterValueType
            The type of this GsaUpdateParameterValue.
        """
        return self._type

    @type.setter
    def type(self, type: "GsaParameterValueType") -> None:
        """Sets the type of this GsaUpdateParameterValue.

        Parameters
        ----------
        type: GsaParameterValueType
            The type of this GsaUpdateParameterValue.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

    @property
    def guid(self) -> "Union[str, Unset_Type]":
        """Gets the guid of this GsaUpdateParameterValue.

        Returns
        -------
        Union[str, Unset_Type]
            The guid of this GsaUpdateParameterValue.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, Unset_Type]") -> None:
        """Sets the guid of this GsaUpdateParameterValue.

        Parameters
        ----------
        guid: Union[str, Unset_Type]
            The guid of this GsaUpdateParameterValue.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        self._guid = guid

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[cls._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen,
        # so we have to extract it from the JSON reference
        return cls.discriminator_value_class_map[discriminator_value].rsplit("/", 1)[-1]

    @classmethod
    def _get_discriminator_field_name(cls) -> str:
        assert cls.discriminator
        name_tokens = cls.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GsaUpdateParameterValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

