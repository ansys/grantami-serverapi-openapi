"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.models.gsa_aggregation_datum import GsaAggregationDatum  # noqa: F401
from ansys.grantami.serverapi_openapi.models.gsa_aggregation_datum_type import GsaAggregationDatumType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaFloatFunctionalAggregation(GsaAggregationDatum):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes
    ----------
    swagger_types: dict[str, str]
        The key is attribute name and the value is attribute type.
    attribute_map: dict[str, str]
        The key is attribute name and the value is json key in definition.
    subtype_mapping: dict[str, str]
        The key is the unmangled property name and the value is the corresponding type.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "datum_type": "GsaAggregationDatumType",
        "grid_graphs": "GsaFloatFunctionalGridGraphAggregation",
        "series_graphs": "GsaFloatFunctionalSeriesGraphAggregation",
    }

    attribute_map: dict[str, str] = {
        "datum_type": "datumType",
        "grid_graphs": "gridGraphs",
        "series_graphs": "seriesGraphs",
    }

    subtype_mapping: dict[str, str] = {
        "seriesGraphs": "GsaFloatFunctionalSeriesGraphAggregation",
        "gridGraphs": "GsaFloatFunctionalGridGraphAggregation",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, datum_type: "GsaAggregationDatumType" = GsaAggregationDatumType.FLOATFUNCTIONALGRAPH, grid_graphs: "Union[GsaFloatFunctionalGridGraphAggregation, Unset_Type]" = Unset, series_graphs: "Union[GsaFloatFunctionalSeriesGraphAggregation, Unset_Type]" = Unset,) -> None:
        """GsaFloatFunctionalAggregation - a model defined in Swagger

        Parameters
        ----------
        datum_type: GsaAggregationDatumType
        grid_graphs: GsaFloatFunctionalGridGraphAggregation, optional
        series_graphs: GsaFloatFunctionalSeriesGraphAggregation, optional
        """
        super().__init__(datum_type=datum_type)
        self._series_graphs: Union[GsaFloatFunctionalSeriesGraphAggregation, Unset_Type] = Unset
        self._grid_graphs: Union[GsaFloatFunctionalGridGraphAggregation, Unset_Type] = Unset

        if series_graphs is not Unset:
            self.series_graphs = series_graphs
        if grid_graphs is not Unset:
            self.grid_graphs = grid_graphs

    @property
    def series_graphs(self) -> "Union[GsaFloatFunctionalSeriesGraphAggregation, Unset_Type]":
        """Gets the series_graphs of this GsaFloatFunctionalAggregation.

        Returns
        -------
        Union[GsaFloatFunctionalSeriesGraphAggregation, Unset_Type]
            The series_graphs of this GsaFloatFunctionalAggregation.
        """
        return self._series_graphs

    @series_graphs.setter
    def series_graphs(self, series_graphs: "Union[GsaFloatFunctionalSeriesGraphAggregation, Unset_Type]") -> None:
        """Sets the series_graphs of this GsaFloatFunctionalAggregation.

        Parameters
        ----------
        series_graphs: Union[GsaFloatFunctionalSeriesGraphAggregation, Unset_Type]
            The series_graphs of this GsaFloatFunctionalAggregation.
        """
        # Field is not nullable
        if series_graphs is None:
            raise ValueError("Invalid value for 'series_graphs', must not be 'None'")
        self._series_graphs = series_graphs

    @property
    def grid_graphs(self) -> "Union[GsaFloatFunctionalGridGraphAggregation, Unset_Type]":
        """Gets the grid_graphs of this GsaFloatFunctionalAggregation.

        Returns
        -------
        Union[GsaFloatFunctionalGridGraphAggregation, Unset_Type]
            The grid_graphs of this GsaFloatFunctionalAggregation.
        """
        return self._grid_graphs

    @grid_graphs.setter
    def grid_graphs(self, grid_graphs: "Union[GsaFloatFunctionalGridGraphAggregation, Unset_Type]") -> None:
        """Sets the grid_graphs of this GsaFloatFunctionalAggregation.

        Parameters
        ----------
        grid_graphs: Union[GsaFloatFunctionalGridGraphAggregation, Unset_Type]
            The grid_graphs of this GsaFloatFunctionalAggregation.
        """
        # Field is not nullable
        if grid_graphs is None:
            raise ValueError("Invalid value for 'grid_graphs', must not be 'None'")
        self._grid_graphs = grid_graphs

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
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
        if not isinstance(other, GsaFloatFunctionalAggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

