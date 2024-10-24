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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaTabularAttributeTarget(ModelBase):
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
        "target_attribute_guid": "str",
        "target_database_guid": "str",
        "target_database_version_guid": "str",
        "target_table_guid": "str",
    }

    attribute_map: dict[str, str] = {
        "target_attribute_guid": "targetAttributeGuid",
        "target_database_guid": "targetDatabaseGuid",
        "target_database_version_guid": "targetDatabaseVersionGuid",
        "target_table_guid": "targetTableGuid",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        target_attribute_guid: "Union[str, Unset_Type]" = Unset,
        target_database_guid: "Union[str, Unset_Type]" = Unset,
        target_database_version_guid: "Union[str, Unset_Type]" = Unset,
        target_table_guid: "Union[str, Unset_Type]" = Unset,
    ) -> None:
        """GsaTabularAttributeTarget - a model defined in Swagger

        Parameters
        ----------
        target_attribute_guid: str, optional
        target_database_guid: str, optional
        target_database_version_guid: str, optional
        target_table_guid: str, optional
        """
        self._target_database_guid: Union[str, Unset_Type] = Unset
        self._target_database_version_guid: Union[str, Unset_Type] = Unset
        self._target_table_guid: Union[str, Unset_Type] = Unset
        self._target_attribute_guid: Union[str, Unset_Type] = Unset

        if target_database_guid is not Unset:
            self.target_database_guid = target_database_guid
        if target_database_version_guid is not Unset:
            self.target_database_version_guid = target_database_version_guid
        if target_table_guid is not Unset:
            self.target_table_guid = target_table_guid
        if target_attribute_guid is not Unset:
            self.target_attribute_guid = target_attribute_guid

    @property
    def target_database_guid(self) -> "Union[str, Unset_Type]":
        """Gets the target_database_guid of this GsaTabularAttributeTarget.

        Returns
        -------
        Union[str, Unset_Type]
            The target_database_guid of this GsaTabularAttributeTarget.
        """
        return self._target_database_guid

    @target_database_guid.setter
    def target_database_guid(self, target_database_guid: "Union[str, Unset_Type]") -> None:
        """Sets the target_database_guid of this GsaTabularAttributeTarget.

        Parameters
        ----------
        target_database_guid: Union[str, Unset_Type]
            The target_database_guid of this GsaTabularAttributeTarget.
        """
        # Field is not nullable
        if target_database_guid is None:
            raise ValueError("Invalid value for 'target_database_guid', must not be 'None'")
        self._target_database_guid = target_database_guid

    @property
    def target_database_version_guid(self) -> "Union[str, Unset_Type]":
        """Gets the target_database_version_guid of this GsaTabularAttributeTarget.

        Returns
        -------
        Union[str, Unset_Type]
            The target_database_version_guid of this GsaTabularAttributeTarget.
        """
        return self._target_database_version_guid

    @target_database_version_guid.setter
    def target_database_version_guid(
        self, target_database_version_guid: "Union[str, Unset_Type]"
    ) -> None:
        """Sets the target_database_version_guid of this GsaTabularAttributeTarget.

        Parameters
        ----------
        target_database_version_guid: Union[str, Unset_Type]
            The target_database_version_guid of this GsaTabularAttributeTarget.
        """
        # Field is not nullable
        if target_database_version_guid is None:
            raise ValueError("Invalid value for 'target_database_version_guid', must not be 'None'")
        self._target_database_version_guid = target_database_version_guid

    @property
    def target_table_guid(self) -> "Union[str, Unset_Type]":
        """Gets the target_table_guid of this GsaTabularAttributeTarget.

        Returns
        -------
        Union[str, Unset_Type]
            The target_table_guid of this GsaTabularAttributeTarget.
        """
        return self._target_table_guid

    @target_table_guid.setter
    def target_table_guid(self, target_table_guid: "Union[str, Unset_Type]") -> None:
        """Sets the target_table_guid of this GsaTabularAttributeTarget.

        Parameters
        ----------
        target_table_guid: Union[str, Unset_Type]
            The target_table_guid of this GsaTabularAttributeTarget.
        """
        # Field is not nullable
        if target_table_guid is None:
            raise ValueError("Invalid value for 'target_table_guid', must not be 'None'")
        self._target_table_guid = target_table_guid

    @property
    def target_attribute_guid(self) -> "Union[str, Unset_Type]":
        """Gets the target_attribute_guid of this GsaTabularAttributeTarget.

        Returns
        -------
        Union[str, Unset_Type]
            The target_attribute_guid of this GsaTabularAttributeTarget.
        """
        return self._target_attribute_guid

    @target_attribute_guid.setter
    def target_attribute_guid(self, target_attribute_guid: "Union[str, Unset_Type]") -> None:
        """Sets the target_attribute_guid of this GsaTabularAttributeTarget.

        Parameters
        ----------
        target_attribute_guid: Union[str, Unset_Type]
            The target_attribute_guid of this GsaTabularAttributeTarget.
        """
        # Field is not nullable
        if target_attribute_guid is None:
            raise ValueError("Invalid value for 'target_attribute_guid', must not be 'None'")
        self._target_attribute_guid = target_attribute_guid

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
        if not isinstance(other, GsaTabularAttributeTarget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
