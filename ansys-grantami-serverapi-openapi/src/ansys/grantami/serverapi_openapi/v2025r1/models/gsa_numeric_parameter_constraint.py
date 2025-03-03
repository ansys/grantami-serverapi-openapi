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

from ansys.grantami.serverapi_openapi.v2025r1.models.gsa_parameter_constraint import (  # noqa: F401
    GsaParameterConstraint,
)
from ansys.grantami.serverapi_openapi.v2025r1.models.gsa_parameter_constraint_type import (
    GsaParameterConstraintType,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaNumericParameterConstraint(GsaParameterConstraint):
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
        "parameter": "GsaObjectIdentifier",
        "type": "GsaParameterConstraintType",
        "gte": "float",
        "lte": "float",
        "significant_figures": "int",
    }

    attribute_map: dict[str, str] = {
        "parameter": "parameter",
        "type": "type",
        "gte": "gte",
        "lte": "lte",
        "significant_figures": "significantFigures",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        parameter: "GsaObjectIdentifier",
        type: "GsaParameterConstraintType" = GsaParameterConstraintType.NUMERIC,
        gte: "Union[float, None, Unset_Type]" = Unset,
        lte: "Union[float, None, Unset_Type]" = Unset,
        significant_figures: "Union[int, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaNumericParameterConstraint - a model defined in Swagger

        Parameters
        ----------
        parameter: GsaObjectIdentifier
        type: GsaParameterConstraintType
        gte: float, optional
        lte: float, optional
        significant_figures: int, optional
        """
        super().__init__(parameter=parameter, type=type)
        self._gte: Union[float, None, Unset_Type] = Unset
        self._lte: Union[float, None, Unset_Type] = Unset
        self._significant_figures: Union[int, None, Unset_Type] = Unset

        if gte is not Unset:
            self.gte = gte
        if lte is not Unset:
            self.lte = lte
        if significant_figures is not Unset:
            self.significant_figures = significant_figures

    @property
    def gte(self) -> "Union[float, None, Unset_Type]":
        """Gets the gte of this GsaNumericParameterConstraint.

        Returns
        -------
        Union[float, None, Unset_Type]
            The gte of this GsaNumericParameterConstraint.
        """
        return self._gte

    @gte.setter
    def gte(self, gte: "Union[float, None, Unset_Type]") -> None:
        """Sets the gte of this GsaNumericParameterConstraint.

        Parameters
        ----------
        gte: Union[float, None, Unset_Type]
            The gte of this GsaNumericParameterConstraint.
        """
        self._gte = gte

    @property
    def lte(self) -> "Union[float, None, Unset_Type]":
        """Gets the lte of this GsaNumericParameterConstraint.

        Returns
        -------
        Union[float, None, Unset_Type]
            The lte of this GsaNumericParameterConstraint.
        """
        return self._lte

    @lte.setter
    def lte(self, lte: "Union[float, None, Unset_Type]") -> None:
        """Sets the lte of this GsaNumericParameterConstraint.

        Parameters
        ----------
        lte: Union[float, None, Unset_Type]
            The lte of this GsaNumericParameterConstraint.
        """
        self._lte = lte

    @property
    def significant_figures(self) -> "Union[int, None, Unset_Type]":
        """Gets the significant_figures of this GsaNumericParameterConstraint.

        Returns
        -------
        Union[int, None, Unset_Type]
            The significant_figures of this GsaNumericParameterConstraint.
        """
        return self._significant_figures

    @significant_figures.setter
    def significant_figures(self, significant_figures: "Union[int, None, Unset_Type]") -> None:
        """Sets the significant_figures of this GsaNumericParameterConstraint.

        Parameters
        ----------
        significant_figures: Union[int, None, Unset_Type]
            The significant_figures of this GsaNumericParameterConstraint.
        """
        self._significant_figures = significant_figures

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
        if not isinstance(other, GsaNumericParameterConstraint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
