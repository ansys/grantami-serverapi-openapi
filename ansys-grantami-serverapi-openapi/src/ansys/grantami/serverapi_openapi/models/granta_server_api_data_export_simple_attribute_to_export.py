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
from ansys.grantami.serverapi_openapi.models.granta_server_api_data_export_attribute_to_export import (
    GrantaServerApiDataExportAttributeToExport,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiDataExportSimpleAttributeToExport(
    GrantaServerApiDataExportAttributeToExport
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
        "attribute_type": "str",
        "guid": "str",
        "identity": "int",
        "roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "summary_roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
    }

    attribute_map: Dict[str, str] = {
        "attribute_type": "attributeType",
        "guid": "guid",
        "identity": "identity",
        "roll_up_type": "rollUpType",
        "summary_roll_up_type": "summaryRollUpType",
    }

    subtype_mapping: Dict[str, str] = {
        "rollUpType": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "summaryRollUpType": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_type: "str" = "simple",
        guid: "Union[str, None, Unset_Type]" = Unset,
        identity: "Union[int, None, Unset_Type]" = Unset,
        roll_up_type: "Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]" = Unset,
        summary_roll_up_type: "Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiDataExportSimpleAttributeToExport - a model defined in Swagger

        Parameters
        ----------
        attribute_type: str
        guid: str, optional
        identity: int, optional
        roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, optional
        summary_roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, optional
        """
        super().__init__(guid=guid, identity=identity)
        self._roll_up_type: Union[
            GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type
        ] = Unset
        self._summary_roll_up_type: Union[
            GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type
        ] = Unset
        self._attribute_type: str

        if roll_up_type is not Unset:
            self.roll_up_type = roll_up_type
        if summary_roll_up_type is not Unset:
            self.summary_roll_up_type = summary_roll_up_type
        self.attribute_type = attribute_type

    @property
    def roll_up_type(
        self,
    ) -> (
        "Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]"
    ):
        """Gets the roll_up_type of this GrantaServerApiDataExportSimpleAttributeToExport.

        Returns
        -------
        Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]
            The roll_up_type of this GrantaServerApiDataExportSimpleAttributeToExport.
        """
        return self._roll_up_type

    @roll_up_type.setter
    def roll_up_type(
        self,
        roll_up_type: "Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]",
    ) -> None:
        """Sets the roll_up_type of this GrantaServerApiDataExportSimpleAttributeToExport.

        Parameters
        ----------
        roll_up_type: Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]
            The roll_up_type of this GrantaServerApiDataExportSimpleAttributeToExport.
        """
        # Field is not nullable
        if roll_up_type is None:
            raise ValueError("Invalid value for 'roll_up_type', must not be 'None'")
        self._roll_up_type = roll_up_type

    @property
    def summary_roll_up_type(
        self,
    ) -> (
        "Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]"
    ):
        """Gets the summary_roll_up_type of this GrantaServerApiDataExportSimpleAttributeToExport.

        Returns
        -------
        Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]
            The summary_roll_up_type of this GrantaServerApiDataExportSimpleAttributeToExport.
        """
        return self._summary_roll_up_type

    @summary_roll_up_type.setter
    def summary_roll_up_type(
        self,
        summary_roll_up_type: "Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]",
    ) -> None:
        """Sets the summary_roll_up_type of this GrantaServerApiDataExportSimpleAttributeToExport.

        Parameters
        ----------
        summary_roll_up_type: Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]
            The summary_roll_up_type of this GrantaServerApiDataExportSimpleAttributeToExport.
        """
        # Field is not nullable
        if summary_roll_up_type is None:
            raise ValueError(
                "Invalid value for 'summary_roll_up_type', must not be 'None'"
            )
        self._summary_roll_up_type = summary_roll_up_type

    @property
    def attribute_type(self) -> "str":
        """Gets the attribute_type of this GrantaServerApiDataExportSimpleAttributeToExport.

        Returns
        -------
        str
            The attribute_type of this GrantaServerApiDataExportSimpleAttributeToExport.
        """
        return self._attribute_type

    @attribute_type.setter
    def attribute_type(self, attribute_type: "str") -> None:
        """Sets the attribute_type of this GrantaServerApiDataExportSimpleAttributeToExport.

        Parameters
        ----------
        attribute_type: str
            The attribute_type of this GrantaServerApiDataExportSimpleAttributeToExport.
        """
        # Field is not nullable
        if attribute_type is None:
            raise ValueError("Invalid value for 'attribute_type', must not be 'None'")
        # Field is required
        if attribute_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'attribute_type', must not be 'Unset'")
        self._attribute_type = attribute_type

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
        if not isinstance(other, GrantaServerApiDataExportSimpleAttributeToExport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
