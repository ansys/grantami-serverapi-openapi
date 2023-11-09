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


class GrantaServerApiSearchDiscreteTextDatumCriterion(
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
        "text_match_behaviour": "GrantaServerApiSearchTextMatchBehaviour",
        "type": "str",
        "value": "str",
    }

    attribute_map = {
        "text_match_behaviour": "textMatchBehaviour",
        "type": "type",
        "value": "value",
    }

    subtype_mapping = {
        "textMatchBehaviour": "GrantaServerApiSearchTextMatchBehaviour",
    }

    discriminator = None

    def __init__(
        self,
        *,
        text_match_behaviour: "Optional[GrantaServerApiSearchTextMatchBehaviour]" = None,
        type: "str" = "discreteText",
        value: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiSearchDiscreteTextDatumCriterion - a model defined in Swagger

        Parameters
        ----------
            text_match_behaviour: GrantaServerApiSearchTextMatchBehaviour, optional
            type: str
            value: str, optional
        """
        super().__init__()
        self._value = None
        self._text_match_behaviour = None
        self._type = None

        if value is not None:
            self.value = value
        if text_match_behaviour is not None:
            self.text_match_behaviour = text_match_behaviour
        self.type = type

    @property
    def value(self) -> "str":
        """Gets the value of this GrantaServerApiSearchDiscreteTextDatumCriterion.

        Returns
        -------
        str
            The value of this GrantaServerApiSearchDiscreteTextDatumCriterion.
        """
        return self._value

    @value.setter
    def value(self, value: "str") -> None:
        """Sets the value of this GrantaServerApiSearchDiscreteTextDatumCriterion.

        Parameters
        ----------
        value: str
            The value of this GrantaServerApiSearchDiscreteTextDatumCriterion.
        """
        self._value = value

    @property
    def text_match_behaviour(self) -> "GrantaServerApiSearchTextMatchBehaviour":
        """Gets the text_match_behaviour of this GrantaServerApiSearchDiscreteTextDatumCriterion.

        Returns
        -------
        GrantaServerApiSearchTextMatchBehaviour
            The text_match_behaviour of this GrantaServerApiSearchDiscreteTextDatumCriterion.
        """
        return self._text_match_behaviour

    @text_match_behaviour.setter
    def text_match_behaviour(
        self, text_match_behaviour: "GrantaServerApiSearchTextMatchBehaviour"
    ) -> None:
        """Sets the text_match_behaviour of this GrantaServerApiSearchDiscreteTextDatumCriterion.

        Parameters
        ----------
        text_match_behaviour: GrantaServerApiSearchTextMatchBehaviour
            The text_match_behaviour of this GrantaServerApiSearchDiscreteTextDatumCriterion.
        """
        self._text_match_behaviour = text_match_behaviour

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchDiscreteTextDatumCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchDiscreteTextDatumCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchDiscreteTextDatumCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchDiscreteTextDatumCriterion.
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
        if issubclass(GrantaServerApiSearchDiscreteTextDatumCriterion, dict):
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
        if not isinstance(other, GrantaServerApiSearchDiscreteTextDatumCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
