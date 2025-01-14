"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaMoveRecordHistory(ModelBase):
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
        "new_parent": "GsaSlimRecordHistory",
    }

    attribute_map: dict[str, str] = {
        "new_parent": "newParent",
    }

    subtype_mapping: dict[str, str] = {
        "newParent": "GsaSlimRecordHistory",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, new_parent: "Union[GsaSlimRecordHistory, Unset_Type]" = Unset,) -> None:
        """GsaMoveRecordHistory - a model defined in Swagger

        Parameters
        ----------
        new_parent: GsaSlimRecordHistory, optional
        """
        self._new_parent: Union[GsaSlimRecordHistory, Unset_Type] = Unset

        if new_parent is not Unset:
            self.new_parent = new_parent

    @property
    def new_parent(self) -> "Union[GsaSlimRecordHistory, Unset_Type]":
        """Gets the new_parent of this GsaMoveRecordHistory.

        Returns
        -------
        Union[GsaSlimRecordHistory, Unset_Type]
            The new_parent of this GsaMoveRecordHistory.
        """
        return self._new_parent

    @new_parent.setter
    def new_parent(self, new_parent: "Union[GsaSlimRecordHistory, Unset_Type]") -> None:
        """Sets the new_parent of this GsaMoveRecordHistory.

        Parameters
        ----------
        new_parent: Union[GsaSlimRecordHistory, Unset_Type]
            The new_parent of this GsaMoveRecordHistory.
        """
        # Field is not nullable
        if new_parent is None:
            raise ValueError("Invalid value for 'new_parent', must not be 'None'")
        self._new_parent = new_parent

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
        if not isinstance(other, GsaMoveRecordHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

