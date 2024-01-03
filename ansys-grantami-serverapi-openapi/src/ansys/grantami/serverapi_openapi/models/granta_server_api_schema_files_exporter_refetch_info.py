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


class GrantaServerApiSchemaFilesExporterRefetchInfo(ModelBase):
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
        "errors": "list[str]",
        "succeeded": "bool",
    }

    attribute_map = {
        "errors": "errors",
        "succeeded": "succeeded",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        errors: "Optional[List[str]]" = None,
        succeeded: "Optional[bool]" = None,
    ) -> None:
        """GrantaServerApiSchemaFilesExporterRefetchInfo - a model defined in Swagger

        Parameters
        ----------
            errors: List[str], optional
            succeeded: bool, optional
        """
        self._succeeded = None
        self._errors = None

        if succeeded is not None:
            self.succeeded = succeeded
        if errors is not None:
            self.errors = errors

    @property
    def succeeded(self) -> "bool":
        """Gets the succeeded of this GrantaServerApiSchemaFilesExporterRefetchInfo.

        Returns
        -------
        bool
            The succeeded of this GrantaServerApiSchemaFilesExporterRefetchInfo.
        """
        return self._succeeded

    @succeeded.setter
    def succeeded(self, succeeded: "bool") -> None:
        """Sets the succeeded of this GrantaServerApiSchemaFilesExporterRefetchInfo.

        Parameters
        ----------
        succeeded: bool
            The succeeded of this GrantaServerApiSchemaFilesExporterRefetchInfo.
        """
        self._succeeded = succeeded

    @property
    def errors(self) -> "list[str]":
        """Gets the errors of this GrantaServerApiSchemaFilesExporterRefetchInfo.

        Returns
        -------
        list[str]
            The errors of this GrantaServerApiSchemaFilesExporterRefetchInfo.
        """
        return self._errors

    @errors.setter
    def errors(self, errors: "list[str]") -> None:
        """Sets the errors of this GrantaServerApiSchemaFilesExporterRefetchInfo.

        Parameters
        ----------
        errors: list[str]
            The errors of this GrantaServerApiSchemaFilesExporterRefetchInfo.
        """
        self._errors = errors

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
        if not isinstance(other, GrantaServerApiSchemaFilesExporterRefetchInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
