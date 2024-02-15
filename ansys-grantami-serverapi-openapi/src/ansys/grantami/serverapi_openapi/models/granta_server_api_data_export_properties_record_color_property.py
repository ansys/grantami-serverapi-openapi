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
from ansys.grantami.serverapi_openapi.models.granta_server_api_data_export_properties_property import (
    GrantaServerApiDataExportPropertiesProperty,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiDataExportPropertiesRecordColorProperty(
    GrantaServerApiDataExportPropertiesProperty
):
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
        "property_name": "str",
        "record_color": "GrantaServerApiRecordColor",
    }

    attribute_map: Dict[str, str] = {
        "property_name": "propertyName",
        "record_color": "recordColor",
    }

    subtype_mapping: Dict[str, str] = {
        "recordColor": "GrantaServerApiRecordColor",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        property_name: "str" = "recordColor",
        record_color: "Optional[GrantaServerApiRecordColor]" = None,
    ) -> None:
        """GrantaServerApiDataExportPropertiesRecordColorProperty - a model defined in Swagger

        Parameters
        ----------
            property_name: str
            record_color: GrantaServerApiRecordColor, optional
        """
        super().__init__()
        self._property_name: str = None  # type: ignore[assignment]
        self._record_color = None

        self.property_name = property_name
        if record_color is not None:
            self.record_color = record_color

    @property
    def property_name(self) -> "str":
        """Gets the property_name of this GrantaServerApiDataExportPropertiesRecordColorProperty.

        Returns
        -------
        str
            The property_name of this GrantaServerApiDataExportPropertiesRecordColorProperty.
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name: "str") -> None:
        """Sets the property_name of this GrantaServerApiDataExportPropertiesRecordColorProperty.

        Parameters
        ----------
        property_name: str
            The property_name of this GrantaServerApiDataExportPropertiesRecordColorProperty.
        """
        if property_name is None:
            raise ValueError("Invalid value for 'property_name', must not be 'None'")
        self._property_name = property_name

    @property
    def record_color(self) -> "Optional[GrantaServerApiRecordColor]":
        """Gets the record_color of this GrantaServerApiDataExportPropertiesRecordColorProperty.

        Returns
        -------
        GrantaServerApiRecordColor
            The record_color of this GrantaServerApiDataExportPropertiesRecordColorProperty.
        """
        return self._record_color

    @record_color.setter
    def record_color(
        self, record_color: "Optional[GrantaServerApiRecordColor]"
    ) -> None:
        """Sets the record_color of this GrantaServerApiDataExportPropertiesRecordColorProperty.

        Parameters
        ----------
        record_color: GrantaServerApiRecordColor
            The record_color of this GrantaServerApiDataExportPropertiesRecordColorProperty.
        """
        self._record_color = record_color

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
        if not isinstance(
            other, GrantaServerApiDataExportPropertiesRecordColorProperty
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
