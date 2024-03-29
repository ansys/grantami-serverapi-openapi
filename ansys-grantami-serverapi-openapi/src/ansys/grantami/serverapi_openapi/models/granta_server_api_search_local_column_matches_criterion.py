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
from ansys.grantami.serverapi_openapi.models.granta_server_api_search_local_column_criterion import (
    GrantaServerApiSearchLocalColumnCriterion,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSearchLocalColumnMatchesCriterion(
    GrantaServerApiSearchLocalColumnCriterion
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
        "inner_criterion": "GrantaServerApiSearchDatumCriterion",
        "guid": "str",
        "identity": "int",
        "local_column_criterion_type": "str",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "inner_criterion": "innerCriterion",
        "guid": "guid",
        "identity": "identity",
        "local_column_criterion_type": "localColumnCriterionType",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {
        "innerCriterion": "GrantaServerApiSearchDatumCriterion",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        inner_criterion: "GrantaServerApiSearchDatumCriterion",
        guid: "Union[str, None, Unset_Type]" = Unset,
        identity: "Union[int, None, Unset_Type]" = Unset,
        local_column_criterion_type: "str" = "matches",
        type: "str" = "localColumn",
    ) -> None:
        """GrantaServerApiSearchLocalColumnMatchesCriterion - a model defined in Swagger

        Parameters
        ----------
        inner_criterion: GrantaServerApiSearchDatumCriterion
        guid: str, optional
        identity: int, optional
        local_column_criterion_type: str
        type: str
        """
        super().__init__(guid=guid, identity=identity, type=type)
        self._inner_criterion: GrantaServerApiSearchDatumCriterion
        self._local_column_criterion_type: str

        self.inner_criterion = inner_criterion
        self.local_column_criterion_type = local_column_criterion_type

    @property
    def inner_criterion(self) -> "GrantaServerApiSearchDatumCriterion":
        """Gets the inner_criterion of this GrantaServerApiSearchLocalColumnMatchesCriterion.

        Returns
        -------
        GrantaServerApiSearchDatumCriterion
            The inner_criterion of this GrantaServerApiSearchLocalColumnMatchesCriterion.
        """
        return self._inner_criterion

    @inner_criterion.setter
    def inner_criterion(
        self, inner_criterion: "GrantaServerApiSearchDatumCriterion"
    ) -> None:
        """Sets the inner_criterion of this GrantaServerApiSearchLocalColumnMatchesCriterion.

        Parameters
        ----------
        inner_criterion: GrantaServerApiSearchDatumCriterion
            The inner_criterion of this GrantaServerApiSearchLocalColumnMatchesCriterion.
        """
        # Field is not nullable
        if inner_criterion is None:
            raise ValueError("Invalid value for 'inner_criterion', must not be 'None'")
        # Field is required
        if inner_criterion is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'inner_criterion', must not be 'Unset'")
        self._inner_criterion = inner_criterion

    @property
    def local_column_criterion_type(self) -> "str":
        """Gets the local_column_criterion_type of this GrantaServerApiSearchLocalColumnMatchesCriterion.

        Returns
        -------
        str
            The local_column_criterion_type of this GrantaServerApiSearchLocalColumnMatchesCriterion.
        """
        return self._local_column_criterion_type

    @local_column_criterion_type.setter
    def local_column_criterion_type(self, local_column_criterion_type: "str") -> None:
        """Sets the local_column_criterion_type of this GrantaServerApiSearchLocalColumnMatchesCriterion.

        Parameters
        ----------
        local_column_criterion_type: str
            The local_column_criterion_type of this GrantaServerApiSearchLocalColumnMatchesCriterion.
        """
        # Field is not nullable
        if local_column_criterion_type is None:
            raise ValueError(
                "Invalid value for 'local_column_criterion_type', must not be 'None'"
            )
        # Field is required
        if local_column_criterion_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'local_column_criterion_type', must not be 'Unset'"
            )
        self._local_column_criterion_type = local_column_criterion_type

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
        if not isinstance(other, GrantaServerApiSearchLocalColumnMatchesCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
