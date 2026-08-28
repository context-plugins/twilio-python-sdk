<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401Transcription — operations

Accessor: `client.api20100401_transcription` · Source: `twilio/apis/api20100401_transcription.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.api20100401_transcription.delete_transcription

- **Route**: `DELETE /2010-04-01/Accounts/{AccountSid}/Transcriptions/{Sid}.json`
- **Server**: `default`
- **Signature**: `def delete_transcription(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.api20100401_transcription.fetch_transcription

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Transcriptions/{Sid}.json`
- **Server**: `default`
- **Signature**: `def fetch_transcription(account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ApiV2010AccountTranscription`
- **Returns (raw)**: `ApiResult[ApiV2010AccountTranscription, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountTranscription` | `twilio/models/api_v2010_account_transcription.py` |

### client.api20100401_transcription.list_transcription

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Transcriptions.json`
- **Server**: `default`
- **Signature**: `def list_transcription(account_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`
- **Params**: `account_sid` — path `AccountSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListTranscriptionResponse`
- **Returns (raw)**: `ApiResult[ListTranscriptionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListTranscriptionResponse` | `twilio/models/list_transcription_response.py` |

