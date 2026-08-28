<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401CallRecording — operations

Accessor: `client.api20100401_call_recording` · Source: `twilio/apis/api20100401_call_recording.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.api20100401_call_recording.create_call_recording

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Recordings.json`
- **Server**: `default`
- **Signature**: `def create_call_recording(account_sid: str, call_sid: str, *, recording_status_callback_event: list[str] | None = None, recording_status_callback: str | None = None, recording_status_callback_method: RecordingStatusCallbackMethod1OrStr | None = None, trim: str | None = None, recording_channels: str | None = None, recording_track: str | None = None, recording_configuration_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `call_sid`
- **Params**: `account_sid` — path `AccountSid` · `call_sid` — path `CallSid` · `recording_status_callback_event` — form field `RecordingStatusCallbackEvent` · `recording_status_callback` — form field `RecordingStatusCallback` · `recording_status_callback_method` — form field `RecordingStatusCallbackMethod` · `trim` — form field `Trim` · `recording_channels` — form field `RecordingChannels` · `recording_track` — form field `RecordingTrack` · `recording_configuration_id` — form field `RecordingConfigurationId`
- **Returns (parsed)**: `ApiV2010AccountCallCallRecording`
- **Returns (raw)**: `ApiResult[ApiV2010AccountCallCallRecording, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RecordingStatusCallbackMethod1OrStr` | `twilio/models/enums/recording_status_callback_method1.py` |
| `ApiV2010AccountCallCallRecording` | `twilio/models/api_v2010_account_call_call_recording.py` |

### client.api20100401_call_recording.delete_call_recording

- **Route**: `DELETE /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Recordings/{Sid}.json`
- **Server**: `default`
- **Signature**: `def delete_call_recording(account_sid: str, call_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `call_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `call_sid` — path `CallSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.api20100401_call_recording.fetch_call_recording

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Recordings/{Sid}.json`
- **Server**: `default`
- **Signature**: `def fetch_call_recording(account_sid: str, call_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `call_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `call_sid` — path `CallSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ApiV2010AccountCallCallRecording`
- **Returns (raw)**: `ApiResult[ApiV2010AccountCallCallRecording, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountCallCallRecording` | `twilio/models/api_v2010_account_call_call_recording.py` |

### client.api20100401_call_recording.list_call_recording

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Recordings.json`
- **Server**: `default`
- **Signature**: `def list_call_recording(account_sid: str, call_sid: str, *, date_created: Date | None = None, date_created_query: Date | None = None, date_created_query_query: Date | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `call_sid`
- **Params**: `account_sid` — path `AccountSid` · `call_sid` — path `CallSid` · `date_created` — query `DateCreated` · `date_created_query` — query `DateCreated<` · `date_created_query_query` — query `DateCreated>` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListCallRecordingResponse`
- **Returns (raw)**: `ApiResult[ListCallRecordingResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListCallRecordingResponse` | `twilio/models/list_call_recording_response.py` |

### client.api20100401_call_recording.update_call_recording

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Recordings/{Sid}.json`
- **Server**: `default`
- **Signature**: `def update_call_recording(account_sid: str, call_sid: str, sid: str, status: CallRecordingEnumStatusOrStr, *, pause_behavior: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `call_sid`, `sid`, `status`
- **Params**: `account_sid` — path `AccountSid` · `call_sid` — path `CallSid` · `sid` — path `Sid` · `status` — form field `Status` · `pause_behavior` — form field `PauseBehavior`
- **Returns (parsed)**: `ApiV2010AccountCallCallRecording`
- **Returns (raw)**: `ApiResult[ApiV2010AccountCallCallRecording, UpdateCallRecordingErrorBody]`
- **Error**: `UpdateCallRecordingErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [408] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CallRecordingEnumStatusOrStr` | `twilio/models/enums/call_recording_enum_status.py` |
| `ApiV2010AccountCallCallRecording` | `twilio/models/api_v2010_account_call_call_recording.py` |
| `UpdateCallRecordingErrorBody` | `twilio/errors/update_call_recording_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio/models/accounts_calls_recordings_sid_json201041408_error1.py` |

