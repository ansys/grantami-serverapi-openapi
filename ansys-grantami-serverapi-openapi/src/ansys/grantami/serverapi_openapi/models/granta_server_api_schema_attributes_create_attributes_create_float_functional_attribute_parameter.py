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


class GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter(
    ModelBase
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
        "parameter": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "default_value": "float",
        "interpolation_method": "GrantaServerApiSchemaAttributesAttributeInterpolationMethod",
        "scale_type": "GrantaServerApiSchemaAttributesAttributeScaleType",
    }

    attribute_map: Dict[str, str] = {
        "parameter": "parameter",
        "default_value": "defaultValue",
        "interpolation_method": "interpolationMethod",
        "scale_type": "scaleType",
    }

    subtype_mapping: Dict[str, str] = {
        "parameter": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "interpolationMethod": "GrantaServerApiSchemaAttributesAttributeInterpolationMethod",
        "scaleType": "GrantaServerApiSchemaAttributesAttributeScaleType",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        parameter: "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        default_value: "Union[float, None, Unset_Type]" = Unset,
        interpolation_method: "Union[GrantaServerApiSchemaAttributesAttributeInterpolationMethod, Unset_Type]" = Unset,
        scale_type: "Union[GrantaServerApiSchemaAttributesAttributeScaleType, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter - a model defined in Swagger

        Parameters
        ----------
        parameter: GrantaServerApiSchemaSlimEntitiesSlimEntity
        default_value: float, optional
        interpolation_method: GrantaServerApiSchemaAttributesAttributeInterpolationMethod, optional
        scale_type: GrantaServerApiSchemaAttributesAttributeScaleType, optional
        """
        self._parameter: GrantaServerApiSchemaSlimEntitiesSlimEntity
        self._default_value: Union[float, None, Unset_Type] = Unset
        self._interpolation_method: Union[
            GrantaServerApiSchemaAttributesAttributeInterpolationMethod, Unset_Type
        ] = Unset
        self._scale_type: Union[
            GrantaServerApiSchemaAttributesAttributeScaleType, Unset_Type
        ] = Unset

        self.parameter = parameter
        if default_value is not Unset:
            self.default_value = default_value
        if interpolation_method is not Unset:
            self.interpolation_method = interpolation_method
        if scale_type is not Unset:
            self.scale_type = scale_type

    @property
    def parameter(self) -> "GrantaServerApiSchemaSlimEntitiesSlimEntity":
        """Gets the parameter of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimEntity
            The parameter of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter.
        """
        return self._parameter

    @parameter.setter
    def parameter(
        self, parameter: "GrantaServerApiSchemaSlimEntitiesSlimEntity"
    ) -> None:
        """Sets the parameter of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter.

        Parameters
        ----------
        parameter: GrantaServerApiSchemaSlimEntitiesSlimEntity
            The parameter of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter.
        """
        # Field is not nullable
        if parameter is None:
            raise ValueError("Invalid value for 'parameter', must not be 'None'")
        # Field is required
        if parameter is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'parameter', must not be 'Unset'")
        self._parameter = parameter

    @property
    def default_value(self) -> "Union[float, None, Unset_Type]":
        """Gets the default_value of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter.

        Returns
        -------
        Union[float, None, Unset_Type]
            The default_value of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter.
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value: "Union[float, None, Unset_Type]") -> None:
        """Sets the default_value of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter.

        Parameters
        ----------
        default_value: Union[float, None, Unset_Type]
            The default_value of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter.
        """
        self._default_value = default_value

    @property
    def interpolation_method(
        self,
    ) -> (
        "Union[GrantaServerApiSchemaAttributesAttributeInterpolationMethod, Unset_Type]"
    ):
        """Gets the interpolation_method of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter.

        Returns
        -------
        Union[GrantaServerApiSchemaAttributesAttributeInterpolationMethod, Unset_Type]
            The interpolation_method of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter.
        """
        return self._interpolation_method

    @interpolation_method.setter
    def interpolation_method(
        self,
        interpolation_method: "Union[GrantaServerApiSchemaAttributesAttributeInterpolationMethod, Unset_Type]",
    ) -> None:
        """Sets the interpolation_method of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter.

        Parameters
        ----------
        interpolation_method: Union[GrantaServerApiSchemaAttributesAttributeInterpolationMethod, Unset_Type]
            The interpolation_method of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter.
        """
        # Field is not nullable
        if interpolation_method is None:
            raise ValueError(
                "Invalid value for 'interpolation_method', must not be 'None'"
            )
        self._interpolation_method = interpolation_method

    @property
    def scale_type(
        self,
    ) -> "Union[GrantaServerApiSchemaAttributesAttributeScaleType, Unset_Type]":
        """Gets the scale_type of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter.

        Returns
        -------
        Union[GrantaServerApiSchemaAttributesAttributeScaleType, Unset_Type]
            The scale_type of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter.
        """
        return self._scale_type

    @scale_type.setter
    def scale_type(
        self,
        scale_type: "Union[GrantaServerApiSchemaAttributesAttributeScaleType, Unset_Type]",
    ) -> None:
        """Sets the scale_type of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter.

        Parameters
        ----------
        scale_type: Union[GrantaServerApiSchemaAttributesAttributeScaleType, Unset_Type]
            The scale_type of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter.
        """
        # Field is not nullable
        if scale_type is None:
            raise ValueError("Invalid value for 'scale_type', must not be 'None'")
        self._scale_type = scale_type

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
            other,
            GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
