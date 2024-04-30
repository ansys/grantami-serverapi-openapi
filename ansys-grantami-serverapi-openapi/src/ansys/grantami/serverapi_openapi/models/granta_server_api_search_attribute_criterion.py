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

from ansys.grantami.serverapi_openapi.models.granta_server_api_search_criterion import (  # noqa: F401
    GrantaServerApiSearchCriterion,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiSearchAttributeCriterion(GrantaServerApiSearchCriterion):
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
        "guid": "str",
        "identity": "int",
        "is_meta_attribute": "bool",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "guid": "guid",
        "identity": "identity",
        "is_meta_attribute": "isMetaAttribute",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator_value_class_map = {
        "matches".lower(): "#/components/schemas/GrantaServerApiSearchAttributeMatchesCriterion",
        "exists".lower(): "#/components/schemas/GrantaServerApiSearchAttributeExistsCriterion",
        "notApplicable".lower(): "#/components/schemas/GrantaServerApiSearchAttributeNotApplicableCriterion",
    }

    discriminator: Optional[str] = "attribute_criterion_type"

    def __init__(
        self,
        *,
        guid: "Union[str, None, Unset_Type]" = Unset,
        identity: "Union[int, None, Unset_Type]" = Unset,
        is_meta_attribute: "Union[bool, Unset_Type]" = Unset,
        type: "str" = "attribute",
    ) -> None:
        """GrantaServerApiSearchAttributeCriterion - a model defined in Swagger

        Parameters
        ----------
        guid: str, optional
        identity: int, optional
        is_meta_attribute: bool, optional
        type: str
        """
        super().__init__()
        self._identity: Union[int, None, Unset_Type] = Unset
        self._guid: Union[str, None, Unset_Type] = Unset
        self._is_meta_attribute: Union[bool, Unset_Type] = Unset
        self._type: str

        if identity is not Unset:
            self.identity = identity
        if guid is not Unset:
            self.guid = guid
        if is_meta_attribute is not Unset:
            self.is_meta_attribute = is_meta_attribute
        self.type = type

    @property
    def identity(self) -> "Union[int, None, Unset_Type]":
        """Gets the identity of this GrantaServerApiSearchAttributeCriterion.

        Returns
        -------
        Union[int, None, Unset_Type]
            The identity of this GrantaServerApiSearchAttributeCriterion.
        """
        return self._identity

    @identity.setter
    def identity(self, identity: "Union[int, None, Unset_Type]") -> None:
        """Sets the identity of this GrantaServerApiSearchAttributeCriterion.

        Parameters
        ----------
        identity: Union[int, None, Unset_Type]
            The identity of this GrantaServerApiSearchAttributeCriterion.
        """
        self._identity = identity

    @property
    def guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the guid of this GrantaServerApiSearchAttributeCriterion.

        Returns
        -------
        Union[str, None, Unset_Type]
            The guid of this GrantaServerApiSearchAttributeCriterion.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the guid of this GrantaServerApiSearchAttributeCriterion.

        Parameters
        ----------
        guid: Union[str, None, Unset_Type]
            The guid of this GrantaServerApiSearchAttributeCriterion.
        """
        self._guid = guid

    @property
    def is_meta_attribute(self) -> "Union[bool, Unset_Type]":
        """Gets the is_meta_attribute of this GrantaServerApiSearchAttributeCriterion.

        Returns
        -------
        Union[bool, Unset_Type]
            The is_meta_attribute of this GrantaServerApiSearchAttributeCriterion.
        """
        return self._is_meta_attribute

    @is_meta_attribute.setter
    def is_meta_attribute(self, is_meta_attribute: "Union[bool, Unset_Type]") -> None:
        """Sets the is_meta_attribute of this GrantaServerApiSearchAttributeCriterion.

        Parameters
        ----------
        is_meta_attribute: Union[bool, Unset_Type]
            The is_meta_attribute of this GrantaServerApiSearchAttributeCriterion.
        """
        # Field is not nullable
        if is_meta_attribute is None:
            raise ValueError("Invalid value for 'is_meta_attribute', must not be 'None'")
        self._is_meta_attribute = is_meta_attribute

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchAttributeCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchAttributeCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchAttributeCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchAttributeCriterion.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
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
        if not isinstance(other, GrantaServerApiSearchAttributeCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
