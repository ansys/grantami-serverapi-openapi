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
from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_parameters_update_parameter import (
    GrantaServerApiSchemaParametersUpdateParameter,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaParametersUpdateDiscreteParameter(
    GrantaServerApiSchemaParametersUpdateParameter
):
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
        "default_parameter_value_guid": "str",
        "guid": "str",
        "help_path": "str",
        "name": "str",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "default_parameter_value_guid": "defaultParameterValueGuid",
        "guid": "guid",
        "help_path": "helpPath",
        "name": "name",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        default_parameter_value_guid: "Union[str, Unset_Type]" = Unset,
        guid: "Union[str, Unset_Type]" = Unset,
        help_path: "Union[str, None, Unset_Type]" = Unset,
        name: "Union[str, Unset_Type]" = Unset,
        type: "str" = "discrete",
    ) -> None:
        """GrantaServerApiSchemaParametersUpdateDiscreteParameter - a model defined in Swagger

        Parameters
        ----------
        default_parameter_value_guid: str, optional
        guid: str, optional
        help_path: str, optional
        name: str, optional
        type: str
        """
        super().__init__(
            default_parameter_value_guid=default_parameter_value_guid,
            guid=guid,
            help_path=help_path,
            name=name,
        )
        self._type: str

        self.type = type

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaParametersUpdateDiscreteParameter.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaParametersUpdateDiscreteParameter.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaParametersUpdateDiscreteParameter.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaParametersUpdateDiscreteParameter.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

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
            other, GrantaServerApiSchemaParametersUpdateDiscreteParameter
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
