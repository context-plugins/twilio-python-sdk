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
    empty_response,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.api_v2010_account_conference_participant import ApiV2010AccountConferenceParticipant
from ..models.enums.amd_status_callback_method import AmdStatusCallbackMethodOrStr
from ..models.enums.announce_method1 import AnnounceMethod1OrStr
from ..models.enums.conference_recording_status_callback_method import ConferenceRecordingStatusCallbackMethodOrStr
from ..models.enums.conference_status_callback_method import ConferenceStatusCallbackMethodOrStr
from ..models.enums.hold_method import HoldMethodOrStr
from ..models.enums.recording_status_callback_method2 import RecordingStatusCallbackMethod2OrStr
from ..models.enums.status_callback_method16 import StatusCallbackMethod16OrStr
from ..models.enums.wait_method import WaitMethodOrStr
from ..models.list_participant_response import ListParticipantResponse
from ..server.server import Server


class Api20100401Participant:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401ParticipantWithRawResponse(client, server, auth)

    def create_participant(
        self,
        account_sid: str,
        conference_sid: str,
        from_: str,
        to: str,
        *,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod16OrStr | None = None,
        status_callback_event: list[str] | None = None,
        label: str | None = None,
        timeout: int | None = None,
        record: bool | None = None,
        muted: bool | None = None,
        beep: str | None = None,
        start_conference_on_enter: bool | None = None,
        end_conference_on_exit: bool | None = None,
        wait_url: str | None = None,
        wait_method: WaitMethodOrStr | None = None,
        early_media: bool | None = None,
        max_participants: int | None = None,
        conference_record: str | None = None,
        conference_trim: str | None = None,
        conference_status_callback: str | None = None,
        conference_status_callback_method: ConferenceStatusCallbackMethodOrStr | None = None,
        conference_status_callback_event: list[str] | None = None,
        recording_channels: str | None = None,
        recording_status_callback: str | None = None,
        recording_status_callback_method: RecordingStatusCallbackMethod2OrStr | None = None,
        sip_auth_username: str | None = None,
        sip_auth_password: str | None = None,
        region: str | None = None,
        conference_recording_status_callback: str | None = None,
        conference_recording_status_callback_method: ConferenceRecordingStatusCallbackMethodOrStr | None = None,
        recording_status_callback_event: list[str] | None = None,
        conference_recording_status_callback_event: list[str] | None = None,
        coaching: bool | None = None,
        call_sid_to_coach: str | None = None,
        jitter_buffer_size: str | None = None,
        byoc: str | None = None,
        caller_id: str | None = None,
        call_reason: str | None = None,
        recording_track: str | None = None,
        recording_configuration_id: str | None = None,
        time_limit: int | None = None,
        machine_detection: str | None = None,
        machine_detection_timeout: int | None = None,
        machine_detection_speech_threshold: int | None = None,
        machine_detection_speech_end_threshold: int | None = None,
        machine_detection_silence_timeout: int | None = None,
        amd_status_callback: str | None = None,
        amd_status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        trim: str | None = None,
        call_token: str | None = None,
        client_notification_url: str | None = None,
        caller_display_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountConferenceParticipant:
        """Conference participants

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            conference_sid: The SID of the participant's conference.
            from_: The phone number, Client identifier, or username portion of SIP address that made this call. Phone
                numbers are in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format (e.g., +16175551212).
                Client identifiers are formatted ``client:name``. If using a phone number, it must be a Twilio number or
                a Verified `outgoing caller id <https://www.twilio.com/docs/voice/api/outgoing-caller-ids>`__ for your
                account. If the ``to`` parameter is a phone number, ``from`` must also be a phone number. If ``to`` is
                sip address, this value of ``from`` should be a username portion to be used to populate the
                P-Asserted-Identity header that is passed to the SIP endpoint.
            to: The phone number, SIP address, Client, TwiML App identifier that received this call. Phone numbers are
                in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format (e.g., +16175551212). SIP addresses
                are formatted as ``sip:name@company.com``. Client identifiers are formatted ``client:name``. TwiML App
                identifiers are formatted ``app:<APP_SID>``. `Custom parameters
                <https://www.twilio.com/docs/voice/api/conference-participant-resource#custom-parameters>`__ may also be
                specified.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``GET`` and
                ``POST`` and defaults to ``POST``.
            status_callback_event: The conference state changes that should generate a call to ``status_callback``. Can
                be: ``initiated``, ``ringing``, ``answered``, and ``completed``. Separate multiple values with a space.
                The default value is ``completed``.
            label: A label for this participant. If one is supplied, it may subsequently be used to fetch, update or
                delete the participant.
            timeout: The number of seconds that we should allow the phone to ring before assuming there is no answer.
                Can be an integer between ``5`` and ``600``, inclusive. The default value is ``60``. We always add a
                5-second timeout buffer to outgoing calls, so value of 10 would result in an actual timeout that was
                closer to 15 seconds.
            record: Whether to record the participant and their conferences, including the time between conferences. Can
                be ``true`` or ``false`` and the default is ``false``.
            muted: Whether the agent is muted in the conference. Can be ``true`` or ``false`` and the default is
                ``false``.
            beep: Whether to play a notification beep to the conference when the participant joins. Can be: ``true``,
                ``false``, ``onEnter``, or ``onExit``. The default value is ``true``.
            start_conference_on_enter: Whether to start the conference when the participant joins, if it has not already
                started. Can be: ``true`` or ``false`` and the default is ``true``. If ``false`` and the conference has
                not started, the participant is muted and hears background music until another participant starts the
                conference.
            end_conference_on_exit: Whether to end the conference when the participant leaves. Can be: ``true`` or
                ``false`` and defaults to ``false``.
            wait_url: The URL that Twilio calls using the ``wait_method`` before the conference has started. The URL may
                return an MP3 file, a WAV file, or a TwiML document. The default value is the URL of our standard hold
                music. If you do not want anything to play while waiting for the conference to start, specify an empty
                string by setting ``wait_url`` to ``''``. For more details on the allowable verbs within the
                ``waitUrl``, see the ``waitUrl`` attribute in the
                https://www.twilio.com/docs/voice/twiml/conference#attributes-waiturl.
            wait_method: The HTTP method we should use to call ``wait_url``. Can be ``GET`` or ``POST`` and the default
                is ``POST``. When using a static audio file, this should be ``GET`` so that we can cache the file.
            early_media: Whether to allow an agent to hear the state of the outbound call, including ringing or
                disconnect messages. Can be: ``true`` or ``false`` and defaults to ``true``.
            max_participants: The maximum number of participants in the conference. Can be a positive integer from ``2``
                to ``250``. The default value is ``250``.
            conference_record: Whether to record the conference the participant is joining. Can be: ``true``, ``false``,
                ``record-from-start``, and ``do-not-record``. The default value is ``false``.
            conference_trim: Whether to trim leading and trailing silence from the conference recording. Can be:
                ``trim-silence`` or ``do-not-trim`` and defaults to ``trim-silence``.
            conference_status_callback: The URL we should call using the ``conference_status_callback_method`` when the
                conference events in ``conference_status_callback_event`` occur. Only the value set by the first
                participant to join the conference is used. Subsequent ``conference_status_callback`` values are
                ignored.
            conference_status_callback_method: The HTTP method we should use to call ``conference_status_callback``. Can
                be: ``GET`` or ``POST`` and defaults to ``POST``.
            conference_status_callback_event: The conference state changes that should generate a call to
                ``conference_status_callback``. Can be: ``start``, ``end``, ``join``, ``leave``, ``mute``, ``hold``,
                ``modify``, ``speaker``, and ``announcement``. Separate multiple values with a space. Defaults to
                ``start end``.
            recording_channels: The recording channels for the final recording. Can be: ``mono`` or ``dual`` and the
                default is ``mono``.
            recording_status_callback: The URL that we should call using the ``recording_status_callback_method`` when
                the recording status changes.
            recording_status_callback_method: The HTTP method we should use when we call ``recording_status_callback``.
                Can be: ``GET`` or ``POST`` and defaults to ``POST``.
            sip_auth_username: The SIP username used for authentication.
            sip_auth_password: The SIP password for authentication.
            region: The `region
                <https://support.twilio.com/hc/en-us/articles/223132167-How-global-low-latency-routing-and-region-selection-work-for-conferences-and-Client-calls>`__
                where we should mix the recorded audio. Can be:``us1``, ``us2``, ``ie1``, ``de1``, ``sg1``, ``br1``,
                ``au1``, or ``jp1``.
            conference_recording_status_callback: The URL we should call using the
                ``conference_recording_status_callback_method`` when the conference recording is available.
            conference_recording_status_callback_method: The HTTP method we should use to call
                ``conference_recording_status_callback``. Can be: ``GET`` or ``POST`` and defaults to ``POST``.
            recording_status_callback_event: The recording state changes that should generate a call to
                ``recording_status_callback``. Can be: ``started``, ``in-progress``, ``paused``, ``resumed``,
                ``stopped``, ``completed``, ``failed``, and ``absent``. Separate multiple values with a space, ex:
                ``'in-progress completed failed'``.
            conference_recording_status_callback_event: The conference recording state changes that generate a call to
                ``conference_recording_status_callback``. Can be: ``in-progress``, ``completed``, ``failed``, and
                ``absent``. Separate multiple values with a space, ex: ``'in-progress completed failed'``
            coaching: Whether the participant is coaching another call. Can be: ``true`` or ``false``. If not present,
                defaults to ``false`` unless ``call_sid_to_coach`` is defined. If ``true``, ``call_sid_to_coach`` must
                be defined.
            call_sid_to_coach: The SID of the participant who is being ``coached``. The participant being coached is the
                only participant who can hear the participant who is ``coaching``.
            jitter_buffer_size: Jitter buffer size for the connecting participant. Twilio will use this setting to apply
                Jitter Buffer before participant's audio is mixed into the conference. Can be: ``off``, ``small``,
                ``medium``, and ``large``. Default to ``large``.
            byoc: The SID of a BYOC (Bring Your Own Carrier) trunk to route this call with. Note that ``byoc`` is only
                meaningful when ``to`` is a phone number; it will otherwise be ignored. (Beta)
            caller_id: The phone number, Client identifier, or username portion of SIP address that made this call.
                Phone numbers are in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format (e.g.,
                +16175551212). Client identifiers are formatted ``client:name``. If using a phone number, it must be a
                Twilio number or a Verified `outgoing caller id
                <https://www.twilio.com/docs/voice/api/outgoing-caller-ids>`__ for your account. If the ``to`` parameter
                is a phone number, ``callerId`` must also be a phone number. If ``to`` is sip address, this value of
                ``callerId`` should be a username portion to be used to populate the From header that is passed to the
                SIP endpoint.
            call_reason: The Reason for the outgoing call. Use it to specify the purpose of the call that is presented
                on the called party's phone. (Branded Calls Beta)
            recording_track: The audio track to record for the call. Can be: ``inbound``, ``outbound`` or ``both``. The
                default is ``both``. ``inbound`` records the audio that is received by Twilio. ``outbound`` records the
                audio that is sent from Twilio. ``both`` records the audio that is received and sent by Twilio.
            recording_configuration_id: The identifier of the configuration to be used when creating and processing the
                recording
            time_limit: The maximum duration of the call in seconds. Constraints depend on account and configuration.
            machine_detection: Whether to detect if a human, answering machine, or fax has picked up the call. Can be:
                ``Enable`` or ``DetectMessageEnd``. Use ``Enable`` if you would like us to return ``AnsweredBy`` as soon
                as the called party is identified. Use ``DetectMessageEnd``, if you would like to leave a message on an
                answering machine. For more information, see `Answering Machine Detection
                <https://www.twilio.com/docs/voice/answering-machine-detection>`__.
            machine_detection_timeout: The number of seconds that we should attempt to detect an answering machine
                before timing out and sending a voice request with ``AnsweredBy`` of ``unknown``. The default timeout is
                30 seconds.
            machine_detection_speech_threshold: The number of milliseconds that is used as the measuring stick for the
                length of the speech activity, where durations lower than this value will be interpreted as a human and
                longer than this value as a machine. Possible Values: 1000-6000. Default: 2400.
            machine_detection_speech_end_threshold: The number of milliseconds of silence after speech activity at which
                point the speech activity is considered complete. Possible Values: 500-5000. Default: 1200.
            machine_detection_silence_timeout: The number of milliseconds of initial silence after which an ``unknown``
                AnsweredBy result will be returned. Possible Values: 2000-10000. Default: 5000.
            amd_status_callback: The URL that we should call using the ``amd_status_callback_method`` to notify customer
                application whether the call was answered by human, machine or fax.
            amd_status_callback_method: The HTTP method we should use when calling the ``amd_status_callback`` URL. Can
                be: ``GET`` or ``POST`` and the default is ``POST``.
            trim: Whether to trim any leading and trailing silence from the participant recording. Can be:
                ``trim-silence`` or ``do-not-trim`` and the default is ``trim-silence``.
            call_token: A token string needed to invoke a forwarded call. A call_token is generated when an incoming
                call is received on a Twilio number. Pass an incoming call's call_token value to a forwarded call via
                the call_token parameter when creating a new call. A forwarded call should bear the same CallerID of the
                original incoming call.
            client_notification_url: The URL that we should use to deliver ``push call notification``.
            caller_display_name: The name that populates the display name in the From header. Must be between 2 and 255
                characters. Only applicable for calls to sip address.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_participant(
            account_sid,
            conference_sid,
            from_,
            to,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            status_callback_event=status_callback_event,
            label=label,
            timeout=timeout,
            record=record,
            muted=muted,
            beep=beep,
            start_conference_on_enter=start_conference_on_enter,
            end_conference_on_exit=end_conference_on_exit,
            wait_url=wait_url,
            wait_method=wait_method,
            early_media=early_media,
            max_participants=max_participants,
            conference_record=conference_record,
            conference_trim=conference_trim,
            conference_status_callback=conference_status_callback,
            conference_status_callback_method=conference_status_callback_method,
            conference_status_callback_event=conference_status_callback_event,
            recording_channels=recording_channels,
            recording_status_callback=recording_status_callback,
            recording_status_callback_method=recording_status_callback_method,
            sip_auth_username=sip_auth_username,
            sip_auth_password=sip_auth_password,
            region=region,
            conference_recording_status_callback=conference_recording_status_callback,
            conference_recording_status_callback_method=conference_recording_status_callback_method,
            recording_status_callback_event=recording_status_callback_event,
            conference_recording_status_callback_event=conference_recording_status_callback_event,
            coaching=coaching,
            call_sid_to_coach=call_sid_to_coach,
            jitter_buffer_size=jitter_buffer_size,
            byoc=byoc,
            caller_id=caller_id,
            call_reason=call_reason,
            recording_track=recording_track,
            recording_configuration_id=recording_configuration_id,
            time_limit=time_limit,
            machine_detection=machine_detection,
            machine_detection_timeout=machine_detection_timeout,
            machine_detection_speech_threshold=machine_detection_speech_threshold,
            machine_detection_speech_end_threshold=machine_detection_speech_end_threshold,
            machine_detection_silence_timeout=machine_detection_silence_timeout,
            amd_status_callback=amd_status_callback,
            amd_status_callback_method=amd_status_callback_method,
            trim=trim,
            call_token=call_token,
            client_notification_url=client_notification_url,
            caller_display_name=caller_display_name,
            request_options=request_options,
        ).unwrap()

    def delete_participant(
        self,
        account_sid: str,
        conference_sid: str,
        call_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Kick a participant from a given conference

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Participant resources to delete.
            conference_sid: The SID of the conference with the participants to delete.
            call_sid: The `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ SID or label of the participant
                to delete. Non URL safe characters in a label must be percent encoded, for example, a space character is
                represented as %20.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_participant(
            account_sid, conference_sid, call_sid, request_options=request_options
        ).unwrap()

    def fetch_participant(
        self,
        account_sid: str,
        conference_sid: str,
        call_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountConferenceParticipant:
        """Fetch an instance of a participant

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Participant resource to fetch.
            conference_sid: The SID of the conference with the participant to fetch.
            call_sid: The `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ SID or label of the participant
                to fetch. Non URL safe characters in a label must be percent encoded, for example, a space character is
                represented as %20.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_participant(
            account_sid, conference_sid, call_sid, request_options=request_options
        ).unwrap()

    def list_participant(
        self,
        account_sid: str,
        conference_sid: str,
        *,
        muted: bool | None = None,
        hold: bool | None = None,
        coaching: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListParticipantResponse:
        """Retrieve a list of participants belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Participant resources to read.
            conference_sid: The SID of the conference with the participants to read.
            muted: Whether to return only participants that are muted. Can be: ``true`` or ``false``.
            hold: Whether to return only participants that are on hold. Can be: ``true`` or ``false``.
            coaching: Whether to return only participants who are coaching another call. Can be: ``true`` or ``false``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_participant(
            account_sid,
            conference_sid,
            muted=muted,
            hold=hold,
            coaching=coaching,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_participant(
        self,
        account_sid: str,
        conference_sid: str,
        call_sid: str,
        *,
        muted: bool | None = None,
        hold: bool | None = None,
        hold_url: str | None = None,
        hold_method: HoldMethodOrStr | None = None,
        announce_url: str | None = None,
        announce_method: AnnounceMethod1OrStr | None = None,
        wait_url: str | None = None,
        wait_method: WaitMethodOrStr | None = None,
        beep_on_exit: bool | None = None,
        end_conference_on_exit: bool | None = None,
        coaching: bool | None = None,
        call_sid_to_coach: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountConferenceParticipant:
        """Update the properties of the participant

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Participant resources to update.
            conference_sid: The SID of the conference with the participant to update.
            call_sid: The `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ SID or label of the participant
                to update. Non URL safe characters in a label must be percent encoded, for example, a space character is
                represented as %20.
            muted: Whether the participant should be muted. Can be ``true`` or ``false``. ``true`` will mute the
                participant, and ``false`` will un-mute them. Anything value other than ``true`` or ``false`` is
                interpreted as ``false``.
            hold: Whether the participant should be on hold. Can be: ``true`` or ``false``. ``true`` puts the
                participant on hold, and ``false`` lets them rejoin the conference.
            hold_url: The URL we call using the ``hold_method`` for music that plays when the participant is on hold.
                The URL may return an MP3 file, a WAV file, or a TwiML document that contains ``<Play>``, ``<Say>``,
                ``<Pause>``, or ``<Redirect>`` verbs.
            hold_method: The HTTP method we should use to call ``hold_url``. Can be: ``GET`` or ``POST`` and the default
                is ``GET``.
            announce_url: The URL we call using the ``announce_method`` for an announcement to the participant. The URL
                may return an MP3 file, a WAV file, or a TwiML document that contains ``<Play>``, ``<Say>``,
                ``<Pause>``, or ``<Redirect>`` verbs.
            announce_method: The HTTP method we should use to call ``announce_url``. Can be: ``GET`` or ``POST`` and
                defaults to ``POST``.
            wait_url: The URL that Twilio calls using the ``wait_method`` before the conference has started. The URL may
                return an MP3 file, a WAV file, or a TwiML document. The default value is the URL of our standard hold
                music. If you do not want anything to play while waiting for the conference to start, specify an empty
                string by setting ``wait_url`` to ``''``. For more details on the allowable verbs within the
                ``waitUrl``, see the ``waitUrl`` attribute in the
                https://www.twilio.com/docs/voice/twiml/conference#attributes-waiturl.
            wait_method: The HTTP method we should use to call ``wait_url``. Can be ``GET`` or ``POST`` and the default
                is ``POST``. When using a static audio file, this should be ``GET`` so that we can cache the file.
            beep_on_exit: Whether to play a notification beep to the conference when the participant exits. Can be:
                ``true`` or ``false``.
            end_conference_on_exit: Whether to end the conference when the participant leaves. Can be: ``true`` or
                ``false`` and defaults to ``false``.
            coaching: Whether the participant is coaching another call. Can be: ``true`` or ``false``. If not present,
                defaults to ``false`` unless ``call_sid_to_coach`` is defined. If ``true``, ``call_sid_to_coach`` must
                be defined.
            call_sid_to_coach: The SID of the participant who is being ``coached``. The participant being coached is the
                only participant who can hear the participant who is ``coaching``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_participant(
            account_sid,
            conference_sid,
            call_sid,
            muted=muted,
            hold=hold,
            hold_url=hold_url,
            hold_method=hold_method,
            announce_url=announce_url,
            announce_method=announce_method,
            wait_url=wait_url,
            wait_method=wait_method,
            beep_on_exit=beep_on_exit,
            end_conference_on_exit=end_conference_on_exit,
            coaching=coaching,
            call_sid_to_coach=call_sid_to_coach,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401ParticipantWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401Participant:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401ParticipantWithRawResponse(client, server, auth)

    async def create_participant(
        self,
        account_sid: str,
        conference_sid: str,
        from_: str,
        to: str,
        *,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod16OrStr | None = None,
        status_callback_event: list[str] | None = None,
        label: str | None = None,
        timeout: int | None = None,
        record: bool | None = None,
        muted: bool | None = None,
        beep: str | None = None,
        start_conference_on_enter: bool | None = None,
        end_conference_on_exit: bool | None = None,
        wait_url: str | None = None,
        wait_method: WaitMethodOrStr | None = None,
        early_media: bool | None = None,
        max_participants: int | None = None,
        conference_record: str | None = None,
        conference_trim: str | None = None,
        conference_status_callback: str | None = None,
        conference_status_callback_method: ConferenceStatusCallbackMethodOrStr | None = None,
        conference_status_callback_event: list[str] | None = None,
        recording_channels: str | None = None,
        recording_status_callback: str | None = None,
        recording_status_callback_method: RecordingStatusCallbackMethod2OrStr | None = None,
        sip_auth_username: str | None = None,
        sip_auth_password: str | None = None,
        region: str | None = None,
        conference_recording_status_callback: str | None = None,
        conference_recording_status_callback_method: ConferenceRecordingStatusCallbackMethodOrStr | None = None,
        recording_status_callback_event: list[str] | None = None,
        conference_recording_status_callback_event: list[str] | None = None,
        coaching: bool | None = None,
        call_sid_to_coach: str | None = None,
        jitter_buffer_size: str | None = None,
        byoc: str | None = None,
        caller_id: str | None = None,
        call_reason: str | None = None,
        recording_track: str | None = None,
        recording_configuration_id: str | None = None,
        time_limit: int | None = None,
        machine_detection: str | None = None,
        machine_detection_timeout: int | None = None,
        machine_detection_speech_threshold: int | None = None,
        machine_detection_speech_end_threshold: int | None = None,
        machine_detection_silence_timeout: int | None = None,
        amd_status_callback: str | None = None,
        amd_status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        trim: str | None = None,
        call_token: str | None = None,
        client_notification_url: str | None = None,
        caller_display_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountConferenceParticipant:
        """Conference participants

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            conference_sid: The SID of the participant's conference.
            from_: The phone number, Client identifier, or username portion of SIP address that made this call. Phone
                numbers are in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format (e.g., +16175551212).
                Client identifiers are formatted ``client:name``. If using a phone number, it must be a Twilio number or
                a Verified `outgoing caller id <https://www.twilio.com/docs/voice/api/outgoing-caller-ids>`__ for your
                account. If the ``to`` parameter is a phone number, ``from`` must also be a phone number. If ``to`` is
                sip address, this value of ``from`` should be a username portion to be used to populate the
                P-Asserted-Identity header that is passed to the SIP endpoint.
            to: The phone number, SIP address, Client, TwiML App identifier that received this call. Phone numbers are
                in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format (e.g., +16175551212). SIP addresses
                are formatted as ``sip:name@company.com``. Client identifiers are formatted ``client:name``. TwiML App
                identifiers are formatted ``app:<APP_SID>``. `Custom parameters
                <https://www.twilio.com/docs/voice/api/conference-participant-resource#custom-parameters>`__ may also be
                specified.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``GET`` and
                ``POST`` and defaults to ``POST``.
            status_callback_event: The conference state changes that should generate a call to ``status_callback``. Can
                be: ``initiated``, ``ringing``, ``answered``, and ``completed``. Separate multiple values with a space.
                The default value is ``completed``.
            label: A label for this participant. If one is supplied, it may subsequently be used to fetch, update or
                delete the participant.
            timeout: The number of seconds that we should allow the phone to ring before assuming there is no answer.
                Can be an integer between ``5`` and ``600``, inclusive. The default value is ``60``. We always add a
                5-second timeout buffer to outgoing calls, so value of 10 would result in an actual timeout that was
                closer to 15 seconds.
            record: Whether to record the participant and their conferences, including the time between conferences. Can
                be ``true`` or ``false`` and the default is ``false``.
            muted: Whether the agent is muted in the conference. Can be ``true`` or ``false`` and the default is
                ``false``.
            beep: Whether to play a notification beep to the conference when the participant joins. Can be: ``true``,
                ``false``, ``onEnter``, or ``onExit``. The default value is ``true``.
            start_conference_on_enter: Whether to start the conference when the participant joins, if it has not already
                started. Can be: ``true`` or ``false`` and the default is ``true``. If ``false`` and the conference has
                not started, the participant is muted and hears background music until another participant starts the
                conference.
            end_conference_on_exit: Whether to end the conference when the participant leaves. Can be: ``true`` or
                ``false`` and defaults to ``false``.
            wait_url: The URL that Twilio calls using the ``wait_method`` before the conference has started. The URL may
                return an MP3 file, a WAV file, or a TwiML document. The default value is the URL of our standard hold
                music. If you do not want anything to play while waiting for the conference to start, specify an empty
                string by setting ``wait_url`` to ``''``. For more details on the allowable verbs within the
                ``waitUrl``, see the ``waitUrl`` attribute in the
                https://www.twilio.com/docs/voice/twiml/conference#attributes-waiturl.
            wait_method: The HTTP method we should use to call ``wait_url``. Can be ``GET`` or ``POST`` and the default
                is ``POST``. When using a static audio file, this should be ``GET`` so that we can cache the file.
            early_media: Whether to allow an agent to hear the state of the outbound call, including ringing or
                disconnect messages. Can be: ``true`` or ``false`` and defaults to ``true``.
            max_participants: The maximum number of participants in the conference. Can be a positive integer from ``2``
                to ``250``. The default value is ``250``.
            conference_record: Whether to record the conference the participant is joining. Can be: ``true``, ``false``,
                ``record-from-start``, and ``do-not-record``. The default value is ``false``.
            conference_trim: Whether to trim leading and trailing silence from the conference recording. Can be:
                ``trim-silence`` or ``do-not-trim`` and defaults to ``trim-silence``.
            conference_status_callback: The URL we should call using the ``conference_status_callback_method`` when the
                conference events in ``conference_status_callback_event`` occur. Only the value set by the first
                participant to join the conference is used. Subsequent ``conference_status_callback`` values are
                ignored.
            conference_status_callback_method: The HTTP method we should use to call ``conference_status_callback``. Can
                be: ``GET`` or ``POST`` and defaults to ``POST``.
            conference_status_callback_event: The conference state changes that should generate a call to
                ``conference_status_callback``. Can be: ``start``, ``end``, ``join``, ``leave``, ``mute``, ``hold``,
                ``modify``, ``speaker``, and ``announcement``. Separate multiple values with a space. Defaults to
                ``start end``.
            recording_channels: The recording channels for the final recording. Can be: ``mono`` or ``dual`` and the
                default is ``mono``.
            recording_status_callback: The URL that we should call using the ``recording_status_callback_method`` when
                the recording status changes.
            recording_status_callback_method: The HTTP method we should use when we call ``recording_status_callback``.
                Can be: ``GET`` or ``POST`` and defaults to ``POST``.
            sip_auth_username: The SIP username used for authentication.
            sip_auth_password: The SIP password for authentication.
            region: The `region
                <https://support.twilio.com/hc/en-us/articles/223132167-How-global-low-latency-routing-and-region-selection-work-for-conferences-and-Client-calls>`__
                where we should mix the recorded audio. Can be:``us1``, ``us2``, ``ie1``, ``de1``, ``sg1``, ``br1``,
                ``au1``, or ``jp1``.
            conference_recording_status_callback: The URL we should call using the
                ``conference_recording_status_callback_method`` when the conference recording is available.
            conference_recording_status_callback_method: The HTTP method we should use to call
                ``conference_recording_status_callback``. Can be: ``GET`` or ``POST`` and defaults to ``POST``.
            recording_status_callback_event: The recording state changes that should generate a call to
                ``recording_status_callback``. Can be: ``started``, ``in-progress``, ``paused``, ``resumed``,
                ``stopped``, ``completed``, ``failed``, and ``absent``. Separate multiple values with a space, ex:
                ``'in-progress completed failed'``.
            conference_recording_status_callback_event: The conference recording state changes that generate a call to
                ``conference_recording_status_callback``. Can be: ``in-progress``, ``completed``, ``failed``, and
                ``absent``. Separate multiple values with a space, ex: ``'in-progress completed failed'``
            coaching: Whether the participant is coaching another call. Can be: ``true`` or ``false``. If not present,
                defaults to ``false`` unless ``call_sid_to_coach`` is defined. If ``true``, ``call_sid_to_coach`` must
                be defined.
            call_sid_to_coach: The SID of the participant who is being ``coached``. The participant being coached is the
                only participant who can hear the participant who is ``coaching``.
            jitter_buffer_size: Jitter buffer size for the connecting participant. Twilio will use this setting to apply
                Jitter Buffer before participant's audio is mixed into the conference. Can be: ``off``, ``small``,
                ``medium``, and ``large``. Default to ``large``.
            byoc: The SID of a BYOC (Bring Your Own Carrier) trunk to route this call with. Note that ``byoc`` is only
                meaningful when ``to`` is a phone number; it will otherwise be ignored. (Beta)
            caller_id: The phone number, Client identifier, or username portion of SIP address that made this call.
                Phone numbers are in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format (e.g.,
                +16175551212). Client identifiers are formatted ``client:name``. If using a phone number, it must be a
                Twilio number or a Verified `outgoing caller id
                <https://www.twilio.com/docs/voice/api/outgoing-caller-ids>`__ for your account. If the ``to`` parameter
                is a phone number, ``callerId`` must also be a phone number. If ``to`` is sip address, this value of
                ``callerId`` should be a username portion to be used to populate the From header that is passed to the
                SIP endpoint.
            call_reason: The Reason for the outgoing call. Use it to specify the purpose of the call that is presented
                on the called party's phone. (Branded Calls Beta)
            recording_track: The audio track to record for the call. Can be: ``inbound``, ``outbound`` or ``both``. The
                default is ``both``. ``inbound`` records the audio that is received by Twilio. ``outbound`` records the
                audio that is sent from Twilio. ``both`` records the audio that is received and sent by Twilio.
            recording_configuration_id: The identifier of the configuration to be used when creating and processing the
                recording
            time_limit: The maximum duration of the call in seconds. Constraints depend on account and configuration.
            machine_detection: Whether to detect if a human, answering machine, or fax has picked up the call. Can be:
                ``Enable`` or ``DetectMessageEnd``. Use ``Enable`` if you would like us to return ``AnsweredBy`` as soon
                as the called party is identified. Use ``DetectMessageEnd``, if you would like to leave a message on an
                answering machine. For more information, see `Answering Machine Detection
                <https://www.twilio.com/docs/voice/answering-machine-detection>`__.
            machine_detection_timeout: The number of seconds that we should attempt to detect an answering machine
                before timing out and sending a voice request with ``AnsweredBy`` of ``unknown``. The default timeout is
                30 seconds.
            machine_detection_speech_threshold: The number of milliseconds that is used as the measuring stick for the
                length of the speech activity, where durations lower than this value will be interpreted as a human and
                longer than this value as a machine. Possible Values: 1000-6000. Default: 2400.
            machine_detection_speech_end_threshold: The number of milliseconds of silence after speech activity at which
                point the speech activity is considered complete. Possible Values: 500-5000. Default: 1200.
            machine_detection_silence_timeout: The number of milliseconds of initial silence after which an ``unknown``
                AnsweredBy result will be returned. Possible Values: 2000-10000. Default: 5000.
            amd_status_callback: The URL that we should call using the ``amd_status_callback_method`` to notify customer
                application whether the call was answered by human, machine or fax.
            amd_status_callback_method: The HTTP method we should use when calling the ``amd_status_callback`` URL. Can
                be: ``GET`` or ``POST`` and the default is ``POST``.
            trim: Whether to trim any leading and trailing silence from the participant recording. Can be:
                ``trim-silence`` or ``do-not-trim`` and the default is ``trim-silence``.
            call_token: A token string needed to invoke a forwarded call. A call_token is generated when an incoming
                call is received on a Twilio number. Pass an incoming call's call_token value to a forwarded call via
                the call_token parameter when creating a new call. A forwarded call should bear the same CallerID of the
                original incoming call.
            client_notification_url: The URL that we should use to deliver ``push call notification``.
            caller_display_name: The name that populates the display name in the From header. Must be between 2 and 255
                characters. Only applicable for calls to sip address.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_participant(
                account_sid,
                conference_sid,
                from_,
                to,
                status_callback=status_callback,
                status_callback_method=status_callback_method,
                status_callback_event=status_callback_event,
                label=label,
                timeout=timeout,
                record=record,
                muted=muted,
                beep=beep,
                start_conference_on_enter=start_conference_on_enter,
                end_conference_on_exit=end_conference_on_exit,
                wait_url=wait_url,
                wait_method=wait_method,
                early_media=early_media,
                max_participants=max_participants,
                conference_record=conference_record,
                conference_trim=conference_trim,
                conference_status_callback=conference_status_callback,
                conference_status_callback_method=conference_status_callback_method,
                conference_status_callback_event=conference_status_callback_event,
                recording_channels=recording_channels,
                recording_status_callback=recording_status_callback,
                recording_status_callback_method=recording_status_callback_method,
                sip_auth_username=sip_auth_username,
                sip_auth_password=sip_auth_password,
                region=region,
                conference_recording_status_callback=conference_recording_status_callback,
                conference_recording_status_callback_method=conference_recording_status_callback_method,
                recording_status_callback_event=recording_status_callback_event,
                conference_recording_status_callback_event=conference_recording_status_callback_event,
                coaching=coaching,
                call_sid_to_coach=call_sid_to_coach,
                jitter_buffer_size=jitter_buffer_size,
                byoc=byoc,
                caller_id=caller_id,
                call_reason=call_reason,
                recording_track=recording_track,
                recording_configuration_id=recording_configuration_id,
                time_limit=time_limit,
                machine_detection=machine_detection,
                machine_detection_timeout=machine_detection_timeout,
                machine_detection_speech_threshold=machine_detection_speech_threshold,
                machine_detection_speech_end_threshold=machine_detection_speech_end_threshold,
                machine_detection_silence_timeout=machine_detection_silence_timeout,
                amd_status_callback=amd_status_callback,
                amd_status_callback_method=amd_status_callback_method,
                trim=trim,
                call_token=call_token,
                client_notification_url=client_notification_url,
                caller_display_name=caller_display_name,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_participant(
        self,
        account_sid: str,
        conference_sid: str,
        call_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Kick a participant from a given conference

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Participant resources to delete.
            conference_sid: The SID of the conference with the participants to delete.
            call_sid: The `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ SID or label of the participant
                to delete. Non URL safe characters in a label must be percent encoded, for example, a space character is
                represented as %20.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_participant(
                account_sid, conference_sid, call_sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_participant(
        self,
        account_sid: str,
        conference_sid: str,
        call_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountConferenceParticipant:
        """Fetch an instance of a participant

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Participant resource to fetch.
            conference_sid: The SID of the conference with the participant to fetch.
            call_sid: The `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ SID or label of the participant
                to fetch. Non URL safe characters in a label must be percent encoded, for example, a space character is
                represented as %20.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_participant(
                account_sid, conference_sid, call_sid, request_options=request_options
            )
        ).unwrap()

    async def list_participant(
        self,
        account_sid: str,
        conference_sid: str,
        *,
        muted: bool | None = None,
        hold: bool | None = None,
        coaching: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListParticipantResponse:
        """Retrieve a list of participants belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Participant resources to read.
            conference_sid: The SID of the conference with the participants to read.
            muted: Whether to return only participants that are muted. Can be: ``true`` or ``false``.
            hold: Whether to return only participants that are on hold. Can be: ``true`` or ``false``.
            coaching: Whether to return only participants who are coaching another call. Can be: ``true`` or ``false``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_participant(
                account_sid,
                conference_sid,
                muted=muted,
                hold=hold,
                coaching=coaching,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_participant(
        self,
        account_sid: str,
        conference_sid: str,
        call_sid: str,
        *,
        muted: bool | None = None,
        hold: bool | None = None,
        hold_url: str | None = None,
        hold_method: HoldMethodOrStr | None = None,
        announce_url: str | None = None,
        announce_method: AnnounceMethod1OrStr | None = None,
        wait_url: str | None = None,
        wait_method: WaitMethodOrStr | None = None,
        beep_on_exit: bool | None = None,
        end_conference_on_exit: bool | None = None,
        coaching: bool | None = None,
        call_sid_to_coach: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountConferenceParticipant:
        """Update the properties of the participant

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Participant resources to update.
            conference_sid: The SID of the conference with the participant to update.
            call_sid: The `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ SID or label of the participant
                to update. Non URL safe characters in a label must be percent encoded, for example, a space character is
                represented as %20.
            muted: Whether the participant should be muted. Can be ``true`` or ``false``. ``true`` will mute the
                participant, and ``false`` will un-mute them. Anything value other than ``true`` or ``false`` is
                interpreted as ``false``.
            hold: Whether the participant should be on hold. Can be: ``true`` or ``false``. ``true`` puts the
                participant on hold, and ``false`` lets them rejoin the conference.
            hold_url: The URL we call using the ``hold_method`` for music that plays when the participant is on hold.
                The URL may return an MP3 file, a WAV file, or a TwiML document that contains ``<Play>``, ``<Say>``,
                ``<Pause>``, or ``<Redirect>`` verbs.
            hold_method: The HTTP method we should use to call ``hold_url``. Can be: ``GET`` or ``POST`` and the default
                is ``GET``.
            announce_url: The URL we call using the ``announce_method`` for an announcement to the participant. The URL
                may return an MP3 file, a WAV file, or a TwiML document that contains ``<Play>``, ``<Say>``,
                ``<Pause>``, or ``<Redirect>`` verbs.
            announce_method: The HTTP method we should use to call ``announce_url``. Can be: ``GET`` or ``POST`` and
                defaults to ``POST``.
            wait_url: The URL that Twilio calls using the ``wait_method`` before the conference has started. The URL may
                return an MP3 file, a WAV file, or a TwiML document. The default value is the URL of our standard hold
                music. If you do not want anything to play while waiting for the conference to start, specify an empty
                string by setting ``wait_url`` to ``''``. For more details on the allowable verbs within the
                ``waitUrl``, see the ``waitUrl`` attribute in the
                https://www.twilio.com/docs/voice/twiml/conference#attributes-waiturl.
            wait_method: The HTTP method we should use to call ``wait_url``. Can be ``GET`` or ``POST`` and the default
                is ``POST``. When using a static audio file, this should be ``GET`` so that we can cache the file.
            beep_on_exit: Whether to play a notification beep to the conference when the participant exits. Can be:
                ``true`` or ``false``.
            end_conference_on_exit: Whether to end the conference when the participant leaves. Can be: ``true`` or
                ``false`` and defaults to ``false``.
            coaching: Whether the participant is coaching another call. Can be: ``true`` or ``false``. If not present,
                defaults to ``false`` unless ``call_sid_to_coach`` is defined. If ``true``, ``call_sid_to_coach`` must
                be defined.
            call_sid_to_coach: The SID of the participant who is being ``coached``. The participant being coached is the
                only participant who can hear the participant who is ``coaching``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_participant(
                account_sid,
                conference_sid,
                call_sid,
                muted=muted,
                hold=hold,
                hold_url=hold_url,
                hold_method=hold_method,
                announce_url=announce_url,
                announce_method=announce_method,
                wait_url=wait_url,
                wait_method=wait_method,
                beep_on_exit=beep_on_exit,
                end_conference_on_exit=end_conference_on_exit,
                coaching=coaching,
                call_sid_to_coach=call_sid_to_coach,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401ParticipantWithRawResponse:
        return self._with_raw_response


class Api20100401ParticipantWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_participant(
        self,
        account_sid: str,
        conference_sid: str,
        from_: str,
        to: str,
        *,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod16OrStr | None = None,
        status_callback_event: list[str] | None = None,
        label: str | None = None,
        timeout: int | None = None,
        record: bool | None = None,
        muted: bool | None = None,
        beep: str | None = None,
        start_conference_on_enter: bool | None = None,
        end_conference_on_exit: bool | None = None,
        wait_url: str | None = None,
        wait_method: WaitMethodOrStr | None = None,
        early_media: bool | None = None,
        max_participants: int | None = None,
        conference_record: str | None = None,
        conference_trim: str | None = None,
        conference_status_callback: str | None = None,
        conference_status_callback_method: ConferenceStatusCallbackMethodOrStr | None = None,
        conference_status_callback_event: list[str] | None = None,
        recording_channels: str | None = None,
        recording_status_callback: str | None = None,
        recording_status_callback_method: RecordingStatusCallbackMethod2OrStr | None = None,
        sip_auth_username: str | None = None,
        sip_auth_password: str | None = None,
        region: str | None = None,
        conference_recording_status_callback: str | None = None,
        conference_recording_status_callback_method: ConferenceRecordingStatusCallbackMethodOrStr | None = None,
        recording_status_callback_event: list[str] | None = None,
        conference_recording_status_callback_event: list[str] | None = None,
        coaching: bool | None = None,
        call_sid_to_coach: str | None = None,
        jitter_buffer_size: str | None = None,
        byoc: str | None = None,
        caller_id: str | None = None,
        call_reason: str | None = None,
        recording_track: str | None = None,
        recording_configuration_id: str | None = None,
        time_limit: int | None = None,
        machine_detection: str | None = None,
        machine_detection_timeout: int | None = None,
        machine_detection_speech_threshold: int | None = None,
        machine_detection_speech_end_threshold: int | None = None,
        machine_detection_silence_timeout: int | None = None,
        amd_status_callback: str | None = None,
        amd_status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        trim: str | None = None,
        call_token: str | None = None,
        client_notification_url: str | None = None,
        caller_display_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountConferenceParticipant, RawError]:
        """Conference participants

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            conference_sid: The SID of the participant's conference.
            from_: The phone number, Client identifier, or username portion of SIP address that made this call. Phone
                numbers are in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format (e.g., +16175551212).
                Client identifiers are formatted ``client:name``. If using a phone number, it must be a Twilio number or
                a Verified `outgoing caller id <https://www.twilio.com/docs/voice/api/outgoing-caller-ids>`__ for your
                account. If the ``to`` parameter is a phone number, ``from`` must also be a phone number. If ``to`` is
                sip address, this value of ``from`` should be a username portion to be used to populate the
                P-Asserted-Identity header that is passed to the SIP endpoint.
            to: The phone number, SIP address, Client, TwiML App identifier that received this call. Phone numbers are
                in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format (e.g., +16175551212). SIP addresses
                are formatted as ``sip:name@company.com``. Client identifiers are formatted ``client:name``. TwiML App
                identifiers are formatted ``app:<APP_SID>``. `Custom parameters
                <https://www.twilio.com/docs/voice/api/conference-participant-resource#custom-parameters>`__ may also be
                specified.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``GET`` and
                ``POST`` and defaults to ``POST``.
            status_callback_event: The conference state changes that should generate a call to ``status_callback``. Can
                be: ``initiated``, ``ringing``, ``answered``, and ``completed``. Separate multiple values with a space.
                The default value is ``completed``.
            label: A label for this participant. If one is supplied, it may subsequently be used to fetch, update or
                delete the participant.
            timeout: The number of seconds that we should allow the phone to ring before assuming there is no answer.
                Can be an integer between ``5`` and ``600``, inclusive. The default value is ``60``. We always add a
                5-second timeout buffer to outgoing calls, so value of 10 would result in an actual timeout that was
                closer to 15 seconds.
            record: Whether to record the participant and their conferences, including the time between conferences. Can
                be ``true`` or ``false`` and the default is ``false``.
            muted: Whether the agent is muted in the conference. Can be ``true`` or ``false`` and the default is
                ``false``.
            beep: Whether to play a notification beep to the conference when the participant joins. Can be: ``true``,
                ``false``, ``onEnter``, or ``onExit``. The default value is ``true``.
            start_conference_on_enter: Whether to start the conference when the participant joins, if it has not already
                started. Can be: ``true`` or ``false`` and the default is ``true``. If ``false`` and the conference has
                not started, the participant is muted and hears background music until another participant starts the
                conference.
            end_conference_on_exit: Whether to end the conference when the participant leaves. Can be: ``true`` or
                ``false`` and defaults to ``false``.
            wait_url: The URL that Twilio calls using the ``wait_method`` before the conference has started. The URL may
                return an MP3 file, a WAV file, or a TwiML document. The default value is the URL of our standard hold
                music. If you do not want anything to play while waiting for the conference to start, specify an empty
                string by setting ``wait_url`` to ``''``. For more details on the allowable verbs within the
                ``waitUrl``, see the ``waitUrl`` attribute in the
                https://www.twilio.com/docs/voice/twiml/conference#attributes-waiturl.
            wait_method: The HTTP method we should use to call ``wait_url``. Can be ``GET`` or ``POST`` and the default
                is ``POST``. When using a static audio file, this should be ``GET`` so that we can cache the file.
            early_media: Whether to allow an agent to hear the state of the outbound call, including ringing or
                disconnect messages. Can be: ``true`` or ``false`` and defaults to ``true``.
            max_participants: The maximum number of participants in the conference. Can be a positive integer from ``2``
                to ``250``. The default value is ``250``.
            conference_record: Whether to record the conference the participant is joining. Can be: ``true``, ``false``,
                ``record-from-start``, and ``do-not-record``. The default value is ``false``.
            conference_trim: Whether to trim leading and trailing silence from the conference recording. Can be:
                ``trim-silence`` or ``do-not-trim`` and defaults to ``trim-silence``.
            conference_status_callback: The URL we should call using the ``conference_status_callback_method`` when the
                conference events in ``conference_status_callback_event`` occur. Only the value set by the first
                participant to join the conference is used. Subsequent ``conference_status_callback`` values are
                ignored.
            conference_status_callback_method: The HTTP method we should use to call ``conference_status_callback``. Can
                be: ``GET`` or ``POST`` and defaults to ``POST``.
            conference_status_callback_event: The conference state changes that should generate a call to
                ``conference_status_callback``. Can be: ``start``, ``end``, ``join``, ``leave``, ``mute``, ``hold``,
                ``modify``, ``speaker``, and ``announcement``. Separate multiple values with a space. Defaults to
                ``start end``.
            recording_channels: The recording channels for the final recording. Can be: ``mono`` or ``dual`` and the
                default is ``mono``.
            recording_status_callback: The URL that we should call using the ``recording_status_callback_method`` when
                the recording status changes.
            recording_status_callback_method: The HTTP method we should use when we call ``recording_status_callback``.
                Can be: ``GET`` or ``POST`` and defaults to ``POST``.
            sip_auth_username: The SIP username used for authentication.
            sip_auth_password: The SIP password for authentication.
            region: The `region
                <https://support.twilio.com/hc/en-us/articles/223132167-How-global-low-latency-routing-and-region-selection-work-for-conferences-and-Client-calls>`__
                where we should mix the recorded audio. Can be:``us1``, ``us2``, ``ie1``, ``de1``, ``sg1``, ``br1``,
                ``au1``, or ``jp1``.
            conference_recording_status_callback: The URL we should call using the
                ``conference_recording_status_callback_method`` when the conference recording is available.
            conference_recording_status_callback_method: The HTTP method we should use to call
                ``conference_recording_status_callback``. Can be: ``GET`` or ``POST`` and defaults to ``POST``.
            recording_status_callback_event: The recording state changes that should generate a call to
                ``recording_status_callback``. Can be: ``started``, ``in-progress``, ``paused``, ``resumed``,
                ``stopped``, ``completed``, ``failed``, and ``absent``. Separate multiple values with a space, ex:
                ``'in-progress completed failed'``.
            conference_recording_status_callback_event: The conference recording state changes that generate a call to
                ``conference_recording_status_callback``. Can be: ``in-progress``, ``completed``, ``failed``, and
                ``absent``. Separate multiple values with a space, ex: ``'in-progress completed failed'``
            coaching: Whether the participant is coaching another call. Can be: ``true`` or ``false``. If not present,
                defaults to ``false`` unless ``call_sid_to_coach`` is defined. If ``true``, ``call_sid_to_coach`` must
                be defined.
            call_sid_to_coach: The SID of the participant who is being ``coached``. The participant being coached is the
                only participant who can hear the participant who is ``coaching``.
            jitter_buffer_size: Jitter buffer size for the connecting participant. Twilio will use this setting to apply
                Jitter Buffer before participant's audio is mixed into the conference. Can be: ``off``, ``small``,
                ``medium``, and ``large``. Default to ``large``.
            byoc: The SID of a BYOC (Bring Your Own Carrier) trunk to route this call with. Note that ``byoc`` is only
                meaningful when ``to`` is a phone number; it will otherwise be ignored. (Beta)
            caller_id: The phone number, Client identifier, or username portion of SIP address that made this call.
                Phone numbers are in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format (e.g.,
                +16175551212). Client identifiers are formatted ``client:name``. If using a phone number, it must be a
                Twilio number or a Verified `outgoing caller id
                <https://www.twilio.com/docs/voice/api/outgoing-caller-ids>`__ for your account. If the ``to`` parameter
                is a phone number, ``callerId`` must also be a phone number. If ``to`` is sip address, this value of
                ``callerId`` should be a username portion to be used to populate the From header that is passed to the
                SIP endpoint.
            call_reason: The Reason for the outgoing call. Use it to specify the purpose of the call that is presented
                on the called party's phone. (Branded Calls Beta)
            recording_track: The audio track to record for the call. Can be: ``inbound``, ``outbound`` or ``both``. The
                default is ``both``. ``inbound`` records the audio that is received by Twilio. ``outbound`` records the
                audio that is sent from Twilio. ``both`` records the audio that is received and sent by Twilio.
            recording_configuration_id: The identifier of the configuration to be used when creating and processing the
                recording
            time_limit: The maximum duration of the call in seconds. Constraints depend on account and configuration.
            machine_detection: Whether to detect if a human, answering machine, or fax has picked up the call. Can be:
                ``Enable`` or ``DetectMessageEnd``. Use ``Enable`` if you would like us to return ``AnsweredBy`` as soon
                as the called party is identified. Use ``DetectMessageEnd``, if you would like to leave a message on an
                answering machine. For more information, see `Answering Machine Detection
                <https://www.twilio.com/docs/voice/answering-machine-detection>`__.
            machine_detection_timeout: The number of seconds that we should attempt to detect an answering machine
                before timing out and sending a voice request with ``AnsweredBy`` of ``unknown``. The default timeout is
                30 seconds.
            machine_detection_speech_threshold: The number of milliseconds that is used as the measuring stick for the
                length of the speech activity, where durations lower than this value will be interpreted as a human and
                longer than this value as a machine. Possible Values: 1000-6000. Default: 2400.
            machine_detection_speech_end_threshold: The number of milliseconds of silence after speech activity at which
                point the speech activity is considered complete. Possible Values: 500-5000. Default: 1200.
            machine_detection_silence_timeout: The number of milliseconds of initial silence after which an ``unknown``
                AnsweredBy result will be returned. Possible Values: 2000-10000. Default: 5000.
            amd_status_callback: The URL that we should call using the ``amd_status_callback_method`` to notify customer
                application whether the call was answered by human, machine or fax.
            amd_status_callback_method: The HTTP method we should use when calling the ``amd_status_callback`` URL. Can
                be: ``GET`` or ``POST`` and the default is ``POST``.
            trim: Whether to trim any leading and trailing silence from the participant recording. Can be:
                ``trim-silence`` or ``do-not-trim`` and the default is ``trim-silence``.
            call_token: A token string needed to invoke a forwarded call. A call_token is generated when an incoming
                call is received on a Twilio number. Pass an incoming call's call_token value to a forwarded call via
                the call_token parameter when creating a new call. A forwarded call should bear the same CallerID of the
                original incoming call.
            client_notification_url: The URL that we should use to deliver ``push call notification``.
            caller_display_name: The name that populates the display name in the From header. Must be between 2 and 255
                characters. Only applicable for calls to sip address.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("ConferenceSid", conference_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("From", from_),
                    param[str]("To", to),
                    param[str | None]("StatusCallback", status_callback),
                    param[StatusCallbackMethod16OrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[list[str] | None]("StatusCallbackEvent", status_callback_event),
                    param[str | None]("Label", label),
                    param[int | None]("Timeout", timeout),
                    param[bool | None]("Record", record),
                    param[bool | None]("Muted", muted),
                    param[str | None]("Beep", beep),
                    param[bool | None]("StartConferenceOnEnter", start_conference_on_enter),
                    param[bool | None]("EndConferenceOnExit", end_conference_on_exit),
                    param[str | None]("WaitUrl", wait_url),
                    param[WaitMethodOrStr | None]("WaitMethod", wait_method),
                    param[bool | None]("EarlyMedia", early_media),
                    param[int | None]("MaxParticipants", max_participants),
                    param[str | None]("ConferenceRecord", conference_record),
                    param[str | None]("ConferenceTrim", conference_trim),
                    param[str | None]("ConferenceStatusCallback", conference_status_callback),
                    param[ConferenceStatusCallbackMethodOrStr | None](
                        "ConferenceStatusCallbackMethod", conference_status_callback_method
                    ),
                    param[list[str] | None]("ConferenceStatusCallbackEvent", conference_status_callback_event),
                    param[str | None]("RecordingChannels", recording_channels),
                    param[str | None]("RecordingStatusCallback", recording_status_callback),
                    param[RecordingStatusCallbackMethod2OrStr | None](
                        "RecordingStatusCallbackMethod", recording_status_callback_method
                    ),
                    param[str | None]("SipAuthUsername", sip_auth_username),
                    param[str | None]("SipAuthPassword", sip_auth_password),
                    param[str | None]("Region", region),
                    param[str | None]("ConferenceRecordingStatusCallback", conference_recording_status_callback),
                    param[ConferenceRecordingStatusCallbackMethodOrStr | None](
                        "ConferenceRecordingStatusCallbackMethod", conference_recording_status_callback_method
                    ),
                    param[list[str] | None]("RecordingStatusCallbackEvent", recording_status_callback_event),
                    param[list[str] | None](
                        "ConferenceRecordingStatusCallbackEvent", conference_recording_status_callback_event
                    ),
                    param[bool | None]("Coaching", coaching),
                    param[str | None]("CallSidToCoach", call_sid_to_coach),
                    param[str | None]("JitterBufferSize", jitter_buffer_size),
                    param[str | None]("Byoc", byoc),
                    param[str | None]("CallerId", caller_id),
                    param[str | None]("CallReason", call_reason),
                    param[str | None]("RecordingTrack", recording_track),
                    param[str | None]("RecordingConfigurationId", recording_configuration_id),
                    param[int | None]("TimeLimit", time_limit),
                    param[str | None]("MachineDetection", machine_detection),
                    param[int | None]("MachineDetectionTimeout", machine_detection_timeout),
                    param[int | None]("MachineDetectionSpeechThreshold", machine_detection_speech_threshold),
                    param[int | None]("MachineDetectionSpeechEndThreshold", machine_detection_speech_end_threshold),
                    param[int | None]("MachineDetectionSilenceTimeout", machine_detection_silence_timeout),
                    param[str | None]("AmdStatusCallback", amd_status_callback),
                    param[AmdStatusCallbackMethodOrStr | None]("AmdStatusCallbackMethod", amd_status_callback_method),
                    param[str | None]("Trim", trim),
                    param[str | None]("CallToken", call_token),
                    param[str | None]("ClientNotificationUrl", client_notification_url),
                    param[str | None]("CallerDisplayName", caller_display_name),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountConferenceParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_participant(
        self,
        account_sid: str,
        conference_sid: str,
        call_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Kick a participant from a given conference

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Participant resources to delete.
            conference_sid: The SID of the conference with the participants to delete.
            call_sid: The `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ SID or label of the participant
                to delete. Non URL safe characters in a label must be percent encoded, for example, a space character is
                represented as %20.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("ConferenceSid", conference_sid),
                param[str]("CallSid", call_sid),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_participant(
        self,
        account_sid: str,
        conference_sid: str,
        call_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountConferenceParticipant, RawError]:
        """Fetch an instance of a participant

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Participant resource to fetch.
            conference_sid: The SID of the conference with the participant to fetch.
            call_sid: The `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ SID or label of the participant
                to fetch. Non URL safe characters in a label must be percent encoded, for example, a space character is
                represented as %20.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("ConferenceSid", conference_sid),
                param[str]("CallSid", call_sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountConferenceParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_participant(
        self,
        account_sid: str,
        conference_sid: str,
        *,
        muted: bool | None = None,
        hold: bool | None = None,
        coaching: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListParticipantResponse, RawError]:
        """Retrieve a list of participants belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Participant resources to read.
            conference_sid: The SID of the conference with the participants to read.
            muted: Whether to return only participants that are muted. Can be: ``true`` or ``false``.
            hold: Whether to return only participants that are on hold. Can be: ``true`` or ``false``.
            coaching: Whether to return only participants who are coaching another call. Can be: ``true`` or ``false``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("ConferenceSid", conference_sid)],
            query_params=[
                param[bool | None]("Muted", muted),
                param[bool | None]("Hold", hold),
                param[bool | None]("Coaching", coaching),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListParticipantResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_participant(
        self,
        account_sid: str,
        conference_sid: str,
        call_sid: str,
        *,
        muted: bool | None = None,
        hold: bool | None = None,
        hold_url: str | None = None,
        hold_method: HoldMethodOrStr | None = None,
        announce_url: str | None = None,
        announce_method: AnnounceMethod1OrStr | None = None,
        wait_url: str | None = None,
        wait_method: WaitMethodOrStr | None = None,
        beep_on_exit: bool | None = None,
        end_conference_on_exit: bool | None = None,
        coaching: bool | None = None,
        call_sid_to_coach: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountConferenceParticipant, RawError]:
        """Update the properties of the participant

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Participant resources to update.
            conference_sid: The SID of the conference with the participant to update.
            call_sid: The `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ SID or label of the participant
                to update. Non URL safe characters in a label must be percent encoded, for example, a space character is
                represented as %20.
            muted: Whether the participant should be muted. Can be ``true`` or ``false``. ``true`` will mute the
                participant, and ``false`` will un-mute them. Anything value other than ``true`` or ``false`` is
                interpreted as ``false``.
            hold: Whether the participant should be on hold. Can be: ``true`` or ``false``. ``true`` puts the
                participant on hold, and ``false`` lets them rejoin the conference.
            hold_url: The URL we call using the ``hold_method`` for music that plays when the participant is on hold.
                The URL may return an MP3 file, a WAV file, or a TwiML document that contains ``<Play>``, ``<Say>``,
                ``<Pause>``, or ``<Redirect>`` verbs.
            hold_method: The HTTP method we should use to call ``hold_url``. Can be: ``GET`` or ``POST`` and the default
                is ``GET``.
            announce_url: The URL we call using the ``announce_method`` for an announcement to the participant. The URL
                may return an MP3 file, a WAV file, or a TwiML document that contains ``<Play>``, ``<Say>``,
                ``<Pause>``, or ``<Redirect>`` verbs.
            announce_method: The HTTP method we should use to call ``announce_url``. Can be: ``GET`` or ``POST`` and
                defaults to ``POST``.
            wait_url: The URL that Twilio calls using the ``wait_method`` before the conference has started. The URL may
                return an MP3 file, a WAV file, or a TwiML document. The default value is the URL of our standard hold
                music. If you do not want anything to play while waiting for the conference to start, specify an empty
                string by setting ``wait_url`` to ``''``. For more details on the allowable verbs within the
                ``waitUrl``, see the ``waitUrl`` attribute in the
                https://www.twilio.com/docs/voice/twiml/conference#attributes-waiturl.
            wait_method: The HTTP method we should use to call ``wait_url``. Can be ``GET`` or ``POST`` and the default
                is ``POST``. When using a static audio file, this should be ``GET`` so that we can cache the file.
            beep_on_exit: Whether to play a notification beep to the conference when the participant exits. Can be:
                ``true`` or ``false``.
            end_conference_on_exit: Whether to end the conference when the participant leaves. Can be: ``true`` or
                ``false`` and defaults to ``false``.
            coaching: Whether the participant is coaching another call. Can be: ``true`` or ``false``. If not present,
                defaults to ``false`` unless ``call_sid_to_coach`` is defined. If ``true``, ``call_sid_to_coach`` must
                be defined.
            call_sid_to_coach: The SID of the participant who is being ``coached``. The participant being coached is the
                only participant who can hear the participant who is ``coaching``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("ConferenceSid", conference_sid),
                param[str]("CallSid", call_sid),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[bool | None]("Muted", muted),
                    param[bool | None]("Hold", hold),
                    param[str | None]("HoldUrl", hold_url),
                    param[HoldMethodOrStr | None]("HoldMethod", hold_method),
                    param[str | None]("AnnounceUrl", announce_url),
                    param[AnnounceMethod1OrStr | None]("AnnounceMethod", announce_method),
                    param[str | None]("WaitUrl", wait_url),
                    param[WaitMethodOrStr | None]("WaitMethod", wait_method),
                    param[bool | None]("BeepOnExit", beep_on_exit),
                    param[bool | None]("EndConferenceOnExit", end_conference_on_exit),
                    param[bool | None]("Coaching", coaching),
                    param[str | None]("CallSidToCoach", call_sid_to_coach),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountConferenceParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401ParticipantWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_participant(
        self,
        account_sid: str,
        conference_sid: str,
        from_: str,
        to: str,
        *,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod16OrStr | None = None,
        status_callback_event: list[str] | None = None,
        label: str | None = None,
        timeout: int | None = None,
        record: bool | None = None,
        muted: bool | None = None,
        beep: str | None = None,
        start_conference_on_enter: bool | None = None,
        end_conference_on_exit: bool | None = None,
        wait_url: str | None = None,
        wait_method: WaitMethodOrStr | None = None,
        early_media: bool | None = None,
        max_participants: int | None = None,
        conference_record: str | None = None,
        conference_trim: str | None = None,
        conference_status_callback: str | None = None,
        conference_status_callback_method: ConferenceStatusCallbackMethodOrStr | None = None,
        conference_status_callback_event: list[str] | None = None,
        recording_channels: str | None = None,
        recording_status_callback: str | None = None,
        recording_status_callback_method: RecordingStatusCallbackMethod2OrStr | None = None,
        sip_auth_username: str | None = None,
        sip_auth_password: str | None = None,
        region: str | None = None,
        conference_recording_status_callback: str | None = None,
        conference_recording_status_callback_method: ConferenceRecordingStatusCallbackMethodOrStr | None = None,
        recording_status_callback_event: list[str] | None = None,
        conference_recording_status_callback_event: list[str] | None = None,
        coaching: bool | None = None,
        call_sid_to_coach: str | None = None,
        jitter_buffer_size: str | None = None,
        byoc: str | None = None,
        caller_id: str | None = None,
        call_reason: str | None = None,
        recording_track: str | None = None,
        recording_configuration_id: str | None = None,
        time_limit: int | None = None,
        machine_detection: str | None = None,
        machine_detection_timeout: int | None = None,
        machine_detection_speech_threshold: int | None = None,
        machine_detection_speech_end_threshold: int | None = None,
        machine_detection_silence_timeout: int | None = None,
        amd_status_callback: str | None = None,
        amd_status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        trim: str | None = None,
        call_token: str | None = None,
        client_notification_url: str | None = None,
        caller_display_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountConferenceParticipant, RawError]:
        """Conference participants

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            conference_sid: The SID of the participant's conference.
            from_: The phone number, Client identifier, or username portion of SIP address that made this call. Phone
                numbers are in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format (e.g., +16175551212).
                Client identifiers are formatted ``client:name``. If using a phone number, it must be a Twilio number or
                a Verified `outgoing caller id <https://www.twilio.com/docs/voice/api/outgoing-caller-ids>`__ for your
                account. If the ``to`` parameter is a phone number, ``from`` must also be a phone number. If ``to`` is
                sip address, this value of ``from`` should be a username portion to be used to populate the
                P-Asserted-Identity header that is passed to the SIP endpoint.
            to: The phone number, SIP address, Client, TwiML App identifier that received this call. Phone numbers are
                in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format (e.g., +16175551212). SIP addresses
                are formatted as ``sip:name@company.com``. Client identifiers are formatted ``client:name``. TwiML App
                identifiers are formatted ``app:<APP_SID>``. `Custom parameters
                <https://www.twilio.com/docs/voice/api/conference-participant-resource#custom-parameters>`__ may also be
                specified.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``GET`` and
                ``POST`` and defaults to ``POST``.
            status_callback_event: The conference state changes that should generate a call to ``status_callback``. Can
                be: ``initiated``, ``ringing``, ``answered``, and ``completed``. Separate multiple values with a space.
                The default value is ``completed``.
            label: A label for this participant. If one is supplied, it may subsequently be used to fetch, update or
                delete the participant.
            timeout: The number of seconds that we should allow the phone to ring before assuming there is no answer.
                Can be an integer between ``5`` and ``600``, inclusive. The default value is ``60``. We always add a
                5-second timeout buffer to outgoing calls, so value of 10 would result in an actual timeout that was
                closer to 15 seconds.
            record: Whether to record the participant and their conferences, including the time between conferences. Can
                be ``true`` or ``false`` and the default is ``false``.
            muted: Whether the agent is muted in the conference. Can be ``true`` or ``false`` and the default is
                ``false``.
            beep: Whether to play a notification beep to the conference when the participant joins. Can be: ``true``,
                ``false``, ``onEnter``, or ``onExit``. The default value is ``true``.
            start_conference_on_enter: Whether to start the conference when the participant joins, if it has not already
                started. Can be: ``true`` or ``false`` and the default is ``true``. If ``false`` and the conference has
                not started, the participant is muted and hears background music until another participant starts the
                conference.
            end_conference_on_exit: Whether to end the conference when the participant leaves. Can be: ``true`` or
                ``false`` and defaults to ``false``.
            wait_url: The URL that Twilio calls using the ``wait_method`` before the conference has started. The URL may
                return an MP3 file, a WAV file, or a TwiML document. The default value is the URL of our standard hold
                music. If you do not want anything to play while waiting for the conference to start, specify an empty
                string by setting ``wait_url`` to ``''``. For more details on the allowable verbs within the
                ``waitUrl``, see the ``waitUrl`` attribute in the
                https://www.twilio.com/docs/voice/twiml/conference#attributes-waiturl.
            wait_method: The HTTP method we should use to call ``wait_url``. Can be ``GET`` or ``POST`` and the default
                is ``POST``. When using a static audio file, this should be ``GET`` so that we can cache the file.
            early_media: Whether to allow an agent to hear the state of the outbound call, including ringing or
                disconnect messages. Can be: ``true`` or ``false`` and defaults to ``true``.
            max_participants: The maximum number of participants in the conference. Can be a positive integer from ``2``
                to ``250``. The default value is ``250``.
            conference_record: Whether to record the conference the participant is joining. Can be: ``true``, ``false``,
                ``record-from-start``, and ``do-not-record``. The default value is ``false``.
            conference_trim: Whether to trim leading and trailing silence from the conference recording. Can be:
                ``trim-silence`` or ``do-not-trim`` and defaults to ``trim-silence``.
            conference_status_callback: The URL we should call using the ``conference_status_callback_method`` when the
                conference events in ``conference_status_callback_event`` occur. Only the value set by the first
                participant to join the conference is used. Subsequent ``conference_status_callback`` values are
                ignored.
            conference_status_callback_method: The HTTP method we should use to call ``conference_status_callback``. Can
                be: ``GET`` or ``POST`` and defaults to ``POST``.
            conference_status_callback_event: The conference state changes that should generate a call to
                ``conference_status_callback``. Can be: ``start``, ``end``, ``join``, ``leave``, ``mute``, ``hold``,
                ``modify``, ``speaker``, and ``announcement``. Separate multiple values with a space. Defaults to
                ``start end``.
            recording_channels: The recording channels for the final recording. Can be: ``mono`` or ``dual`` and the
                default is ``mono``.
            recording_status_callback: The URL that we should call using the ``recording_status_callback_method`` when
                the recording status changes.
            recording_status_callback_method: The HTTP method we should use when we call ``recording_status_callback``.
                Can be: ``GET`` or ``POST`` and defaults to ``POST``.
            sip_auth_username: The SIP username used for authentication.
            sip_auth_password: The SIP password for authentication.
            region: The `region
                <https://support.twilio.com/hc/en-us/articles/223132167-How-global-low-latency-routing-and-region-selection-work-for-conferences-and-Client-calls>`__
                where we should mix the recorded audio. Can be:``us1``, ``us2``, ``ie1``, ``de1``, ``sg1``, ``br1``,
                ``au1``, or ``jp1``.
            conference_recording_status_callback: The URL we should call using the
                ``conference_recording_status_callback_method`` when the conference recording is available.
            conference_recording_status_callback_method: The HTTP method we should use to call
                ``conference_recording_status_callback``. Can be: ``GET`` or ``POST`` and defaults to ``POST``.
            recording_status_callback_event: The recording state changes that should generate a call to
                ``recording_status_callback``. Can be: ``started``, ``in-progress``, ``paused``, ``resumed``,
                ``stopped``, ``completed``, ``failed``, and ``absent``. Separate multiple values with a space, ex:
                ``'in-progress completed failed'``.
            conference_recording_status_callback_event: The conference recording state changes that generate a call to
                ``conference_recording_status_callback``. Can be: ``in-progress``, ``completed``, ``failed``, and
                ``absent``. Separate multiple values with a space, ex: ``'in-progress completed failed'``
            coaching: Whether the participant is coaching another call. Can be: ``true`` or ``false``. If not present,
                defaults to ``false`` unless ``call_sid_to_coach`` is defined. If ``true``, ``call_sid_to_coach`` must
                be defined.
            call_sid_to_coach: The SID of the participant who is being ``coached``. The participant being coached is the
                only participant who can hear the participant who is ``coaching``.
            jitter_buffer_size: Jitter buffer size for the connecting participant. Twilio will use this setting to apply
                Jitter Buffer before participant's audio is mixed into the conference. Can be: ``off``, ``small``,
                ``medium``, and ``large``. Default to ``large``.
            byoc: The SID of a BYOC (Bring Your Own Carrier) trunk to route this call with. Note that ``byoc`` is only
                meaningful when ``to`` is a phone number; it will otherwise be ignored. (Beta)
            caller_id: The phone number, Client identifier, or username portion of SIP address that made this call.
                Phone numbers are in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format (e.g.,
                +16175551212). Client identifiers are formatted ``client:name``. If using a phone number, it must be a
                Twilio number or a Verified `outgoing caller id
                <https://www.twilio.com/docs/voice/api/outgoing-caller-ids>`__ for your account. If the ``to`` parameter
                is a phone number, ``callerId`` must also be a phone number. If ``to`` is sip address, this value of
                ``callerId`` should be a username portion to be used to populate the From header that is passed to the
                SIP endpoint.
            call_reason: The Reason for the outgoing call. Use it to specify the purpose of the call that is presented
                on the called party's phone. (Branded Calls Beta)
            recording_track: The audio track to record for the call. Can be: ``inbound``, ``outbound`` or ``both``. The
                default is ``both``. ``inbound`` records the audio that is received by Twilio. ``outbound`` records the
                audio that is sent from Twilio. ``both`` records the audio that is received and sent by Twilio.
            recording_configuration_id: The identifier of the configuration to be used when creating and processing the
                recording
            time_limit: The maximum duration of the call in seconds. Constraints depend on account and configuration.
            machine_detection: Whether to detect if a human, answering machine, or fax has picked up the call. Can be:
                ``Enable`` or ``DetectMessageEnd``. Use ``Enable`` if you would like us to return ``AnsweredBy`` as soon
                as the called party is identified. Use ``DetectMessageEnd``, if you would like to leave a message on an
                answering machine. For more information, see `Answering Machine Detection
                <https://www.twilio.com/docs/voice/answering-machine-detection>`__.
            machine_detection_timeout: The number of seconds that we should attempt to detect an answering machine
                before timing out and sending a voice request with ``AnsweredBy`` of ``unknown``. The default timeout is
                30 seconds.
            machine_detection_speech_threshold: The number of milliseconds that is used as the measuring stick for the
                length of the speech activity, where durations lower than this value will be interpreted as a human and
                longer than this value as a machine. Possible Values: 1000-6000. Default: 2400.
            machine_detection_speech_end_threshold: The number of milliseconds of silence after speech activity at which
                point the speech activity is considered complete. Possible Values: 500-5000. Default: 1200.
            machine_detection_silence_timeout: The number of milliseconds of initial silence after which an ``unknown``
                AnsweredBy result will be returned. Possible Values: 2000-10000. Default: 5000.
            amd_status_callback: The URL that we should call using the ``amd_status_callback_method`` to notify customer
                application whether the call was answered by human, machine or fax.
            amd_status_callback_method: The HTTP method we should use when calling the ``amd_status_callback`` URL. Can
                be: ``GET`` or ``POST`` and the default is ``POST``.
            trim: Whether to trim any leading and trailing silence from the participant recording. Can be:
                ``trim-silence`` or ``do-not-trim`` and the default is ``trim-silence``.
            call_token: A token string needed to invoke a forwarded call. A call_token is generated when an incoming
                call is received on a Twilio number. Pass an incoming call's call_token value to a forwarded call via
                the call_token parameter when creating a new call. A forwarded call should bear the same CallerID of the
                original incoming call.
            client_notification_url: The URL that we should use to deliver ``push call notification``.
            caller_display_name: The name that populates the display name in the From header. Must be between 2 and 255
                characters. Only applicable for calls to sip address.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("ConferenceSid", conference_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("From", from_),
                    param[str]("To", to),
                    param[str | None]("StatusCallback", status_callback),
                    param[StatusCallbackMethod16OrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[list[str] | None]("StatusCallbackEvent", status_callback_event),
                    param[str | None]("Label", label),
                    param[int | None]("Timeout", timeout),
                    param[bool | None]("Record", record),
                    param[bool | None]("Muted", muted),
                    param[str | None]("Beep", beep),
                    param[bool | None]("StartConferenceOnEnter", start_conference_on_enter),
                    param[bool | None]("EndConferenceOnExit", end_conference_on_exit),
                    param[str | None]("WaitUrl", wait_url),
                    param[WaitMethodOrStr | None]("WaitMethod", wait_method),
                    param[bool | None]("EarlyMedia", early_media),
                    param[int | None]("MaxParticipants", max_participants),
                    param[str | None]("ConferenceRecord", conference_record),
                    param[str | None]("ConferenceTrim", conference_trim),
                    param[str | None]("ConferenceStatusCallback", conference_status_callback),
                    param[ConferenceStatusCallbackMethodOrStr | None](
                        "ConferenceStatusCallbackMethod", conference_status_callback_method
                    ),
                    param[list[str] | None]("ConferenceStatusCallbackEvent", conference_status_callback_event),
                    param[str | None]("RecordingChannels", recording_channels),
                    param[str | None]("RecordingStatusCallback", recording_status_callback),
                    param[RecordingStatusCallbackMethod2OrStr | None](
                        "RecordingStatusCallbackMethod", recording_status_callback_method
                    ),
                    param[str | None]("SipAuthUsername", sip_auth_username),
                    param[str | None]("SipAuthPassword", sip_auth_password),
                    param[str | None]("Region", region),
                    param[str | None]("ConferenceRecordingStatusCallback", conference_recording_status_callback),
                    param[ConferenceRecordingStatusCallbackMethodOrStr | None](
                        "ConferenceRecordingStatusCallbackMethod", conference_recording_status_callback_method
                    ),
                    param[list[str] | None]("RecordingStatusCallbackEvent", recording_status_callback_event),
                    param[list[str] | None](
                        "ConferenceRecordingStatusCallbackEvent", conference_recording_status_callback_event
                    ),
                    param[bool | None]("Coaching", coaching),
                    param[str | None]("CallSidToCoach", call_sid_to_coach),
                    param[str | None]("JitterBufferSize", jitter_buffer_size),
                    param[str | None]("Byoc", byoc),
                    param[str | None]("CallerId", caller_id),
                    param[str | None]("CallReason", call_reason),
                    param[str | None]("RecordingTrack", recording_track),
                    param[str | None]("RecordingConfigurationId", recording_configuration_id),
                    param[int | None]("TimeLimit", time_limit),
                    param[str | None]("MachineDetection", machine_detection),
                    param[int | None]("MachineDetectionTimeout", machine_detection_timeout),
                    param[int | None]("MachineDetectionSpeechThreshold", machine_detection_speech_threshold),
                    param[int | None]("MachineDetectionSpeechEndThreshold", machine_detection_speech_end_threshold),
                    param[int | None]("MachineDetectionSilenceTimeout", machine_detection_silence_timeout),
                    param[str | None]("AmdStatusCallback", amd_status_callback),
                    param[AmdStatusCallbackMethodOrStr | None]("AmdStatusCallbackMethod", amd_status_callback_method),
                    param[str | None]("Trim", trim),
                    param[str | None]("CallToken", call_token),
                    param[str | None]("ClientNotificationUrl", client_notification_url),
                    param[str | None]("CallerDisplayName", caller_display_name),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountConferenceParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_participant(
        self,
        account_sid: str,
        conference_sid: str,
        call_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Kick a participant from a given conference

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Participant resources to delete.
            conference_sid: The SID of the conference with the participants to delete.
            call_sid: The `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ SID or label of the participant
                to delete. Non URL safe characters in a label must be percent encoded, for example, a space character is
                represented as %20.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("ConferenceSid", conference_sid),
                param[str]("CallSid", call_sid),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_participant(
        self,
        account_sid: str,
        conference_sid: str,
        call_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountConferenceParticipant, RawError]:
        """Fetch an instance of a participant

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Participant resource to fetch.
            conference_sid: The SID of the conference with the participant to fetch.
            call_sid: The `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ SID or label of the participant
                to fetch. Non URL safe characters in a label must be percent encoded, for example, a space character is
                represented as %20.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("ConferenceSid", conference_sid),
                param[str]("CallSid", call_sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountConferenceParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_participant(
        self,
        account_sid: str,
        conference_sid: str,
        *,
        muted: bool | None = None,
        hold: bool | None = None,
        coaching: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListParticipantResponse, RawError]:
        """Retrieve a list of participants belonging to the account used to make the request

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Participant resources to read.
            conference_sid: The SID of the conference with the participants to read.
            muted: Whether to return only participants that are muted. Can be: ``true`` or ``false``.
            hold: Whether to return only participants that are on hold. Can be: ``true`` or ``false``.
            coaching: Whether to return only participants who are coaching another call. Can be: ``true`` or ``false``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants.json"
            ),
            path_params=[param[str]("AccountSid", account_sid), param[str]("ConferenceSid", conference_sid)],
            query_params=[
                param[bool | None]("Muted", muted),
                param[bool | None]("Hold", hold),
                param[bool | None]("Coaching", coaching),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListParticipantResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_participant(
        self,
        account_sid: str,
        conference_sid: str,
        call_sid: str,
        *,
        muted: bool | None = None,
        hold: bool | None = None,
        hold_url: str | None = None,
        hold_method: HoldMethodOrStr | None = None,
        announce_url: str | None = None,
        announce_method: AnnounceMethod1OrStr | None = None,
        wait_url: str | None = None,
        wait_method: WaitMethodOrStr | None = None,
        beep_on_exit: bool | None = None,
        end_conference_on_exit: bool | None = None,
        coaching: bool | None = None,
        call_sid_to_coach: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountConferenceParticipant, RawError]:
        """Update the properties of the participant

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Participant resources to update.
            conference_sid: The SID of the conference with the participant to update.
            call_sid: The `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ SID or label of the participant
                to update. Non URL safe characters in a label must be percent encoded, for example, a space character is
                represented as %20.
            muted: Whether the participant should be muted. Can be ``true`` or ``false``. ``true`` will mute the
                participant, and ``false`` will un-mute them. Anything value other than ``true`` or ``false`` is
                interpreted as ``false``.
            hold: Whether the participant should be on hold. Can be: ``true`` or ``false``. ``true`` puts the
                participant on hold, and ``false`` lets them rejoin the conference.
            hold_url: The URL we call using the ``hold_method`` for music that plays when the participant is on hold.
                The URL may return an MP3 file, a WAV file, or a TwiML document that contains ``<Play>``, ``<Say>``,
                ``<Pause>``, or ``<Redirect>`` verbs.
            hold_method: The HTTP method we should use to call ``hold_url``. Can be: ``GET`` or ``POST`` and the default
                is ``GET``.
            announce_url: The URL we call using the ``announce_method`` for an announcement to the participant. The URL
                may return an MP3 file, a WAV file, or a TwiML document that contains ``<Play>``, ``<Say>``,
                ``<Pause>``, or ``<Redirect>`` verbs.
            announce_method: The HTTP method we should use to call ``announce_url``. Can be: ``GET`` or ``POST`` and
                defaults to ``POST``.
            wait_url: The URL that Twilio calls using the ``wait_method`` before the conference has started. The URL may
                return an MP3 file, a WAV file, or a TwiML document. The default value is the URL of our standard hold
                music. If you do not want anything to play while waiting for the conference to start, specify an empty
                string by setting ``wait_url`` to ``''``. For more details on the allowable verbs within the
                ``waitUrl``, see the ``waitUrl`` attribute in the
                https://www.twilio.com/docs/voice/twiml/conference#attributes-waiturl.
            wait_method: The HTTP method we should use to call ``wait_url``. Can be ``GET`` or ``POST`` and the default
                is ``POST``. When using a static audio file, this should be ``GET`` so that we can cache the file.
            beep_on_exit: Whether to play a notification beep to the conference when the participant exits. Can be:
                ``true`` or ``false``.
            end_conference_on_exit: Whether to end the conference when the participant leaves. Can be: ``true`` or
                ``false`` and defaults to ``false``.
            coaching: Whether the participant is coaching another call. Can be: ``true`` or ``false``. If not present,
                defaults to ``false`` unless ``call_sid_to_coach`` is defined. If ``true``, ``call_sid_to_coach`` must
                be defined.
            call_sid_to_coach: The SID of the participant who is being ``coached``. The participant being coached is the
                only participant who can hear the participant who is ``coaching``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}.json"
            ),
            path_params=[
                param[str]("AccountSid", account_sid),
                param[str]("ConferenceSid", conference_sid),
                param[str]("CallSid", call_sid),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[bool | None]("Muted", muted),
                    param[bool | None]("Hold", hold),
                    param[str | None]("HoldUrl", hold_url),
                    param[HoldMethodOrStr | None]("HoldMethod", hold_method),
                    param[str | None]("AnnounceUrl", announce_url),
                    param[AnnounceMethod1OrStr | None]("AnnounceMethod", announce_method),
                    param[str | None]("WaitUrl", wait_url),
                    param[WaitMethodOrStr | None]("WaitMethod", wait_method),
                    param[bool | None]("BeepOnExit", beep_on_exit),
                    param[bool | None]("EndConferenceOnExit", end_conference_on_exit),
                    param[bool | None]("Coaching", coaching),
                    param[str | None]("CallSidToCoach", call_sid_to_coach),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountConferenceParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
