# Copyright (C) 2023 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaSearchClusterStatus(ModelBase):
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
        "cluster_unavailable": "bool",
        "disk_status": "dict(str, GsaDiskStatus)",
        "disk_threshold": "str",
        "disk_threshold_max_headroom": "str",
    }

    attribute_map: dict[str, str] = {
        "cluster_unavailable": "clusterUnavailable",
        "disk_status": "diskStatus",
        "disk_threshold": "diskThreshold",
        "disk_threshold_max_headroom": "diskThresholdMaxHeadroom",
    }

    subtype_mapping: dict[str, str] = {
        "diskStatus": "GsaDiskStatus",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        cluster_unavailable: "Union[bool, None, Unset_Type]" = Unset,
        disk_status: "Union[dict[str, GsaDiskStatus], None, Unset_Type]" = Unset,
        disk_threshold: "Union[str, None, Unset_Type]" = Unset,
        disk_threshold_max_headroom: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaSearchClusterStatus - a model defined in Swagger

        Parameters
        ----------
        cluster_unavailable: bool, optional
        disk_status: dict[str, GsaDiskStatus], optional
        disk_threshold: str, optional
        disk_threshold_max_headroom: str, optional
        """
        self._disk_status: Union[dict[str, GsaDiskStatus], None, Unset_Type] = Unset
        self._disk_threshold: Union[str, None, Unset_Type] = Unset
        self._disk_threshold_max_headroom: Union[str, None, Unset_Type] = Unset
        self._cluster_unavailable: Union[bool, None, Unset_Type] = Unset

        if disk_status is not Unset:
            self.disk_status = disk_status
        if disk_threshold is not Unset:
            self.disk_threshold = disk_threshold
        if disk_threshold_max_headroom is not Unset:
            self.disk_threshold_max_headroom = disk_threshold_max_headroom
        if cluster_unavailable is not Unset:
            self.cluster_unavailable = cluster_unavailable

    @property
    def disk_status(self) -> "Union[dict[str, GsaDiskStatus], None, Unset_Type]":
        """Gets the disk_status of this GsaSearchClusterStatus.
        The status of the disk compared to the Elasticsearch space thresholds.

        Returns
        -------
        Union[dict[str, GsaDiskStatus], None, Unset_Type]
            The disk_status of this GsaSearchClusterStatus.
        """
        return self._disk_status

    @disk_status.setter
    def disk_status(self, disk_status: "Union[dict[str, GsaDiskStatus], None, Unset_Type]") -> None:
        """Sets the disk_status of this GsaSearchClusterStatus.
        The status of the disk compared to the Elasticsearch space thresholds.

        Parameters
        ----------
        disk_status: Union[dict[str, GsaDiskStatus], None, Unset_Type]
            The disk_status of this GsaSearchClusterStatus.
        """
        self._disk_status = disk_status

    @property
    def disk_threshold(self) -> "Union[str, None, Unset_Type]":
        """Gets the disk_threshold of this GsaSearchClusterStatus.
        The 'flood stage' disk usage threshold from Elasticsearch. Elasticsearch enforces a read-only block on indexes once this is exceeded.

        Returns
        -------
        Union[str, None, Unset_Type]
            The disk_threshold of this GsaSearchClusterStatus.
        """
        return self._disk_threshold

    @disk_threshold.setter
    def disk_threshold(self, disk_threshold: "Union[str, None, Unset_Type]") -> None:
        """Sets the disk_threshold of this GsaSearchClusterStatus.
        The 'flood stage' disk usage threshold from Elasticsearch. Elasticsearch enforces a read-only block on indexes once this is exceeded.

        Parameters
        ----------
        disk_threshold: Union[str, None, Unset_Type]
            The disk_threshold of this GsaSearchClusterStatus.
        """
        self._disk_threshold = disk_threshold

    @property
    def disk_threshold_max_headroom(self) -> "Union[str, None, Unset_Type]":
        """Gets the disk_threshold_max_headroom of this GsaSearchClusterStatus.
        The maximum headroom of the Elasticsearch 'flood stage'. If set, nodes with at least this amount of space will not be set as read-only even if they exceed the disk threshold

        Returns
        -------
        Union[str, None, Unset_Type]
            The disk_threshold_max_headroom of this GsaSearchClusterStatus.
        """
        return self._disk_threshold_max_headroom

    @disk_threshold_max_headroom.setter
    def disk_threshold_max_headroom(
        self, disk_threshold_max_headroom: "Union[str, None, Unset_Type]"
    ) -> None:
        """Sets the disk_threshold_max_headroom of this GsaSearchClusterStatus.
        The maximum headroom of the Elasticsearch 'flood stage'. If set, nodes with at least this amount of space will not be set as read-only even if they exceed the disk threshold

        Parameters
        ----------
        disk_threshold_max_headroom: Union[str, None, Unset_Type]
            The disk_threshold_max_headroom of this GsaSearchClusterStatus.
        """
        self._disk_threshold_max_headroom = disk_threshold_max_headroom

    @property
    def cluster_unavailable(self) -> "Union[bool, None, Unset_Type]":
        """Gets the cluster_unavailable of this GsaSearchClusterStatus.
        True if the cluster could not be contacted.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The cluster_unavailable of this GsaSearchClusterStatus.
        """
        return self._cluster_unavailable

    @cluster_unavailable.setter
    def cluster_unavailable(self, cluster_unavailable: "Union[bool, None, Unset_Type]") -> None:
        """Sets the cluster_unavailable of this GsaSearchClusterStatus.
        True if the cluster could not be contacted.

        Parameters
        ----------
        cluster_unavailable: Union[bool, None, Unset_Type]
            The cluster_unavailable of this GsaSearchClusterStatus.
        """
        self._cluster_unavailable = cluster_unavailable

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
        if not isinstance(other, GsaSearchClusterStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
