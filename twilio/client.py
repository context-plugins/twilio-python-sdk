from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.api20100401_account import Api20100401Account
from .apis.api20100401_add_on_result import Api20100401AddOnResult
from .apis.api20100401_address import Api20100401Address
from .apis.api20100401_all_time import Api20100401AllTime
from .apis.api20100401_application import Api20100401Application
from .apis.api20100401_assigned_add_on import Api20100401AssignedAddOn
from .apis.api20100401_assigned_add_on_extension import Api20100401AssignedAddOnExtension
from .apis.api20100401_auth_calls_credential_list_mapping import Api20100401AuthCallsCredentialListMapping
from .apis.api20100401_auth_calls_ip_access_control_list_mapping import Api20100401AuthCallsIpAccessControlListMapping
from .apis.api20100401_auth_registrations_credential_list_mapping import (
    Api20100401AuthRegistrationsCredentialListMapping,
)
from .apis.api20100401_authorized_connect_app import Api20100401AuthorizedConnectApp
from .apis.api20100401_available_phone_number_country import Api20100401AvailablePhoneNumberCountry
from .apis.api20100401_balance import Api20100401Balance
from .apis.api20100401_call import Api20100401Call
from .apis.api20100401_call_notification import Api20100401CallNotification
from .apis.api20100401_call_recording import Api20100401CallRecording
from .apis.api20100401_call_transcription import Api20100401CallTranscription
from .apis.api20100401_conference import Api20100401Conference
from .apis.api20100401_conference_recording import Api20100401ConferenceRecording
from .apis.api20100401_connect_app import Api20100401ConnectApp
from .apis.api20100401_credential import Api20100401Credential
from .apis.api20100401_credential_list import Api20100401CredentialList
from .apis.api20100401_credential_list_mapping import Api20100401CredentialListMapping
from .apis.api20100401_daily import Api20100401Daily
from .apis.api20100401_data import Api20100401Data
from .apis.api20100401_dependent_phone_number import Api20100401DependentPhoneNumber
from .apis.api20100401_domain import Api20100401Domain
from .apis.api20100401_event import Api20100401Event
from .apis.api20100401_feedback import Api20100401Feedback
from .apis.api20100401_incoming_phone_number import Api20100401IncomingPhoneNumber
from .apis.api20100401_incoming_phone_number_local import Api20100401IncomingPhoneNumberLocal
from .apis.api20100401_incoming_phone_number_mobile import Api20100401IncomingPhoneNumberMobile
from .apis.api20100401_incoming_phone_number_toll_free import Api20100401IncomingPhoneNumberTollFree
from .apis.api20100401_ip_access_control_list import Api20100401IpAccessControlList
from .apis.api20100401_ip_access_control_list_mapping import Api20100401IpAccessControlListMapping
from .apis.api20100401_key import Api20100401Key
from .apis.api20100401_last_month import Api20100401LastMonth
from .apis.api20100401_local import Api20100401Local
from .apis.api20100401_machine_to_machine import Api20100401MachineToMachine
from .apis.api20100401_media import Api20100401Media
from .apis.api20100401_media_instance import Api20100401MediaInstance
from .apis.api20100401_member import Api20100401Member
from .apis.api20100401_message import Api20100401Message
from .apis.api20100401_mobile import Api20100401Mobile
from .apis.api20100401_monthly import Api20100401Monthly
from .apis.api20100401_national import Api20100401National
from .apis.api20100401_new_key import Api20100401NewKey
from .apis.api20100401_new_signing_key import Api20100401NewSigningKey
from .apis.api20100401_notification import Api20100401Notification
from .apis.api20100401_outgoing_caller_id import Api20100401OutgoingCallerId
from .apis.api20100401_participant import Api20100401Participant
from .apis.api20100401_payload import Api20100401Payload
from .apis.api20100401_payment import Api20100401Payment
from .apis.api20100401_queue import Api20100401Queue
from .apis.api20100401_record import Api20100401Record
from .apis.api20100401_recording import Api20100401Recording
from .apis.api20100401_recording_transcription import Api20100401RecordingTranscription
from .apis.api20100401_shared_cost import Api20100401SharedCost
from .apis.api20100401_short_code import Api20100401ShortCode
from .apis.api20100401_signing_key import Api20100401SigningKey
from .apis.api20100401_sip_ip_address import Api20100401SipIpAddress
from .apis.api20100401_siprec import Api20100401Siprec
from .apis.api20100401_stream import Api20100401Stream
from .apis.api20100401_this_month import Api20100401ThisMonth
from .apis.api20100401_today import Api20100401Today
from .apis.api20100401_token import Api20100401Token
from .apis.api20100401_toll_free import Api20100401TollFree
from .apis.api20100401_transcription import Api20100401Transcription
from .apis.api20100401_trigger import Api20100401Trigger
from .apis.api20100401_user_defined_message import Api20100401UserDefinedMessage
from .apis.api20100401_user_defined_message_subscription import Api20100401UserDefinedMessageSubscription
from .apis.api20100401_validation_request import Api20100401ValidationRequest
from .apis.api20100401_voip import Api20100401Voip
from .apis.api20100401_yearly import Api20100401Yearly
from .apis.api20100401_yesterday import Api20100401Yesterday
from .apis.content_v2_content import ContentV2Content
from .apis.content_v2_content_and_approvals import ContentV2ContentAndApprovals
from .apis.contentv1_approval_create import Contentv1ApprovalCreate
from .apis.contentv1_approval_fetch import Contentv1ApprovalFetch
from .apis.contentv1_content_and_approvals_api import Contentv1ContentAndApprovalsApi
from .apis.contentv1_content_api import Contentv1ContentApi
from .apis.contentv1_legacy_content_api import Contentv1LegacyContentApi
from .apis.conversations_v1_address_configuration import ConversationsV1AddressConfiguration
from .apis.conversations_v1_binding import ConversationsV1Binding
from .apis.conversations_v1_configuration_api import ConversationsV1ConfigurationApi
from .apis.conversations_v1_conversation_api import ConversationsV1ConversationApi
from .apis.conversations_v1_conversation_with_participants_api import ConversationsV1ConversationWithParticipantsApi
from .apis.conversations_v1_credential_api import ConversationsV1CredentialApi
from .apis.conversations_v1_delivery_receipt import ConversationsV1DeliveryReceipt
from .apis.conversations_v1_message import ConversationsV1Message
from .apis.conversations_v1_notification import ConversationsV1Notification
from .apis.conversations_v1_participant import ConversationsV1Participant
from .apis.conversations_v1_participant_conversation_api import ConversationsV1ParticipantConversationApi
from .apis.conversations_v1_role_api import ConversationsV1RoleApi
from .apis.conversations_v1_service_api import ConversationsV1ServiceApi
from .apis.conversations_v1_user_api import ConversationsV1UserApi
from .apis.conversations_v1_user_conversation import ConversationsV1UserConversation
from .apis.conversations_v1_webhook import ConversationsV1Webhook
from .apis.conversations_v2_action_api import ConversationsV2ActionApi
from .apis.conversations_v2_communication_api import ConversationsV2CommunicationApi
from .apis.conversations_v2_configuration_api import ConversationsV2ConfigurationApi
from .apis.conversations_v2_conversation_api import ConversationsV2ConversationApi
from .apis.conversations_v2_operation import ConversationsV2Operation
from .apis.conversations_v2_participant_api import ConversationsV2ParticipantApi
from .apis.flex_v1_assessments import FlexV1Assessments
from .apis.flex_v1_channel_api import FlexV1ChannelApi
from .apis.flex_v1_configuration_api import FlexV1ConfigurationApi
from .apis.flex_v1_configured_plugin import FlexV1ConfiguredPlugin
from .apis.flex_v1_flex_flow_api import FlexV1FlexFlowApi
from .apis.flex_v1_insights_assessments_comment_api import FlexV1InsightsAssessmentsCommentApi
from .apis.flex_v1_insights_conversations_api import FlexV1InsightsConversationsApi
from .apis.flex_v1_insights_questionnaires_api import FlexV1InsightsQuestionnairesApi
from .apis.flex_v1_insights_questionnaires_category_api import FlexV1InsightsQuestionnairesCategoryApi
from .apis.flex_v1_insights_questionnaires_question_api import FlexV1InsightsQuestionnairesQuestionApi
from .apis.flex_v1_insights_segments_api import FlexV1InsightsSegmentsApi
from .apis.flex_v1_insights_session_api import FlexV1InsightsSessionApi
from .apis.flex_v1_insights_settings_answer_sets_api import FlexV1InsightsSettingsAnswerSetsApi
from .apis.flex_v1_insights_settings_comment_api import FlexV1InsightsSettingsCommentApi
from .apis.flex_v1_insights_user_roles_api import FlexV1InsightsUserRolesApi
from .apis.flex_v1_interaction_api import FlexV1InteractionApi
from .apis.flex_v1_interaction_channel import FlexV1InteractionChannel
from .apis.flex_v1_interaction_channel_invite import FlexV1InteractionChannelInvite
from .apis.flex_v1_interaction_channel_participant import FlexV1InteractionChannelParticipant
from .apis.flex_v1_interaction_transfer import FlexV1InteractionTransfer
from .apis.flex_v1_plugin_api import FlexV1PluginApi
from .apis.flex_v1_plugin_archive_api import FlexV1PluginArchiveApi
from .apis.flex_v1_plugin_configuration_api import FlexV1PluginConfigurationApi
from .apis.flex_v1_plugin_configuration_archive_api import FlexV1PluginConfigurationArchiveApi
from .apis.flex_v1_plugin_release_api import FlexV1PluginReleaseApi
from .apis.flex_v1_plugin_version_archive_api import FlexV1PluginVersionArchiveApi
from .apis.flex_v1_plugin_versions import FlexV1PluginVersions
from .apis.flex_v1_provisioning_status_api import FlexV1ProvisioningStatusApi
from .apis.flex_v1_web_channel_api import FlexV1WebChannelApi
from .apis.flex_v2_flex_user_api import FlexV2FlexUserApi
from .apis.flex_v2_web_channels import FlexV2WebChannels
from .apis.insights_v1_annotation import InsightsV1Annotation
from .apis.insights_v1_call_api import InsightsV1CallApi
from .apis.insights_v1_call_summaries_api import InsightsV1CallSummariesApi
from .apis.insights_v1_call_summary_api import InsightsV1CallSummaryApi
from .apis.insights_v1_conference_api import InsightsV1ConferenceApi
from .apis.insights_v1_conference_participant import InsightsV1ConferenceParticipant
from .apis.insights_v1_create_account_report import InsightsV1CreateAccountReport
from .apis.insights_v1_create_inbound_phone_numbers_report import InsightsV1CreateInboundPhoneNumbersReport
from .apis.insights_v1_create_outbound_phone_numbers_report import InsightsV1CreateOutboundPhoneNumbersReport
from .apis.insights_v1_event import InsightsV1Event
from .apis.insights_v1_get_account_report import InsightsV1GetAccountReport
from .apis.insights_v1_get_inbound_phone_numbers_report import InsightsV1GetInboundPhoneNumbersReport
from .apis.insights_v1_get_outbound_phone_numbers_report import InsightsV1GetOutboundPhoneNumbersReport
from .apis.insights_v1_metric import InsightsV1Metric
from .apis.insights_v1_participant import InsightsV1Participant
from .apis.insights_v1_room import InsightsV1Room
from .apis.insights_v1_setting import InsightsV1Setting
from .apis.lookups_v1_phone_number_api import LookupsV1PhoneNumberApi
from .apis.lookups_v2_phone_number import LookupsV2PhoneNumber
from .apis.messaging_v1_alpha_sender import MessagingV1AlphaSender
from .apis.messaging_v1_brand_registration import MessagingV1BrandRegistration
from .apis.messaging_v1_brand_registration_otp import MessagingV1BrandRegistrationOtp
from .apis.messaging_v1_brand_vetting import MessagingV1BrandVetting
from .apis.messaging_v1_channel_sender import MessagingV1ChannelSender
from .apis.messaging_v1_deactivations import MessagingV1Deactivations
from .apis.messaging_v1_destination_alpha_sender import MessagingV1DestinationAlphaSender
from .apis.messaging_v1_domain_certs import MessagingV1DomainCerts
from .apis.messaging_v1_domain_config_api import MessagingV1DomainConfigApi
from .apis.messaging_v1_domain_config_messaging_service_api import MessagingV1DomainConfigMessagingServiceApi
from .apis.messaging_v1_domain_validate_dns import MessagingV1DomainValidateDns
from .apis.messaging_v1_external_campaign_api import MessagingV1ExternalCampaignApi
from .apis.messaging_v1_linkshortening_messaging_service_api import MessagingV1LinkshorteningMessagingServiceApi
from .apis.messaging_v1_linkshortening_messaging_service_domain_association_api import (
    MessagingV1LinkshorteningMessagingServiceDomainAssociationApi,
)
from .apis.messaging_v1_phone_number import MessagingV1PhoneNumber
from .apis.messaging_v1_request_managed_cert_api import MessagingV1RequestManagedCertApi
from .apis.messaging_v1_service_api import MessagingV1ServiceApi
from .apis.messaging_v1_short_code import MessagingV1ShortCode
from .apis.messaging_v1_tollfree_verification_api import MessagingV1TollfreeVerificationApi
from .apis.messaging_v1_us_app_to_person import MessagingV1UsAppToPerson
from .apis.messaging_v1_us_app_to_person_usecase import MessagingV1UsAppToPersonUsecase
from .apis.messaging_v1_usecase_api import MessagingV1UsecaseApi
from .apis.messaging_v2_channels_sender import MessagingV2ChannelsSender
from .apis.messaging_v2_domain_certs import MessagingV2DomainCerts
from .apis.messaging_v2_typing_indicator import MessagingV2TypingIndicator
from .apis.messaging_v3_typing_indicator import MessagingV3TypingIndicator
from .apis.numbers_v1_bulk_eligibility_api import NumbersV1BulkEligibilityApi
from .apis.numbers_v1_eligibility_api import NumbersV1EligibilityApi
from .apis.numbers_v1_porting_port_in_api import NumbersV1PortingPortInApi
from .apis.numbers_v1_porting_port_in_phone_number_api import NumbersV1PortingPortInPhoneNumberApi
from .apis.numbers_v1_porting_portability_api import NumbersV1PortingPortabilityApi
from .apis.numbers_v1_porting_webhook_configuration_api import NumbersV1PortingWebhookConfigurationApi
from .apis.numbers_v1_porting_webhook_configuration_delete_api import NumbersV1PortingWebhookConfigurationDeleteApi
from .apis.numbers_v1_porting_webhook_configuration_fetch_api import NumbersV1PortingWebhookConfigurationFetchApi
from .apis.numbers_v1_sender_id_registration import NumbersV1SenderIdRegistration
from .apis.numbers_v1_sender_id_registration_embedded_session import NumbersV1SenderIdRegistrationEmbeddedSession
from .apis.numbers_v1_signing_request_configuration_api import NumbersV1SigningRequestConfigurationApi
from .apis.numbers_v2_authorization_document_api import NumbersV2AuthorizationDocumentApi
from .apis.numbers_v2_bulk_hosted_number_order_api import NumbersV2BulkHostedNumberOrderApi
from .apis.numbers_v2_bundle import NumbersV2Bundle
from .apis.numbers_v2_bundle_clone_api import NumbersV2BundleCloneApi
from .apis.numbers_v2_bundle_copy import NumbersV2BundleCopy
from .apis.numbers_v2_dependent_hosted_number_order import NumbersV2DependentHostedNumberOrder
from .apis.numbers_v2_end_user import NumbersV2EndUser
from .apis.numbers_v2_end_user_type import NumbersV2EndUserType
from .apis.numbers_v2_evaluation import NumbersV2Evaluation
from .apis.numbers_v2_hosted_number_order_api import NumbersV2HostedNumberOrderApi
from .apis.numbers_v2_item_assignment import NumbersV2ItemAssignment
from .apis.numbers_v2_regulation import NumbersV2Regulation
from .apis.numbers_v2_replace_items import NumbersV2ReplaceItems
from .apis.numbers_v2_supporting_document import NumbersV2SupportingDocument
from .apis.numbers_v2_supporting_document_type import NumbersV2SupportingDocumentType
from .apis.numbers_v3_hosted_numbers_hosted_number_order_api import NumbersV3HostedNumbersHostedNumberOrderApi
from .apis.proxy_v1_interaction import ProxyV1Interaction
from .apis.proxy_v1_message_interaction import ProxyV1MessageInteraction
from .apis.proxy_v1_participant import ProxyV1Participant
from .apis.proxy_v1_phone_number import ProxyV1PhoneNumber
from .apis.proxy_v1_service_api import ProxyV1ServiceApi
from .apis.proxy_v1_session import ProxyV1Session
from .apis.studio_v1_engagement import StudioV1Engagement
from .apis.studio_v1_engagement_context import StudioV1EngagementContext
from .apis.studio_v1_execution import StudioV1Execution
from .apis.studio_v1_execution_context import StudioV1ExecutionContext
from .apis.studio_v1_execution_step import StudioV1ExecutionStep
from .apis.studio_v1_execution_step_context import StudioV1ExecutionStepContext
from .apis.studio_v1_flow_api import StudioV1FlowApi
from .apis.studio_v1_step import StudioV1Step
from .apis.studio_v1_step_context import StudioV1StepContext
from .apis.studio_v2_execution import StudioV2Execution
from .apis.studio_v2_execution_context import StudioV2ExecutionContext
from .apis.studio_v2_execution_step import StudioV2ExecutionStep
from .apis.studio_v2_execution_step_context import StudioV2ExecutionStepContext
from .apis.studio_v2_flow_api import StudioV2FlowApi
from .apis.studio_v2_flow_revision import StudioV2FlowRevision
from .apis.studio_v2_flow_test_user_api import StudioV2FlowTestUserApi
from .apis.studio_v2_flow_validate_api import StudioV2FlowValidateApi
from .apis.sync_v1_document import SyncV1Document
from .apis.sync_v1_document_permission import SyncV1DocumentPermission
from .apis.sync_v1_service_api import SyncV1ServiceApi
from .apis.sync_v1_stream_message import SyncV1StreamMessage
from .apis.sync_v1_sync_list import SyncV1SyncList
from .apis.sync_v1_sync_list_item import SyncV1SyncListItem
from .apis.sync_v1_sync_list_permission import SyncV1SyncListPermission
from .apis.sync_v1_sync_map import SyncV1SyncMap
from .apis.sync_v1_sync_map_item import SyncV1SyncMapItem
from .apis.sync_v1_sync_map_permission import SyncV1SyncMapPermission
from .apis.sync_v1_sync_stream import SyncV1SyncStream
from .apis.taskrouter_v1_activity import TaskrouterV1Activity
from .apis.taskrouter_v1_event import TaskrouterV1Event
from .apis.taskrouter_v1_task import TaskrouterV1Task
from .apis.taskrouter_v1_task_channel import TaskrouterV1TaskChannel
from .apis.taskrouter_v1_task_queue import TaskrouterV1TaskQueue
from .apis.taskrouter_v1_task_queue_bulk_real_time_statistics import TaskrouterV1TaskQueueBulkRealTimeStatistics
from .apis.taskrouter_v1_task_queue_cumulative_statistics import TaskrouterV1TaskQueueCumulativeStatistics
from .apis.taskrouter_v1_task_queue_real_time_statistics import TaskrouterV1TaskQueueRealTimeStatistics
from .apis.taskrouter_v1_task_queue_statistics import TaskrouterV1TaskQueueStatistics
from .apis.taskrouter_v1_task_queues_statistics import TaskrouterV1TaskQueuesStatistics
from .apis.taskrouter_v1_task_reservation import TaskrouterV1TaskReservation
from .apis.taskrouter_v1_worker import TaskrouterV1Worker
from .apis.taskrouter_v1_worker_channel import TaskrouterV1WorkerChannel
from .apis.taskrouter_v1_worker_reservation import TaskrouterV1WorkerReservation
from .apis.taskrouter_v1_worker_statistics import TaskrouterV1WorkerStatistics
from .apis.taskrouter_v1_workers_cumulative_statistics import TaskrouterV1WorkersCumulativeStatistics
from .apis.taskrouter_v1_workers_real_time_statistics import TaskrouterV1WorkersRealTimeStatistics
from .apis.taskrouter_v1_workers_statistics import TaskrouterV1WorkersStatistics
from .apis.taskrouter_v1_workflow import TaskrouterV1Workflow
from .apis.taskrouter_v1_workflow_cumulative_statistics import TaskrouterV1WorkflowCumulativeStatistics
from .apis.taskrouter_v1_workflow_real_time_statistics import TaskrouterV1WorkflowRealTimeStatistics
from .apis.taskrouter_v1_workflow_statistics import TaskrouterV1WorkflowStatistics
from .apis.taskrouter_v1_workspace_api import TaskrouterV1WorkspaceApi
from .apis.taskrouter_v1_workspace_cumulative_statistics import TaskrouterV1WorkspaceCumulativeStatistics
from .apis.taskrouter_v1_workspace_real_time_statistics import TaskrouterV1WorkspaceRealTimeStatistics
from .apis.taskrouter_v1_workspace_statistics import TaskrouterV1WorkspaceStatistics
from .apis.trusthub_v1_compliance_inquiries import TrusthubV1ComplianceInquiries
from .apis.trusthub_v1_compliance_registration_inquiries import TrusthubV1ComplianceRegistrationInquiries
from .apis.trusthub_v1_compliance_tollfree_inquiries import TrusthubV1ComplianceTollfreeInquiries
from .apis.trusthub_v1_customer_profiles import TrusthubV1CustomerProfiles
from .apis.trusthub_v1_customer_profiles_channel_endpoint_assignment import (
    TrusthubV1CustomerProfilesChannelEndpointAssignment,
)
from .apis.trusthub_v1_customer_profiles_entity_assignments import TrusthubV1CustomerProfilesEntityAssignments
from .apis.trusthub_v1_customer_profiles_evaluations import TrusthubV1CustomerProfilesEvaluations
from .apis.trusthub_v1_end_user_api import TrusthubV1EndUserApi
from .apis.trusthub_v1_end_user_type import TrusthubV1EndUserType
from .apis.trusthub_v1_policies_api import TrusthubV1PoliciesApi
from .apis.trusthub_v1_supporting_document_api import TrusthubV1SupportingDocumentApi
from .apis.trusthub_v1_supporting_document_type import TrusthubV1SupportingDocumentType
from .apis.trusthub_v1_trust_products import TrusthubV1TrustProducts
from .apis.trusthub_v1_trust_products_channel_endpoint_assignment import (
    TrusthubV1TrustProductsChannelEndpointAssignment,
)
from .apis.trusthub_v1_trust_products_entity_assignments import TrusthubV1TrustProductsEntityAssignments
from .apis.trusthub_v1_trust_products_evaluations import TrusthubV1TrustProductsEvaluations
from .apis.twilio_insights import TwilioInsights
from .apis.v2_short_code_applications import V2ShortCodeApplications
from .apis.verify_v2_access_token import VerifyV2AccessToken
from .apis.verify_v2_bucket import VerifyV2Bucket
from .apis.verify_v2_challenge import VerifyV2Challenge
from .apis.verify_v2_entity import VerifyV2Entity
from .apis.verify_v2_factor import VerifyV2Factor
from .apis.verify_v2_form_api import VerifyV2FormApi
from .apis.verify_v2_messaging_configuration import VerifyV2MessagingConfiguration
from .apis.verify_v2_new_challenge import VerifyV2NewChallenge
from .apis.verify_v2_new_factor import VerifyV2NewFactor
from .apis.verify_v2_notification import VerifyV2Notification
from .apis.verify_v2_rate_limit import VerifyV2RateLimit
from .apis.verify_v2_safelist_api import VerifyV2SafelistApi
from .apis.verify_v2_service_api import VerifyV2ServiceApi
from .apis.verify_v2_template import VerifyV2Template
from .apis.verify_v2_verification import VerifyV2Verification
from .apis.verify_v2_verification_attempt_api import VerifyV2VerificationAttemptApi
from .apis.verify_v2_verification_attempts_summary_api import VerifyV2VerificationAttemptsSummaryApi
from .apis.verify_v2_verification_check import VerifyV2VerificationCheck
from .apis.verify_v2_webhook import VerifyV2Webhook
from .apis.video_v1_anonymize import VideoV1Anonymize
from .apis.video_v1_composition_api import VideoV1CompositionApi
from .apis.video_v1_composition_hook_api import VideoV1CompositionHookApi
from .apis.video_v1_composition_settings_api import VideoV1CompositionSettingsApi
from .apis.video_v1_participant import VideoV1Participant
from .apis.video_v1_published_track import VideoV1PublishedTrack
from .apis.video_v1_recording_api import VideoV1RecordingApi
from .apis.video_v1_recording_rules import VideoV1RecordingRules
from .apis.video_v1_recording_settings_api import VideoV1RecordingSettingsApi
from .apis.video_v1_room_api import VideoV1RoomApi
from .apis.video_v1_room_recording import VideoV1RoomRecording
from .apis.video_v1_subscribe_rules import VideoV1SubscribeRules
from .apis.video_v1_subscribed_track import VideoV1SubscribedTrack
from .apis.video_v1_transcriptions import VideoV1Transcriptions
from .auth import AuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseTwilioClient
from .core import (
    ApiResult,
    BasicAuthCredentials,
    BasicAuthCredentialsOrDict,
    BasicAuthScheme,
    HttpClient,
    HttpxClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    json_body,
    json_decoder,
    no_auth,
    param,
    raw_error_response,
)
from .errors.create_lookup_phone_number_overrides_error import (
    CreateLookupPhoneNumberOverridesErrorBody,
    create_lookup_phone_number_overrides_error_mapper,
)
from .errors.delete_lookup_phone_number_overrides_error import (
    DeleteLookupPhoneNumberOverridesErrorBody,
    delete_lookup_phone_number_overrides_error_mapper,
)
from .errors.delete_lookup_rate_limit_error import DeleteLookupRateLimitErrorBody, delete_lookup_rate_limit_error_mapper
from .errors.fetch_lookup_account_rate_limits_error import (
    FetchLookupAccountRateLimitsErrorBody,
    fetch_lookup_account_rate_limits_error_mapper,
)
from .errors.fetch_lookup_phone_number_overrides_error import (
    FetchLookupPhoneNumberOverridesErrorBody,
    fetch_lookup_phone_number_overrides_error_mapper,
)
from .errors.fetch_lookup_rate_limit_error import FetchLookupRateLimitErrorBody, fetch_lookup_rate_limit_error_mapper
from .errors.update_lookup_phone_number_overrides_error import (
    UpdateLookupPhoneNumberOverridesErrorBody,
    update_lookup_phone_number_overrides_error_mapper,
)
from .errors.update_lookup_rate_limit_error import UpdateLookupRateLimitErrorBody, update_lookup_rate_limit_error_mapper
from .models.approve_passkeys_challenge_request import (
    ApprovePasskeysChallengeRequest,
    ApprovePasskeysChallengeRequestDict,
)
from .models.lookup_request import LookupRequest, LookupRequestDict
from .models.lookup_response1 import LookupResponse1
from .models.overrides_request import OverridesRequest, OverridesRequestDict
from .models.overrides_response import OverridesResponse
from .models.rate_limit_list_response import RateLimitListResponse
from .models.rate_limit_request import RateLimitRequest, RateLimitRequestDict
from .models.rate_limit_response import RateLimitResponse
from .models.v2_services_passkeys_approve_challenge_response import V2ServicesPasskeysApproveChallengeResponse
from .models.v2_services_passkeys_verify_factor_response import V2ServicesPasskeysVerifyFactorResponse
from .models.verify_passkeys_factor_request import VerifyPasskeysFactorRequest, VerifyPasskeysFactorRequestDict
from .server.server import Server
from .server.server_config import ServerConfigOrDict


