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

from ansys.grantami.serverapi_openapi.models.granta_server_api_search_attribute_criterion import (
    GrantaServerApiSearchAttributeCriterion,
)  # noqa: F401

if TYPE_CHECKING:
    from . import *


class GrantaServerApiSearchAttributeMatchesCriterion(
    GrantaServerApiSearchAttributeCriterion
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

    """
    swagger_types = {
        "attribute_criterion_type": "str",
        "guid": "str",
        "identity": "int",
        "inner_criterion": "GrantaServerApiSearchDatumCriterion",
        "is_meta_attribute": "bool",
        "type": "str",
    }

    attribute_map = {
        "attribute_criterion_type": "attributeCriterionType",
        "guid": "guid",
        "identity": "identity",
        "inner_criterion": "innerCriterion",
        "is_meta_attribute": "isMetaAttribute",
        "type": "type",
    }

    subtype_mapping = {
        "innerCriterion": "GrantaServerApiSearchDatumCriterion",
    }

    def __init__(
        self,
        *,
        attribute_criterion_type: "str" = "matches",
        guid: "Optional[str]" = None,
        identity: "Optional[int]" = None,
        inner_criterion: "Optional[GrantaServerApiSearchDatumCriterion]" = None,
        is_meta_attribute: "Optional[bool]" = None,
        type: "str" = "attribute",
    ) -> None:
        """GrantaServerApiSearchAttributeMatchesCriterion - a model defined in Swagger

        Parameters
        ----------
            attribute_criterion_type: str
            guid: str, optional
            identity: int, optional
            inner_criterion: GrantaServerApiSearchDatumCriterion, optional
            is_meta_attribute: bool, optional
            type: str
        """
        super().__init__(
            guid=guid, identity=identity, is_meta_attribute=is_meta_attribute, type=type
        )
        self._inner_criterion = None
        self._attribute_criterion_type = None
        self.discriminator = None
        if inner_criterion is not None:
            self.inner_criterion = inner_criterion
        self.attribute_criterion_type = attribute_criterion_type

    @property
    def inner_criterion(self) -> "GrantaServerApiSearchDatumCriterion":
        """Gets the inner_criterion of this GrantaServerApiSearchAttributeMatchesCriterion.

        Returns
        -------
        GrantaServerApiSearchDatumCriterion
            The inner_criterion of this GrantaServerApiSearchAttributeMatchesCriterion.
        """
        return self._inner_criterion

    @inner_criterion.setter
    def inner_criterion(
        self, inner_criterion: "GrantaServerApiSearchDatumCriterion"
    ) -> None:
        """Sets the inner_criterion of this GrantaServerApiSearchAttributeMatchesCriterion.

        Parameters
        ----------
        inner_criterion: GrantaServerApiSearchDatumCriterion
            The inner_criterion of this GrantaServerApiSearchAttributeMatchesCriterion.
        """
        self._inner_criterion = inner_criterion

    @property
    def attribute_criterion_type(self) -> "str":
        """Gets the attribute_criterion_type of this GrantaServerApiSearchAttributeMatchesCriterion.

        Returns
        -------
        str
            The attribute_criterion_type of this GrantaServerApiSearchAttributeMatchesCriterion.
        """
        return self._attribute_criterion_type

    @attribute_criterion_type.setter
    def attribute_criterion_type(self, attribute_criterion_type: "str") -> None:
        """Sets the attribute_criterion_type of this GrantaServerApiSearchAttributeMatchesCriterion.

        Parameters
        ----------
        attribute_criterion_type: str
            The attribute_criterion_type of this GrantaServerApiSearchAttributeMatchesCriterion.
        """
        if attribute_criterion_type is None:
            raise ValueError(
                "Invalid value for 'attribute_criterion_type', must not be 'None'"
            )
        self._attribute_criterion_type = attribute_criterion_type

    def get_real_child_model(self, data: ModelBase) -> str:
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
        if issubclass(GrantaServerApiSearchAttributeMatchesCriterion, dict):
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
        if not isinstance(other, GrantaServerApiSearchAttributeMatchesCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
