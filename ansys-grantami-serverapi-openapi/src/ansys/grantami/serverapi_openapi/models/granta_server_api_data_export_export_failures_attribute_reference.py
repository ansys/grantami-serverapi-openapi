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


class GrantaServerApiDataExportExportFailuresAttributeReference(ModelBase):
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
        "database_key": "str",
        "attribute_guid": "str",
        "attribute_identity": "int",
    }

    attribute_map: Dict[str, str] = {
        "database_key": "databaseKey",
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        database_key: "str",
        attribute_guid: "Union[str, None, Unset_Type]" = Unset,
        attribute_identity: "Union[int, None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiDataExportExportFailuresAttributeReference - a model defined in Swagger

        Parameters
        ----------
        database_key: str
        attribute_guid: str, optional
        attribute_identity: int, optional
        """
        self._database_key: str
        self._attribute_identity: Union[int, None, Unset_Type] = Unset
        self._attribute_guid: Union[str, None, Unset_Type] = Unset

        self.database_key = database_key
        if attribute_identity is not Unset:
            self.attribute_identity = attribute_identity
        if attribute_guid is not Unset:
            self.attribute_guid = attribute_guid

    @property
    def database_key(self) -> "str":
        """Gets the database_key of this GrantaServerApiDataExportExportFailuresAttributeReference.

        Returns
        -------
        str
            The database_key of this GrantaServerApiDataExportExportFailuresAttributeReference.
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key: "str") -> None:
        """Sets the database_key of this GrantaServerApiDataExportExportFailuresAttributeReference.

        Parameters
        ----------
        database_key: str
            The database_key of this GrantaServerApiDataExportExportFailuresAttributeReference.
        """
        # Field is not nullable
        if database_key is None:
            raise ValueError("Invalid value for 'database_key', must not be 'None'")
        # Field is required
        if database_key is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'database_key', must not be 'Unset'")
        self._database_key = database_key

    @property
    def attribute_identity(self) -> "Union[int, None, Unset_Type]":
        """Gets the attribute_identity of this GrantaServerApiDataExportExportFailuresAttributeReference.

        Returns
        -------
        Union[int, None, Unset_Type]
            The attribute_identity of this GrantaServerApiDataExportExportFailuresAttributeReference.
        """
        return self._attribute_identity

    @attribute_identity.setter
    def attribute_identity(
        self, attribute_identity: "Union[int, None, Unset_Type]"
    ) -> None:
        """Sets the attribute_identity of this GrantaServerApiDataExportExportFailuresAttributeReference.

        Parameters
        ----------
        attribute_identity: Union[int, None, Unset_Type]
            The attribute_identity of this GrantaServerApiDataExportExportFailuresAttributeReference.
        """
        self._attribute_identity = attribute_identity

    @property
    def attribute_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the attribute_guid of this GrantaServerApiDataExportExportFailuresAttributeReference.

        Returns
        -------
        Union[str, None, Unset_Type]
            The attribute_guid of this GrantaServerApiDataExportExportFailuresAttributeReference.
        """
        return self._attribute_guid

    @attribute_guid.setter
    def attribute_guid(self, attribute_guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the attribute_guid of this GrantaServerApiDataExportExportFailuresAttributeReference.

        Parameters
        ----------
        attribute_guid: Union[str, None, Unset_Type]
            The attribute_guid of this GrantaServerApiDataExportExportFailuresAttributeReference.
        """
        self._attribute_guid = attribute_guid

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
        if not isinstance(
            other, GrantaServerApiDataExportExportFailuresAttributeReference
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
