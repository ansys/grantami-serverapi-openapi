# Copyright (C) 2023 - 2024 ANSYS, Inc. and/or its affiliates.
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
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, Union  # noqa: F401

from ansys.grantami.serverapi_openapi.models.gsa_attribute import GsaAttribute  # noqa: F401
from ansys.grantami.serverapi_openapi.models.gsa_attribute_type import GsaAttributeType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaDiscreteAttribute(GsaAttribute):
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
        "default_threshold_type": "GsaAttributeThresholdType",
        "discrete_type": "GsaSlimNamedEntity",
        "display_names": "dict(str, str)",
        "guid": "str",
        "info": "GsaAttributeInfo",
        "is_hidden_from_search_criteria": "bool",
        "is_multi_valued": "bool",
        "name": "str",
        "table": "GsaSlimEntity",
        "type": "GsaAttributeType",
        "about_attribute": "GsaSlimNamedEntity",
        "axis_name": "str",
        "help_path": "str",
    }

    attribute_map: Dict[str, str] = {
        "default_threshold_type": "defaultThresholdType",
        "discrete_type": "discreteType",
        "display_names": "displayNames",
        "guid": "guid",
        "info": "info",
        "is_hidden_from_search_criteria": "isHiddenFromSearchCriteria",
        "is_multi_valued": "isMultiValued",
        "name": "name",
        "table": "table",
        "type": "type",
        "about_attribute": "aboutAttribute",
        "axis_name": "axisName",
        "help_path": "helpPath",
    }

    subtype_mapping: Dict[str, str] = {
        "discreteType": "GsaSlimNamedEntity",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        default_threshold_type: "GsaAttributeThresholdType",
        discrete_type: "GsaSlimNamedEntity",
        display_names: "Dict[str, str]",
        guid: "str",
        info: "GsaAttributeInfo",
        is_hidden_from_search_criteria: "bool",
        is_multi_valued: "bool",
        name: "str",
        table: "GsaSlimEntity",
        type: "GsaAttributeType" = GsaAttributeType.DISCRETE,
        about_attribute: "Union[GsaSlimNamedEntity, Unset_Type]" = Unset,
        axis_name: "Union[str, None, Unset_Type]" = Unset,
        help_path: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaDiscreteAttribute - a model defined in Swagger

        Parameters
        ----------
        default_threshold_type: GsaAttributeThresholdType
        discrete_type: GsaSlimNamedEntity
        display_names: Dict[str, str]
        guid: str
        info: GsaAttributeInfo
        is_hidden_from_search_criteria: bool
        is_multi_valued: bool
        name: str
        table: GsaSlimEntity
        type: GsaAttributeType
        about_attribute: GsaSlimNamedEntity, optional
        axis_name: str, optional
        help_path: str, optional
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
        self._discrete_type: GsaSlimNamedEntity
        self._is_multi_valued: bool

        self.discrete_type = discrete_type
        self.is_multi_valued = is_multi_valued

    @property
    def discrete_type(self) -> "GsaSlimNamedEntity":
        """Gets the discrete_type of this GsaDiscreteAttribute.

        Returns
        -------
        GsaSlimNamedEntity
            The discrete_type of this GsaDiscreteAttribute.
        """
        return self._discrete_type

    @discrete_type.setter
    def discrete_type(self, discrete_type: "GsaSlimNamedEntity") -> None:
        """Sets the discrete_type of this GsaDiscreteAttribute.

        Parameters
        ----------
        discrete_type: GsaSlimNamedEntity
            The discrete_type of this GsaDiscreteAttribute.
        """
        # Field is not nullable
        if discrete_type is None:
            raise ValueError("Invalid value for 'discrete_type', must not be 'None'")
        # Field is required
        if discrete_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'discrete_type', must not be 'Unset'")
        self._discrete_type = discrete_type

    @property
    def is_multi_valued(self) -> "bool":
        """Gets the is_multi_valued of this GsaDiscreteAttribute.

        Returns
        -------
        bool
            The is_multi_valued of this GsaDiscreteAttribute.
        """
        return self._is_multi_valued

    @is_multi_valued.setter
    def is_multi_valued(self, is_multi_valued: "bool") -> None:
        """Sets the is_multi_valued of this GsaDiscreteAttribute.

        Parameters
        ----------
        is_multi_valued: bool
            The is_multi_valued of this GsaDiscreteAttribute.
        """
        # Field is not nullable
        if is_multi_valued is None:
            raise ValueError("Invalid value for 'is_multi_valued', must not be 'None'")
        # Field is required
        if is_multi_valued is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'is_multi_valued', must not be 'Unset'")
        self._is_multi_valued = is_multi_valued

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
        if not isinstance(other, GsaDiscreteAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other