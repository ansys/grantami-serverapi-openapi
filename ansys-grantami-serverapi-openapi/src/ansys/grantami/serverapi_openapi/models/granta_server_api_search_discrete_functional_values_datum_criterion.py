"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase

from ansys.grantami.serverapi_openapi.models.granta_server_api_search_datum_criterion import (
    GrantaServerApiSearchDatumCriterion,
)  # noqa: F401

if TYPE_CHECKING:
    from . import *


class GrantaServerApiSearchDiscreteFunctionalValuesDatumCriterion(
    GrantaServerApiSearchDatumCriterion
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
    swagger_types = {
        "any_guids": "list[str]",
        "any_identities": "list[int]",
        "constraints": "list[GrantaServerApiSearchParameterConstraint]",
        "type": "str",
    }

    attribute_map = {
        "any_guids": "anyGuids",
        "any_identities": "anyIdentities",
        "constraints": "constraints",
        "type": "type",
    }

    subtype_mapping = {
        "constraints": "GrantaServerApiSearchParameterConstraint",
    }

    discriminator = None

    def __init__(
        self,
        *,
        any_guids: "Optional[List[str]]" = None,
        any_identities: "Optional[List[int]]" = None,
        constraints: "Optional[List[GrantaServerApiSearchParameterConstraint]]" = None,
        type: "str" = "discreteFunctionalValues",
    ) -> None:
        """GrantaServerApiSearchDiscreteFunctionalValuesDatumCriterion - a model defined in Swagger

        Parameters
        ----------
            any_guids: List[str], optional
            any_identities: List[int], optional
            constraints: List[GrantaServerApiSearchParameterConstraint], optional
            type: str
        """
        super().__init__()
        self._any_identities = None
        self._any_guids = None
        self._type = None
        self._constraints = None

        if any_identities is not None:
            self.any_identities = any_identities
        if any_guids is not None:
            self.any_guids = any_guids
        self.type = type
        if constraints is not None:
            self.constraints = constraints

    @property
    def any_identities(self) -> "list[int]":
        """Gets the any_identities of this GrantaServerApiSearchDiscreteFunctionalValuesDatumCriterion.
        Match any of these discrete type identities

        Returns
        -------
        list[int]
            The any_identities of this GrantaServerApiSearchDiscreteFunctionalValuesDatumCriterion.
        """
        return self._any_identities

    @any_identities.setter
    def any_identities(self, any_identities: "list[int]") -> None:
        """Sets the any_identities of this GrantaServerApiSearchDiscreteFunctionalValuesDatumCriterion.
        Match any of these discrete type identities

        Parameters
        ----------
        any_identities: list[int]
            The any_identities of this GrantaServerApiSearchDiscreteFunctionalValuesDatumCriterion.
        """
        self._any_identities = any_identities

    @property
    def any_guids(self) -> "list[str]":
        """Gets the any_guids of this GrantaServerApiSearchDiscreteFunctionalValuesDatumCriterion.
        Match any of these discrete type GUIDs

        Returns
        -------
        list[str]
            The any_guids of this GrantaServerApiSearchDiscreteFunctionalValuesDatumCriterion.
        """
        return self._any_guids

    @any_guids.setter
    def any_guids(self, any_guids: "list[str]") -> None:
        """Sets the any_guids of this GrantaServerApiSearchDiscreteFunctionalValuesDatumCriterion.
        Match any of these discrete type GUIDs

        Parameters
        ----------
        any_guids: list[str]
            The any_guids of this GrantaServerApiSearchDiscreteFunctionalValuesDatumCriterion.
        """
        self._any_guids = any_guids

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchDiscreteFunctionalValuesDatumCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchDiscreteFunctionalValuesDatumCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchDiscreteFunctionalValuesDatumCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchDiscreteFunctionalValuesDatumCriterion.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @property
    def constraints(self) -> "list[GrantaServerApiSearchParameterConstraint]":
        """Gets the constraints of this GrantaServerApiSearchDiscreteFunctionalValuesDatumCriterion.
        Constraints on the parameters of the attribute. Unspecified parameters will be assumed to be unconstrained.

        Returns
        -------
        list[GrantaServerApiSearchParameterConstraint]
            The constraints of this GrantaServerApiSearchDiscreteFunctionalValuesDatumCriterion.
        """
        return self._constraints

    @constraints.setter
    def constraints(
        self, constraints: "list[GrantaServerApiSearchParameterConstraint]"
    ) -> None:
        """Sets the constraints of this GrantaServerApiSearchDiscreteFunctionalValuesDatumCriterion.
        Constraints on the parameters of the attribute. Unspecified parameters will be assumed to be unconstrained.

        Parameters
        ----------
        constraints: list[GrantaServerApiSearchParameterConstraint]
            The constraints of this GrantaServerApiSearchDiscreteFunctionalValuesDatumCriterion.
        """
        self._constraints = constraints

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

    def to_dict(self) -> Dict:
        """Returns the model properties as a dict

        Returns
        -------
        Dict
            Dictionary indexed by property name containing all the model properties
        """
        result = {}

        for attr in self.swagger_types.keys():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(
            GrantaServerApiSearchDiscreteFunctionalValuesDatumCriterion, dict
        ):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model

        Returns
        -------
        str
            String representation of the model as a dictionary
        """
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(
            other, GrantaServerApiSearchDiscreteFunctionalValuesDatumCriterion
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
