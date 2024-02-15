"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase


if TYPE_CHECKING:
    from . import *


class GrantaServerApiDataExportAttributeToExport(ModelBase):
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
    swagger_types = {
        "guid": "str",
        "identity": "int",
    }

    attribute_map = {
        "guid": "guid",
        "identity": "identity",
    }

    subtype_mapping = {}

    discriminator_value_class_map = {
        "link".lower(): "#/components/schemas/GrantaServerApiDataExportLinkAttributeToExport",
        "simple".lower(): "#/components/schemas/GrantaServerApiDataExportSimpleAttributeToExport",
    }

    discriminator = "attribute_type"

    def __init__(
        self,
        *,
        guid: "Optional[str]" = None,
        identity: "Optional[int]" = None,
    ) -> None:
        """GrantaServerApiDataExportAttributeToExport - a model defined in Swagger

        Parameters
        ----------
            guid: str, optional
            identity: int, optional
        """
        self._identity = None
        self._guid = None

        if identity is not None:
            self.identity = identity
        if guid is not None:
            self.guid = guid

    @property
    def identity(self) -> "int":
        """Gets the identity of this GrantaServerApiDataExportAttributeToExport.

        Returns
        -------
        int
            The identity of this GrantaServerApiDataExportAttributeToExport.
        """
        return self._identity

    @identity.setter
    def identity(self, identity: "int") -> None:
        """Sets the identity of this GrantaServerApiDataExportAttributeToExport.

        Parameters
        ----------
        identity: int
            The identity of this GrantaServerApiDataExportAttributeToExport.
        """
        self._identity = identity

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiDataExportAttributeToExport.

        Returns
        -------
        str
            The guid of this GrantaServerApiDataExportAttributeToExport.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiDataExportAttributeToExport.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiDataExportAttributeToExport.
        """
        self._guid = guid

    @classmethod
    def get_real_child_model(cls, data: ModelBase) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[cls._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen,
        # so we have to extract it from the JSON reference
        return cls.discriminator_value_class_map.get(discriminator_value).rsplit(
            "/", 1
        )[-1]

    @classmethod
    def _get_discriminator_field_name(cls) -> str:
        name_tokens = cls.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiDataExportAttributeToExport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
