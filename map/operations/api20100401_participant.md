<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401Participant — operations

Accessor: `client.api20100401_participant` · Source: `twilio/apis/api20100401_participant.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.api20100401_participant.create_participant

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants.json`
- **Server**: `default`
- **Signature**: `def create_participant(account_sid: str, conference_sid: str, from_: str, to: str, *, status_callback: str | None = None, status_callback_method: StatusCallbackMethod16OrStr | None = None, status_callback_event: list[str] | None = None, label: str | None = None, timeout: int | None = None, record: bool | None = None, muted: bool | None = None, beep: str | None = None, start_conference_on_enter: bool | None = None, end_conference_on_exit: bool | None = None, wait_url: str | None = None, wait_method: WaitMethodOrStr | None = None, early_media: bool | None = None, max_participants: int | None = None, conference_record: str | None = None, conference_trim: str | None = None, conference_status_callback: str | None = None, conference_status_callback_method: ConferenceStatusCallbackMethodOrStr | None = None, conference_status_callback_event: list[str] | None = None, recording_channels: str | None = None, recording_status_callback: str | None = None, recording_status_callback_method: RecordingStatusCallbackMethod2OrStr | None = None, sip_auth_username: str | None = None, sip_auth_password: str | None = None, region: str | None = None, conference_recording_status_callback: str | None = None, conference_recording_status_callback_method: ConferenceRecordingStatusCallbackMethodOrStr | None = None, recording_status_callback_event: list[str] | None = None, conference_recording_status_callback_event: list[str] | None = None, coaching: bool | None = None, call_sid_to_coach: str | None = None, jitter_buffer_size: str | None = None, byoc: str | None = None, caller_id: str | None = None, call_reason: str | None = None, recording_track: str | None = None, recording_configuration_id: str | None = None, time_limit: int | None = None, machine_detection: str | None = None, machine_detection_timeout: int | None = None, machine_detection_speech_threshold: int | None = None, machine_detection_speech_end_threshold: int | None = None, machine_detection_silence_timeout: int | None = None, amd_status_callback: str | None = None, amd_status_callback_method: AmdStatusCallbackMethodOrStr | None = None, trim: str | None = None, call_token: str | None = None, client_notification_url: str | None = None, caller_display_name: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `conference_sid`, `from_`, `to`
- **Params**: `account_sid` — path `AccountSid` · `conference_sid` — path `ConferenceSid` · `from_` — form field `From` · `to` — form field `To` · `status_callback` — form field `StatusCallback` · `status_callback_method` — form field `StatusCallbackMethod` · `status_callback_event` — form field `StatusCallbackEvent` · `label` — form field `Label` · `timeout` — form field `Timeout` · `record` — form field `Record` · `muted` — form field `Muted` · `beep` — form field `Beep` · `start_conference_on_enter` — form field `StartConferenceOnEnter` · `end_conference_on_exit` — form field `EndConferenceOnExit` · `wait_url` — form field `WaitUrl` · `wait_method` — form field `WaitMethod` · `early_media` — form field `EarlyMedia` · `max_participants` — form field `MaxParticipants` · `conference_record` — form field `ConferenceRecord` · `conference_trim` — form field `ConferenceTrim` · `conference_status_callback` — form field `ConferenceStatusCallback` · `conference_status_callback_method` — form field `ConferenceStatusCallbackMethod` · `conference_status_callback_event` — form field `ConferenceStatusCallbackEvent` · `recording_channels` — form field `RecordingChannels` · `recording_status_callback` — form field `RecordingStatusCallback` · `recording_status_callback_method` — form field `RecordingStatusCallbackMethod` · `sip_auth_username` — form field `SipAuthUsername` · `sip_auth_password` — form field `SipAuthPassword` · `region` — form field `Region` · `conference_recording_status_callback` — form field `ConferenceRecordingStatusCallback` · `conference_recording_status_callback_method` — form field `ConferenceRecordingStatusCallbackMethod` · `recording_status_callback_event` — form field `RecordingStatusCallbackEvent` · `conference_recording_status_callback_event` — form field `ConferenceRecordingStatusCallbackEvent` · `coaching` — form field `Coaching` · `call_sid_to_coach` — form field `CallSidToCoach` · `jitter_buffer_size` — form field `JitterBufferSize` · `byoc` — form field `Byoc` · `caller_id` — form field `CallerId` · `call_reason` — form field `CallReason` · `recording_track` — form field `RecordingTrack` · `recording_configuration_id` — form field `RecordingConfigurationId` · `time_limit` — form field `TimeLimit` · `machine_detection` — form field `MachineDetection` · `machine_detection_timeout` — form field `MachineDetectionTimeout` · `machine_detection_speech_threshold` — form field `MachineDetectionSpeechThreshold` · `machine_detection_speech_end_threshold` — form field `MachineDetectionSpeechEndThreshold` · `machine_detection_silence_timeout` — form field `MachineDetectionSilenceTimeout` · `amd_status_callback` — form field `AmdStatusCallback` · `amd_status_callback_method` — form field `AmdStatusCallbackMethod` · `trim` — form field `Trim` · `call_token` — form field `CallToken` · `client_notification_url` — form field `ClientNotificationUrl` · `caller_display_name` — form field `CallerDisplayName`
- **Returns (parsed)**: `ApiV2010AccountConferenceParticipant`
- **Returns (raw)**: `ApiResult[ApiV2010AccountConferenceParticipant, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StatusCallbackMethod16OrStr` | `twilio/models/enums/status_callback_method16.py` |
| `WaitMethodOrStr` | `twilio/models/enums/wait_method.py` |
| `ConferenceStatusCallbackMethodOrStr` | `twilio/models/enums/conference_status_callback_method.py` |
| `RecordingStatusCallbackMethod2OrStr` | `twilio/models/enums/recording_status_callback_method2.py` |
| `ConferenceRecordingStatusCallbackMethodOrStr` | `twilio/models/enums/conference_recording_status_callback_method.py` |
| `AmdStatusCallbackMethodOrStr` | `twilio/models/enums/amd_status_callback_method.py` |
| `ApiV2010AccountConferenceParticipant` | `twilio/models/api_v2010_account_conference_participant.py` |

### client.api20100401_participant.delete_participant

- **Route**: `DELETE /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}.json`
- **Server**: `default`
- **Signature**: `def delete_participant(account_sid: str, conference_sid: str, call_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `conference_sid`, `call_sid`
- **Params**: `account_sid` — path `AccountSid` · `conference_sid` — path `ConferenceSid` · `call_sid` — path `CallSid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.api20100401_participant.fetch_participant

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}.json`
- **Server**: `default`
- **Signature**: `def fetch_participant(account_sid: str, conference_sid: str, call_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `conference_sid`, `call_sid`
- **Params**: `account_sid` — path `AccountSid` · `conference_sid` — path `ConferenceSid` · `call_sid` — path `CallSid`
- **Returns (parsed)**: `ApiV2010AccountConferenceParticipant`
- **Returns (raw)**: `ApiResult[ApiV2010AccountConferenceParticipant, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountConferenceParticipant` | `twilio/models/api_v2010_account_conference_participant.py` |

### client.api20100401_participant.list_participant

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants.json`
- **Server**: `default`
- **Signature**: `def list_participant(account_sid: str, conference_sid: str, *, muted: bool | None = None, hold: bool | None = None, coaching: bool | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `conference_sid`
- **Params**: `account_sid` — path `AccountSid` · `conference_sid` — path `ConferenceSid` · `muted` — query `Muted` · `hold` — query `Hold` · `coaching` — query `Coaching` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListParticipantResponse`
- **Returns (raw)**: `ApiResult[ListParticipantResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListParticipantResponse` | `twilio/models/list_participant_response.py` |

### client.api20100401_participant.update_participant

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}.json`
- **Server**: `default`
- **Signature**: `def update_participant(account_sid: str, conference_sid: str, call_sid: str, *, muted: bool | None = None, hold: bool | None = None, hold_url: str | None = None, hold_method: HoldMethodOrStr | None = None, announce_url: str | None = None, announce_method: AnnounceMethod1OrStr | None = None, wait_url: str | None = None, wait_method: WaitMethodOrStr | None = None, beep_on_exit: bool | None = None, end_conference_on_exit: bool | None = None, coaching: bool | None = None, call_sid_to_coach: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `conference_sid`, `call_sid`
- **Params**: `account_sid` — path `AccountSid` · `conference_sid` — path `ConferenceSid` · `call_sid` — path `CallSid` · `muted` — form field `Muted` · `hold` — form field `Hold` · `hold_url` — form field `HoldUrl` · `hold_method` — form field `HoldMethod` · `announce_url` — form field `AnnounceUrl` · `announce_method` — form field `AnnounceMethod` · `wait_url` — form field `WaitUrl` · `wait_method` — form field `WaitMethod` · `beep_on_exit` — form field `BeepOnExit` · `end_conference_on_exit` — form field `EndConferenceOnExit` · `coaching` — form field `Coaching` · `call_sid_to_coach` — form field `CallSidToCoach`
- **Returns (parsed)**: `ApiV2010AccountConferenceParticipant`
- **Returns (raw)**: `ApiResult[ApiV2010AccountConferenceParticipant, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `HoldMethodOrStr` | `twilio/models/enums/hold_method.py` |
| `AnnounceMethod1OrStr` | `twilio/models/enums/announce_method1.py` |
| `WaitMethodOrStr` | `twilio/models/enums/wait_method.py` |
| `ApiV2010AccountConferenceParticipant` | `twilio/models/api_v2010_account_conference_participant.py` |

