"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.models.gsa_property import GsaProperty  # noqa: F401
from ansys.grantami.serverapi_openapi.models.gsa_record_property import GsaRecordProperty


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaRecordColorProperty(GsaProperty):
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
        "property_name": "GsaRecordProperty",
        "record_color": "GsaRecordColor",
    }

    attribute_map: dict[str, str] = {
        "property_name": "propertyName",
        "record_color": "recordColor",
    }

    subtype_mapping: dict[str, str] = {
        "recordColor": "GsaRecordColor",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, property_name: "GsaRecordProperty" = GsaRecordProperty.RECORDCOLOR, record_color: "Union[GsaRecordColor, Unset_Type]" = Unset,) -> None:
        """GsaRecordColorProperty - a model defined in Swagger

        Parameters
        ----------
        property_name: GsaRecordProperty
        record_color: GsaRecordColor, optional
        """
        super().__init__(property_name=property_name)
        self._record_color: Union[GsaRecordColor, Unset_Type] = Unset

        if record_color is not Unset:
            self.record_color = record_color

    @property
    def record_color(self) -> "Union[GsaRecordColor, Unset_Type]":
        """Gets the record_color of this GsaRecordColorProperty.

        Returns
        -------
        Union[GsaRecordColor, Unset_Type]
            The record_color of this GsaRecordColorProperty.
        """
        return self._record_color

    @record_color.setter
    def record_color(self, record_color: "Union[GsaRecordColor, Unset_Type]") -> None:
        """Sets the record_color of this GsaRecordColorProperty.

        Parameters
        ----------
        record_color: Union[GsaRecordColor, Unset_Type]
            The record_color of this GsaRecordColorProperty.
        """
        # Field is not nullable
        if record_color is None:
            raise ValueError("Invalid value for 'record_color', must not be 'None'")
        self._record_color = record_color

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
        if not isinstance(other, GsaRecordColorProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

