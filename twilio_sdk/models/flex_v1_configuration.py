from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.configuration_enum_status import ConfigurationEnumStatusOrStr


class FlexV1Configuration(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Configuration
    resource."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the Configuration resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the Configuration resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    attributes: OptionalNullable[Any] = UNSET
    """An object that contains application-specific data."""

    status: Optional[ConfigurationEnumStatusOrStr] = UNSET
    """The status of the Flex onboarding. Can be: ``ok``, ``inprogress``,``notstarted``."""

    taskrouter_workspace_sid: OptionalNullable[str] = UNSET
    """The SID of the TaskRouter Workspace."""

    taskrouter_target_workflow_sid: OptionalNullable[str] = UNSET
    """The SID of the TaskRouter target Workflow."""

    taskrouter_target_taskqueue_sid: OptionalNullable[str] = UNSET
    """The SID of the TaskRouter Target TaskQueue."""

    taskrouter_taskqueues: Optional[list[Any | None]] = UNSET
    """The list of TaskRouter TaskQueues."""

    taskrouter_skills: Optional[list[Any | None]] = UNSET
    """The Skill description for TaskRouter workers."""

    taskrouter_worker_channels: OptionalNullable[Any] = UNSET
    """The TaskRouter default channel capacities and availability for workers."""

    taskrouter_worker_attributes: OptionalNullable[Any] = UNSET
    """The TaskRouter Worker attributes."""

    taskrouter_offline_activity_sid: OptionalNullable[str] = UNSET
    """The TaskRouter SID of the offline activity."""

    runtime_domain: OptionalNullable[str] = UNSET
    """The URL where the Flex instance is hosted."""

    messaging_service_instance_sid: OptionalNullable[str] = UNSET
    """The SID of the Messaging service instance."""

    chat_service_instance_sid: OptionalNullable[str] = UNSET
    """The SID of the chat service this user belongs to."""

    flex_service_instance_sid: OptionalNullable[str] = UNSET
    """The SID of the Flex service instance."""

    flex_instance_sid: OptionalNullable[str] = UNSET
    """The SID of the Flex instance."""

    ui_language: OptionalNullable[str] = UNSET
    """The primary language of the Flex UI."""

    ui_attributes: OptionalNullable[Any] = UNSET
    """The object that describes Flex UI characteristics and settings."""

    ui_dependencies: OptionalNullable[Any] = UNSET
    """The object that defines the NPM packages and versions to be used in Hosted Flex."""

    ui_version: OptionalNullable[str] = UNSET
    """The Pinned UI version."""

    service_version: OptionalNullable[str] = UNSET
    """The Flex Service version."""

    call_recording_enabled: OptionalNullable[bool] = UNSET
    """Whether call recording is enabled."""

    call_recording_webhook_url: OptionalNullable[str] = UNSET
    """The call recording webhook URL."""

    crm_enabled: OptionalNullable[bool] = UNSET
    """Whether CRM is present for Flex."""

    crm_type: OptionalNullable[str] = UNSET
    """The CRM type."""

    crm_callback_url: OptionalNullable[str] = UNSET
    """The CRM Callback URL."""

    crm_fallback_url: OptionalNullable[str] = UNSET
    """The CRM Fallback URL."""

    crm_attributes: OptionalNullable[Any] = UNSET
    """An object that contains the CRM attributes."""

    public_attributes: OptionalNullable[Any] = UNSET
    """The list of public attributes, which are visible to unauthenticated clients."""

    plugin_service_enabled: OptionalNullable[bool] = UNSET
    """Whether the plugin service enabled."""

    plugin_service_attributes: OptionalNullable[Any] = UNSET
    """The plugin service attributes."""

    integrations: Optional[list[Any | None]] = UNSET
    """A list of objects that contain the configurations for the Integrations supported in this configuration."""

    outbound_call_flows: OptionalNullable[Any] = UNSET
    """The list of outbound call flows."""

    serverless_service_sids: Optional[list[str | None]] = UNSET
    """The list of serverless service SIDs."""

    queue_stats_configuration: OptionalNullable[Any] = UNSET
    """Configurable parameters for Queues Statistics."""

    notifications: OptionalNullable[Any] = UNSET
    """Configurable parameters for Notifications."""

    markdown: OptionalNullable[Any] = UNSET
    """Configurable parameters for Markdown."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Configuration resource."""

    flex_insights_hr: OptionalNullable[Any] = UNSET
    """Object with enabled/disabled flag with list of workspaces."""

    flex_insights_drilldown: OptionalNullable[bool] = UNSET
    """Setting this to true will redirect Flex UI to the URL set in flex_url"""

    flex_url: OptionalNullable[str] = UNSET
    """URL to redirect to in case drilldown is enabled."""

    channel_configs: Optional[list[Any | None]] = UNSET
    """Settings for different limits for Flex Conversations channels attachments."""

    debugger_integration: OptionalNullable[Any] = UNSET
    """Configurable parameters for Debugger Integration."""

    flex_ui_status_report: OptionalNullable[Any] = UNSET
    """Configurable parameters for Flex UI Status report."""

    agent_conv_end_methods: OptionalNullable[Any] = UNSET
    """Agent conversation end methods."""

    citrix_voice_vdi: OptionalNullable[Any] = UNSET
    """Citrix voice vdi configuration and settings."""

    offline_config: OptionalNullable[Any] = UNSET
    """Presence and presence ttl configuration"""


class FlexV1ConfigurationDict(TypedDict):
    account_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    attributes: NotRequired[Any | None]
    status: NotRequired[ConfigurationEnumStatusOrStr]
    taskrouter_workspace_sid: NotRequired[str | None]
    taskrouter_target_workflow_sid: NotRequired[str | None]
    taskrouter_target_taskqueue_sid: NotRequired[str | None]
    taskrouter_taskqueues: NotRequired[list[Any | None]]
    taskrouter_skills: NotRequired[list[Any | None]]
    taskrouter_worker_channels: NotRequired[Any | None]
    taskrouter_worker_attributes: NotRequired[Any | None]
    taskrouter_offline_activity_sid: NotRequired[str | None]
    runtime_domain: NotRequired[str | None]
    messaging_service_instance_sid: NotRequired[str | None]
    chat_service_instance_sid: NotRequired[str | None]
    flex_service_instance_sid: NotRequired[str | None]
    flex_instance_sid: NotRequired[str | None]
    ui_language: NotRequired[str | None]
    ui_attributes: NotRequired[Any | None]
    ui_dependencies: NotRequired[Any | None]
    ui_version: NotRequired[str | None]
    service_version: NotRequired[str | None]
    call_recording_enabled: NotRequired[bool | None]
    call_recording_webhook_url: NotRequired[str | None]
    crm_enabled: NotRequired[bool | None]
    crm_type: NotRequired[str | None]
    crm_callback_url: NotRequired[str | None]
    crm_fallback_url: NotRequired[str | None]
    crm_attributes: NotRequired[Any | None]
    public_attributes: NotRequired[Any | None]
    plugin_service_enabled: NotRequired[bool | None]
    plugin_service_attributes: NotRequired[Any | None]
    integrations: NotRequired[list[Any | None]]
    outbound_call_flows: NotRequired[Any | None]
    serverless_service_sids: NotRequired[list[str | None]]
    queue_stats_configuration: NotRequired[Any | None]
    notifications: NotRequired[Any | None]
    markdown: NotRequired[Any | None]
    url: NotRequired[AnyUrl | None]
    flex_insights_hr: NotRequired[Any | None]
    flex_insights_drilldown: NotRequired[bool | None]
    flex_url: NotRequired[str | None]
    channel_configs: NotRequired[list[Any | None]]
    debugger_integration: NotRequired[Any | None]
    flex_ui_status_report: NotRequired[Any | None]
    agent_conv_end_methods: NotRequired[Any | None]
    citrix_voice_vdi: NotRequired[Any | None]
    offline_config: NotRequired[Any | None]
