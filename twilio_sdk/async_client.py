from __future__ import annotations

from functools import cached_property
from types import TracebackType
from uuid import UUID, uuid4

from typing_extensions import Self

from .apis.api20100401_account import AsyncApi20100401Account
from .apis.api20100401_add_on_result import AsyncApi20100401AddOnResult
from .apis.api20100401_address import AsyncApi20100401Address
from .apis.api20100401_all_time import AsyncApi20100401AllTime
from .apis.api20100401_application import AsyncApi20100401Application
from .apis.api20100401_assigned_add_on import AsyncApi20100401AssignedAddOn
from .apis.api20100401_assigned_add_on_extension import AsyncApi20100401AssignedAddOnExtension
from .apis.api20100401_auth_calls_credential_list_mapping import AsyncApi20100401AuthCallsCredentialListMapping
from .apis.api20100401_auth_calls_ip_access_control_list_mapping import (
    AsyncApi20100401AuthCallsIpAccessControlListMapping,
)
from .apis.api20100401_auth_registrations_credential_list_mapping import (
    AsyncApi20100401AuthRegistrationsCredentialListMapping,
)
from .apis.api20100401_authorized_connect_app import AsyncApi20100401AuthorizedConnectApp
from .apis.api20100401_available_phone_number_country import AsyncApi20100401AvailablePhoneNumberCountry
from .apis.api20100401_balance import AsyncApi20100401Balance
from .apis.api20100401_call import AsyncApi20100401Call
from .apis.api20100401_call_notification import AsyncApi20100401CallNotification
from .apis.api20100401_call_recording import AsyncApi20100401CallRecording
from .apis.api20100401_call_transcription import AsyncApi20100401CallTranscription
from .apis.api20100401_conference import AsyncApi20100401Conference
from .apis.api20100401_conference_recording import AsyncApi20100401ConferenceRecording
from .apis.api20100401_connect_app import AsyncApi20100401ConnectApp
from .apis.api20100401_credential import AsyncApi20100401Credential
from .apis.api20100401_credential_list import AsyncApi20100401CredentialList
from .apis.api20100401_credential_list_mapping import AsyncApi20100401CredentialListMapping
from .apis.api20100401_daily import AsyncApi20100401Daily
from .apis.api20100401_data import AsyncApi20100401Data
from .apis.api20100401_dependent_phone_number import AsyncApi20100401DependentPhoneNumber
from .apis.api20100401_domain import AsyncApi20100401Domain
from .apis.api20100401_event import AsyncApi20100401Event
from .apis.api20100401_feedback import AsyncApi20100401Feedback
from .apis.api20100401_incoming_phone_number import AsyncApi20100401IncomingPhoneNumber
from .apis.api20100401_incoming_phone_number_local import AsyncApi20100401IncomingPhoneNumberLocal
from .apis.api20100401_incoming_phone_number_mobile import AsyncApi20100401IncomingPhoneNumberMobile
from .apis.api20100401_incoming_phone_number_toll_free import AsyncApi20100401IncomingPhoneNumberTollFree
from .apis.api20100401_ip_access_control_list import AsyncApi20100401IpAccessControlList
from .apis.api20100401_ip_access_control_list_mapping import AsyncApi20100401IpAccessControlListMapping
from .apis.api20100401_key import AsyncApi20100401Key
from .apis.api20100401_last_month import AsyncApi20100401LastMonth
from .apis.api20100401_local import AsyncApi20100401Local
from .apis.api20100401_machine_to_machine import AsyncApi20100401MachineToMachine
from .apis.api20100401_media import AsyncApi20100401Media
from .apis.api20100401_media_instance import AsyncApi20100401MediaInstance
from .apis.api20100401_member import AsyncApi20100401Member
from .apis.api20100401_message import AsyncApi20100401Message
from .apis.api20100401_mobile import AsyncApi20100401Mobile
from .apis.api20100401_monthly import AsyncApi20100401Monthly
from .apis.api20100401_national import AsyncApi20100401National
from .apis.api20100401_new_key import AsyncApi20100401NewKey
from .apis.api20100401_new_signing_key import AsyncApi20100401NewSigningKey
from .apis.api20100401_notification import AsyncApi20100401Notification
from .apis.api20100401_outgoing_caller_id import AsyncApi20100401OutgoingCallerId
from .apis.api20100401_participant import AsyncApi20100401Participant
from .apis.api20100401_payload import AsyncApi20100401Payload
from .apis.api20100401_payment import AsyncApi20100401Payment
from .apis.api20100401_queue import AsyncApi20100401Queue
from .apis.api20100401_record import AsyncApi20100401Record
from .apis.api20100401_recording import AsyncApi20100401Recording
from .apis.api20100401_recording_transcription import AsyncApi20100401RecordingTranscription
from .apis.api20100401_shared_cost import AsyncApi20100401SharedCost
from .apis.api20100401_short_code import AsyncApi20100401ShortCode
from .apis.api20100401_signing_key import AsyncApi20100401SigningKey
from .apis.api20100401_sip_ip_address import AsyncApi20100401SipIpAddress
from .apis.api20100401_siprec import AsyncApi20100401Siprec
from .apis.api20100401_stream import AsyncApi20100401Stream
from .apis.api20100401_this_month import AsyncApi20100401ThisMonth
from .apis.api20100401_today import AsyncApi20100401Today
from .apis.api20100401_token import AsyncApi20100401Token
from .apis.api20100401_toll_free import AsyncApi20100401TollFree
from .apis.api20100401_transcription import AsyncApi20100401Transcription
from .apis.api20100401_trigger import AsyncApi20100401Trigger
from .apis.api20100401_user_defined_message import AsyncApi20100401UserDefinedMessage
from .apis.api20100401_user_defined_message_subscription import AsyncApi20100401UserDefinedMessageSubscription
from .apis.api20100401_validation_request import AsyncApi20100401ValidationRequest
from .apis.api20100401_voip import AsyncApi20100401Voip
from .apis.api20100401_yearly import AsyncApi20100401Yearly
from .apis.api20100401_yesterday import AsyncApi20100401Yesterday
from .apis.content_v2_content import AsyncContentV2Content
from .apis.content_v2_content_and_approvals import AsyncContentV2ContentAndApprovals
from .apis.contentv1_approval_create import AsyncContentv1ApprovalCreate
from .apis.contentv1_approval_fetch import AsyncContentv1ApprovalFetch
from .apis.contentv1_content_and_approvals_api import AsyncContentv1ContentAndApprovalsApi
from .apis.contentv1_content_api import AsyncContentv1ContentApi
from .apis.contentv1_legacy_content_api import AsyncContentv1LegacyContentApi
from .apis.conversations_v1_address_configuration import AsyncConversationsV1AddressConfiguration
from .apis.conversations_v1_binding import AsyncConversationsV1Binding
from .apis.conversations_v1_configuration_api import AsyncConversationsV1ConfigurationApi
from .apis.conversations_v1_conversation_api import AsyncConversationsV1ConversationApi
from .apis.conversations_v1_conversation_with_participants_api import (
    AsyncConversationsV1ConversationWithParticipantsApi,
)
from .apis.conversations_v1_credential_api import AsyncConversationsV1CredentialApi
from .apis.conversations_v1_delivery_receipt import AsyncConversationsV1DeliveryReceipt
from .apis.conversations_v1_message import AsyncConversationsV1Message
from .apis.conversations_v1_notification import AsyncConversationsV1Notification
from .apis.conversations_v1_participant import AsyncConversationsV1Participant
from .apis.conversations_v1_participant_conversation_api import AsyncConversationsV1ParticipantConversationApi
from .apis.conversations_v1_role_api import AsyncConversationsV1RoleApi
from .apis.conversations_v1_service_api import AsyncConversationsV1ServiceApi
from .apis.conversations_v1_user_api import AsyncConversationsV1UserApi
from .apis.conversations_v1_user_conversation import AsyncConversationsV1UserConversation
from .apis.conversations_v1_webhook import AsyncConversationsV1Webhook
from .apis.conversations_v2_action_api import AsyncConversationsV2ActionApi
from .apis.conversations_v2_communication_api import AsyncConversationsV2CommunicationApi
from .apis.conversations_v2_configuration_api import AsyncConversationsV2ConfigurationApi
from .apis.conversations_v2_conversation_api import AsyncConversationsV2ConversationApi
from .apis.conversations_v2_operation import AsyncConversationsV2Operation
from .apis.conversations_v2_participant_api import AsyncConversationsV2ParticipantApi
from .apis.flex_v1_assessments import AsyncFlexV1Assessments
from .apis.flex_v1_channel_api import AsyncFlexV1ChannelApi
from .apis.flex_v1_configuration_api import AsyncFlexV1ConfigurationApi
from .apis.flex_v1_configured_plugin import AsyncFlexV1ConfiguredPlugin
from .apis.flex_v1_flex_flow_api import AsyncFlexV1FlexFlowApi
from .apis.flex_v1_insights_assessments_comment_api import AsyncFlexV1InsightsAssessmentsCommentApi
from .apis.flex_v1_insights_conversations_api import AsyncFlexV1InsightsConversationsApi
from .apis.flex_v1_insights_questionnaires_api import AsyncFlexV1InsightsQuestionnairesApi
from .apis.flex_v1_insights_questionnaires_category_api import AsyncFlexV1InsightsQuestionnairesCategoryApi
from .apis.flex_v1_insights_questionnaires_question_api import AsyncFlexV1InsightsQuestionnairesQuestionApi
from .apis.flex_v1_insights_segments_api import AsyncFlexV1InsightsSegmentsApi
from .apis.flex_v1_insights_session_api import AsyncFlexV1InsightsSessionApi
from .apis.flex_v1_insights_settings_answer_sets_api import AsyncFlexV1InsightsSettingsAnswerSetsApi
from .apis.flex_v1_insights_settings_comment_api import AsyncFlexV1InsightsSettingsCommentApi
from .apis.flex_v1_insights_user_roles_api import AsyncFlexV1InsightsUserRolesApi
from .apis.flex_v1_interaction_api import AsyncFlexV1InteractionApi
from .apis.flex_v1_interaction_channel import AsyncFlexV1InteractionChannel
from .apis.flex_v1_interaction_channel_invite import AsyncFlexV1InteractionChannelInvite
from .apis.flex_v1_interaction_channel_participant import AsyncFlexV1InteractionChannelParticipant
from .apis.flex_v1_interaction_transfer import AsyncFlexV1InteractionTransfer
from .apis.flex_v1_plugin_api import AsyncFlexV1PluginApi
from .apis.flex_v1_plugin_archive_api import AsyncFlexV1PluginArchiveApi
from .apis.flex_v1_plugin_configuration_api import AsyncFlexV1PluginConfigurationApi
from .apis.flex_v1_plugin_configuration_archive_api import AsyncFlexV1PluginConfigurationArchiveApi
from .apis.flex_v1_plugin_release_api import AsyncFlexV1PluginReleaseApi
from .apis.flex_v1_plugin_version_archive_api import AsyncFlexV1PluginVersionArchiveApi
from .apis.flex_v1_plugin_versions import AsyncFlexV1PluginVersions
from .apis.flex_v1_provisioning_status_api import AsyncFlexV1ProvisioningStatusApi
from .apis.flex_v1_web_channel_api import AsyncFlexV1WebChannelApi
from .apis.flex_v2_flex_user_api import AsyncFlexV2FlexUserApi
from .apis.flex_v2_web_channels import AsyncFlexV2WebChannels
from .apis.insights_v1_annotation import AsyncInsightsV1Annotation
from .apis.insights_v1_call_api import AsyncInsightsV1CallApi
from .apis.insights_v1_call_summaries_api import AsyncInsightsV1CallSummariesApi
from .apis.insights_v1_call_summary_api import AsyncInsightsV1CallSummaryApi
from .apis.insights_v1_conference_api import AsyncInsightsV1ConferenceApi
from .apis.insights_v1_conference_participant import AsyncInsightsV1ConferenceParticipant
from .apis.insights_v1_create_account_report import AsyncInsightsV1CreateAccountReport
from .apis.insights_v1_create_inbound_phone_numbers_report import AsyncInsightsV1CreateInboundPhoneNumbersReport
from .apis.insights_v1_create_outbound_phone_numbers_report import AsyncInsightsV1CreateOutboundPhoneNumbersReport
from .apis.insights_v1_event import AsyncInsightsV1Event
from .apis.insights_v1_get_account_report import AsyncInsightsV1GetAccountReport
from .apis.insights_v1_get_inbound_phone_numbers_report import AsyncInsightsV1GetInboundPhoneNumbersReport
from .apis.insights_v1_get_outbound_phone_numbers_report import AsyncInsightsV1GetOutboundPhoneNumbersReport
from .apis.insights_v1_metric import AsyncInsightsV1Metric
from .apis.insights_v1_participant import AsyncInsightsV1Participant
from .apis.insights_v1_room import AsyncInsightsV1Room
from .apis.insights_v1_setting import AsyncInsightsV1Setting
from .apis.lookups_v1_phone_number_api import AsyncLookupsV1PhoneNumberApi
from .apis.lookups_v2_phone_number import AsyncLookupsV2PhoneNumber
from .apis.messaging_v1_alpha_sender import AsyncMessagingV1AlphaSender
from .apis.messaging_v1_brand_registration import AsyncMessagingV1BrandRegistration
from .apis.messaging_v1_brand_registration_otp import AsyncMessagingV1BrandRegistrationOtp
from .apis.messaging_v1_brand_vetting import AsyncMessagingV1BrandVetting
from .apis.messaging_v1_channel_sender import AsyncMessagingV1ChannelSender
from .apis.messaging_v1_deactivations import AsyncMessagingV1Deactivations
from .apis.messaging_v1_destination_alpha_sender import AsyncMessagingV1DestinationAlphaSender
from .apis.messaging_v1_domain_certs import AsyncMessagingV1DomainCerts
from .apis.messaging_v1_domain_config_api import AsyncMessagingV1DomainConfigApi
from .apis.messaging_v1_domain_config_messaging_service_api import AsyncMessagingV1DomainConfigMessagingServiceApi
from .apis.messaging_v1_domain_validate_dns import AsyncMessagingV1DomainValidateDns
from .apis.messaging_v1_external_campaign_api import AsyncMessagingV1ExternalCampaignApi
from .apis.messaging_v1_linkshortening_messaging_service_api import AsyncMessagingV1LinkshorteningMessagingServiceApi
from .apis.messaging_v1_linkshortening_messaging_service_domain_association_api import (
    AsyncMessagingV1LinkshorteningMessagingServiceDomainAssociationApi,
)
from .apis.messaging_v1_phone_number import AsyncMessagingV1PhoneNumber
from .apis.messaging_v1_request_managed_cert_api import AsyncMessagingV1RequestManagedCertApi
from .apis.messaging_v1_service_api import AsyncMessagingV1ServiceApi
from .apis.messaging_v1_short_code import AsyncMessagingV1ShortCode
from .apis.messaging_v1_tollfree_verification_api import AsyncMessagingV1TollfreeVerificationApi
from .apis.messaging_v1_us_app_to_person import AsyncMessagingV1UsAppToPerson
from .apis.messaging_v1_us_app_to_person_usecase import AsyncMessagingV1UsAppToPersonUsecase
from .apis.messaging_v1_usecase_api import AsyncMessagingV1UsecaseApi
from .apis.messaging_v2_channels_sender import AsyncMessagingV2ChannelsSender
from .apis.messaging_v2_domain_certs import AsyncMessagingV2DomainCerts
from .apis.messaging_v2_typing_indicator import AsyncMessagingV2TypingIndicator
from .apis.messaging_v3_typing_indicator import AsyncMessagingV3TypingIndicator
from .apis.numbers_v1_bulk_eligibility_api import AsyncNumbersV1BulkEligibilityApi
from .apis.numbers_v1_eligibility_api import AsyncNumbersV1EligibilityApi
from .apis.numbers_v1_porting_port_in_api import AsyncNumbersV1PortingPortInApi
from .apis.numbers_v1_porting_port_in_phone_number_api import AsyncNumbersV1PortingPortInPhoneNumberApi
from .apis.numbers_v1_porting_portability_api import AsyncNumbersV1PortingPortabilityApi
from .apis.numbers_v1_porting_webhook_configuration_api import AsyncNumbersV1PortingWebhookConfigurationApi
from .apis.numbers_v1_porting_webhook_configuration_delete_api import AsyncNumbersV1PortingWebhookConfigurationDeleteApi
from .apis.numbers_v1_porting_webhook_configuration_fetch_api import AsyncNumbersV1PortingWebhookConfigurationFetchApi
from .apis.numbers_v1_sender_id_registration import AsyncNumbersV1SenderIdRegistration
from .apis.numbers_v1_sender_id_registration_embedded_session import AsyncNumbersV1SenderIdRegistrationEmbeddedSession
from .apis.numbers_v1_signing_request_configuration_api import AsyncNumbersV1SigningRequestConfigurationApi
from .apis.numbers_v2_authorization_document_api import AsyncNumbersV2AuthorizationDocumentApi
from .apis.numbers_v2_bulk_hosted_number_order_api import AsyncNumbersV2BulkHostedNumberOrderApi
from .apis.numbers_v2_bundle import AsyncNumbersV2Bundle
from .apis.numbers_v2_bundle_clone_api import AsyncNumbersV2BundleCloneApi
from .apis.numbers_v2_bundle_copy import AsyncNumbersV2BundleCopy
from .apis.numbers_v2_dependent_hosted_number_order import AsyncNumbersV2DependentHostedNumberOrder
from .apis.numbers_v2_end_user import AsyncNumbersV2EndUser
from .apis.numbers_v2_end_user_type import AsyncNumbersV2EndUserType
from .apis.numbers_v2_evaluation import AsyncNumbersV2Evaluation
from .apis.numbers_v2_hosted_number_order_api import AsyncNumbersV2HostedNumberOrderApi
from .apis.numbers_v2_item_assignment import AsyncNumbersV2ItemAssignment
from .apis.numbers_v2_regulation import AsyncNumbersV2Regulation
from .apis.numbers_v2_replace_items import AsyncNumbersV2ReplaceItems
from .apis.numbers_v2_supporting_document import AsyncNumbersV2SupportingDocument
from .apis.numbers_v2_supporting_document_type import AsyncNumbersV2SupportingDocumentType
from .apis.numbers_v3_hosted_numbers_hosted_number_order_api import AsyncNumbersV3HostedNumbersHostedNumberOrderApi
from .apis.proxy_v1_interaction import AsyncProxyV1Interaction
from .apis.proxy_v1_message_interaction import AsyncProxyV1MessageInteraction
from .apis.proxy_v1_participant import AsyncProxyV1Participant
from .apis.proxy_v1_phone_number import AsyncProxyV1PhoneNumber
from .apis.proxy_v1_service_api import AsyncProxyV1ServiceApi
from .apis.proxy_v1_session import AsyncProxyV1Session
from .apis.studio_v1_engagement import AsyncStudioV1Engagement
from .apis.studio_v1_engagement_context import AsyncStudioV1EngagementContext
from .apis.studio_v1_execution import AsyncStudioV1Execution
from .apis.studio_v1_execution_context import AsyncStudioV1ExecutionContext
from .apis.studio_v1_execution_step import AsyncStudioV1ExecutionStep
from .apis.studio_v1_execution_step_context import AsyncStudioV1ExecutionStepContext
from .apis.studio_v1_flow_api import AsyncStudioV1FlowApi
from .apis.studio_v1_step import AsyncStudioV1Step
from .apis.studio_v1_step_context import AsyncStudioV1StepContext
from .apis.studio_v2_execution import AsyncStudioV2Execution
from .apis.studio_v2_execution_context import AsyncStudioV2ExecutionContext
from .apis.studio_v2_execution_step import AsyncStudioV2ExecutionStep
from .apis.studio_v2_execution_step_context import AsyncStudioV2ExecutionStepContext
from .apis.studio_v2_flow_api import AsyncStudioV2FlowApi
from .apis.studio_v2_flow_revision import AsyncStudioV2FlowRevision
from .apis.studio_v2_flow_test_user_api import AsyncStudioV2FlowTestUserApi
from .apis.studio_v2_flow_validate_api import AsyncStudioV2FlowValidateApi
from .apis.sync_v1_document import AsyncSyncV1Document
from .apis.sync_v1_document_permission import AsyncSyncV1DocumentPermission
from .apis.sync_v1_service_api import AsyncSyncV1ServiceApi
from .apis.sync_v1_stream_message import AsyncSyncV1StreamMessage
from .apis.sync_v1_sync_list import AsyncSyncV1SyncList
from .apis.sync_v1_sync_list_item import AsyncSyncV1SyncListItem
from .apis.sync_v1_sync_list_permission import AsyncSyncV1SyncListPermission
from .apis.sync_v1_sync_map import AsyncSyncV1SyncMap
from .apis.sync_v1_sync_map_item import AsyncSyncV1SyncMapItem
from .apis.sync_v1_sync_map_permission import AsyncSyncV1SyncMapPermission
from .apis.sync_v1_sync_stream import AsyncSyncV1SyncStream
from .apis.taskrouter_v1_activity import AsyncTaskrouterV1Activity
from .apis.taskrouter_v1_event import AsyncTaskrouterV1Event
from .apis.taskrouter_v1_task import AsyncTaskrouterV1Task
from .apis.taskrouter_v1_task_channel import AsyncTaskrouterV1TaskChannel
from .apis.taskrouter_v1_task_queue import AsyncTaskrouterV1TaskQueue
from .apis.taskrouter_v1_task_queue_bulk_real_time_statistics import AsyncTaskrouterV1TaskQueueBulkRealTimeStatistics
from .apis.taskrouter_v1_task_queue_cumulative_statistics import AsyncTaskrouterV1TaskQueueCumulativeStatistics
from .apis.taskrouter_v1_task_queue_real_time_statistics import AsyncTaskrouterV1TaskQueueRealTimeStatistics
from .apis.taskrouter_v1_task_queue_statistics import AsyncTaskrouterV1TaskQueueStatistics
from .apis.taskrouter_v1_task_queues_statistics import AsyncTaskrouterV1TaskQueuesStatistics
from .apis.taskrouter_v1_task_reservation import AsyncTaskrouterV1TaskReservation
from .apis.taskrouter_v1_worker import AsyncTaskrouterV1Worker
from .apis.taskrouter_v1_worker_channel import AsyncTaskrouterV1WorkerChannel
from .apis.taskrouter_v1_worker_reservation import AsyncTaskrouterV1WorkerReservation
from .apis.taskrouter_v1_worker_statistics import AsyncTaskrouterV1WorkerStatistics
from .apis.taskrouter_v1_workers_cumulative_statistics import AsyncTaskrouterV1WorkersCumulativeStatistics
from .apis.taskrouter_v1_workers_real_time_statistics import AsyncTaskrouterV1WorkersRealTimeStatistics
from .apis.taskrouter_v1_workers_statistics import AsyncTaskrouterV1WorkersStatistics
from .apis.taskrouter_v1_workflow import AsyncTaskrouterV1Workflow
from .apis.taskrouter_v1_workflow_cumulative_statistics import AsyncTaskrouterV1WorkflowCumulativeStatistics
from .apis.taskrouter_v1_workflow_real_time_statistics import AsyncTaskrouterV1WorkflowRealTimeStatistics
from .apis.taskrouter_v1_workflow_statistics import AsyncTaskrouterV1WorkflowStatistics
from .apis.taskrouter_v1_workspace_api import AsyncTaskrouterV1WorkspaceApi
from .apis.taskrouter_v1_workspace_cumulative_statistics import AsyncTaskrouterV1WorkspaceCumulativeStatistics
from .apis.taskrouter_v1_workspace_real_time_statistics import AsyncTaskrouterV1WorkspaceRealTimeStatistics
from .apis.taskrouter_v1_workspace_statistics import AsyncTaskrouterV1WorkspaceStatistics
from .apis.trusthub_v1_compliance_inquiries import AsyncTrusthubV1ComplianceInquiries
from .apis.trusthub_v1_compliance_registration_inquiries import AsyncTrusthubV1ComplianceRegistrationInquiries
from .apis.trusthub_v1_compliance_tollfree_inquiries import AsyncTrusthubV1ComplianceTollfreeInquiries
from .apis.trusthub_v1_customer_profiles import AsyncTrusthubV1CustomerProfiles
from .apis.trusthub_v1_customer_profiles_channel_endpoint_assignment import (
    AsyncTrusthubV1CustomerProfilesChannelEndpointAssignment,
)
from .apis.trusthub_v1_customer_profiles_entity_assignments import AsyncTrusthubV1CustomerProfilesEntityAssignments
from .apis.trusthub_v1_customer_profiles_evaluations import AsyncTrusthubV1CustomerProfilesEvaluations
from .apis.trusthub_v1_end_user_api import AsyncTrusthubV1EndUserApi
from .apis.trusthub_v1_end_user_type import AsyncTrusthubV1EndUserType
from .apis.trusthub_v1_policies_api import AsyncTrusthubV1PoliciesApi
from .apis.trusthub_v1_supporting_document_api import AsyncTrusthubV1SupportingDocumentApi
from .apis.trusthub_v1_supporting_document_type import AsyncTrusthubV1SupportingDocumentType
from .apis.trusthub_v1_trust_products import AsyncTrusthubV1TrustProducts
from .apis.trusthub_v1_trust_products_channel_endpoint_assignment import (
    AsyncTrusthubV1TrustProductsChannelEndpointAssignment,
)
from .apis.trusthub_v1_trust_products_entity_assignments import AsyncTrusthubV1TrustProductsEntityAssignments
from .apis.trusthub_v1_trust_products_evaluations import AsyncTrusthubV1TrustProductsEvaluations
from .apis.twilio_insights import AsyncTwilioInsights
from .apis.v2_short_code_applications import AsyncV2ShortCodeApplications
from .apis.verify_v2_access_token import AsyncVerifyV2AccessToken
from .apis.verify_v2_bucket import AsyncVerifyV2Bucket
from .apis.verify_v2_challenge import AsyncVerifyV2Challenge
from .apis.verify_v2_entity import AsyncVerifyV2Entity
from .apis.verify_v2_factor import AsyncVerifyV2Factor
from .apis.verify_v2_form_api import AsyncVerifyV2FormApi
from .apis.verify_v2_messaging_configuration import AsyncVerifyV2MessagingConfiguration
from .apis.verify_v2_new_challenge import AsyncVerifyV2NewChallenge
from .apis.verify_v2_new_factor import AsyncVerifyV2NewFactor
from .apis.verify_v2_notification import AsyncVerifyV2Notification
from .apis.verify_v2_rate_limit import AsyncVerifyV2RateLimit
from .apis.verify_v2_safelist_api import AsyncVerifyV2SafelistApi
from .apis.verify_v2_service_api import AsyncVerifyV2ServiceApi
from .apis.verify_v2_template import AsyncVerifyV2Template
from .apis.verify_v2_verification import AsyncVerifyV2Verification
from .apis.verify_v2_verification_attempt_api import AsyncVerifyV2VerificationAttemptApi
from .apis.verify_v2_verification_attempts_summary_api import AsyncVerifyV2VerificationAttemptsSummaryApi
from .apis.verify_v2_verification_check import AsyncVerifyV2VerificationCheck
from .apis.verify_v2_webhook import AsyncVerifyV2Webhook
from .apis.video_v1_anonymize import AsyncVideoV1Anonymize
from .apis.video_v1_composition_api import AsyncVideoV1CompositionApi
from .apis.video_v1_composition_hook_api import AsyncVideoV1CompositionHookApi
from .apis.video_v1_composition_settings_api import AsyncVideoV1CompositionSettingsApi
from .apis.video_v1_participant import AsyncVideoV1Participant
from .apis.video_v1_published_track import AsyncVideoV1PublishedTrack
from .apis.video_v1_recording_api import AsyncVideoV1RecordingApi
from .apis.video_v1_recording_rules import AsyncVideoV1RecordingRules
from .apis.video_v1_recording_settings_api import AsyncVideoV1RecordingSettingsApi
from .apis.video_v1_room_api import AsyncVideoV1RoomApi
from .apis.video_v1_room_recording import AsyncVideoV1RoomRecording
from .apis.video_v1_subscribe_rules import AsyncVideoV1SubscribeRules
from .apis.video_v1_subscribed_track import AsyncVideoV1SubscribedTrack
from .apis.video_v1_transcriptions import AsyncVideoV1Transcriptions
from .auth import AsyncAuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseTwilioSdkClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiResult,
    AsyncHttpClient,
    AsyncHttpxClient,
    AsyncRawClient,
    BasicAuthCredentials,
    BasicAuthCredentialsOrDict,
    BasicAuthScheme,
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


