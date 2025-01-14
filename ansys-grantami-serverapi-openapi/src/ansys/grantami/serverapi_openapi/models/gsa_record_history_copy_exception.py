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


class GsaRecordHistoryCopyException(ModelBase):
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
        "code": "SystemNetHttpStatusCode",
        "errors": "list[GsaErrorDetail]",
        "message": "str",
    }

    attribute_map: dict[str, str] = {
        "code": "code",
        "errors": "errors",
        "message": "message",
    }

    subtype_mapping: dict[str, str] = {
        "code": "SystemNetHttpStatusCode",
        "errors": "GsaErrorDetail",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, code: "Union[SystemNetHttpStatusCode, Unset_Type]" = Unset, errors: "Union[list[GsaErrorDetail], None, Unset_Type]" = Unset, message: "Union[str, None, Unset_Type]" = Unset,) -> None:
        """GsaRecordHistoryCopyException - a model defined in Swagger

        Parameters
        ----------
        code: SystemNetHttpStatusCode, optional
        errors: list[GsaErrorDetail], optional
        message: str, optional
        """
        self._message: Union[str, None, Unset_Type] = Unset
        self._code: Union[SystemNetHttpStatusCode, Unset_Type] = Unset
        self._errors: Union[list[GsaErrorDetail], None, Unset_Type] = Unset

        if message is not Unset:
            self.message = message
        if code is not Unset:
            self.code = code
        if errors is not Unset:
            self.errors = errors

    @property
    def message(self) -> "Union[str, None, Unset_Type]":
        """Gets the message of this GsaRecordHistoryCopyException.

        Returns
        -------
        Union[str, None, Unset_Type]
            The message of this GsaRecordHistoryCopyException.
        """
        return self._message

    @message.setter
    def message(self, message: "Union[str, None, Unset_Type]") -> None:
        """Sets the message of this GsaRecordHistoryCopyException.

        Parameters
        ----------
        message: Union[str, None, Unset_Type]
            The message of this GsaRecordHistoryCopyException.
        """
        self._message = message

    @property
    def code(self) -> "Union[SystemNetHttpStatusCode, Unset_Type]":
        """Gets the code of this GsaRecordHistoryCopyException.

        Returns
        -------
        Union[SystemNetHttpStatusCode, Unset_Type]
            The code of this GsaRecordHistoryCopyException.
        """
        return self._code

    @code.setter
    def code(self, code: "Union[SystemNetHttpStatusCode, Unset_Type]") -> None:
        """Sets the code of this GsaRecordHistoryCopyException.

        Parameters
        ----------
        code: Union[SystemNetHttpStatusCode, Unset_Type]
            The code of this GsaRecordHistoryCopyException.
        """
        # Field is not nullable
        if code is None:
            raise ValueError("Invalid value for 'code', must not be 'None'")
        self._code = code

    @property
    def errors(self) -> "Union[list[GsaErrorDetail], None, Unset_Type]":
        """Gets the errors of this GsaRecordHistoryCopyException.

        Returns
        -------
        Union[list[GsaErrorDetail], None, Unset_Type]
            The errors of this GsaRecordHistoryCopyException.
        """
        return self._errors

    @errors.setter
    def errors(self, errors: "Union[list[GsaErrorDetail], None, Unset_Type]") -> None:
        """Sets the errors of this GsaRecordHistoryCopyException.

        Parameters
        ----------
        errors: Union[list[GsaErrorDetail], None, Unset_Type]
            The errors of this GsaRecordHistoryCopyException.
        """
        self._errors = errors

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
        if not isinstance(other, GsaRecordHistoryCopyException):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

