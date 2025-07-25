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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional  # noqa: F401

from ansys.grantami.serverapi_openapi.v2024r2.models.granta_server_api_aggregations_aggregation import (  # noqa: F401
    GrantaServerApiAggregationsAggregation,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiAggregationsAttributeAggregation(GrantaServerApiAggregationsAggregation):
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
    discriminator_class_map: dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "attribute_guid": "str",
        "attribute_identity": "int",
        "count": "int",
        "type": "str",
    }

    attribute_map: dict[str, str] = {
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "count": "count",
        "type": "type",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator_value_class_map = {
        "value".lower(): "#/components/schemas/GrantaServerApiAggregationsAttributeValueAggregation",
        "exists".lower(): "#/components/schemas/GrantaServerApiAggregationsAttributeExistsAggregation",
    }

    discriminator: Optional[str] = "attribute_aggregation_type"

    def __init__(
        self,
        *,
        attribute_guid: "str | None | Unset_Type" = Unset,
        attribute_identity: "int | None | Unset_Type" = Unset,
        count: "int | Unset_Type" = Unset,
        type: "str" = "attribute",
    ) -> None:
        """GrantaServerApiAggregationsAttributeAggregation - a model defined in Swagger

        Parameters
        ----------
        attribute_guid: str | None, optional
        attribute_identity: int | None, optional
        count: int, optional
        type: str
        """
        super().__init__()
        self._attribute_identity: int | None | Unset_Type = Unset
        self._attribute_guid: str | None | Unset_Type = Unset
        self._type: str
        self._count: int | Unset_Type = Unset

        if attribute_identity is not Unset:
            self.attribute_identity = attribute_identity
        if attribute_guid is not Unset:
            self.attribute_guid = attribute_guid
        self.type = type
        if count is not Unset:
            self.count = count

    @property
    def attribute_identity(self) -> "int | None | Unset_Type":
        """Gets the attribute_identity of this GrantaServerApiAggregationsAttributeAggregation.
        The identity of the attribute that was aggregated over.

        Returns
        -------
        int | None | Unset_Type
            The attribute_identity of this GrantaServerApiAggregationsAttributeAggregation.
        """
        return self._attribute_identity

    @attribute_identity.setter
    def attribute_identity(self, attribute_identity: "int | None | Unset_Type") -> None:
        """Sets the attribute_identity of this GrantaServerApiAggregationsAttributeAggregation.
        The identity of the attribute that was aggregated over.

        Parameters
        ----------
        attribute_identity: int | None | Unset_Type
            The attribute_identity of this GrantaServerApiAggregationsAttributeAggregation.
        """
        self._attribute_identity = attribute_identity

    @property
    def attribute_guid(self) -> "str | None | Unset_Type":
        """Gets the attribute_guid of this GrantaServerApiAggregationsAttributeAggregation.
        The GUID of the attribute that was aggregated over.

        Returns
        -------
        str | None | Unset_Type
            The attribute_guid of this GrantaServerApiAggregationsAttributeAggregation.
        """
        return self._attribute_guid

    @attribute_guid.setter
    def attribute_guid(self, attribute_guid: "str | None | Unset_Type") -> None:
        """Sets the attribute_guid of this GrantaServerApiAggregationsAttributeAggregation.
        The GUID of the attribute that was aggregated over.

        Parameters
        ----------
        attribute_guid: str | None | Unset_Type
            The attribute_guid of this GrantaServerApiAggregationsAttributeAggregation.
        """
        self._attribute_guid = attribute_guid

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiAggregationsAttributeAggregation.

        Returns
        -------
        str
            The type of this GrantaServerApiAggregationsAttributeAggregation.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiAggregationsAttributeAggregation.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiAggregationsAttributeAggregation.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

    @property
    def count(self) -> "int | Unset_Type":
        """Gets the count of this GrantaServerApiAggregationsAttributeAggregation.
        The number of records that have a populated (applicable) value for this attribute.  (For multi-valued attributes: the number of records that have one or more populated  (applicable) values for this attribute.)                For a tabular attribute, this will be the number of records that have at least one  tabular row in this attribute, even if those rows might be filtered out from users'  views in some clients.

        Returns
        -------
        int | Unset_Type
            The count of this GrantaServerApiAggregationsAttributeAggregation.
        """
        return self._count

    @count.setter
    def count(self, count: "int | Unset_Type") -> None:
        """Sets the count of this GrantaServerApiAggregationsAttributeAggregation.
        The number of records that have a populated (applicable) value for this attribute.  (For multi-valued attributes: the number of records that have one or more populated  (applicable) values for this attribute.)                For a tabular attribute, this will be the number of records that have at least one  tabular row in this attribute, even if those rows might be filtered out from users'  views in some clients.

        Parameters
        ----------
        count: int | Unset_Type
            The count of this GrantaServerApiAggregationsAttributeAggregation.
        """
        # Field is not nullable
        if count is None:
            raise ValueError("Invalid value for 'count', must not be 'None'")
        self._count = count

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[cls._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen,
        # so we have to extract it from the JSON reference
        return cls.discriminator_value_class_map[discriminator_value].rsplit("/", 1)[-1]

    @classmethod
    def _get_discriminator_field_name(cls) -> str:
        assert cls.discriminator
        name_tokens = cls.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiAggregationsAttributeAggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
