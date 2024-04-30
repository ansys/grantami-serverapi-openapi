# Copyright (C) 2021 - 2024 ANSYS, Inc. and/or its affiliates.
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

from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_parameters_parameter_content import (  # noqa: F401
    GrantaServerApiSchemaParametersParameterContent,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiSchemaParametersDiscreteParameterContent(
    GrantaServerApiSchemaParametersParameterContent
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
        "parameter": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "parameter_range": "GrantaServerApiSchemaParametersDiscreteRange",
        "parameter_value": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "parameter": "parameter",
        "parameter_range": "parameterRange",
        "parameter_value": "parameterValue",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {
        "parameterValue": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "parameterRange": "GrantaServerApiSchemaParametersDiscreteRange",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        parameter: "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        parameter_range: "GrantaServerApiSchemaParametersDiscreteRange",
        parameter_value: "Union[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, Unset_Type]" = Unset,
        type: "str" = "discrete",
    ) -> None:
        """GrantaServerApiSchemaParametersDiscreteParameterContent - a model defined in Swagger

        Parameters
        ----------
        parameter: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
        parameter_range: GrantaServerApiSchemaParametersDiscreteRange
        parameter_value: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, optional
        type: str
        """
        super().__init__(parameter=parameter)
        self._type: str
        self._parameter_value: Union[
            GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, Unset_Type
        ] = Unset
        self._parameter_range: GrantaServerApiSchemaParametersDiscreteRange

        self.type = type
        if parameter_value is not Unset:
            self.parameter_value = parameter_value
        self.parameter_range = parameter_range

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaParametersDiscreteParameterContent.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaParametersDiscreteParameterContent.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaParametersDiscreteParameterContent.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaParametersDiscreteParameterContent.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

    @property
    def parameter_value(
        self,
    ) -> "Union[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, Unset_Type]":
        """Gets the parameter_value of this GrantaServerApiSchemaParametersDiscreteParameterContent.

        Returns
        -------
        Union[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, Unset_Type]
            The parameter_value of this GrantaServerApiSchemaParametersDiscreteParameterContent.
        """
        return self._parameter_value

    @parameter_value.setter
    def parameter_value(
        self, parameter_value: "Union[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, Unset_Type]"
    ) -> None:
        """Sets the parameter_value of this GrantaServerApiSchemaParametersDiscreteParameterContent.

        Parameters
        ----------
        parameter_value: Union[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, Unset_Type]
            The parameter_value of this GrantaServerApiSchemaParametersDiscreteParameterContent.
        """
        # Field is not nullable
        if parameter_value is None:
            raise ValueError("Invalid value for 'parameter_value', must not be 'None'")
        self._parameter_value = parameter_value

    @property
    def parameter_range(self) -> "GrantaServerApiSchemaParametersDiscreteRange":
        """Gets the parameter_range of this GrantaServerApiSchemaParametersDiscreteParameterContent.

        Returns
        -------
        GrantaServerApiSchemaParametersDiscreteRange
            The parameter_range of this GrantaServerApiSchemaParametersDiscreteParameterContent.
        """
        return self._parameter_range

    @parameter_range.setter
    def parameter_range(
        self, parameter_range: "GrantaServerApiSchemaParametersDiscreteRange"
    ) -> None:
        """Sets the parameter_range of this GrantaServerApiSchemaParametersDiscreteParameterContent.

        Parameters
        ----------
        parameter_range: GrantaServerApiSchemaParametersDiscreteRange
            The parameter_range of this GrantaServerApiSchemaParametersDiscreteParameterContent.
        """
        # Field is not nullable
        if parameter_range is None:
            raise ValueError("Invalid value for 'parameter_range', must not be 'None'")
        # Field is required
        if parameter_range is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'parameter_range', must not be 'Unset'")
        self._parameter_range = parameter_range

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
        if not isinstance(other, GrantaServerApiSchemaParametersDiscreteParameterContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
