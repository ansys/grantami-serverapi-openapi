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

from ansys.grantami.serverapi_openapi.v251.models.gsa_data_export_rollup_datum import (  # noqa: F401
    GsaDataExportRollupDatum,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaDataExportValueRollupDatum(GsaDataExportRollupDatum):
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
        "type": "str",
        "attribute_guid": "str",
        "attribute_identity": "int",
        "database_key": "str",
        "roll_up_type": "GsaTabularColumnRollUpType",
        "value": "object",
    }

    attribute_map: dict[str, str] = {
        "type": "type",
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "database_key": "databaseKey",
        "roll_up_type": "rollUpType",
        "value": "value",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        type: "str" = "valueRollup",
        attribute_guid: "Union[str, None, Unset_Type]" = Unset,
        attribute_identity: "Union[int, None, Unset_Type]" = Unset,
        database_key: "Union[str, None, Unset_Type]" = Unset,
        roll_up_type: "Union[GsaTabularColumnRollUpType, Unset_Type]" = Unset,
        value: "Union[object, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaDataExportValueRollupDatum - a model defined in Swagger

        Parameters
        ----------
        type: str
        attribute_guid: str, optional
        attribute_identity: int, optional
        database_key: str, optional
        roll_up_type: GsaTabularColumnRollUpType, optional
        value: object, optional
        """
        super().__init__(
            type=type,
            attribute_guid=attribute_guid,
            attribute_identity=attribute_identity,
            database_key=database_key,
            roll_up_type=roll_up_type,
        )
        self._value: Union[object, None, Unset_Type] = Unset

        if value is not Unset:
            self.value = value

    @property
    def value(self) -> "Union[object, None, Unset_Type]":
        """Gets the value of this GsaDataExportValueRollupDatum.

        Returns
        -------
        Union[object, None, Unset_Type]
            The value of this GsaDataExportValueRollupDatum.
        """
        return self._value

    @value.setter
    def value(self, value: "Union[object, None, Unset_Type]") -> None:
        """Sets the value of this GsaDataExportValueRollupDatum.

        Parameters
        ----------
        value: Union[object, None, Unset_Type]
            The value of this GsaDataExportValueRollupDatum.
        """
        self._value = value

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
        if not isinstance(other, GsaDataExportValueRollupDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
