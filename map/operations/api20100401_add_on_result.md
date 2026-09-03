<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401AddOnResult — operations

Accessor: `client.api20100401_add_on_result` · Source: `twilio_sdk/apis/api20100401_add_on_result.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.api20100401_add_on_result.delete_recording_add_on_result

- **Route**: `DELETE /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{Sid}.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default`
- **Signature**: `def delete_recording_add_on_result(account_sid: str, reference_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `reference_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `reference_sid` — path `ReferenceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.api20100401_add_on_result.fetch_recording_add_on_result

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{Sid}.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default`
- **Signature**: `def fetch_recording_add_on_result(account_sid: str, reference_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `reference_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `reference_sid` — path `ReferenceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ApiV2010AccountRecordingRecordingAddOnResult`
- **Returns (raw)**: `ApiResult[ApiV2010AccountRecordingRecordingAddOnResult, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountRecordingRecordingAddOnResult` | `twilio_sdk/models/api_v2010_account_recording_recording_add_on_result.py` |

### client.api20100401_add_on_result.list_recording_add_on_result

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default`
- **Signature**: `def list_recording_add_on_result(account_sid: str, reference_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `reference_sid`
- **Params**: `account_sid` — path `AccountSid` · `reference_sid` — path `ReferenceSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListRecordingAddOnResultResponse`
- **Returns (raw)**: `ApiResult[ListRecordingAddOnResultResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListRecordingAddOnResultResponse` | `twilio_sdk/models/list_recording_add_on_result_response.py` |

