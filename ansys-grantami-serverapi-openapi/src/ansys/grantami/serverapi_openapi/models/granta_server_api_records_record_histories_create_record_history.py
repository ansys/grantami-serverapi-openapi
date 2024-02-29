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


class GrantaServerApiRecordsRecordHistoriesCreateRecordHistory(ModelBase):
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
        "name": "str",
        "record_type": "GrantaServerApiRecordType",
        "guid": "str",
        "parent": "GrantaServerApiRecordsRecordHistoriesSlimRecordHistory",
        "record_color": "GrantaServerApiRecordColor",
        "short_name": "str",
    }

    attribute_map: Dict[str, str] = {
        "name": "name",
        "record_type": "recordType",
        "guid": "guid",
        "parent": "parent",
        "record_color": "recordColor",
        "short_name": "shortName",
    }

    subtype_mapping: Dict[str, str] = {
        "recordType": "GrantaServerApiRecordType",
        "parent": "GrantaServerApiRecordsRecordHistoriesSlimRecordHistory",
        "recordColor": "GrantaServerApiRecordColor",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        name: "str",
        record_type: "GrantaServerApiRecordType",
        guid: "Union[str, Unset_Type]" = Unset,
        parent: "Union[GrantaServerApiRecordsRecordHistoriesSlimRecordHistory, Unset_Type]" = Unset,
        record_color: "Union[GrantaServerApiRecordColor, Unset_Type]" = Unset,
        short_name: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiRecordsRecordHistoriesCreateRecordHistory - a model defined in Swagger

        Parameters
        ----------
        name: str
        record_type: GrantaServerApiRecordType
        guid: str, optional
        parent: GrantaServerApiRecordsRecordHistoriesSlimRecordHistory, optional
        record_color: GrantaServerApiRecordColor, optional
        short_name: str, optional
        """
        self._record_type: GrantaServerApiRecordType
        self._name: str
        self._short_name: Union[str, None, Unset_Type] = Unset
        self._parent: Union[
            GrantaServerApiRecordsRecordHistoriesSlimRecordHistory, Unset_Type
        ] = Unset
        self._record_color: Union[GrantaServerApiRecordColor, Unset_Type] = Unset
        self._guid: Union[str, Unset_Type] = Unset

        self.record_type = record_type
        self.name = name
        if short_name is not Unset:
            self.short_name = short_name
        if parent is not Unset:
            self.parent = parent
        if record_color is not Unset:
            self.record_color = record_color
        if guid is not Unset:
            self.guid = guid

    @property
    def record_type(self) -> "GrantaServerApiRecordType":
        """Gets the record_type of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.

        Returns
        -------
        GrantaServerApiRecordType
            The record_type of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type: "GrantaServerApiRecordType") -> None:
        """Sets the record_type of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.

        Parameters
        ----------
        record_type: GrantaServerApiRecordType
            The record_type of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.
        """
        # Field is not nullable
        if record_type is None:
            raise ValueError("Invalid value for 'record_type', must not be 'None'")
        # Field is required
        if record_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'record_type', must not be 'Unset'")
        self._record_type = record_type

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.

        Returns
        -------
        str
            The name of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        # Field is required
        if name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'name', must not be 'Unset'")
        self._name = name

    @property
    def short_name(self) -> "Union[str, None, Unset_Type]":
        """Gets the short_name of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.

        Returns
        -------
        Union[str, None, Unset_Type]
            The short_name of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name: "Union[str, None, Unset_Type]") -> None:
        """Sets the short_name of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.

        Parameters
        ----------
        short_name: Union[str, None, Unset_Type]
            The short_name of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.
        """
        self._short_name = short_name

    @property
    def parent(
        self,
    ) -> "Union[GrantaServerApiRecordsRecordHistoriesSlimRecordHistory, Unset_Type]":
        """Gets the parent of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.

        Returns
        -------
        Union[GrantaServerApiRecordsRecordHistoriesSlimRecordHistory, Unset_Type]
            The parent of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.
        """
        return self._parent

    @parent.setter
    def parent(
        self,
        parent: "Union[GrantaServerApiRecordsRecordHistoriesSlimRecordHistory, Unset_Type]",
    ) -> None:
        """Sets the parent of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.

        Parameters
        ----------
        parent: Union[GrantaServerApiRecordsRecordHistoriesSlimRecordHistory, Unset_Type]
            The parent of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.
        """
        # Field is not nullable
        if parent is None:
            raise ValueError("Invalid value for 'parent', must not be 'None'")
        self._parent = parent

    @property
    def record_color(self) -> "Union[GrantaServerApiRecordColor, Unset_Type]":
        """Gets the record_color of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.

        Returns
        -------
        Union[GrantaServerApiRecordColor, Unset_Type]
            The record_color of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.
        """
        return self._record_color

    @record_color.setter
    def record_color(
        self, record_color: "Union[GrantaServerApiRecordColor, Unset_Type]"
    ) -> None:
        """Sets the record_color of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.

        Parameters
        ----------
        record_color: Union[GrantaServerApiRecordColor, Unset_Type]
            The record_color of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.
        """
        # Field is not nullable
        if record_color is None:
            raise ValueError("Invalid value for 'record_color', must not be 'None'")
        self._record_color = record_color

    @property
    def guid(self) -> "Union[str, Unset_Type]":
        """Gets the guid of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.

        Returns
        -------
        Union[str, Unset_Type]
            The guid of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, Unset_Type]") -> None:
        """Sets the guid of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.

        Parameters
        ----------
        guid: Union[str, Unset_Type]
            The guid of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.
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
        if not isinstance(
            other, GrantaServerApiRecordsRecordHistoriesCreateRecordHistory
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
