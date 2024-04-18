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


class GrantaServerApiSchemaParametersCreateParameter(ModelBase):
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
        "default_parameter_value_index": "int",
        "name": "str",
        "guid": "str",
        "help_path": "str",
    }

    attribute_map: Dict[str, str] = {
        "default_parameter_value_index": "defaultParameterValueIndex",
        "name": "name",
        "guid": "guid",
        "help_path": "helpPath",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator_value_class_map = {
        "discrete".lower(): "#/components/schemas/GrantaServerApiSchemaParametersCreateDiscreteParameter",
        "numeric".lower(): "#/components/schemas/GrantaServerApiSchemaParametersCreateNumericParameter",
    }

    discriminator: Optional[str] = "type"

    def __init__(
        self,
        *,
        default_parameter_value_index: "int",
        name: "str",
        guid: "Union[str, Unset_Type]" = Unset,
        help_path: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaParametersCreateParameter - a model defined in Swagger

        Parameters
        ----------
        default_parameter_value_index: int
        name: str
        guid: str, optional
        help_path: str, optional
        """
        self._help_path: Union[str, None, Unset_Type] = Unset
        self._default_parameter_value_index: int
        self._name: str
        self._guid: Union[str, Unset_Type] = Unset

        if help_path is not Unset:
            self.help_path = help_path
        self.default_parameter_value_index = default_parameter_value_index
        self.name = name
        if guid is not Unset:
            self.guid = guid

    @property
    def help_path(self) -> "Union[str, None, Unset_Type]":
        """Gets the help_path of this GrantaServerApiSchemaParametersCreateParameter.

        Returns
        -------
        Union[str, None, Unset_Type]
            The help_path of this GrantaServerApiSchemaParametersCreateParameter.
        """
        return self._help_path

    @help_path.setter
    def help_path(self, help_path: "Union[str, None, Unset_Type]") -> None:
        """Sets the help_path of this GrantaServerApiSchemaParametersCreateParameter.

        Parameters
        ----------
        help_path: Union[str, None, Unset_Type]
            The help_path of this GrantaServerApiSchemaParametersCreateParameter.
        """
        self._help_path = help_path

    @property
    def default_parameter_value_index(self) -> "int":
        """Gets the default_parameter_value_index of this GrantaServerApiSchemaParametersCreateParameter.

        Returns
        -------
        int
            The default_parameter_value_index of this GrantaServerApiSchemaParametersCreateParameter.
        """
        return self._default_parameter_value_index

    @default_parameter_value_index.setter
    def default_parameter_value_index(
        self, default_parameter_value_index: "int"
    ) -> None:
        """Sets the default_parameter_value_index of this GrantaServerApiSchemaParametersCreateParameter.

        Parameters
        ----------
        default_parameter_value_index: int
            The default_parameter_value_index of this GrantaServerApiSchemaParametersCreateParameter.
        """
        # Field is not nullable
        if default_parameter_value_index is None:
            raise ValueError(
                "Invalid value for 'default_parameter_value_index', must not be 'None'"
            )
        # Field is required
        if default_parameter_value_index is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'default_parameter_value_index', must not be 'Unset'"
            )
        self._default_parameter_value_index = default_parameter_value_index

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaParametersCreateParameter.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaParametersCreateParameter.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaParametersCreateParameter.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaParametersCreateParameter.
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
        """Gets the guid of this GrantaServerApiSchemaParametersCreateParameter.

        Returns
        -------
        Union[str, Unset_Type]
            The guid of this GrantaServerApiSchemaParametersCreateParameter.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, Unset_Type]") -> None:
        """Sets the guid of this GrantaServerApiSchemaParametersCreateParameter.

        Parameters
        ----------
        guid: Union[str, Unset_Type]
            The guid of this GrantaServerApiSchemaParametersCreateParameter.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        self._guid = guid

    @classmethod
    def get_real_child_model(cls, data: Dict[str, str]) -> str:
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
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiSchemaParametersCreateParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
