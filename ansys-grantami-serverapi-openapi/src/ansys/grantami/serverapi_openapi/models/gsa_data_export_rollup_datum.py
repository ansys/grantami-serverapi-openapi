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


class GsaDataExportRollupDatum(ModelBase):
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
        "type": "str",
        "attribute_guid": "str",
        "attribute_identity": "int",
        "database_key": "str",
        "roll_up_type": "GsaTabularColumnRollUpType",
    }

    attribute_map: Dict[str, str] = {
        "type": "type",
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "database_key": "databaseKey",
        "roll_up_type": "rollUpType",
    }

    subtype_mapping: Dict[str, str] = {
        "rollUpType": "GsaTabularColumnRollUpType",
    }

    discriminator_value_class_map = {
        "statisticalRollup".lower(): "#/components/schemas/GsaDataExportNumericRollupDatum",
        "valueRollup".lower(): "#/components/schemas/GsaDataExportValueRollupDatum",
        "valuesRollup".lower(): "#/components/schemas/GsaDataExportValuesRollupDatum",
        "countRollup".lower(): "#/components/schemas/GsaDataExportCountRollupDatum",
    }

    discriminator: Optional[str] = "type"

    def __init__(
        self,
        *,
        type: "str",
        attribute_guid: "Union[str, None, Unset_Type]" = Unset,
        attribute_identity: "Union[int, None, Unset_Type]" = Unset,
        database_key: "Union[str, None, Unset_Type]" = Unset,
        roll_up_type: "Union[GsaTabularColumnRollUpType, Unset_Type]" = Unset,
    ) -> None:
        """GsaDataExportRollupDatum - a model defined in Swagger

        Parameters
        ----------
        type: str
        attribute_guid: str, optional
        attribute_identity: int, optional
        database_key: str, optional
        roll_up_type: GsaTabularColumnRollUpType, optional
        """
        self._database_key: Union[str, None, Unset_Type] = Unset
        self._attribute_identity: Union[int, None, Unset_Type] = Unset
        self._attribute_guid: Union[str, None, Unset_Type] = Unset
        self._roll_up_type: Union[GsaTabularColumnRollUpType, Unset_Type] = Unset
        self._type: str

        if database_key is not Unset:
            self.database_key = database_key
        if attribute_identity is not Unset:
            self.attribute_identity = attribute_identity
        if attribute_guid is not Unset:
            self.attribute_guid = attribute_guid
        if roll_up_type is not Unset:
            self.roll_up_type = roll_up_type
        self.type = type

    @property
    def database_key(self) -> "Union[str, None, Unset_Type]":
        """Gets the database_key of this GsaDataExportRollupDatum.
        The database key of the rolled up data

        Returns
        -------
        Union[str, None, Unset_Type]
            The database_key of this GsaDataExportRollupDatum.
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key: "Union[str, None, Unset_Type]") -> None:
        """Sets the database_key of this GsaDataExportRollupDatum.
        The database key of the rolled up data

        Parameters
        ----------
        database_key: Union[str, None, Unset_Type]
            The database_key of this GsaDataExportRollupDatum.
        """
        self._database_key = database_key

    @property
    def attribute_identity(self) -> "Union[int, None, Unset_Type]":
        """Gets the attribute_identity of this GsaDataExportRollupDatum.
        The attribute identity of the rolled up data.  If the data came from a local column, this is the column identity.  If the data came from linked records, this is the identity of the tabular attribute

        Returns
        -------
        Union[int, None, Unset_Type]
            The attribute_identity of this GsaDataExportRollupDatum.
        """
        return self._attribute_identity

    @attribute_identity.setter
    def attribute_identity(self, attribute_identity: "Union[int, None, Unset_Type]") -> None:
        """Sets the attribute_identity of this GsaDataExportRollupDatum.
        The attribute identity of the rolled up data.  If the data came from a local column, this is the column identity.  If the data came from linked records, this is the identity of the tabular attribute

        Parameters
        ----------
        attribute_identity: Union[int, None, Unset_Type]
            The attribute_identity of this GsaDataExportRollupDatum.
        """
        self._attribute_identity = attribute_identity

    @property
    def attribute_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the attribute_guid of this GsaDataExportRollupDatum.
        The attribute GUID of the rolled up data.  If the data came from a local column, this is the column GUID.  If the data came from linked records, this is the GUID of the tabular attribute

        Returns
        -------
        Union[str, None, Unset_Type]
            The attribute_guid of this GsaDataExportRollupDatum.
        """
        return self._attribute_guid

    @attribute_guid.setter
    def attribute_guid(self, attribute_guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the attribute_guid of this GsaDataExportRollupDatum.
        The attribute GUID of the rolled up data.  If the data came from a local column, this is the column GUID.  If the data came from linked records, this is the GUID of the tabular attribute

        Parameters
        ----------
        attribute_guid: Union[str, None, Unset_Type]
            The attribute_guid of this GsaDataExportRollupDatum.
        """
        self._attribute_guid = attribute_guid

    @property
    def roll_up_type(self) -> "Union[GsaTabularColumnRollUpType, Unset_Type]":
        """Gets the roll_up_type of this GsaDataExportRollupDatum.

        Returns
        -------
        Union[GsaTabularColumnRollUpType, Unset_Type]
            The roll_up_type of this GsaDataExportRollupDatum.
        """
        return self._roll_up_type

    @roll_up_type.setter
    def roll_up_type(self, roll_up_type: "Union[GsaTabularColumnRollUpType, Unset_Type]") -> None:
        """Sets the roll_up_type of this GsaDataExportRollupDatum.

        Parameters
        ----------
        roll_up_type: Union[GsaTabularColumnRollUpType, Unset_Type]
            The roll_up_type of this GsaDataExportRollupDatum.
        """
        # Field is not nullable
        if roll_up_type is None:
            raise ValueError("Invalid value for 'roll_up_type', must not be 'None'")
        self._roll_up_type = roll_up_type

    @property
    def type(self) -> "str":
        """Gets the type of this GsaDataExportRollupDatum.

        Returns
        -------
        str
            The type of this GsaDataExportRollupDatum.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GsaDataExportRollupDatum.

        Parameters
        ----------
        type: str
            The type of this GsaDataExportRollupDatum.
        """
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

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
        if not isinstance(other, GsaDataExportRollupDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
