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
from ansys.grantami.serverapi_openapi.models.granta_server_api_data_export_properties_property import (
    GrantaServerApiDataExportPropertiesProperty,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiDataExportPropertiesTableGuidProperty(
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
        "table_guid": "str",
    }

    attribute_map: Dict[str, str] = {
        "property_name": "propertyName",
        "table_guid": "tableGuid",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        property_name: "str" = "tableGuid",
        table_guid: "Union[str, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiDataExportPropertiesTableGuidProperty - a model defined in Swagger

        Parameters
        ----------
        property_name: str
        table_guid: str, optional
        """
        super().__init__()
        self._property_name: str
        self._table_guid: Union[str, Unset_Type] = Unset

        self.property_name = property_name
        if table_guid is not Unset:
            self.table_guid = table_guid

    @property
    def property_name(self) -> "str":
        """Gets the property_name of this GrantaServerApiDataExportPropertiesTableGuidProperty.

        Returns
        -------
        str
            The property_name of this GrantaServerApiDataExportPropertiesTableGuidProperty.
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name: "str") -> None:
        """Sets the property_name of this GrantaServerApiDataExportPropertiesTableGuidProperty.

        Parameters
        ----------
        property_name: str
            The property_name of this GrantaServerApiDataExportPropertiesTableGuidProperty.
        """
        # Field is not nullable
        if property_name is None:
            raise ValueError("Invalid value for 'property_name', must not be 'None'")
        # Field is required
        if property_name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'property_name', must not be 'Unset'")
        self._property_name = property_name

    @property
    def table_guid(self) -> "Union[str, Unset_Type]":
        """Gets the table_guid of this GrantaServerApiDataExportPropertiesTableGuidProperty.

        Returns
        -------
        Union[str, Unset_Type]
            The table_guid of this GrantaServerApiDataExportPropertiesTableGuidProperty.
        """
        return self._table_guid

    @table_guid.setter
    def table_guid(self, table_guid: "Union[str, Unset_Type]") -> None:
        """Sets the table_guid of this GrantaServerApiDataExportPropertiesTableGuidProperty.

        Parameters
        ----------
        table_guid: Union[str, Unset_Type]
            The table_guid of this GrantaServerApiDataExportPropertiesTableGuidProperty.
        """
        # Field is not nullable
        if table_guid is None:
            raise ValueError("Invalid value for 'table_guid', must not be 'None'")
        self._table_guid = table_guid

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
        if not isinstance(other, GrantaServerApiDataExportPropertiesTableGuidProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
