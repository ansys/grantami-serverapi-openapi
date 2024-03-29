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


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiDataExportPropertiesProperty(ModelBase):
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
    discriminator_class_map: Dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: Dict[str, str] = {}

    attribute_map: Dict[str, str] = {}

    subtype_mapping: Dict[str, str] = {}

    discriminator_value_class_map = {
        "createdByUser".lower(): "#/components/schemas/GrantaServerApiDataExportPropertiesCreatedByUserProperty",
        "createdDate".lower(): "#/components/schemas/GrantaServerApiDataExportPropertiesCreatedDateProperty",
        "databaseKey".lower(): "#/components/schemas/GrantaServerApiDataExportPropertiesDatabaseKeyProperty",
        "fullName".lower(): "#/components/schemas/GrantaServerApiDataExportPropertiesFullNameProperty",
        "lastModifiedDate".lower(): "#/components/schemas/GrantaServerApiDataExportPropertiesLastModifiedDateProperty",
        "lastModifiedByUser".lower(): "#/components/schemas/GrantaServerApiDataExportPropertiesLastModifiedByUserProperty",
        "recordColor".lower(): "#/components/schemas/GrantaServerApiDataExportPropertiesRecordColorProperty",
        "recordGuid".lower(): "#/components/schemas/GrantaServerApiDataExportPropertiesRecordGuidProperty",
        "recordIdentity".lower(): "#/components/schemas/GrantaServerApiDataExportPropertiesRecordIdentityProperty",
        "recordHistoryGuid".lower(): "#/components/schemas/GrantaServerApiDataExportPropertiesRecordHistoryGuidProperty",
        "recordHistoryIdentity".lower(): "#/components/schemas/GrantaServerApiDataExportPropertiesRecordHistoryIdentityProperty",
        "recordType".lower(): "#/components/schemas/GrantaServerApiDataExportPropertiesRecordTypeProperty",
        "releasedDate".lower(): "#/components/schemas/GrantaServerApiDataExportPropertiesReleasedDateProperty",
        "shortName".lower(): "#/components/schemas/GrantaServerApiDataExportPropertiesShortNameProperty",
        "tableGuid".lower(): "#/components/schemas/GrantaServerApiDataExportPropertiesTableGuidProperty",
        "tableIdentity".lower(): "#/components/schemas/GrantaServerApiDataExportPropertiesTableIdentityProperty",
        "tableName".lower(): "#/components/schemas/GrantaServerApiDataExportPropertiesTableNameProperty",
        "versionNumber".lower(): "#/components/schemas/GrantaServerApiDataExportPropertiesVersionNumberProperty",
        "versionState".lower(): "#/components/schemas/GrantaServerApiDataExportPropertiesVersionStateProperty",
    }

    discriminator: Optional[str] = "property_name"

    def __init__(
        self,
    ) -> None:
        """GrantaServerApiDataExportPropertiesProperty - a model defined in Swagger"""

    @classmethod
    def get_real_child_model(cls, data: Dict[str, str]) -> str:
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
        if not isinstance(other, GrantaServerApiDataExportPropertiesProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
