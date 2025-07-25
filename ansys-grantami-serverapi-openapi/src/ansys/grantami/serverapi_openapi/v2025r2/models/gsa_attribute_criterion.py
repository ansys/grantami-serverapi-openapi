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

from ansys.grantami.serverapi_openapi.v2025r2.models.gsa_criterion import GsaCriterion  # noqa: F401
from ansys.grantami.serverapi_openapi.v2025r2.models.gsa_criterion_type import GsaCriterionType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaAttributeCriterion(GsaCriterion):
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
        "attribute_criterion_type": "GsaAttributeCriterionType",
        "type": "GsaCriterionType",
        "guid": "str",
        "identity": "int",
        "is_meta_attribute": "bool",
    }

    attribute_map: dict[str, str] = {
        "attribute_criterion_type": "attributeCriterionType",
        "type": "type",
        "guid": "guid",
        "identity": "identity",
        "is_meta_attribute": "isMetaAttribute",
    }

    subtype_mapping: dict[str, str] = {
        "attributeCriterionType": "GsaAttributeCriterionType",
    }

    discriminator_value_class_map = {
        "matches".lower(): "#/components/schemas/GsaAttributeMatchesCriterion",
        "exists".lower(): "#/components/schemas/GsaAttributeExistsCriterion",
        "notApplicable".lower(): "#/components/schemas/GsaAttributeNotApplicableCriterion",
    }

    discriminator: Optional[str] = "attribute_criterion_type"

    def __init__(
        self,
        *,
        attribute_criterion_type: "GsaAttributeCriterionType",
        type: "GsaCriterionType" = GsaCriterionType.ATTRIBUTE,
        guid: "str | None | Unset_Type" = Unset,
        identity: "int | None | Unset_Type" = Unset,
        is_meta_attribute: "bool | Unset_Type" = Unset,
    ) -> None:
        """GsaAttributeCriterion - a model defined in Swagger

        Parameters
        ----------
        attribute_criterion_type: GsaAttributeCriterionType
        type: GsaCriterionType
        guid: str | None, optional
        identity: int | None, optional
        is_meta_attribute: bool, optional
        """
        super().__init__(type=type)
        self._identity: int | None | Unset_Type = Unset
        self._guid: str | None | Unset_Type = Unset
        self._is_meta_attribute: bool | Unset_Type = Unset
        self._attribute_criterion_type: GsaAttributeCriterionType

        if identity is not Unset:
            self.identity = identity
        if guid is not Unset:
            self.guid = guid
        if is_meta_attribute is not Unset:
            self.is_meta_attribute = is_meta_attribute
        self.attribute_criterion_type = attribute_criterion_type

    @property
    def identity(self) -> "int | None | Unset_Type":
        """Gets the identity of this GsaAttributeCriterion.

        Returns
        -------
        int | None | Unset_Type
            The identity of this GsaAttributeCriterion.
        """
        return self._identity

    @identity.setter
    def identity(self, identity: "int | None | Unset_Type") -> None:
        """Sets the identity of this GsaAttributeCriterion.

        Parameters
        ----------
        identity: int | None | Unset_Type
            The identity of this GsaAttributeCriterion.
        """
        self._identity = identity

    @property
    def guid(self) -> "str | None | Unset_Type":
        """Gets the guid of this GsaAttributeCriterion.

        Returns
        -------
        str | None | Unset_Type
            The guid of this GsaAttributeCriterion.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str | None | Unset_Type") -> None:
        """Sets the guid of this GsaAttributeCriterion.

        Parameters
        ----------
        guid: str | None | Unset_Type
            The guid of this GsaAttributeCriterion.
        """
        self._guid = guid

    @property
    def is_meta_attribute(self) -> "bool | Unset_Type":
        """Gets the is_meta_attribute of this GsaAttributeCriterion.

        Returns
        -------
        bool | Unset_Type
            The is_meta_attribute of this GsaAttributeCriterion.
        """
        return self._is_meta_attribute

    @is_meta_attribute.setter
    def is_meta_attribute(self, is_meta_attribute: "bool | Unset_Type") -> None:
        """Sets the is_meta_attribute of this GsaAttributeCriterion.

        Parameters
        ----------
        is_meta_attribute: bool | Unset_Type
            The is_meta_attribute of this GsaAttributeCriterion.
        """
        # Field is not nullable
        if is_meta_attribute is None:
            raise ValueError("Invalid value for 'is_meta_attribute', must not be 'None'")
        self._is_meta_attribute = is_meta_attribute

    @property
    def attribute_criterion_type(self) -> "GsaAttributeCriterionType":
        """Gets the attribute_criterion_type of this GsaAttributeCriterion.

        Returns
        -------
        GsaAttributeCriterionType
            The attribute_criterion_type of this GsaAttributeCriterion.
        """
        return self._attribute_criterion_type

    @attribute_criterion_type.setter
    def attribute_criterion_type(
        self, attribute_criterion_type: "GsaAttributeCriterionType"
    ) -> None:
        """Sets the attribute_criterion_type of this GsaAttributeCriterion.

        Parameters
        ----------
        attribute_criterion_type: GsaAttributeCriterionType
            The attribute_criterion_type of this GsaAttributeCriterion.
        """
        # Field is not nullable
        if attribute_criterion_type is None:
            raise ValueError("Invalid value for 'attribute_criterion_type', must not be 'None'")
        # Field is required
        if attribute_criterion_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'attribute_criterion_type', must not be 'Unset'")
        self._attribute_criterion_type = attribute_criterion_type

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
        if not isinstance(other, GsaAttributeCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
