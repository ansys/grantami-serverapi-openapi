"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import (
    TYPE_CHECKING,
    Any,
    BinaryIO,
    Dict,
    List,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_record_link_groups_update_record_link_group import (
    GrantaServerApiSchemaRecordLinkGroupsUpdateRecordLinkGroup,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup(
    GrantaServerApiSchemaRecordLinkGroupsUpdateRecordLinkGroup
):
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
        "attribute_pairs": "list[GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair]",
        "forbid_orphans": "bool",
        "guid": "str",
        "name": "str",
        "referential_integrity_model": "GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel",
        "reverse_name": "str",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "attribute_pairs": "attributePairs",
        "forbid_orphans": "forbidOrphans",
        "guid": "guid",
        "name": "name",
        "referential_integrity_model": "referentialIntegrityModel",
        "reverse_name": "reverseName",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {
        "referentialIntegrityModel": "GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel",
        "attributePairs": "GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_pairs: "Union[List[GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair], Unset_Type]" = Unset,
        forbid_orphans: "Union[bool, Unset_Type]" = Unset,
        guid: "Union[str, Unset_Type]" = Unset,
        name: "Union[str, Unset_Type]" = Unset,
        referential_integrity_model: "Union[GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel, Unset_Type]" = Unset,
        reverse_name: "Union[str, Unset_Type]" = Unset,
        type: "str" = "dynamic",
    ) -> None:
        """GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup - a model defined in Swagger

        Parameters
        ----------
        attribute_pairs: List[GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair], optional
        forbid_orphans: bool, optional
        guid: str, optional
        name: str, optional
        referential_integrity_model: GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel, optional
        reverse_name: str, optional
        type: str
        """
        super().__init__(guid=guid, name=name, reverse_name=reverse_name)
        self._forbid_orphans: Union[bool, Unset_Type] = Unset
        self._referential_integrity_model: Union[
            GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel, Unset_Type
        ] = Unset
        self._attribute_pairs: Union[
            List[GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair],
            Unset_Type,
        ] = Unset
        self._type: str

        if forbid_orphans is not Unset:
            self.forbid_orphans = forbid_orphans
        if referential_integrity_model is not Unset:
            self.referential_integrity_model = referential_integrity_model
        if attribute_pairs is not Unset:
            self.attribute_pairs = attribute_pairs
        self.type = type

    @property
    def forbid_orphans(self) -> "Union[bool, Unset_Type]":
        """Gets the forbid_orphans of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.

        Returns
        -------
        Union[bool, Unset_Type]
            The forbid_orphans of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.
        """
        return self._forbid_orphans

    @forbid_orphans.setter
    def forbid_orphans(self, forbid_orphans: "Union[bool, Unset_Type]") -> None:
        """Sets the forbid_orphans of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.

        Parameters
        ----------
        forbid_orphans: Union[bool, Unset_Type]
            The forbid_orphans of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.
        """
        # Field is not nullable
        if forbid_orphans is None:
            raise ValueError("Invalid value for 'forbid_orphans', must not be 'None'")
        self._forbid_orphans = forbid_orphans

    @property
    def referential_integrity_model(
        self,
    ) -> "Union[GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel, Unset_Type]":
        """Gets the referential_integrity_model of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.

        Returns
        -------
        Union[GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel, Unset_Type]
            The referential_integrity_model of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.
        """
        return self._referential_integrity_model

    @referential_integrity_model.setter
    def referential_integrity_model(
        self,
        referential_integrity_model: "Union[GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel, Unset_Type]",
    ) -> None:
        """Sets the referential_integrity_model of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.

        Parameters
        ----------
        referential_integrity_model: Union[GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel, Unset_Type]
            The referential_integrity_model of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.
        """
        # Field is not nullable
        if referential_integrity_model is None:
            raise ValueError(
                "Invalid value for 'referential_integrity_model', must not be 'None'"
            )
        self._referential_integrity_model = referential_integrity_model

    @property
    def attribute_pairs(
        self,
    ) -> "Union[List[GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair], Unset_Type]":
        """Gets the attribute_pairs of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.

        Returns
        -------
        Union[List[GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair], Unset_Type]
            The attribute_pairs of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.
        """
        return self._attribute_pairs

    @attribute_pairs.setter
    def attribute_pairs(
        self,
        attribute_pairs: "Union[List[GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair], Unset_Type]",
    ) -> None:
        """Sets the attribute_pairs of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.

        Parameters
        ----------
        attribute_pairs: Union[List[GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair], Unset_Type]
            The attribute_pairs of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.
        """
        # Field is not nullable
        if attribute_pairs is None:
            raise ValueError("Invalid value for 'attribute_pairs', must not be 'None'")
        self._attribute_pairs = attribute_pairs

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.
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
        if not isinstance(
            other, GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
