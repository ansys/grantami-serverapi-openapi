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

from ansys.grantami.serverapi_openapi.models.granta_server_api_search_attribute_criterion import (  # noqa: F401
    GrantaServerApiSearchAttributeCriterion,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiSearchAttributeExistsCriterion(GrantaServerApiSearchAttributeCriterion):
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
        "attribute_criterion_type": "str",
        "guid": "str",
        "identity": "int",
        "inner_criterion": "GrantaServerApiSearchDatumExistsCriterion",
        "is_meta_attribute": "bool",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "attribute_criterion_type": "attributeCriterionType",
        "guid": "guid",
        "identity": "identity",
        "inner_criterion": "innerCriterion",
        "is_meta_attribute": "isMetaAttribute",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {
        "innerCriterion": "GrantaServerApiSearchDatumExistsCriterion",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_criterion_type: "str" = "exists",
        guid: "Union[str, None, Unset_Type]" = Unset,
        identity: "Union[int, None, Unset_Type]" = Unset,
        inner_criterion: "Union[GrantaServerApiSearchDatumExistsCriterion, Unset_Type]" = Unset,
        is_meta_attribute: "Union[bool, Unset_Type]" = Unset,
        type: "str" = "attribute",
    ) -> None:
        """GrantaServerApiSearchAttributeExistsCriterion - a model defined in Swagger

        Parameters
        ----------
        attribute_criterion_type: str
        guid: str, optional
        identity: int, optional
        inner_criterion: GrantaServerApiSearchDatumExistsCriterion, optional
        is_meta_attribute: bool, optional
        type: str
        """
        super().__init__(
            guid=guid, identity=identity, is_meta_attribute=is_meta_attribute, type=type
        )
        self._inner_criterion: Union[GrantaServerApiSearchDatumExistsCriterion, Unset_Type] = Unset
        self._attribute_criterion_type: str

        if inner_criterion is not Unset:
            self.inner_criterion = inner_criterion
        self.attribute_criterion_type = attribute_criterion_type

    @property
    def inner_criterion(self) -> "Union[GrantaServerApiSearchDatumExistsCriterion, Unset_Type]":
        """Gets the inner_criterion of this GrantaServerApiSearchAttributeExistsCriterion.

        Returns
        -------
        Union[GrantaServerApiSearchDatumExistsCriterion, Unset_Type]
            The inner_criterion of this GrantaServerApiSearchAttributeExistsCriterion.
        """
        return self._inner_criterion

    @inner_criterion.setter
    def inner_criterion(
        self, inner_criterion: "Union[GrantaServerApiSearchDatumExistsCriterion, Unset_Type]"
    ) -> None:
        """Sets the inner_criterion of this GrantaServerApiSearchAttributeExistsCriterion.

        Parameters
        ----------
        inner_criterion: Union[GrantaServerApiSearchDatumExistsCriterion, Unset_Type]
            The inner_criterion of this GrantaServerApiSearchAttributeExistsCriterion.
        """
        # Field is not nullable
        if inner_criterion is None:
            raise ValueError("Invalid value for 'inner_criterion', must not be 'None'")
        self._inner_criterion = inner_criterion

    @property
    def attribute_criterion_type(self) -> "str":
        """Gets the attribute_criterion_type of this GrantaServerApiSearchAttributeExistsCriterion.

        Returns
        -------
        str
            The attribute_criterion_type of this GrantaServerApiSearchAttributeExistsCriterion.
        """
        return self._attribute_criterion_type

    @attribute_criterion_type.setter
    def attribute_criterion_type(self, attribute_criterion_type: "str") -> None:
        """Sets the attribute_criterion_type of this GrantaServerApiSearchAttributeExistsCriterion.

        Parameters
        ----------
        attribute_criterion_type: str
            The attribute_criterion_type of this GrantaServerApiSearchAttributeExistsCriterion.
        """
        # Field is not nullable
        if attribute_criterion_type is None:
            raise ValueError("Invalid value for 'attribute_criterion_type', must not be 'None'")
        # Field is required
        if attribute_criterion_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'attribute_criterion_type', must not be 'Unset'")
        self._attribute_criterion_type = attribute_criterion_type

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
        if not isinstance(other, GrantaServerApiSearchAttributeExistsCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
