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


class GrantaServerApiDataExportExportFailuresDatumReference(ModelBase):
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
    swagger_types = {
        "attribute_identity": "int",
        "database_key": "str",
        "record_history_identity": "int",
        "attribute_guid": "str",
    }

    attribute_map = {
        "attribute_identity": "attributeIdentity",
        "database_key": "databaseKey",
        "record_history_identity": "recordHistoryIdentity",
        "attribute_guid": "attributeGuid",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        attribute_identity: "int",
        database_key: "str",
        record_history_identity: "int",
        attribute_guid: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiDataExportExportFailuresDatumReference - a model defined in Swagger

        Parameters
        ----------
            attribute_identity: int
            database_key: str
            record_history_identity: int
            attribute_guid: str, optional
        """
        self._database_key = None
        self._record_history_identity = None
        self._attribute_identity = None
        self._attribute_guid = None

        self.database_key = database_key
        self.record_history_identity = record_history_identity
        self.attribute_identity = attribute_identity
        if attribute_guid is not None:
            self.attribute_guid = attribute_guid

    @property
    def database_key(self) -> "str":
        """Gets the database_key of this GrantaServerApiDataExportExportFailuresDatumReference.

        Returns
        -------
        str
            The database_key of this GrantaServerApiDataExportExportFailuresDatumReference.
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key: "str") -> None:
        """Sets the database_key of this GrantaServerApiDataExportExportFailuresDatumReference.

        Parameters
        ----------
        database_key: str
            The database_key of this GrantaServerApiDataExportExportFailuresDatumReference.
        """
        if database_key is None:
            raise ValueError("Invalid value for 'database_key', must not be 'None'")
        self._database_key = database_key

    @property
    def record_history_identity(self) -> "int":
        """Gets the record_history_identity of this GrantaServerApiDataExportExportFailuresDatumReference.

        Returns
        -------
        int
            The record_history_identity of this GrantaServerApiDataExportExportFailuresDatumReference.
        """
        return self._record_history_identity

    @record_history_identity.setter
    def record_history_identity(self, record_history_identity: "int") -> None:
        """Sets the record_history_identity of this GrantaServerApiDataExportExportFailuresDatumReference.

        Parameters
        ----------
        record_history_identity: int
            The record_history_identity of this GrantaServerApiDataExportExportFailuresDatumReference.
        """
        if record_history_identity is None:
            raise ValueError(
                "Invalid value for 'record_history_identity', must not be 'None'"
            )
        self._record_history_identity = record_history_identity

    @property
    def attribute_identity(self) -> "int":
        """Gets the attribute_identity of this GrantaServerApiDataExportExportFailuresDatumReference.

        Returns
        -------
        int
            The attribute_identity of this GrantaServerApiDataExportExportFailuresDatumReference.
        """
        return self._attribute_identity

    @attribute_identity.setter
    def attribute_identity(self, attribute_identity: "int") -> None:
        """Sets the attribute_identity of this GrantaServerApiDataExportExportFailuresDatumReference.

        Parameters
        ----------
        attribute_identity: int
            The attribute_identity of this GrantaServerApiDataExportExportFailuresDatumReference.
        """
        if attribute_identity is None:
            raise ValueError(
                "Invalid value for 'attribute_identity', must not be 'None'"
            )
        self._attribute_identity = attribute_identity

    @property
    def attribute_guid(self) -> "str":
        """Gets the attribute_guid of this GrantaServerApiDataExportExportFailuresDatumReference.

        Returns
        -------
        str
            The attribute_guid of this GrantaServerApiDataExportExportFailuresDatumReference.
        """
        return self._attribute_guid

    @attribute_guid.setter
    def attribute_guid(self, attribute_guid: "str") -> None:
        """Sets the attribute_guid of this GrantaServerApiDataExportExportFailuresDatumReference.

        Parameters
        ----------
        attribute_guid: str
            The attribute_guid of this GrantaServerApiDataExportExportFailuresDatumReference.
        """
        self._attribute_guid = attribute_guid

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
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiDataExportExportFailuresDatumReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
