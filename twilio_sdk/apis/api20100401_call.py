from __future__ import annotations

from pydantic import AnyUrl

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    RFC3339DateTime,
    SecuredRawResponse,
    empty_response,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.api_v2010_account_call import ApiV2010AccountCall
from ..models.enums.async_amd_status_callback_method import AsyncAmdStatusCallbackMethodOrStr
from ..models.enums.call_enum_status import CallEnumStatusOrStr
from ..models.enums.call_enum_update_status import CallEnumUpdateStatusOrStr
from ..models.enums.fallback_method import FallbackMethodOrStr
from ..models.enums.method import MethodOrStr
from ..models.enums.method1 import Method1OrStr
from ..models.enums.recording_status_callback_method import RecordingStatusCallbackMethodOrStr
from ..models.enums.status_callback_method8 import StatusCallbackMethod8OrStr
from ..models.enums.status_callback_method9 import StatusCallbackMethod9OrStr
from ..models.list_call_response import ListCallResponse
from ..server.server import Server


class Api20100401Call:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401CallWithRawResponse(client, server, auth)

    def create_call(
        self,
        account_sid: str,
        to: str,
        from_: str,
        *,
        method: MethodOrStr | None = None,
        fallback_url: AnyUrl | None = None,
        fallback_method: FallbackMethodOrStr | None = None,
        status_callback: AnyUrl | None = None,
        status_callback_event: list[str] | None = None,
        status_callback_method: StatusCallbackMethod8OrStr | None = None,
        send_digits: str | None = None,
        timeout: int | None = None,
        record: bool | None = None,
        recording_channels: str | None = None,
        recording_status_callback: str | None = None,
        recording_status_callback_method: RecordingStatusCallbackMethodOrStr | None = None,
        recording_configuration_id: str | None = None,
        sip_auth_username: str | None = None,
        sip_auth_password: str | None = None,
        machine_detection: str | None = None,
        machine_detection_timeout: int | None = None,
        recording_status_callback_event: list[str] | None = None,
        trim: str | None = None,
        caller_id: str | None = None,
        machine_detection_speech_threshold: int | None = None,
        machine_detection_speech_end_threshold: int | None = None,
        machine_detection_silence_timeout: int | None = None,
        async_amd: str | None = None,
        async_amd_status_callback: AnyUrl | None = None,
        async_amd_status_callback_method: AsyncAmdStatusCallbackMethodOrStr | None = None,
        byoc: str | None = None,
        call_reason: str | None = None,
        call_token: str | None = None,
        recording_track: str | None = None,
        time_limit: int | None = None,
        client_notification_url: AnyUrl | None = None,
        url: AnyUrl | None = None,
        twiml: str | None = None,
        application_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountCall:
        """Create a new outgoing call to phones, SIP-enabled endpoints or Twilio Client connections

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            to: The phone number, SIP address, or client identifier to call.
            from_: The phone number or client identifier to use as the caller id. If using a phone number, it must be a
                Twilio number or a Verified `outgoing caller id
                <https://www.twilio.com/docs/voice/api/outgoing-caller-ids>`__ for your account. If the ``to`` parameter
                is a phone number, ``From`` must also be a phone number.
            method: The HTTP method we should use when calling the ``url`` parameter's value. Can be: ``GET`` or
                ``POST`` and the default is ``POST``. If an ``application_sid`` parameter is present, this parameter is
                ignored.
            fallback_url: The URL that we call using the ``fallback_method`` if an error occurs when requesting or
                executing the TwiML at ``url``. If an ``application_sid`` parameter is present, this parameter is
                ignored.
            fallback_method: The HTTP method that we should use to request the ``fallback_url``. Can be: ``GET`` or
                ``POST`` and the default is ``POST``. If an ``application_sid`` parameter is present, this parameter is
                ignored.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application. If no ``status_callback_event`` is specified, we will send the ``completed`` status.
                If an ``application_sid`` parameter is present, this parameter is ignored. URLs must contain a valid
                hostname (underscores are not permitted).
            status_callback_event: The call progress events that we will send to the ``status_callback`` URL. Can be:
                ``initiated``, ``ringing``, ``answered``, and ``completed``. If no event is specified, we send the
                ``completed`` status. If you want to receive multiple events, specify each one in a separate
                ``status_callback_event`` parameter. See the code sample for `monitoring call progress
                <https://www.twilio.com/docs/voice/api/call-resource?code-sample=code-create-a-call-resource-and-specify-a-statuscallbackevent&code-sdk-version=json>`__.
                If an ``application_sid`` is present, this parameter is ignored.
            status_callback_method: The HTTP method we should use when calling the ``status_callback`` URL. Can be:
                ``GET`` or ``POST`` and the default is ``POST``. If an ``application_sid`` parameter is present, this
                parameter is ignored.
            send_digits: The string of keys to dial after connecting to the number, with a maximum length of 32 digits.
                Valid digits in the string include any digit (``0``-``9``), '``A``', '``B``', '``C``', '``D``', '``#``',
                and '``*``'. You can also use '``w``' to insert a half-second pause and '``W``' to insert a one-second
                pause. For example, to pause for one second after connecting and then dial extension 1234 followed by
                the # key, set this parameter to ``W1234#``. Be sure to URL-encode this string because the '``#``'
                character has special meaning in a URL. If both ``SendDigits`` and ``MachineDetection`` parameters are
                provided, then ``MachineDetection`` will be ignored.
            timeout: The integer number of seconds that we should allow the phone to ring before assuming there is no
                answer. The default is ``60`` seconds and the maximum is ``600`` seconds. For some call flows, we will
                add a 5-second buffer to the timeout value you provide. For this reason, a timeout value of 10 seconds
                could result in an actual timeout closer to 15 seconds. You can set this to a short time, such as ``15``
                seconds, to hang up before reaching an answering machine or voicemail.
            record: Whether to record the call. Can be ``true`` to record the phone call, or ``false`` to not. The
                default is ``false``. The ``recording_url`` is sent to the ``status_callback`` URL.
            recording_channels: The number of channels in the final recording. Can be: ``mono`` or ``dual``. The default
                is ``mono``. ``mono`` records both legs of the call in a single channel of the recording file. ``dual``
                records each leg to a separate channel of the recording file. The first channel of a dual-channel
                recording contains the parent call and the second channel contains the child call.
            recording_status_callback: The URL that we call when the recording is available to be accessed.
            recording_status_callback_method: The HTTP method we should use when calling the
                ``recording_status_callback`` URL. Can be: ``GET`` or ``POST`` and the default is ``POST``.
            recording_configuration_id: The identifier of the configuration to be used when creating and processing the
                recording
            sip_auth_username: The username used to authenticate the caller making a SIP call.
            sip_auth_password: The password required to authenticate the user account specified in
                ``sip_auth_username``.
            machine_detection: Whether to detect if a human, answering machine, or fax has picked up the call. Can be:
                ``Enable`` or ``DetectMessageEnd``. Use ``Enable`` if you would like us to return ``AnsweredBy`` as soon
                as the called party is identified. Use ``DetectMessageEnd``, if you would like to leave a message on an
                answering machine. If ``send_digits`` is provided, this parameter is ignored. For more information, see
                `Answering Machine Detection <https://www.twilio.com/docs/voice/answering-machine-detection>`__.
            machine_detection_timeout: The number of seconds that we should attempt to detect an answering machine
                before timing out and sending a voice request with ``AnsweredBy`` of ``unknown``. The default timeout is
                30 seconds.
            recording_status_callback_event: The recording status events that will trigger calls to the URL specified in
                ``recording_status_callback``. Can be: ``in-progress``, ``completed`` and ``absent``. Defaults to
                ``completed``. Separate multiple values with a space.
            trim: Whether to trim any leading and trailing silence from the recording. Can be: ``trim-silence`` or
                ``do-not-trim`` and the default is ``trim-silence``.
            caller_id: The phone number, SIP address, or Client identifier that made this call. Phone numbers are in
                `E.164 format <https://wwnw.twilio.com/docs/glossary/what-e164>`__ (e.g., +16175551212). SIP addresses
                are formatted as ``name@company.com``.
            machine_detection_speech_threshold: The number of milliseconds that is used as the measuring stick for the
                length of the speech activity, where durations lower than this value will be interpreted as a human and
                longer than this value as a machine. Possible Values: 1000-6000. Default: 2400.
            machine_detection_speech_end_threshold: The number of milliseconds of silence after speech activity at which
                point the speech activity is considered complete. Possible Values: 500-5000. Default: 1200.
            machine_detection_silence_timeout: The number of milliseconds of initial silence after which an ``unknown``
                AnsweredBy result will be returned. Possible Values: 2000-10000. Default: 5000.
            async_amd: Select whether to perform answering machine detection in the background. Default, blocks the
                execution of the call until Answering Machine Detection is completed. Can be: ``true`` or ``false``.
            async_amd_status_callback: The URL that we should call using the ``async_amd_status_callback_method`` to
                notify customer application whether the call was answered by human, machine or fax.
            async_amd_status_callback_method: The HTTP method we should use when calling the
                ``async_amd_status_callback`` URL. Can be: ``GET`` or ``POST`` and the default is ``POST``.
            byoc: The SID of a BYOC (Bring Your Own Carrier) trunk to route this call with. Note that ``byoc`` is only
                meaningful when ``to`` is a phone number; it will otherwise be ignored. (Beta)
            call_reason: The Reason for the outgoing call. Use it to specify the purpose of the call that is presented
                on the called party's phone. (Branded Calls Beta)
            call_token: A token string needed to invoke a forwarded call. A call_token is generated when an incoming
                call is received on a Twilio number. Pass an incoming call's call_token value to a forwarded call via
                the call_token parameter when creating a new call. A forwarded call should bear the same CallerID of the
                original incoming call.
            recording_track: The audio track to record for the call. Can be: ``inbound``, ``outbound`` or ``both``. The
                default is ``both``. ``inbound`` records the audio that is received by Twilio. ``outbound`` records the
                audio that is generated from Twilio. ``both`` records the audio that is received and generated by
                Twilio.
            time_limit: The maximum duration of the call in seconds. Constraints depend on account and configuration.
            client_notification_url: The URL that we should use to deliver ``push call notification``.
            url: The absolute URL that returns the TwiML instructions for the call. We will call this URL using the
                ``method`` when the call connects. For more information, see the `Url Parameter
                <https://www.twilio.com/docs/voice/make-calls#specify-a-url-parameter>`__ section in `Making Calls
                <https://www.twilio.com/docs/voice/make-calls>`__.
            twiml: TwiML instructions for the call Twilio will use without fetching Twiml from url parameter. If both
                ``twiml`` and ``url`` are provided then ``twiml`` parameter will be ignored. Max 4000 characters.
            application_sid: The SID of the Application resource that will handle the call, if the call will be handled
                by an application.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_call(
            account_sid,
            to,
            from_,
            method=method,
            fallback_url=fallback_url,
            fallback_method=fallback_method,
            status_callback=status_callback,
            status_callback_event=status_callback_event,
            status_callback_method=status_callback_method,
            send_digits=send_digits,
            timeout=timeout,
            record=record,
            recording_channels=recording_channels,
            recording_status_callback=recording_status_callback,
            recording_status_callback_method=recording_status_callback_method,
            recording_configuration_id=recording_configuration_id,
            sip_auth_username=sip_auth_username,
            sip_auth_password=sip_auth_password,
            machine_detection=machine_detection,
            machine_detection_timeout=machine_detection_timeout,
            recording_status_callback_event=recording_status_callback_event,
            trim=trim,
            caller_id=caller_id,
            machine_detection_speech_threshold=machine_detection_speech_threshold,
            machine_detection_speech_end_threshold=machine_detection_speech_end_threshold,
            machine_detection_silence_timeout=machine_detection_silence_timeout,
            async_amd=async_amd,
            async_amd_status_callback=async_amd_status_callback,
            async_amd_status_callback_method=async_amd_status_callback_method,
            byoc=byoc,
            call_reason=call_reason,
            call_token=call_token,
            recording_track=recording_track,
            time_limit=time_limit,
            client_notification_url=client_notification_url,
            url=url,
            twiml=twiml,
            application_sid=application_sid,
            request_options=request_options,
        ).unwrap()

    def delete_call(self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a Call record from your account. Once the record is deleted, it will no longer appear in the API and
        Account Portal logs.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Call
                resource(s) to delete.
            sid: The Twilio-provided Call SID that uniquely identifies the Call resource to delete
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_call(account_sid, sid, request_options=request_options).unwrap()

    def fetch_call(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountCall:
        """Fetch the call specified by the provided Call SID

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Call
                resource(s) to fetch.
            sid: The SID of the Call resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_call(account_sid, sid, request_options=request_options).unwrap()

    def list_call(
        self,
        account_sid: str,
        *,
        to: str | None = None,
        from_: str | None = None,
        parent_call_sid: str | None = None,
        status: CallEnumStatusOrStr | None = None,
        start_time: RFC3339DateTime | None = None,
        start_time_query: RFC3339DateTime | None = None,
        start_time_query_query: RFC3339DateTime | None = None,
        end_time: RFC3339DateTime | None = None,
        end_time_query: RFC3339DateTime | None = None,
        end_time_query_query: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCallResponse:
        """Retrieves a collection of calls made to and from your account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Call
                resource(s) to read.
            to: Only show calls made to this phone number, SIP address, Client identifier or SIM SID.
            from_: Only include calls from this phone number, SIP address, Client identifier or SIM SID.
            parent_call_sid: Only include calls spawned by calls with this SID.
            status: The status of the calls to include. Can be: ``queued``, ``ringing``, ``in-progress``, ``canceled``,
                ``completed``, ``failed``, ``busy``, or ``no-answer``.
            start_time: Only include calls that started on this date. Specify a date as ``YYYY-MM-DD`` in UTC, for
                example: ``2009-07-06``, to read only calls that started on this date.
            start_time_query: Only include calls that started before this date. Specify a date as ``YYYY-MM-DD`` in UTC,
                for example: ``2009-07-06``, to read only calls that started before this date.
            start_time_query_query: Only include calls that started on or after this date. Specify a date as
                ``YYYY-MM-DD`` in UTC, for example: ``2009-07-06``, to read only calls that started on or after this
                date.
            end_time: Only include calls that ended on this date. Specify a date as ``YYYY-MM-DD`` in UTC, for example:
                ``2009-07-06``, to read only calls that ended on this date.
            end_time_query: Only include calls that ended before this date. Specify a date as ``YYYY-MM-DD`` in UTC, for
                example: ``2009-07-06``, to read only calls that ended before this date.
            end_time_query_query: Only include calls that ended on or after this date. Specify a date as ``YYYY-MM-DD``
                in UTC, for example: ``2009-07-06``, to read only calls that ended on or after this date.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_call(
            account_sid,
            to=to,
            from_=from_,
            parent_call_sid=parent_call_sid,
            status=status,
            start_time=start_time,
            start_time_query=start_time_query,
            start_time_query_query=start_time_query_query,
            end_time=end_time,
            end_time_query=end_time_query,
            end_time_query_query=end_time_query_query,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_call(
        self,
        account_sid: str,
        sid: str,
        *,
        url: AnyUrl | None = None,
        method: Method1OrStr | None = None,
        status: CallEnumUpdateStatusOrStr | None = None,
        fallback_url: AnyUrl | None = None,
        fallback_method: FallbackMethodOrStr | None = None,
        status_callback: AnyUrl | None = None,
        status_callback_method: StatusCallbackMethod9OrStr | None = None,
        twiml: str | None = None,
        time_limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountCall:
        """Initiates a call redirect or terminates a call

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Call
                resource(s) to update.
            sid: The Twilio-provided string that uniquely identifies the Call resource to update
            url: The absolute URL that returns the TwiML instructions for the call. We will call this URL using the
                ``method`` when the call connects. For more information, see the `Url Parameter
                <https://www.twilio.com/docs/voice/make-calls#specify-a-url-parameter>`__ section in `Making Calls
                <https://www.twilio.com/docs/voice/make-calls>`__.
            method: The HTTP method we should use when calling the ``url``. Can be: ``GET`` or ``POST`` and the default
                is ``POST``. If an ``application_sid`` parameter is present, this parameter is ignored.
            status: Value sent with the request.
            fallback_url: The URL that we call using the ``fallback_method`` if an error occurs when requesting or
                executing the TwiML at ``url``. If an ``application_sid`` parameter is present, this parameter is
                ignored.
            fallback_method: The HTTP method that we should use to request the ``fallback_url``. Can be: ``GET`` or
                ``POST`` and the default is ``POST``. If an ``application_sid`` parameter is present, this parameter is
                ignored.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application. If no ``status_callback_event`` is specified, we will send the ``completed`` status.
                If an ``application_sid`` parameter is present, this parameter is ignored. URLs must contain a valid
                hostname (underscores are not permitted).
            status_callback_method: The HTTP method we should use when requesting the ``status_callback`` URL. Can be:
                ``GET`` or ``POST`` and the default is ``POST``. If an ``application_sid`` parameter is present, this
                parameter is ignored.
            twiml: TwiML instructions for the call Twilio will use without fetching Twiml from url. Twiml and url
                parameters are mutually exclusive
            time_limit: The maximum duration of the call in seconds. Constraints depend on account and configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_call(
            account_sid,
            sid,
            url=url,
            method=method,
            status=status,
            fallback_url=fallback_url,
            fallback_method=fallback_method,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            twiml=twiml,
            time_limit=time_limit,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401CallWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401Call:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401CallWithRawResponse(client, server, auth)

    async def create_call(
        self,
        account_sid: str,
        to: str,
        from_: str,
        *,
        method: MethodOrStr | None = None,
        fallback_url: AnyUrl | None = None,
        fallback_method: FallbackMethodOrStr | None = None,
        status_callback: AnyUrl | None = None,
        status_callback_event: list[str] | None = None,
        status_callback_method: StatusCallbackMethod8OrStr | None = None,
        send_digits: str | None = None,
        timeout: int | None = None,
        record: bool | None = None,
        recording_channels: str | None = None,
        recording_status_callback: str | None = None,
        recording_status_callback_method: RecordingStatusCallbackMethodOrStr | None = None,
        recording_configuration_id: str | None = None,
        sip_auth_username: str | None = None,
        sip_auth_password: str | None = None,
        machine_detection: str | None = None,
        machine_detection_timeout: int | None = None,
        recording_status_callback_event: list[str] | None = None,
        trim: str | None = None,
        caller_id: str | None = None,
        machine_detection_speech_threshold: int | None = None,
        machine_detection_speech_end_threshold: int | None = None,
        machine_detection_silence_timeout: int | None = None,
        async_amd: str | None = None,
        async_amd_status_callback: AnyUrl | None = None,
        async_amd_status_callback_method: AsyncAmdStatusCallbackMethodOrStr | None = None,
        byoc: str | None = None,
        call_reason: str | None = None,
        call_token: str | None = None,
        recording_track: str | None = None,
        time_limit: int | None = None,
        client_notification_url: AnyUrl | None = None,
        url: AnyUrl | None = None,
        twiml: str | None = None,
        application_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountCall:
        """Create a new outgoing call to phones, SIP-enabled endpoints or Twilio Client connections

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            to: The phone number, SIP address, or client identifier to call.
            from_: The phone number or client identifier to use as the caller id. If using a phone number, it must be a
                Twilio number or a Verified `outgoing caller id
                <https://www.twilio.com/docs/voice/api/outgoing-caller-ids>`__ for your account. If the ``to`` parameter
                is a phone number, ``From`` must also be a phone number.
            method: The HTTP method we should use when calling the ``url`` parameter's value. Can be: ``GET`` or
                ``POST`` and the default is ``POST``. If an ``application_sid`` parameter is present, this parameter is
                ignored.
            fallback_url: The URL that we call using the ``fallback_method`` if an error occurs when requesting or
                executing the TwiML at ``url``. If an ``application_sid`` parameter is present, this parameter is
                ignored.
            fallback_method: The HTTP method that we should use to request the ``fallback_url``. Can be: ``GET`` or
                ``POST`` and the default is ``POST``. If an ``application_sid`` parameter is present, this parameter is
                ignored.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application. If no ``status_callback_event`` is specified, we will send the ``completed`` status.
                If an ``application_sid`` parameter is present, this parameter is ignored. URLs must contain a valid
                hostname (underscores are not permitted).
            status_callback_event: The call progress events that we will send to the ``status_callback`` URL. Can be:
                ``initiated``, ``ringing``, ``answered``, and ``completed``. If no event is specified, we send the
                ``completed`` status. If you want to receive multiple events, specify each one in a separate
                ``status_callback_event`` parameter. See the code sample for `monitoring call progress
                <https://www.twilio.com/docs/voice/api/call-resource?code-sample=code-create-a-call-resource-and-specify-a-statuscallbackevent&code-sdk-version=json>`__.
                If an ``application_sid`` is present, this parameter is ignored.
            status_callback_method: The HTTP method we should use when calling the ``status_callback`` URL. Can be:
                ``GET`` or ``POST`` and the default is ``POST``. If an ``application_sid`` parameter is present, this
                parameter is ignored.
            send_digits: The string of keys to dial after connecting to the number, with a maximum length of 32 digits.
                Valid digits in the string include any digit (``0``-``9``), '``A``', '``B``', '``C``', '``D``', '``#``',
                and '``*``'. You can also use '``w``' to insert a half-second pause and '``W``' to insert a one-second
                pause. For example, to pause for one second after connecting and then dial extension 1234 followed by
                the # key, set this parameter to ``W1234#``. Be sure to URL-encode this string because the '``#``'
                character has special meaning in a URL. If both ``SendDigits`` and ``MachineDetection`` parameters are
                provided, then ``MachineDetection`` will be ignored.
            timeout: The integer number of seconds that we should allow the phone to ring before assuming there is no
                answer. The default is ``60`` seconds and the maximum is ``600`` seconds. For some call flows, we will
                add a 5-second buffer to the timeout value you provide. For this reason, a timeout value of 10 seconds
                could result in an actual timeout closer to 15 seconds. You can set this to a short time, such as ``15``
                seconds, to hang up before reaching an answering machine or voicemail.
            record: Whether to record the call. Can be ``true`` to record the phone call, or ``false`` to not. The
                default is ``false``. The ``recording_url`` is sent to the ``status_callback`` URL.
            recording_channels: The number of channels in the final recording. Can be: ``mono`` or ``dual``. The default
                is ``mono``. ``mono`` records both legs of the call in a single channel of the recording file. ``dual``
                records each leg to a separate channel of the recording file. The first channel of a dual-channel
                recording contains the parent call and the second channel contains the child call.
            recording_status_callback: The URL that we call when the recording is available to be accessed.
            recording_status_callback_method: The HTTP method we should use when calling the
                ``recording_status_callback`` URL. Can be: ``GET`` or ``POST`` and the default is ``POST``.
            recording_configuration_id: The identifier of the configuration to be used when creating and processing the
                recording
            sip_auth_username: The username used to authenticate the caller making a SIP call.
            sip_auth_password: The password required to authenticate the user account specified in
                ``sip_auth_username``.
            machine_detection: Whether to detect if a human, answering machine, or fax has picked up the call. Can be:
                ``Enable`` or ``DetectMessageEnd``. Use ``Enable`` if you would like us to return ``AnsweredBy`` as soon
                as the called party is identified. Use ``DetectMessageEnd``, if you would like to leave a message on an
                answering machine. If ``send_digits`` is provided, this parameter is ignored. For more information, see
                `Answering Machine Detection <https://www.twilio.com/docs/voice/answering-machine-detection>`__.
            machine_detection_timeout: The number of seconds that we should attempt to detect an answering machine
                before timing out and sending a voice request with ``AnsweredBy`` of ``unknown``. The default timeout is
                30 seconds.
            recording_status_callback_event: The recording status events that will trigger calls to the URL specified in
                ``recording_status_callback``. Can be: ``in-progress``, ``completed`` and ``absent``. Defaults to
                ``completed``. Separate multiple values with a space.
            trim: Whether to trim any leading and trailing silence from the recording. Can be: ``trim-silence`` or
                ``do-not-trim`` and the default is ``trim-silence``.
            caller_id: The phone number, SIP address, or Client identifier that made this call. Phone numbers are in
                `E.164 format <https://wwnw.twilio.com/docs/glossary/what-e164>`__ (e.g., +16175551212). SIP addresses
                are formatted as ``name@company.com``.
            machine_detection_speech_threshold: The number of milliseconds that is used as the measuring stick for the
                length of the speech activity, where durations lower than this value will be interpreted as a human and
                longer than this value as a machine. Possible Values: 1000-6000. Default: 2400.
            machine_detection_speech_end_threshold: The number of milliseconds of silence after speech activity at which
                point the speech activity is considered complete. Possible Values: 500-5000. Default: 1200.
            machine_detection_silence_timeout: The number of milliseconds of initial silence after which an ``unknown``
                AnsweredBy result will be returned. Possible Values: 2000-10000. Default: 5000.
            async_amd: Select whether to perform answering machine detection in the background. Default, blocks the
                execution of the call until Answering Machine Detection is completed. Can be: ``true`` or ``false``.
            async_amd_status_callback: The URL that we should call using the ``async_amd_status_callback_method`` to
                notify customer application whether the call was answered by human, machine or fax.
            async_amd_status_callback_method: The HTTP method we should use when calling the
                ``async_amd_status_callback`` URL. Can be: ``GET`` or ``POST`` and the default is ``POST``.
            byoc: The SID of a BYOC (Bring Your Own Carrier) trunk to route this call with. Note that ``byoc`` is only
                meaningful when ``to`` is a phone number; it will otherwise be ignored. (Beta)
            call_reason: The Reason for the outgoing call. Use it to specify the purpose of the call that is presented
                on the called party's phone. (Branded Calls Beta)
            call_token: A token string needed to invoke a forwarded call. A call_token is generated when an incoming
                call is received on a Twilio number. Pass an incoming call's call_token value to a forwarded call via
                the call_token parameter when creating a new call. A forwarded call should bear the same CallerID of the
                original incoming call.
            recording_track: The audio track to record for the call. Can be: ``inbound``, ``outbound`` or ``both``. The
                default is ``both``. ``inbound`` records the audio that is received by Twilio. ``outbound`` records the
                audio that is generated from Twilio. ``both`` records the audio that is received and generated by
                Twilio.
            time_limit: The maximum duration of the call in seconds. Constraints depend on account and configuration.
            client_notification_url: The URL that we should use to deliver ``push call notification``.
            url: The absolute URL that returns the TwiML instructions for the call. We will call this URL using the
                ``method`` when the call connects. For more information, see the `Url Parameter
                <https://www.twilio.com/docs/voice/make-calls#specify-a-url-parameter>`__ section in `Making Calls
                <https://www.twilio.com/docs/voice/make-calls>`__.
            twiml: TwiML instructions for the call Twilio will use without fetching Twiml from url parameter. If both
                ``twiml`` and ``url`` are provided then ``twiml`` parameter will be ignored. Max 4000 characters.
            application_sid: The SID of the Application resource that will handle the call, if the call will be handled
                by an application.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_call(
                account_sid,
                to,
                from_,
                method=method,
                fallback_url=fallback_url,
                fallback_method=fallback_method,
                status_callback=status_callback,
                status_callback_event=status_callback_event,
                status_callback_method=status_callback_method,
                send_digits=send_digits,
                timeout=timeout,
                record=record,
                recording_channels=recording_channels,
                recording_status_callback=recording_status_callback,
                recording_status_callback_method=recording_status_callback_method,
                recording_configuration_id=recording_configuration_id,
                sip_auth_username=sip_auth_username,
                sip_auth_password=sip_auth_password,
                machine_detection=machine_detection,
                machine_detection_timeout=machine_detection_timeout,
                recording_status_callback_event=recording_status_callback_event,
                trim=trim,
                caller_id=caller_id,
                machine_detection_speech_threshold=machine_detection_speech_threshold,
                machine_detection_speech_end_threshold=machine_detection_speech_end_threshold,
                machine_detection_silence_timeout=machine_detection_silence_timeout,
                async_amd=async_amd,
                async_amd_status_callback=async_amd_status_callback,
                async_amd_status_callback_method=async_amd_status_callback_method,
                byoc=byoc,
                call_reason=call_reason,
                call_token=call_token,
                recording_track=recording_track,
                time_limit=time_limit,
                client_notification_url=client_notification_url,
                url=url,
                twiml=twiml,
                application_sid=application_sid,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_call(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a Call record from your account. Once the record is deleted, it will no longer appear in the API and
        Account Portal logs.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Call
                resource(s) to delete.
            sid: The Twilio-provided Call SID that uniquely identifies the Call resource to delete
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_call(account_sid, sid, request_options=request_options)).unwrap()

    async def fetch_call(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountCall:
        """Fetch the call specified by the provided Call SID

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Call
                resource(s) to fetch.
            sid: The SID of the Call resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_call(account_sid, sid, request_options=request_options)).unwrap()

    async def list_call(
        self,
        account_sid: str,
        *,
        to: str | None = None,
        from_: str | None = None,
        parent_call_sid: str | None = None,
        status: CallEnumStatusOrStr | None = None,
        start_time: RFC3339DateTime | None = None,
        start_time_query: RFC3339DateTime | None = None,
        start_time_query_query: RFC3339DateTime | None = None,
        end_time: RFC3339DateTime | None = None,
        end_time_query: RFC3339DateTime | None = None,
        end_time_query_query: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCallResponse:
        """Retrieves a collection of calls made to and from your account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Call
                resource(s) to read.
            to: Only show calls made to this phone number, SIP address, Client identifier or SIM SID.
            from_: Only include calls from this phone number, SIP address, Client identifier or SIM SID.
            parent_call_sid: Only include calls spawned by calls with this SID.
            status: The status of the calls to include. Can be: ``queued``, ``ringing``, ``in-progress``, ``canceled``,
                ``completed``, ``failed``, ``busy``, or ``no-answer``.
            start_time: Only include calls that started on this date. Specify a date as ``YYYY-MM-DD`` in UTC, for
                example: ``2009-07-06``, to read only calls that started on this date.
            start_time_query: Only include calls that started before this date. Specify a date as ``YYYY-MM-DD`` in UTC,
                for example: ``2009-07-06``, to read only calls that started before this date.
            start_time_query_query: Only include calls that started on or after this date. Specify a date as
                ``YYYY-MM-DD`` in UTC, for example: ``2009-07-06``, to read only calls that started on or after this
                date.
            end_time: Only include calls that ended on this date. Specify a date as ``YYYY-MM-DD`` in UTC, for example:
                ``2009-07-06``, to read only calls that ended on this date.
            end_time_query: Only include calls that ended before this date. Specify a date as ``YYYY-MM-DD`` in UTC, for
                example: ``2009-07-06``, to read only calls that ended before this date.
            end_time_query_query: Only include calls that ended on or after this date. Specify a date as ``YYYY-MM-DD``
                in UTC, for example: ``2009-07-06``, to read only calls that ended on or after this date.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_call(
                account_sid,
                to=to,
                from_=from_,
                parent_call_sid=parent_call_sid,
                status=status,
                start_time=start_time,
                start_time_query=start_time_query,
                start_time_query_query=start_time_query_query,
                end_time=end_time,
                end_time_query=end_time_query,
                end_time_query_query=end_time_query_query,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_call(
        self,
        account_sid: str,
        sid: str,
        *,
        url: AnyUrl | None = None,
        method: Method1OrStr | None = None,
        status: CallEnumUpdateStatusOrStr | None = None,
        fallback_url: AnyUrl | None = None,
        fallback_method: FallbackMethodOrStr | None = None,
        status_callback: AnyUrl | None = None,
        status_callback_method: StatusCallbackMethod9OrStr | None = None,
        twiml: str | None = None,
        time_limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountCall:
        """Initiates a call redirect or terminates a call

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Call
                resource(s) to update.
            sid: The Twilio-provided string that uniquely identifies the Call resource to update
            url: The absolute URL that returns the TwiML instructions for the call. We will call this URL using the
                ``method`` when the call connects. For more information, see the `Url Parameter
                <https://www.twilio.com/docs/voice/make-calls#specify-a-url-parameter>`__ section in `Making Calls
                <https://www.twilio.com/docs/voice/make-calls>`__.
            method: The HTTP method we should use when calling the ``url``. Can be: ``GET`` or ``POST`` and the default
                is ``POST``. If an ``application_sid`` parameter is present, this parameter is ignored.
            status: Value sent with the request.
            fallback_url: The URL that we call using the ``fallback_method`` if an error occurs when requesting or
                executing the TwiML at ``url``. If an ``application_sid`` parameter is present, this parameter is
                ignored.
            fallback_method: The HTTP method that we should use to request the ``fallback_url``. Can be: ``GET`` or
                ``POST`` and the default is ``POST``. If an ``application_sid`` parameter is present, this parameter is
                ignored.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application. If no ``status_callback_event`` is specified, we will send the ``completed`` status.
                If an ``application_sid`` parameter is present, this parameter is ignored. URLs must contain a valid
                hostname (underscores are not permitted).
            status_callback_method: The HTTP method we should use when requesting the ``status_callback`` URL. Can be:
                ``GET`` or ``POST`` and the default is ``POST``. If an ``application_sid`` parameter is present, this
                parameter is ignored.
            twiml: TwiML instructions for the call Twilio will use without fetching Twiml from url. Twiml and url
                parameters are mutually exclusive
            time_limit: The maximum duration of the call in seconds. Constraints depend on account and configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_call(
                account_sid,
                sid,
                url=url,
                method=method,
                status=status,
                fallback_url=fallback_url,
                fallback_method=fallback_method,
                status_callback=status_callback,
                status_callback_method=status_callback_method,
                twiml=twiml,
                time_limit=time_limit,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401CallWithRawResponse:
        return self._with_raw_response


class Api20100401CallWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_call(
        self,
        account_sid: str,
        to: str,
        from_: str,
        *,
        method: MethodOrStr | None = None,
        fallback_url: AnyUrl | None = None,
        fallback_method: FallbackMethodOrStr | None = None,
        status_callback: AnyUrl | None = None,
        status_callback_event: list[str] | None = None,
        status_callback_method: StatusCallbackMethod8OrStr | None = None,
        send_digits: str | None = None,
        timeout: int | None = None,
        record: bool | None = None,
        recording_channels: str | None = None,
        recording_status_callback: str | None = None,
        recording_status_callback_method: RecordingStatusCallbackMethodOrStr | None = None,
        recording_configuration_id: str | None = None,
        sip_auth_username: str | None = None,
        sip_auth_password: str | None = None,
        machine_detection: str | None = None,
        machine_detection_timeout: int | None = None,
        recording_status_callback_event: list[str] | None = None,
        trim: str | None = None,
        caller_id: str | None = None,
        machine_detection_speech_threshold: int | None = None,
        machine_detection_speech_end_threshold: int | None = None,
        machine_detection_silence_timeout: int | None = None,
        async_amd: str | None = None,
        async_amd_status_callback: AnyUrl | None = None,
        async_amd_status_callback_method: AsyncAmdStatusCallbackMethodOrStr | None = None,
        byoc: str | None = None,
        call_reason: str | None = None,
        call_token: str | None = None,
        recording_track: str | None = None,
        time_limit: int | None = None,
        client_notification_url: AnyUrl | None = None,
        url: AnyUrl | None = None,
        twiml: str | None = None,
        application_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountCall, RawError]:
        """Create a new outgoing call to phones, SIP-enabled endpoints or Twilio Client connections

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            to: The phone number, SIP address, or client identifier to call.
            from_: The phone number or client identifier to use as the caller id. If using a phone number, it must be a
                Twilio number or a Verified `outgoing caller id
                <https://www.twilio.com/docs/voice/api/outgoing-caller-ids>`__ for your account. If the ``to`` parameter
                is a phone number, ``From`` must also be a phone number.
            method: The HTTP method we should use when calling the ``url`` parameter's value. Can be: ``GET`` or
                ``POST`` and the default is ``POST``. If an ``application_sid`` parameter is present, this parameter is
                ignored.
            fallback_url: The URL that we call using the ``fallback_method`` if an error occurs when requesting or
                executing the TwiML at ``url``. If an ``application_sid`` parameter is present, this parameter is
                ignored.
            fallback_method: The HTTP method that we should use to request the ``fallback_url``. Can be: ``GET`` or
                ``POST`` and the default is ``POST``. If an ``application_sid`` parameter is present, this parameter is
                ignored.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application. If no ``status_callback_event`` is specified, we will send the ``completed`` status.
                If an ``application_sid`` parameter is present, this parameter is ignored. URLs must contain a valid
                hostname (underscores are not permitted).
            status_callback_event: The call progress events that we will send to the ``status_callback`` URL. Can be:
                ``initiated``, ``ringing``, ``answered``, and ``completed``. If no event is specified, we send the
                ``completed`` status. If you want to receive multiple events, specify each one in a separate
                ``status_callback_event`` parameter. See the code sample for `monitoring call progress
                <https://www.twilio.com/docs/voice/api/call-resource?code-sample=code-create-a-call-resource-and-specify-a-statuscallbackevent&code-sdk-version=json>`__.
                If an ``application_sid`` is present, this parameter is ignored.
            status_callback_method: The HTTP method we should use when calling the ``status_callback`` URL. Can be:
                ``GET`` or ``POST`` and the default is ``POST``. If an ``application_sid`` parameter is present, this
                parameter is ignored.
            send_digits: The string of keys to dial after connecting to the number, with a maximum length of 32 digits.
                Valid digits in the string include any digit (``0``-``9``), '``A``', '``B``', '``C``', '``D``', '``#``',
                and '``*``'. You can also use '``w``' to insert a half-second pause and '``W``' to insert a one-second
                pause. For example, to pause for one second after connecting and then dial extension 1234 followed by
                the # key, set this parameter to ``W1234#``. Be sure to URL-encode this string because the '``#``'
                character has special meaning in a URL. If both ``SendDigits`` and ``MachineDetection`` parameters are
                provided, then ``MachineDetection`` will be ignored.
            timeout: The integer number of seconds that we should allow the phone to ring before assuming there is no
                answer. The default is ``60`` seconds and the maximum is ``600`` seconds. For some call flows, we will
                add a 5-second buffer to the timeout value you provide. For this reason, a timeout value of 10 seconds
                could result in an actual timeout closer to 15 seconds. You can set this to a short time, such as ``15``
                seconds, to hang up before reaching an answering machine or voicemail.
            record: Whether to record the call. Can be ``true`` to record the phone call, or ``false`` to not. The
                default is ``false``. The ``recording_url`` is sent to the ``status_callback`` URL.
            recording_channels: The number of channels in the final recording. Can be: ``mono`` or ``dual``. The default
                is ``mono``. ``mono`` records both legs of the call in a single channel of the recording file. ``dual``
                records each leg to a separate channel of the recording file. The first channel of a dual-channel
                recording contains the parent call and the second channel contains the child call.
            recording_status_callback: The URL that we call when the recording is available to be accessed.
            recording_status_callback_method: The HTTP method we should use when calling the
                ``recording_status_callback`` URL. Can be: ``GET`` or ``POST`` and the default is ``POST``.
            recording_configuration_id: The identifier of the configuration to be used when creating and processing the
                recording
            sip_auth_username: The username used to authenticate the caller making a SIP call.
            sip_auth_password: The password required to authenticate the user account specified in
                ``sip_auth_username``.
            machine_detection: Whether to detect if a human, answering machine, or fax has picked up the call. Can be:
                ``Enable`` or ``DetectMessageEnd``. Use ``Enable`` if you would like us to return ``AnsweredBy`` as soon
                as the called party is identified. Use ``DetectMessageEnd``, if you would like to leave a message on an
                answering machine. If ``send_digits`` is provided, this parameter is ignored. For more information, see
                `Answering Machine Detection <https://www.twilio.com/docs/voice/answering-machine-detection>`__.
            machine_detection_timeout: The number of seconds that we should attempt to detect an answering machine
                before timing out and sending a voice request with ``AnsweredBy`` of ``unknown``. The default timeout is
                30 seconds.
            recording_status_callback_event: The recording status events that will trigger calls to the URL specified in
                ``recording_status_callback``. Can be: ``in-progress``, ``completed`` and ``absent``. Defaults to
                ``completed``. Separate multiple values with a space.
            trim: Whether to trim any leading and trailing silence from the recording. Can be: ``trim-silence`` or
                ``do-not-trim`` and the default is ``trim-silence``.
            caller_id: The phone number, SIP address, or Client identifier that made this call. Phone numbers are in
                `E.164 format <https://wwnw.twilio.com/docs/glossary/what-e164>`__ (e.g., +16175551212). SIP addresses
                are formatted as ``name@company.com``.
            machine_detection_speech_threshold: The number of milliseconds that is used as the measuring stick for the
                length of the speech activity, where durations lower than this value will be interpreted as a human and
                longer than this value as a machine. Possible Values: 1000-6000. Default: 2400.
            machine_detection_speech_end_threshold: The number of milliseconds of silence after speech activity at which
                point the speech activity is considered complete. Possible Values: 500-5000. Default: 1200.
            machine_detection_silence_timeout: The number of milliseconds of initial silence after which an ``unknown``
                AnsweredBy result will be returned. Possible Values: 2000-10000. Default: 5000.
            async_amd: Select whether to perform answering machine detection in the background. Default, blocks the
                execution of the call until Answering Machine Detection is completed. Can be: ``true`` or ``false``.
            async_amd_status_callback: The URL that we should call using the ``async_amd_status_callback_method`` to
                notify customer application whether the call was answered by human, machine or fax.
            async_amd_status_callback_method: The HTTP method we should use when calling the
                ``async_amd_status_callback`` URL. Can be: ``GET`` or ``POST`` and the default is ``POST``.
            byoc: The SID of a BYOC (Bring Your Own Carrier) trunk to route this call with. Note that ``byoc`` is only
                meaningful when ``to`` is a phone number; it will otherwise be ignored. (Beta)
            call_reason: The Reason for the outgoing call. Use it to specify the purpose of the call that is presented
                on the called party's phone. (Branded Calls Beta)
            call_token: A token string needed to invoke a forwarded call. A call_token is generated when an incoming
                call is received on a Twilio number. Pass an incoming call's call_token value to a forwarded call via
                the call_token parameter when creating a new call. A forwarded call should bear the same CallerID of the
                original incoming call.
            recording_track: The audio track to record for the call. Can be: ``inbound``, ``outbound`` or ``both``. The
                default is ``both``. ``inbound`` records the audio that is received by Twilio. ``outbound`` records the
                audio that is generated from Twilio. ``both`` records the audio that is received and generated by
                Twilio.
            time_limit: The maximum duration of the call in seconds. Constraints depend on account and configuration.
            client_notification_url: The URL that we should use to deliver ``push call notification``.
            url: The absolute URL that returns the TwiML instructions for the call. We will call this URL using the
                ``method`` when the call connects. For more information, see the `Url Parameter
                <https://www.twilio.com/docs/voice/make-calls#specify-a-url-parameter>`__ section in `Making Calls
                <https://www.twilio.com/docs/voice/make-calls>`__.
            twiml: TwiML instructions for the call Twilio will use without fetching Twiml from url parameter. If both
                ``twiml`` and ``url`` are provided then ``twiml`` parameter will be ignored. Max 4000 characters.
            application_sid: The SID of the Application resource that will handle the call, if the call will be handled
                by an application.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Calls.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            body=form_body(
                [
                    param[str]("To", to),
                    param[str]("From", from_),
                    param[MethodOrStr | None]("Method", method),
                    param[AnyUrl | None]("FallbackUrl", fallback_url),
                    param[FallbackMethodOrStr | None]("FallbackMethod", fallback_method),
                    param[AnyUrl | None]("StatusCallback", status_callback),
                    param[list[str] | None]("StatusCallbackEvent", status_callback_event),
                    param[StatusCallbackMethod8OrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[str | None]("SendDigits", send_digits),
                    param[int | None]("Timeout", timeout),
                    param[bool | None]("Record", record),
                    param[str | None]("RecordingChannels", recording_channels),
                    param[str | None]("RecordingStatusCallback", recording_status_callback),
                    param[RecordingStatusCallbackMethodOrStr | None](
                        "RecordingStatusCallbackMethod", recording_status_callback_method
                    ),
                    param[str | None]("RecordingConfigurationId", recording_configuration_id),
                    param[str | None]("SipAuthUsername", sip_auth_username),
                    param[str | None]("SipAuthPassword", sip_auth_password),
                    param[str | None]("MachineDetection", machine_detection),
                    param[int | None]("MachineDetectionTimeout", machine_detection_timeout),
                    param[list[str] | None]("RecordingStatusCallbackEvent", recording_status_callback_event),
                    param[str | None]("Trim", trim),
                    param[str | None]("CallerId", caller_id),
                    param[int | None]("MachineDetectionSpeechThreshold", machine_detection_speech_threshold),
                    param[int | None]("MachineDetectionSpeechEndThreshold", machine_detection_speech_end_threshold),
                    param[int | None]("MachineDetectionSilenceTimeout", machine_detection_silence_timeout),
                    param[str | None]("AsyncAmd", async_amd),
                    param[AnyUrl | None]("AsyncAmdStatusCallback", async_amd_status_callback),
                    param[AsyncAmdStatusCallbackMethodOrStr | None](
                        "AsyncAmdStatusCallbackMethod", async_amd_status_callback_method
                    ),
                    param[str | None]("Byoc", byoc),
                    param[str | None]("CallReason", call_reason),
                    param[str | None]("CallToken", call_token),
                    param[str | None]("RecordingTrack", recording_track),
                    param[int | None]("TimeLimit", time_limit),
                    param[AnyUrl | None]("ClientNotificationUrl", client_notification_url),
                    param[AnyUrl | None]("Url", url),
                    param[str | None]("Twiml", twiml),
                    param[str | None]("ApplicationSid", application_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountCall],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_call(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a Call record from your account. Once the record is deleted, it will no longer appear in the API and
        Account Portal logs.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Call
                resource(s) to delete.
            sid: The Twilio-provided Call SID that uniquely identifies the Call resource to delete
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Calls/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_call(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountCall, RawError]:
        """Fetch the call specified by the provided Call SID

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Call
                resource(s) to fetch.
            sid: The SID of the Call resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Calls/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountCall],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_call(
        self,
        account_sid: str,
        *,
        to: str | None = None,
        from_: str | None = None,
        parent_call_sid: str | None = None,
        status: CallEnumStatusOrStr | None = None,
        start_time: RFC3339DateTime | None = None,
        start_time_query: RFC3339DateTime | None = None,
        start_time_query_query: RFC3339DateTime | None = None,
        end_time: RFC3339DateTime | None = None,
        end_time_query: RFC3339DateTime | None = None,
        end_time_query_query: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCallResponse, RawError]:
        """Retrieves a collection of calls made to and from your account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Call
                resource(s) to read.
            to: Only show calls made to this phone number, SIP address, Client identifier or SIM SID.
            from_: Only include calls from this phone number, SIP address, Client identifier or SIM SID.
            parent_call_sid: Only include calls spawned by calls with this SID.
            status: The status of the calls to include. Can be: ``queued``, ``ringing``, ``in-progress``, ``canceled``,
                ``completed``, ``failed``, ``busy``, or ``no-answer``.
            start_time: Only include calls that started on this date. Specify a date as ``YYYY-MM-DD`` in UTC, for
                example: ``2009-07-06``, to read only calls that started on this date.
            start_time_query: Only include calls that started before this date. Specify a date as ``YYYY-MM-DD`` in UTC,
                for example: ``2009-07-06``, to read only calls that started before this date.
            start_time_query_query: Only include calls that started on or after this date. Specify a date as
                ``YYYY-MM-DD`` in UTC, for example: ``2009-07-06``, to read only calls that started on or after this
                date.
            end_time: Only include calls that ended on this date. Specify a date as ``YYYY-MM-DD`` in UTC, for example:
                ``2009-07-06``, to read only calls that ended on this date.
            end_time_query: Only include calls that ended before this date. Specify a date as ``YYYY-MM-DD`` in UTC, for
                example: ``2009-07-06``, to read only calls that ended before this date.
            end_time_query_query: Only include calls that ended on or after this date. Specify a date as ``YYYY-MM-DD``
                in UTC, for example: ``2009-07-06``, to read only calls that ended on or after this date.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Calls.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[str | None]("To", to),
                param[str | None]("From", from_),
                param[str | None]("ParentCallSid", parent_call_sid),
                param[CallEnumStatusOrStr | None]("Status", status),
                param[RFC3339DateTime | None]("StartTime", start_time),
                param[RFC3339DateTime | None]("StartTime<", start_time_query),
                param[RFC3339DateTime | None]("StartTime>", start_time_query_query),
                param[RFC3339DateTime | None]("EndTime", end_time),
                param[RFC3339DateTime | None]("EndTime<", end_time_query),
                param[RFC3339DateTime | None]("EndTime>", end_time_query_query),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListCallResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_call(
        self,
        account_sid: str,
        sid: str,
        *,
        url: AnyUrl | None = None,
        method: Method1OrStr | None = None,
        status: CallEnumUpdateStatusOrStr | None = None,
        fallback_url: AnyUrl | None = None,
        fallback_method: FallbackMethodOrStr | None = None,
        status_callback: AnyUrl | None = None,
        status_callback_method: StatusCallbackMethod9OrStr | None = None,
        twiml: str | None = None,
        time_limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountCall, RawError]:
        """Initiates a call redirect or terminates a call

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Call
                resource(s) to update.
            sid: The Twilio-provided string that uniquely identifies the Call resource to update
            url: The absolute URL that returns the TwiML instructions for the call. We will call this URL using the
                ``method`` when the call connects. For more information, see the `Url Parameter
                <https://www.twilio.com/docs/voice/make-calls#specify-a-url-parameter>`__ section in `Making Calls
                <https://www.twilio.com/docs/voice/make-calls>`__.
            method: The HTTP method we should use when calling the ``url``. Can be: ``GET`` or ``POST`` and the default
                is ``POST``. If an ``application_sid`` parameter is present, this parameter is ignored.
            status: Value sent with the request.
            fallback_url: The URL that we call using the ``fallback_method`` if an error occurs when requesting or
                executing the TwiML at ``url``. If an ``application_sid`` parameter is present, this parameter is
                ignored.
            fallback_method: The HTTP method that we should use to request the ``fallback_url``. Can be: ``GET`` or
                ``POST`` and the default is ``POST``. If an ``application_sid`` parameter is present, this parameter is
                ignored.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application. If no ``status_callback_event`` is specified, we will send the ``completed`` status.
                If an ``application_sid`` parameter is present, this parameter is ignored. URLs must contain a valid
                hostname (underscores are not permitted).
            status_callback_method: The HTTP method we should use when requesting the ``status_callback`` URL. Can be:
                ``GET`` or ``POST`` and the default is ``POST``. If an ``application_sid`` parameter is present, this
                parameter is ignored.
            twiml: TwiML instructions for the call Twilio will use without fetching Twiml from url. Twiml and url
                parameters are mutually exclusive
            time_limit: The maximum duration of the call in seconds. Constraints depend on account and configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Calls/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            body=form_body(
                [
                    param[AnyUrl | None]("Url", url),
                    param[Method1OrStr | None]("Method", method),
                    param[CallEnumUpdateStatusOrStr | None]("Status", status),
                    param[AnyUrl | None]("FallbackUrl", fallback_url),
                    param[FallbackMethodOrStr | None]("FallbackMethod", fallback_method),
                    param[AnyUrl | None]("StatusCallback", status_callback),
                    param[StatusCallbackMethod9OrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[str | None]("Twiml", twiml),
                    param[int | None]("TimeLimit", time_limit),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountCall],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401CallWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_call(
        self,
        account_sid: str,
        to: str,
        from_: str,
        *,
        method: MethodOrStr | None = None,
        fallback_url: AnyUrl | None = None,
        fallback_method: FallbackMethodOrStr | None = None,
        status_callback: AnyUrl | None = None,
        status_callback_event: list[str] | None = None,
        status_callback_method: StatusCallbackMethod8OrStr | None = None,
        send_digits: str | None = None,
        timeout: int | None = None,
        record: bool | None = None,
        recording_channels: str | None = None,
        recording_status_callback: str | None = None,
        recording_status_callback_method: RecordingStatusCallbackMethodOrStr | None = None,
        recording_configuration_id: str | None = None,
        sip_auth_username: str | None = None,
        sip_auth_password: str | None = None,
        machine_detection: str | None = None,
        machine_detection_timeout: int | None = None,
        recording_status_callback_event: list[str] | None = None,
        trim: str | None = None,
        caller_id: str | None = None,
        machine_detection_speech_threshold: int | None = None,
        machine_detection_speech_end_threshold: int | None = None,
        machine_detection_silence_timeout: int | None = None,
        async_amd: str | None = None,
        async_amd_status_callback: AnyUrl | None = None,
        async_amd_status_callback_method: AsyncAmdStatusCallbackMethodOrStr | None = None,
        byoc: str | None = None,
        call_reason: str | None = None,
        call_token: str | None = None,
        recording_track: str | None = None,
        time_limit: int | None = None,
        client_notification_url: AnyUrl | None = None,
        url: AnyUrl | None = None,
        twiml: str | None = None,
        application_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountCall, RawError]:
        """Create a new outgoing call to phones, SIP-enabled endpoints or Twilio Client connections

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            to: The phone number, SIP address, or client identifier to call.
            from_: The phone number or client identifier to use as the caller id. If using a phone number, it must be a
                Twilio number or a Verified `outgoing caller id
                <https://www.twilio.com/docs/voice/api/outgoing-caller-ids>`__ for your account. If the ``to`` parameter
                is a phone number, ``From`` must also be a phone number.
            method: The HTTP method we should use when calling the ``url`` parameter's value. Can be: ``GET`` or
                ``POST`` and the default is ``POST``. If an ``application_sid`` parameter is present, this parameter is
                ignored.
            fallback_url: The URL that we call using the ``fallback_method`` if an error occurs when requesting or
                executing the TwiML at ``url``. If an ``application_sid`` parameter is present, this parameter is
                ignored.
            fallback_method: The HTTP method that we should use to request the ``fallback_url``. Can be: ``GET`` or
                ``POST`` and the default is ``POST``. If an ``application_sid`` parameter is present, this parameter is
                ignored.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application. If no ``status_callback_event`` is specified, we will send the ``completed`` status.
                If an ``application_sid`` parameter is present, this parameter is ignored. URLs must contain a valid
                hostname (underscores are not permitted).
            status_callback_event: The call progress events that we will send to the ``status_callback`` URL. Can be:
                ``initiated``, ``ringing``, ``answered``, and ``completed``. If no event is specified, we send the
                ``completed`` status. If you want to receive multiple events, specify each one in a separate
                ``status_callback_event`` parameter. See the code sample for `monitoring call progress
                <https://www.twilio.com/docs/voice/api/call-resource?code-sample=code-create-a-call-resource-and-specify-a-statuscallbackevent&code-sdk-version=json>`__.
                If an ``application_sid`` is present, this parameter is ignored.
            status_callback_method: The HTTP method we should use when calling the ``status_callback`` URL. Can be:
                ``GET`` or ``POST`` and the default is ``POST``. If an ``application_sid`` parameter is present, this
                parameter is ignored.
            send_digits: The string of keys to dial after connecting to the number, with a maximum length of 32 digits.
                Valid digits in the string include any digit (``0``-``9``), '``A``', '``B``', '``C``', '``D``', '``#``',
                and '``*``'. You can also use '``w``' to insert a half-second pause and '``W``' to insert a one-second
                pause. For example, to pause for one second after connecting and then dial extension 1234 followed by
                the # key, set this parameter to ``W1234#``. Be sure to URL-encode this string because the '``#``'
                character has special meaning in a URL. If both ``SendDigits`` and ``MachineDetection`` parameters are
                provided, then ``MachineDetection`` will be ignored.
            timeout: The integer number of seconds that we should allow the phone to ring before assuming there is no
                answer. The default is ``60`` seconds and the maximum is ``600`` seconds. For some call flows, we will
                add a 5-second buffer to the timeout value you provide. For this reason, a timeout value of 10 seconds
                could result in an actual timeout closer to 15 seconds. You can set this to a short time, such as ``15``
                seconds, to hang up before reaching an answering machine or voicemail.
            record: Whether to record the call. Can be ``true`` to record the phone call, or ``false`` to not. The
                default is ``false``. The ``recording_url`` is sent to the ``status_callback`` URL.
            recording_channels: The number of channels in the final recording. Can be: ``mono`` or ``dual``. The default
                is ``mono``. ``mono`` records both legs of the call in a single channel of the recording file. ``dual``
                records each leg to a separate channel of the recording file. The first channel of a dual-channel
                recording contains the parent call and the second channel contains the child call.
            recording_status_callback: The URL that we call when the recording is available to be accessed.
            recording_status_callback_method: The HTTP method we should use when calling the
                ``recording_status_callback`` URL. Can be: ``GET`` or ``POST`` and the default is ``POST``.
            recording_configuration_id: The identifier of the configuration to be used when creating and processing the
                recording
            sip_auth_username: The username used to authenticate the caller making a SIP call.
            sip_auth_password: The password required to authenticate the user account specified in
                ``sip_auth_username``.
            machine_detection: Whether to detect if a human, answering machine, or fax has picked up the call. Can be:
                ``Enable`` or ``DetectMessageEnd``. Use ``Enable`` if you would like us to return ``AnsweredBy`` as soon
                as the called party is identified. Use ``DetectMessageEnd``, if you would like to leave a message on an
                answering machine. If ``send_digits`` is provided, this parameter is ignored. For more information, see
                `Answering Machine Detection <https://www.twilio.com/docs/voice/answering-machine-detection>`__.
            machine_detection_timeout: The number of seconds that we should attempt to detect an answering machine
                before timing out and sending a voice request with ``AnsweredBy`` of ``unknown``. The default timeout is
                30 seconds.
            recording_status_callback_event: The recording status events that will trigger calls to the URL specified in
                ``recording_status_callback``. Can be: ``in-progress``, ``completed`` and ``absent``. Defaults to
                ``completed``. Separate multiple values with a space.
            trim: Whether to trim any leading and trailing silence from the recording. Can be: ``trim-silence`` or
                ``do-not-trim`` and the default is ``trim-silence``.
            caller_id: The phone number, SIP address, or Client identifier that made this call. Phone numbers are in
                `E.164 format <https://wwnw.twilio.com/docs/glossary/what-e164>`__ (e.g., +16175551212). SIP addresses
                are formatted as ``name@company.com``.
            machine_detection_speech_threshold: The number of milliseconds that is used as the measuring stick for the
                length of the speech activity, where durations lower than this value will be interpreted as a human and
                longer than this value as a machine. Possible Values: 1000-6000. Default: 2400.
            machine_detection_speech_end_threshold: The number of milliseconds of silence after speech activity at which
                point the speech activity is considered complete. Possible Values: 500-5000. Default: 1200.
            machine_detection_silence_timeout: The number of milliseconds of initial silence after which an ``unknown``
                AnsweredBy result will be returned. Possible Values: 2000-10000. Default: 5000.
            async_amd: Select whether to perform answering machine detection in the background. Default, blocks the
                execution of the call until Answering Machine Detection is completed. Can be: ``true`` or ``false``.
            async_amd_status_callback: The URL that we should call using the ``async_amd_status_callback_method`` to
                notify customer application whether the call was answered by human, machine or fax.
            async_amd_status_callback_method: The HTTP method we should use when calling the
                ``async_amd_status_callback`` URL. Can be: ``GET`` or ``POST`` and the default is ``POST``.
            byoc: The SID of a BYOC (Bring Your Own Carrier) trunk to route this call with. Note that ``byoc`` is only
                meaningful when ``to`` is a phone number; it will otherwise be ignored. (Beta)
            call_reason: The Reason for the outgoing call. Use it to specify the purpose of the call that is presented
                on the called party's phone. (Branded Calls Beta)
            call_token: A token string needed to invoke a forwarded call. A call_token is generated when an incoming
                call is received on a Twilio number. Pass an incoming call's call_token value to a forwarded call via
                the call_token parameter when creating a new call. A forwarded call should bear the same CallerID of the
                original incoming call.
            recording_track: The audio track to record for the call. Can be: ``inbound``, ``outbound`` or ``both``. The
                default is ``both``. ``inbound`` records the audio that is received by Twilio. ``outbound`` records the
                audio that is generated from Twilio. ``both`` records the audio that is received and generated by
                Twilio.
            time_limit: The maximum duration of the call in seconds. Constraints depend on account and configuration.
            client_notification_url: The URL that we should use to deliver ``push call notification``.
            url: The absolute URL that returns the TwiML instructions for the call. We will call this URL using the
                ``method`` when the call connects. For more information, see the `Url Parameter
                <https://www.twilio.com/docs/voice/make-calls#specify-a-url-parameter>`__ section in `Making Calls
                <https://www.twilio.com/docs/voice/make-calls>`__.
            twiml: TwiML instructions for the call Twilio will use without fetching Twiml from url parameter. If both
                ``twiml`` and ``url`` are provided then ``twiml`` parameter will be ignored. Max 4000 characters.
            application_sid: The SID of the Application resource that will handle the call, if the call will be handled
                by an application.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Calls.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            body=form_body(
                [
                    param[str]("To", to),
                    param[str]("From", from_),
                    param[MethodOrStr | None]("Method", method),
                    param[AnyUrl | None]("FallbackUrl", fallback_url),
                    param[FallbackMethodOrStr | None]("FallbackMethod", fallback_method),
                    param[AnyUrl | None]("StatusCallback", status_callback),
                    param[list[str] | None]("StatusCallbackEvent", status_callback_event),
                    param[StatusCallbackMethod8OrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[str | None]("SendDigits", send_digits),
                    param[int | None]("Timeout", timeout),
                    param[bool | None]("Record", record),
                    param[str | None]("RecordingChannels", recording_channels),
                    param[str | None]("RecordingStatusCallback", recording_status_callback),
                    param[RecordingStatusCallbackMethodOrStr | None](
                        "RecordingStatusCallbackMethod", recording_status_callback_method
                    ),
                    param[str | None]("RecordingConfigurationId", recording_configuration_id),
                    param[str | None]("SipAuthUsername", sip_auth_username),
                    param[str | None]("SipAuthPassword", sip_auth_password),
                    param[str | None]("MachineDetection", machine_detection),
                    param[int | None]("MachineDetectionTimeout", machine_detection_timeout),
                    param[list[str] | None]("RecordingStatusCallbackEvent", recording_status_callback_event),
                    param[str | None]("Trim", trim),
                    param[str | None]("CallerId", caller_id),
                    param[int | None]("MachineDetectionSpeechThreshold", machine_detection_speech_threshold),
                    param[int | None]("MachineDetectionSpeechEndThreshold", machine_detection_speech_end_threshold),
                    param[int | None]("MachineDetectionSilenceTimeout", machine_detection_silence_timeout),
                    param[str | None]("AsyncAmd", async_amd),
                    param[AnyUrl | None]("AsyncAmdStatusCallback", async_amd_status_callback),
                    param[AsyncAmdStatusCallbackMethodOrStr | None](
                        "AsyncAmdStatusCallbackMethod", async_amd_status_callback_method
                    ),
                    param[str | None]("Byoc", byoc),
                    param[str | None]("CallReason", call_reason),
                    param[str | None]("CallToken", call_token),
                    param[str | None]("RecordingTrack", recording_track),
                    param[int | None]("TimeLimit", time_limit),
                    param[AnyUrl | None]("ClientNotificationUrl", client_notification_url),
                    param[AnyUrl | None]("Url", url),
                    param[str | None]("Twiml", twiml),
                    param[str | None]("ApplicationSid", application_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountCall],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_call(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a Call record from your account. Once the record is deleted, it will no longer appear in the API and
        Account Portal logs.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Call
                resource(s) to delete.
            sid: The Twilio-provided Call SID that uniquely identifies the Call resource to delete
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Calls/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_call(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountCall, RawError]:
        """Fetch the call specified by the provided Call SID

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Call
                resource(s) to fetch.
            sid: The SID of the Call resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Calls/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountCall],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_call(
        self,
        account_sid: str,
        *,
        to: str | None = None,
        from_: str | None = None,
        parent_call_sid: str | None = None,
        status: CallEnumStatusOrStr | None = None,
        start_time: RFC3339DateTime | None = None,
        start_time_query: RFC3339DateTime | None = None,
        start_time_query_query: RFC3339DateTime | None = None,
        end_time: RFC3339DateTime | None = None,
        end_time_query: RFC3339DateTime | None = None,
        end_time_query_query: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCallResponse, RawError]:
        """Retrieves a collection of calls made to and from your account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Call
                resource(s) to read.
            to: Only show calls made to this phone number, SIP address, Client identifier or SIM SID.
            from_: Only include calls from this phone number, SIP address, Client identifier or SIM SID.
            parent_call_sid: Only include calls spawned by calls with this SID.
            status: The status of the calls to include. Can be: ``queued``, ``ringing``, ``in-progress``, ``canceled``,
                ``completed``, ``failed``, ``busy``, or ``no-answer``.
            start_time: Only include calls that started on this date. Specify a date as ``YYYY-MM-DD`` in UTC, for
                example: ``2009-07-06``, to read only calls that started on this date.
            start_time_query: Only include calls that started before this date. Specify a date as ``YYYY-MM-DD`` in UTC,
                for example: ``2009-07-06``, to read only calls that started before this date.
            start_time_query_query: Only include calls that started on or after this date. Specify a date as
                ``YYYY-MM-DD`` in UTC, for example: ``2009-07-06``, to read only calls that started on or after this
                date.
            end_time: Only include calls that ended on this date. Specify a date as ``YYYY-MM-DD`` in UTC, for example:
                ``2009-07-06``, to read only calls that ended on this date.
            end_time_query: Only include calls that ended before this date. Specify a date as ``YYYY-MM-DD`` in UTC, for
                example: ``2009-07-06``, to read only calls that ended before this date.
            end_time_query_query: Only include calls that ended on or after this date. Specify a date as ``YYYY-MM-DD``
                in UTC, for example: ``2009-07-06``, to read only calls that ended on or after this date.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Calls.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[str | None]("To", to),
                param[str | None]("From", from_),
                param[str | None]("ParentCallSid", parent_call_sid),
                param[CallEnumStatusOrStr | None]("Status", status),
                param[RFC3339DateTime | None]("StartTime", start_time),
                param[RFC3339DateTime | None]("StartTime<", start_time_query),
                param[RFC3339DateTime | None]("StartTime>", start_time_query_query),
                param[RFC3339DateTime | None]("EndTime", end_time),
                param[RFC3339DateTime | None]("EndTime<", end_time_query),
                param[RFC3339DateTime | None]("EndTime>", end_time_query_query),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListCallResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_call(
        self,
        account_sid: str,
        sid: str,
        *,
        url: AnyUrl | None = None,
        method: Method1OrStr | None = None,
        status: CallEnumUpdateStatusOrStr | None = None,
        fallback_url: AnyUrl | None = None,
        fallback_method: FallbackMethodOrStr | None = None,
        status_callback: AnyUrl | None = None,
        status_callback_method: StatusCallbackMethod9OrStr | None = None,
        twiml: str | None = None,
        time_limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountCall, RawError]:
        """Initiates a call redirect or terminates a call

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Call
                resource(s) to update.
            sid: The Twilio-provided string that uniquely identifies the Call resource to update
            url: The absolute URL that returns the TwiML instructions for the call. We will call this URL using the
                ``method`` when the call connects. For more information, see the `Url Parameter
                <https://www.twilio.com/docs/voice/make-calls#specify-a-url-parameter>`__ section in `Making Calls
                <https://www.twilio.com/docs/voice/make-calls>`__.
            method: The HTTP method we should use when calling the ``url``. Can be: ``GET`` or ``POST`` and the default
                is ``POST``. If an ``application_sid`` parameter is present, this parameter is ignored.
            status: Value sent with the request.
            fallback_url: The URL that we call using the ``fallback_method`` if an error occurs when requesting or
                executing the TwiML at ``url``. If an ``application_sid`` parameter is present, this parameter is
                ignored.
            fallback_method: The HTTP method that we should use to request the ``fallback_url``. Can be: ``GET`` or
                ``POST`` and the default is ``POST``. If an ``application_sid`` parameter is present, this parameter is
                ignored.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application. If no ``status_callback_event`` is specified, we will send the ``completed`` status.
                If an ``application_sid`` parameter is present, this parameter is ignored. URLs must contain a valid
                hostname (underscores are not permitted).
            status_callback_method: The HTTP method we should use when requesting the ``status_callback`` URL. Can be:
                ``GET`` or ``POST`` and the default is ``POST``. If an ``application_sid`` parameter is present, this
                parameter is ignored.
            twiml: TwiML instructions for the call Twilio will use without fetching Twiml from url. Twiml and url
                parameters are mutually exclusive
            time_limit: The maximum duration of the call in seconds. Constraints depend on account and configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Calls/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            body=form_body(
                [
                    param[AnyUrl | None]("Url", url),
                    param[Method1OrStr | None]("Method", method),
                    param[CallEnumUpdateStatusOrStr | None]("Status", status),
                    param[AnyUrl | None]("FallbackUrl", fallback_url),
                    param[FallbackMethodOrStr | None]("FallbackMethod", fallback_method),
                    param[AnyUrl | None]("StatusCallback", status_callback),
                    param[StatusCallbackMethod9OrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[str | None]("Twiml", twiml),
                    param[int | None]("TimeLimit", time_limit),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountCall],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
