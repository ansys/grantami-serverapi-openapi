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


class GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute(ModelBase):
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
        "name": "str",
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "guid": "str",
        "help_path": "str",
    }

    attribute_map = {
        "name": "name",
        "about_attribute": "aboutAttribute",
        "default_threshold_type": "defaultThresholdType",
        "guid": "guid",
        "help_path": "helpPath",
    }

    subtype_mapping = {
        "defaultThresholdType": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "aboutAttribute": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
    }

    discriminator_value_class_map = {
        "point".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute",
        "integer".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateIntegerAttribute",
        "range".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateRangeAttribute",
        "logical".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateLogicalAttribute",
        "shortText".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute",
        "longText".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateLongTextAttribute",
        "dateTime".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateDateTimeAttribute",
        "discrete".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteAttribute",
        "hyperlink".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateHyperlinkAttribute",
        "file".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateFileAttribute",
        "picture".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreatePictureAttribute",
        "link".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateTabularAttribute",
        "floatFunctional".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute",
        "discreteFunctional".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteFunctionalAttribute",
        "mathsFunctional".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateMathsFunctionalAttribute",
    }

    discriminator = "type"

    def __init__(
        self,
        *,
        name: "str",
        about_attribute: "Optional[GrantaServerApiSchemaSlimEntitiesSlimEntity]" = None,
        default_threshold_type: "Optional[GrantaServerApiSchemaAttributesAttributeThresholdType]" = None,
        guid: "Optional[str]" = None,
        help_path: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute - a model defined in Swagger

        Parameters
        ----------
            name: str
            about_attribute: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
            default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType, optional
            guid: str, optional
            help_path: str, optional
        """
        self._default_threshold_type = None
        self._help_path = None
        self._about_attribute = None
        self._name = None
        self._guid = None

        if default_threshold_type is not None:
            self.default_threshold_type = default_threshold_type
        if help_path is not None:
            self.help_path = help_path
        if about_attribute is not None:
            self.about_attribute = about_attribute
        self.name = name
        if guid is not None:
            self.guid = guid

    @property
    def default_threshold_type(
        self,
    ) -> "GrantaServerApiSchemaAttributesAttributeThresholdType":
        """Gets the default_threshold_type of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.

        Returns
        -------
        GrantaServerApiSchemaAttributesAttributeThresholdType
            The default_threshold_type of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.
        """
        return self._default_threshold_type

    @default_threshold_type.setter
    def default_threshold_type(
        self,
        default_threshold_type: "GrantaServerApiSchemaAttributesAttributeThresholdType",
    ) -> None:
        """Sets the default_threshold_type of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.

        Parameters
        ----------
        default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType
            The default_threshold_type of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.
        """
        self._default_threshold_type = default_threshold_type

    @property
    def help_path(self) -> "str":
        """Gets the help_path of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.

        Returns
        -------
        str
            The help_path of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.
        """
        return self._help_path

    @help_path.setter
    def help_path(self, help_path: "str") -> None:
        """Sets the help_path of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.

        Parameters
        ----------
        help_path: str
            The help_path of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.
        """
        self._help_path = help_path

    @property
    def about_attribute(self) -> "GrantaServerApiSchemaSlimEntitiesSlimEntity":
        """Gets the about_attribute of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimEntity
            The about_attribute of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.
        """
        return self._about_attribute

    @about_attribute.setter
    def about_attribute(
        self, about_attribute: "GrantaServerApiSchemaSlimEntitiesSlimEntity"
    ) -> None:
        """Sets the about_attribute of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.

        Parameters
        ----------
        about_attribute: GrantaServerApiSchemaSlimEntitiesSlimEntity
            The about_attribute of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.
        """
        self._about_attribute = about_attribute

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.
        """
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.
        """
        self._guid = guid

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
        if issubclass(
            GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute, dict
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
            other, GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other