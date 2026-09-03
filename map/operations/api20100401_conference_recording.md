<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401ConferenceRecording — operations

Accessor: `client.api20100401_conference_recording` · Source: `twilio_sdk/apis/api20100401_conference_recording.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.api20100401_conference_recording.delete_conference_recording

- **Route**: `DELETE /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings/{Sid}.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default`
- **Signature**: `def delete_conference_recording(account_sid: str, conference_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `conference_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `conference_sid` — path `ConferenceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.api20100401_conference_recording.fetch_conference_recording

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings/{Sid}.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default`
- **Signature**: `def fetch_conference_recording(account_sid: str, conference_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `conference_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `conference_sid` — path `ConferenceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ApiV2010AccountConferenceConferenceRecording`
- **Returns (raw)**: `ApiResult[ApiV2010AccountConferenceConferenceRecording, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountConferenceConferenceRecording` | `twilio_sdk/models/api_v2010_account_conference_conference_recording.py` |

### client.api20100401_conference_recording.list_conference_recording

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default`
- **Signature**: `def list_conference_recording(account_sid: str, conference_sid: str, *, date_created: Date | None = None, date_created_query: Date | None = None, date_created_query_query: Date | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `conference_sid`
- **Params**: `account_sid` — path `AccountSid` · `conference_sid` — path `ConferenceSid` · `date_created` — query `DateCreated` · `date_created_query` — query `DateCreated<` · `date_created_query_query` — query `DateCreated>` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListConferenceRecordingResponse`
- **Returns (raw)**: `ApiResult[ListConferenceRecordingResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListConferenceRecordingResponse` | `twilio_sdk/models/list_conference_recording_response.py` |

### client.api20100401_conference_recording.update_conference_recording

- **Route**: `POST /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings/{Sid}.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default`
- **Signature**: `def update_conference_recording(account_sid: str, conference_sid: str, sid: str, status: ConferenceRecordingEnumStatusOrStr, *, pause_behavior: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `conference_sid`, `sid`, `status`
- **Params**: `account_sid` — path `AccountSid` · `conference_sid` — path `ConferenceSid` · `sid` — path `Sid` · `status` — form field `Status` · `pause_behavior` — form field `PauseBehavior`
- **Returns (parsed)**: `ApiV2010AccountConferenceConferenceRecording`
- **Returns (raw)**: `ApiResult[ApiV2010AccountConferenceConferenceRecording, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConferenceRecordingEnumStatusOrStr` | `twilio_sdk/models/enums/conference_recording_enum_status.py` |
| `ApiV2010AccountConferenceConferenceRecording` | `twilio_sdk/models/api_v2010_account_conference_conference_recording.py` |

