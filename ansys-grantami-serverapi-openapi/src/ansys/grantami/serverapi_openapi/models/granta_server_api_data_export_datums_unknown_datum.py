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
from ansys.grantami.serverapi_openapi.models.granta_server_api_data_export_datums_datum import (
    GrantaServerApiDataExportDatumsDatum,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiDataExportDatumsUnknownDatum(GrantaServerApiDataExportDatumsDatum):
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
        "attribute_guid": "str",
        "attribute_identity": "int",
        "meta_datums": "list[GrantaServerApiDataExportDatumsDatum]",
        "not_applicable": "str",
    }

    attribute_map: Dict[str, str] = {
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "meta_datums": "metaDatums",
        "not_applicable": "notApplicable",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_guid: "Union[str, Unset_Type]" = Unset,
        attribute_identity: "Union[int, Unset_Type]" = Unset,
        meta_datums: "Union[List[GrantaServerApiDataExportDatumsDatum], None, Unset_Type]" = Unset,
        not_applicable: "str" = "unknown",
    ) -> None:
        """GrantaServerApiDataExportDatumsUnknownDatum - a model defined in Swagger

        Parameters
        ----------
        attribute_guid: str, optional
        attribute_identity: int, optional
        meta_datums: List[GrantaServerApiDataExportDatumsDatum], optional
        not_applicable: str
        """
        super().__init__(
            attribute_guid=attribute_guid,
            attribute_identity=attribute_identity,
            meta_datums=meta_datums,
        )
        self._not_applicable: str

        self.not_applicable = not_applicable

    @property
    def not_applicable(self) -> "str":
        """Gets the not_applicable of this GrantaServerApiDataExportDatumsUnknownDatum.

        Returns
        -------
        str
            The not_applicable of this GrantaServerApiDataExportDatumsUnknownDatum.
        """
        return self._not_applicable

    @not_applicable.setter
    def not_applicable(self, not_applicable: "str") -> None:
        """Sets the not_applicable of this GrantaServerApiDataExportDatumsUnknownDatum.

        Parameters
        ----------
        not_applicable: str
            The not_applicable of this GrantaServerApiDataExportDatumsUnknownDatum.
        """
        # Field is not nullable
        if not_applicable is None:
            raise ValueError("Invalid value for 'not_applicable', must not be 'None'")
        # Field is required
        if not_applicable is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'not_applicable', must not be 'Unset'")
        self._not_applicable = not_applicable

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
        if not isinstance(other, GrantaServerApiDataExportDatumsUnknownDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
