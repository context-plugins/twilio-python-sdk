from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.enums.call_summaries_enum_answered_by import CallSummariesEnumAnsweredByOrStr
from ..models.enums.call_summaries_enum_processing_state_request import CallSummariesEnumProcessingStateRequestOrStr
from ..models.enums.call_summaries_enum_sort_by import CallSummariesEnumSortByOrStr
from ..models.list_call_summaries_response import ListCallSummariesResponse
from ..server.server import Server


class InsightsV1CallSummariesApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InsightsV1CallSummariesApiWithRawResponse(client, server, auth)

    def list_call_summaries(
        self,
        *,
        from_: str | None = None,
        to: str | None = None,
        from_carrier: str | None = None,
        to_carrier: str | None = None,
        from_country_code: str | None = None,
        to_country_code: str | None = None,
        verified_caller: bool | None = None,
        has_tag: bool | None = None,
        start_time: str | None = None,
        end_time: str | None = None,
        call_type: str | None = None,
        call_state: str | None = None,
        direction: str | None = None,
        processing_state: CallSummariesEnumProcessingStateRequestOrStr | None = None,
        sort_by: CallSummariesEnumSortByOrStr | None = None,
        subaccount: str | None = None,
        abnormal_session: bool | None = None,
        answered_by: CallSummariesEnumAnsweredByOrStr | None = None,
        answered_by_annotation: str | None = None,
        connectivity_issue_annotation: str | None = None,
        quality_issue_annotation: str | None = None,
        spam_annotation: bool | None = None,
        call_score_annotation: str | None = None,
        branded_enabled: bool | None = None,
        voice_integrity_enabled: bool | None = None,
        branded_bundle_sid: str | None = None,
        branded_logo: bool | None = None,
        branded_type: str | None = None,
        branded_use_case: str | None = None,
        branded_call_reason: str | None = None,
        voice_integrity_bundle_sid: str | None = None,
        voice_integrity_use_case: str | None = None,
        business_profile_identity: str | None = None,
        business_profile_industry: str | None = None,
        business_profile_bundle_sid: str | None = None,
        business_profile_type: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCallSummariesResponse:
        """Get a list of Call Summaries.

        Args:
            from_: A calling party. Could be an E.164 number, a SIP URI, or a Twilio Client registered name.
            to: A called party. Could be an E.164 number, a SIP URI, or a Twilio Client registered name.
            from_carrier: An origination carrier.
            to_carrier: A destination carrier.
            from_country_code: A source country code based on phone number in From.
            to_country_code: A destination country code. Based on phone number in To.
            verified_caller: A boolean flag indicating whether or not the caller was verified using SHAKEN/STIR.One of
                'true' or 'false'.
            has_tag: A boolean flag indicating the presence of one or more `Voice Insights Call Tags
                <https://www.twilio.com/docs/voice/voice-insights/api/call/details-call-tags>`__.
            start_time: A Start time of the calls. xm (x minutes), xh (x hours), xd (x days), 1w, 30m, 3d, 4w or
                datetime-ISO. Defaults to 4h.
            end_time: An End Time of the calls. xm (x minutes), xh (x hours), xd (x days), 1w, 30m, 3d, 4w or
                datetime-ISO. Defaults to 0m.
            call_type: A Call Type of the calls. One of ``carrier``, ``sip``, ``trunking`` or ``client``.
            call_state: A Call State of the calls. One of ``ringing``, ``completed``, ``busy``, ``fail``, ``noanswer``,
                ``canceled``, ``answered``, ``undialed``.
            direction: A Direction of the calls. One of ``outbound_api``, ``outbound_dial``, ``inbound``,
                ``trunking_originating``, ``trunking_terminating``.
            processing_state: A Processing State of the Call Summaries. One of ``completed``, ``partial`` or ``all``.
            sort_by: A Sort By criterion for the returned list of Call Summaries. One of ``start_time`` or ``end_time``.
            subaccount: A unique SID identifier of a Subaccount.
            abnormal_session: A boolean flag indicating an abnormal session where the last SIP response was not 200 OK.
            answered_by: An Answered By value for the calls based on ``Answering Machine Detection (AMD)``. One of
                ``unknown``, ``machine_start``, ``machine_end_beep``, ``machine_end_silence``, ``machine_end_other``,
                ``human`` or ``fax``.
            answered_by_annotation: Either machine or human.
            connectivity_issue_annotation: A Connectivity Issue with the calls. One of ``no_connectivity_issue``,
                ``invalid_number``, ``caller_id``, ``dropped_call``, or ``number_reachability``.
            quality_issue_annotation: A subjective Quality Issue with the calls. One of ``no_quality_issue``,
                ``low_volume``, ``choppy_robotic``, ``echo``, ``dtmf``, ``latency``, ``owa``, ``static_noise``.
            spam_annotation: A boolean flag indicating spam calls.
            call_score_annotation: A Call Score of the calls. Use a range of 1-5 to indicate the call experience score,
                with the following mapping as a reference for the rated call [5: Excellent, 4: Good, 3 : Fair, 2 : Poor,
                1: Bad].
            branded_enabled: A boolean flag indicating whether or not the calls were branded using Twilio Branded Calls.
                One of 'true' or 'false'
            voice_integrity_enabled: A boolean flag indicating whether or not the phone number had voice integrity
                enabled.One of 'true' or 'false'
            branded_bundle_sid: A unique SID identifier of the Branded Call.
            branded_logo: Indicates whether the branded logo was displayed during the in_brand branded call. Possible
                values are true (logo was present) or false (logo was not present).
            branded_type: Indicates whether the Branded Call is in_band vs out_of_band.
            branded_use_case: Specifies the user-defined purpose for the call, as provided during the setup of in_band
                branded calling.
            branded_call_reason: Specifies the user-defined reason for the call, which will be displayed to the end user
                on their mobile device during an in_band branded call.
            voice_integrity_bundle_sid: A unique SID identifier of the Voice Integrity Profile.
            voice_integrity_use_case: A Voice Integrity Use Case . Is of type enum. One of 'abandoned_cart',
                'appointment_reminders', 'appointment_scheduling', 'asset_management', 'automated_support',
                'call_tracking', 'click_to_call', 'contact_tracing', 'contactless_delivery', 'customer_support',
                'dating/social', 'delivery_notifications', 'distance_learning', 'emergency_notifications',
                'employee_notifications', 'exam_proctoring', 'field_notifications', 'first_responder', 'fraud_alerts',
                'group_messaging', 'identify_&_verification', 'intelligent_routing', 'lead_alerts', 'lead_distribution',
                'lead_generation', 'lead_management', 'lead_nurturing', 'marketing_events', 'mass_alerts',
                'meetings/collaboration', 'order_notifications', 'outbound_dialer', 'pharmacy', 'phone_system',
                'purchase_confirmation', 'remote_appointments', 'rewards_program', 'self-service', 'service_alerts',
                'shift_management', 'survey/research', 'telehealth', 'telemarketing', 'therapy_(individual+group)'.
            business_profile_identity: A Business Identity of the calls. Is of type enum. One of 'direct_customer',
                'isv_reseller_or_partner'.
            business_profile_industry: A Business Industry of the calls. Is of type enum. One of 'automotive',
                'agriculture', 'banking', 'consumer', 'construction', 'education', 'engineering', 'energy',
                'oil_and_gas', 'fast_moving_consumer_goods', 'financial', 'fintech', 'food_and_beverage', 'government',
                'healthcare', 'hospitality', 'insurance', 'legal', 'manufacturing', 'media', 'online',
                'professional_services', 'raw_materials', 'real_estate', 'religion', 'retail', 'jewelry', 'technology',
                'telecommunications', 'transportation', 'travel', 'electronics', 'not_for_profit'
            business_profile_bundle_sid: A unique SID identifier of the Business Profile.
            business_profile_type: A Business Profile Type of the calls. Is of type enum. One of 'primary', 'secondary'.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_call_summaries(
            from_=from_,
            to=to,
            from_carrier=from_carrier,
            to_carrier=to_carrier,
            from_country_code=from_country_code,
            to_country_code=to_country_code,
            verified_caller=verified_caller,
            has_tag=has_tag,
            start_time=start_time,
            end_time=end_time,
            call_type=call_type,
            call_state=call_state,
            direction=direction,
            processing_state=processing_state,
            sort_by=sort_by,
            subaccount=subaccount,
            abnormal_session=abnormal_session,
            answered_by=answered_by,
            answered_by_annotation=answered_by_annotation,
            connectivity_issue_annotation=connectivity_issue_annotation,
            quality_issue_annotation=quality_issue_annotation,
            spam_annotation=spam_annotation,
            call_score_annotation=call_score_annotation,
            branded_enabled=branded_enabled,
            voice_integrity_enabled=voice_integrity_enabled,
            branded_bundle_sid=branded_bundle_sid,
            branded_logo=branded_logo,
            branded_type=branded_type,
            branded_use_case=branded_use_case,
            branded_call_reason=branded_call_reason,
            voice_integrity_bundle_sid=voice_integrity_bundle_sid,
            voice_integrity_use_case=voice_integrity_use_case,
            business_profile_identity=business_profile_identity,
            business_profile_industry=business_profile_industry,
            business_profile_bundle_sid=business_profile_bundle_sid,
            business_profile_type=business_profile_type,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> InsightsV1CallSummariesApiWithRawResponse:
        return self._with_raw_response


class AsyncInsightsV1CallSummariesApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInsightsV1CallSummariesApiWithRawResponse(client, server, auth)

    async def list_call_summaries(
        self,
        *,
        from_: str | None = None,
        to: str | None = None,
        from_carrier: str | None = None,
        to_carrier: str | None = None,
        from_country_code: str | None = None,
        to_country_code: str | None = None,
        verified_caller: bool | None = None,
        has_tag: bool | None = None,
        start_time: str | None = None,
        end_time: str | None = None,
        call_type: str | None = None,
        call_state: str | None = None,
        direction: str | None = None,
        processing_state: CallSummariesEnumProcessingStateRequestOrStr | None = None,
        sort_by: CallSummariesEnumSortByOrStr | None = None,
        subaccount: str | None = None,
        abnormal_session: bool | None = None,
        answered_by: CallSummariesEnumAnsweredByOrStr | None = None,
        answered_by_annotation: str | None = None,
        connectivity_issue_annotation: str | None = None,
        quality_issue_annotation: str | None = None,
        spam_annotation: bool | None = None,
        call_score_annotation: str | None = None,
        branded_enabled: bool | None = None,
        voice_integrity_enabled: bool | None = None,
        branded_bundle_sid: str | None = None,
        branded_logo: bool | None = None,
        branded_type: str | None = None,
        branded_use_case: str | None = None,
        branded_call_reason: str | None = None,
        voice_integrity_bundle_sid: str | None = None,
        voice_integrity_use_case: str | None = None,
        business_profile_identity: str | None = None,
        business_profile_industry: str | None = None,
        business_profile_bundle_sid: str | None = None,
        business_profile_type: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCallSummariesResponse:
        """Get a list of Call Summaries.

        Args:
            from_: A calling party. Could be an E.164 number, a SIP URI, or a Twilio Client registered name.
            to: A called party. Could be an E.164 number, a SIP URI, or a Twilio Client registered name.
            from_carrier: An origination carrier.
            to_carrier: A destination carrier.
            from_country_code: A source country code based on phone number in From.
            to_country_code: A destination country code. Based on phone number in To.
            verified_caller: A boolean flag indicating whether or not the caller was verified using SHAKEN/STIR.One of
                'true' or 'false'.
            has_tag: A boolean flag indicating the presence of one or more `Voice Insights Call Tags
                <https://www.twilio.com/docs/voice/voice-insights/api/call/details-call-tags>`__.
            start_time: A Start time of the calls. xm (x minutes), xh (x hours), xd (x days), 1w, 30m, 3d, 4w or
                datetime-ISO. Defaults to 4h.
            end_time: An End Time of the calls. xm (x minutes), xh (x hours), xd (x days), 1w, 30m, 3d, 4w or
                datetime-ISO. Defaults to 0m.
            call_type: A Call Type of the calls. One of ``carrier``, ``sip``, ``trunking`` or ``client``.
            call_state: A Call State of the calls. One of ``ringing``, ``completed``, ``busy``, ``fail``, ``noanswer``,
                ``canceled``, ``answered``, ``undialed``.
            direction: A Direction of the calls. One of ``outbound_api``, ``outbound_dial``, ``inbound``,
                ``trunking_originating``, ``trunking_terminating``.
            processing_state: A Processing State of the Call Summaries. One of ``completed``, ``partial`` or ``all``.
            sort_by: A Sort By criterion for the returned list of Call Summaries. One of ``start_time`` or ``end_time``.
            subaccount: A unique SID identifier of a Subaccount.
            abnormal_session: A boolean flag indicating an abnormal session where the last SIP response was not 200 OK.
            answered_by: An Answered By value for the calls based on ``Answering Machine Detection (AMD)``. One of
                ``unknown``, ``machine_start``, ``machine_end_beep``, ``machine_end_silence``, ``machine_end_other``,
                ``human`` or ``fax``.
            answered_by_annotation: Either machine or human.
            connectivity_issue_annotation: A Connectivity Issue with the calls. One of ``no_connectivity_issue``,
                ``invalid_number``, ``caller_id``, ``dropped_call``, or ``number_reachability``.
            quality_issue_annotation: A subjective Quality Issue with the calls. One of ``no_quality_issue``,
                ``low_volume``, ``choppy_robotic``, ``echo``, ``dtmf``, ``latency``, ``owa``, ``static_noise``.
            spam_annotation: A boolean flag indicating spam calls.
            call_score_annotation: A Call Score of the calls. Use a range of 1-5 to indicate the call experience score,
                with the following mapping as a reference for the rated call [5: Excellent, 4: Good, 3 : Fair, 2 : Poor,
                1: Bad].
            branded_enabled: A boolean flag indicating whether or not the calls were branded using Twilio Branded Calls.
                One of 'true' or 'false'
            voice_integrity_enabled: A boolean flag indicating whether or not the phone number had voice integrity
                enabled.One of 'true' or 'false'
            branded_bundle_sid: A unique SID identifier of the Branded Call.
            branded_logo: Indicates whether the branded logo was displayed during the in_brand branded call. Possible
                values are true (logo was present) or false (logo was not present).
            branded_type: Indicates whether the Branded Call is in_band vs out_of_band.
            branded_use_case: Specifies the user-defined purpose for the call, as provided during the setup of in_band
                branded calling.
            branded_call_reason: Specifies the user-defined reason for the call, which will be displayed to the end user
                on their mobile device during an in_band branded call.
            voice_integrity_bundle_sid: A unique SID identifier of the Voice Integrity Profile.
            voice_integrity_use_case: A Voice Integrity Use Case . Is of type enum. One of 'abandoned_cart',
                'appointment_reminders', 'appointment_scheduling', 'asset_management', 'automated_support',
                'call_tracking', 'click_to_call', 'contact_tracing', 'contactless_delivery', 'customer_support',
                'dating/social', 'delivery_notifications', 'distance_learning', 'emergency_notifications',
                'employee_notifications', 'exam_proctoring', 'field_notifications', 'first_responder', 'fraud_alerts',
                'group_messaging', 'identify_&_verification', 'intelligent_routing', 'lead_alerts', 'lead_distribution',
                'lead_generation', 'lead_management', 'lead_nurturing', 'marketing_events', 'mass_alerts',
                'meetings/collaboration', 'order_notifications', 'outbound_dialer', 'pharmacy', 'phone_system',
                'purchase_confirmation', 'remote_appointments', 'rewards_program', 'self-service', 'service_alerts',
                'shift_management', 'survey/research', 'telehealth', 'telemarketing', 'therapy_(individual+group)'.
            business_profile_identity: A Business Identity of the calls. Is of type enum. One of 'direct_customer',
                'isv_reseller_or_partner'.
            business_profile_industry: A Business Industry of the calls. Is of type enum. One of 'automotive',
                'agriculture', 'banking', 'consumer', 'construction', 'education', 'engineering', 'energy',
                'oil_and_gas', 'fast_moving_consumer_goods', 'financial', 'fintech', 'food_and_beverage', 'government',
                'healthcare', 'hospitality', 'insurance', 'legal', 'manufacturing', 'media', 'online',
                'professional_services', 'raw_materials', 'real_estate', 'religion', 'retail', 'jewelry', 'technology',
                'telecommunications', 'transportation', 'travel', 'electronics', 'not_for_profit'
            business_profile_bundle_sid: A unique SID identifier of the Business Profile.
            business_profile_type: A Business Profile Type of the calls. Is of type enum. One of 'primary', 'secondary'.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_call_summaries(
                from_=from_,
                to=to,
                from_carrier=from_carrier,
                to_carrier=to_carrier,
                from_country_code=from_country_code,
                to_country_code=to_country_code,
                verified_caller=verified_caller,
                has_tag=has_tag,
                start_time=start_time,
                end_time=end_time,
                call_type=call_type,
                call_state=call_state,
                direction=direction,
                processing_state=processing_state,
                sort_by=sort_by,
                subaccount=subaccount,
                abnormal_session=abnormal_session,
                answered_by=answered_by,
                answered_by_annotation=answered_by_annotation,
                connectivity_issue_annotation=connectivity_issue_annotation,
                quality_issue_annotation=quality_issue_annotation,
                spam_annotation=spam_annotation,
                call_score_annotation=call_score_annotation,
                branded_enabled=branded_enabled,
                voice_integrity_enabled=voice_integrity_enabled,
                branded_bundle_sid=branded_bundle_sid,
                branded_logo=branded_logo,
                branded_type=branded_type,
                branded_use_case=branded_use_case,
                branded_call_reason=branded_call_reason,
                voice_integrity_bundle_sid=voice_integrity_bundle_sid,
                voice_integrity_use_case=voice_integrity_use_case,
                business_profile_identity=business_profile_identity,
                business_profile_industry=business_profile_industry,
                business_profile_bundle_sid=business_profile_bundle_sid,
                business_profile_type=business_profile_type,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncInsightsV1CallSummariesApiWithRawResponse:
        return self._with_raw_response


class InsightsV1CallSummariesApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_call_summaries(
        self,
        *,
        from_: str | None = None,
        to: str | None = None,
        from_carrier: str | None = None,
        to_carrier: str | None = None,
        from_country_code: str | None = None,
        to_country_code: str | None = None,
        verified_caller: bool | None = None,
        has_tag: bool | None = None,
        start_time: str | None = None,
        end_time: str | None = None,
        call_type: str | None = None,
        call_state: str | None = None,
        direction: str | None = None,
        processing_state: CallSummariesEnumProcessingStateRequestOrStr | None = None,
        sort_by: CallSummariesEnumSortByOrStr | None = None,
        subaccount: str | None = None,
        abnormal_session: bool | None = None,
        answered_by: CallSummariesEnumAnsweredByOrStr | None = None,
        answered_by_annotation: str | None = None,
        connectivity_issue_annotation: str | None = None,
        quality_issue_annotation: str | None = None,
        spam_annotation: bool | None = None,
        call_score_annotation: str | None = None,
        branded_enabled: bool | None = None,
        voice_integrity_enabled: bool | None = None,
        branded_bundle_sid: str | None = None,
        branded_logo: bool | None = None,
        branded_type: str | None = None,
        branded_use_case: str | None = None,
        branded_call_reason: str | None = None,
        voice_integrity_bundle_sid: str | None = None,
        voice_integrity_use_case: str | None = None,
        business_profile_identity: str | None = None,
        business_profile_industry: str | None = None,
        business_profile_bundle_sid: str | None = None,
        business_profile_type: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCallSummariesResponse, RawError]:
        """Get a list of Call Summaries.

        Args:
            from_: A calling party. Could be an E.164 number, a SIP URI, or a Twilio Client registered name.
            to: A called party. Could be an E.164 number, a SIP URI, or a Twilio Client registered name.
            from_carrier: An origination carrier.
            to_carrier: A destination carrier.
            from_country_code: A source country code based on phone number in From.
            to_country_code: A destination country code. Based on phone number in To.
            verified_caller: A boolean flag indicating whether or not the caller was verified using SHAKEN/STIR.One of
                'true' or 'false'.
            has_tag: A boolean flag indicating the presence of one or more `Voice Insights Call Tags
                <https://www.twilio.com/docs/voice/voice-insights/api/call/details-call-tags>`__.
            start_time: A Start time of the calls. xm (x minutes), xh (x hours), xd (x days), 1w, 30m, 3d, 4w or
                datetime-ISO. Defaults to 4h.
            end_time: An End Time of the calls. xm (x minutes), xh (x hours), xd (x days), 1w, 30m, 3d, 4w or
                datetime-ISO. Defaults to 0m.
            call_type: A Call Type of the calls. One of ``carrier``, ``sip``, ``trunking`` or ``client``.
            call_state: A Call State of the calls. One of ``ringing``, ``completed``, ``busy``, ``fail``, ``noanswer``,
                ``canceled``, ``answered``, ``undialed``.
            direction: A Direction of the calls. One of ``outbound_api``, ``outbound_dial``, ``inbound``,
                ``trunking_originating``, ``trunking_terminating``.
            processing_state: A Processing State of the Call Summaries. One of ``completed``, ``partial`` or ``all``.
            sort_by: A Sort By criterion for the returned list of Call Summaries. One of ``start_time`` or ``end_time``.
            subaccount: A unique SID identifier of a Subaccount.
            abnormal_session: A boolean flag indicating an abnormal session where the last SIP response was not 200 OK.
            answered_by: An Answered By value for the calls based on ``Answering Machine Detection (AMD)``. One of
                ``unknown``, ``machine_start``, ``machine_end_beep``, ``machine_end_silence``, ``machine_end_other``,
                ``human`` or ``fax``.
            answered_by_annotation: Either machine or human.
            connectivity_issue_annotation: A Connectivity Issue with the calls. One of ``no_connectivity_issue``,
                ``invalid_number``, ``caller_id``, ``dropped_call``, or ``number_reachability``.
            quality_issue_annotation: A subjective Quality Issue with the calls. One of ``no_quality_issue``,
                ``low_volume``, ``choppy_robotic``, ``echo``, ``dtmf``, ``latency``, ``owa``, ``static_noise``.
            spam_annotation: A boolean flag indicating spam calls.
            call_score_annotation: A Call Score of the calls. Use a range of 1-5 to indicate the call experience score,
                with the following mapping as a reference for the rated call [5: Excellent, 4: Good, 3 : Fair, 2 : Poor,
                1: Bad].
            branded_enabled: A boolean flag indicating whether or not the calls were branded using Twilio Branded Calls.
                One of 'true' or 'false'
            voice_integrity_enabled: A boolean flag indicating whether or not the phone number had voice integrity
                enabled.One of 'true' or 'false'
            branded_bundle_sid: A unique SID identifier of the Branded Call.
            branded_logo: Indicates whether the branded logo was displayed during the in_brand branded call. Possible
                values are true (logo was present) or false (logo was not present).
            branded_type: Indicates whether the Branded Call is in_band vs out_of_band.
            branded_use_case: Specifies the user-defined purpose for the call, as provided during the setup of in_band
                branded calling.
            branded_call_reason: Specifies the user-defined reason for the call, which will be displayed to the end user
                on their mobile device during an in_band branded call.
            voice_integrity_bundle_sid: A unique SID identifier of the Voice Integrity Profile.
            voice_integrity_use_case: A Voice Integrity Use Case . Is of type enum. One of 'abandoned_cart',
                'appointment_reminders', 'appointment_scheduling', 'asset_management', 'automated_support',
                'call_tracking', 'click_to_call', 'contact_tracing', 'contactless_delivery', 'customer_support',
                'dating/social', 'delivery_notifications', 'distance_learning', 'emergency_notifications',
                'employee_notifications', 'exam_proctoring', 'field_notifications', 'first_responder', 'fraud_alerts',
                'group_messaging', 'identify_&_verification', 'intelligent_routing', 'lead_alerts', 'lead_distribution',
                'lead_generation', 'lead_management', 'lead_nurturing', 'marketing_events', 'mass_alerts',
                'meetings/collaboration', 'order_notifications', 'outbound_dialer', 'pharmacy', 'phone_system',
                'purchase_confirmation', 'remote_appointments', 'rewards_program', 'self-service', 'service_alerts',
                'shift_management', 'survey/research', 'telehealth', 'telemarketing', 'therapy_(individual+group)'.
            business_profile_identity: A Business Identity of the calls. Is of type enum. One of 'direct_customer',
                'isv_reseller_or_partner'.
            business_profile_industry: A Business Industry of the calls. Is of type enum. One of 'automotive',
                'agriculture', 'banking', 'consumer', 'construction', 'education', 'engineering', 'energy',
                'oil_and_gas', 'fast_moving_consumer_goods', 'financial', 'fintech', 'food_and_beverage', 'government',
                'healthcare', 'hospitality', 'insurance', 'legal', 'manufacturing', 'media', 'online',
                'professional_services', 'raw_materials', 'real_estate', 'religion', 'retail', 'jewelry', 'technology',
                'telecommunications', 'transportation', 'travel', 'electronics', 'not_for_profit'
            business_profile_bundle_sid: A unique SID identifier of the Business Profile.
            business_profile_type: A Business Profile Type of the calls. Is of type enum. One of 'primary', 'secondary'.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v1/Voice/Summaries"),
            query_params=[
                param[str | None]("From", from_),
                param[str | None]("To", to),
                param[str | None]("FromCarrier", from_carrier),
                param[str | None]("ToCarrier", to_carrier),
                param[str | None]("FromCountryCode", from_country_code),
                param[str | None]("ToCountryCode", to_country_code),
                param[bool | None]("VerifiedCaller", verified_caller),
                param[bool | None]("HasTag", has_tag),
                param[str | None]("StartTime", start_time),
                param[str | None]("EndTime", end_time),
                param[str | None]("CallType", call_type),
                param[str | None]("CallState", call_state),
                param[str | None]("Direction", direction),
                param[CallSummariesEnumProcessingStateRequestOrStr | None]("ProcessingState", processing_state),
                param[CallSummariesEnumSortByOrStr | None]("SortBy", sort_by),
                param[str | None]("Subaccount", subaccount),
                param[bool | None]("AbnormalSession", abnormal_session),
                param[CallSummariesEnumAnsweredByOrStr | None]("AnsweredBy", answered_by),
                param[str | None]("AnsweredByAnnotation", answered_by_annotation),
                param[str | None]("ConnectivityIssueAnnotation", connectivity_issue_annotation),
                param[str | None]("QualityIssueAnnotation", quality_issue_annotation),
                param[bool | None]("SpamAnnotation", spam_annotation),
                param[str | None]("CallScoreAnnotation", call_score_annotation),
                param[bool | None]("BrandedEnabled", branded_enabled),
                param[bool | None]("VoiceIntegrityEnabled", voice_integrity_enabled),
                param[str | None]("BrandedBundleSid", branded_bundle_sid),
                param[bool | None]("BrandedLogo", branded_logo),
                param[str | None]("BrandedType", branded_type),
                param[str | None]("BrandedUseCase", branded_use_case),
                param[str | None]("BrandedCallReason", branded_call_reason),
                param[str | None]("VoiceIntegrityBundleSid", voice_integrity_bundle_sid),
                param[str | None]("VoiceIntegrityUseCase", voice_integrity_use_case),
                param[str | None]("BusinessProfileIdentity", business_profile_identity),
                param[str | None]("BusinessProfileIndustry", business_profile_industry),
                param[str | None]("BusinessProfileBundleSid", business_profile_bundle_sid),
                param[str | None]("BusinessProfileType", business_profile_type),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListCallSummariesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncInsightsV1CallSummariesApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_call_summaries(
        self,
        *,
        from_: str | None = None,
        to: str | None = None,
        from_carrier: str | None = None,
        to_carrier: str | None = None,
        from_country_code: str | None = None,
        to_country_code: str | None = None,
        verified_caller: bool | None = None,
        has_tag: bool | None = None,
        start_time: str | None = None,
        end_time: str | None = None,
        call_type: str | None = None,
        call_state: str | None = None,
        direction: str | None = None,
        processing_state: CallSummariesEnumProcessingStateRequestOrStr | None = None,
        sort_by: CallSummariesEnumSortByOrStr | None = None,
        subaccount: str | None = None,
        abnormal_session: bool | None = None,
        answered_by: CallSummariesEnumAnsweredByOrStr | None = None,
        answered_by_annotation: str | None = None,
        connectivity_issue_annotation: str | None = None,
        quality_issue_annotation: str | None = None,
        spam_annotation: bool | None = None,
        call_score_annotation: str | None = None,
        branded_enabled: bool | None = None,
        voice_integrity_enabled: bool | None = None,
        branded_bundle_sid: str | None = None,
        branded_logo: bool | None = None,
        branded_type: str | None = None,
        branded_use_case: str | None = None,
        branded_call_reason: str | None = None,
        voice_integrity_bundle_sid: str | None = None,
        voice_integrity_use_case: str | None = None,
        business_profile_identity: str | None = None,
        business_profile_industry: str | None = None,
        business_profile_bundle_sid: str | None = None,
        business_profile_type: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCallSummariesResponse, RawError]:
        """Get a list of Call Summaries.

        Args:
            from_: A calling party. Could be an E.164 number, a SIP URI, or a Twilio Client registered name.
            to: A called party. Could be an E.164 number, a SIP URI, or a Twilio Client registered name.
            from_carrier: An origination carrier.
            to_carrier: A destination carrier.
            from_country_code: A source country code based on phone number in From.
            to_country_code: A destination country code. Based on phone number in To.
            verified_caller: A boolean flag indicating whether or not the caller was verified using SHAKEN/STIR.One of
                'true' or 'false'.
            has_tag: A boolean flag indicating the presence of one or more `Voice Insights Call Tags
                <https://www.twilio.com/docs/voice/voice-insights/api/call/details-call-tags>`__.
            start_time: A Start time of the calls. xm (x minutes), xh (x hours), xd (x days), 1w, 30m, 3d, 4w or
                datetime-ISO. Defaults to 4h.
            end_time: An End Time of the calls. xm (x minutes), xh (x hours), xd (x days), 1w, 30m, 3d, 4w or
                datetime-ISO. Defaults to 0m.
            call_type: A Call Type of the calls. One of ``carrier``, ``sip``, ``trunking`` or ``client``.
            call_state: A Call State of the calls. One of ``ringing``, ``completed``, ``busy``, ``fail``, ``noanswer``,
                ``canceled``, ``answered``, ``undialed``.
            direction: A Direction of the calls. One of ``outbound_api``, ``outbound_dial``, ``inbound``,
                ``trunking_originating``, ``trunking_terminating``.
            processing_state: A Processing State of the Call Summaries. One of ``completed``, ``partial`` or ``all``.
            sort_by: A Sort By criterion for the returned list of Call Summaries. One of ``start_time`` or ``end_time``.
            subaccount: A unique SID identifier of a Subaccount.
            abnormal_session: A boolean flag indicating an abnormal session where the last SIP response was not 200 OK.
            answered_by: An Answered By value for the calls based on ``Answering Machine Detection (AMD)``. One of
                ``unknown``, ``machine_start``, ``machine_end_beep``, ``machine_end_silence``, ``machine_end_other``,
                ``human`` or ``fax``.
            answered_by_annotation: Either machine or human.
            connectivity_issue_annotation: A Connectivity Issue with the calls. One of ``no_connectivity_issue``,
                ``invalid_number``, ``caller_id``, ``dropped_call``, or ``number_reachability``.
            quality_issue_annotation: A subjective Quality Issue with the calls. One of ``no_quality_issue``,
                ``low_volume``, ``choppy_robotic``, ``echo``, ``dtmf``, ``latency``, ``owa``, ``static_noise``.
            spam_annotation: A boolean flag indicating spam calls.
            call_score_annotation: A Call Score of the calls. Use a range of 1-5 to indicate the call experience score,
                with the following mapping as a reference for the rated call [5: Excellent, 4: Good, 3 : Fair, 2 : Poor,
                1: Bad].
            branded_enabled: A boolean flag indicating whether or not the calls were branded using Twilio Branded Calls.
                One of 'true' or 'false'
            voice_integrity_enabled: A boolean flag indicating whether or not the phone number had voice integrity
                enabled.One of 'true' or 'false'
            branded_bundle_sid: A unique SID identifier of the Branded Call.
            branded_logo: Indicates whether the branded logo was displayed during the in_brand branded call. Possible
                values are true (logo was present) or false (logo was not present).
            branded_type: Indicates whether the Branded Call is in_band vs out_of_band.
            branded_use_case: Specifies the user-defined purpose for the call, as provided during the setup of in_band
                branded calling.
            branded_call_reason: Specifies the user-defined reason for the call, which will be displayed to the end user
                on their mobile device during an in_band branded call.
            voice_integrity_bundle_sid: A unique SID identifier of the Voice Integrity Profile.
            voice_integrity_use_case: A Voice Integrity Use Case . Is of type enum. One of 'abandoned_cart',
                'appointment_reminders', 'appointment_scheduling', 'asset_management', 'automated_support',
                'call_tracking', 'click_to_call', 'contact_tracing', 'contactless_delivery', 'customer_support',
                'dating/social', 'delivery_notifications', 'distance_learning', 'emergency_notifications',
                'employee_notifications', 'exam_proctoring', 'field_notifications', 'first_responder', 'fraud_alerts',
                'group_messaging', 'identify_&_verification', 'intelligent_routing', 'lead_alerts', 'lead_distribution',
                'lead_generation', 'lead_management', 'lead_nurturing', 'marketing_events', 'mass_alerts',
                'meetings/collaboration', 'order_notifications', 'outbound_dialer', 'pharmacy', 'phone_system',
                'purchase_confirmation', 'remote_appointments', 'rewards_program', 'self-service', 'service_alerts',
                'shift_management', 'survey/research', 'telehealth', 'telemarketing', 'therapy_(individual+group)'.
            business_profile_identity: A Business Identity of the calls. Is of type enum. One of 'direct_customer',
                'isv_reseller_or_partner'.
            business_profile_industry: A Business Industry of the calls. Is of type enum. One of 'automotive',
                'agriculture', 'banking', 'consumer', 'construction', 'education', 'engineering', 'energy',
                'oil_and_gas', 'fast_moving_consumer_goods', 'financial', 'fintech', 'food_and_beverage', 'government',
                'healthcare', 'hospitality', 'insurance', 'legal', 'manufacturing', 'media', 'online',
                'professional_services', 'raw_materials', 'real_estate', 'religion', 'retail', 'jewelry', 'technology',
                'telecommunications', 'transportation', 'travel', 'electronics', 'not_for_profit'
            business_profile_bundle_sid: A unique SID identifier of the Business Profile.
            business_profile_type: A Business Profile Type of the calls. Is of type enum. One of 'primary', 'secondary'.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v1/Voice/Summaries"),
            query_params=[
                param[str | None]("From", from_),
                param[str | None]("To", to),
                param[str | None]("FromCarrier", from_carrier),
                param[str | None]("ToCarrier", to_carrier),
                param[str | None]("FromCountryCode", from_country_code),
                param[str | None]("ToCountryCode", to_country_code),
                param[bool | None]("VerifiedCaller", verified_caller),
                param[bool | None]("HasTag", has_tag),
                param[str | None]("StartTime", start_time),
                param[str | None]("EndTime", end_time),
                param[str | None]("CallType", call_type),
                param[str | None]("CallState", call_state),
                param[str | None]("Direction", direction),
                param[CallSummariesEnumProcessingStateRequestOrStr | None]("ProcessingState", processing_state),
                param[CallSummariesEnumSortByOrStr | None]("SortBy", sort_by),
                param[str | None]("Subaccount", subaccount),
                param[bool | None]("AbnormalSession", abnormal_session),
                param[CallSummariesEnumAnsweredByOrStr | None]("AnsweredBy", answered_by),
                param[str | None]("AnsweredByAnnotation", answered_by_annotation),
                param[str | None]("ConnectivityIssueAnnotation", connectivity_issue_annotation),
                param[str | None]("QualityIssueAnnotation", quality_issue_annotation),
                param[bool | None]("SpamAnnotation", spam_annotation),
                param[str | None]("CallScoreAnnotation", call_score_annotation),
                param[bool | None]("BrandedEnabled", branded_enabled),
                param[bool | None]("VoiceIntegrityEnabled", voice_integrity_enabled),
                param[str | None]("BrandedBundleSid", branded_bundle_sid),
                param[bool | None]("BrandedLogo", branded_logo),
                param[str | None]("BrandedType", branded_type),
                param[str | None]("BrandedUseCase", branded_use_case),
                param[str | None]("BrandedCallReason", branded_call_reason),
                param[str | None]("VoiceIntegrityBundleSid", voice_integrity_bundle_sid),
                param[str | None]("VoiceIntegrityUseCase", voice_integrity_use_case),
                param[str | None]("BusinessProfileIdentity", business_profile_identity),
                param[str | None]("BusinessProfileIndustry", business_profile_industry),
                param[str | None]("BusinessProfileBundleSid", business_profile_bundle_sid),
                param[str | None]("BusinessProfileType", business_profile_type),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListCallSummariesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
