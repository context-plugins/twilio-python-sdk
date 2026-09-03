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
from ..models.enums.amd_status_callback_method import AmdStatusCallbackMethodOrStr
from ..models.enums.call_enum_event import CallEnumEventOrStr
from ..models.enums.task_reservation_enum_conference_event import TaskReservationEnumConferenceEventOrStr
from ..models.enums.task_reservation_enum_status import TaskReservationEnumStatusOrStr
from ..models.enums.task_reservation_enum_supervisor_mode import TaskReservationEnumSupervisorModeOrStr
from ..models.list_task_reservation_response import ListTaskReservationResponse
from ..models.taskrouter_v1_workspace_task_task_reservation import TaskrouterV1WorkspaceTaskTaskReservation
from ..server.server import Server


class TaskrouterV1TaskReservation:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TaskrouterV1TaskReservationWithRawResponse(client, server, auth)

    def fetch_task_reservation(
        self, workspace_sid: str, task_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TaskrouterV1WorkspaceTaskTaskReservation:
        """Tasks reserved for workers

        Args:
            workspace_sid: The SID of the Workspace with the TaskReservation resource to fetch.
            task_sid: The SID of the reserved Task resource with the TaskReservation resource to fetch.
            sid: The SID of the TaskReservation resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_task_reservation(
            workspace_sid, task_sid, sid, request_options=request_options
        ).unwrap()

    def list_task_reservation(
        self,
        workspace_sid: str,
        task_sid: str,
        *,
        reservation_status: TaskReservationEnumStatusOrStr | None = None,
        worker_sid: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTaskReservationResponse:
        """Tasks reserved for workers

        Args:
            workspace_sid: The SID of the Workspace with the TaskReservation resources to read.
            task_sid: The SID of the reserved Task resource with the TaskReservation resources to read.
            reservation_status: Returns the list of reservations for a task with a specified ReservationStatus. Can be:
                ``pending``, ``accepted``, ``rejected``, or ``timeout``.
            worker_sid: The SID of the reserved Worker resource to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_task_reservation(
            workspace_sid,
            task_sid,
            reservation_status=reservation_status,
            worker_sid=worker_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_task_reservation(
        self,
        workspace_sid: str,
        task_sid: str,
        sid: str,
        *,
        if_match: str | None = None,
        reservation_status: TaskReservationEnumStatusOrStr | None = None,
        worker_activity_sid: str | None = None,
        instruction: str | None = None,
        dequeue_post_work_activity_sid: str | None = None,
        dequeue_from: str | None = None,
        dequeue_record: str | None = None,
        dequeue_timeout: int | None = None,
        dequeue_to: str | None = None,
        dequeue_status_callback_url: str | None = None,
        call_from: str | None = None,
        call_record: str | None = None,
        call_timeout: int | None = None,
        call_to: str | None = None,
        call_url: str | None = None,
        call_status_callback_url: str | None = None,
        call_accept: bool | None = None,
        redirect_call_sid: str | None = None,
        redirect_accept: bool | None = None,
        redirect_url: str | None = None,
        to: str | None = None,
        from_: str | None = None,
        status_callback: str | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        status_callback_event: list[CallEnumEventOrStr] | None = None,
        timeout: int | None = None,
        record: bool | None = None,
        muted: bool | None = None,
        beep: str | None = None,
        start_conference_on_enter: bool | None = None,
        end_conference_on_exit: bool | None = None,
        wait_url: str | None = None,
        wait_method: AmdStatusCallbackMethodOrStr | None = None,
        early_media: bool | None = None,
        max_participants: int | None = None,
        conference_status_callback: str | None = None,
        conference_status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        conference_status_callback_event: list[TaskReservationEnumConferenceEventOrStr] | None = None,
        conference_record: str | None = None,
        conference_trim: str | None = None,
        recording_channels: str | None = None,
        recording_status_callback: str | None = None,
        recording_status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        conference_recording_status_callback: str | None = None,
        conference_recording_status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        region: str | None = None,
        sip_auth_username: str | None = None,
        sip_auth_password: str | None = None,
        dequeue_status_callback_event: list[str] | None = None,
        post_work_activity_sid: str | None = None,
        supervisor_mode: TaskReservationEnumSupervisorModeOrStr | None = None,
        supervisor: str | None = None,
        end_conference_on_customer_exit: bool | None = None,
        beep_on_customer_entrance: bool | None = None,
        jitter_buffer_size: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceTaskTaskReservation:
        """Tasks reserved for workers

        Args:
            workspace_sid: The SID of the Workspace with the TaskReservation resources to update.
            task_sid: The SID of the reserved Task resource with the TaskReservation resources to update.
            sid: The SID of the TaskReservation resource to update.
            if_match: The If-Match HTTP request header
            reservation_status: The current status of the reservation. Can be: ``pending``, ``accepted``, ``rejected``,
                or ``timeout``.
            worker_activity_sid: The new worker activity SID if rejecting a reservation.
            instruction: The assignment instruction for reservation.
            dequeue_post_work_activity_sid: The SID of the Activity resource to start after executing a Dequeue
                instruction.
            dequeue_from: The Caller ID of the call to the worker when executing a Dequeue instruction.
            dequeue_record: Whether to record both legs of a call when executing a Dequeue instruction or which leg to
                record.
            dequeue_timeout: Timeout for call when executing a Dequeue instruction.
            dequeue_to: The Contact URI of the worker when executing a Dequeue instruction. Can be the URI of the Twilio
                Client, the SIP URI for Programmable SIP, or the `E.164
                <https://www.twilio.com/docs/glossary/what-e164>`__ formatted phone number, depending on the
                destination.
            dequeue_status_callback_url: The Callback URL for completed call event when executing a Dequeue instruction.
            call_from: The Caller ID of the outbound call when executing a Call instruction.
            call_record: Whether to record both legs of a call when executing a Call instruction or which leg to record.
            call_timeout: Timeout for call when executing a Call instruction.
            call_to: The Contact URI of the worker when executing a Call instruction. Can be the URI of the Twilio
                Client, the SIP URI for Programmable SIP, or the `E.164
                <https://www.twilio.com/docs/glossary/what-e164>`__ formatted phone number, depending on the
                destination.
            call_url: TwiML URI executed on answering the worker's leg as a result of the Call instruction.
            call_status_callback_url: The URL to call for the completed call event when executing a Call instruction.
            call_accept: Whether to accept a reservation when executing a Call instruction.
            redirect_call_sid: The Call SID of the call parked in the queue when executing a Redirect instruction.
            redirect_accept: Whether the reservation should be accepted when executing a Redirect instruction.
            redirect_url: TwiML URI to redirect the call to when executing the Redirect instruction.
            to: The Contact URI of the worker when executing a Conference instruction. Can be the URI of the Twilio
                Client, the SIP URI for Programmable SIP, or the `E.164
                <https://www.twilio.com/docs/glossary/what-e164>`__ formatted phone number, depending on the
                destination.
            from_: The Caller ID of the call to the worker when executing a Conference instruction.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``POST`` or
                ``GET`` and the default is ``POST``.
            status_callback_event: The call progress events that we will send to ``status_callback``. Can be:
                ``initiated``, ``ringing``, ``answered``, or ``completed``.
            timeout: Timeout for call when executing a Conference instruction.
            record: Whether to record the participant and their conferences, including the time between conferences. The
                default is ``false``.
            muted: Whether the agent is muted in the conference. The default is ``false``.
            beep: Whether to play a notification beep when the participant joins or when to play a beep. Can be:
                ``true``, ``false``, ``onEnter``, or ``onExit``. The default value is ``true``.
            start_conference_on_enter: Whether to start the conference when the participant joins, if it has not already
                started. The default is ``true``. If ``false`` and the conference has not started, the participant is
                muted and hears background music until another participant starts the conference.
            end_conference_on_exit: Whether to end the conference when the agent leaves.
            wait_url: The URL we should call using the ``wait_method`` for the music to play while participants are
                waiting for the conference to start. The default value is the URL of our standard hold music. `Learn
                more about hold music <https://www.twilio.com/labs/twimlets/holdmusic>`__.
            wait_method: The HTTP method we should use to call ``wait_url``. Can be ``GET`` or ``POST`` and the default
                is ``POST``. When using a static audio file, this should be ``GET`` so that we can cache the file.
            early_media: Whether to allow an agent to hear the state of the outbound call, including ringing or
                disconnect messages. The default is ``true``.
            max_participants: The maximum number of participants in the conference. Can be a positive integer from ``2``
                to ``250``. The default value is ``250``.
            conference_status_callback: The URL we should call using the ``conference_status_callback_method`` when the
                conference events in ``conference_status_callback_event`` occur. Only the value set by the first
                participant to join the conference is used. Subsequent ``conference_status_callback`` values are
                ignored.
            conference_status_callback_method: The HTTP method we should use to call ``conference_status_callback``. Can
                be: ``GET`` or ``POST`` and defaults to ``POST``.
            conference_status_callback_event: The conference status events that we will send to
                ``conference_status_callback``. Can be: ``start``, ``end``, ``join``, ``leave``, ``mute``, ``hold``,
                ``speaker``.
            conference_record: Whether to record the conference the participant is joining or when to record the
                conference. Can be: ``true``, ``false``, ``record-from-start``, and ``do-not-record``. The default value
                is ``false``.
            conference_trim: How to trim the leading and trailing silence from your recorded conference audio files. Can
                be: ``trim-silence`` or ``do-not-trim`` and defaults to ``trim-silence``.
            recording_channels: The recording channels for the final recording. Can be: ``mono`` or ``dual`` and the
                default is ``mono``.
            recording_status_callback: The URL that we should call using the ``recording_status_callback_method`` when
                the recording status changes.
            recording_status_callback_method: The HTTP method we should use when we call ``recording_status_callback``.
                Can be: ``GET`` or ``POST`` and defaults to ``POST``.
            conference_recording_status_callback: The URL we should call using the
                ``conference_recording_status_callback_method`` when the conference recording is available.
            conference_recording_status_callback_method: The HTTP method we should use to call
                ``conference_recording_status_callback``. Can be: ``GET`` or ``POST`` and defaults to ``POST``.
            region: The `region
                <https://support.twilio.com/hc/en-us/articles/223132167-How-global-low-latency-routing-and-region-selection-work-for-conferences-and-Client-calls>`__
                where we should mix the recorded audio. Can be:``us1``, ``us2``, ``ie1``, ``de1``, ``sg1``, ``br1``,
                ``au1``, or ``jp1``.
            sip_auth_username: The SIP username used for authentication.
            sip_auth_password: The SIP password for authentication.
            dequeue_status_callback_event: The Call progress events sent via webhooks as a result of a Dequeue
                instruction.
            post_work_activity_sid: The new worker activity SID after executing a Conference instruction.
            supervisor_mode: Value sent with the request.
            supervisor: The Supervisor SID/URI when executing the Supervise instruction.
            end_conference_on_customer_exit: Whether to end the conference when the customer leaves.
            beep_on_customer_entrance: Whether to play a notification beep when the customer joins.
            jitter_buffer_size: The jitter buffer size for conference. Can be: ``small``, ``medium``, ``large``,
                ``off``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_task_reservation(
            workspace_sid,
            task_sid,
            sid,
            if_match=if_match,
            reservation_status=reservation_status,
            worker_activity_sid=worker_activity_sid,
            instruction=instruction,
            dequeue_post_work_activity_sid=dequeue_post_work_activity_sid,
            dequeue_from=dequeue_from,
            dequeue_record=dequeue_record,
            dequeue_timeout=dequeue_timeout,
            dequeue_to=dequeue_to,
            dequeue_status_callback_url=dequeue_status_callback_url,
            call_from=call_from,
            call_record=call_record,
            call_timeout=call_timeout,
            call_to=call_to,
            call_url=call_url,
            call_status_callback_url=call_status_callback_url,
            call_accept=call_accept,
            redirect_call_sid=redirect_call_sid,
            redirect_accept=redirect_accept,
            redirect_url=redirect_url,
            to=to,
            from_=from_,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            status_callback_event=status_callback_event,
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
            conference_status_callback=conference_status_callback,
            conference_status_callback_method=conference_status_callback_method,
            conference_status_callback_event=conference_status_callback_event,
            conference_record=conference_record,
            conference_trim=conference_trim,
            recording_channels=recording_channels,
            recording_status_callback=recording_status_callback,
            recording_status_callback_method=recording_status_callback_method,
            conference_recording_status_callback=conference_recording_status_callback,
            conference_recording_status_callback_method=conference_recording_status_callback_method,
            region=region,
            sip_auth_username=sip_auth_username,
            sip_auth_password=sip_auth_password,
            dequeue_status_callback_event=dequeue_status_callback_event,
            post_work_activity_sid=post_work_activity_sid,
            supervisor_mode=supervisor_mode,
            supervisor=supervisor,
            end_conference_on_customer_exit=end_conference_on_customer_exit,
            beep_on_customer_entrance=beep_on_customer_entrance,
            jitter_buffer_size=jitter_buffer_size,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> TaskrouterV1TaskReservationWithRawResponse:
        return self._with_raw_response


class AsyncTaskrouterV1TaskReservation:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTaskrouterV1TaskReservationWithRawResponse(client, server, auth)

    async def fetch_task_reservation(
        self, workspace_sid: str, task_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TaskrouterV1WorkspaceTaskTaskReservation:
        """Tasks reserved for workers

        Args:
            workspace_sid: The SID of the Workspace with the TaskReservation resource to fetch.
            task_sid: The SID of the reserved Task resource with the TaskReservation resource to fetch.
            sid: The SID of the TaskReservation resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_task_reservation(
                workspace_sid, task_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_task_reservation(
        self,
        workspace_sid: str,
        task_sid: str,
        *,
        reservation_status: TaskReservationEnumStatusOrStr | None = None,
        worker_sid: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTaskReservationResponse:
        """Tasks reserved for workers

        Args:
            workspace_sid: The SID of the Workspace with the TaskReservation resources to read.
            task_sid: The SID of the reserved Task resource with the TaskReservation resources to read.
            reservation_status: Returns the list of reservations for a task with a specified ReservationStatus. Can be:
                ``pending``, ``accepted``, ``rejected``, or ``timeout``.
            worker_sid: The SID of the reserved Worker resource to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_task_reservation(
                workspace_sid,
                task_sid,
                reservation_status=reservation_status,
                worker_sid=worker_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_task_reservation(
        self,
        workspace_sid: str,
        task_sid: str,
        sid: str,
        *,
        if_match: str | None = None,
        reservation_status: TaskReservationEnumStatusOrStr | None = None,
        worker_activity_sid: str | None = None,
        instruction: str | None = None,
        dequeue_post_work_activity_sid: str | None = None,
        dequeue_from: str | None = None,
        dequeue_record: str | None = None,
        dequeue_timeout: int | None = None,
        dequeue_to: str | None = None,
        dequeue_status_callback_url: str | None = None,
        call_from: str | None = None,
        call_record: str | None = None,
        call_timeout: int | None = None,
        call_to: str | None = None,
        call_url: str | None = None,
        call_status_callback_url: str | None = None,
        call_accept: bool | None = None,
        redirect_call_sid: str | None = None,
        redirect_accept: bool | None = None,
        redirect_url: str | None = None,
        to: str | None = None,
        from_: str | None = None,
        status_callback: str | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        status_callback_event: list[CallEnumEventOrStr] | None = None,
        timeout: int | None = None,
        record: bool | None = None,
        muted: bool | None = None,
        beep: str | None = None,
        start_conference_on_enter: bool | None = None,
        end_conference_on_exit: bool | None = None,
        wait_url: str | None = None,
        wait_method: AmdStatusCallbackMethodOrStr | None = None,
        early_media: bool | None = None,
        max_participants: int | None = None,
        conference_status_callback: str | None = None,
        conference_status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        conference_status_callback_event: list[TaskReservationEnumConferenceEventOrStr] | None = None,
        conference_record: str | None = None,
        conference_trim: str | None = None,
        recording_channels: str | None = None,
        recording_status_callback: str | None = None,
        recording_status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        conference_recording_status_callback: str | None = None,
        conference_recording_status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        region: str | None = None,
        sip_auth_username: str | None = None,
        sip_auth_password: str | None = None,
        dequeue_status_callback_event: list[str] | None = None,
        post_work_activity_sid: str | None = None,
        supervisor_mode: TaskReservationEnumSupervisorModeOrStr | None = None,
        supervisor: str | None = None,
        end_conference_on_customer_exit: bool | None = None,
        beep_on_customer_entrance: bool | None = None,
        jitter_buffer_size: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceTaskTaskReservation:
        """Tasks reserved for workers

        Args:
            workspace_sid: The SID of the Workspace with the TaskReservation resources to update.
            task_sid: The SID of the reserved Task resource with the TaskReservation resources to update.
            sid: The SID of the TaskReservation resource to update.
            if_match: The If-Match HTTP request header
            reservation_status: The current status of the reservation. Can be: ``pending``, ``accepted``, ``rejected``,
                or ``timeout``.
            worker_activity_sid: The new worker activity SID if rejecting a reservation.
            instruction: The assignment instruction for reservation.
            dequeue_post_work_activity_sid: The SID of the Activity resource to start after executing a Dequeue
                instruction.
            dequeue_from: The Caller ID of the call to the worker when executing a Dequeue instruction.
            dequeue_record: Whether to record both legs of a call when executing a Dequeue instruction or which leg to
                record.
            dequeue_timeout: Timeout for call when executing a Dequeue instruction.
            dequeue_to: The Contact URI of the worker when executing a Dequeue instruction. Can be the URI of the Twilio
                Client, the SIP URI for Programmable SIP, or the `E.164
                <https://www.twilio.com/docs/glossary/what-e164>`__ formatted phone number, depending on the
                destination.
            dequeue_status_callback_url: The Callback URL for completed call event when executing a Dequeue instruction.
            call_from: The Caller ID of the outbound call when executing a Call instruction.
            call_record: Whether to record both legs of a call when executing a Call instruction or which leg to record.
            call_timeout: Timeout for call when executing a Call instruction.
            call_to: The Contact URI of the worker when executing a Call instruction. Can be the URI of the Twilio
                Client, the SIP URI for Programmable SIP, or the `E.164
                <https://www.twilio.com/docs/glossary/what-e164>`__ formatted phone number, depending on the
                destination.
            call_url: TwiML URI executed on answering the worker's leg as a result of the Call instruction.
            call_status_callback_url: The URL to call for the completed call event when executing a Call instruction.
            call_accept: Whether to accept a reservation when executing a Call instruction.
            redirect_call_sid: The Call SID of the call parked in the queue when executing a Redirect instruction.
            redirect_accept: Whether the reservation should be accepted when executing a Redirect instruction.
            redirect_url: TwiML URI to redirect the call to when executing the Redirect instruction.
            to: The Contact URI of the worker when executing a Conference instruction. Can be the URI of the Twilio
                Client, the SIP URI for Programmable SIP, or the `E.164
                <https://www.twilio.com/docs/glossary/what-e164>`__ formatted phone number, depending on the
                destination.
            from_: The Caller ID of the call to the worker when executing a Conference instruction.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``POST`` or
                ``GET`` and the default is ``POST``.
            status_callback_event: The call progress events that we will send to ``status_callback``. Can be:
                ``initiated``, ``ringing``, ``answered``, or ``completed``.
            timeout: Timeout for call when executing a Conference instruction.
            record: Whether to record the participant and their conferences, including the time between conferences. The
                default is ``false``.
            muted: Whether the agent is muted in the conference. The default is ``false``.
            beep: Whether to play a notification beep when the participant joins or when to play a beep. Can be:
                ``true``, ``false``, ``onEnter``, or ``onExit``. The default value is ``true``.
            start_conference_on_enter: Whether to start the conference when the participant joins, if it has not already
                started. The default is ``true``. If ``false`` and the conference has not started, the participant is
                muted and hears background music until another participant starts the conference.
            end_conference_on_exit: Whether to end the conference when the agent leaves.
            wait_url: The URL we should call using the ``wait_method`` for the music to play while participants are
                waiting for the conference to start. The default value is the URL of our standard hold music. `Learn
                more about hold music <https://www.twilio.com/labs/twimlets/holdmusic>`__.
            wait_method: The HTTP method we should use to call ``wait_url``. Can be ``GET`` or ``POST`` and the default
                is ``POST``. When using a static audio file, this should be ``GET`` so that we can cache the file.
            early_media: Whether to allow an agent to hear the state of the outbound call, including ringing or
                disconnect messages. The default is ``true``.
            max_participants: The maximum number of participants in the conference. Can be a positive integer from ``2``
                to ``250``. The default value is ``250``.
            conference_status_callback: The URL we should call using the ``conference_status_callback_method`` when the
                conference events in ``conference_status_callback_event`` occur. Only the value set by the first
                participant to join the conference is used. Subsequent ``conference_status_callback`` values are
                ignored.
            conference_status_callback_method: The HTTP method we should use to call ``conference_status_callback``. Can
                be: ``GET`` or ``POST`` and defaults to ``POST``.
            conference_status_callback_event: The conference status events that we will send to
                ``conference_status_callback``. Can be: ``start``, ``end``, ``join``, ``leave``, ``mute``, ``hold``,
                ``speaker``.
            conference_record: Whether to record the conference the participant is joining or when to record the
                conference. Can be: ``true``, ``false``, ``record-from-start``, and ``do-not-record``. The default value
                is ``false``.
            conference_trim: How to trim the leading and trailing silence from your recorded conference audio files. Can
                be: ``trim-silence`` or ``do-not-trim`` and defaults to ``trim-silence``.
            recording_channels: The recording channels for the final recording. Can be: ``mono`` or ``dual`` and the
                default is ``mono``.
            recording_status_callback: The URL that we should call using the ``recording_status_callback_method`` when
                the recording status changes.
            recording_status_callback_method: The HTTP method we should use when we call ``recording_status_callback``.
                Can be: ``GET`` or ``POST`` and defaults to ``POST``.
            conference_recording_status_callback: The URL we should call using the
                ``conference_recording_status_callback_method`` when the conference recording is available.
            conference_recording_status_callback_method: The HTTP method we should use to call
                ``conference_recording_status_callback``. Can be: ``GET`` or ``POST`` and defaults to ``POST``.
            region: The `region
                <https://support.twilio.com/hc/en-us/articles/223132167-How-global-low-latency-routing-and-region-selection-work-for-conferences-and-Client-calls>`__
                where we should mix the recorded audio. Can be:``us1``, ``us2``, ``ie1``, ``de1``, ``sg1``, ``br1``,
                ``au1``, or ``jp1``.
            sip_auth_username: The SIP username used for authentication.
            sip_auth_password: The SIP password for authentication.
            dequeue_status_callback_event: The Call progress events sent via webhooks as a result of a Dequeue
                instruction.
            post_work_activity_sid: The new worker activity SID after executing a Conference instruction.
            supervisor_mode: Value sent with the request.
            supervisor: The Supervisor SID/URI when executing the Supervise instruction.
            end_conference_on_customer_exit: Whether to end the conference when the customer leaves.
            beep_on_customer_entrance: Whether to play a notification beep when the customer joins.
            jitter_buffer_size: The jitter buffer size for conference. Can be: ``small``, ``medium``, ``large``,
                ``off``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_task_reservation(
                workspace_sid,
                task_sid,
                sid,
                if_match=if_match,
                reservation_status=reservation_status,
                worker_activity_sid=worker_activity_sid,
                instruction=instruction,
                dequeue_post_work_activity_sid=dequeue_post_work_activity_sid,
                dequeue_from=dequeue_from,
                dequeue_record=dequeue_record,
                dequeue_timeout=dequeue_timeout,
                dequeue_to=dequeue_to,
                dequeue_status_callback_url=dequeue_status_callback_url,
                call_from=call_from,
                call_record=call_record,
                call_timeout=call_timeout,
                call_to=call_to,
                call_url=call_url,
                call_status_callback_url=call_status_callback_url,
                call_accept=call_accept,
                redirect_call_sid=redirect_call_sid,
                redirect_accept=redirect_accept,
                redirect_url=redirect_url,
                to=to,
                from_=from_,
                status_callback=status_callback,
                status_callback_method=status_callback_method,
                status_callback_event=status_callback_event,
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
                conference_status_callback=conference_status_callback,
                conference_status_callback_method=conference_status_callback_method,
                conference_status_callback_event=conference_status_callback_event,
                conference_record=conference_record,
                conference_trim=conference_trim,
                recording_channels=recording_channels,
                recording_status_callback=recording_status_callback,
                recording_status_callback_method=recording_status_callback_method,
                conference_recording_status_callback=conference_recording_status_callback,
                conference_recording_status_callback_method=conference_recording_status_callback_method,
                region=region,
                sip_auth_username=sip_auth_username,
                sip_auth_password=sip_auth_password,
                dequeue_status_callback_event=dequeue_status_callback_event,
                post_work_activity_sid=post_work_activity_sid,
                supervisor_mode=supervisor_mode,
                supervisor=supervisor,
                end_conference_on_customer_exit=end_conference_on_customer_exit,
                beep_on_customer_entrance=beep_on_customer_entrance,
                jitter_buffer_size=jitter_buffer_size,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTaskrouterV1TaskReservationWithRawResponse:
        return self._with_raw_response


class TaskrouterV1TaskReservationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_task_reservation(
        self, workspace_sid: str, task_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TaskrouterV1WorkspaceTaskTaskReservation, RawError]:
        """Tasks reserved for workers

        Args:
            workspace_sid: The SID of the Workspace with the TaskReservation resource to fetch.
            task_sid: The SID of the reserved Task resource with the TaskReservation resource to fetch.
            sid: The SID of the TaskReservation resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Tasks/{TaskSid}/Reservations/{Sid}"),
            path_params=[
                param[str]("WorkspaceSid", workspace_sid), param[str]("TaskSid", task_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTaskTaskReservation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_task_reservation(
        self,
        workspace_sid: str,
        task_sid: str,
        *,
        reservation_status: TaskReservationEnumStatusOrStr | None = None,
        worker_sid: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTaskReservationResponse, RawError]:
        """Tasks reserved for workers

        Args:
            workspace_sid: The SID of the Workspace with the TaskReservation resources to read.
            task_sid: The SID of the reserved Task resource with the TaskReservation resources to read.
            reservation_status: Returns the list of reservations for a task with a specified ReservationStatus. Can be:
                ``pending``, ``accepted``, ``rejected``, or ``timeout``.
            worker_sid: The SID of the reserved Worker resource to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Tasks/{TaskSid}/Reservations"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("TaskSid", task_sid)],
            query_params=[
                param[TaskReservationEnumStatusOrStr | None]("ReservationStatus", reservation_status),
                param[str | None]("WorkerSid", worker_sid),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListTaskReservationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_task_reservation(
        self,
        workspace_sid: str,
        task_sid: str,
        sid: str,
        *,
        if_match: str | None = None,
        reservation_status: TaskReservationEnumStatusOrStr | None = None,
        worker_activity_sid: str | None = None,
        instruction: str | None = None,
        dequeue_post_work_activity_sid: str | None = None,
        dequeue_from: str | None = None,
        dequeue_record: str | None = None,
        dequeue_timeout: int | None = None,
        dequeue_to: str | None = None,
        dequeue_status_callback_url: str | None = None,
        call_from: str | None = None,
        call_record: str | None = None,
        call_timeout: int | None = None,
        call_to: str | None = None,
        call_url: str | None = None,
        call_status_callback_url: str | None = None,
        call_accept: bool | None = None,
        redirect_call_sid: str | None = None,
        redirect_accept: bool | None = None,
        redirect_url: str | None = None,
        to: str | None = None,
        from_: str | None = None,
        status_callback: str | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        status_callback_event: list[CallEnumEventOrStr] | None = None,
        timeout: int | None = None,
        record: bool | None = None,
        muted: bool | None = None,
        beep: str | None = None,
        start_conference_on_enter: bool | None = None,
        end_conference_on_exit: bool | None = None,
        wait_url: str | None = None,
        wait_method: AmdStatusCallbackMethodOrStr | None = None,
        early_media: bool | None = None,
        max_participants: int | None = None,
        conference_status_callback: str | None = None,
        conference_status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        conference_status_callback_event: list[TaskReservationEnumConferenceEventOrStr] | None = None,
        conference_record: str | None = None,
        conference_trim: str | None = None,
        recording_channels: str | None = None,
        recording_status_callback: str | None = None,
        recording_status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        conference_recording_status_callback: str | None = None,
        conference_recording_status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        region: str | None = None,
        sip_auth_username: str | None = None,
        sip_auth_password: str | None = None,
        dequeue_status_callback_event: list[str] | None = None,
        post_work_activity_sid: str | None = None,
        supervisor_mode: TaskReservationEnumSupervisorModeOrStr | None = None,
        supervisor: str | None = None,
        end_conference_on_customer_exit: bool | None = None,
        beep_on_customer_entrance: bool | None = None,
        jitter_buffer_size: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceTaskTaskReservation, RawError]:
        """Tasks reserved for workers

        Args:
            workspace_sid: The SID of the Workspace with the TaskReservation resources to update.
            task_sid: The SID of the reserved Task resource with the TaskReservation resources to update.
            sid: The SID of the TaskReservation resource to update.
            if_match: The If-Match HTTP request header
            reservation_status: The current status of the reservation. Can be: ``pending``, ``accepted``, ``rejected``,
                or ``timeout``.
            worker_activity_sid: The new worker activity SID if rejecting a reservation.
            instruction: The assignment instruction for reservation.
            dequeue_post_work_activity_sid: The SID of the Activity resource to start after executing a Dequeue
                instruction.
            dequeue_from: The Caller ID of the call to the worker when executing a Dequeue instruction.
            dequeue_record: Whether to record both legs of a call when executing a Dequeue instruction or which leg to
                record.
            dequeue_timeout: Timeout for call when executing a Dequeue instruction.
            dequeue_to: The Contact URI of the worker when executing a Dequeue instruction. Can be the URI of the Twilio
                Client, the SIP URI for Programmable SIP, or the `E.164
                <https://www.twilio.com/docs/glossary/what-e164>`__ formatted phone number, depending on the
                destination.
            dequeue_status_callback_url: The Callback URL for completed call event when executing a Dequeue instruction.
            call_from: The Caller ID of the outbound call when executing a Call instruction.
            call_record: Whether to record both legs of a call when executing a Call instruction or which leg to record.
            call_timeout: Timeout for call when executing a Call instruction.
            call_to: The Contact URI of the worker when executing a Call instruction. Can be the URI of the Twilio
                Client, the SIP URI for Programmable SIP, or the `E.164
                <https://www.twilio.com/docs/glossary/what-e164>`__ formatted phone number, depending on the
                destination.
            call_url: TwiML URI executed on answering the worker's leg as a result of the Call instruction.
            call_status_callback_url: The URL to call for the completed call event when executing a Call instruction.
            call_accept: Whether to accept a reservation when executing a Call instruction.
            redirect_call_sid: The Call SID of the call parked in the queue when executing a Redirect instruction.
            redirect_accept: Whether the reservation should be accepted when executing a Redirect instruction.
            redirect_url: TwiML URI to redirect the call to when executing the Redirect instruction.
            to: The Contact URI of the worker when executing a Conference instruction. Can be the URI of the Twilio
                Client, the SIP URI for Programmable SIP, or the `E.164
                <https://www.twilio.com/docs/glossary/what-e164>`__ formatted phone number, depending on the
                destination.
            from_: The Caller ID of the call to the worker when executing a Conference instruction.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``POST`` or
                ``GET`` and the default is ``POST``.
            status_callback_event: The call progress events that we will send to ``status_callback``. Can be:
                ``initiated``, ``ringing``, ``answered``, or ``completed``.
            timeout: Timeout for call when executing a Conference instruction.
            record: Whether to record the participant and their conferences, including the time between conferences. The
                default is ``false``.
            muted: Whether the agent is muted in the conference. The default is ``false``.
            beep: Whether to play a notification beep when the participant joins or when to play a beep. Can be:
                ``true``, ``false``, ``onEnter``, or ``onExit``. The default value is ``true``.
            start_conference_on_enter: Whether to start the conference when the participant joins, if it has not already
                started. The default is ``true``. If ``false`` and the conference has not started, the participant is
                muted and hears background music until another participant starts the conference.
            end_conference_on_exit: Whether to end the conference when the agent leaves.
            wait_url: The URL we should call using the ``wait_method`` for the music to play while participants are
                waiting for the conference to start. The default value is the URL of our standard hold music. `Learn
                more about hold music <https://www.twilio.com/labs/twimlets/holdmusic>`__.
            wait_method: The HTTP method we should use to call ``wait_url``. Can be ``GET`` or ``POST`` and the default
                is ``POST``. When using a static audio file, this should be ``GET`` so that we can cache the file.
            early_media: Whether to allow an agent to hear the state of the outbound call, including ringing or
                disconnect messages. The default is ``true``.
            max_participants: The maximum number of participants in the conference. Can be a positive integer from ``2``
                to ``250``. The default value is ``250``.
            conference_status_callback: The URL we should call using the ``conference_status_callback_method`` when the
                conference events in ``conference_status_callback_event`` occur. Only the value set by the first
                participant to join the conference is used. Subsequent ``conference_status_callback`` values are
                ignored.
            conference_status_callback_method: The HTTP method we should use to call ``conference_status_callback``. Can
                be: ``GET`` or ``POST`` and defaults to ``POST``.
            conference_status_callback_event: The conference status events that we will send to
                ``conference_status_callback``. Can be: ``start``, ``end``, ``join``, ``leave``, ``mute``, ``hold``,
                ``speaker``.
            conference_record: Whether to record the conference the participant is joining or when to record the
                conference. Can be: ``true``, ``false``, ``record-from-start``, and ``do-not-record``. The default value
                is ``false``.
            conference_trim: How to trim the leading and trailing silence from your recorded conference audio files. Can
                be: ``trim-silence`` or ``do-not-trim`` and defaults to ``trim-silence``.
            recording_channels: The recording channels for the final recording. Can be: ``mono`` or ``dual`` and the
                default is ``mono``.
            recording_status_callback: The URL that we should call using the ``recording_status_callback_method`` when
                the recording status changes.
            recording_status_callback_method: The HTTP method we should use when we call ``recording_status_callback``.
                Can be: ``GET`` or ``POST`` and defaults to ``POST``.
            conference_recording_status_callback: The URL we should call using the
                ``conference_recording_status_callback_method`` when the conference recording is available.
            conference_recording_status_callback_method: The HTTP method we should use to call
                ``conference_recording_status_callback``. Can be: ``GET`` or ``POST`` and defaults to ``POST``.
            region: The `region
                <https://support.twilio.com/hc/en-us/articles/223132167-How-global-low-latency-routing-and-region-selection-work-for-conferences-and-Client-calls>`__
                where we should mix the recorded audio. Can be:``us1``, ``us2``, ``ie1``, ``de1``, ``sg1``, ``br1``,
                ``au1``, or ``jp1``.
            sip_auth_username: The SIP username used for authentication.
            sip_auth_password: The SIP password for authentication.
            dequeue_status_callback_event: The Call progress events sent via webhooks as a result of a Dequeue
                instruction.
            post_work_activity_sid: The new worker activity SID after executing a Conference instruction.
            supervisor_mode: Value sent with the request.
            supervisor: The Supervisor SID/URI when executing the Supervise instruction.
            end_conference_on_customer_exit: Whether to end the conference when the customer leaves.
            beep_on_customer_entrance: Whether to play a notification beep when the customer joins.
            jitter_buffer_size: The jitter buffer size for conference. Can be: ``small``, ``medium``, ``large``,
                ``off``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Tasks/{TaskSid}/Reservations/{Sid}"),
            path_params=[
                param[str]("WorkspaceSid", workspace_sid), param[str]("TaskSid", task_sid), param[str]("Sid", sid)
            ],
            headers=[param[str | None]("If-Match", if_match), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[TaskReservationEnumStatusOrStr | None]("ReservationStatus", reservation_status),
                    param[str | None]("WorkerActivitySid", worker_activity_sid),
                    param[str | None]("Instruction", instruction),
                    param[str | None]("DequeuePostWorkActivitySid", dequeue_post_work_activity_sid),
                    param[str | None]("DequeueFrom", dequeue_from),
                    param[str | None]("DequeueRecord", dequeue_record),
                    param[int | None]("DequeueTimeout", dequeue_timeout),
                    param[str | None]("DequeueTo", dequeue_to),
                    param[str | None]("DequeueStatusCallbackUrl", dequeue_status_callback_url),
                    param[str | None]("CallFrom", call_from),
                    param[str | None]("CallRecord", call_record),
                    param[int | None]("CallTimeout", call_timeout),
                    param[str | None]("CallTo", call_to),
                    param[str | None]("CallUrl", call_url),
                    param[str | None]("CallStatusCallbackUrl", call_status_callback_url),
                    param[bool | None]("CallAccept", call_accept),
                    param[str | None]("RedirectCallSid", redirect_call_sid),
                    param[bool | None]("RedirectAccept", redirect_accept),
                    param[str | None]("RedirectUrl", redirect_url),
                    param[str | None]("To", to),
                    param[str | None]("From", from_),
                    param[str | None]("StatusCallback", status_callback),
                    param[AmdStatusCallbackMethodOrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[list[CallEnumEventOrStr] | None]("StatusCallbackEvent", status_callback_event),
                    param[int | None]("Timeout", timeout),
                    param[bool | None]("Record", record),
                    param[bool | None]("Muted", muted),
                    param[str | None]("Beep", beep),
                    param[bool | None]("StartConferenceOnEnter", start_conference_on_enter),
                    param[bool | None]("EndConferenceOnExit", end_conference_on_exit),
                    param[str | None]("WaitUrl", wait_url),
                    param[AmdStatusCallbackMethodOrStr | None]("WaitMethod", wait_method),
                    param[bool | None]("EarlyMedia", early_media),
                    param[int | None]("MaxParticipants", max_participants),
                    param[str | None]("ConferenceStatusCallback", conference_status_callback),
                    param[AmdStatusCallbackMethodOrStr | None](
                        "ConferenceStatusCallbackMethod", conference_status_callback_method
                    ),
                    param[list[TaskReservationEnumConferenceEventOrStr] | None](
                        "ConferenceStatusCallbackEvent", conference_status_callback_event
                    ),
                    param[str | None]("ConferenceRecord", conference_record),
                    param[str | None]("ConferenceTrim", conference_trim),
                    param[str | None]("RecordingChannels", recording_channels),
                    param[str | None]("RecordingStatusCallback", recording_status_callback),
                    param[AmdStatusCallbackMethodOrStr | None](
                        "RecordingStatusCallbackMethod", recording_status_callback_method
                    ),
                    param[str | None]("ConferenceRecordingStatusCallback", conference_recording_status_callback),
                    param[AmdStatusCallbackMethodOrStr | None](
                        "ConferenceRecordingStatusCallbackMethod", conference_recording_status_callback_method
                    ),
                    param[str | None]("Region", region),
                    param[str | None]("SipAuthUsername", sip_auth_username),
                    param[str | None]("SipAuthPassword", sip_auth_password),
                    param[list[str] | None]("DequeueStatusCallbackEvent", dequeue_status_callback_event),
                    param[str | None]("PostWorkActivitySid", post_work_activity_sid),
                    param[TaskReservationEnumSupervisorModeOrStr | None]("SupervisorMode", supervisor_mode),
                    param[str | None]("Supervisor", supervisor),
                    param[bool | None]("EndConferenceOnCustomerExit", end_conference_on_customer_exit),
                    param[bool | None]("BeepOnCustomerEntrance", beep_on_customer_entrance),
                    param[str | None]("JitterBufferSize", jitter_buffer_size),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTaskTaskReservation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTaskrouterV1TaskReservationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_task_reservation(
        self, workspace_sid: str, task_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TaskrouterV1WorkspaceTaskTaskReservation, RawError]:
        """Tasks reserved for workers

        Args:
            workspace_sid: The SID of the Workspace with the TaskReservation resource to fetch.
            task_sid: The SID of the reserved Task resource with the TaskReservation resource to fetch.
            sid: The SID of the TaskReservation resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Tasks/{TaskSid}/Reservations/{Sid}"),
            path_params=[
                param[str]("WorkspaceSid", workspace_sid), param[str]("TaskSid", task_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTaskTaskReservation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_task_reservation(
        self,
        workspace_sid: str,
        task_sid: str,
        *,
        reservation_status: TaskReservationEnumStatusOrStr | None = None,
        worker_sid: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTaskReservationResponse, RawError]:
        """Tasks reserved for workers

        Args:
            workspace_sid: The SID of the Workspace with the TaskReservation resources to read.
            task_sid: The SID of the reserved Task resource with the TaskReservation resources to read.
            reservation_status: Returns the list of reservations for a task with a specified ReservationStatus. Can be:
                ``pending``, ``accepted``, ``rejected``, or ``timeout``.
            worker_sid: The SID of the reserved Worker resource to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Tasks/{TaskSid}/Reservations"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("TaskSid", task_sid)],
            query_params=[
                param[TaskReservationEnumStatusOrStr | None]("ReservationStatus", reservation_status),
                param[str | None]("WorkerSid", worker_sid),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListTaskReservationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_task_reservation(
        self,
        workspace_sid: str,
        task_sid: str,
        sid: str,
        *,
        if_match: str | None = None,
        reservation_status: TaskReservationEnumStatusOrStr | None = None,
        worker_activity_sid: str | None = None,
        instruction: str | None = None,
        dequeue_post_work_activity_sid: str | None = None,
        dequeue_from: str | None = None,
        dequeue_record: str | None = None,
        dequeue_timeout: int | None = None,
        dequeue_to: str | None = None,
        dequeue_status_callback_url: str | None = None,
        call_from: str | None = None,
        call_record: str | None = None,
        call_timeout: int | None = None,
        call_to: str | None = None,
        call_url: str | None = None,
        call_status_callback_url: str | None = None,
        call_accept: bool | None = None,
        redirect_call_sid: str | None = None,
        redirect_accept: bool | None = None,
        redirect_url: str | None = None,
        to: str | None = None,
        from_: str | None = None,
        status_callback: str | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        status_callback_event: list[CallEnumEventOrStr] | None = None,
        timeout: int | None = None,
        record: bool | None = None,
        muted: bool | None = None,
        beep: str | None = None,
        start_conference_on_enter: bool | None = None,
        end_conference_on_exit: bool | None = None,
        wait_url: str | None = None,
        wait_method: AmdStatusCallbackMethodOrStr | None = None,
        early_media: bool | None = None,
        max_participants: int | None = None,
        conference_status_callback: str | None = None,
        conference_status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        conference_status_callback_event: list[TaskReservationEnumConferenceEventOrStr] | None = None,
        conference_record: str | None = None,
        conference_trim: str | None = None,
        recording_channels: str | None = None,
        recording_status_callback: str | None = None,
        recording_status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        conference_recording_status_callback: str | None = None,
        conference_recording_status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        region: str | None = None,
        sip_auth_username: str | None = None,
        sip_auth_password: str | None = None,
        dequeue_status_callback_event: list[str] | None = None,
        post_work_activity_sid: str | None = None,
        supervisor_mode: TaskReservationEnumSupervisorModeOrStr | None = None,
        supervisor: str | None = None,
        end_conference_on_customer_exit: bool | None = None,
        beep_on_customer_entrance: bool | None = None,
        jitter_buffer_size: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceTaskTaskReservation, RawError]:
        """Tasks reserved for workers

        Args:
            workspace_sid: The SID of the Workspace with the TaskReservation resources to update.
            task_sid: The SID of the reserved Task resource with the TaskReservation resources to update.
            sid: The SID of the TaskReservation resource to update.
            if_match: The If-Match HTTP request header
            reservation_status: The current status of the reservation. Can be: ``pending``, ``accepted``, ``rejected``,
                or ``timeout``.
            worker_activity_sid: The new worker activity SID if rejecting a reservation.
            instruction: The assignment instruction for reservation.
            dequeue_post_work_activity_sid: The SID of the Activity resource to start after executing a Dequeue
                instruction.
            dequeue_from: The Caller ID of the call to the worker when executing a Dequeue instruction.
            dequeue_record: Whether to record both legs of a call when executing a Dequeue instruction or which leg to
                record.
            dequeue_timeout: Timeout for call when executing a Dequeue instruction.
            dequeue_to: The Contact URI of the worker when executing a Dequeue instruction. Can be the URI of the Twilio
                Client, the SIP URI for Programmable SIP, or the `E.164
                <https://www.twilio.com/docs/glossary/what-e164>`__ formatted phone number, depending on the
                destination.
            dequeue_status_callback_url: The Callback URL for completed call event when executing a Dequeue instruction.
            call_from: The Caller ID of the outbound call when executing a Call instruction.
            call_record: Whether to record both legs of a call when executing a Call instruction or which leg to record.
            call_timeout: Timeout for call when executing a Call instruction.
            call_to: The Contact URI of the worker when executing a Call instruction. Can be the URI of the Twilio
                Client, the SIP URI for Programmable SIP, or the `E.164
                <https://www.twilio.com/docs/glossary/what-e164>`__ formatted phone number, depending on the
                destination.
            call_url: TwiML URI executed on answering the worker's leg as a result of the Call instruction.
            call_status_callback_url: The URL to call for the completed call event when executing a Call instruction.
            call_accept: Whether to accept a reservation when executing a Call instruction.
            redirect_call_sid: The Call SID of the call parked in the queue when executing a Redirect instruction.
            redirect_accept: Whether the reservation should be accepted when executing a Redirect instruction.
            redirect_url: TwiML URI to redirect the call to when executing the Redirect instruction.
            to: The Contact URI of the worker when executing a Conference instruction. Can be the URI of the Twilio
                Client, the SIP URI for Programmable SIP, or the `E.164
                <https://www.twilio.com/docs/glossary/what-e164>`__ formatted phone number, depending on the
                destination.
            from_: The Caller ID of the call to the worker when executing a Conference instruction.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information to
                your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``POST`` or
                ``GET`` and the default is ``POST``.
            status_callback_event: The call progress events that we will send to ``status_callback``. Can be:
                ``initiated``, ``ringing``, ``answered``, or ``completed``.
            timeout: Timeout for call when executing a Conference instruction.
            record: Whether to record the participant and their conferences, including the time between conferences. The
                default is ``false``.
            muted: Whether the agent is muted in the conference. The default is ``false``.
            beep: Whether to play a notification beep when the participant joins or when to play a beep. Can be:
                ``true``, ``false``, ``onEnter``, or ``onExit``. The default value is ``true``.
            start_conference_on_enter: Whether to start the conference when the participant joins, if it has not already
                started. The default is ``true``. If ``false`` and the conference has not started, the participant is
                muted and hears background music until another participant starts the conference.
            end_conference_on_exit: Whether to end the conference when the agent leaves.
            wait_url: The URL we should call using the ``wait_method`` for the music to play while participants are
                waiting for the conference to start. The default value is the URL of our standard hold music. `Learn
                more about hold music <https://www.twilio.com/labs/twimlets/holdmusic>`__.
            wait_method: The HTTP method we should use to call ``wait_url``. Can be ``GET`` or ``POST`` and the default
                is ``POST``. When using a static audio file, this should be ``GET`` so that we can cache the file.
            early_media: Whether to allow an agent to hear the state of the outbound call, including ringing or
                disconnect messages. The default is ``true``.
            max_participants: The maximum number of participants in the conference. Can be a positive integer from ``2``
                to ``250``. The default value is ``250``.
            conference_status_callback: The URL we should call using the ``conference_status_callback_method`` when the
                conference events in ``conference_status_callback_event`` occur. Only the value set by the first
                participant to join the conference is used. Subsequent ``conference_status_callback`` values are
                ignored.
            conference_status_callback_method: The HTTP method we should use to call ``conference_status_callback``. Can
                be: ``GET`` or ``POST`` and defaults to ``POST``.
            conference_status_callback_event: The conference status events that we will send to
                ``conference_status_callback``. Can be: ``start``, ``end``, ``join``, ``leave``, ``mute``, ``hold``,
                ``speaker``.
            conference_record: Whether to record the conference the participant is joining or when to record the
                conference. Can be: ``true``, ``false``, ``record-from-start``, and ``do-not-record``. The default value
                is ``false``.
            conference_trim: How to trim the leading and trailing silence from your recorded conference audio files. Can
                be: ``trim-silence`` or ``do-not-trim`` and defaults to ``trim-silence``.
            recording_channels: The recording channels for the final recording. Can be: ``mono`` or ``dual`` and the
                default is ``mono``.
            recording_status_callback: The URL that we should call using the ``recording_status_callback_method`` when
                the recording status changes.
            recording_status_callback_method: The HTTP method we should use when we call ``recording_status_callback``.
                Can be: ``GET`` or ``POST`` and defaults to ``POST``.
            conference_recording_status_callback: The URL we should call using the
                ``conference_recording_status_callback_method`` when the conference recording is available.
            conference_recording_status_callback_method: The HTTP method we should use to call
                ``conference_recording_status_callback``. Can be: ``GET`` or ``POST`` and defaults to ``POST``.
            region: The `region
                <https://support.twilio.com/hc/en-us/articles/223132167-How-global-low-latency-routing-and-region-selection-work-for-conferences-and-Client-calls>`__
                where we should mix the recorded audio. Can be:``us1``, ``us2``, ``ie1``, ``de1``, ``sg1``, ``br1``,
                ``au1``, or ``jp1``.
            sip_auth_username: The SIP username used for authentication.
            sip_auth_password: The SIP password for authentication.
            dequeue_status_callback_event: The Call progress events sent via webhooks as a result of a Dequeue
                instruction.
            post_work_activity_sid: The new worker activity SID after executing a Conference instruction.
            supervisor_mode: Value sent with the request.
            supervisor: The Supervisor SID/URI when executing the Supervise instruction.
            end_conference_on_customer_exit: Whether to end the conference when the customer leaves.
            beep_on_customer_entrance: Whether to play a notification beep when the customer joins.
            jitter_buffer_size: The jitter buffer size for conference. Can be: ``small``, ``medium``, ``large``,
                ``off``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Tasks/{TaskSid}/Reservations/{Sid}"),
            path_params=[
                param[str]("WorkspaceSid", workspace_sid), param[str]("TaskSid", task_sid), param[str]("Sid", sid)
            ],
            headers=[param[str | None]("If-Match", if_match), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[TaskReservationEnumStatusOrStr | None]("ReservationStatus", reservation_status),
                    param[str | None]("WorkerActivitySid", worker_activity_sid),
                    param[str | None]("Instruction", instruction),
                    param[str | None]("DequeuePostWorkActivitySid", dequeue_post_work_activity_sid),
                    param[str | None]("DequeueFrom", dequeue_from),
                    param[str | None]("DequeueRecord", dequeue_record),
                    param[int | None]("DequeueTimeout", dequeue_timeout),
                    param[str | None]("DequeueTo", dequeue_to),
                    param[str | None]("DequeueStatusCallbackUrl", dequeue_status_callback_url),
                    param[str | None]("CallFrom", call_from),
                    param[str | None]("CallRecord", call_record),
                    param[int | None]("CallTimeout", call_timeout),
                    param[str | None]("CallTo", call_to),
                    param[str | None]("CallUrl", call_url),
                    param[str | None]("CallStatusCallbackUrl", call_status_callback_url),
                    param[bool | None]("CallAccept", call_accept),
                    param[str | None]("RedirectCallSid", redirect_call_sid),
                    param[bool | None]("RedirectAccept", redirect_accept),
                    param[str | None]("RedirectUrl", redirect_url),
                    param[str | None]("To", to),
                    param[str | None]("From", from_),
                    param[str | None]("StatusCallback", status_callback),
                    param[AmdStatusCallbackMethodOrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[list[CallEnumEventOrStr] | None]("StatusCallbackEvent", status_callback_event),
                    param[int | None]("Timeout", timeout),
                    param[bool | None]("Record", record),
                    param[bool | None]("Muted", muted),
                    param[str | None]("Beep", beep),
                    param[bool | None]("StartConferenceOnEnter", start_conference_on_enter),
                    param[bool | None]("EndConferenceOnExit", end_conference_on_exit),
                    param[str | None]("WaitUrl", wait_url),
                    param[AmdStatusCallbackMethodOrStr | None]("WaitMethod", wait_method),
                    param[bool | None]("EarlyMedia", early_media),
                    param[int | None]("MaxParticipants", max_participants),
                    param[str | None]("ConferenceStatusCallback", conference_status_callback),
                    param[AmdStatusCallbackMethodOrStr | None](
                        "ConferenceStatusCallbackMethod", conference_status_callback_method
                    ),
                    param[list[TaskReservationEnumConferenceEventOrStr] | None](
                        "ConferenceStatusCallbackEvent", conference_status_callback_event
                    ),
                    param[str | None]("ConferenceRecord", conference_record),
                    param[str | None]("ConferenceTrim", conference_trim),
                    param[str | None]("RecordingChannels", recording_channels),
                    param[str | None]("RecordingStatusCallback", recording_status_callback),
                    param[AmdStatusCallbackMethodOrStr | None](
                        "RecordingStatusCallbackMethod", recording_status_callback_method
                    ),
                    param[str | None]("ConferenceRecordingStatusCallback", conference_recording_status_callback),
                    param[AmdStatusCallbackMethodOrStr | None](
                        "ConferenceRecordingStatusCallbackMethod", conference_recording_status_callback_method
                    ),
                    param[str | None]("Region", region),
                    param[str | None]("SipAuthUsername", sip_auth_username),
                    param[str | None]("SipAuthPassword", sip_auth_password),
                    param[list[str] | None]("DequeueStatusCallbackEvent", dequeue_status_callback_event),
                    param[str | None]("PostWorkActivitySid", post_work_activity_sid),
                    param[TaskReservationEnumSupervisorModeOrStr | None]("SupervisorMode", supervisor_mode),
                    param[str | None]("Supervisor", supervisor),
                    param[bool | None]("EndConferenceOnCustomerExit", end_conference_on_customer_exit),
                    param[bool | None]("BeepOnCustomerEntrance", beep_on_customer_entrance),
                    param[str | None]("JitterBufferSize", jitter_buffer_size),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTaskTaskReservation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
