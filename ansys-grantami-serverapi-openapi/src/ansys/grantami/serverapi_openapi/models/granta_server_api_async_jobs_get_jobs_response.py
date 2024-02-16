"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    BinaryIO,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiAsyncJobsGetJobsResponse(ModelBase):  # type: ignore[misc]
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
    swagger_types: Dict[str, str] = {
        "results": "list[GrantaServerApiAsyncJobsJob]",
        "total_result_count": "int",
    }

    attribute_map: Dict[str, str] = {
        "results": "results",
        "total_result_count": "totalResultCount",
    }

    subtype_mapping: Dict[str, str] = {
        "results": "GrantaServerApiAsyncJobsJob",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        results: "Optional[List[GrantaServerApiAsyncJobsJob]]" = None,
        total_result_count: "Optional[int]" = None,
    ) -> None:
        """GrantaServerApiAsyncJobsGetJobsResponse - a model defined in Swagger

        Parameters
        ----------
            results: List[GrantaServerApiAsyncJobsJob], optional
            total_result_count: int, optional
        """
        self._total_result_count = None
        self._results = None

        if total_result_count is not None:
            self.total_result_count = total_result_count
        if results is not None:
            self.results = results

    @property
    def total_result_count(self) -> "Optional[int]":
        """Gets the total_result_count of this GrantaServerApiAsyncJobsGetJobsResponse.

        Returns
        -------
        int
            The total_result_count of this GrantaServerApiAsyncJobsGetJobsResponse.
        """
        return self._total_result_count

    @total_result_count.setter
    def total_result_count(self, total_result_count: "Optional[int]") -> None:
        """Sets the total_result_count of this GrantaServerApiAsyncJobsGetJobsResponse.

        Parameters
        ----------
        total_result_count: int
            The total_result_count of this GrantaServerApiAsyncJobsGetJobsResponse.
        """
        self._total_result_count = total_result_count

    @property
    def results(self) -> "Optional[List[GrantaServerApiAsyncJobsJob]]":
        """Gets the results of this GrantaServerApiAsyncJobsGetJobsResponse.

        Returns
        -------
        list[GrantaServerApiAsyncJobsJob]
            The results of this GrantaServerApiAsyncJobsGetJobsResponse.
        """
        return self._results

    @results.setter
    def results(self, results: "Optional[List[GrantaServerApiAsyncJobsJob]]") -> None:
        """Sets the results of this GrantaServerApiAsyncJobsGetJobsResponse.

        Parameters
        ----------
        results: List[GrantaServerApiAsyncJobsJob]
            The results of this GrantaServerApiAsyncJobsGetJobsResponse.
        """
        self._results = results

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

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()  # type: ignore[no-any-return]

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiAsyncJobsGetJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
