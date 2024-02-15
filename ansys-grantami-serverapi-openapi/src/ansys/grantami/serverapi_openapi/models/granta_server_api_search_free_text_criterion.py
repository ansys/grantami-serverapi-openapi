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
    Dict,
    List,
    BinaryIO,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase
from ansys.grantami.serverapi_openapi.models.granta_server_api_search_criterion import (
    GrantaServerApiSearchCriterion,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSearchFreeTextCriterion(GrantaServerApiSearchCriterion):
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
    discriminator_class_map: Dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: Dict[str, str] = {
        "type": "str",
        "value": "str",
    }

    attribute_map: Dict[str, str] = {
        "type": "type",
        "value": "value",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator_value_class_map = {
        "all".lower(): "#/components/schemas/GrantaServerApiSearchFreeTextAllCriterion",
        "allAttributes".lower(): "#/components/schemas/GrantaServerApiSearchFreeTextAllAttributesCriterion",
        "excludingAttributes".lower(): "#/components/schemas/GrantaServerApiSearchFreeTextExcludingAttributesCriterion",
        "specifiedAttributes".lower(): "#/components/schemas/GrantaServerApiSearchFreeTextSpecifiedAttributesCriterion",
        "allLocalColumns".lower(): "#/components/schemas/GrantaServerApiSearchFreeTextAllLocalColumnsCriterion",
        "excludingLocalColumns".lower(): "#/components/schemas/GrantaServerApiSearchFreeTextExcludingLocalColumnsCriterion",
        "specifiedLocalColumns".lower(): "#/components/schemas/GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion",
    }

    discriminator: Optional[str] = "free_text_criterion_type"

    def __init__(
        self,
        *,
        type: "str" = "text",
        value: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiSearchFreeTextCriterion - a model defined in Swagger

        Parameters
        ----------
            type: str
            value: str, optional
        """
        super().__init__()
        self._value = None
        self._type: str = None  # type: ignore[assignment]

        if value is not None:
            self.value = value
        self.type = type

    @property
    def value(self) -> "Optional[str]":
        """Gets the value of this GrantaServerApiSearchFreeTextCriterion.

        Returns
        -------
        str
            The value of this GrantaServerApiSearchFreeTextCriterion.
        """
        return self._value

    @value.setter
    def value(self, value: "Optional[str]") -> None:
        """Sets the value of this GrantaServerApiSearchFreeTextCriterion.

        Parameters
        ----------
        value: str
            The value of this GrantaServerApiSearchFreeTextCriterion.
        """
        self._value = value

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchFreeTextCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchFreeTextCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchFreeTextCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchFreeTextCriterion.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @classmethod
    def get_real_child_model(cls, data: ModelBase) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[cls._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen,
        # so we have to extract it from the JSON reference
        return cls.discriminator_value_class_map[discriminator_value].rsplit("/", 1)[-1]

    @classmethod
    def _get_discriminator_field_name(cls) -> str:
        assert cls.discriminator
        name_tokens = cls.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()  # type: ignore[no-any-return]

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiSearchFreeTextCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
