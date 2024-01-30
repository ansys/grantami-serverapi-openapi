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
    swagger_types = {
        "full_name": "str",
        "record_type": "GrantaServerApiRecordType",
        "guid": "str",
        "parent": "GrantaServerApiRecordsRecordHistoriesSlimRecordHistory",
        "tree_name": "str",
    }

    attribute_map = {
        "full_name": "fullName",
        "record_type": "recordType",
        "guid": "guid",
        "parent": "parent",
        "tree_name": "treeName",
    }

    subtype_mapping = {
        "recordType": "GrantaServerApiRecordType",
        "parent": "GrantaServerApiRecordsRecordHistoriesSlimRecordHistory",
    }

    discriminator = None

    def __init__(
        self,
        *,
        full_name: "str",
        record_type: "GrantaServerApiRecordType",
        guid: "Optional[str]" = None,
        parent: "Optional[GrantaServerApiRecordsRecordHistoriesSlimRecordHistory]" = None,
        tree_name: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiRecordsRecordHistoriesCreateRecordHistory - a model defined in Swagger

        Parameters
        ----------
            full_name: str
            record_type: GrantaServerApiRecordType
            guid: str, optional
            parent: GrantaServerApiRecordsRecordHistoriesSlimRecordHistory, optional
            tree_name: str, optional
        """
        self._record_type = None
        self._full_name = None
        self._tree_name = None
        self._parent = None
        self._guid = None

        self.record_type = record_type
        self.full_name = full_name
        if tree_name is not None:
            self.tree_name = tree_name
        if parent is not None:
            self.parent = parent
        if guid is not None:
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
        if record_type is None:
            raise ValueError("Invalid value for 'record_type', must not be 'None'")
        self._record_type = record_type

    @property
    def full_name(self) -> "str":
        """Gets the full_name of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.

        Returns
        -------
        str
            The full_name of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name: "str") -> None:
        """Sets the full_name of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.

        Parameters
        ----------
        full_name: str
            The full_name of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.
        """
        if full_name is None:
            raise ValueError("Invalid value for 'full_name', must not be 'None'")
        self._full_name = full_name

    @property
    def tree_name(self) -> "str":
        """Gets the tree_name of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.

        Returns
        -------
        str
            The tree_name of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.
        """
        return self._tree_name

    @tree_name.setter
    def tree_name(self, tree_name: "str") -> None:
        """Sets the tree_name of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.

        Parameters
        ----------
        tree_name: str
            The tree_name of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.
        """
        self._tree_name = tree_name

    @property
    def parent(self) -> "GrantaServerApiRecordsRecordHistoriesSlimRecordHistory":
        """Gets the parent of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.

        Returns
        -------
        GrantaServerApiRecordsRecordHistoriesSlimRecordHistory
            The parent of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.
        """
        return self._parent

    @parent.setter
    def parent(
        self, parent: "GrantaServerApiRecordsRecordHistoriesSlimRecordHistory"
    ) -> None:
        """Sets the parent of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.

        Parameters
        ----------
        parent: GrantaServerApiRecordsRecordHistoriesSlimRecordHistory
            The parent of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.
        """
        self._parent = parent

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.

        Returns
        -------
        str
            The guid of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiRecordsRecordHistoriesCreateRecordHistory.
        """
        self._guid = guid

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
        if not isinstance(
            other, GrantaServerApiRecordsRecordHistoriesCreateRecordHistory
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
