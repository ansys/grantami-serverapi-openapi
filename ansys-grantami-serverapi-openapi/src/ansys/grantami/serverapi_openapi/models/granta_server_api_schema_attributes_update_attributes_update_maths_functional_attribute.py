"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase

from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_attributes_update_attributes_update_attribute import (
    GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute,
)  # noqa: F401

if TYPE_CHECKING:
    from . import *


class GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute(
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

    """
    swagger_types = {
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "allow_all_compatible_expressions": "bool",
        "allow_extrapolation": "bool",
        "attribute_parameters": "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
        "axis_name": "str",
        "default_content": "GrantaServerApiSchemaAttributesMathsContent",
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "expressions": "list[GrantaServerApiSchemaSlimEntitiesSlimExpression]",
        "guid": "str",
        "help_path": "str",
        "is_range": "bool",
        "name": "str",
        "type": "str",
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimUnit",
    }

    attribute_map = {
        "about_attribute": "aboutAttribute",
        "allow_all_compatible_expressions": "allowAllCompatibleExpressions",
        "allow_extrapolation": "allowExtrapolation",
        "attribute_parameters": "attributeParameters",
        "axis_name": "axisName",
        "default_content": "defaultContent",
        "default_threshold_type": "defaultThresholdType",
        "expressions": "expressions",
        "guid": "guid",
        "help_path": "helpPath",
        "is_range": "isRange",
        "name": "name",
        "type": "type",
        "unit": "unit",
    }

    subtype_mapping = {
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimUnit",
        "attributeParameters": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "expressions": "GrantaServerApiSchemaSlimEntitiesSlimExpression",
        "defaultContent": "GrantaServerApiSchemaAttributesMathsContent",
    }

    def __init__(
        self,
        *,
        about_attribute: "Optional[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]" = None,
        allow_all_compatible_expressions: "Optional[bool]" = None,
        allow_extrapolation: "Optional[bool]" = None,
        attribute_parameters: "Optional[List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]]" = None,
        axis_name: "Optional[str]" = None,
        default_content: "Optional[GrantaServerApiSchemaAttributesMathsContent]" = None,
        default_threshold_type: "Optional[GrantaServerApiSchemaAttributesAttributeThresholdType]" = None,
        expressions: "Optional[List[GrantaServerApiSchemaSlimEntitiesSlimExpression]]" = None,
        guid: "Optional[str]" = None,
        help_path: "Optional[str]" = None,
        is_range: "Optional[bool]" = None,
        name: "Optional[str]" = None,
        type: "str" = "mathsFunctional",
        unit: "Optional[GrantaServerApiSchemaSlimEntitiesSlimUnit]" = None,
    ) -> None:
        """GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute - a model defined in Swagger

        Parameters
        ----------
            about_attribute: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, optional
            allow_all_compatible_expressions: bool, optional
            allow_extrapolation: bool, optional
            attribute_parameters: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity], optional
            axis_name: str, optional
            default_content: GrantaServerApiSchemaAttributesMathsContent, optional
            default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType, optional
            expressions: List[GrantaServerApiSchemaSlimEntitiesSlimExpression], optional
            guid: str, optional
            help_path: str, optional
            is_range: bool, optional
            name: str, optional
            type: str
            unit: GrantaServerApiSchemaSlimEntitiesSlimUnit, optional
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
        self._unit = None
        self._attribute_parameters = None
        self._expressions = None
        self._allow_extrapolation = None
        self._is_range = None
        self._default_content = None
        self._allow_all_compatible_expressions = None
        self.discriminator = None
        self.type = type
        if unit is not None:
            self.unit = unit
        if attribute_parameters is not None:
            self.attribute_parameters = attribute_parameters
        if expressions is not None:
            self.expressions = expressions
        if allow_extrapolation is not None:
            self.allow_extrapolation = allow_extrapolation
        if is_range is not None:
            self.is_range = is_range
        if default_content is not None:
            self.default_content = default_content
        if allow_all_compatible_expressions is not None:
            self.allow_all_compatible_expressions = allow_all_compatible_expressions

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @property
    def unit(self) -> "GrantaServerApiSchemaSlimEntitiesSlimUnit":
        """Gets the unit of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimUnit
            The unit of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "GrantaServerApiSchemaSlimEntitiesSlimUnit") -> None:
        """Sets the unit of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Parameters
        ----------
        unit: GrantaServerApiSchemaSlimEntitiesSlimUnit
            The unit of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        self._unit = unit

    @property
    def attribute_parameters(
        self,
    ) -> "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]":
        """Gets the attribute_parameters of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The attribute_parameters of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        return self._attribute_parameters

    @attribute_parameters.setter
    def attribute_parameters(
        self,
        attribute_parameters: "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
    ) -> None:
        """Sets the attribute_parameters of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Parameters
        ----------
        attribute_parameters: list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The attribute_parameters of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        self._attribute_parameters = attribute_parameters

    @property
    def expressions(self) -> "list[GrantaServerApiSchemaSlimEntitiesSlimExpression]":
        """Gets the expressions of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimExpression]
            The expressions of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        return self._expressions

    @expressions.setter
    def expressions(
        self, expressions: "list[GrantaServerApiSchemaSlimEntitiesSlimExpression]"
    ) -> None:
        """Sets the expressions of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Parameters
        ----------
        expressions: list[GrantaServerApiSchemaSlimEntitiesSlimExpression]
            The expressions of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        self._expressions = expressions

    @property
    def allow_extrapolation(self) -> "bool":
        """Gets the allow_extrapolation of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Returns
        -------
        bool
            The allow_extrapolation of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        return self._allow_extrapolation

    @allow_extrapolation.setter
    def allow_extrapolation(self, allow_extrapolation: "bool") -> None:
        """Sets the allow_extrapolation of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Parameters
        ----------
        allow_extrapolation: bool
            The allow_extrapolation of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        self._allow_extrapolation = allow_extrapolation

    @property
    def is_range(self) -> "bool":
        """Gets the is_range of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Returns
        -------
        bool
            The is_range of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        return self._is_range

    @is_range.setter
    def is_range(self, is_range: "bool") -> None:
        """Sets the is_range of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Parameters
        ----------
        is_range: bool
            The is_range of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        self._is_range = is_range

    @property
    def default_content(self) -> "GrantaServerApiSchemaAttributesMathsContent":
        """Gets the default_content of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Returns
        -------
        GrantaServerApiSchemaAttributesMathsContent
            The default_content of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        return self._default_content

    @default_content.setter
    def default_content(
        self, default_content: "GrantaServerApiSchemaAttributesMathsContent"
    ) -> None:
        """Sets the default_content of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Parameters
        ----------
        default_content: GrantaServerApiSchemaAttributesMathsContent
            The default_content of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        self._default_content = default_content

    @property
    def allow_all_compatible_expressions(self) -> "bool":
        """Gets the allow_all_compatible_expressions of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Returns
        -------
        bool
            The allow_all_compatible_expressions of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        return self._allow_all_compatible_expressions

    @allow_all_compatible_expressions.setter
    def allow_all_compatible_expressions(
        self, allow_all_compatible_expressions: "bool"
    ) -> None:
        """Sets the allow_all_compatible_expressions of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Parameters
        ----------
        allow_all_compatible_expressions: bool
            The allow_all_compatible_expressions of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        self._allow_all_compatible_expressions = allow_all_compatible_expressions

    def get_real_child_model(self, data: ModelBase) -> str:
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

    def to_dict(self) -> Dict:
        """Returns the model properties as a dict

        Returns
        -------
        Dict
            Dictionary indexed by property name containing all the model properties
        """
        result = {}

        for attr in self.swagger_types.keys():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(
            GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute,
            dict,
        ):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model

        Returns
        -------
        str
            String representation of the model as a dictionary
        """
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(
            other,
            GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