class TwilioClient(BaseTwilioClient[RawClient]):
    def __init__(
        self,
        *,
        server_config: ServerConfigOrDict | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_http_client: HttpClient | None = None,
        account_sid_auth_token: BasicAuthCredentialsOrDict | None = None,
    ) -> None:
        super().__init__(server_config=server_config, timeout=timeout)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else HttpxClient(timeout=timeout)
        )
        self._auth = AuthSchemes(
            account_sid_auth_token=(
                BasicAuthScheme(BasicAuthCredentials.coerce(account_sid_auth_token))
                if account_sid_auth_token is not None
                else no_auth
            ),
        )

    @cached_property
    def api20100401_account(self) -> Api20100401Account:
        return Api20100401Account(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_add_on_result(self) -> Api20100401AddOnResult:
        return Api20100401AddOnResult(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_address(self) -> Api20100401Address:
        return Api20100401Address(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_all_time(self) -> Api20100401AllTime:
        return Api20100401AllTime(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_application(self) -> Api20100401Application:
        return Api20100401Application(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_assigned_add_on(self) -> Api20100401AssignedAddOn:
        return Api20100401AssignedAddOn(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_assigned_add_on_extension(self) -> Api20100401AssignedAddOnExtension:
        return Api20100401AssignedAddOnExtension(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_auth_calls_credential_list_mapping(self) -> Api20100401AuthCallsCredentialListMapping:
        return Api20100401AuthCallsCredentialListMapping(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_auth_calls_ip_access_control_list_mapping(self) -> Api20100401AuthCallsIpAccessControlListMapping:
        return Api20100401AuthCallsIpAccessControlListMapping(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_auth_registrations_credential_list_mapping(
        self
    ) -> Api20100401AuthRegistrationsCredentialListMapping:
        return Api20100401AuthRegistrationsCredentialListMapping(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_authorized_connect_app(self) -> Api20100401AuthorizedConnectApp:
        return Api20100401AuthorizedConnectApp(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_available_phone_number_country(self) -> Api20100401AvailablePhoneNumberCountry:
        return Api20100401AvailablePhoneNumberCountry(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_balance(self) -> Api20100401Balance:
        return Api20100401Balance(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_call(self) -> Api20100401Call:
        return Api20100401Call(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_call_notification(self) -> Api20100401CallNotification:
        return Api20100401CallNotification(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_call_recording(self) -> Api20100401CallRecording:
        return Api20100401CallRecording(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_call_transcription(self) -> Api20100401CallTranscription:
        return Api20100401CallTranscription(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_conference(self) -> Api20100401Conference:
        return Api20100401Conference(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_conference_recording(self) -> Api20100401ConferenceRecording:
        return Api20100401ConferenceRecording(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_connect_app(self) -> Api20100401ConnectApp:
        return Api20100401ConnectApp(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_credential(self) -> Api20100401Credential:
        return Api20100401Credential(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_credential_list(self) -> Api20100401CredentialList:
        return Api20100401CredentialList(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_credential_list_mapping(self) -> Api20100401CredentialListMapping:
        return Api20100401CredentialListMapping(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_daily(self) -> Api20100401Daily:
        return Api20100401Daily(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_data(self) -> Api20100401Data:
        return Api20100401Data(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_dependent_phone_number(self) -> Api20100401DependentPhoneNumber:
        return Api20100401DependentPhoneNumber(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_domain(self) -> Api20100401Domain:
        return Api20100401Domain(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_event(self) -> Api20100401Event:
        return Api20100401Event(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_feedback(self) -> Api20100401Feedback:
        return Api20100401Feedback(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_incoming_phone_number(self) -> Api20100401IncomingPhoneNumber:
        return Api20100401IncomingPhoneNumber(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_incoming_phone_number_local(self) -> Api20100401IncomingPhoneNumberLocal:
        return Api20100401IncomingPhoneNumberLocal(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_incoming_phone_number_mobile(self) -> Api20100401IncomingPhoneNumberMobile:
        return Api20100401IncomingPhoneNumberMobile(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_incoming_phone_number_toll_free(self) -> Api20100401IncomingPhoneNumberTollFree:
        return Api20100401IncomingPhoneNumberTollFree(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_ip_access_control_list(self) -> Api20100401IpAccessControlList:
        return Api20100401IpAccessControlList(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_ip_access_control_list_mapping(self) -> Api20100401IpAccessControlListMapping:
        return Api20100401IpAccessControlListMapping(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_key(self) -> Api20100401Key:
        return Api20100401Key(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_last_month(self) -> Api20100401LastMonth:
        return Api20100401LastMonth(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_local(self) -> Api20100401Local:
        return Api20100401Local(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_machine_to_machine(self) -> Api20100401MachineToMachine:
        return Api20100401MachineToMachine(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_media(self) -> Api20100401Media:
        return Api20100401Media(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_media_instance(self) -> Api20100401MediaInstance:
        return Api20100401MediaInstance(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_member(self) -> Api20100401Member:
        return Api20100401Member(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_message(self) -> Api20100401Message:
        return Api20100401Message(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_mobile(self) -> Api20100401Mobile:
        return Api20100401Mobile(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_monthly(self) -> Api20100401Monthly:
        return Api20100401Monthly(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_national(self) -> Api20100401National:
        return Api20100401National(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_new_key(self) -> Api20100401NewKey:
        return Api20100401NewKey(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_new_signing_key(self) -> Api20100401NewSigningKey:
        return Api20100401NewSigningKey(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_notification(self) -> Api20100401Notification:
        return Api20100401Notification(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_outgoing_caller_id(self) -> Api20100401OutgoingCallerId:
        return Api20100401OutgoingCallerId(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_participant(self) -> Api20100401Participant:
        return Api20100401Participant(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_payload(self) -> Api20100401Payload:
        return Api20100401Payload(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_payment(self) -> Api20100401Payment:
        return Api20100401Payment(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_queue(self) -> Api20100401Queue:
        return Api20100401Queue(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_record(self) -> Api20100401Record:
        return Api20100401Record(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_recording(self) -> Api20100401Recording:
        return Api20100401Recording(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_recording_transcription(self) -> Api20100401RecordingTranscription:
        return Api20100401RecordingTranscription(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_shared_cost(self) -> Api20100401SharedCost:
        return Api20100401SharedCost(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_short_code(self) -> Api20100401ShortCode:
        return Api20100401ShortCode(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_signing_key(self) -> Api20100401SigningKey:
        return Api20100401SigningKey(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_sip_ip_address(self) -> Api20100401SipIpAddress:
        return Api20100401SipIpAddress(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_siprec(self) -> Api20100401Siprec:
        return Api20100401Siprec(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_stream(self) -> Api20100401Stream:
        return Api20100401Stream(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_this_month(self) -> Api20100401ThisMonth:
        return Api20100401ThisMonth(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_today(self) -> Api20100401Today:
        return Api20100401Today(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_token(self) -> Api20100401Token:
        return Api20100401Token(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_toll_free(self) -> Api20100401TollFree:
        return Api20100401TollFree(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_transcription(self) -> Api20100401Transcription:
        return Api20100401Transcription(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_trigger(self) -> Api20100401Trigger:
        return Api20100401Trigger(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_user_defined_message(self) -> Api20100401UserDefinedMessage:
        return Api20100401UserDefinedMessage(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_user_defined_message_subscription(self) -> Api20100401UserDefinedMessageSubscription:
        return Api20100401UserDefinedMessageSubscription(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_validation_request(self) -> Api20100401ValidationRequest:
        return Api20100401ValidationRequest(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_voip(self) -> Api20100401Voip:
        return Api20100401Voip(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_yearly(self) -> Api20100401Yearly:
        return Api20100401Yearly(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_yesterday(self) -> Api20100401Yesterday:
        return Api20100401Yesterday(self._raw_client, self._server, self._auth)

    @cached_property
    def content_v2_content(self) -> ContentV2Content:
        return ContentV2Content(self._raw_client, self._server, self._auth)

    @cached_property
    def content_v2_content_and_approvals(self) -> ContentV2ContentAndApprovals:
        return ContentV2ContentAndApprovals(self._raw_client, self._server, self._auth)

    @cached_property
    def contentv1_approval_create(self) -> Contentv1ApprovalCreate:
        return Contentv1ApprovalCreate(self._raw_client, self._server, self._auth)

    @cached_property
    def contentv1_approval_fetch(self) -> Contentv1ApprovalFetch:
        return Contentv1ApprovalFetch(self._raw_client, self._server, self._auth)

    @cached_property
    def contentv1_content_api(self) -> Contentv1ContentApi:
        return Contentv1ContentApi(self._raw_client, self._server, self._auth)

    @cached_property
    def contentv1_content_and_approvals_api(self) -> Contentv1ContentAndApprovalsApi:
        return Contentv1ContentAndApprovalsApi(self._raw_client, self._server, self._auth)

    @cached_property
    def contentv1_legacy_content_api(self) -> Contentv1LegacyContentApi:
        return Contentv1LegacyContentApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_address_configuration(self) -> ConversationsV1AddressConfiguration:
        return ConversationsV1AddressConfiguration(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_binding(self) -> ConversationsV1Binding:
        return ConversationsV1Binding(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_configuration_api(self) -> ConversationsV1ConfigurationApi:
        return ConversationsV1ConfigurationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_conversation_api(self) -> ConversationsV1ConversationApi:
        return ConversationsV1ConversationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_conversation_with_participants_api(self) -> ConversationsV1ConversationWithParticipantsApi:
        return ConversationsV1ConversationWithParticipantsApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_credential_api(self) -> ConversationsV1CredentialApi:
        return ConversationsV1CredentialApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_delivery_receipt(self) -> ConversationsV1DeliveryReceipt:
        return ConversationsV1DeliveryReceipt(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_message(self) -> ConversationsV1Message:
        return ConversationsV1Message(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_notification(self) -> ConversationsV1Notification:
        return ConversationsV1Notification(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_participant(self) -> ConversationsV1Participant:
        return ConversationsV1Participant(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_participant_conversation_api(self) -> ConversationsV1ParticipantConversationApi:
        return ConversationsV1ParticipantConversationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_role_api(self) -> ConversationsV1RoleApi:
        return ConversationsV1RoleApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_service_api(self) -> ConversationsV1ServiceApi:
        return ConversationsV1ServiceApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_user_api(self) -> ConversationsV1UserApi:
        return ConversationsV1UserApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_user_conversation(self) -> ConversationsV1UserConversation:
        return ConversationsV1UserConversation(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_webhook(self) -> ConversationsV1Webhook:
        return ConversationsV1Webhook(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v2_action_api(self) -> ConversationsV2ActionApi:
        return ConversationsV2ActionApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v2_communication_api(self) -> ConversationsV2CommunicationApi:
        return ConversationsV2CommunicationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v2_configuration_api(self) -> ConversationsV2ConfigurationApi:
        return ConversationsV2ConfigurationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v2_conversation_api(self) -> ConversationsV2ConversationApi:
        return ConversationsV2ConversationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v2_operation(self) -> ConversationsV2Operation:
        return ConversationsV2Operation(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v2_participant_api(self) -> ConversationsV2ParticipantApi:
        return ConversationsV2ParticipantApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_assessments(self) -> FlexV1Assessments:
        return FlexV1Assessments(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_channel_api(self) -> FlexV1ChannelApi:
        return FlexV1ChannelApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_configuration_api(self) -> FlexV1ConfigurationApi:
        return FlexV1ConfigurationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_configured_plugin(self) -> FlexV1ConfiguredPlugin:
        return FlexV1ConfiguredPlugin(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_flex_flow_api(self) -> FlexV1FlexFlowApi:
        return FlexV1FlexFlowApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_insights_assessments_comment_api(self) -> FlexV1InsightsAssessmentsCommentApi:
        return FlexV1InsightsAssessmentsCommentApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_insights_conversations_api(self) -> FlexV1InsightsConversationsApi:
        return FlexV1InsightsConversationsApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_insights_questionnaires_api(self) -> FlexV1InsightsQuestionnairesApi:
        return FlexV1InsightsQuestionnairesApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_insights_questionnaires_category_api(self) -> FlexV1InsightsQuestionnairesCategoryApi:
        return FlexV1InsightsQuestionnairesCategoryApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_insights_questionnaires_question_api(self) -> FlexV1InsightsQuestionnairesQuestionApi:
        return FlexV1InsightsQuestionnairesQuestionApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_insights_segments_api(self) -> FlexV1InsightsSegmentsApi:
        return FlexV1InsightsSegmentsApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_insights_session_api(self) -> FlexV1InsightsSessionApi:
        return FlexV1InsightsSessionApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_insights_settings_answer_sets_api(self) -> FlexV1InsightsSettingsAnswerSetsApi:
        return FlexV1InsightsSettingsAnswerSetsApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_insights_settings_comment_api(self) -> FlexV1InsightsSettingsCommentApi:
        return FlexV1InsightsSettingsCommentApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_insights_user_roles_api(self) -> FlexV1InsightsUserRolesApi:
        return FlexV1InsightsUserRolesApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_interaction_api(self) -> FlexV1InteractionApi:
        return FlexV1InteractionApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_interaction_channel(self) -> FlexV1InteractionChannel:
        return FlexV1InteractionChannel(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_interaction_channel_invite(self) -> FlexV1InteractionChannelInvite:
        return FlexV1InteractionChannelInvite(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_interaction_channel_participant(self) -> FlexV1InteractionChannelParticipant:
        return FlexV1InteractionChannelParticipant(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_interaction_transfer(self) -> FlexV1InteractionTransfer:
        return FlexV1InteractionTransfer(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_plugin_api(self) -> FlexV1PluginApi:
        return FlexV1PluginApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_plugin_archive_api(self) -> FlexV1PluginArchiveApi:
        return FlexV1PluginArchiveApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_plugin_configuration_api(self) -> FlexV1PluginConfigurationApi:
        return FlexV1PluginConfigurationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_plugin_configuration_archive_api(self) -> FlexV1PluginConfigurationArchiveApi:
        return FlexV1PluginConfigurationArchiveApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_plugin_release_api(self) -> FlexV1PluginReleaseApi:
        return FlexV1PluginReleaseApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_plugin_version_archive_api(self) -> FlexV1PluginVersionArchiveApi:
        return FlexV1PluginVersionArchiveApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_plugin_versions(self) -> FlexV1PluginVersions:
        return FlexV1PluginVersions(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_provisioning_status_api(self) -> FlexV1ProvisioningStatusApi:
        return FlexV1ProvisioningStatusApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_web_channel_api(self) -> FlexV1WebChannelApi:
        return FlexV1WebChannelApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v2_flex_user_api(self) -> FlexV2FlexUserApi:
        return FlexV2FlexUserApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v2_web_channels(self) -> FlexV2WebChannels:
        return FlexV2WebChannels(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_annotation(self) -> InsightsV1Annotation:
        return InsightsV1Annotation(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_call_api(self) -> InsightsV1CallApi:
        return InsightsV1CallApi(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_call_summaries_api(self) -> InsightsV1CallSummariesApi:
        return InsightsV1CallSummariesApi(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_call_summary_api(self) -> InsightsV1CallSummaryApi:
        return InsightsV1CallSummaryApi(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_conference_api(self) -> InsightsV1ConferenceApi:
        return InsightsV1ConferenceApi(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_conference_participant(self) -> InsightsV1ConferenceParticipant:
        return InsightsV1ConferenceParticipant(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_create_account_report(self) -> InsightsV1CreateAccountReport:
        return InsightsV1CreateAccountReport(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_create_inbound_phone_numbers_report(self) -> InsightsV1CreateInboundPhoneNumbersReport:
        return InsightsV1CreateInboundPhoneNumbersReport(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_create_outbound_phone_numbers_report(self) -> InsightsV1CreateOutboundPhoneNumbersReport:
        return InsightsV1CreateOutboundPhoneNumbersReport(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_event(self) -> InsightsV1Event:
        return InsightsV1Event(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_get_account_report(self) -> InsightsV1GetAccountReport:
        return InsightsV1GetAccountReport(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_get_inbound_phone_numbers_report(self) -> InsightsV1GetInboundPhoneNumbersReport:
        return InsightsV1GetInboundPhoneNumbersReport(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_get_outbound_phone_numbers_report(self) -> InsightsV1GetOutboundPhoneNumbersReport:
        return InsightsV1GetOutboundPhoneNumbersReport(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_metric(self) -> InsightsV1Metric:
        return InsightsV1Metric(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_participant(self) -> InsightsV1Participant:
        return InsightsV1Participant(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_room(self) -> InsightsV1Room:
        return InsightsV1Room(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_setting(self) -> InsightsV1Setting:
        return InsightsV1Setting(self._raw_client, self._server, self._auth)

    @cached_property
    def lookups_v1_phone_number_api(self) -> LookupsV1PhoneNumberApi:
        return LookupsV1PhoneNumberApi(self._raw_client, self._server, self._auth)

    @cached_property
    def lookups_v2_phone_number(self) -> LookupsV2PhoneNumber:
        return LookupsV2PhoneNumber(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_alpha_sender(self) -> MessagingV1AlphaSender:
        return MessagingV1AlphaSender(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_brand_registration(self) -> MessagingV1BrandRegistration:
        return MessagingV1BrandRegistration(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_brand_registration_otp(self) -> MessagingV1BrandRegistrationOtp:
        return MessagingV1BrandRegistrationOtp(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_brand_vetting(self) -> MessagingV1BrandVetting:
        return MessagingV1BrandVetting(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_channel_sender(self) -> MessagingV1ChannelSender:
        return MessagingV1ChannelSender(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_deactivations(self) -> MessagingV1Deactivations:
        return MessagingV1Deactivations(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_destination_alpha_sender(self) -> MessagingV1DestinationAlphaSender:
        return MessagingV1DestinationAlphaSender(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_domain_certs(self) -> MessagingV1DomainCerts:
        return MessagingV1DomainCerts(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_domain_config_api(self) -> MessagingV1DomainConfigApi:
        return MessagingV1DomainConfigApi(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_domain_config_messaging_service_api(self) -> MessagingV1DomainConfigMessagingServiceApi:
        return MessagingV1DomainConfigMessagingServiceApi(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_domain_validate_dns(self) -> MessagingV1DomainValidateDns:
        return MessagingV1DomainValidateDns(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_external_campaign_api(self) -> MessagingV1ExternalCampaignApi:
        return MessagingV1ExternalCampaignApi(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_linkshortening_messaging_service_api(self) -> MessagingV1LinkshorteningMessagingServiceApi:
        return MessagingV1LinkshorteningMessagingServiceApi(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_linkshortening_messaging_service_domain_association_api(
        self
    ) -> MessagingV1LinkshorteningMessagingServiceDomainAssociationApi:
        return MessagingV1LinkshorteningMessagingServiceDomainAssociationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_phone_number(self) -> MessagingV1PhoneNumber:
        return MessagingV1PhoneNumber(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_request_managed_cert_api(self) -> MessagingV1RequestManagedCertApi:
        return MessagingV1RequestManagedCertApi(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_service_api(self) -> MessagingV1ServiceApi:
        return MessagingV1ServiceApi(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_short_code(self) -> MessagingV1ShortCode:
        return MessagingV1ShortCode(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_tollfree_verification_api(self) -> MessagingV1TollfreeVerificationApi:
        return MessagingV1TollfreeVerificationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_us_app_to_person(self) -> MessagingV1UsAppToPerson:
        return MessagingV1UsAppToPerson(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_us_app_to_person_usecase(self) -> MessagingV1UsAppToPersonUsecase:
        return MessagingV1UsAppToPersonUsecase(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_usecase_api(self) -> MessagingV1UsecaseApi:
        return MessagingV1UsecaseApi(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v2_channels_sender(self) -> MessagingV2ChannelsSender:
        return MessagingV2ChannelsSender(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v2_domain_certs(self) -> MessagingV2DomainCerts:
        return MessagingV2DomainCerts(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v2_typing_indicator(self) -> MessagingV2TypingIndicator:
        return MessagingV2TypingIndicator(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v3_typing_indicator(self) -> MessagingV3TypingIndicator:
        return MessagingV3TypingIndicator(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v1_bulk_eligibility_api(self) -> NumbersV1BulkEligibilityApi:
        return NumbersV1BulkEligibilityApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v1_eligibility_api(self) -> NumbersV1EligibilityApi:
        return NumbersV1EligibilityApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v1_porting_port_in_api(self) -> NumbersV1PortingPortInApi:
        return NumbersV1PortingPortInApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v1_porting_port_in_phone_number_api(self) -> NumbersV1PortingPortInPhoneNumberApi:
        return NumbersV1PortingPortInPhoneNumberApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v1_porting_portability_api(self) -> NumbersV1PortingPortabilityApi:
        return NumbersV1PortingPortabilityApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v1_porting_webhook_configuration_api(self) -> NumbersV1PortingWebhookConfigurationApi:
        return NumbersV1PortingWebhookConfigurationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v1_porting_webhook_configuration_delete_api(self) -> NumbersV1PortingWebhookConfigurationDeleteApi:
        return NumbersV1PortingWebhookConfigurationDeleteApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v1_porting_webhook_configuration_fetch_api(self) -> NumbersV1PortingWebhookConfigurationFetchApi:
        return NumbersV1PortingWebhookConfigurationFetchApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v1_sender_id_registration(self) -> NumbersV1SenderIdRegistration:
        return NumbersV1SenderIdRegistration(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v1_sender_id_registration_embedded_session(self) -> NumbersV1SenderIdRegistrationEmbeddedSession:
        return NumbersV1SenderIdRegistrationEmbeddedSession(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v1_signing_request_configuration_api(self) -> NumbersV1SigningRequestConfigurationApi:
        return NumbersV1SigningRequestConfigurationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_authorization_document_api(self) -> NumbersV2AuthorizationDocumentApi:
        return NumbersV2AuthorizationDocumentApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_bulk_hosted_number_order_api(self) -> NumbersV2BulkHostedNumberOrderApi:
        return NumbersV2BulkHostedNumberOrderApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_bundle(self) -> NumbersV2Bundle:
        return NumbersV2Bundle(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_bundle_clone_api(self) -> NumbersV2BundleCloneApi:
        return NumbersV2BundleCloneApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_bundle_copy(self) -> NumbersV2BundleCopy:
        return NumbersV2BundleCopy(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_dependent_hosted_number_order(self) -> NumbersV2DependentHostedNumberOrder:
        return NumbersV2DependentHostedNumberOrder(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_end_user(self) -> NumbersV2EndUser:
        return NumbersV2EndUser(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_end_user_type(self) -> NumbersV2EndUserType:
        return NumbersV2EndUserType(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_evaluation(self) -> NumbersV2Evaluation:
        return NumbersV2Evaluation(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_hosted_number_order_api(self) -> NumbersV2HostedNumberOrderApi:
        return NumbersV2HostedNumberOrderApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_item_assignment(self) -> NumbersV2ItemAssignment:
        return NumbersV2ItemAssignment(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_regulation(self) -> NumbersV2Regulation:
        return NumbersV2Regulation(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_replace_items(self) -> NumbersV2ReplaceItems:
        return NumbersV2ReplaceItems(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_supporting_document(self) -> NumbersV2SupportingDocument:
        return NumbersV2SupportingDocument(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_supporting_document_type(self) -> NumbersV2SupportingDocumentType:
        return NumbersV2SupportingDocumentType(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v3_hosted_numbers_hosted_number_order_api(self) -> NumbersV3HostedNumbersHostedNumberOrderApi:
        return NumbersV3HostedNumbersHostedNumberOrderApi(self._raw_client, self._server, self._auth)

    @cached_property
    def proxy_v1_interaction(self) -> ProxyV1Interaction:
        return ProxyV1Interaction(self._raw_client, self._server, self._auth)

    @cached_property
    def proxy_v1_message_interaction(self) -> ProxyV1MessageInteraction:
        return ProxyV1MessageInteraction(self._raw_client, self._server, self._auth)

    @cached_property
    def proxy_v1_participant(self) -> ProxyV1Participant:
        return ProxyV1Participant(self._raw_client, self._server, self._auth)

    @cached_property
    def proxy_v1_phone_number(self) -> ProxyV1PhoneNumber:
        return ProxyV1PhoneNumber(self._raw_client, self._server, self._auth)

    @cached_property
    def proxy_v1_service_api(self) -> ProxyV1ServiceApi:
        return ProxyV1ServiceApi(self._raw_client, self._server, self._auth)

    @cached_property
    def proxy_v1_session(self) -> ProxyV1Session:
        return ProxyV1Session(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v1_engagement(self) -> StudioV1Engagement:
        return StudioV1Engagement(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v1_engagement_context(self) -> StudioV1EngagementContext:
        return StudioV1EngagementContext(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v1_execution(self) -> StudioV1Execution:
        return StudioV1Execution(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v1_execution_context(self) -> StudioV1ExecutionContext:
        return StudioV1ExecutionContext(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v1_execution_step(self) -> StudioV1ExecutionStep:
        return StudioV1ExecutionStep(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v1_execution_step_context(self) -> StudioV1ExecutionStepContext:
        return StudioV1ExecutionStepContext(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v1_flow_api(self) -> StudioV1FlowApi:
        return StudioV1FlowApi(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v1_step(self) -> StudioV1Step:
        return StudioV1Step(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v1_step_context(self) -> StudioV1StepContext:
        return StudioV1StepContext(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v2_execution(self) -> StudioV2Execution:
        return StudioV2Execution(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v2_execution_context(self) -> StudioV2ExecutionContext:
        return StudioV2ExecutionContext(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v2_execution_step(self) -> StudioV2ExecutionStep:
        return StudioV2ExecutionStep(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v2_execution_step_context(self) -> StudioV2ExecutionStepContext:
        return StudioV2ExecutionStepContext(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v2_flow_api(self) -> StudioV2FlowApi:
        return StudioV2FlowApi(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v2_flow_revision(self) -> StudioV2FlowRevision:
        return StudioV2FlowRevision(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v2_flow_test_user_api(self) -> StudioV2FlowTestUserApi:
        return StudioV2FlowTestUserApi(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v2_flow_validate_api(self) -> StudioV2FlowValidateApi:
        return StudioV2FlowValidateApi(self._raw_client, self._server, self._auth)

    @cached_property
    def sync_v1_document(self) -> SyncV1Document:
        return SyncV1Document(self._raw_client, self._server, self._auth)

    @cached_property
    def sync_v1_document_permission(self) -> SyncV1DocumentPermission:
        return SyncV1DocumentPermission(self._raw_client, self._server, self._auth)

    @cached_property
    def sync_v1_service_api(self) -> SyncV1ServiceApi:
        return SyncV1ServiceApi(self._raw_client, self._server, self._auth)

    @cached_property
    def sync_v1_stream_message(self) -> SyncV1StreamMessage:
        return SyncV1StreamMessage(self._raw_client, self._server, self._auth)

    @cached_property
    def sync_v1_sync_list(self) -> SyncV1SyncList:
        return SyncV1SyncList(self._raw_client, self._server, self._auth)

    @cached_property
    def sync_v1_sync_list_item(self) -> SyncV1SyncListItem:
        return SyncV1SyncListItem(self._raw_client, self._server, self._auth)

    @cached_property
    def sync_v1_sync_list_permission(self) -> SyncV1SyncListPermission:
        return SyncV1SyncListPermission(self._raw_client, self._server, self._auth)

    @cached_property
    def sync_v1_sync_map(self) -> SyncV1SyncMap:
        return SyncV1SyncMap(self._raw_client, self._server, self._auth)

    @cached_property
    def sync_v1_sync_map_item(self) -> SyncV1SyncMapItem:
        return SyncV1SyncMapItem(self._raw_client, self._server, self._auth)

    @cached_property
    def sync_v1_sync_map_permission(self) -> SyncV1SyncMapPermission:
        return SyncV1SyncMapPermission(self._raw_client, self._server, self._auth)

    @cached_property
    def sync_v1_sync_stream(self) -> SyncV1SyncStream:
        return SyncV1SyncStream(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_activity(self) -> TaskrouterV1Activity:
        return TaskrouterV1Activity(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_event(self) -> TaskrouterV1Event:
        return TaskrouterV1Event(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_task(self) -> TaskrouterV1Task:
        return TaskrouterV1Task(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_task_channel(self) -> TaskrouterV1TaskChannel:
        return TaskrouterV1TaskChannel(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_task_queue(self) -> TaskrouterV1TaskQueue:
        return TaskrouterV1TaskQueue(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_task_queue_bulk_real_time_statistics(self) -> TaskrouterV1TaskQueueBulkRealTimeStatistics:
        return TaskrouterV1TaskQueueBulkRealTimeStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_task_queue_cumulative_statistics(self) -> TaskrouterV1TaskQueueCumulativeStatistics:
        return TaskrouterV1TaskQueueCumulativeStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_task_queue_real_time_statistics(self) -> TaskrouterV1TaskQueueRealTimeStatistics:
        return TaskrouterV1TaskQueueRealTimeStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_task_queue_statistics(self) -> TaskrouterV1TaskQueueStatistics:
        return TaskrouterV1TaskQueueStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_task_queues_statistics(self) -> TaskrouterV1TaskQueuesStatistics:
        return TaskrouterV1TaskQueuesStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_task_reservation(self) -> TaskrouterV1TaskReservation:
        return TaskrouterV1TaskReservation(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_worker(self) -> TaskrouterV1Worker:
        return TaskrouterV1Worker(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_worker_channel(self) -> TaskrouterV1WorkerChannel:
        return TaskrouterV1WorkerChannel(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_worker_reservation(self) -> TaskrouterV1WorkerReservation:
        return TaskrouterV1WorkerReservation(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_worker_statistics(self) -> TaskrouterV1WorkerStatistics:
        return TaskrouterV1WorkerStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_workers_cumulative_statistics(self) -> TaskrouterV1WorkersCumulativeStatistics:
        return TaskrouterV1WorkersCumulativeStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_workers_real_time_statistics(self) -> TaskrouterV1WorkersRealTimeStatistics:
        return TaskrouterV1WorkersRealTimeStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_workers_statistics(self) -> TaskrouterV1WorkersStatistics:
        return TaskrouterV1WorkersStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_workflow(self) -> TaskrouterV1Workflow:
        return TaskrouterV1Workflow(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_workflow_cumulative_statistics(self) -> TaskrouterV1WorkflowCumulativeStatistics:
        return TaskrouterV1WorkflowCumulativeStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_workflow_real_time_statistics(self) -> TaskrouterV1WorkflowRealTimeStatistics:
        return TaskrouterV1WorkflowRealTimeStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_workflow_statistics(self) -> TaskrouterV1WorkflowStatistics:
        return TaskrouterV1WorkflowStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_workspace_api(self) -> TaskrouterV1WorkspaceApi:
        return TaskrouterV1WorkspaceApi(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_workspace_cumulative_statistics(self) -> TaskrouterV1WorkspaceCumulativeStatistics:
        return TaskrouterV1WorkspaceCumulativeStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_workspace_real_time_statistics(self) -> TaskrouterV1WorkspaceRealTimeStatistics:
        return TaskrouterV1WorkspaceRealTimeStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_workspace_statistics(self) -> TaskrouterV1WorkspaceStatistics:
        return TaskrouterV1WorkspaceStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_compliance_inquiries(self) -> TrusthubV1ComplianceInquiries:
        return TrusthubV1ComplianceInquiries(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_compliance_registration_inquiries(self) -> TrusthubV1ComplianceRegistrationInquiries:
        return TrusthubV1ComplianceRegistrationInquiries(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_compliance_tollfree_inquiries(self) -> TrusthubV1ComplianceTollfreeInquiries:
        return TrusthubV1ComplianceTollfreeInquiries(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_customer_profiles(self) -> TrusthubV1CustomerProfiles:
        return TrusthubV1CustomerProfiles(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_customer_profiles_channel_endpoint_assignment(
        self
    ) -> TrusthubV1CustomerProfilesChannelEndpointAssignment:
        return TrusthubV1CustomerProfilesChannelEndpointAssignment(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_customer_profiles_entity_assignments(self) -> TrusthubV1CustomerProfilesEntityAssignments:
        return TrusthubV1CustomerProfilesEntityAssignments(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_customer_profiles_evaluations(self) -> TrusthubV1CustomerProfilesEvaluations:
        return TrusthubV1CustomerProfilesEvaluations(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_end_user_api(self) -> TrusthubV1EndUserApi:
        return TrusthubV1EndUserApi(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_end_user_type(self) -> TrusthubV1EndUserType:
        return TrusthubV1EndUserType(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_policies_api(self) -> TrusthubV1PoliciesApi:
        return TrusthubV1PoliciesApi(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_supporting_document_api(self) -> TrusthubV1SupportingDocumentApi:
        return TrusthubV1SupportingDocumentApi(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_supporting_document_type(self) -> TrusthubV1SupportingDocumentType:
        return TrusthubV1SupportingDocumentType(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_trust_products(self) -> TrusthubV1TrustProducts:
        return TrusthubV1TrustProducts(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_trust_products_channel_endpoint_assignment(
        self
    ) -> TrusthubV1TrustProductsChannelEndpointAssignment:
        return TrusthubV1TrustProductsChannelEndpointAssignment(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_trust_products_entity_assignments(self) -> TrusthubV1TrustProductsEntityAssignments:
        return TrusthubV1TrustProductsEntityAssignments(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_trust_products_evaluations(self) -> TrusthubV1TrustProductsEvaluations:
        return TrusthubV1TrustProductsEvaluations(self._raw_client, self._server, self._auth)

    @cached_property
    def twilio_insights(self) -> TwilioInsights:
        return TwilioInsights(self._raw_client, self._server, self._auth)

    @cached_property
    def v2_short_code_applications(self) -> V2ShortCodeApplications:
        return V2ShortCodeApplications(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_access_token(self) -> VerifyV2AccessToken:
        return VerifyV2AccessToken(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_bucket(self) -> VerifyV2Bucket:
        return VerifyV2Bucket(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_challenge(self) -> VerifyV2Challenge:
        return VerifyV2Challenge(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_entity(self) -> VerifyV2Entity:
        return VerifyV2Entity(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_factor(self) -> VerifyV2Factor:
        return VerifyV2Factor(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_form_api(self) -> VerifyV2FormApi:
        return VerifyV2FormApi(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_messaging_configuration(self) -> VerifyV2MessagingConfiguration:
        return VerifyV2MessagingConfiguration(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_new_challenge(self) -> VerifyV2NewChallenge:
        return VerifyV2NewChallenge(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_new_factor(self) -> VerifyV2NewFactor:
        return VerifyV2NewFactor(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_notification(self) -> VerifyV2Notification:
        return VerifyV2Notification(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_rate_limit(self) -> VerifyV2RateLimit:
        return VerifyV2RateLimit(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_safelist_api(self) -> VerifyV2SafelistApi:
        return VerifyV2SafelistApi(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_service_api(self) -> VerifyV2ServiceApi:
        return VerifyV2ServiceApi(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_template(self) -> VerifyV2Template:
        return VerifyV2Template(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_verification(self) -> VerifyV2Verification:
        return VerifyV2Verification(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_verification_attempt_api(self) -> VerifyV2VerificationAttemptApi:
        return VerifyV2VerificationAttemptApi(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_verification_attempts_summary_api(self) -> VerifyV2VerificationAttemptsSummaryApi:
        return VerifyV2VerificationAttemptsSummaryApi(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_verification_check(self) -> VerifyV2VerificationCheck:
        return VerifyV2VerificationCheck(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_webhook(self) -> VerifyV2Webhook:
        return VerifyV2Webhook(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_anonymize(self) -> VideoV1Anonymize:
        return VideoV1Anonymize(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_composition_api(self) -> VideoV1CompositionApi:
        return VideoV1CompositionApi(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_composition_hook_api(self) -> VideoV1CompositionHookApi:
        return VideoV1CompositionHookApi(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_composition_settings_api(self) -> VideoV1CompositionSettingsApi:
        return VideoV1CompositionSettingsApi(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_participant(self) -> VideoV1Participant:
        return VideoV1Participant(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_published_track(self) -> VideoV1PublishedTrack:
        return VideoV1PublishedTrack(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_recording_api(self) -> VideoV1RecordingApi:
        return VideoV1RecordingApi(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_recording_rules(self) -> VideoV1RecordingRules:
        return VideoV1RecordingRules(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_recording_settings_api(self) -> VideoV1RecordingSettingsApi:
        return VideoV1RecordingSettingsApi(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_room_api(self) -> VideoV1RoomApi:
        return VideoV1RoomApi(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_room_recording(self) -> VideoV1RoomRecording:
        return VideoV1RoomRecording(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_subscribe_rules(self) -> VideoV1SubscribeRules:
        return VideoV1SubscribeRules(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_subscribed_track(self) -> VideoV1SubscribedTrack:
        return VideoV1SubscribedTrack(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_transcriptions(self) -> VideoV1Transcriptions:
        return VideoV1Transcriptions(self._raw_client, self._server, self._auth)

    @cached_property
    def with_raw_response(self) -> ApiWithRawResponse:
        return ApiWithRawResponse(self._raw_client, self._server, self._auth)

    def create_bulk_lookup(
        self,
        *,
        body: LookupRequest | LookupRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LookupResponse1:
        """Discussions made regarding how to help the customer to correlation request and response objects:
        - Respecting the natural order (requests vs. response)
        - Using phone numbers as unique key
        - Adding a correlation_id key

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.create_bulk_lookup(body=body, request_options=request_options).unwrap()

    def create_lookup_phone_number_overrides(
        self,
        field: str,
        phone_number: str,
        *,
        body: OverridesRequest | OverridesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OverridesResponse:
        """Create an Override for a specific package and phone number.

        Args:
            field: Value sent with the request.
            phone_number: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: Bad Request ``error`` is ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self.with_raw_response.create_lookup_phone_number_overrides(
            field, phone_number, body=body, request_options=request_options
        ).unwrap()

    def delete_lookup_phone_number_overrides(
        self, field: str, phone_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete an Override for a specific package and phone number.

        Args:
            field: Value sent with the request.
            phone_number: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content

        Raises:
            ApiError: Bad Request ``error`` is ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self.with_raw_response.delete_lookup_phone_number_overrides(
            field, phone_number, request_options=request_options
        ).unwrap()

    def delete_lookup_rate_limit(
        self, field: str, bucket: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            field: bucket name
            bucket: bucket name
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content

        Raises:
            ApiError: Bad Request ``error`` is ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self.with_raw_response.delete_lookup_rate_limit(field, bucket, request_options=request_options).unwrap()

    def fetch_lookup_account_rate_limits(
        self, *, fields: list[str] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> RateLimitListResponse:
        """Retrieve the list of rate limits for all fields (if any) It returns also the twilio rate limits.

        Args:
            fields: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request ``error`` is ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self.with_raw_response.fetch_lookup_account_rate_limits(
            fields=fields, request_options=request_options
        ).unwrap()

    def fetch_lookup_phone_number_overrides(
        self, field: str, phone_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> OverridesResponse:
        """Retrieve an Override for a specific package and phone number.

        Args:
            field: Value sent with the request.
            phone_number: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Not Found ``error`` is ``AccountsCallsRecordingsSidJson201041408Error1 |
                RawError``."""
        return self.with_raw_response.fetch_lookup_phone_number_overrides(
            field, phone_number, request_options=request_options
        ).unwrap()

    def fetch_lookup_rate_limit(
        self, field: str, bucket: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RateLimitResponse:
        """Send a ``GET`` request.

        Args:
            field: bucket name
            bucket: bucket name
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Not Found ``error`` is ``AccountsCallsRecordingsSidJson201041408Error1 |
                RawError``."""
        return self.with_raw_response.fetch_lookup_rate_limit(field, bucket, request_options=request_options).unwrap()

    def update_challenge_passkeys(
        self,
        service_sid: str,
        body: ApprovePasskeysChallengeRequest | ApprovePasskeysChallengeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V2ServicesPasskeysApproveChallengeResponse:
        """Approve a Passkeys challenge

        Args:
            service_sid: The unique SID identifier of the Service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Approved

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.update_challenge_passkeys(
            service_sid, body, request_options=request_options
        ).unwrap()

    def update_lookup_phone_number_overrides(
        self,
        field: str,
        phone_number: str,
        *,
        body: OverridesRequest | OverridesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OverridesResponse:
        """Update an Override for a specific package and phone number.

        Args:
            field: Value sent with the request.
            phone_number: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Not Found ``error`` is ``AccountsCallsRecordingsSidJson201041408Error1 |
                RawError``."""
        return self.with_raw_response.update_lookup_phone_number_overrides(
            field, phone_number, body=body, request_options=request_options
        ).unwrap()

    def update_lookup_rate_limit(
        self,
        field: str,
        bucket: str,
        *,
        body: RateLimitRequest | RateLimitRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RateLimitResponse:
        """Send a ``PUT`` request.

        Args:
            field: field name
            bucket: bucket name
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request ``error`` is ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self.with_raw_response.update_lookup_rate_limit(
            field, bucket, body=body, request_options=request_options
        ).unwrap()

    def update_passkeys_factor(
        self,
        service_sid: str,
        body: VerifyPasskeysFactorRequest | VerifyPasskeysFactorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V2ServicesPasskeysVerifyFactorResponse:
        """Verify a Passkeys Factor

        Args:
            service_sid: The unique SID identifier of the Service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.update_passkeys_factor(
            service_sid, body, request_options=request_options
        ).unwrap()

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


class ApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_bulk_lookup(
        self,
        *,
        body: LookupRequest | LookupRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LookupResponse1, RawError]:
        """Discussions made regarding how to help the customer to correlation request and response objects:
        - Respecting the natural order (requests vs. response)
        - Using phone numbers as unique key
        - Adding a correlation_id key

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default4("/v2/batch/query"),
            body=json_body[LookupRequest | LookupRequestDict | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[LookupResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_lookup_phone_number_overrides(
        self,
        field: str,
        phone_number: str,
        *,
        body: OverridesRequest | OverridesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OverridesResponse, CreateLookupPhoneNumberOverridesErrorBody]:
        """Create an Override for a specific package and phone number.

        Args:
            field: Value sent with the request.
            phone_number: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default4("/v2/PhoneNumbers/{PhoneNumber}/Overrides/{Field}"),
            path_params=[param[str]("Field", field), param[str]("PhoneNumber", phone_number)],
            body=json_body[OverridesRequest | OverridesRequestDict | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[OverridesResponse],
            error_mapper=create_lookup_phone_number_overrides_error_mapper,
            request_options=request_options,
        )

    def delete_lookup_phone_number_overrides(
        self, field: str, phone_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteLookupPhoneNumberOverridesErrorBody]:
        """Delete an Override for a specific package and phone number.

        Args:
            field: Value sent with the request.
            phone_number: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default4("/v2/PhoneNumbers/{PhoneNumber}/Overrides/{Field}"),
            path_params=[param[str]("Field", field), param[str]("PhoneNumber", phone_number)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=delete_lookup_phone_number_overrides_error_mapper,
            request_options=request_options,
        )

    def delete_lookup_rate_limit(
        self, field: str, bucket: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteLookupRateLimitErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            field: bucket name
            bucket: bucket name
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default4("/v2/RateLimits/Fields/{Field}/Bucket/{Bucket}"),
            path_params=[param[str]("Field", field), param[str]("Bucket", bucket)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=delete_lookup_rate_limit_error_mapper,
            request_options=request_options,
        )

    def fetch_lookup_account_rate_limits(
        self, *, fields: list[str] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RateLimitListResponse, FetchLookupAccountRateLimitsErrorBody]:
        """Retrieve the list of rate limits for all fields (if any) It returns also the twilio rate limits.

        Args:
            fields: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default4("/v2/RateLimits"),
            query_params=[param[list[str] | None]("Fields", fields)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[RateLimitListResponse],
            error_mapper=fetch_lookup_account_rate_limits_error_mapper,
            request_options=request_options,
        )

    def fetch_lookup_phone_number_overrides(
        self, field: str, phone_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OverridesResponse, FetchLookupPhoneNumberOverridesErrorBody]:
        """Retrieve an Override for a specific package and phone number.

        Args:
            field: Value sent with the request.
            phone_number: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default4("/v2/PhoneNumbers/{PhoneNumber}/Overrides/{Field}"),
            path_params=[param[str]("Field", field), param[str]("PhoneNumber", phone_number)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[OverridesResponse],
            error_mapper=fetch_lookup_phone_number_overrides_error_mapper,
            request_options=request_options,
        )

    def fetch_lookup_rate_limit(
        self, field: str, bucket: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RateLimitResponse, FetchLookupRateLimitErrorBody]:
        """Send a ``GET`` request.

        Args:
            field: bucket name
            bucket: bucket name
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default4("/v2/RateLimits/Fields/{Field}/Bucket/{Bucket}"),
            path_params=[param[str]("Field", field), param[str]("Bucket", bucket)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[RateLimitResponse],
            error_mapper=fetch_lookup_rate_limit_error_mapper,
            request_options=request_options,
        )

    def update_challenge_passkeys(
        self,
        service_sid: str,
        body: ApprovePasskeysChallengeRequest | ApprovePasskeysChallengeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V2ServicesPasskeysApproveChallengeResponse, RawError]:
        """Approve a Passkeys challenge

        Args:
            service_sid: The unique SID identifier of the Service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/Passkeys/ApproveChallenge"),
            path_params=[param[str]("ServiceSid", service_sid)],
            body=json_body[ApprovePasskeysChallengeRequest | ApprovePasskeysChallengeRequestDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[V2ServicesPasskeysApproveChallengeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_lookup_phone_number_overrides(
        self,
        field: str,
        phone_number: str,
        *,
        body: OverridesRequest | OverridesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OverridesResponse, UpdateLookupPhoneNumberOverridesErrorBody]:
        """Update an Override for a specific package and phone number.

        Args:
            field: Value sent with the request.
            phone_number: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default4("/v2/PhoneNumbers/{PhoneNumber}/Overrides/{Field}"),
            path_params=[param[str]("Field", field), param[str]("PhoneNumber", phone_number)],
            body=json_body[OverridesRequest | OverridesRequestDict | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[OverridesResponse],
            error_mapper=update_lookup_phone_number_overrides_error_mapper,
            request_options=request_options,
        )

    def update_lookup_rate_limit(
        self,
        field: str,
        bucket: str,
        *,
        body: RateLimitRequest | RateLimitRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RateLimitResponse, UpdateLookupRateLimitErrorBody]:
        """Send a ``PUT`` request.

        Args:
            field: field name
            bucket: bucket name
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default4("/v2/RateLimits/Fields/{Field}/Bucket/{Bucket}"),
            path_params=[param[str]("Field", field), param[str]("Bucket", bucket)],
            body=json_body[RateLimitRequest | RateLimitRequestDict | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[RateLimitResponse],
            error_mapper=update_lookup_rate_limit_error_mapper,
            request_options=request_options,
        )

    def update_passkeys_factor(
        self,
        service_sid: str,
        body: VerifyPasskeysFactorRequest | VerifyPasskeysFactorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V2ServicesPasskeysVerifyFactorResponse, RawError]:
        """Verify a Passkeys Factor

        Args:
            service_sid: The unique SID identifier of the Service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/Passkeys/VerifyFactor"),
            path_params=[param[str]("ServiceSid", service_sid)],
            body=json_body[VerifyPasskeysFactorRequest | VerifyPasskeysFactorRequestDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[V2ServicesPasskeysVerifyFactorResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


Client = TwilioClient
