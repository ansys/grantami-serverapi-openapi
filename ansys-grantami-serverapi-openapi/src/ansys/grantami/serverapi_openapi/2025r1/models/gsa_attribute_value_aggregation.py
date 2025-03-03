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

from ansys.grantami.serverapi_openapi.2025r1.models.gsa_aggregation_type import GsaAggregationType
from ansys.grantami.serverapi_openapi.2025r1.models.gsa_attribute_aggregation import (  # noqa: F401
    GsaAttributeAggregation,
)
from ansys.grantami.serverapi_openapi.2025r1.models.gsa_attribute_aggregation_type import (
    GsaAttributeAggregationType,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaAttributeValueAggregation(GsaAttributeAggregation):
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
        "attribute_aggregation_type": "GsaAttributeAggregationType",
        "type": "GsaAggregationType",
        "aggregation_datum": "GsaAggregationDatum",
        "attribute_guid": "str",
        "attribute_identity": "int",
        "count": "int",
    }

    attribute_map: dict[str, str] = {
        "attribute_aggregation_type": "attributeAggregationType",
        "type": "type",
        "aggregation_datum": "aggregationDatum",
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "count": "count",
    }

    subtype_mapping: dict[str, str] = {
        "aggregationDatum": "GsaAggregationDatum",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, attribute_aggregation_type: "GsaAttributeAggregationType" = GsaAttributeAggregationType.VALUE, type: "GsaAggregationType" = GsaAggregationType.ATTRIBUTE, aggregation_datum: "Union[GsaAggregationDatum, Unset_Type]" = Unset, attribute_guid: "Union[str, None, Unset_Type]" = Unset, attribute_identity: "Union[int, None, Unset_Type]" = Unset, count: "Union[int, Unset_Type]" = Unset,) -> None:
        """GsaAttributeValueAggregation - a model defined in Swagger

        Parameters
        ----------
        attribute_aggregation_type: GsaAttributeAggregationType
        type: GsaAggregationType
        aggregation_datum: GsaAggregationDatum, optional
        attribute_guid: str, optional
        attribute_identity: int, optional
        count: int, optional
        """
        super().__init__(attribute_aggregation_type=attribute_aggregation_type, type=type, attribute_guid=attribute_guid, attribute_identity=attribute_identity, count=count)
        self._aggregation_datum: Union[GsaAggregationDatum, Unset_Type] = Unset

        if aggregation_datum is not Unset:
            self.aggregation_datum = aggregation_datum

    @property
    def aggregation_datum(self) -> "Union[GsaAggregationDatum, Unset_Type]":
        """Gets the aggregation_datum of this GsaAttributeValueAggregation.

        Returns
        -------
        Union[GsaAggregationDatum, Unset_Type]
            The aggregation_datum of this GsaAttributeValueAggregation.
        """
        return self._aggregation_datum

    @aggregation_datum.setter
    def aggregation_datum(self, aggregation_datum: "Union[GsaAggregationDatum, Unset_Type]") -> None:
        """Sets the aggregation_datum of this GsaAttributeValueAggregation.

        Parameters
        ----------
        aggregation_datum: Union[GsaAggregationDatum, Unset_Type]
            The aggregation_datum of this GsaAttributeValueAggregation.
        """
        # Field is not nullable
        if aggregation_datum is None:
            raise ValueError("Invalid value for 'aggregation_datum', must not be 'None'")
        self._aggregation_datum = aggregation_datum

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
        if not isinstance(other, GsaAttributeValueAggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

