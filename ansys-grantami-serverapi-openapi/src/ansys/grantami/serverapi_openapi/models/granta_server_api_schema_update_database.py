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


class GrantaServerApiSchemaUpdateDatabase(ModelBase):
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
        "author": "str",
        "company": "str",
        "currency_code": "str",
        "guid": "str",
        "name": "str",
        "notes": "str",
        "version_guid": "str",
    }

    attribute_map: Dict[str, str] = {
        "author": "author",
        "company": "company",
        "currency_code": "currencyCode",
        "guid": "guid",
        "name": "name",
        "notes": "notes",
        "version_guid": "versionGuid",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        author: "Union[str, None, Unset_Type]" = Unset,
        company: "Union[str, None, Unset_Type]" = Unset,
        currency_code: "Union[str, None, Unset_Type]" = Unset,
        guid: "Union[str, Unset_Type]" = Unset,
        name: "Union[str, Unset_Type]" = Unset,
        notes: "Union[str, None, Unset_Type]" = Unset,
        version_guid: "Union[str, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaUpdateDatabase - a model defined in Swagger

        Parameters
        ----------
        author: str, optional
        company: str, optional
        currency_code: str, optional
        guid: str, optional
        name: str, optional
        notes: str, optional
        version_guid: str, optional
        """
        self._author: Union[str, None, Unset_Type] = Unset
        self._company: Union[str, None, Unset_Type] = Unset
        self._notes: Union[str, None, Unset_Type] = Unset
        self._currency_code: Union[str, None, Unset_Type] = Unset
        self._version_guid: Union[str, Unset_Type] = Unset
        self._name: Union[str, Unset_Type] = Unset
        self._guid: Union[str, Unset_Type] = Unset

        if author is not Unset:
            self.author = author
        if company is not Unset:
            self.company = company
        if notes is not Unset:
            self.notes = notes
        if currency_code is not Unset:
            self.currency_code = currency_code
        if version_guid is not Unset:
            self.version_guid = version_guid
        if name is not Unset:
            self.name = name
        if guid is not Unset:
            self.guid = guid

    @property
    def author(self) -> "Union[str, None, Unset_Type]":
        """Gets the author of this GrantaServerApiSchemaUpdateDatabase.

        Returns
        -------
        Union[str, None, Unset_Type]
            The author of this GrantaServerApiSchemaUpdateDatabase.
        """
        return self._author

    @author.setter
    def author(self, author: "Union[str, None, Unset_Type]") -> None:
        """Sets the author of this GrantaServerApiSchemaUpdateDatabase.

        Parameters
        ----------
        author: Union[str, None, Unset_Type]
            The author of this GrantaServerApiSchemaUpdateDatabase.
        """
        self._author = author

    @property
    def company(self) -> "Union[str, None, Unset_Type]":
        """Gets the company of this GrantaServerApiSchemaUpdateDatabase.

        Returns
        -------
        Union[str, None, Unset_Type]
            The company of this GrantaServerApiSchemaUpdateDatabase.
        """
        return self._company

    @company.setter
    def company(self, company: "Union[str, None, Unset_Type]") -> None:
        """Sets the company of this GrantaServerApiSchemaUpdateDatabase.

        Parameters
        ----------
        company: Union[str, None, Unset_Type]
            The company of this GrantaServerApiSchemaUpdateDatabase.
        """
        self._company = company

    @property
    def notes(self) -> "Union[str, None, Unset_Type]":
        """Gets the notes of this GrantaServerApiSchemaUpdateDatabase.

        Returns
        -------
        Union[str, None, Unset_Type]
            The notes of this GrantaServerApiSchemaUpdateDatabase.
        """
        return self._notes

    @notes.setter
    def notes(self, notes: "Union[str, None, Unset_Type]") -> None:
        """Sets the notes of this GrantaServerApiSchemaUpdateDatabase.

        Parameters
        ----------
        notes: Union[str, None, Unset_Type]
            The notes of this GrantaServerApiSchemaUpdateDatabase.
        """
        self._notes = notes

    @property
    def currency_code(self) -> "Union[str, None, Unset_Type]":
        """Gets the currency_code of this GrantaServerApiSchemaUpdateDatabase.

        Returns
        -------
        Union[str, None, Unset_Type]
            The currency_code of this GrantaServerApiSchemaUpdateDatabase.
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code: "Union[str, None, Unset_Type]") -> None:
        """Sets the currency_code of this GrantaServerApiSchemaUpdateDatabase.

        Parameters
        ----------
        currency_code: Union[str, None, Unset_Type]
            The currency_code of this GrantaServerApiSchemaUpdateDatabase.
        """
        self._currency_code = currency_code

    @property
    def version_guid(self) -> "Union[str, Unset_Type]":
        """Gets the version_guid of this GrantaServerApiSchemaUpdateDatabase.

        Returns
        -------
        Union[str, Unset_Type]
            The version_guid of this GrantaServerApiSchemaUpdateDatabase.
        """
        return self._version_guid

    @version_guid.setter
    def version_guid(self, version_guid: "Union[str, Unset_Type]") -> None:
        """Sets the version_guid of this GrantaServerApiSchemaUpdateDatabase.

        Parameters
        ----------
        version_guid: Union[str, Unset_Type]
            The version_guid of this GrantaServerApiSchemaUpdateDatabase.
        """
        # Field is not nullable
        if version_guid is None:
            raise ValueError("Invalid value for 'version_guid', must not be 'None'")
        self._version_guid = version_guid

    @property
    def name(self) -> "Union[str, Unset_Type]":
        """Gets the name of this GrantaServerApiSchemaUpdateDatabase.

        Returns
        -------
        Union[str, Unset_Type]
            The name of this GrantaServerApiSchemaUpdateDatabase.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, Unset_Type]") -> None:
        """Sets the name of this GrantaServerApiSchemaUpdateDatabase.

        Parameters
        ----------
        name: Union[str, Unset_Type]
            The name of this GrantaServerApiSchemaUpdateDatabase.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

    @property
    def guid(self) -> "Union[str, Unset_Type]":
        """Gets the guid of this GrantaServerApiSchemaUpdateDatabase.

        Returns
        -------
        Union[str, Unset_Type]
            The guid of this GrantaServerApiSchemaUpdateDatabase.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, Unset_Type]") -> None:
        """Sets the guid of this GrantaServerApiSchemaUpdateDatabase.

        Parameters
        ----------
        guid: Union[str, Unset_Type]
            The guid of this GrantaServerApiSchemaUpdateDatabase.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        self._guid = guid

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
        if not isinstance(other, GrantaServerApiSchemaUpdateDatabase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
