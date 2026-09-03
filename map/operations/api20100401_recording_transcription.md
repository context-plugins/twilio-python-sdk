<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401RecordingTranscription — operations

Accessor: `client.api20100401_recording_transcription` · Source: `twilio_sdk/apis/api20100401_recording_transcription.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.api20100401_recording_transcription.delete_recording_transcription

- **Route**: `DELETE /2010-04-01/Accounts/{AccountSid}/Recordings/{RecordingSid}/Transcriptions/{Sid}.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default`
- **Signature**: `def delete_recording_transcription(account_sid: str, recording_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `recording_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `recording_sid` — path `RecordingSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.api20100401_recording_transcription.fetch_recording_transcription

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Recordings/{RecordingSid}/Transcriptions/{Sid}.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default`
- **Signature**: `def fetch_recording_transcription(account_sid: str, recording_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `recording_sid`, `sid`
- **Params**: `account_sid` — path `AccountSid` · `recording_sid` — path `RecordingSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ApiV2010AccountRecordingRecordingTranscription`
- **Returns (raw)**: `ApiResult[ApiV2010AccountRecordingRecordingTranscription, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV2010AccountRecordingRecordingTranscription` | `twilio_sdk/models/api_v2010_account_recording_recording_transcription.py` |

### client.api20100401_recording_transcription.list_recording_transcription

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Recordings/{RecordingSid}/Transcriptions.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default`
- **Signature**: `def list_recording_transcription(account_sid: str, recording_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`, `recording_sid`
- **Params**: `account_sid` — path `AccountSid` · `recording_sid` — path `RecordingSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListRecordingTranscriptionResponse`
- **Returns (raw)**: `ApiResult[ListRecordingTranscriptionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListRecordingTranscriptionResponse` | `twilio_sdk/models/list_recording_transcription_response.py` |

