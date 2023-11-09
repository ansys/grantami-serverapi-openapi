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

from ansys.grantami.serverapi_openapi.models.granta_server_api_aggregations_local_column_aggregation import (
    GrantaServerApiAggregationsLocalColumnAggregation,
)  # noqa: F401

if TYPE_CHECKING:
    from . import *


class GrantaServerApiAggregationsLocalColumnExistsAggregation(
    GrantaServerApiAggregationsLocalColumnAggregation
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
        "count": "int",
        "local_column_aggregation_type": "str",
        "local_column_guid": "str",
        "local_column_identity": "int",
    }

    attribute_map = {
        "count": "count",
        "local_column_aggregation_type": "localColumnAggregationType",
        "local_column_guid": "localColumnGuid",
        "local_column_identity": "localColumnIdentity",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        count: "Optional[int]" = None,
        local_column_aggregation_type: "str" = "exists",
        local_column_guid: "Optional[str]" = None,
        local_column_identity: "Optional[int]" = None,
    ) -> None:
        """GrantaServerApiAggregationsLocalColumnExistsAggregation - a model defined in Swagger

        Parameters
        ----------
            count: int, optional
            local_column_aggregation_type: str
            local_column_guid: str, optional
            local_column_identity: int, optional
        """
        super().__init__(
            count=count,
            local_column_guid=local_column_guid,
            local_column_identity=local_column_identity,
        )
        self._local_column_aggregation_type = None

        self.local_column_aggregation_type = local_column_aggregation_type

    @property
    def local_column_aggregation_type(self) -> "str":
        """Gets the local_column_aggregation_type of this GrantaServerApiAggregationsLocalColumnExistsAggregation.

        Returns
        -------
        str
            The local_column_aggregation_type of this GrantaServerApiAggregationsLocalColumnExistsAggregation.
        """
        return self._local_column_aggregation_type

    @local_column_aggregation_type.setter
    def local_column_aggregation_type(
        self, local_column_aggregation_type: "str"
    ) -> None:
        """Sets the local_column_aggregation_type of this GrantaServerApiAggregationsLocalColumnExistsAggregation.

        Parameters
        ----------
        local_column_aggregation_type: str
            The local_column_aggregation_type of this GrantaServerApiAggregationsLocalColumnExistsAggregation.
        """
        if local_column_aggregation_type is None:
            raise ValueError(
                "Invalid value for 'local_column_aggregation_type', must not be 'None'"
            )
        self._local_column_aggregation_type = local_column_aggregation_type

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
        if issubclass(GrantaServerApiAggregationsLocalColumnExistsAggregation, dict):
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
            other, GrantaServerApiAggregationsLocalColumnExistsAggregation
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
