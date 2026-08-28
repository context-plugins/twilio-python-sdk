<!-- Generated file — do not edit; regenerated with the SDK. -->

# TaskrouterV1TaskReservation — operations

Accessor: `client.taskrouter_v1_task_reservation` · Source: `twilio_sdk/apis/taskrouter_v1_task_reservation.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.taskrouter_v1_task_reservation.fetch_task_reservation

- **Route**: `GET /v1/Workspaces/{WorkspaceSid}/Tasks/{TaskSid}/Reservations/{Sid}`
- **Server**: `default8`
- **Signature**: `def fetch_task_reservation(workspace_sid: str, task_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `task_sid`, `sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `task_sid` — path `TaskSid` · `sid` — path `Sid`
- **Returns (parsed)**: `TaskrouterV1WorkspaceTaskTaskReservation`
- **Returns (raw)**: `ApiResult[TaskrouterV1WorkspaceTaskTaskReservation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskrouterV1WorkspaceTaskTaskReservation` | `twilio_sdk/models/taskrouter_v1_workspace_task_task_reservation.py` |

### client.taskrouter_v1_task_reservation.list_task_reservation

- **Route**: `GET /v1/Workspaces/{WorkspaceSid}/Tasks/{TaskSid}/Reservations`
- **Server**: `default8`
- **Signature**: `def list_task_reservation(workspace_sid: str, task_sid: str, *, reservation_status: TaskReservationEnumStatusOrStr | None = None, worker_sid: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `task_sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `task_sid` — path `TaskSid` · `reservation_status` — query `ReservationStatus` · `worker_sid` — query `WorkerSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListTaskReservationResponse`
- **Returns (raw)**: `ApiResult[ListTaskReservationResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskReservationEnumStatusOrStr` | `twilio_sdk/models/enums/task_reservation_enum_status.py` |
| `ListTaskReservationResponse` | `twilio_sdk/models/list_task_reservation_response.py` |

### client.taskrouter_v1_task_reservation.update_task_reservation

- **Route**: `POST /v1/Workspaces/{WorkspaceSid}/Tasks/{TaskSid}/Reservations/{Sid}`
- **Server**: `default8`
- **Signature**: `def update_task_reservation(workspace_sid: str, task_sid: str, sid: str, *, if_match: str | None = None, reservation_status: TaskReservationEnumStatusOrStr | None = None, worker_activity_sid: str | None = None, instruction: str | None = None, dequeue_post_work_activity_sid: str | None = None, dequeue_from: str | None = None, dequeue_record: str | None = None, dequeue_timeout: int | None = None, dequeue_to: str | None = None, dequeue_status_callback_url: AnyUrl | None = None, call_from: str | None = None, call_record: str | None = None, call_timeout: int | None = None, call_to: str | None = None, call_url: AnyUrl | None = None, call_status_callback_url: AnyUrl | None = None, call_accept: bool | None = None, redirect_call_sid: str | None = None, redirect_accept: bool | None = None, redirect_url: AnyUrl | None = None, to: str | None = None, from_: str | None = None, status_callback: AnyUrl | None = None, status_callback_method: AmdStatusCallbackMethodOrStr | None = None, status_callback_event: list[CallEnumEventOrStr] | None = None, timeout: int | None = None, record: bool | None = None, muted: bool | None = None, beep: str | None = None, start_conference_on_enter: bool | None = None, end_conference_on_exit: bool | None = None, wait_url: AnyUrl | None = None, wait_method: AmdStatusCallbackMethodOrStr | None = None, early_media: bool | None = None, max_participants: int | None = None, conference_status_callback: AnyUrl | None = None, conference_status_callback_method: AmdStatusCallbackMethodOrStr | None = None, conference_status_callback_event: list[TaskReservationEnumConferenceEventOrStr] | None = None, conference_record: str | None = None, conference_trim: str | None = None, recording_channels: str | None = None, recording_status_callback: AnyUrl | None = None, recording_status_callback_method: AmdStatusCallbackMethodOrStr | None = None, conference_recording_status_callback: AnyUrl | None = None, conference_recording_status_callback_method: AmdStatusCallbackMethodOrStr | None = None, region: str | None = None, sip_auth_username: str | None = None, sip_auth_password: str | None = None, dequeue_status_callback_event: list[str] | None = None, post_work_activity_sid: str | None = None, supervisor_mode: TaskReservationEnumSupervisorModeOrStr | None = None, supervisor: str | None = None, end_conference_on_customer_exit: bool | None = None, beep_on_customer_entrance: bool | None = None, jitter_buffer_size: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workspace_sid`, `task_sid`, `sid`
- **Params**: `workspace_sid` — path `WorkspaceSid` · `task_sid` — path `TaskSid` · `sid` — path `Sid` · `if_match` — header `If-Match` · `reservation_status` — form field `ReservationStatus` · `worker_activity_sid` — form field `WorkerActivitySid` · `instruction` — form field `Instruction` · `dequeue_post_work_activity_sid` — form field `DequeuePostWorkActivitySid` · `dequeue_from` — form field `DequeueFrom` · `dequeue_record` — form field `DequeueRecord` · `dequeue_timeout` — form field `DequeueTimeout` · `dequeue_to` — form field `DequeueTo` · `dequeue_status_callback_url` — form field `DequeueStatusCallbackUrl` · `call_from` — form field `CallFrom` · `call_record` — form field `CallRecord` · `call_timeout` — form field `CallTimeout` · `call_to` — form field `CallTo` · `call_url` — form field `CallUrl` · `call_status_callback_url` — form field `CallStatusCallbackUrl` · `call_accept` — form field `CallAccept` · `redirect_call_sid` — form field `RedirectCallSid` · `redirect_accept` — form field `RedirectAccept` · `redirect_url` — form field `RedirectUrl` · `to` — form field `To` · `from_` — form field `From` · `status_callback` — form field `StatusCallback` · `status_callback_method` — form field `StatusCallbackMethod` · `status_callback_event` — form field `StatusCallbackEvent` · `timeout` — form field `Timeout` · `record` — form field `Record` · `muted` — form field `Muted` · `beep` — form field `Beep` · `start_conference_on_enter` — form field `StartConferenceOnEnter` · `end_conference_on_exit` — form field `EndConferenceOnExit` · `wait_url` — form field `WaitUrl` · `wait_method` — form field `WaitMethod` · `early_media` — form field `EarlyMedia` · `max_participants` — form field `MaxParticipants` · `conference_status_callback` — form field `ConferenceStatusCallback` · `conference_status_callback_method` — form field `ConferenceStatusCallbackMethod` · `conference_status_callback_event` — form field `ConferenceStatusCallbackEvent` · `conference_record` — form field `ConferenceRecord` · `conference_trim` — form field `ConferenceTrim` · `recording_channels` — form field `RecordingChannels` · `recording_status_callback` — form field `RecordingStatusCallback` · `recording_status_callback_method` — form field `RecordingStatusCallbackMethod` · `conference_recording_status_callback` — form field `ConferenceRecordingStatusCallback` · `conference_recording_status_callback_method` — form field `ConferenceRecordingStatusCallbackMethod` · `region` — form field `Region` · `sip_auth_username` — form field `SipAuthUsername` · `sip_auth_password` — form field `SipAuthPassword` · `dequeue_status_callback_event` — form field `DequeueStatusCallbackEvent` · `post_work_activity_sid` — form field `PostWorkActivitySid` · `supervisor_mode` — form field `SupervisorMode` · `supervisor` — form field `Supervisor` · `end_conference_on_customer_exit` — form field `EndConferenceOnCustomerExit` · `beep_on_customer_entrance` — form field `BeepOnCustomerEntrance` · `jitter_buffer_size` — form field `JitterBufferSize`
- **Returns (parsed)**: `TaskrouterV1WorkspaceTaskTaskReservation`
- **Returns (raw)**: `ApiResult[TaskrouterV1WorkspaceTaskTaskReservation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaskReservationEnumStatusOrStr` | `twilio_sdk/models/enums/task_reservation_enum_status.py` |
| `AmdStatusCallbackMethodOrStr` | `twilio_sdk/models/enums/amd_status_callback_method.py` |
| `CallEnumEventOrStr` | `twilio_sdk/models/enums/call_enum_event.py` |
| `TaskReservationEnumConferenceEventOrStr` | `twilio_sdk/models/enums/task_reservation_enum_conference_event.py` |
| `TaskReservationEnumSupervisorModeOrStr` | `twilio_sdk/models/enums/task_reservation_enum_supervisor_mode.py` |
| `TaskrouterV1WorkspaceTaskTaskReservation` | `twilio_sdk/models/taskrouter_v1_workspace_task_task_reservation.py` |

