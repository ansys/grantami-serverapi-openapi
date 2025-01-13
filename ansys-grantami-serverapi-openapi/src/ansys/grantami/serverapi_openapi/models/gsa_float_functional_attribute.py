# Copyright (C) 2023 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from ansys.grantami.serverapi_openapi.models.gsa_attribute import GsaAttribute  # noqa: F401
from ansys.grantami.serverapi_openapi.models.gsa_attribute_type import GsaAttributeType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaFloatFunctionalAttribute(GsaAttribute):
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
        "attribute_parameters": "list[GsaFloatFunctionalAttributeParameter]",
        "default_threshold_type": "GsaAttributeThresholdType",
        "display_names": "dict(str, str)",
        "guid": "str",
        "info": "GsaAttributeInfo",
        "is_hidden_from_search_criteria": "bool",
        "is_range": "bool",
        "name": "str",
        "table": "GsaSlimEntity",
        "type": "GsaAttributeType",
        "about_attribute": "GsaSlimTypedAttribute",
        "axis_name": "GsaAxisName",
        "help_path": "str",
        "unit": "GsaSlimUnit",
    }

    attribute_map: dict[str, str] = {
        "attribute_parameters": "attributeParameters",
        "default_threshold_type": "defaultThresholdType",
        "display_names": "displayNames",
        "guid": "guid",
        "info": "info",
        "is_hidden_from_search_criteria": "isHiddenFromSearchCriteria",
        "is_range": "isRange",
        "name": "name",
        "table": "table",
        "type": "type",
        "about_attribute": "aboutAttribute",
        "axis_name": "axisName",
        "help_path": "helpPath",
        "unit": "unit",
    }

    subtype_mapping: dict[str, str] = {
        "unit": "GsaSlimUnit",
        "attributeParameters": "GsaFloatFunctionalAttributeParameter",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_parameters: "list[GsaFloatFunctionalAttributeParameter]",
        default_threshold_type: "GsaAttributeThresholdType",
        display_names: "dict[str, str]",
        guid: "str",
        info: "GsaAttributeInfo",
        is_hidden_from_search_criteria: "bool",
        is_range: "bool",
        name: "str",
        table: "GsaSlimEntity",
        type: "GsaAttributeType" = GsaAttributeType.FLOATFUNCTIONAL,
        about_attribute: "Union[GsaSlimTypedAttribute, Unset_Type]" = Unset,
        axis_name: "Union[GsaAxisName, Unset_Type]" = Unset,
        help_path: "Union[str, None, Unset_Type]" = Unset,
        unit: "Union[GsaSlimUnit, Unset_Type]" = Unset,
    ) -> None:
        """GsaFloatFunctionalAttribute - a model defined in Swagger

        Parameters
        ----------
        attribute_parameters: list[GsaFloatFunctionalAttributeParameter]
        default_threshold_type: GsaAttributeThresholdType
        display_names: dict[str, str]
        guid: str
        info: GsaAttributeInfo
        is_hidden_from_search_criteria: bool
        is_range: bool
        name: str
        table: GsaSlimEntity
        type: GsaAttributeType
        about_attribute: GsaSlimTypedAttribute, optional
        axis_name: GsaAxisName, optional
        help_path: str, optional
        unit: GsaSlimUnit, optional
        """
        super().__init__(
            default_threshold_type=default_threshold_type,
            display_names=display_names,
            guid=guid,
            info=info,
            is_hidden_from_search_criteria=is_hidden_from_search_criteria,
            name=name,
            table=table,
            type=type,
            about_attribute=about_attribute,
            axis_name=axis_name,
            help_path=help_path,
        )
        self._unit: Union[GsaSlimUnit, Unset_Type] = Unset
        self._attribute_parameters: list[GsaFloatFunctionalAttributeParameter]
        self._is_range: bool

        if unit is not Unset:
            self.unit = unit
        self.attribute_parameters = attribute_parameters
        self.is_range = is_range

    @property
    def unit(self) -> "Union[GsaSlimUnit, Unset_Type]":
        """Gets the unit of this GsaFloatFunctionalAttribute.

        Returns
        -------
        Union[GsaSlimUnit, Unset_Type]
            The unit of this GsaFloatFunctionalAttribute.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "Union[GsaSlimUnit, Unset_Type]") -> None:
        """Sets the unit of this GsaFloatFunctionalAttribute.

        Parameters
        ----------
        unit: Union[GsaSlimUnit, Unset_Type]
            The unit of this GsaFloatFunctionalAttribute.
        """
        # Field is not nullable
        if unit is None:
            raise ValueError("Invalid value for 'unit', must not be 'None'")
        self._unit = unit

    @property
    def attribute_parameters(self) -> "list[GsaFloatFunctionalAttributeParameter]":
        """Gets the attribute_parameters of this GsaFloatFunctionalAttribute.

        Returns
        -------
        list[GsaFloatFunctionalAttributeParameter]
            The attribute_parameters of this GsaFloatFunctionalAttribute.
        """
        return self._attribute_parameters

    @attribute_parameters.setter
    def attribute_parameters(
        self, attribute_parameters: "list[GsaFloatFunctionalAttributeParameter]"
    ) -> None:
        """Sets the attribute_parameters of this GsaFloatFunctionalAttribute.

        Parameters
        ----------
        attribute_parameters: list[GsaFloatFunctionalAttributeParameter]
            The attribute_parameters of this GsaFloatFunctionalAttribute.
        """
        # Field is not nullable
        if attribute_parameters is None:
            raise ValueError("Invalid value for 'attribute_parameters', must not be 'None'")
        # Field is required
        if attribute_parameters is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'attribute_parameters', must not be 'Unset'")
        self._attribute_parameters = attribute_parameters

    @property
    def is_range(self) -> "bool":
        """Gets the is_range of this GsaFloatFunctionalAttribute.

        Returns
        -------
        bool
            The is_range of this GsaFloatFunctionalAttribute.
        """
        return self._is_range

    @is_range.setter
    def is_range(self, is_range: "bool") -> None:
        """Sets the is_range of this GsaFloatFunctionalAttribute.

        Parameters
        ----------
        is_range: bool
            The is_range of this GsaFloatFunctionalAttribute.
        """
        # Field is not nullable
        if is_range is None:
            raise ValueError("Invalid value for 'is_range', must not be 'None'")
        # Field is required
        if is_range is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'is_range', must not be 'Unset'")
        self._is_range = is_range

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
        if not isinstance(other, GsaFloatFunctionalAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
