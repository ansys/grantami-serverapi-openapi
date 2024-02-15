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
from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_attributes_attribute import (
    GrantaServerApiSchemaAttributesAttribute,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute(
    GrantaServerApiSchemaAttributesAttribute
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
        "attribute_parameters": "list[GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter]",
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "discrete_type": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "display_names": "dict(str, str)",
        "guid": "str",
        "info": "GrantaServerApiSchemaAttributesAttributeAttributeInfo",
        "name": "str",
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "axis_name": "str",
        "help_path": "str",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "attribute_parameters": "attributeParameters",
        "default_threshold_type": "defaultThresholdType",
        "discrete_type": "discreteType",
        "display_names": "displayNames",
        "guid": "guid",
        "info": "info",
        "name": "name",
        "about_attribute": "aboutAttribute",
        "axis_name": "axisName",
        "help_path": "helpPath",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {
        "discreteType": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "attributeParameters": "GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_parameters: "List[GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter]",
        default_threshold_type: "GrantaServerApiSchemaAttributesAttributeThresholdType",
        discrete_type: "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        display_names: "Dict[str, str]",
        guid: "str",
        info: "GrantaServerApiSchemaAttributesAttributeAttributeInfo",
        name: "str",
        about_attribute: "Optional[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]" = None,
        axis_name: "Optional[str]" = None,
        help_path: "Optional[str]" = None,
        type: "str" = "discreteFunctional",
    ) -> None:
        """GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute - a model defined in Swagger

        Parameters
        ----------
            attribute_parameters: List[GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter]
            default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType
            discrete_type: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
            display_names: Dict[str, str]
            guid: str
            info: GrantaServerApiSchemaAttributesAttributeAttributeInfo
            name: str
            about_attribute: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, optional
            axis_name: str, optional
            help_path: str, optional
            type: str
        """
        super().__init__(
            default_threshold_type=default_threshold_type,
            display_names=display_names,
            guid=guid,
            info=info,
            name=name,
            about_attribute=about_attribute,
            axis_name=axis_name,
            help_path=help_path,
        )
        self._type: str = None  # type: ignore[assignment]
        self._discrete_type: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity = None  # type: ignore[assignment]
        self._attribute_parameters: List[GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter] = None  # type: ignore[assignment]

        self.type = type
        self.discrete_type = discrete_type
        self.attribute_parameters = attribute_parameters

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @property
    def discrete_type(self) -> "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity":
        """Gets the discrete_type of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
            The discrete_type of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute.
        """
        return self._discrete_type

    @discrete_type.setter
    def discrete_type(
        self, discrete_type: "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity"
    ) -> None:
        """Sets the discrete_type of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute.

        Parameters
        ----------
        discrete_type: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
            The discrete_type of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute.
        """
        if discrete_type is None:
            raise ValueError("Invalid value for 'discrete_type', must not be 'None'")
        self._discrete_type = discrete_type

    @property
    def attribute_parameters(
        self,
    ) -> "List[GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter]":
        """Gets the attribute_parameters of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute.

        Returns
        -------
        list[GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter]
            The attribute_parameters of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute.
        """
        return self._attribute_parameters

    @attribute_parameters.setter
    def attribute_parameters(
        self,
        attribute_parameters: "List[GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter]",
    ) -> None:
        """Sets the attribute_parameters of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute.

        Parameters
        ----------
        attribute_parameters: List[GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter]
            The attribute_parameters of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute.
        """
        if attribute_parameters is None:
            raise ValueError(
                "Invalid value for 'attribute_parameters', must not be 'None'"
            )
        self._attribute_parameters = attribute_parameters

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
        return self.to_str()  # type: ignore[no-any-return]

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(
            other, GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
