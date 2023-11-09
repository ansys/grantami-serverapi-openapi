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


class GrantaServerApiSearchPointDatumCriterion(GrantaServerApiSearchDatumCriterion):
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
        "gte": "float",
        "lte": "float",
        "type": "str",
    }

    attribute_map = {
        "gte": "gte",
        "lte": "lte",
        "type": "type",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        gte: "Optional[float]" = None,
        lte: "Optional[float]" = None,
        type: "str" = "point",
    ) -> None:
        """GrantaServerApiSearchPointDatumCriterion - a model defined in Swagger

        Parameters
        ----------
            gte: float, optional
            lte: float, optional
            type: str
        """
        super().__init__()
        self._gte = None
        self._lte = None
        self._type = None

        if gte is not None:
            self.gte = gte
        if lte is not None:
            self.lte = lte
        self.type = type

    @property
    def gte(self) -> "float":
        """Gets the gte of this GrantaServerApiSearchPointDatumCriterion.
        Greater than or equal

        Returns
        -------
        float
            The gte of this GrantaServerApiSearchPointDatumCriterion.
        """
        return self._gte

    @gte.setter
    def gte(self, gte: "float") -> None:
        """Sets the gte of this GrantaServerApiSearchPointDatumCriterion.
        Greater than or equal

        Parameters
        ----------
        gte: float
            The gte of this GrantaServerApiSearchPointDatumCriterion.
        """
        self._gte = gte

    @property
    def lte(self) -> "float":
        """Gets the lte of this GrantaServerApiSearchPointDatumCriterion.
        Less than or equal

        Returns
        -------
        float
            The lte of this GrantaServerApiSearchPointDatumCriterion.
        """
        return self._lte

    @lte.setter
    def lte(self, lte: "float") -> None:
        """Sets the lte of this GrantaServerApiSearchPointDatumCriterion.
        Less than or equal

        Parameters
        ----------
        lte: float
            The lte of this GrantaServerApiSearchPointDatumCriterion.
        """
        self._lte = lte

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchPointDatumCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchPointDatumCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchPointDatumCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchPointDatumCriterion.
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
        if issubclass(GrantaServerApiSearchPointDatumCriterion, dict):
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
        if not isinstance(other, GrantaServerApiSearchPointDatumCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
