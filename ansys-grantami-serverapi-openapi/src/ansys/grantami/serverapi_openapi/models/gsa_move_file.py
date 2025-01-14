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


class GsaMoveFile(ModelBase):
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
        "folder_guid": "str",
    }

    attribute_map: dict[str, str] = {
        "folder_guid": "folderGuid",
    }

    subtype_mapping: dict[str, str] = {
    }

    discriminator: Optional[str] = None

    def __init__(self, *, folder_guid: "str",) -> None:
        """GsaMoveFile - a model defined in Swagger

        Parameters
        ----------
        folder_guid: str
        """
        self._folder_guid: str

        self.folder_guid = folder_guid

    @property
    def folder_guid(self) -> "str":
        """Gets the folder_guid of this GsaMoveFile.

        Returns
        -------
        str
            The folder_guid of this GsaMoveFile.
        """
        return self._folder_guid

    @folder_guid.setter
    def folder_guid(self, folder_guid: "str") -> None:
        """Sets the folder_guid of this GsaMoveFile.

        Parameters
        ----------
        folder_guid: str
            The folder_guid of this GsaMoveFile.
        """
        # Field is not nullable
        if folder_guid is None:
            raise ValueError("Invalid value for 'folder_guid', must not be 'None'")
        # Field is required
        if folder_guid is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'folder_guid', must not be 'Unset'")
        self._folder_guid = folder_guid

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
        if not isinstance(other, GsaMoveFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

