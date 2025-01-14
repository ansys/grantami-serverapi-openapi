"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.models.gsa_update_attribute import GsaUpdateAttribute  # noqa: F401
from ansys.grantami.serverapi_openapi.models.gsa_attribute_type import GsaAttributeType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaUpdateShortTextAttribute(GsaUpdateAttribute):
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
        "type": "GsaAttributeType",
        "about_attribute": "GsaSlimEntity",
        "axis_name": "GsaUpdateAxisName",
        "data_rule": "GsaSlimEntity",
        "default_threshold_type": "GsaAttributeThresholdType",
        "guid": "str",
        "help_path": "str",
        "is_hidden_from_search_criteria": "bool",
        "is_unique": "bool",
        "name": "str",
    }

    attribute_map: dict[str, str] = {
        "type": "type",
        "about_attribute": "aboutAttribute",
        "axis_name": "axisName",
        "data_rule": "dataRule",
        "default_threshold_type": "defaultThresholdType",
        "guid": "guid",
        "help_path": "helpPath",
        "is_hidden_from_search_criteria": "isHiddenFromSearchCriteria",
        "is_unique": "isUnique",
        "name": "name",
    }

    subtype_mapping: dict[str, str] = {
        "dataRule": "GsaSlimEntity",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, type: "GsaAttributeType" = GsaAttributeType.SHORTTEXT, about_attribute: "Union[GsaSlimEntity, Unset_Type]" = Unset, axis_name: "Union[GsaUpdateAxisName, Unset_Type]" = Unset, data_rule: "Union[GsaSlimEntity, Unset_Type]" = Unset, default_threshold_type: "Union[GsaAttributeThresholdType, Unset_Type]" = Unset, guid: "Union[str, Unset_Type]" = Unset, help_path: "Union[str, None, Unset_Type]" = Unset, is_hidden_from_search_criteria: "Union[bool, None, Unset_Type]" = Unset, is_unique: "Union[bool, Unset_Type]" = Unset, name: "Union[str, Unset_Type]" = Unset,) -> None:
        """GsaUpdateShortTextAttribute - a model defined in Swagger

        Parameters
        ----------
        type: GsaAttributeType
        about_attribute: GsaSlimEntity, optional
        axis_name: GsaUpdateAxisName, optional
        data_rule: GsaSlimEntity, optional
        default_threshold_type: GsaAttributeThresholdType, optional
        guid: str, optional
        help_path: str, optional
        is_hidden_from_search_criteria: bool, optional
        is_unique: bool, optional
        name: str, optional
        """
        super().__init__(type=type, about_attribute=about_attribute, axis_name=axis_name, default_threshold_type=default_threshold_type, guid=guid, help_path=help_path, is_hidden_from_search_criteria=is_hidden_from_search_criteria, name=name)
        self._is_unique: Union[bool, Unset_Type] = Unset
        self._data_rule: Union[GsaSlimEntity, Unset_Type] = Unset

        if is_unique is not Unset:
            self.is_unique = is_unique
        if data_rule is not Unset:
            self.data_rule = data_rule

    @property
    def is_unique(self) -> "Union[bool, Unset_Type]":
        """Gets the is_unique of this GsaUpdateShortTextAttribute.
        Whether or not the attribute is constrained to contain a unique value

        Returns
        -------
        Union[bool, Unset_Type]
            The is_unique of this GsaUpdateShortTextAttribute.
        """
        return self._is_unique

    @is_unique.setter
    def is_unique(self, is_unique: "Union[bool, Unset_Type]") -> None:
        """Sets the is_unique of this GsaUpdateShortTextAttribute.
        Whether or not the attribute is constrained to contain a unique value

        Parameters
        ----------
        is_unique: Union[bool, Unset_Type]
            The is_unique of this GsaUpdateShortTextAttribute.
        """
        # Field is not nullable
        if is_unique is None:
            raise ValueError("Invalid value for 'is_unique', must not be 'None'")
        self._is_unique = is_unique

    @property
    def data_rule(self) -> "Union[GsaSlimEntity, Unset_Type]":
        """Gets the data_rule of this GsaUpdateShortTextAttribute.

        Returns
        -------
        Union[GsaSlimEntity, Unset_Type]
            The data_rule of this GsaUpdateShortTextAttribute.
        """
        return self._data_rule

    @data_rule.setter
    def data_rule(self, data_rule: "Union[GsaSlimEntity, Unset_Type]") -> None:
        """Sets the data_rule of this GsaUpdateShortTextAttribute.

        Parameters
        ----------
        data_rule: Union[GsaSlimEntity, Unset_Type]
            The data_rule of this GsaUpdateShortTextAttribute.
        """
        # Field is not nullable
        if data_rule is None:
            raise ValueError("Invalid value for 'data_rule', must not be 'None'")
        self._data_rule = data_rule

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
        if not isinstance(other, GsaUpdateShortTextAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

