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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaEnabledLicensesInfo(ModelBase):
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
        "is_flex_licensing_enabled": "bool",
        "mi_server_enabled": "bool",
        "ml_enabled": "bool",
        "plm_sync_enabled": "bool",
        "restricted_substances_ba_enabled": "bool",
        "sustainability_enabled_enabled": "bool",
        "workflow_advanced_enabled": "bool",
        "expiry_date": "datetime",
    }

    attribute_map: dict[str, str] = {
        "is_flex_licensing_enabled": "isFlexLicensingEnabled",
        "mi_server_enabled": "miServerEnabled",
        "ml_enabled": "MLEnabled",
        "plm_sync_enabled": "PLMSyncEnabled",
        "restricted_substances_ba_enabled": "restrictedSubstancesBAEnabled",
        "sustainability_enabled_enabled": "sustainabilityEnabledEnabled",
        "workflow_advanced_enabled": "workflowAdvancedEnabled",
        "expiry_date": "expiryDate",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        is_flex_licensing_enabled: "bool",
        mi_server_enabled: "bool",
        ml_enabled: "bool",
        plm_sync_enabled: "bool",
        restricted_substances_ba_enabled: "bool",
        sustainability_enabled_enabled: "bool",
        workflow_advanced_enabled: "bool",
        expiry_date: "datetime | None | Unset_Type" = Unset,
    ) -> None:
        """GsaEnabledLicensesInfo - a model defined in Swagger

        Parameters
        ----------
        is_flex_licensing_enabled: bool
        mi_server_enabled: bool
        ml_enabled: bool
        plm_sync_enabled: bool
        restricted_substances_ba_enabled: bool
        sustainability_enabled_enabled: bool
        workflow_advanced_enabled: bool
        expiry_date: datetime | None, optional
        """
        self._is_flex_licensing_enabled: bool
        self._mi_server_enabled: bool
        self._workflow_advanced_enabled: bool
        self._restricted_substances_ba_enabled: bool
        self._sustainability_enabled_enabled: bool
        self._plm_sync_enabled: bool
        self._ml_enabled: bool
        self._expiry_date: datetime | None | Unset_Type = Unset

        self.is_flex_licensing_enabled = is_flex_licensing_enabled
        self.mi_server_enabled = mi_server_enabled
        self.workflow_advanced_enabled = workflow_advanced_enabled
        self.restricted_substances_ba_enabled = restricted_substances_ba_enabled
        self.sustainability_enabled_enabled = sustainability_enabled_enabled
        self.plm_sync_enabled = plm_sync_enabled
        self.ml_enabled = ml_enabled
        if expiry_date is not Unset:
            self.expiry_date = expiry_date

    @property
    def is_flex_licensing_enabled(self) -> "bool":
        """Gets the is_flex_licensing_enabled of this GsaEnabledLicensesInfo.
        Gets a flag indicating whether FlexLM licensing is enabled. If true, MI is in Ansys  licensing mode. If false, MI is in classic licensing mode.

        Returns
        -------
        bool
            The is_flex_licensing_enabled of this GsaEnabledLicensesInfo.
        """
        return self._is_flex_licensing_enabled

    @is_flex_licensing_enabled.setter
    def is_flex_licensing_enabled(self, is_flex_licensing_enabled: "bool") -> None:
        """Sets the is_flex_licensing_enabled of this GsaEnabledLicensesInfo.
        Gets a flag indicating whether FlexLM licensing is enabled. If true, MI is in Ansys  licensing mode. If false, MI is in classic licensing mode.

        Parameters
        ----------
        is_flex_licensing_enabled: bool
            The is_flex_licensing_enabled of this GsaEnabledLicensesInfo.
        """
        # Field is not nullable
        if is_flex_licensing_enabled is None:
            raise ValueError("Invalid value for 'is_flex_licensing_enabled', must not be 'None'")
        # Field is required
        if is_flex_licensing_enabled is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'is_flex_licensing_enabled', must not be 'Unset'")
        self._is_flex_licensing_enabled = is_flex_licensing_enabled

    @property
    def mi_server_enabled(self) -> "bool":
        """Gets the mi_server_enabled of this GsaEnabledLicensesInfo.
        Gets a flag indicating whether MI Server is enabled. In Ansys licensing mode, this corresponds  to an MI Server license having been checked out. In classic licensing mode, it is set to true.

        Returns
        -------
        bool
            The mi_server_enabled of this GsaEnabledLicensesInfo.
        """
        return self._mi_server_enabled

    @mi_server_enabled.setter
    def mi_server_enabled(self, mi_server_enabled: "bool") -> None:
        """Sets the mi_server_enabled of this GsaEnabledLicensesInfo.
        Gets a flag indicating whether MI Server is enabled. In Ansys licensing mode, this corresponds  to an MI Server license having been checked out. In classic licensing mode, it is set to true.

        Parameters
        ----------
        mi_server_enabled: bool
            The mi_server_enabled of this GsaEnabledLicensesInfo.
        """
        # Field is not nullable
        if mi_server_enabled is None:
            raise ValueError("Invalid value for 'mi_server_enabled', must not be 'None'")
        # Field is required
        if mi_server_enabled is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'mi_server_enabled', must not be 'Unset'")
        self._mi_server_enabled = mi_server_enabled

    @property
    def workflow_advanced_enabled(self) -> "bool":
        """Gets the workflow_advanced_enabled of this GsaEnabledLicensesInfo.
        Gets a flag indicating whether advanced workflow features are enabled. In Ansys  licensing mode, this corresponds to a Workflow Advanced license having been checked out. In classic licensing mode, it  is set to true.

        Returns
        -------
        bool
            The workflow_advanced_enabled of this GsaEnabledLicensesInfo.
        """
        return self._workflow_advanced_enabled

    @workflow_advanced_enabled.setter
    def workflow_advanced_enabled(self, workflow_advanced_enabled: "bool") -> None:
        """Sets the workflow_advanced_enabled of this GsaEnabledLicensesInfo.
        Gets a flag indicating whether advanced workflow features are enabled. In Ansys  licensing mode, this corresponds to a Workflow Advanced license having been checked out. In classic licensing mode, it  is set to true.

        Parameters
        ----------
        workflow_advanced_enabled: bool
            The workflow_advanced_enabled of this GsaEnabledLicensesInfo.
        """
        # Field is not nullable
        if workflow_advanced_enabled is None:
            raise ValueError("Invalid value for 'workflow_advanced_enabled', must not be 'None'")
        # Field is required
        if workflow_advanced_enabled is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'workflow_advanced_enabled', must not be 'Unset'")
        self._workflow_advanced_enabled = workflow_advanced_enabled

    @property
    def restricted_substances_ba_enabled(self) -> "bool":
        """Gets the restricted_substances_ba_enabled of this GsaEnabledLicensesInfo.
        Gets a flag indicating whether features associated with the Restricted Substances Analytics  product are enabled. In Ansys licensing mode, this corresponds to a Restricted Substances Analytics license (granta_mi_rsba) having been checked  out. In classic licensing mode, it is set to false.

        Returns
        -------
        bool
            The restricted_substances_ba_enabled of this GsaEnabledLicensesInfo.
        """
        return self._restricted_substances_ba_enabled

    @restricted_substances_ba_enabled.setter
    def restricted_substances_ba_enabled(self, restricted_substances_ba_enabled: "bool") -> None:
        """Sets the restricted_substances_ba_enabled of this GsaEnabledLicensesInfo.
        Gets a flag indicating whether features associated with the Restricted Substances Analytics  product are enabled. In Ansys licensing mode, this corresponds to a Restricted Substances Analytics license (granta_mi_rsba) having been checked  out. In classic licensing mode, it is set to false.

        Parameters
        ----------
        restricted_substances_ba_enabled: bool
            The restricted_substances_ba_enabled of this GsaEnabledLicensesInfo.
        """
        # Field is not nullable
        if restricted_substances_ba_enabled is None:
            raise ValueError(
                "Invalid value for 'restricted_substances_ba_enabled', must not be 'None'"
            )
        # Field is required
        if restricted_substances_ba_enabled is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'restricted_substances_ba_enabled', must not be 'Unset'"
            )
        self._restricted_substances_ba_enabled = restricted_substances_ba_enabled

    @property
    def sustainability_enabled_enabled(self) -> "bool":
        """Gets the sustainability_enabled_enabled of this GsaEnabledLicensesInfo.
        Gets a flag indicating whether features associated with the Sustainability Analytics  product are enabled. In Ansys licensing mode, this corresponds to a Sustainability Analytics license (granta_mi_sus) having been checked  out. In classic licensing mode, it is set to false.

        Returns
        -------
        bool
            The sustainability_enabled_enabled of this GsaEnabledLicensesInfo.
        """
        return self._sustainability_enabled_enabled

    @sustainability_enabled_enabled.setter
    def sustainability_enabled_enabled(self, sustainability_enabled_enabled: "bool") -> None:
        """Sets the sustainability_enabled_enabled of this GsaEnabledLicensesInfo.
        Gets a flag indicating whether features associated with the Sustainability Analytics  product are enabled. In Ansys licensing mode, this corresponds to a Sustainability Analytics license (granta_mi_sus) having been checked  out. In classic licensing mode, it is set to false.

        Parameters
        ----------
        sustainability_enabled_enabled: bool
            The sustainability_enabled_enabled of this GsaEnabledLicensesInfo.
        """
        # Field is not nullable
        if sustainability_enabled_enabled is None:
            raise ValueError(
                "Invalid value for 'sustainability_enabled_enabled', must not be 'None'"
            )
        # Field is required
        if sustainability_enabled_enabled is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'sustainability_enabled_enabled', must not be 'Unset'"
            )
        self._sustainability_enabled_enabled = sustainability_enabled_enabled

    @property
    def plm_sync_enabled(self) -> "bool":
        """Gets the plm_sync_enabled of this GsaEnabledLicensesInfo.
        Gets a flag indicating whether features associated with the PLM Sync (notably MI Enterprise Connect) are enabled.  In Ansys licensing mode, this corresponds to a PLM sync license having been checked out. In classic licensing mode, it is set to true.

        Returns
        -------
        bool
            The plm_sync_enabled of this GsaEnabledLicensesInfo.
        """
        return self._plm_sync_enabled

    @plm_sync_enabled.setter
    def plm_sync_enabled(self, plm_sync_enabled: "bool") -> None:
        """Sets the plm_sync_enabled of this GsaEnabledLicensesInfo.
        Gets a flag indicating whether features associated with the PLM Sync (notably MI Enterprise Connect) are enabled.  In Ansys licensing mode, this corresponds to a PLM sync license having been checked out. In classic licensing mode, it is set to true.

        Parameters
        ----------
        plm_sync_enabled: bool
            The plm_sync_enabled of this GsaEnabledLicensesInfo.
        """
        # Field is not nullable
        if plm_sync_enabled is None:
            raise ValueError("Invalid value for 'plm_sync_enabled', must not be 'None'")
        # Field is required
        if plm_sync_enabled is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'plm_sync_enabled', must not be 'Unset'")
        self._plm_sync_enabled = plm_sync_enabled

    @property
    def ml_enabled(self) -> "bool":
        """Gets the ml_enabled of this GsaEnabledLicensesInfo.
        Gets a flag indicating whether features associated with the ML (Machine Learning) are enabled.  In Ansys licensing mode, this corresponds to a ML license having been checked out. In classic licensing mode, it is set to false.

        Returns
        -------
        bool
            The ml_enabled of this GsaEnabledLicensesInfo.
        """
        return self._ml_enabled

    @ml_enabled.setter
    def ml_enabled(self, ml_enabled: "bool") -> None:
        """Sets the ml_enabled of this GsaEnabledLicensesInfo.
        Gets a flag indicating whether features associated with the ML (Machine Learning) are enabled.  In Ansys licensing mode, this corresponds to a ML license having been checked out. In classic licensing mode, it is set to false.

        Parameters
        ----------
        ml_enabled: bool
            The ml_enabled of this GsaEnabledLicensesInfo.
        """
        # Field is not nullable
        if ml_enabled is None:
            raise ValueError("Invalid value for 'ml_enabled', must not be 'None'")
        # Field is required
        if ml_enabled is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'ml_enabled', must not be 'Unset'")
        self._ml_enabled = ml_enabled

    @property
    def expiry_date(self) -> "datetime | None | Unset_Type":
        """Gets the expiry_date of this GsaEnabledLicensesInfo.
        Gets expiry date of Server license.

        Returns
        -------
        datetime | None | Unset_Type
            The expiry_date of this GsaEnabledLicensesInfo.
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date: "datetime | None | Unset_Type") -> None:
        """Sets the expiry_date of this GsaEnabledLicensesInfo.
        Gets expiry date of Server license.

        Parameters
        ----------
        expiry_date: datetime | None | Unset_Type
            The expiry_date of this GsaEnabledLicensesInfo.
        """
        self._expiry_date = expiry_date

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
        if not isinstance(other, GsaEnabledLicensesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
