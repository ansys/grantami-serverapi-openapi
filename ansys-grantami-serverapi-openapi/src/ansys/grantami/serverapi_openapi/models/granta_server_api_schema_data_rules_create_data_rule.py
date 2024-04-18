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


class GrantaServerApiSchemaDataRulesCreateDataRule(ModelBase):
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
        "description": "str",
        "name": "str",
        "regular_expression": "str",
        "guid": "str",
    }

    attribute_map: Dict[str, str] = {
        "description": "description",
        "name": "name",
        "regular_expression": "regularExpression",
        "guid": "guid",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        description: "str",
        name: "str",
        regular_expression: "str",
        guid: "Union[str, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaDataRulesCreateDataRule - a model defined in Swagger

        Parameters
        ----------
        description: str
        name: str
        regular_expression: str
        guid: str, optional
        """
        self._description: str
        self._regular_expression: str
        self._name: str
        self._guid: Union[str, Unset_Type] = Unset

        self.description = description
        self.regular_expression = regular_expression
        self.name = name
        if guid is not Unset:
            self.guid = guid

    @property
    def description(self) -> "str":
        """Gets the description of this GrantaServerApiSchemaDataRulesCreateDataRule.

        Returns
        -------
        str
            The description of this GrantaServerApiSchemaDataRulesCreateDataRule.
        """
        return self._description

    @description.setter
    def description(self, description: "str") -> None:
        """Sets the description of this GrantaServerApiSchemaDataRulesCreateDataRule.

        Parameters
        ----------
        description: str
            The description of this GrantaServerApiSchemaDataRulesCreateDataRule.
        """
        # Field is not nullable
        if description is None:
            raise ValueError("Invalid value for 'description', must not be 'None'")
        # Field is required
        if description is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'description', must not be 'Unset'")
        self._description = description

    @property
    def regular_expression(self) -> "str":
        """Gets the regular_expression of this GrantaServerApiSchemaDataRulesCreateDataRule.

        Returns
        -------
        str
            The regular_expression of this GrantaServerApiSchemaDataRulesCreateDataRule.
        """
        return self._regular_expression

    @regular_expression.setter
    def regular_expression(self, regular_expression: "str") -> None:
        """Sets the regular_expression of this GrantaServerApiSchemaDataRulesCreateDataRule.

        Parameters
        ----------
        regular_expression: str
            The regular_expression of this GrantaServerApiSchemaDataRulesCreateDataRule.
        """
        # Field is not nullable
        if regular_expression is None:
            raise ValueError(
                "Invalid value for 'regular_expression', must not be 'None'"
            )
        # Field is required
        if regular_expression is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'regular_expression', must not be 'Unset'"
            )
        self._regular_expression = regular_expression

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaDataRulesCreateDataRule.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaDataRulesCreateDataRule.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaDataRulesCreateDataRule.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaDataRulesCreateDataRule.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        # Field is required
        if name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'name', must not be 'Unset'")
        self._name = name

    @property
    def guid(self) -> "Union[str, Unset_Type]":
        """Gets the guid of this GrantaServerApiSchemaDataRulesCreateDataRule.

        Returns
        -------
        Union[str, Unset_Type]
            The guid of this GrantaServerApiSchemaDataRulesCreateDataRule.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, Unset_Type]") -> None:
        """Sets the guid of this GrantaServerApiSchemaDataRulesCreateDataRule.

        Parameters
        ----------
        guid: Union[str, Unset_Type]
            The guid of this GrantaServerApiSchemaDataRulesCreateDataRule.
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
        if not isinstance(other, GrantaServerApiSchemaDataRulesCreateDataRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
