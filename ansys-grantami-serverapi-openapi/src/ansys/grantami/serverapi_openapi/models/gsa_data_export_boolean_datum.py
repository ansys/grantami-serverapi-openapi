"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.models.gsa_data_export_applicable_datum import GsaDataExportApplicableDatum  # noqa: F401
from ansys.grantami.serverapi_openapi.models.gsa_attribute_type import GsaAttributeType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaDataExportBooleanDatum(GsaDataExportApplicableDatum):
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
        "attribute_guid": "str",
        "attribute_identity": "int",
        "datum_type": "GsaAttributeType",
        "not_applicable": "str",
        "datum_value": "bool",
        "meta_datums": "list[GsaDataExportDatum]",
    }

    attribute_map: dict[str, str] = {
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "datum_type": "datumType",
        "not_applicable": "notApplicable",
        "datum_value": "datumValue",
        "meta_datums": "metaDatums",
    }

    subtype_mapping: dict[str, str] = {
    }

    discriminator: Optional[str] = None

    def __init__(self, *, attribute_guid: "str", attribute_identity: "int", datum_type: "GsaAttributeType" = GsaAttributeType.LOGICAL, not_applicable: "str" = "applicable", datum_value: "Union[bool, Unset_Type]" = Unset, meta_datums: "Union[list[GsaDataExportDatum], None, Unset_Type]" = Unset,) -> None:
        """GsaDataExportBooleanDatum - a model defined in Swagger

        Parameters
        ----------
        attribute_guid: str
        attribute_identity: int
        datum_type: GsaAttributeType
        not_applicable: str
        datum_value: bool, optional
        meta_datums: list[GsaDataExportDatum], optional
        """
        super().__init__(attribute_guid=attribute_guid, attribute_identity=attribute_identity, datum_type=datum_type, not_applicable=not_applicable, meta_datums=meta_datums)
        self._datum_value: Union[bool, Unset_Type] = Unset

        if datum_value is not Unset:
            self.datum_value = datum_value

    @property
    def datum_value(self) -> "Union[bool, Unset_Type]":
        """Gets the datum_value of this GsaDataExportBooleanDatum.

        Returns
        -------
        Union[bool, Unset_Type]
            The datum_value of this GsaDataExportBooleanDatum.
        """
        return self._datum_value

    @datum_value.setter
    def datum_value(self, datum_value: "Union[bool, Unset_Type]") -> None:
        """Sets the datum_value of this GsaDataExportBooleanDatum.

        Parameters
        ----------
        datum_value: Union[bool, Unset_Type]
            The datum_value of this GsaDataExportBooleanDatum.
        """
        # Field is not nullable
        if datum_value is None:
            raise ValueError("Invalid value for 'datum_value', must not be 'None'")
        self._datum_value = datum_value

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
        if not isinstance(other, GsaDataExportBooleanDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

