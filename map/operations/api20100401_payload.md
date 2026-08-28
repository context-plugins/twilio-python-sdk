<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401Payload — operations

Accessor: `client.api20100401_payload` · Source: `twilio/apis/api20100401_payload.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.api20100401_payload.delete_recording_add_on_result_payload

- **Route**: `DELETE /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{AddOnResultSid}/Payloads/{Sid}.json`
- **Server**: `default`
- **Signature**: `def delete_recording_add_on_result_payload(account_sid: str, reference_sid: str, add_on_result_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `reference_sid`, `add_on_result_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `reference_sid` — path `ReferenceSid` · `add_on_result_sid` — path `AddOnResultSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.api20100401_payload.fetch_recording_add_on_result_payload

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{AddOnResultSid}/Payloads/{Sid}.json`
- **Server**: `default`
- **Signature**: `def fetch_recording_add_on_result_payload(account_sid: str, reference_sid: str, add_on_result_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `reference_sid`, `add_on_result_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `reference_sid` — path `ReferenceSid` · `add_on_result_sid` — path `AddOnResultSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload`
- **Returns (raw)**: `ApiResult[ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload` | `twilio/models/api_v2010_account_recording_recording_add_on_result_recording_add_on_result_payload.py` |

### client.api20100401_payload.list_recording_add_on_result_payload

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{AddOnResultSid}/Payloads.json`
- **Server**: `default`
- **Signature**: `def list_recording_add_on_result_payload(account_sid: str, reference_sid: str, add_on_result_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `reference_sid`, `add_on_result_sid`
- **Params**: `account_sid` — path `AccountSid` · `reference_sid` — path `ReferenceSid` · `add_on_result_sid` — path `AddOnResultSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListRecordingAddOnResultPayloadResponse`
- **Returns (raw)**: `ApiResult[ListRecordingAddOnResultPayloadResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListRecordingAddOnResultPayloadResponse` | `twilio/models/list_recording_add_on_result_payload_response.py` |

