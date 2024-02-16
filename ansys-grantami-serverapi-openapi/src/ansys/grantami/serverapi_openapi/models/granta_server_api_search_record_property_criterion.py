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
    Dict,
    List,
    BinaryIO,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase
from ansys.grantami.serverapi_openapi.models.granta_server_api_search_criterion import (
    GrantaServerApiSearchCriterion,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSearchRecordPropertyCriterion(GrantaServerApiSearchCriterion):
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
        "_property": "GrantaServerApiSearchSearchableRecordProperty",
        "inner_criterion": "GrantaServerApiSearchDatumCriterion",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "_property": "property",
        "inner_criterion": "innerCriterion",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {
        "property": "GrantaServerApiSearchSearchableRecordProperty",
        "innerCriterion": "GrantaServerApiSearchDatumCriterion",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        _property: "Optional[GrantaServerApiSearchSearchableRecordProperty]" = None,
        inner_criterion: "Optional[GrantaServerApiSearchDatumCriterion]" = None,
        type: "str" = "recordProperty",
    ) -> None:
        """GrantaServerApiSearchRecordPropertyCriterion - a model defined in Swagger

        Parameters
        ----------
            _property: GrantaServerApiSearchSearchableRecordProperty, optional
            inner_criterion: GrantaServerApiSearchDatumCriterion, optional
            type: str
        """
        super().__init__()
        self.__property = None
        self._inner_criterion = None
        self._type: str = None  # type: ignore[assignment]

        if _property is not None:
            self._property = _property
        if inner_criterion is not None:
            self.inner_criterion = inner_criterion
        self.type = type

    @property
    def _property(self) -> "Optional[GrantaServerApiSearchSearchableRecordProperty]":
        """Gets the _property of this GrantaServerApiSearchRecordPropertyCriterion.

        Returns
        -------
        GrantaServerApiSearchSearchableRecordProperty
            The _property of this GrantaServerApiSearchRecordPropertyCriterion.
        """
        return self.__property

    @_property.setter
    def _property(
        self, _property: "Optional[GrantaServerApiSearchSearchableRecordProperty]"
    ) -> None:
        """Sets the _property of this GrantaServerApiSearchRecordPropertyCriterion.

        Parameters
        ----------
        _property: GrantaServerApiSearchSearchableRecordProperty
            The _property of this GrantaServerApiSearchRecordPropertyCriterion.
        """
        self.__property = _property

    @property
    def inner_criterion(self) -> "Optional[GrantaServerApiSearchDatumCriterion]":
        """Gets the inner_criterion of this GrantaServerApiSearchRecordPropertyCriterion.

        Returns
        -------
        GrantaServerApiSearchDatumCriterion
            The inner_criterion of this GrantaServerApiSearchRecordPropertyCriterion.
        """
        return self._inner_criterion

    @inner_criterion.setter
    def inner_criterion(
        self, inner_criterion: "Optional[GrantaServerApiSearchDatumCriterion]"
    ) -> None:
        """Sets the inner_criterion of this GrantaServerApiSearchRecordPropertyCriterion.

        Parameters
        ----------
        inner_criterion: GrantaServerApiSearchDatumCriterion
            The inner_criterion of this GrantaServerApiSearchRecordPropertyCriterion.
        """
        self._inner_criterion = inner_criterion

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchRecordPropertyCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchRecordPropertyCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchRecordPropertyCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchRecordPropertyCriterion.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @classmethod
    def get_real_child_model(cls, data: ModelBase) -> str:
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
        return self.to_str()  # type: ignore[no-any-return]

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiSearchRecordPropertyCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
