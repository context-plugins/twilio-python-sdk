<!-- Generated file — do not edit; regenerated with the SDK. -->

# SyncV1StreamMessage — operations

Accessor: `client.sync_v1_stream_message` · Source: `twilio_sdk/apis/sync_v1_stream_message.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sync_v1_stream_message.create_stream_message

- **Route**: `POST /v1/Services/{ServiceSid}/Streams/{StreamSid}/Messages`
- **Auth**: `account_sid_auth_token`
- **Server**: `default12`
- **Signature**: `def create_stream_message(service_sid: str, stream_sid: str, data: Any, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `stream_sid`, `data`
- **Params**: `service_sid` — path `ServiceSid` · `stream_sid` — path `StreamSid` · `data` — form field `Data`
- **Returns (parsed)**: `SyncV1ServiceSyncStreamStreamMessage`
- **Returns (raw)**: `ApiResult[SyncV1ServiceSyncStreamStreamMessage, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SyncV1ServiceSyncStreamStreamMessage` | `twilio_sdk/models/sync_v1_service_sync_stream_stream_message.py` |

