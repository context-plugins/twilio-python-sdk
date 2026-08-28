<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401Recording — operations

Accessor: `client.api20100401_recording` · Source: `twilio/apis/api20100401_recording.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.api20100401_recording.delete_recording

- **Route**: `DELETE /2010-04-01/Accounts/{AccountSid}/Recordings/{Sid}.json`
- **Server**: `default`
- **Signature**: `def delete_recording(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.api20100401_recording.fetch_recording

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Recordings/{Sid}.json`
- **Server**: `default`
- **Signature**: `def fetch_recording(account_sid: str, sid: str, *, include_soft_deleted: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid` · `include_soft_deleted` — query `IncludeSoftDeleted`
- **Returns (parsed)**: `ApiV2010AccountRecording`
- **Returns (raw)**: `ApiResult[ApiV2010AccountRecording, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountRecording` | `twilio/models/api_v2010_account_recording.py` |

### client.api20100401_recording.list_recording

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Recordings.json`
- **Server**: `default`
- **Signature**: `def list_recording(account_sid: str, *, date_created: RFC3339DateTime | None = None, date_created_query: RFC3339DateTime | None = None, date_created_query_query: RFC3339DateTime | None = None, call_sid: str | None = None, conference_sid: str | None = None, include_soft_deleted: bool | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`
- **Params**: `account_sid` — path `AccountSid` · `date_created` — query `DateCreated` · `date_created_query` — query `DateCreated<` · `date_created_query_query` — query `DateCreated>` · `call_sid` — query `CallSid` · `conference_sid` — query `ConferenceSid` · `include_soft_deleted` — query `IncludeSoftDeleted` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListRecordingResponse`
- **Returns (raw)**: `ApiResult[ListRecordingResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListRecordingResponse` | `twilio/models/list_recording_response.py` |

