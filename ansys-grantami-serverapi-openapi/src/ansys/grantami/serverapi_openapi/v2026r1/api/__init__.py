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

# flake8: noqa

# import API ABC
from ansys.openapi.common import ApiBase

# import apis into api package
from .activity_log_api import ActivityLogApi
from .aggregation_api import AggregationApi
from .blob_infos_api import BlobInfosApi
from .blobs_api import BlobsApi
from .bulk_api import BulkApi
from .data_api import DataApi
from .data_export_api import DataExportApi
from .data_updater_api import DataUpdaterApi
from .database_api import DatabaseApi
from .graph_api import GraphApi
from .help_location_api import HelpLocationApi
from .identities_api import IdentitiesApi
from .integration_api import IntegrationApi
from .job_queue_api import JobQueueApi
from .license_api import LicenseApi
from .list_audit_log_api import ListAuditLogApi
from .list_item_api import ListItemApi
from .list_management_api import ListManagementApi
from .list_permissions_api import ListPermissionsApi
from .metrics_api import MetricsApi
from .permission_based_access_control_api import PermissionBasedAccessControlApi
from .records___record_histories_api import RecordsRecordHistoriesApi
from .records___record_versions_api import RecordsRecordVersionsApi
from .schema___attributes_api import SchemaAttributesApi
from .schema___configurations_api import SchemaConfigurationsApi
from .schema___constants_api import SchemaConstantsApi
from .schema___data_rules_api import SchemaDataRulesApi
from .schema___databases_api import SchemaDatabasesApi
from .schema___discrete_types___discrete_values_api import SchemaDiscreteTypesDiscreteValuesApi
from .schema___discrete_types_api import SchemaDiscreteTypesApi
from .schema___display_names_api import SchemaDisplayNamesApi
from .schema___exporters_api import SchemaExportersApi
from .schema___expressions_api import SchemaExpressionsApi
from .schema___global_standard_names_api import SchemaGlobalStandardNamesApi
from .schema___help_files_api import SchemaHelpFilesApi
from .schema___home_pages_api import SchemaHomePagesApi
from .schema___layout_sections_api import SchemaLayoutSectionsApi
from .schema___layouts_api import SchemaLayoutsApi
from .schema___parameters_api import SchemaParametersApi
from .schema___profile_tables_api import SchemaProfileTablesApi
from .schema___profiles_api import SchemaProfilesApi
from .schema___record_link_groups_api import SchemaRecordLinkGroupsApi
from .schema___replacement_strings_api import SchemaReplacementStringsApi
from .schema___standard_names_api import SchemaStandardNamesApi
from .schema___subsets_api import SchemaSubsetsApi
from .schema___tables_api import SchemaTablesApi
from .schema___units_api import SchemaUnitsApi
from .schema_api import SchemaApi
from .search_api import SearchApi
from .server_manager_api import ServerManagerApi
from .status_api import StatusApi

__all__ = [
    "ApiBase",
    "ActivityLogApi",
    "AggregationApi",
    "BlobInfosApi",
    "BlobsApi",
    "BulkApi",
    "DataApi",
    "DataExportApi",
    "DataUpdaterApi",
    "DatabaseApi",
    "GraphApi",
    "HelpLocationApi",
    "IdentitiesApi",
    "IntegrationApi",
    "JobQueueApi",
    "LicenseApi",
    "ListAuditLogApi",
    "ListItemApi",
    "ListManagementApi",
    "ListPermissionsApi",
    "MetricsApi",
    "PermissionBasedAccessControlApi",
    "RecordsRecordHistoriesApi",
    "RecordsRecordVersionsApi",
    "SchemaApi",
    "SchemaAttributesApi",
    "SchemaConfigurationsApi",
    "SchemaConstantsApi",
    "SchemaDataRulesApi",
    "SchemaDatabasesApi",
    "SchemaDiscreteTypesDiscreteValuesApi",
    "SchemaDiscreteTypesApi",
    "SchemaDisplayNamesApi",
    "SchemaExportersApi",
    "SchemaExpressionsApi",
    "SchemaGlobalStandardNamesApi",
    "SchemaHelpFilesApi",
    "SchemaHomePagesApi",
    "SchemaLayoutSectionsApi",
    "SchemaLayoutsApi",
    "SchemaParametersApi",
    "SchemaProfileTablesApi",
    "SchemaProfilesApi",
    "SchemaRecordLinkGroupsApi",
    "SchemaReplacementStringsApi",
    "SchemaStandardNamesApi",
    "SchemaSubsetsApi",
    "SchemaTablesApi",
    "SchemaUnitsApi",
    "SearchApi",
    "ServerManagerApi",
    "StatusApi",
]
