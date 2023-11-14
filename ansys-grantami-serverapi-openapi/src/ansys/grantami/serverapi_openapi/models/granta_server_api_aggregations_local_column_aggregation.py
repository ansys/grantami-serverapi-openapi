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


if TYPE_CHECKING:
    from . import *


class GrantaServerApiAggregationsLocalColumnAggregation(ModelBase):
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
    discriminator_class_map: Dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types = {
        "count": "int",
        "local_column_guid": "str",
        "local_column_identity": "int",
    }

    attribute_map = {
        "count": "count",
        "local_column_guid": "localColumnGuid",
        "local_column_identity": "localColumnIdentity",
    }

    subtype_mapping = {}

    discriminator_value_class_map = {
        "value".lower(): "#/components/schemas/GrantaServerApiAggregationsLocalColumnValueAggregation",
        "exists".lower(): "#/components/schemas/GrantaServerApiAggregationsLocalColumnExistsAggregation",
    }

    discriminator = "local_column_aggregation_type"

    def __init__(
        self,
        *,
        count: "Optional[int]" = None,
        local_column_guid: "Optional[str]" = None,
        local_column_identity: "Optional[int]" = None,
    ) -> None:
        """GrantaServerApiAggregationsLocalColumnAggregation - a model defined in Swagger

        Parameters
        ----------
            count: int, optional
            local_column_guid: str, optional
            local_column_identity: int, optional
        """
        self._local_column_identity = None
        self._local_column_guid = None
        self._count = None

        if local_column_identity is not None:
            self.local_column_identity = local_column_identity
        if local_column_guid is not None:
            self.local_column_guid = local_column_guid
        if count is not None:
            self.count = count

    @property
    def local_column_identity(self) -> "int":
        """Gets the local_column_identity of this GrantaServerApiAggregationsLocalColumnAggregation.
        The identity of the local column that was aggregated over.

        Returns
        -------
        int
            The local_column_identity of this GrantaServerApiAggregationsLocalColumnAggregation.
        """
        return self._local_column_identity

    @local_column_identity.setter
    def local_column_identity(self, local_column_identity: "int") -> None:
        """Sets the local_column_identity of this GrantaServerApiAggregationsLocalColumnAggregation.
        The identity of the local column that was aggregated over.

        Parameters
        ----------
        local_column_identity: int
            The local_column_identity of this GrantaServerApiAggregationsLocalColumnAggregation.
        """
        self._local_column_identity = local_column_identity

    @property
    def local_column_guid(self) -> "str":
        """Gets the local_column_guid of this GrantaServerApiAggregationsLocalColumnAggregation.
        The GUID of the local column that was aggregated over.

        Returns
        -------
        str
            The local_column_guid of this GrantaServerApiAggregationsLocalColumnAggregation.
        """
        return self._local_column_guid

    @local_column_guid.setter
    def local_column_guid(self, local_column_guid: "str") -> None:
        """Sets the local_column_guid of this GrantaServerApiAggregationsLocalColumnAggregation.
        The GUID of the local column that was aggregated over.

        Parameters
        ----------
        local_column_guid: str
            The local_column_guid of this GrantaServerApiAggregationsLocalColumnAggregation.
        """
        self._local_column_guid = local_column_guid

    @property
    def count(self) -> "int":
        """Gets the count of this GrantaServerApiAggregationsLocalColumnAggregation.
        The number of records that have a populated (applicable) value for this local column.

        Returns
        -------
        int
            The count of this GrantaServerApiAggregationsLocalColumnAggregation.
        """
        return self._count

    @count.setter
    def count(self, count: "int") -> None:
        """Sets the count of this GrantaServerApiAggregationsLocalColumnAggregation.
        The number of records that have a populated (applicable) value for this local column.

        Parameters
        ----------
        count: int
            The count of this GrantaServerApiAggregationsLocalColumnAggregation.
        """
        self._count = count

    @classmethod
    def get_real_child_model(cls, data: ModelBase) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[cls._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen,
        # so we have to extract it from the JSON reference
        return cls.discriminator_value_class_map.get(discriminator_value).rsplit(
            "/", 1
        )[-1]

    @classmethod
    def _get_discriminator_field_name(cls) -> str:
        name_tokens = cls.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

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
        if issubclass(GrantaServerApiAggregationsLocalColumnAggregation, dict):
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
        if not isinstance(other, GrantaServerApiAggregationsLocalColumnAggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other