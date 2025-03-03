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

from ansys.grantami.serverapi_openapi.v2025r1.models.gsa_criterion_type import GsaCriterionType
from ansys.grantami.serverapi_openapi.v2025r1.models.gsa_local_column_criterion import (  # noqa: F401
    GsaLocalColumnCriterion,
)
from ansys.grantami.serverapi_openapi.v2025r1.models.gsa_local_column_criterion_type import (
    GsaLocalColumnCriterionType,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaLocalColumnExistsCriterion(GsaLocalColumnCriterion):
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
        "inner_criterion": "GsaDatumExistsCriterion",
        "local_column_criterion_type": "GsaLocalColumnCriterionType",
        "type": "GsaCriterionType",
        "guid": "str",
        "identity": "int",
    }

    attribute_map: dict[str, str] = {
        "inner_criterion": "innerCriterion",
        "local_column_criterion_type": "localColumnCriterionType",
        "type": "type",
        "guid": "guid",
        "identity": "identity",
    }

    subtype_mapping: dict[str, str] = {
        "innerCriterion": "GsaDatumExistsCriterion",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        inner_criterion: "GsaDatumExistsCriterion",
        local_column_criterion_type: "GsaLocalColumnCriterionType" = GsaLocalColumnCriterionType.EXISTS,
        type: "GsaCriterionType" = GsaCriterionType.LOCALCOLUMN,
        guid: "Union[str, None, Unset_Type]" = Unset,
        identity: "Union[int, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaLocalColumnExistsCriterion - a model defined in Swagger

        Parameters
        ----------
        inner_criterion: GsaDatumExistsCriterion
        local_column_criterion_type: GsaLocalColumnCriterionType
        type: GsaCriterionType
        guid: str, optional
        identity: int, optional
        """
        super().__init__(
            local_column_criterion_type=local_column_criterion_type,
            type=type,
            guid=guid,
            identity=identity,
        )
        self._inner_criterion: GsaDatumExistsCriterion

        self.inner_criterion = inner_criterion

    @property
    def inner_criterion(self) -> "GsaDatumExistsCriterion":
        """Gets the inner_criterion of this GsaLocalColumnExistsCriterion.

        Returns
        -------
        GsaDatumExistsCriterion
            The inner_criterion of this GsaLocalColumnExistsCriterion.
        """
        return self._inner_criterion

    @inner_criterion.setter
    def inner_criterion(self, inner_criterion: "GsaDatumExistsCriterion") -> None:
        """Sets the inner_criterion of this GsaLocalColumnExistsCriterion.

        Parameters
        ----------
        inner_criterion: GsaDatumExistsCriterion
            The inner_criterion of this GsaLocalColumnExistsCriterion.
        """
        # Field is not nullable
        if inner_criterion is None:
            raise ValueError("Invalid value for 'inner_criterion', must not be 'None'")
        # Field is required
        if inner_criterion is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'inner_criterion', must not be 'Unset'")
        self._inner_criterion = inner_criterion

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
        if not isinstance(other, GsaLocalColumnExistsCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
