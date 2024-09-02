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

from ansys.grantami.serverapi_openapi.models.gsa_datum_criterion import (  # noqa: F401
    GsaDatumCriterion,
)
from ansys.grantami.serverapi_openapi.models.gsa_datum_criterion_type import GsaDatumCriterionType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaDiscreteFunctionalValuesDatumCriterion(GsaDatumCriterion):
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
        "type": "GsaDatumCriterionType",
        "any_guids": "list[str]",
        "any_identities": "list[int]",
        "constraints": "list[GsaParameterConstraint]",
    }

    attribute_map: Dict[str, str] = {
        "type": "type",
        "any_guids": "anyGuids",
        "any_identities": "anyIdentities",
        "constraints": "constraints",
    }

    subtype_mapping: Dict[str, str] = {
        "constraints": "GsaParameterConstraint",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        type: "GsaDatumCriterionType" = GsaDatumCriterionType.DISCRETEFUNCTIONALVALUES,
        any_guids: "Union[List[str], None, Unset_Type]" = Unset,
        any_identities: "Union[List[int], None, Unset_Type]" = Unset,
        constraints: "Union[List[GsaParameterConstraint], None, Unset_Type]" = Unset,
    ) -> None:
        """GsaDiscreteFunctionalValuesDatumCriterion - a model defined in Swagger

        Parameters
        ----------
        type: GsaDatumCriterionType
        any_guids: List[str], optional
        any_identities: List[int], optional
        constraints: List[GsaParameterConstraint], optional
        """
        super().__init__(type=type)
        self._any_identities: Union[List[int], None, Unset_Type] = Unset
        self._any_guids: Union[List[str], None, Unset_Type] = Unset
        self._constraints: Union[List[GsaParameterConstraint], None, Unset_Type] = Unset

        if any_identities is not Unset:
            self.any_identities = any_identities
        if any_guids is not Unset:
            self.any_guids = any_guids
        if constraints is not Unset:
            self.constraints = constraints

    @property
    def any_identities(self) -> "Union[List[int], None, Unset_Type]":
        """Gets the any_identities of this GsaDiscreteFunctionalValuesDatumCriterion.
        Match any of these discrete type identities

        Returns
        -------
        Union[List[int], None, Unset_Type]
            The any_identities of this GsaDiscreteFunctionalValuesDatumCriterion.
        """
        return self._any_identities

    @any_identities.setter
    def any_identities(self, any_identities: "Union[List[int], None, Unset_Type]") -> None:
        """Sets the any_identities of this GsaDiscreteFunctionalValuesDatumCriterion.
        Match any of these discrete type identities

        Parameters
        ----------
        any_identities: Union[List[int], None, Unset_Type]
            The any_identities of this GsaDiscreteFunctionalValuesDatumCriterion.
        """
        self._any_identities = any_identities

    @property
    def any_guids(self) -> "Union[List[str], None, Unset_Type]":
        """Gets the any_guids of this GsaDiscreteFunctionalValuesDatumCriterion.
        Match any of these discrete type GUIDs

        Returns
        -------
        Union[List[str], None, Unset_Type]
            The any_guids of this GsaDiscreteFunctionalValuesDatumCriterion.
        """
        return self._any_guids

    @any_guids.setter
    def any_guids(self, any_guids: "Union[List[str], None, Unset_Type]") -> None:
        """Sets the any_guids of this GsaDiscreteFunctionalValuesDatumCriterion.
        Match any of these discrete type GUIDs

        Parameters
        ----------
        any_guids: Union[List[str], None, Unset_Type]
            The any_guids of this GsaDiscreteFunctionalValuesDatumCriterion.
        """
        self._any_guids = any_guids

    @property
    def constraints(self) -> "Union[List[GsaParameterConstraint], None, Unset_Type]":
        """Gets the constraints of this GsaDiscreteFunctionalValuesDatumCriterion.
        Constraints on the parameters of the attribute. Unspecified parameters will be assumed to be unconstrained.

        Returns
        -------
        Union[List[GsaParameterConstraint], None, Unset_Type]
            The constraints of this GsaDiscreteFunctionalValuesDatumCriterion.
        """
        return self._constraints

    @constraints.setter
    def constraints(
        self, constraints: "Union[List[GsaParameterConstraint], None, Unset_Type]"
    ) -> None:
        """Sets the constraints of this GsaDiscreteFunctionalValuesDatumCriterion.
        Constraints on the parameters of the attribute. Unspecified parameters will be assumed to be unconstrained.

        Parameters
        ----------
        constraints: Union[List[GsaParameterConstraint], None, Unset_Type]
            The constraints of this GsaDiscreteFunctionalValuesDatumCriterion.
        """
        self._constraints = constraints

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
        if not isinstance(other, GsaDiscreteFunctionalValuesDatumCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
