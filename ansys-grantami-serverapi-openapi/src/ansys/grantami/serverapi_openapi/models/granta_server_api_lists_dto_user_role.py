"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from enum import Enum


class GrantaServerApiListsDtoUserRole(Enum):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Allowed Enum values
    """
    NONE = "None"
    OWNER = "Owner"
    SUBSCRIBER = "Subscriber"
    CURATOR = "Curator"
    ADMINISTRATOR = "Administrator"
    PUBLISHER = "Publisher"