class AsyncTwilioSdkClient(BaseTwilioSdkClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        server_config: ServerConfigOrDict | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_async_http_client: AsyncHttpClient | None = None,
        account_sid_auth_token: BasicAuthCredentialsOrDict | None = None,
    ) -> None:
        super().__init__(server_config=server_config, timeout=timeout)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpxClient(timeout=timeout)
            ),
            global_headers=[
                param[str]("User-Agent", "TwilioSdkClient/1.0.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "1.0.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AsyncAuthSchemes(
            account_sid_auth_token=(
                BasicAuthScheme(BasicAuthCredentials.coerce(account_sid_auth_token))
                if account_sid_auth_token is not None
                else no_auth
            ),
        )

    @cached_property
    def api20100401_account(self) -> AsyncApi20100401Account:
        return AsyncApi20100401Account(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_add_on_result(self) -> AsyncApi20100401AddOnResult:
        return AsyncApi20100401AddOnResult(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_address(self) -> AsyncApi20100401Address:
        return AsyncApi20100401Address(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_all_time(self) -> AsyncApi20100401AllTime:
        return AsyncApi20100401AllTime(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_application(self) -> AsyncApi20100401Application:
        return AsyncApi20100401Application(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_assigned_add_on(self) -> AsyncApi20100401AssignedAddOn:
        return AsyncApi20100401AssignedAddOn(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_assigned_add_on_extension(self) -> AsyncApi20100401AssignedAddOnExtension:
        return AsyncApi20100401AssignedAddOnExtension(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_auth_calls_credential_list_mapping(self) -> AsyncApi20100401AuthCallsCredentialListMapping:
        return AsyncApi20100401AuthCallsCredentialListMapping(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_auth_calls_ip_access_control_list_mapping(
        self
    ) -> AsyncApi20100401AuthCallsIpAccessControlListMapping:
        return AsyncApi20100401AuthCallsIpAccessControlListMapping(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_auth_registrations_credential_list_mapping(
        self
    ) -> AsyncApi20100401AuthRegistrationsCredentialListMapping:
        return AsyncApi20100401AuthRegistrationsCredentialListMapping(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_authorized_connect_app(self) -> AsyncApi20100401AuthorizedConnectApp:
        return AsyncApi20100401AuthorizedConnectApp(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_available_phone_number_country(self) -> AsyncApi20100401AvailablePhoneNumberCountry:
        return AsyncApi20100401AvailablePhoneNumberCountry(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_balance(self) -> AsyncApi20100401Balance:
        return AsyncApi20100401Balance(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_call(self) -> AsyncApi20100401Call:
        return AsyncApi20100401Call(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_call_notification(self) -> AsyncApi20100401CallNotification:
        return AsyncApi20100401CallNotification(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_call_recording(self) -> AsyncApi20100401CallRecording:
        return AsyncApi20100401CallRecording(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_call_transcription(self) -> AsyncApi20100401CallTranscription:
        return AsyncApi20100401CallTranscription(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_conference(self) -> AsyncApi20100401Conference:
        return AsyncApi20100401Conference(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_conference_recording(self) -> AsyncApi20100401ConferenceRecording:
        return AsyncApi20100401ConferenceRecording(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_connect_app(self) -> AsyncApi20100401ConnectApp:
        return AsyncApi20100401ConnectApp(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_credential(self) -> AsyncApi20100401Credential:
        return AsyncApi20100401Credential(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_credential_list(self) -> AsyncApi20100401CredentialList:
        return AsyncApi20100401CredentialList(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_credential_list_mapping(self) -> AsyncApi20100401CredentialListMapping:
        return AsyncApi20100401CredentialListMapping(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_daily(self) -> AsyncApi20100401Daily:
        return AsyncApi20100401Daily(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_data(self) -> AsyncApi20100401Data:
        return AsyncApi20100401Data(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_dependent_phone_number(self) -> AsyncApi20100401DependentPhoneNumber:
        return AsyncApi20100401DependentPhoneNumber(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_domain(self) -> AsyncApi20100401Domain:
        return AsyncApi20100401Domain(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_event(self) -> AsyncApi20100401Event:
        return AsyncApi20100401Event(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_feedback(self) -> AsyncApi20100401Feedback:
        return AsyncApi20100401Feedback(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_incoming_phone_number(self) -> AsyncApi20100401IncomingPhoneNumber:
        return AsyncApi20100401IncomingPhoneNumber(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_incoming_phone_number_local(self) -> AsyncApi20100401IncomingPhoneNumberLocal:
        return AsyncApi20100401IncomingPhoneNumberLocal(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_incoming_phone_number_mobile(self) -> AsyncApi20100401IncomingPhoneNumberMobile:
        return AsyncApi20100401IncomingPhoneNumberMobile(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_incoming_phone_number_toll_free(self) -> AsyncApi20100401IncomingPhoneNumberTollFree:
        return AsyncApi20100401IncomingPhoneNumberTollFree(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_ip_access_control_list(self) -> AsyncApi20100401IpAccessControlList:
        return AsyncApi20100401IpAccessControlList(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_ip_access_control_list_mapping(self) -> AsyncApi20100401IpAccessControlListMapping:
        return AsyncApi20100401IpAccessControlListMapping(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_key(self) -> AsyncApi20100401Key:
        return AsyncApi20100401Key(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_last_month(self) -> AsyncApi20100401LastMonth:
        return AsyncApi20100401LastMonth(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_local(self) -> AsyncApi20100401Local:
        return AsyncApi20100401Local(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_machine_to_machine(self) -> AsyncApi20100401MachineToMachine:
        return AsyncApi20100401MachineToMachine(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_media(self) -> AsyncApi20100401Media:
        return AsyncApi20100401Media(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_media_instance(self) -> AsyncApi20100401MediaInstance:
        return AsyncApi20100401MediaInstance(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_member(self) -> AsyncApi20100401Member:
        return AsyncApi20100401Member(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_message(self) -> AsyncApi20100401Message:
        return AsyncApi20100401Message(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_mobile(self) -> AsyncApi20100401Mobile:
        return AsyncApi20100401Mobile(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_monthly(self) -> AsyncApi20100401Monthly:
        return AsyncApi20100401Monthly(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_national(self) -> AsyncApi20100401National:
        return AsyncApi20100401National(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_new_key(self) -> AsyncApi20100401NewKey:
        return AsyncApi20100401NewKey(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_new_signing_key(self) -> AsyncApi20100401NewSigningKey:
        return AsyncApi20100401NewSigningKey(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_notification(self) -> AsyncApi20100401Notification:
        return AsyncApi20100401Notification(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_outgoing_caller_id(self) -> AsyncApi20100401OutgoingCallerId:
        return AsyncApi20100401OutgoingCallerId(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_participant(self) -> AsyncApi20100401Participant:
        return AsyncApi20100401Participant(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_payload(self) -> AsyncApi20100401Payload:
        return AsyncApi20100401Payload(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_payment(self) -> AsyncApi20100401Payment:
        return AsyncApi20100401Payment(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_queue(self) -> AsyncApi20100401Queue:
        return AsyncApi20100401Queue(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_record(self) -> AsyncApi20100401Record:
        return AsyncApi20100401Record(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_recording(self) -> AsyncApi20100401Recording:
        return AsyncApi20100401Recording(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_recording_transcription(self) -> AsyncApi20100401RecordingTranscription:
        return AsyncApi20100401RecordingTranscription(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_shared_cost(self) -> AsyncApi20100401SharedCost:
        return AsyncApi20100401SharedCost(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_short_code(self) -> AsyncApi20100401ShortCode:
        return AsyncApi20100401ShortCode(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_signing_key(self) -> AsyncApi20100401SigningKey:
        return AsyncApi20100401SigningKey(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_sip_ip_address(self) -> AsyncApi20100401SipIpAddress:
        return AsyncApi20100401SipIpAddress(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_siprec(self) -> AsyncApi20100401Siprec:
        return AsyncApi20100401Siprec(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_stream(self) -> AsyncApi20100401Stream:
        return AsyncApi20100401Stream(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_this_month(self) -> AsyncApi20100401ThisMonth:
        return AsyncApi20100401ThisMonth(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_today(self) -> AsyncApi20100401Today:
        return AsyncApi20100401Today(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_token(self) -> AsyncApi20100401Token:
        return AsyncApi20100401Token(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_toll_free(self) -> AsyncApi20100401TollFree:
        return AsyncApi20100401TollFree(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_transcription(self) -> AsyncApi20100401Transcription:
        return AsyncApi20100401Transcription(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_trigger(self) -> AsyncApi20100401Trigger:
        return AsyncApi20100401Trigger(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_user_defined_message(self) -> AsyncApi20100401UserDefinedMessage:
        return AsyncApi20100401UserDefinedMessage(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_user_defined_message_subscription(self) -> AsyncApi20100401UserDefinedMessageSubscription:
        return AsyncApi20100401UserDefinedMessageSubscription(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_validation_request(self) -> AsyncApi20100401ValidationRequest:
        return AsyncApi20100401ValidationRequest(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_voip(self) -> AsyncApi20100401Voip:
        return AsyncApi20100401Voip(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_yearly(self) -> AsyncApi20100401Yearly:
        return AsyncApi20100401Yearly(self._raw_client, self._server, self._auth)

    @cached_property
    def api20100401_yesterday(self) -> AsyncApi20100401Yesterday:
        return AsyncApi20100401Yesterday(self._raw_client, self._server, self._auth)

    @cached_property
    def content_v2_content(self) -> AsyncContentV2Content:
        return AsyncContentV2Content(self._raw_client, self._server, self._auth)

    @cached_property
    def content_v2_content_and_approvals(self) -> AsyncContentV2ContentAndApprovals:
        return AsyncContentV2ContentAndApprovals(self._raw_client, self._server, self._auth)

    @cached_property
    def contentv1_approval_create(self) -> AsyncContentv1ApprovalCreate:
        return AsyncContentv1ApprovalCreate(self._raw_client, self._server, self._auth)

    @cached_property
    def contentv1_approval_fetch(self) -> AsyncContentv1ApprovalFetch:
        return AsyncContentv1ApprovalFetch(self._raw_client, self._server, self._auth)

    @cached_property
    def contentv1_content_api(self) -> AsyncContentv1ContentApi:
        return AsyncContentv1ContentApi(self._raw_client, self._server, self._auth)

    @cached_property
    def contentv1_content_and_approvals_api(self) -> AsyncContentv1ContentAndApprovalsApi:
        return AsyncContentv1ContentAndApprovalsApi(self._raw_client, self._server, self._auth)

    @cached_property
    def contentv1_legacy_content_api(self) -> AsyncContentv1LegacyContentApi:
        return AsyncContentv1LegacyContentApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_address_configuration(self) -> AsyncConversationsV1AddressConfiguration:
        return AsyncConversationsV1AddressConfiguration(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_binding(self) -> AsyncConversationsV1Binding:
        return AsyncConversationsV1Binding(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_configuration_api(self) -> AsyncConversationsV1ConfigurationApi:
        return AsyncConversationsV1ConfigurationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_conversation_api(self) -> AsyncConversationsV1ConversationApi:
        return AsyncConversationsV1ConversationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_conversation_with_participants_api(
        self
    ) -> AsyncConversationsV1ConversationWithParticipantsApi:
        return AsyncConversationsV1ConversationWithParticipantsApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_credential_api(self) -> AsyncConversationsV1CredentialApi:
        return AsyncConversationsV1CredentialApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_delivery_receipt(self) -> AsyncConversationsV1DeliveryReceipt:
        return AsyncConversationsV1DeliveryReceipt(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_message(self) -> AsyncConversationsV1Message:
        return AsyncConversationsV1Message(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_notification(self) -> AsyncConversationsV1Notification:
        return AsyncConversationsV1Notification(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_participant(self) -> AsyncConversationsV1Participant:
        return AsyncConversationsV1Participant(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_participant_conversation_api(self) -> AsyncConversationsV1ParticipantConversationApi:
        return AsyncConversationsV1ParticipantConversationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_role_api(self) -> AsyncConversationsV1RoleApi:
        return AsyncConversationsV1RoleApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_service_api(self) -> AsyncConversationsV1ServiceApi:
        return AsyncConversationsV1ServiceApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_user_api(self) -> AsyncConversationsV1UserApi:
        return AsyncConversationsV1UserApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_user_conversation(self) -> AsyncConversationsV1UserConversation:
        return AsyncConversationsV1UserConversation(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v1_webhook(self) -> AsyncConversationsV1Webhook:
        return AsyncConversationsV1Webhook(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v2_action_api(self) -> AsyncConversationsV2ActionApi:
        return AsyncConversationsV2ActionApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v2_communication_api(self) -> AsyncConversationsV2CommunicationApi:
        return AsyncConversationsV2CommunicationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v2_configuration_api(self) -> AsyncConversationsV2ConfigurationApi:
        return AsyncConversationsV2ConfigurationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v2_conversation_api(self) -> AsyncConversationsV2ConversationApi:
        return AsyncConversationsV2ConversationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v2_operation(self) -> AsyncConversationsV2Operation:
        return AsyncConversationsV2Operation(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations_v2_participant_api(self) -> AsyncConversationsV2ParticipantApi:
        return AsyncConversationsV2ParticipantApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_assessments(self) -> AsyncFlexV1Assessments:
        return AsyncFlexV1Assessments(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_channel_api(self) -> AsyncFlexV1ChannelApi:
        return AsyncFlexV1ChannelApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_configuration_api(self) -> AsyncFlexV1ConfigurationApi:
        return AsyncFlexV1ConfigurationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_configured_plugin(self) -> AsyncFlexV1ConfiguredPlugin:
        return AsyncFlexV1ConfiguredPlugin(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_flex_flow_api(self) -> AsyncFlexV1FlexFlowApi:
        return AsyncFlexV1FlexFlowApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_insights_assessments_comment_api(self) -> AsyncFlexV1InsightsAssessmentsCommentApi:
        return AsyncFlexV1InsightsAssessmentsCommentApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_insights_conversations_api(self) -> AsyncFlexV1InsightsConversationsApi:
        return AsyncFlexV1InsightsConversationsApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_insights_questionnaires_api(self) -> AsyncFlexV1InsightsQuestionnairesApi:
        return AsyncFlexV1InsightsQuestionnairesApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_insights_questionnaires_category_api(self) -> AsyncFlexV1InsightsQuestionnairesCategoryApi:
        return AsyncFlexV1InsightsQuestionnairesCategoryApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_insights_questionnaires_question_api(self) -> AsyncFlexV1InsightsQuestionnairesQuestionApi:
        return AsyncFlexV1InsightsQuestionnairesQuestionApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_insights_segments_api(self) -> AsyncFlexV1InsightsSegmentsApi:
        return AsyncFlexV1InsightsSegmentsApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_insights_session_api(self) -> AsyncFlexV1InsightsSessionApi:
        return AsyncFlexV1InsightsSessionApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_insights_settings_answer_sets_api(self) -> AsyncFlexV1InsightsSettingsAnswerSetsApi:
        return AsyncFlexV1InsightsSettingsAnswerSetsApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_insights_settings_comment_api(self) -> AsyncFlexV1InsightsSettingsCommentApi:
        return AsyncFlexV1InsightsSettingsCommentApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_insights_user_roles_api(self) -> AsyncFlexV1InsightsUserRolesApi:
        return AsyncFlexV1InsightsUserRolesApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_interaction_api(self) -> AsyncFlexV1InteractionApi:
        return AsyncFlexV1InteractionApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_interaction_channel(self) -> AsyncFlexV1InteractionChannel:
        return AsyncFlexV1InteractionChannel(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_interaction_channel_invite(self) -> AsyncFlexV1InteractionChannelInvite:
        return AsyncFlexV1InteractionChannelInvite(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_interaction_channel_participant(self) -> AsyncFlexV1InteractionChannelParticipant:
        return AsyncFlexV1InteractionChannelParticipant(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_interaction_transfer(self) -> AsyncFlexV1InteractionTransfer:
        return AsyncFlexV1InteractionTransfer(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_plugin_api(self) -> AsyncFlexV1PluginApi:
        return AsyncFlexV1PluginApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_plugin_archive_api(self) -> AsyncFlexV1PluginArchiveApi:
        return AsyncFlexV1PluginArchiveApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_plugin_configuration_api(self) -> AsyncFlexV1PluginConfigurationApi:
        return AsyncFlexV1PluginConfigurationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_plugin_configuration_archive_api(self) -> AsyncFlexV1PluginConfigurationArchiveApi:
        return AsyncFlexV1PluginConfigurationArchiveApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_plugin_release_api(self) -> AsyncFlexV1PluginReleaseApi:
        return AsyncFlexV1PluginReleaseApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_plugin_version_archive_api(self) -> AsyncFlexV1PluginVersionArchiveApi:
        return AsyncFlexV1PluginVersionArchiveApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_plugin_versions(self) -> AsyncFlexV1PluginVersions:
        return AsyncFlexV1PluginVersions(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_provisioning_status_api(self) -> AsyncFlexV1ProvisioningStatusApi:
        return AsyncFlexV1ProvisioningStatusApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v1_web_channel_api(self) -> AsyncFlexV1WebChannelApi:
        return AsyncFlexV1WebChannelApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v2_flex_user_api(self) -> AsyncFlexV2FlexUserApi:
        return AsyncFlexV2FlexUserApi(self._raw_client, self._server, self._auth)

    @cached_property
    def flex_v2_web_channels(self) -> AsyncFlexV2WebChannels:
        return AsyncFlexV2WebChannels(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_annotation(self) -> AsyncInsightsV1Annotation:
        return AsyncInsightsV1Annotation(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_call_api(self) -> AsyncInsightsV1CallApi:
        return AsyncInsightsV1CallApi(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_call_summaries_api(self) -> AsyncInsightsV1CallSummariesApi:
        return AsyncInsightsV1CallSummariesApi(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_call_summary_api(self) -> AsyncInsightsV1CallSummaryApi:
        return AsyncInsightsV1CallSummaryApi(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_conference_api(self) -> AsyncInsightsV1ConferenceApi:
        return AsyncInsightsV1ConferenceApi(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_conference_participant(self) -> AsyncInsightsV1ConferenceParticipant:
        return AsyncInsightsV1ConferenceParticipant(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_create_account_report(self) -> AsyncInsightsV1CreateAccountReport:
        return AsyncInsightsV1CreateAccountReport(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_create_inbound_phone_numbers_report(self) -> AsyncInsightsV1CreateInboundPhoneNumbersReport:
        return AsyncInsightsV1CreateInboundPhoneNumbersReport(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_create_outbound_phone_numbers_report(self) -> AsyncInsightsV1CreateOutboundPhoneNumbersReport:
        return AsyncInsightsV1CreateOutboundPhoneNumbersReport(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_event(self) -> AsyncInsightsV1Event:
        return AsyncInsightsV1Event(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_get_account_report(self) -> AsyncInsightsV1GetAccountReport:
        return AsyncInsightsV1GetAccountReport(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_get_inbound_phone_numbers_report(self) -> AsyncInsightsV1GetInboundPhoneNumbersReport:
        return AsyncInsightsV1GetInboundPhoneNumbersReport(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_get_outbound_phone_numbers_report(self) -> AsyncInsightsV1GetOutboundPhoneNumbersReport:
        return AsyncInsightsV1GetOutboundPhoneNumbersReport(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_metric(self) -> AsyncInsightsV1Metric:
        return AsyncInsightsV1Metric(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_participant(self) -> AsyncInsightsV1Participant:
        return AsyncInsightsV1Participant(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_room(self) -> AsyncInsightsV1Room:
        return AsyncInsightsV1Room(self._raw_client, self._server, self._auth)

    @cached_property
    def insights_v1_setting(self) -> AsyncInsightsV1Setting:
        return AsyncInsightsV1Setting(self._raw_client, self._server, self._auth)

    @cached_property
    def lookups_v1_phone_number_api(self) -> AsyncLookupsV1PhoneNumberApi:
        return AsyncLookupsV1PhoneNumberApi(self._raw_client, self._server, self._auth)

    @cached_property
    def lookups_v2_phone_number(self) -> AsyncLookupsV2PhoneNumber:
        return AsyncLookupsV2PhoneNumber(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_alpha_sender(self) -> AsyncMessagingV1AlphaSender:
        return AsyncMessagingV1AlphaSender(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_brand_registration(self) -> AsyncMessagingV1BrandRegistration:
        return AsyncMessagingV1BrandRegistration(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_brand_registration_otp(self) -> AsyncMessagingV1BrandRegistrationOtp:
        return AsyncMessagingV1BrandRegistrationOtp(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_brand_vetting(self) -> AsyncMessagingV1BrandVetting:
        return AsyncMessagingV1BrandVetting(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_channel_sender(self) -> AsyncMessagingV1ChannelSender:
        return AsyncMessagingV1ChannelSender(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_deactivations(self) -> AsyncMessagingV1Deactivations:
        return AsyncMessagingV1Deactivations(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_destination_alpha_sender(self) -> AsyncMessagingV1DestinationAlphaSender:
        return AsyncMessagingV1DestinationAlphaSender(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_domain_certs(self) -> AsyncMessagingV1DomainCerts:
        return AsyncMessagingV1DomainCerts(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_domain_config_api(self) -> AsyncMessagingV1DomainConfigApi:
        return AsyncMessagingV1DomainConfigApi(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_domain_config_messaging_service_api(self) -> AsyncMessagingV1DomainConfigMessagingServiceApi:
        return AsyncMessagingV1DomainConfigMessagingServiceApi(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_domain_validate_dns(self) -> AsyncMessagingV1DomainValidateDns:
        return AsyncMessagingV1DomainValidateDns(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_external_campaign_api(self) -> AsyncMessagingV1ExternalCampaignApi:
        return AsyncMessagingV1ExternalCampaignApi(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_linkshortening_messaging_service_api(self) -> AsyncMessagingV1LinkshorteningMessagingServiceApi:
        return AsyncMessagingV1LinkshorteningMessagingServiceApi(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_linkshortening_messaging_service_domain_association_api(
        self
    ) -> AsyncMessagingV1LinkshorteningMessagingServiceDomainAssociationApi:
        return AsyncMessagingV1LinkshorteningMessagingServiceDomainAssociationApi(
            self._raw_client, self._server, self._auth
        )

    @cached_property
    def messaging_v1_phone_number(self) -> AsyncMessagingV1PhoneNumber:
        return AsyncMessagingV1PhoneNumber(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_request_managed_cert_api(self) -> AsyncMessagingV1RequestManagedCertApi:
        return AsyncMessagingV1RequestManagedCertApi(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_service_api(self) -> AsyncMessagingV1ServiceApi:
        return AsyncMessagingV1ServiceApi(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_short_code(self) -> AsyncMessagingV1ShortCode:
        return AsyncMessagingV1ShortCode(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_tollfree_verification_api(self) -> AsyncMessagingV1TollfreeVerificationApi:
        return AsyncMessagingV1TollfreeVerificationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_us_app_to_person(self) -> AsyncMessagingV1UsAppToPerson:
        return AsyncMessagingV1UsAppToPerson(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_us_app_to_person_usecase(self) -> AsyncMessagingV1UsAppToPersonUsecase:
        return AsyncMessagingV1UsAppToPersonUsecase(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v1_usecase_api(self) -> AsyncMessagingV1UsecaseApi:
        return AsyncMessagingV1UsecaseApi(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v2_channels_sender(self) -> AsyncMessagingV2ChannelsSender:
        return AsyncMessagingV2ChannelsSender(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v2_domain_certs(self) -> AsyncMessagingV2DomainCerts:
        return AsyncMessagingV2DomainCerts(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v2_typing_indicator(self) -> AsyncMessagingV2TypingIndicator:
        return AsyncMessagingV2TypingIndicator(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging_v3_typing_indicator(self) -> AsyncMessagingV3TypingIndicator:
        return AsyncMessagingV3TypingIndicator(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v1_bulk_eligibility_api(self) -> AsyncNumbersV1BulkEligibilityApi:
        return AsyncNumbersV1BulkEligibilityApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v1_eligibility_api(self) -> AsyncNumbersV1EligibilityApi:
        return AsyncNumbersV1EligibilityApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v1_porting_port_in_api(self) -> AsyncNumbersV1PortingPortInApi:
        return AsyncNumbersV1PortingPortInApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v1_porting_port_in_phone_number_api(self) -> AsyncNumbersV1PortingPortInPhoneNumberApi:
        return AsyncNumbersV1PortingPortInPhoneNumberApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v1_porting_portability_api(self) -> AsyncNumbersV1PortingPortabilityApi:
        return AsyncNumbersV1PortingPortabilityApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v1_porting_webhook_configuration_api(self) -> AsyncNumbersV1PortingWebhookConfigurationApi:
        return AsyncNumbersV1PortingWebhookConfigurationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v1_porting_webhook_configuration_delete_api(self) -> AsyncNumbersV1PortingWebhookConfigurationDeleteApi:
        return AsyncNumbersV1PortingWebhookConfigurationDeleteApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v1_porting_webhook_configuration_fetch_api(self) -> AsyncNumbersV1PortingWebhookConfigurationFetchApi:
        return AsyncNumbersV1PortingWebhookConfigurationFetchApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v1_sender_id_registration(self) -> AsyncNumbersV1SenderIdRegistration:
        return AsyncNumbersV1SenderIdRegistration(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v1_sender_id_registration_embedded_session(self) -> AsyncNumbersV1SenderIdRegistrationEmbeddedSession:
        return AsyncNumbersV1SenderIdRegistrationEmbeddedSession(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v1_signing_request_configuration_api(self) -> AsyncNumbersV1SigningRequestConfigurationApi:
        return AsyncNumbersV1SigningRequestConfigurationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_authorization_document_api(self) -> AsyncNumbersV2AuthorizationDocumentApi:
        return AsyncNumbersV2AuthorizationDocumentApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_bulk_hosted_number_order_api(self) -> AsyncNumbersV2BulkHostedNumberOrderApi:
        return AsyncNumbersV2BulkHostedNumberOrderApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_bundle(self) -> AsyncNumbersV2Bundle:
        return AsyncNumbersV2Bundle(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_bundle_clone_api(self) -> AsyncNumbersV2BundleCloneApi:
        return AsyncNumbersV2BundleCloneApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_bundle_copy(self) -> AsyncNumbersV2BundleCopy:
        return AsyncNumbersV2BundleCopy(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_dependent_hosted_number_order(self) -> AsyncNumbersV2DependentHostedNumberOrder:
        return AsyncNumbersV2DependentHostedNumberOrder(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_end_user(self) -> AsyncNumbersV2EndUser:
        return AsyncNumbersV2EndUser(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_end_user_type(self) -> AsyncNumbersV2EndUserType:
        return AsyncNumbersV2EndUserType(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_evaluation(self) -> AsyncNumbersV2Evaluation:
        return AsyncNumbersV2Evaluation(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_hosted_number_order_api(self) -> AsyncNumbersV2HostedNumberOrderApi:
        return AsyncNumbersV2HostedNumberOrderApi(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_item_assignment(self) -> AsyncNumbersV2ItemAssignment:
        return AsyncNumbersV2ItemAssignment(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_regulation(self) -> AsyncNumbersV2Regulation:
        return AsyncNumbersV2Regulation(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_replace_items(self) -> AsyncNumbersV2ReplaceItems:
        return AsyncNumbersV2ReplaceItems(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_supporting_document(self) -> AsyncNumbersV2SupportingDocument:
        return AsyncNumbersV2SupportingDocument(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v2_supporting_document_type(self) -> AsyncNumbersV2SupportingDocumentType:
        return AsyncNumbersV2SupportingDocumentType(self._raw_client, self._server, self._auth)

    @cached_property
    def numbers_v3_hosted_numbers_hosted_number_order_api(self) -> AsyncNumbersV3HostedNumbersHostedNumberOrderApi:
        return AsyncNumbersV3HostedNumbersHostedNumberOrderApi(self._raw_client, self._server, self._auth)

    @cached_property
    def proxy_v1_interaction(self) -> AsyncProxyV1Interaction:
        return AsyncProxyV1Interaction(self._raw_client, self._server, self._auth)

    @cached_property
    def proxy_v1_message_interaction(self) -> AsyncProxyV1MessageInteraction:
        return AsyncProxyV1MessageInteraction(self._raw_client, self._server, self._auth)

    @cached_property
    def proxy_v1_participant(self) -> AsyncProxyV1Participant:
        return AsyncProxyV1Participant(self._raw_client, self._server, self._auth)

    @cached_property
    def proxy_v1_phone_number(self) -> AsyncProxyV1PhoneNumber:
        return AsyncProxyV1PhoneNumber(self._raw_client, self._server, self._auth)

    @cached_property
    def proxy_v1_service_api(self) -> AsyncProxyV1ServiceApi:
        return AsyncProxyV1ServiceApi(self._raw_client, self._server, self._auth)

    @cached_property
    def proxy_v1_session(self) -> AsyncProxyV1Session:
        return AsyncProxyV1Session(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v1_engagement(self) -> AsyncStudioV1Engagement:
        return AsyncStudioV1Engagement(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v1_engagement_context(self) -> AsyncStudioV1EngagementContext:
        return AsyncStudioV1EngagementContext(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v1_execution(self) -> AsyncStudioV1Execution:
        return AsyncStudioV1Execution(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v1_execution_context(self) -> AsyncStudioV1ExecutionContext:
        return AsyncStudioV1ExecutionContext(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v1_execution_step(self) -> AsyncStudioV1ExecutionStep:
        return AsyncStudioV1ExecutionStep(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v1_execution_step_context(self) -> AsyncStudioV1ExecutionStepContext:
        return AsyncStudioV1ExecutionStepContext(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v1_flow_api(self) -> AsyncStudioV1FlowApi:
        return AsyncStudioV1FlowApi(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v1_step(self) -> AsyncStudioV1Step:
        return AsyncStudioV1Step(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v1_step_context(self) -> AsyncStudioV1StepContext:
        return AsyncStudioV1StepContext(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v2_execution(self) -> AsyncStudioV2Execution:
        return AsyncStudioV2Execution(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v2_execution_context(self) -> AsyncStudioV2ExecutionContext:
        return AsyncStudioV2ExecutionContext(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v2_execution_step(self) -> AsyncStudioV2ExecutionStep:
        return AsyncStudioV2ExecutionStep(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v2_execution_step_context(self) -> AsyncStudioV2ExecutionStepContext:
        return AsyncStudioV2ExecutionStepContext(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v2_flow_api(self) -> AsyncStudioV2FlowApi:
        return AsyncStudioV2FlowApi(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v2_flow_revision(self) -> AsyncStudioV2FlowRevision:
        return AsyncStudioV2FlowRevision(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v2_flow_test_user_api(self) -> AsyncStudioV2FlowTestUserApi:
        return AsyncStudioV2FlowTestUserApi(self._raw_client, self._server, self._auth)

    @cached_property
    def studio_v2_flow_validate_api(self) -> AsyncStudioV2FlowValidateApi:
        return AsyncStudioV2FlowValidateApi(self._raw_client, self._server, self._auth)

    @cached_property
    def sync_v1_document(self) -> AsyncSyncV1Document:
        return AsyncSyncV1Document(self._raw_client, self._server, self._auth)

    @cached_property
    def sync_v1_document_permission(self) -> AsyncSyncV1DocumentPermission:
        return AsyncSyncV1DocumentPermission(self._raw_client, self._server, self._auth)

    @cached_property
    def sync_v1_service_api(self) -> AsyncSyncV1ServiceApi:
        return AsyncSyncV1ServiceApi(self._raw_client, self._server, self._auth)

    @cached_property
    def sync_v1_stream_message(self) -> AsyncSyncV1StreamMessage:
        return AsyncSyncV1StreamMessage(self._raw_client, self._server, self._auth)

    @cached_property
    def sync_v1_sync_list(self) -> AsyncSyncV1SyncList:
        return AsyncSyncV1SyncList(self._raw_client, self._server, self._auth)

    @cached_property
    def sync_v1_sync_list_item(self) -> AsyncSyncV1SyncListItem:
        return AsyncSyncV1SyncListItem(self._raw_client, self._server, self._auth)

    @cached_property
    def sync_v1_sync_list_permission(self) -> AsyncSyncV1SyncListPermission:
        return AsyncSyncV1SyncListPermission(self._raw_client, self._server, self._auth)

    @cached_property
    def sync_v1_sync_map(self) -> AsyncSyncV1SyncMap:
        return AsyncSyncV1SyncMap(self._raw_client, self._server, self._auth)

    @cached_property
    def sync_v1_sync_map_item(self) -> AsyncSyncV1SyncMapItem:
        return AsyncSyncV1SyncMapItem(self._raw_client, self._server, self._auth)

    @cached_property
    def sync_v1_sync_map_permission(self) -> AsyncSyncV1SyncMapPermission:
        return AsyncSyncV1SyncMapPermission(self._raw_client, self._server, self._auth)

    @cached_property
    def sync_v1_sync_stream(self) -> AsyncSyncV1SyncStream:
        return AsyncSyncV1SyncStream(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_activity(self) -> AsyncTaskrouterV1Activity:
        return AsyncTaskrouterV1Activity(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_event(self) -> AsyncTaskrouterV1Event:
        return AsyncTaskrouterV1Event(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_task(self) -> AsyncTaskrouterV1Task:
        return AsyncTaskrouterV1Task(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_task_channel(self) -> AsyncTaskrouterV1TaskChannel:
        return AsyncTaskrouterV1TaskChannel(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_task_queue(self) -> AsyncTaskrouterV1TaskQueue:
        return AsyncTaskrouterV1TaskQueue(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_task_queue_bulk_real_time_statistics(self) -> AsyncTaskrouterV1TaskQueueBulkRealTimeStatistics:
        return AsyncTaskrouterV1TaskQueueBulkRealTimeStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_task_queue_cumulative_statistics(self) -> AsyncTaskrouterV1TaskQueueCumulativeStatistics:
        return AsyncTaskrouterV1TaskQueueCumulativeStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_task_queue_real_time_statistics(self) -> AsyncTaskrouterV1TaskQueueRealTimeStatistics:
        return AsyncTaskrouterV1TaskQueueRealTimeStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_task_queue_statistics(self) -> AsyncTaskrouterV1TaskQueueStatistics:
        return AsyncTaskrouterV1TaskQueueStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_task_queues_statistics(self) -> AsyncTaskrouterV1TaskQueuesStatistics:
        return AsyncTaskrouterV1TaskQueuesStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_task_reservation(self) -> AsyncTaskrouterV1TaskReservation:
        return AsyncTaskrouterV1TaskReservation(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_worker(self) -> AsyncTaskrouterV1Worker:
        return AsyncTaskrouterV1Worker(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_worker_channel(self) -> AsyncTaskrouterV1WorkerChannel:
        return AsyncTaskrouterV1WorkerChannel(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_worker_reservation(self) -> AsyncTaskrouterV1WorkerReservation:
        return AsyncTaskrouterV1WorkerReservation(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_worker_statistics(self) -> AsyncTaskrouterV1WorkerStatistics:
        return AsyncTaskrouterV1WorkerStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_workers_cumulative_statistics(self) -> AsyncTaskrouterV1WorkersCumulativeStatistics:
        return AsyncTaskrouterV1WorkersCumulativeStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_workers_real_time_statistics(self) -> AsyncTaskrouterV1WorkersRealTimeStatistics:
        return AsyncTaskrouterV1WorkersRealTimeStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_workers_statistics(self) -> AsyncTaskrouterV1WorkersStatistics:
        return AsyncTaskrouterV1WorkersStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_workflow(self) -> AsyncTaskrouterV1Workflow:
        return AsyncTaskrouterV1Workflow(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_workflow_cumulative_statistics(self) -> AsyncTaskrouterV1WorkflowCumulativeStatistics:
        return AsyncTaskrouterV1WorkflowCumulativeStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_workflow_real_time_statistics(self) -> AsyncTaskrouterV1WorkflowRealTimeStatistics:
        return AsyncTaskrouterV1WorkflowRealTimeStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_workflow_statistics(self) -> AsyncTaskrouterV1WorkflowStatistics:
        return AsyncTaskrouterV1WorkflowStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_workspace_api(self) -> AsyncTaskrouterV1WorkspaceApi:
        return AsyncTaskrouterV1WorkspaceApi(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_workspace_cumulative_statistics(self) -> AsyncTaskrouterV1WorkspaceCumulativeStatistics:
        return AsyncTaskrouterV1WorkspaceCumulativeStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_workspace_real_time_statistics(self) -> AsyncTaskrouterV1WorkspaceRealTimeStatistics:
        return AsyncTaskrouterV1WorkspaceRealTimeStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def taskrouter_v1_workspace_statistics(self) -> AsyncTaskrouterV1WorkspaceStatistics:
        return AsyncTaskrouterV1WorkspaceStatistics(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_compliance_inquiries(self) -> AsyncTrusthubV1ComplianceInquiries:
        return AsyncTrusthubV1ComplianceInquiries(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_compliance_registration_inquiries(self) -> AsyncTrusthubV1ComplianceRegistrationInquiries:
        return AsyncTrusthubV1ComplianceRegistrationInquiries(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_compliance_tollfree_inquiries(self) -> AsyncTrusthubV1ComplianceTollfreeInquiries:
        return AsyncTrusthubV1ComplianceTollfreeInquiries(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_customer_profiles(self) -> AsyncTrusthubV1CustomerProfiles:
        return AsyncTrusthubV1CustomerProfiles(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_customer_profiles_channel_endpoint_assignment(
        self
    ) -> AsyncTrusthubV1CustomerProfilesChannelEndpointAssignment:
        return AsyncTrusthubV1CustomerProfilesChannelEndpointAssignment(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_customer_profiles_entity_assignments(self) -> AsyncTrusthubV1CustomerProfilesEntityAssignments:
        return AsyncTrusthubV1CustomerProfilesEntityAssignments(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_customer_profiles_evaluations(self) -> AsyncTrusthubV1CustomerProfilesEvaluations:
        return AsyncTrusthubV1CustomerProfilesEvaluations(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_end_user_api(self) -> AsyncTrusthubV1EndUserApi:
        return AsyncTrusthubV1EndUserApi(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_end_user_type(self) -> AsyncTrusthubV1EndUserType:
        return AsyncTrusthubV1EndUserType(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_policies_api(self) -> AsyncTrusthubV1PoliciesApi:
        return AsyncTrusthubV1PoliciesApi(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_supporting_document_api(self) -> AsyncTrusthubV1SupportingDocumentApi:
        return AsyncTrusthubV1SupportingDocumentApi(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_supporting_document_type(self) -> AsyncTrusthubV1SupportingDocumentType:
        return AsyncTrusthubV1SupportingDocumentType(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_trust_products(self) -> AsyncTrusthubV1TrustProducts:
        return AsyncTrusthubV1TrustProducts(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_trust_products_channel_endpoint_assignment(
        self
    ) -> AsyncTrusthubV1TrustProductsChannelEndpointAssignment:
        return AsyncTrusthubV1TrustProductsChannelEndpointAssignment(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_trust_products_entity_assignments(self) -> AsyncTrusthubV1TrustProductsEntityAssignments:
        return AsyncTrusthubV1TrustProductsEntityAssignments(self._raw_client, self._server, self._auth)

    @cached_property
    def trusthub_v1_trust_products_evaluations(self) -> AsyncTrusthubV1TrustProductsEvaluations:
        return AsyncTrusthubV1TrustProductsEvaluations(self._raw_client, self._server, self._auth)

    @cached_property
    def twilio_insights(self) -> AsyncTwilioInsights:
        return AsyncTwilioInsights(self._raw_client, self._server, self._auth)

    @cached_property
    def v2_short_code_applications(self) -> AsyncV2ShortCodeApplications:
        return AsyncV2ShortCodeApplications(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_access_token(self) -> AsyncVerifyV2AccessToken:
        return AsyncVerifyV2AccessToken(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_bucket(self) -> AsyncVerifyV2Bucket:
        return AsyncVerifyV2Bucket(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_challenge(self) -> AsyncVerifyV2Challenge:
        return AsyncVerifyV2Challenge(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_entity(self) -> AsyncVerifyV2Entity:
        return AsyncVerifyV2Entity(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_factor(self) -> AsyncVerifyV2Factor:
        return AsyncVerifyV2Factor(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_form_api(self) -> AsyncVerifyV2FormApi:
        return AsyncVerifyV2FormApi(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_messaging_configuration(self) -> AsyncVerifyV2MessagingConfiguration:
        return AsyncVerifyV2MessagingConfiguration(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_new_challenge(self) -> AsyncVerifyV2NewChallenge:
        return AsyncVerifyV2NewChallenge(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_new_factor(self) -> AsyncVerifyV2NewFactor:
        return AsyncVerifyV2NewFactor(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_notification(self) -> AsyncVerifyV2Notification:
        return AsyncVerifyV2Notification(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_rate_limit(self) -> AsyncVerifyV2RateLimit:
        return AsyncVerifyV2RateLimit(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_safelist_api(self) -> AsyncVerifyV2SafelistApi:
        return AsyncVerifyV2SafelistApi(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_service_api(self) -> AsyncVerifyV2ServiceApi:
        return AsyncVerifyV2ServiceApi(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_template(self) -> AsyncVerifyV2Template:
        return AsyncVerifyV2Template(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_verification(self) -> AsyncVerifyV2Verification:
        return AsyncVerifyV2Verification(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_verification_attempt_api(self) -> AsyncVerifyV2VerificationAttemptApi:
        return AsyncVerifyV2VerificationAttemptApi(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_verification_attempts_summary_api(self) -> AsyncVerifyV2VerificationAttemptsSummaryApi:
        return AsyncVerifyV2VerificationAttemptsSummaryApi(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_verification_check(self) -> AsyncVerifyV2VerificationCheck:
        return AsyncVerifyV2VerificationCheck(self._raw_client, self._server, self._auth)

    @cached_property
    def verify_v2_webhook(self) -> AsyncVerifyV2Webhook:
        return AsyncVerifyV2Webhook(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_anonymize(self) -> AsyncVideoV1Anonymize:
        return AsyncVideoV1Anonymize(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_composition_api(self) -> AsyncVideoV1CompositionApi:
        return AsyncVideoV1CompositionApi(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_composition_hook_api(self) -> AsyncVideoV1CompositionHookApi:
        return AsyncVideoV1CompositionHookApi(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_composition_settings_api(self) -> AsyncVideoV1CompositionSettingsApi:
        return AsyncVideoV1CompositionSettingsApi(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_participant(self) -> AsyncVideoV1Participant:
        return AsyncVideoV1Participant(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_published_track(self) -> AsyncVideoV1PublishedTrack:
        return AsyncVideoV1PublishedTrack(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_recording_api(self) -> AsyncVideoV1RecordingApi:
        return AsyncVideoV1RecordingApi(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_recording_rules(self) -> AsyncVideoV1RecordingRules:
        return AsyncVideoV1RecordingRules(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_recording_settings_api(self) -> AsyncVideoV1RecordingSettingsApi:
        return AsyncVideoV1RecordingSettingsApi(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_room_api(self) -> AsyncVideoV1RoomApi:
        return AsyncVideoV1RoomApi(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_room_recording(self) -> AsyncVideoV1RoomRecording:
        return AsyncVideoV1RoomRecording(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_subscribe_rules(self) -> AsyncVideoV1SubscribeRules:
        return AsyncVideoV1SubscribeRules(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_subscribed_track(self) -> AsyncVideoV1SubscribedTrack:
        return AsyncVideoV1SubscribedTrack(self._raw_client, self._server, self._auth)

    @cached_property
    def video_v1_transcriptions(self) -> AsyncVideoV1Transcriptions:
        return AsyncVideoV1Transcriptions(self._raw_client, self._server, self._auth)

    @cached_property
    def with_raw_response(self) -> AsyncApiWithRawResponse:
        return AsyncApiWithRawResponse(self._raw_client, self._server, self._auth)

    async def create_bulk_lookup(
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
        return (await self.with_raw_response.create_bulk_lookup(body=body, request_options=request_options)).unwrap()

    async def create_lookup_phone_number_overrides(
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
        return (
            await self.with_raw_response.create_lookup_phone_number_overrides(
                field, phone_number, body=body, request_options=request_options
            )
        ).unwrap()

    async def delete_lookup_phone_number_overrides(
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
        return (
            await self.with_raw_response.delete_lookup_phone_number_overrides(
                field, phone_number, request_options=request_options
            )
        ).unwrap()

    async def delete_lookup_rate_limit(
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
        return (
            await self.with_raw_response.delete_lookup_rate_limit(field, bucket, request_options=request_options)
        ).unwrap()

    async def fetch_lookup_account_rate_limits(
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
        return (
            await self.with_raw_response.fetch_lookup_account_rate_limits(
                fields=fields, request_options=request_options
            )
        ).unwrap()

    async def fetch_lookup_phone_number_overrides(
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
        return (
            await self.with_raw_response.fetch_lookup_phone_number_overrides(
                field, phone_number, request_options=request_options
            )
        ).unwrap()

    async def fetch_lookup_rate_limit(
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
        return (
            await self.with_raw_response.fetch_lookup_rate_limit(field, bucket, request_options=request_options)
        ).unwrap()

    async def update_challenge_passkeys(
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
        return (
            await self.with_raw_response.update_challenge_passkeys(service_sid, body, request_options=request_options)
        ).unwrap()

    async def update_lookup_phone_number_overrides(
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
        return (
            await self.with_raw_response.update_lookup_phone_number_overrides(
                field, phone_number, body=body, request_options=request_options
            )
        ).unwrap()

    async def update_lookup_rate_limit(
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
        return (
            await self.with_raw_response.update_lookup_rate_limit(
                field, bucket, body=body, request_options=request_options
            )
        ).unwrap()

    async def update_passkeys_factor(
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
        return (
            await self.with_raw_response.update_passkeys_factor(service_sid, body, request_options=request_options)
        ).unwrap()

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


class AsyncApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_bulk_lookup(
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
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default4("/v2/batch/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LookupRequest | LookupRequestDict | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[LookupResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_lookup_phone_number_overrides(
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
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default4("/v2/PhoneNumbers/{PhoneNumber}/Overrides/{Field}"),
            path_params=[param[str]("Field", field), param[str]("PhoneNumber", phone_number)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OverridesRequest | OverridesRequestDict | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[OverridesResponse],
            error_mapper=create_lookup_phone_number_overrides_error_mapper,
            request_options=request_options,
        )

    async def delete_lookup_phone_number_overrides(
        self, field: str, phone_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteLookupPhoneNumberOverridesErrorBody]:
        """Delete an Override for a specific package and phone number.

        Args:
            field: Value sent with the request.
            phone_number: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default4("/v2/PhoneNumbers/{PhoneNumber}/Overrides/{Field}"),
            path_params=[param[str]("Field", field), param[str]("PhoneNumber", phone_number)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=delete_lookup_phone_number_overrides_error_mapper,
            request_options=request_options,
        )

    async def delete_lookup_rate_limit(
        self, field: str, bucket: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteLookupRateLimitErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            field: bucket name
            bucket: bucket name
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default4("/v2/RateLimits/Fields/{Field}/Bucket/{Bucket}"),
            path_params=[param[str]("Field", field), param[str]("Bucket", bucket)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=delete_lookup_rate_limit_error_mapper,
            request_options=request_options,
        )

    async def fetch_lookup_account_rate_limits(
        self, *, fields: list[str] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RateLimitListResponse, FetchLookupAccountRateLimitsErrorBody]:
        """Retrieve the list of rate limits for all fields (if any) It returns also the twilio rate limits.

        Args:
            fields: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default4("/v2/RateLimits"),
            query_params=[param[list[str] | None]("Fields", fields)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[RateLimitListResponse],
            error_mapper=fetch_lookup_account_rate_limits_error_mapper,
            request_options=request_options,
        )

    async def fetch_lookup_phone_number_overrides(
        self, field: str, phone_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OverridesResponse, FetchLookupPhoneNumberOverridesErrorBody]:
        """Retrieve an Override for a specific package and phone number.

        Args:
            field: Value sent with the request.
            phone_number: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default4("/v2/PhoneNumbers/{PhoneNumber}/Overrides/{Field}"),
            path_params=[param[str]("Field", field), param[str]("PhoneNumber", phone_number)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[OverridesResponse],
            error_mapper=fetch_lookup_phone_number_overrides_error_mapper,
            request_options=request_options,
        )

    async def fetch_lookup_rate_limit(
        self, field: str, bucket: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RateLimitResponse, FetchLookupRateLimitErrorBody]:
        """Send a ``GET`` request.

        Args:
            field: bucket name
            bucket: bucket name
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default4("/v2/RateLimits/Fields/{Field}/Bucket/{Bucket}"),
            path_params=[param[str]("Field", field), param[str]("Bucket", bucket)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[RateLimitResponse],
            error_mapper=fetch_lookup_rate_limit_error_mapper,
            request_options=request_options,
        )

    async def update_challenge_passkeys(
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
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/Passkeys/ApproveChallenge"),
            path_params=[param[str]("ServiceSid", service_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ApprovePasskeysChallengeRequest | ApprovePasskeysChallengeRequestDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[V2ServicesPasskeysApproveChallengeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_lookup_phone_number_overrides(
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
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default4("/v2/PhoneNumbers/{PhoneNumber}/Overrides/{Field}"),
            path_params=[param[str]("Field", field), param[str]("PhoneNumber", phone_number)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OverridesRequest | OverridesRequestDict | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[OverridesResponse],
            error_mapper=update_lookup_phone_number_overrides_error_mapper,
            request_options=request_options,
        )

    async def update_lookup_rate_limit(
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
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default4("/v2/RateLimits/Fields/{Field}/Bucket/{Bucket}"),
            path_params=[param[str]("Field", field), param[str]("Bucket", bucket)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RateLimitRequest | RateLimitRequestDict | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[RateLimitResponse],
            error_mapper=update_lookup_rate_limit_error_mapper,
            request_options=request_options,
        )

    async def update_passkeys_factor(
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
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/v2/Services/{ServiceSid}/Passkeys/VerifyFactor"),
            path_params=[param[str]("ServiceSid", service_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VerifyPasskeysFactorRequest | VerifyPasskeysFactorRequestDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[V2ServicesPasskeysVerifyFactorResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


AsyncClient = AsyncTwilioSdkClient
