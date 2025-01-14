"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.models.gsa_data_modification_error_detail import GsaDataModificationErrorDetail  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaUsageDataModificationErrorDetail(GsaDataModificationErrorDetail):
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
        "message": "str",
        "reason": "str",
        "referenced_by_type": "GsaReferencedByType",
    }

    attribute_map: dict[str, str] = {
        "message": "message",
        "reason": "reason",
        "referenced_by_type": "referencedByType",
    }

    subtype_mapping: dict[str, str] = {
        "referencedByType": "GsaReferencedByType",
    }

    discriminator_value_class_map = {
        "expression".lower(): "#/components/schemas/GsaExpressionUsageDataModificationErrorDetail",
        "versionControlledData".lower(): "#/components/schemas/GsaVersionControlledDataUsageDataModificationErrorDetail",
        "dynamicLinkGroup".lower(): "#/components/schemas/GsaDynamicLinkGroupUsageDataModificationErrorDetail",
        "tabularAttribute".lower(): "#/components/schemas/GsaTabularAttributeUsageDataModificationErrorDetail",
        "xyChartTemplate".lower(): "#/components/schemas/GsaXYChartTemplateUsageDataModificationErrorDetail",
        "searchMask".lower(): "#/components/schemas/GsaSearchMaskUsageDataModificationErrorDetail",
        "securityAttribute".lower(): "#/components/schemas/GsaSecurityAttributeUsageDataModificationErrorDetail",
        "attribute".lower(): "#/components/schemas/GsaAttributeUsageDataModificationErrorDetail",
        "data".lower(): "#/components/schemas/GsaDataUsageDataModificationErrorDetail",
        "defaultParameterValue".lower(): "#/components/schemas/GsaDefaultParameterValueUsageDataModificationErrorDetail",
    }

    discriminator: Optional[str] = "referenced_by_type"

    def __init__(self, *, message: "str", reason: "str" = "usage", referenced_by_type: "GsaReferencedByType",) -> None:
        """GsaUsageDataModificationErrorDetail - a model defined in Swagger

        Parameters
        ----------
        message: str
        reason: str
        referenced_by_type: GsaReferencedByType
        """
        super().__init__(message=message, reason=reason)
        self._referenced_by_type: GsaReferencedByType

        self.referenced_by_type = referenced_by_type

    @property
    def referenced_by_type(self) -> "GsaReferencedByType":
        """Gets the referenced_by_type of this GsaUsageDataModificationErrorDetail.

        Returns
        -------
        GsaReferencedByType
            The referenced_by_type of this GsaUsageDataModificationErrorDetail.
        """
        return self._referenced_by_type

    @referenced_by_type.setter
    def referenced_by_type(self, referenced_by_type: "GsaReferencedByType") -> None:
        """Sets the referenced_by_type of this GsaUsageDataModificationErrorDetail.

        Parameters
        ----------
        referenced_by_type: GsaReferencedByType
            The referenced_by_type of this GsaUsageDataModificationErrorDetail.
        """
        # Field is not nullable
        if referenced_by_type is None:
            raise ValueError("Invalid value for 'referenced_by_type', must not be 'None'")
        # Field is required
        if referenced_by_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'referenced_by_type', must not be 'Unset'")
        self._referenced_by_type = referenced_by_type

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
        if not isinstance(other, GsaUsageDataModificationErrorDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

