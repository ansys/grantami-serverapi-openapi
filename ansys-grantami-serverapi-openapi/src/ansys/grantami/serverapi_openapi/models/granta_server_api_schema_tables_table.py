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


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaTablesTable(ModelBase):
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
        "display_names": "dict(str, str)",
        "guid": "str",
        "is_hidden_from_browse": "bool",
        "is_hidden_from_search": "bool",
        "is_versioned": "bool",
        "layouts": "list[GrantaServerApiSchemaSlimEntitiesSlimLayout]",
        "name": "str",
        "subsets": "list[GrantaServerApiSchemaSlimEntitiesSlimSubset]",
        "version_state": "GrantaServerApiVersionState",
        "default_layout": "GrantaServerApiSchemaSlimEntitiesSlimLayout",
        "default_subset": "GrantaServerApiSchemaSlimEntitiesSlimSubset",
    }

    attribute_map: Dict[str, str] = {
        "display_names": "displayNames",
        "guid": "guid",
        "is_hidden_from_browse": "isHiddenFromBrowse",
        "is_hidden_from_search": "isHiddenFromSearch",
        "is_versioned": "isVersioned",
        "layouts": "layouts",
        "name": "name",
        "subsets": "subsets",
        "version_state": "versionState",
        "default_layout": "defaultLayout",
        "default_subset": "defaultSubset",
    }

    subtype_mapping: Dict[str, str] = {
        "defaultSubset": "GrantaServerApiSchemaSlimEntitiesSlimSubset",
        "subsets": "GrantaServerApiSchemaSlimEntitiesSlimSubset",
        "defaultLayout": "GrantaServerApiSchemaSlimEntitiesSlimLayout",
        "layouts": "GrantaServerApiSchemaSlimEntitiesSlimLayout",
        "versionState": "GrantaServerApiVersionState",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        display_names: "Dict[str, str]",
        guid: "str",
        is_hidden_from_browse: "bool",
        is_hidden_from_search: "bool",
        is_versioned: "bool",
        layouts: "List[GrantaServerApiSchemaSlimEntitiesSlimLayout]",
        name: "str",
        subsets: "List[GrantaServerApiSchemaSlimEntitiesSlimSubset]",
        version_state: "GrantaServerApiVersionState",
        default_layout: "Union[GrantaServerApiSchemaSlimEntitiesSlimLayout, Unset_Type]" = Unset,
        default_subset: "Union[GrantaServerApiSchemaSlimEntitiesSlimSubset, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaTablesTable - a model defined in Swagger

        Parameters
        ----------
        display_names: Dict[str, str]
        guid: str
        is_hidden_from_browse: bool
        is_hidden_from_search: bool
        is_versioned: bool
        layouts: List[GrantaServerApiSchemaSlimEntitiesSlimLayout]
        name: str
        subsets: List[GrantaServerApiSchemaSlimEntitiesSlimSubset]
        version_state: GrantaServerApiVersionState
        default_layout: GrantaServerApiSchemaSlimEntitiesSlimLayout, optional
        default_subset: GrantaServerApiSchemaSlimEntitiesSlimSubset, optional
        """
        self._default_subset: Union[
            GrantaServerApiSchemaSlimEntitiesSlimSubset, Unset_Type
        ] = Unset
        self._subsets: List[GrantaServerApiSchemaSlimEntitiesSlimSubset]
        self._default_layout: Union[
            GrantaServerApiSchemaSlimEntitiesSlimLayout, Unset_Type
        ] = Unset
        self._layouts: List[GrantaServerApiSchemaSlimEntitiesSlimLayout]
        self._version_state: GrantaServerApiVersionState
        self._is_hidden_from_browse: bool
        self._is_hidden_from_search: bool
        self._is_versioned: bool
        self._display_names: Dict[str, str]
        self._name: str
        self._guid: str

        if default_subset is not Unset:
            self.default_subset = default_subset
        self.subsets = subsets
        if default_layout is not Unset:
            self.default_layout = default_layout
        self.layouts = layouts
        self.version_state = version_state
        self.is_hidden_from_browse = is_hidden_from_browse
        self.is_hidden_from_search = is_hidden_from_search
        self.is_versioned = is_versioned
        self.display_names = display_names
        self.name = name
        self.guid = guid

    @property
    def default_subset(
        self,
    ) -> "Union[GrantaServerApiSchemaSlimEntitiesSlimSubset, Unset_Type]":
        """Gets the default_subset of this GrantaServerApiSchemaTablesTable.

        Returns
        -------
        Union[GrantaServerApiSchemaSlimEntitiesSlimSubset, Unset_Type]
            The default_subset of this GrantaServerApiSchemaTablesTable.
        """
        return self._default_subset

    @default_subset.setter
    def default_subset(
        self,
        default_subset: "Union[GrantaServerApiSchemaSlimEntitiesSlimSubset, Unset_Type]",
    ) -> None:
        """Sets the default_subset of this GrantaServerApiSchemaTablesTable.

        Parameters
        ----------
        default_subset: Union[GrantaServerApiSchemaSlimEntitiesSlimSubset, Unset_Type]
            The default_subset of this GrantaServerApiSchemaTablesTable.
        """
        # Field is not nullable
        if default_subset is None:
            raise ValueError("Invalid value for 'default_subset', must not be 'None'")
        self._default_subset = default_subset

    @property
    def subsets(self) -> "List[GrantaServerApiSchemaSlimEntitiesSlimSubset]":
        """Gets the subsets of this GrantaServerApiSchemaTablesTable.

        Returns
        -------
        List[GrantaServerApiSchemaSlimEntitiesSlimSubset]
            The subsets of this GrantaServerApiSchemaTablesTable.
        """
        return self._subsets

    @subsets.setter
    def subsets(
        self, subsets: "List[GrantaServerApiSchemaSlimEntitiesSlimSubset]"
    ) -> None:
        """Sets the subsets of this GrantaServerApiSchemaTablesTable.

        Parameters
        ----------
        subsets: List[GrantaServerApiSchemaSlimEntitiesSlimSubset]
            The subsets of this GrantaServerApiSchemaTablesTable.
        """
        # Field is not nullable
        if subsets is None:
            raise ValueError("Invalid value for 'subsets', must not be 'None'")
        # Field is required
        if subsets is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'subsets', must not be 'Unset'")
        self._subsets = subsets

    @property
    def default_layout(
        self,
    ) -> "Union[GrantaServerApiSchemaSlimEntitiesSlimLayout, Unset_Type]":
        """Gets the default_layout of this GrantaServerApiSchemaTablesTable.

        Returns
        -------
        Union[GrantaServerApiSchemaSlimEntitiesSlimLayout, Unset_Type]
            The default_layout of this GrantaServerApiSchemaTablesTable.
        """
        return self._default_layout

    @default_layout.setter
    def default_layout(
        self,
        default_layout: "Union[GrantaServerApiSchemaSlimEntitiesSlimLayout, Unset_Type]",
    ) -> None:
        """Sets the default_layout of this GrantaServerApiSchemaTablesTable.

        Parameters
        ----------
        default_layout: Union[GrantaServerApiSchemaSlimEntitiesSlimLayout, Unset_Type]
            The default_layout of this GrantaServerApiSchemaTablesTable.
        """
        # Field is not nullable
        if default_layout is None:
            raise ValueError("Invalid value for 'default_layout', must not be 'None'")
        self._default_layout = default_layout

    @property
    def layouts(self) -> "List[GrantaServerApiSchemaSlimEntitiesSlimLayout]":
        """Gets the layouts of this GrantaServerApiSchemaTablesTable.

        Returns
        -------
        List[GrantaServerApiSchemaSlimEntitiesSlimLayout]
            The layouts of this GrantaServerApiSchemaTablesTable.
        """
        return self._layouts

    @layouts.setter
    def layouts(
        self, layouts: "List[GrantaServerApiSchemaSlimEntitiesSlimLayout]"
    ) -> None:
        """Sets the layouts of this GrantaServerApiSchemaTablesTable.

        Parameters
        ----------
        layouts: List[GrantaServerApiSchemaSlimEntitiesSlimLayout]
            The layouts of this GrantaServerApiSchemaTablesTable.
        """
        # Field is not nullable
        if layouts is None:
            raise ValueError("Invalid value for 'layouts', must not be 'None'")
        # Field is required
        if layouts is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'layouts', must not be 'Unset'")
        self._layouts = layouts

    @property
    def version_state(self) -> "GrantaServerApiVersionState":
        """Gets the version_state of this GrantaServerApiSchemaTablesTable.

        Returns
        -------
        GrantaServerApiVersionState
            The version_state of this GrantaServerApiSchemaTablesTable.
        """
        return self._version_state

    @version_state.setter
    def version_state(self, version_state: "GrantaServerApiVersionState") -> None:
        """Sets the version_state of this GrantaServerApiSchemaTablesTable.

        Parameters
        ----------
        version_state: GrantaServerApiVersionState
            The version_state of this GrantaServerApiSchemaTablesTable.
        """
        # Field is not nullable
        if version_state is None:
            raise ValueError("Invalid value for 'version_state', must not be 'None'")
        # Field is required
        if version_state is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'version_state', must not be 'Unset'")
        self._version_state = version_state

    @property
    def is_hidden_from_browse(self) -> "bool":
        """Gets the is_hidden_from_browse of this GrantaServerApiSchemaTablesTable.

        Returns
        -------
        bool
            The is_hidden_from_browse of this GrantaServerApiSchemaTablesTable.
        """
        return self._is_hidden_from_browse

    @is_hidden_from_browse.setter
    def is_hidden_from_browse(self, is_hidden_from_browse: "bool") -> None:
        """Sets the is_hidden_from_browse of this GrantaServerApiSchemaTablesTable.

        Parameters
        ----------
        is_hidden_from_browse: bool
            The is_hidden_from_browse of this GrantaServerApiSchemaTablesTable.
        """
        # Field is not nullable
        if is_hidden_from_browse is None:
            raise ValueError(
                "Invalid value for 'is_hidden_from_browse', must not be 'None'"
            )
        # Field is required
        if is_hidden_from_browse is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'is_hidden_from_browse', must not be 'Unset'"
            )
        self._is_hidden_from_browse = is_hidden_from_browse

    @property
    def is_hidden_from_search(self) -> "bool":
        """Gets the is_hidden_from_search of this GrantaServerApiSchemaTablesTable.

        Returns
        -------
        bool
            The is_hidden_from_search of this GrantaServerApiSchemaTablesTable.
        """
        return self._is_hidden_from_search

    @is_hidden_from_search.setter
    def is_hidden_from_search(self, is_hidden_from_search: "bool") -> None:
        """Sets the is_hidden_from_search of this GrantaServerApiSchemaTablesTable.

        Parameters
        ----------
        is_hidden_from_search: bool
            The is_hidden_from_search of this GrantaServerApiSchemaTablesTable.
        """
        # Field is not nullable
        if is_hidden_from_search is None:
            raise ValueError(
                "Invalid value for 'is_hidden_from_search', must not be 'None'"
            )
        # Field is required
        if is_hidden_from_search is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'is_hidden_from_search', must not be 'Unset'"
            )
        self._is_hidden_from_search = is_hidden_from_search

    @property
    def is_versioned(self) -> "bool":
        """Gets the is_versioned of this GrantaServerApiSchemaTablesTable.

        Returns
        -------
        bool
            The is_versioned of this GrantaServerApiSchemaTablesTable.
        """
        return self._is_versioned

    @is_versioned.setter
    def is_versioned(self, is_versioned: "bool") -> None:
        """Sets the is_versioned of this GrantaServerApiSchemaTablesTable.

        Parameters
        ----------
        is_versioned: bool
            The is_versioned of this GrantaServerApiSchemaTablesTable.
        """
        # Field is not nullable
        if is_versioned is None:
            raise ValueError("Invalid value for 'is_versioned', must not be 'None'")
        # Field is required
        if is_versioned is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'is_versioned', must not be 'Unset'")
        self._is_versioned = is_versioned

    @property
    def display_names(self) -> "Dict[str, str]":
        """Gets the display_names of this GrantaServerApiSchemaTablesTable.

        Returns
        -------
        Dict[str, str]
            The display_names of this GrantaServerApiSchemaTablesTable.
        """
        return self._display_names

    @display_names.setter
    def display_names(self, display_names: "Dict[str, str]") -> None:
        """Sets the display_names of this GrantaServerApiSchemaTablesTable.

        Parameters
        ----------
        display_names: Dict[str, str]
            The display_names of this GrantaServerApiSchemaTablesTable.
        """
        # Field is not nullable
        if display_names is None:
            raise ValueError("Invalid value for 'display_names', must not be 'None'")
        # Field is required
        if display_names is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'display_names', must not be 'Unset'")
        self._display_names = display_names

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaTablesTable.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaTablesTable.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaTablesTable.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaTablesTable.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        # Field is required
        if name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'name', must not be 'Unset'")
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaTablesTable.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaTablesTable.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaTablesTable.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaTablesTable.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        # Field is required
        if guid is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'guid', must not be 'Unset'")
        self._guid = guid

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
        if not isinstance(other, GrantaServerApiSchemaTablesTable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
