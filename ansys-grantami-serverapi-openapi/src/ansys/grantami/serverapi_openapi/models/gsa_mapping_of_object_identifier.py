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

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaMappingOfObjectIdentifier(ModelBase):
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
        "link_source_type": "GsaLinkSourceType",
        "parameter_mappings": "list[GsaMappingOfObjectIdentifier]",
        "source": "GsaObjectIdentifier",
        "target_guid": "str",
        "target_identity": "int",
    }

    attribute_map: dict[str, str] = {
        "link_source_type": "linkSourceType",
        "parameter_mappings": "parameterMappings",
        "source": "source",
        "target_guid": "targetGuid",
        "target_identity": "targetIdentity",
    }

    subtype_mapping: dict[str, str] = {
        "source": "GsaObjectIdentifier",
        "parameterMappings": "GsaMappingOfObjectIdentifier",
        "linkSourceType": "GsaLinkSourceType",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        link_source_type: "Union[GsaLinkSourceType, Unset_Type]" = Unset,
        parameter_mappings: "Union[list[GsaMappingOfObjectIdentifier], None, Unset_Type]" = Unset,
        source: "Union[GsaObjectIdentifier, Unset_Type]" = Unset,
        target_guid: "Union[str, Unset_Type]" = Unset,
        target_identity: "Union[int, Unset_Type]" = Unset,
    ) -> None:
        """GsaMappingOfObjectIdentifier - a model defined in Swagger

        Parameters
        ----------
        link_source_type: GsaLinkSourceType, optional
        parameter_mappings: list[GsaMappingOfObjectIdentifier], optional
        source: GsaObjectIdentifier, optional
        target_guid: str, optional
        target_identity: int, optional
        """
        self._source: Union[GsaObjectIdentifier, Unset_Type] = Unset
        self._target_identity: Union[int, Unset_Type] = Unset
        self._target_guid: Union[str, Unset_Type] = Unset
        self._parameter_mappings: Union[list[GsaMappingOfObjectIdentifier], None, Unset_Type] = (
            Unset
        )
        self._link_source_type: Union[GsaLinkSourceType, Unset_Type] = Unset

        if source is not Unset:
            self.source = source
        if target_identity is not Unset:
            self.target_identity = target_identity
        if target_guid is not Unset:
            self.target_guid = target_guid
        if parameter_mappings is not Unset:
            self.parameter_mappings = parameter_mappings
        if link_source_type is not Unset:
            self.link_source_type = link_source_type

    @property
    def source(self) -> "Union[GsaObjectIdentifier, Unset_Type]":
        """Gets the source of this GsaMappingOfObjectIdentifier.

        Returns
        -------
        Union[GsaObjectIdentifier, Unset_Type]
            The source of this GsaMappingOfObjectIdentifier.
        """
        return self._source

    @source.setter
    def source(self, source: "Union[GsaObjectIdentifier, Unset_Type]") -> None:
        """Sets the source of this GsaMappingOfObjectIdentifier.

        Parameters
        ----------
        source: Union[GsaObjectIdentifier, Unset_Type]
            The source of this GsaMappingOfObjectIdentifier.
        """
        # Field is not nullable
        if source is None:
            raise ValueError("Invalid value for 'source', must not be 'None'")
        self._source = source

    @property
    def target_identity(self) -> "Union[int, Unset_Type]":
        """Gets the target_identity of this GsaMappingOfObjectIdentifier.
        The identity of the integration schema attribute

        Returns
        -------
        Union[int, Unset_Type]
            The target_identity of this GsaMappingOfObjectIdentifier.
        """
        return self._target_identity

    @target_identity.setter
    def target_identity(self, target_identity: "Union[int, Unset_Type]") -> None:
        """Sets the target_identity of this GsaMappingOfObjectIdentifier.
        The identity of the integration schema attribute

        Parameters
        ----------
        target_identity: Union[int, Unset_Type]
            The target_identity of this GsaMappingOfObjectIdentifier.
        """
        # Field is not nullable
        if target_identity is None:
            raise ValueError("Invalid value for 'target_identity', must not be 'None'")
        self._target_identity = target_identity

    @property
    def target_guid(self) -> "Union[str, Unset_Type]":
        """Gets the target_guid of this GsaMappingOfObjectIdentifier.
        The guid of the integration schema attribute

        Returns
        -------
        Union[str, Unset_Type]
            The target_guid of this GsaMappingOfObjectIdentifier.
        """
        return self._target_guid

    @target_guid.setter
    def target_guid(self, target_guid: "Union[str, Unset_Type]") -> None:
        """Sets the target_guid of this GsaMappingOfObjectIdentifier.
        The guid of the integration schema attribute

        Parameters
        ----------
        target_guid: Union[str, Unset_Type]
            The target_guid of this GsaMappingOfObjectIdentifier.
        """
        # Field is not nullable
        if target_guid is None:
            raise ValueError("Invalid value for 'target_guid', must not be 'None'")
        self._target_guid = target_guid

    @property
    def parameter_mappings(self) -> "Union[list[GsaMappingOfObjectIdentifier], None, Unset_Type]":
        """Gets the parameter_mappings of this GsaMappingOfObjectIdentifier.
        Any mapped parameters (float functional attributes only). The target parameters must be defined on the target integration attribute.  Not every parameters from the source database needs to be mapped for each attribute.

        Returns
        -------
        Union[list[GsaMappingOfObjectIdentifier], None, Unset_Type]
            The parameter_mappings of this GsaMappingOfObjectIdentifier.
        """
        return self._parameter_mappings

    @parameter_mappings.setter
    def parameter_mappings(
        self, parameter_mappings: "Union[list[GsaMappingOfObjectIdentifier], None, Unset_Type]"
    ) -> None:
        """Sets the parameter_mappings of this GsaMappingOfObjectIdentifier.
        Any mapped parameters (float functional attributes only). The target parameters must be defined on the target integration attribute.  Not every parameters from the source database needs to be mapped for each attribute.

        Parameters
        ----------
        parameter_mappings: Union[list[GsaMappingOfObjectIdentifier], None, Unset_Type]
            The parameter_mappings of this GsaMappingOfObjectIdentifier.
        """
        self._parameter_mappings = parameter_mappings

    @property
    def link_source_type(self) -> "Union[GsaLinkSourceType, Unset_Type]":
        """Gets the link_source_type of this GsaMappingOfObjectIdentifier.

        Returns
        -------
        Union[GsaLinkSourceType, Unset_Type]
            The link_source_type of this GsaMappingOfObjectIdentifier.
        """
        return self._link_source_type

    @link_source_type.setter
    def link_source_type(self, link_source_type: "Union[GsaLinkSourceType, Unset_Type]") -> None:
        """Sets the link_source_type of this GsaMappingOfObjectIdentifier.

        Parameters
        ----------
        link_source_type: Union[GsaLinkSourceType, Unset_Type]
            The link_source_type of this GsaMappingOfObjectIdentifier.
        """
        # Field is not nullable
        if link_source_type is None:
            raise ValueError("Invalid value for 'link_source_type', must not be 'None'")
        self._link_source_type = link_source_type

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
        if not isinstance(other, GsaMappingOfObjectIdentifier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
