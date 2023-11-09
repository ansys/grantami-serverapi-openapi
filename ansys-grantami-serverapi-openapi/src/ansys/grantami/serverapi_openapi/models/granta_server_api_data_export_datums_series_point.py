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


class GrantaServerApiDataExportDatumsSeriesPoint(ModelBase):
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
        "x": "float",
        "x_name": "str",
        "y_high": "float",
        "y_low": "float",
    }

    attribute_map = {
        "x": "x",
        "x_name": "xName",
        "y_high": "yHigh",
        "y_low": "yLow",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        x: "Optional[float]" = None,
        x_name: "Optional[str]" = None,
        y_high: "Optional[float]" = None,
        y_low: "Optional[float]" = None,
    ) -> None:
        """GrantaServerApiDataExportDatumsSeriesPoint - a model defined in Swagger

        Parameters
        ----------
            x: float, optional
            x_name: str, optional
            y_high: float, optional
            y_low: float, optional
        """
        self._x = None
        self._x_name = None
        self._y_low = None
        self._y_high = None

        if x is not None:
            self.x = x
        if x_name is not None:
            self.x_name = x_name
        if y_low is not None:
            self.y_low = y_low
        if y_high is not None:
            self.y_high = y_high

    @property
    def x(self) -> "float":
        """Gets the x of this GrantaServerApiDataExportDatumsSeriesPoint.

        Returns
        -------
        float
            The x of this GrantaServerApiDataExportDatumsSeriesPoint.
        """
        return self._x

    @x.setter
    def x(self, x: "float") -> None:
        """Sets the x of this GrantaServerApiDataExportDatumsSeriesPoint.

        Parameters
        ----------
        x: float
            The x of this GrantaServerApiDataExportDatumsSeriesPoint.
        """
        self._x = x

    @property
    def x_name(self) -> "str":
        """Gets the x_name of this GrantaServerApiDataExportDatumsSeriesPoint.

        Returns
        -------
        str
            The x_name of this GrantaServerApiDataExportDatumsSeriesPoint.
        """
        return self._x_name

    @x_name.setter
    def x_name(self, x_name: "str") -> None:
        """Sets the x_name of this GrantaServerApiDataExportDatumsSeriesPoint.

        Parameters
        ----------
        x_name: str
            The x_name of this GrantaServerApiDataExportDatumsSeriesPoint.
        """
        self._x_name = x_name

    @property
    def y_low(self) -> "float":
        """Gets the y_low of this GrantaServerApiDataExportDatumsSeriesPoint.

        Returns
        -------
        float
            The y_low of this GrantaServerApiDataExportDatumsSeriesPoint.
        """
        return self._y_low

    @y_low.setter
    def y_low(self, y_low: "float") -> None:
        """Sets the y_low of this GrantaServerApiDataExportDatumsSeriesPoint.

        Parameters
        ----------
        y_low: float
            The y_low of this GrantaServerApiDataExportDatumsSeriesPoint.
        """
        self._y_low = y_low

    @property
    def y_high(self) -> "float":
        """Gets the y_high of this GrantaServerApiDataExportDatumsSeriesPoint.

        Returns
        -------
        float
            The y_high of this GrantaServerApiDataExportDatumsSeriesPoint.
        """
        return self._y_high

    @y_high.setter
    def y_high(self, y_high: "float") -> None:
        """Sets the y_high of this GrantaServerApiDataExportDatumsSeriesPoint.

        Parameters
        ----------
        y_high: float
            The y_high of this GrantaServerApiDataExportDatumsSeriesPoint.
        """
        self._y_high = y_high

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
        if issubclass(GrantaServerApiDataExportDatumsSeriesPoint, dict):
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
        if not isinstance(other, GrantaServerApiDataExportDatumsSeriesPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
