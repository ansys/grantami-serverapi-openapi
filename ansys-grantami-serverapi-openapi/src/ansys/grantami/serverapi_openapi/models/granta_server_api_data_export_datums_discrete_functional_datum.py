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

from ansys.grantami.serverapi_openapi.models.granta_server_api_data_export_datums_applicable_datum import (
    GrantaServerApiDataExportDatumsApplicableDatum,
)  # noqa: F401

if TYPE_CHECKING:
    from . import *


class GrantaServerApiDataExportDatumsDiscreteFunctionalDatum(
    GrantaServerApiDataExportDatumsApplicableDatum
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
    discriminator_class_map: Dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types = {
        "attribute_guid": "str",
        "attribute_identity": "int",
        "datum_type": "str",
        "meta_datums": "list[GrantaServerApiDataExportDatumsDatum]",
        "not_applicable": "str",
        "parameters": "list[GrantaServerApiFunctionalDatumParameterInfo]",
        "x_axis_parameter": "GrantaServerApiFunctionalDatumParameterInfo",
    }

    attribute_map = {
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "datum_type": "datumType",
        "meta_datums": "metaDatums",
        "not_applicable": "notApplicable",
        "parameters": "parameters",
        "x_axis_parameter": "xAxisParameter",
    }

    subtype_mapping = {
        "xAxisParameter": "GrantaServerApiFunctionalDatumParameterInfo",
        "parameters": "GrantaServerApiFunctionalDatumParameterInfo",
    }

    discriminator_value_class_map = {
        "grid".lower(): "#/components/schemas/GrantaServerApiDataExportDatumsDiscreteFunctionalGridDatum",
        "series".lower(): "#/components/schemas/GrantaServerApiDataExportDatumsDiscreteFunctionalSeriesDatum",
    }

    discriminator = "graph_type"

    def __init__(
        self,
        *,
        attribute_guid: "Optional[str]" = None,
        attribute_identity: "Optional[int]" = None,
        datum_type: "str" = "discreteFunctional",
        meta_datums: "Optional[List[GrantaServerApiDataExportDatumsDatum]]" = None,
        not_applicable: "str" = "applicable",
        parameters: "Optional[List[GrantaServerApiFunctionalDatumParameterInfo]]" = None,
        x_axis_parameter: "Optional[GrantaServerApiFunctionalDatumParameterInfo]" = None,
    ) -> None:
        """GrantaServerApiDataExportDatumsDiscreteFunctionalDatum - a model defined in Swagger

        Parameters
        ----------
            attribute_guid: str, optional
            attribute_identity: int, optional
            datum_type: str
            meta_datums: List[GrantaServerApiDataExportDatumsDatum], optional
            not_applicable: str
            parameters: List[GrantaServerApiFunctionalDatumParameterInfo], optional
            x_axis_parameter: GrantaServerApiFunctionalDatumParameterInfo, optional
        """
        super().__init__(
            attribute_guid=attribute_guid,
            attribute_identity=attribute_identity,
            meta_datums=meta_datums,
            not_applicable=not_applicable,
        )
        self._datum_type = None
        self._x_axis_parameter = None
        self._parameters = None

        self.datum_type = datum_type
        if x_axis_parameter is not None:
            self.x_axis_parameter = x_axis_parameter
        if parameters is not None:
            self.parameters = parameters

    @property
    def datum_type(self) -> "str":
        """Gets the datum_type of this GrantaServerApiDataExportDatumsDiscreteFunctionalDatum.

        Returns
        -------
        str
            The datum_type of this GrantaServerApiDataExportDatumsDiscreteFunctionalDatum.
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type: "str") -> None:
        """Sets the datum_type of this GrantaServerApiDataExportDatumsDiscreteFunctionalDatum.

        Parameters
        ----------
        datum_type: str
            The datum_type of this GrantaServerApiDataExportDatumsDiscreteFunctionalDatum.
        """
        if datum_type is None:
            raise ValueError("Invalid value for 'datum_type', must not be 'None'")
        self._datum_type = datum_type

    @property
    def x_axis_parameter(self) -> "GrantaServerApiFunctionalDatumParameterInfo":
        """Gets the x_axis_parameter of this GrantaServerApiDataExportDatumsDiscreteFunctionalDatum.

        Returns
        -------
        GrantaServerApiFunctionalDatumParameterInfo
            The x_axis_parameter of this GrantaServerApiDataExportDatumsDiscreteFunctionalDatum.
        """
        return self._x_axis_parameter

    @x_axis_parameter.setter
    def x_axis_parameter(
        self, x_axis_parameter: "GrantaServerApiFunctionalDatumParameterInfo"
    ) -> None:
        """Sets the x_axis_parameter of this GrantaServerApiDataExportDatumsDiscreteFunctionalDatum.

        Parameters
        ----------
        x_axis_parameter: GrantaServerApiFunctionalDatumParameterInfo
            The x_axis_parameter of this GrantaServerApiDataExportDatumsDiscreteFunctionalDatum.
        """
        self._x_axis_parameter = x_axis_parameter

    @property
    def parameters(self) -> "list[GrantaServerApiFunctionalDatumParameterInfo]":
        """Gets the parameters of this GrantaServerApiDataExportDatumsDiscreteFunctionalDatum.

        Returns
        -------
        list[GrantaServerApiFunctionalDatumParameterInfo]
            The parameters of this GrantaServerApiDataExportDatumsDiscreteFunctionalDatum.
        """
        return self._parameters

    @parameters.setter
    def parameters(
        self, parameters: "list[GrantaServerApiFunctionalDatumParameterInfo]"
    ) -> None:
        """Sets the parameters of this GrantaServerApiDataExportDatumsDiscreteFunctionalDatum.

        Parameters
        ----------
        parameters: list[GrantaServerApiFunctionalDatumParameterInfo]
            The parameters of this GrantaServerApiDataExportDatumsDiscreteFunctionalDatum.
        """
        self._parameters = parameters

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
        if issubclass(GrantaServerApiDataExportDatumsDiscreteFunctionalDatum, dict):
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
            other, GrantaServerApiDataExportDatumsDiscreteFunctionalDatum
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
