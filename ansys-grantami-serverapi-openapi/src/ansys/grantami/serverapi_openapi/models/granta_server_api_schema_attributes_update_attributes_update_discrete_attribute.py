"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase
from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_attributes_update_attributes_update_attribute import (
    GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute,
)  # noqa: F401


if TYPE_CHECKING:
    from . import *


class GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteAttribute(
    GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute
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
    swagger_types = {
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "axis_name": "str",
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "guid": "str",
        "help_path": "str",
        "is_multi_valued": "bool",
        "name": "str",
        "type": "str",
    }

    attribute_map = {
        "about_attribute": "aboutAttribute",
        "axis_name": "axisName",
        "default_threshold_type": "defaultThresholdType",
        "guid": "guid",
        "help_path": "helpPath",
        "is_multi_valued": "isMultiValued",
        "name": "name",
        "type": "type",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        about_attribute: "Optional[GrantaServerApiSchemaSlimEntitiesSlimEntity]" = None,
        axis_name: "Optional[str]" = None,
        default_threshold_type: "Optional[GrantaServerApiSchemaAttributesAttributeThresholdType]" = None,
        guid: "Optional[str]" = None,
        help_path: "Optional[str]" = None,
        is_multi_valued: "Optional[bool]" = None,
        name: "Optional[str]" = None,
        type: "str" = "discrete",
    ) -> None:
        """GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteAttribute - a model defined in Swagger

        Parameters
        ----------
            about_attribute: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
            axis_name: str, optional
            default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType, optional
            guid: str, optional
            help_path: str, optional
            is_multi_valued: bool, optional
            name: str, optional
            type: str
        """
        super().__init__(
            about_attribute=about_attribute,
            axis_name=axis_name,
            default_threshold_type=default_threshold_type,
            guid=guid,
            help_path=help_path,
            name=name,
        )
        self._type = None
        self._is_multi_valued = None

        self.type = type
        if is_multi_valued is not None:
            self.is_multi_valued = is_multi_valued

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteAttribute.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteAttribute.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteAttribute.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @property
    def is_multi_valued(self) -> "bool":
        """Gets the is_multi_valued of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteAttribute.

        Returns
        -------
        bool
            The is_multi_valued of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteAttribute.
        """
        return self._is_multi_valued

    @is_multi_valued.setter
    def is_multi_valued(self, is_multi_valued: "bool") -> None:
        """Sets the is_multi_valued of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteAttribute.

        Parameters
        ----------
        is_multi_valued: bool
            The is_multi_valued of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteAttribute.
        """
        self._is_multi_valued = is_multi_valued

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
            other,
            GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteAttribute,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
