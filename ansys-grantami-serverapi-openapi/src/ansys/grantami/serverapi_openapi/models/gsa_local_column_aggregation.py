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

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaLocalColumnAggregation(ModelBase):
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
    discriminator_class_map: Dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: Dict[str, str] = {
        "local_column_aggregation_type": "GsaLocalColumnAggregationType",
        "count": "int",
        "local_column_guid": "str",
        "local_column_identity": "int",
    }

    attribute_map: Dict[str, str] = {
        "local_column_aggregation_type": "localColumnAggregationType",
        "count": "count",
        "local_column_guid": "localColumnGuid",
        "local_column_identity": "localColumnIdentity",
    }

    subtype_mapping: Dict[str, str] = {
        "localColumnAggregationType": "GsaLocalColumnAggregationType",
    }

    discriminator_value_class_map = {
        "value".lower(): "#/components/schemas/GsaLocalColumnValueAggregation",
        "exists".lower(): "#/components/schemas/GsaLocalColumnExistsAggregation",
    }

    discriminator: Optional[str] = "localColumnAggregationType"

    def __init__(
        self,
        *,
        local_column_aggregation_type: "GsaLocalColumnAggregationType",
        count: "Union[int, Unset_Type]" = Unset,
        local_column_guid: "Union[str, None, Unset_Type]" = Unset,
        local_column_identity: "Union[int, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaLocalColumnAggregation - a model defined in Swagger

        Parameters
        ----------
        local_column_aggregation_type: GsaLocalColumnAggregationType
        count: int, optional
        local_column_guid: str, optional
        local_column_identity: int, optional
        """
        self._local_column_identity: Union[int, None, Unset_Type] = Unset
        self._local_column_guid: Union[str, None, Unset_Type] = Unset
        self._local_column_aggregation_type: GsaLocalColumnAggregationType
        self._count: Union[int, Unset_Type] = Unset

        if local_column_identity is not Unset:
            self.local_column_identity = local_column_identity
        if local_column_guid is not Unset:
            self.local_column_guid = local_column_guid
        self.local_column_aggregation_type = local_column_aggregation_type
        if count is not Unset:
            self.count = count

    @property
    def local_column_identity(self) -> "Union[int, None, Unset_Type]":
        """Gets the local_column_identity of this GsaLocalColumnAggregation.
        The identity of the local column that was aggregated over.

        Returns
        -------
        Union[int, None, Unset_Type]
            The local_column_identity of this GsaLocalColumnAggregation.
        """
        return self._local_column_identity

    @local_column_identity.setter
    def local_column_identity(self, local_column_identity: "Union[int, None, Unset_Type]") -> None:
        """Sets the local_column_identity of this GsaLocalColumnAggregation.
        The identity of the local column that was aggregated over.

        Parameters
        ----------
        local_column_identity: Union[int, None, Unset_Type]
            The local_column_identity of this GsaLocalColumnAggregation.
        """
        self._local_column_identity = local_column_identity

    @property
    def local_column_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the local_column_guid of this GsaLocalColumnAggregation.
        The GUID of the local column that was aggregated over.

        Returns
        -------
        Union[str, None, Unset_Type]
            The local_column_guid of this GsaLocalColumnAggregation.
        """
        return self._local_column_guid

    @local_column_guid.setter
    def local_column_guid(self, local_column_guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the local_column_guid of this GsaLocalColumnAggregation.
        The GUID of the local column that was aggregated over.

        Parameters
        ----------
        local_column_guid: Union[str, None, Unset_Type]
            The local_column_guid of this GsaLocalColumnAggregation.
        """
        self._local_column_guid = local_column_guid

    @property
    def local_column_aggregation_type(self) -> "GsaLocalColumnAggregationType":
        """Gets the local_column_aggregation_type of this GsaLocalColumnAggregation.

        Returns
        -------
        GsaLocalColumnAggregationType
            The local_column_aggregation_type of this GsaLocalColumnAggregation.
        """
        return self._local_column_aggregation_type

    @local_column_aggregation_type.setter
    def local_column_aggregation_type(
        self, local_column_aggregation_type: "GsaLocalColumnAggregationType"
    ) -> None:
        """Sets the local_column_aggregation_type of this GsaLocalColumnAggregation.

        Parameters
        ----------
        local_column_aggregation_type: GsaLocalColumnAggregationType
            The local_column_aggregation_type of this GsaLocalColumnAggregation.
        """
        # Field is not nullable
        if local_column_aggregation_type is None:
            raise ValueError(
                "Invalid value for 'local_column_aggregation_type', must not be 'None'"
            )
        # Field is required
        if local_column_aggregation_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'local_column_aggregation_type', must not be 'Unset'"
            )
        self._local_column_aggregation_type = local_column_aggregation_type

    @property
    def count(self) -> "Union[int, Unset_Type]":
        """Gets the count of this GsaLocalColumnAggregation.
        The number of records that have a populated (applicable) value for this local column.

        Returns
        -------
        Union[int, Unset_Type]
            The count of this GsaLocalColumnAggregation.
        """
        return self._count

    @count.setter
    def count(self, count: "Union[int, Unset_Type]") -> None:
        """Sets the count of this GsaLocalColumnAggregation.
        The number of records that have a populated (applicable) value for this local column.

        Parameters
        ----------
        count: Union[int, Unset_Type]
            The count of this GsaLocalColumnAggregation.
        """
        # Field is not nullable
        if count is None:
            raise ValueError("Invalid value for 'count', must not be 'None'")
        self._count = count

    @classmethod
    def get_real_child_model(cls, data: Dict[str, str]) -> str:
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
        if not isinstance(other, GsaLocalColumnAggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other