from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.api_v2010_account_call_realtime_transcription import ApiV2010AccountCallRealtimeTranscription
from ..models.enums.realtime_transcription_enum_track import RealtimeTranscriptionEnumTrackOrStr
from ..models.enums.realtime_transcription_enum_update_status import RealtimeTranscriptionEnumUpdateStatusOrStr
from ..models.enums.status_callback_method17 import StatusCallbackMethod17OrStr
from ..server.server import Server


class Api20100401CallTranscription:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401CallTranscriptionWithRawResponse(client, server, auth)

    def create_realtime_transcription(
        self,
        account_sid: str,
        call_sid: str,
        *,
        name: str | None = None,
        track: RealtimeTranscriptionEnumTrackOrStr | None = None,
        status_callback_url: str | None = None,
        status_callback_method: StatusCallbackMethod17OrStr | None = None,
        inbound_track_label: str | None = None,
        outbound_track_label: str | None = None,
        partial_results: bool | None = None,
        language_code: str | None = None,
        transcription_engine: str | None = None,
        profanity_filter: bool | None = None,
        speech_model: str | None = None,
        hints: str | None = None,
        enable_automatic_punctuation: bool | None = None,
        intelligence_service: str | None = None,
        conversation_configuration: str | None = None,
        conversation_id: str | None = None,
        transcription_configuration_id: str | None = None,
        enable_provider_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountCallRealtimeTranscription:
        """Create a Transcription

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created this
                Transcription resource.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the Transcription
                resource is associated with.
            name: The user-specified name of this Transcription, if one was given when the Transcription was created.
                This may be used to stop the Transcription.
            track: One of ``inbound_track``, ``outbound_track``, ``both_tracks``.
            status_callback_url: Absolute URL of the status callback.
            status_callback_method: The http method for the status_callback (one of GET, POST).
            inbound_track_label: Friendly name given to the Inbound Track
            outbound_track_label: Friendly name given to the Outbound Track
            partial_results: Indicates if partial results are going to be sent to the customer
            language_code: Language code used by the transcription engine, specified in `BCP-47
                <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__ format
            transcription_engine: Definition of the transcription engine to be used, among those supported by Twilio
            profanity_filter: indicates if the server will attempt to filter out profanities, replacing all but the
                initial character in each filtered word with asterisks
            speech_model: Recognition model used by the transcription engine, among those supported by the provider
            hints: A Phrase contains words and phrase "hints" so that the speech recognition engine is more likely to
                recognize them.
            enable_automatic_punctuation: The provider will add punctuation to recognition result
            intelligence_service: The SID or unique name of the `Intelligence Service
                <https://www.twilio.com/docs/conversational-intelligence/api/service-resource>`__ for persisting
                transcripts and running post-call Language Operators
            conversation_configuration: The ID of the Conversations Configuration for customizing conversation behavior
                in Intelligence Service
            conversation_id: The ID of the Conversation for associating this Transcription with an existing Conversation
                in Intelligence Service
            transcription_configuration_id: The ID of the RealTimeTranscription Configuration for configuring all the
                non-default behaviors in one go.
            enable_provider_data: Whether the callback includes raw provider data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_realtime_transcription(
            account_sid,
            call_sid,
            name=name,
            track=track,
            status_callback_url=status_callback_url,
            status_callback_method=status_callback_method,
            inbound_track_label=inbound_track_label,
            outbound_track_label=outbound_track_label,
            partial_results=partial_results,
            language_code=language_code,
            transcription_engine=transcription_engine,
            profanity_filter=profanity_filter,
            speech_model=speech_model,
            hints=hints,
            enable_automatic_punctuation=enable_automatic_punctuation,
            intelligence_service=intelligence_service,
            conversation_configuration=conversation_configuration,
            conversation_id=conversation_id,
            transcription_configuration_id=transcription_configuration_id,
            enable_provider_data=enable_provider_data,
            request_options=request_options,
        ).unwrap()

    def update_realtime_transcription(
        self,
        account_sid: str,
        call_sid: str,
        sid: str,
        status: RealtimeTranscriptionEnumUpdateStatusOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountCallRealtimeTranscription:
        """Stop a Transcription using either the SID of the Transcription resource or the ``name`` used when creating
        the resource

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created this
                Transcription resource.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the Transcription
                resource is associated with.
            sid: The SID of the Transcription resource, or the ``name`` used when creating the resource
            status: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_realtime_transcription(
            account_sid, call_sid, sid, status, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401CallTranscriptionWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401CallTranscription:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401CallTranscriptionWithRawResponse(client, server, auth)

    async def create_realtime_transcription(
        self,
        account_sid: str,
        call_sid: str,
        *,
        name: str | None = None,
        track: RealtimeTranscriptionEnumTrackOrStr | None = None,
        status_callback_url: str | None = None,
        status_callback_method: StatusCallbackMethod17OrStr | None = None,
        inbound_track_label: str | None = None,
        outbound_track_label: str | None = None,
        partial_results: bool | None = None,
        language_code: str | None = None,
        transcription_engine: str | None = None,
        profanity_filter: bool | None = None,
        speech_model: str | None = None,
        hints: str | None = None,
        enable_automatic_punctuation: bool | None = None,
        intelligence_service: str | None = None,
        conversation_configuration: str | None = None,
        conversation_id: str | None = None,
        transcription_configuration_id: str | None = None,
        enable_provider_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountCallRealtimeTranscription:
        """Create a Transcription

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created this
                Transcription resource.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the Transcription
                resource is associated with.
            name: The user-specified name of this Transcription, if one was given when the Transcription was created.
                This may be used to stop the Transcription.
            track: One of ``inbound_track``, ``outbound_track``, ``both_tracks``.
            status_callback_url: Absolute URL of the status callback.
            status_callback_method: The http method for the status_callback (one of GET, POST).
            inbound_track_label: Friendly name given to the Inbound Track
            outbound_track_label: Friendly name given to the Outbound Track
            partial_results: Indicates if partial results are going to be sent to the customer
            language_code: Language code used by the transcription engine, specified in `BCP-47
                <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__ format
            transcription_engine: Definition of the transcription engine to be used, among those supported by Twilio
            profanity_filter: indicates if the server will attempt to filter out profanities, replacing all but the
                initial character in each filtered word with asterisks
            speech_model: Recognition model used by the transcription engine, among those supported by the provider
            hints: A Phrase contains words and phrase "hints" so that the speech recognition engine is more likely to
                recognize them.
            enable_automatic_punctuation: The provider will add punctuation to recognition result
            intelligence_service: The SID or unique name of the `Intelligence Service
                <https://www.twilio.com/docs/conversational-intelligence/api/service-resource>`__ for persisting
                transcripts and running post-call Language Operators
            conversation_configuration: The ID of the Conversations Configuration for customizing conversation behavior
                in Intelligence Service
            conversation_id: The ID of the Conversation for associating this Transcription with an existing Conversation
                in Intelligence Service
            transcription_configuration_id: The ID of the RealTimeTranscription Configuration for configuring all the
                non-default behaviors in one go.
            enable_provider_data: Whether the callback includes raw provider data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_realtime_transcription(
                account_sid,
                call_sid,
                name=name,
                track=track,
                status_callback_url=status_callback_url,
                status_callback_method=status_callback_method,
                inbound_track_label=inbound_track_label,
                outbound_track_label=outbound_track_label,
                partial_results=partial_results,
                language_code=language_code,
                transcription_engine=transcription_engine,
                profanity_filter=profanity_filter,
                speech_model=speech_model,
                hints=hints,
                enable_automatic_punctuation=enable_automatic_punctuation,
                intelligence_service=intelligence_service,
                conversation_configuration=conversation_configuration,
                conversation_id=conversation_id,
                transcription_configuration_id=transcription_configuration_id,
                enable_provider_data=enable_provider_data,
                request_options=request_options,
            )
        ).unwrap()

    async def update_realtime_transcription(
        self,
        account_sid: str,
        call_sid: str,
        sid: str,
        status: RealtimeTranscriptionEnumUpdateStatusOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountCallRealtimeTranscription:
        """Stop a Transcription using either the SID of the Transcription resource or the ``name`` used when creating
        the resource

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created this
                Transcription resource.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the Transcription
                resource is associated with.
            sid: The SID of the Transcription resource, or the ``name`` used when creating the resource
            status: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_realtime_transcription(
                account_sid, call_sid, sid, status, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401CallTranscriptionWithRawResponse:
        return self._with_raw_response


class Api20100401CallTranscriptionWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_realtime_transcription(
        self,
        account_sid: str,
        call_sid: str,
        *,
        name: str | None = None,
        track: RealtimeTranscriptionEnumTrackOrStr | None = None,
        status_callback_url: str | None = None,
        status_callback_method: StatusCallbackMethod17OrStr | None = None,
        inbound_track_label: str | None = None,
        outbound_track_label: str | None = None,
        partial_results: bool | None = None,
        language_code: str | None = None,
        transcription_engine: str | None = None,
        profanity_filter: bool | None = None,
        speech_model: str | None = None,
        hints: str | None = None,
        enable_automatic_punctuation: bool | None = None,
        intelligence_service: str | None = None,
        conversation_configuration: str | None = None,
        conversation_id: str | None = None,
        transcription_configuration_id: str | None = None,
        enable_provider_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountCallRealtimeTranscription, RawError]:
        """Create a Transcription

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created this
                Transcription resource.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the Transcription
                resource is associated with.
            name: The user-specified name of this Transcription, if one was given when the Transcription was created.
                This may be used to stop the Transcription.
            track: One of ``inbound_track``, ``outbound_track``, ``both_tracks``.
            status_callback_url: Absolute URL of the status callback.
            status_callback_method: The http method for the status_callback (one of GET, POST).
            inbound_track_label: Friendly name given to the Inbound Track
            outbound_track_label: Friendly name given to the Outbound Track
            partial_results: Indicates if partial results are going to be sent to the customer
            language_code: Language code used by the transcription engine, specified in `BCP-47
                <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__ format
            transcription_engine: Definition of the transcription engine to be used, among those supported by Twilio
            profanity_filter: indicates if the server will attempt to filter out profanities, replacing all but the
                initial character in each filtered word with asterisks
            speech_model: Recognition model used by the transcription engine, among those supported by the provider
            hints: A Phrase contains words and phrase "hints" so that the speech recognition engine is more likely to
                recognize them.
            enable_automatic_punctuation: The provider will add punctuation to recognition result
            intelligence_service: The SID or unique name of the `Intelligence Service
                <https://www.twilio.com/docs/conversational-intelligence/api/service-resource>`__ for persisting
                transcripts and running post-call Language Operators
            conversation_configuration: The ID of the Conversations Configuration for customizing conversation behavior
                in Intelligence Service
            conversation_id: The ID of the Conversation for associating this Transcription with an existing Conversation
                in Intelligence Service
            transcription_configuration_id: The ID of the RealTimeTranscription Configuration for configuring all the
                non-default behaviors in one go.
            enable_provider_data: Whether the callback includes raw provider data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Transcriptions.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("CallSid", call_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("Name", name),
                    param[RealtimeTranscriptionEnumTrackOrStr | None]("Track", track),
                    param[str | None]("StatusCallbackUrl", status_callback_url),
                    param[StatusCallbackMethod17OrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[str | None]("InboundTrackLabel", inbound_track_label),
                    param[str | None]("OutboundTrackLabel", outbound_track_label),
                    param[bool | None]("PartialResults", partial_results),
                    param[str | None]("LanguageCode", language_code),
                    param[str | None]("TranscriptionEngine", transcription_engine),
                    param[bool | None]("ProfanityFilter", profanity_filter),
                    param[str | None]("SpeechModel", speech_model),
                    param[str | None]("Hints", hints),
                    param[bool | None]("EnableAutomaticPunctuation", enable_automatic_punctuation),
                    param[str | None]("IntelligenceService", intelligence_service),
                    param[str | None]("ConversationConfiguration", conversation_configuration),
                    param[str | None]("ConversationId", conversation_id),
                    param[str | None]("TranscriptionConfigurationId", transcription_configuration_id),
                    param[bool | None]("EnableProviderData", enable_provider_data),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountCallRealtimeTranscription],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_realtime_transcription(
        self,
        account_sid: str,
        call_sid: str,
        sid: str,
        status: RealtimeTranscriptionEnumUpdateStatusOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountCallRealtimeTranscription, RawError]:
        """Stop a Transcription using either the SID of the Transcription resource or the ``name`` used when creating
        the resource

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created this
                Transcription resource.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the Transcription
                resource is associated with.
            sid: The SID of the Transcription resource, or the ``name`` used when creating the resource
            status: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Transcriptions/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("CallSid", call_sid), param[str]("Sid", sid)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[RealtimeTranscriptionEnumUpdateStatusOrStr]("Status", status)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountCallRealtimeTranscription],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401CallTranscriptionWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_realtime_transcription(
        self,
        account_sid: str,
        call_sid: str,
        *,
        name: str | None = None,
        track: RealtimeTranscriptionEnumTrackOrStr | None = None,
        status_callback_url: str | None = None,
        status_callback_method: StatusCallbackMethod17OrStr | None = None,
        inbound_track_label: str | None = None,
        outbound_track_label: str | None = None,
        partial_results: bool | None = None,
        language_code: str | None = None,
        transcription_engine: str | None = None,
        profanity_filter: bool | None = None,
        speech_model: str | None = None,
        hints: str | None = None,
        enable_automatic_punctuation: bool | None = None,
        intelligence_service: str | None = None,
        conversation_configuration: str | None = None,
        conversation_id: str | None = None,
        transcription_configuration_id: str | None = None,
        enable_provider_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountCallRealtimeTranscription, RawError]:
        """Create a Transcription

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created this
                Transcription resource.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the Transcription
                resource is associated with.
            name: The user-specified name of this Transcription, if one was given when the Transcription was created.
                This may be used to stop the Transcription.
            track: One of ``inbound_track``, ``outbound_track``, ``both_tracks``.
            status_callback_url: Absolute URL of the status callback.
            status_callback_method: The http method for the status_callback (one of GET, POST).
            inbound_track_label: Friendly name given to the Inbound Track
            outbound_track_label: Friendly name given to the Outbound Track
            partial_results: Indicates if partial results are going to be sent to the customer
            language_code: Language code used by the transcription engine, specified in `BCP-47
                <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__ format
            transcription_engine: Definition of the transcription engine to be used, among those supported by Twilio
            profanity_filter: indicates if the server will attempt to filter out profanities, replacing all but the
                initial character in each filtered word with asterisks
            speech_model: Recognition model used by the transcription engine, among those supported by the provider
            hints: A Phrase contains words and phrase "hints" so that the speech recognition engine is more likely to
                recognize them.
            enable_automatic_punctuation: The provider will add punctuation to recognition result
            intelligence_service: The SID or unique name of the `Intelligence Service
                <https://www.twilio.com/docs/conversational-intelligence/api/service-resource>`__ for persisting
                transcripts and running post-call Language Operators
            conversation_configuration: The ID of the Conversations Configuration for customizing conversation behavior
                in Intelligence Service
            conversation_id: The ID of the Conversation for associating this Transcription with an existing Conversation
                in Intelligence Service
            transcription_configuration_id: The ID of the RealTimeTranscription Configuration for configuring all the
                non-default behaviors in one go.
            enable_provider_data: Whether the callback includes raw provider data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Transcriptions.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("CallSid", call_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("Name", name),
                    param[RealtimeTranscriptionEnumTrackOrStr | None]("Track", track),
                    param[str | None]("StatusCallbackUrl", status_callback_url),
                    param[StatusCallbackMethod17OrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[str | None]("InboundTrackLabel", inbound_track_label),
                    param[str | None]("OutboundTrackLabel", outbound_track_label),
                    param[bool | None]("PartialResults", partial_results),
                    param[str | None]("LanguageCode", language_code),
                    param[str | None]("TranscriptionEngine", transcription_engine),
                    param[bool | None]("ProfanityFilter", profanity_filter),
                    param[str | None]("SpeechModel", speech_model),
                    param[str | None]("Hints", hints),
                    param[bool | None]("EnableAutomaticPunctuation", enable_automatic_punctuation),
                    param[str | None]("IntelligenceService", intelligence_service),
                    param[str | None]("ConversationConfiguration", conversation_configuration),
                    param[str | None]("ConversationId", conversation_id),
                    param[str | None]("TranscriptionConfigurationId", transcription_configuration_id),
                    param[bool | None]("EnableProviderData", enable_provider_data),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountCallRealtimeTranscription],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_realtime_transcription(
        self,
        account_sid: str,
        call_sid: str,
        sid: str,
        status: RealtimeTranscriptionEnumUpdateStatusOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountCallRealtimeTranscription, RawError]:
        """Stop a Transcription using either the SID of the Transcription resource or the ``name`` used when creating
        the resource

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created this
                Transcription resource.
            call_sid: The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the Transcription
                resource is associated with.
            sid: The SID of the Transcription resource, or the ``name`` used when creating the resource
            status: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Transcriptions/{Sid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid), param[str]("CallSid", call_sid), param[str]("Sid", sid)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[RealtimeTranscriptionEnumUpdateStatusOrStr]("Status", status)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountCallRealtimeTranscription],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
