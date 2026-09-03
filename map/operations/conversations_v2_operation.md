<!-- Generated file — do not edit; regenerated with the SDK. -->

# ConversationsV2Operation — operations

Accessor: `client.conversations_v2_operation` · Source: `twilio_sdk/apis/conversations_v2_operation.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.conversations_v2_operation.fetch_operation_status

- **Route**: `GET /v2/ControlPlane/Operations/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default7`
- **Signature**: `def fetch_operation_status(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `ConversationsV2OperationStatus`
- **Returns (raw)**: `ApiResult[ConversationsV2OperationStatus, FetchOperationStatusErrorBody]`
- **Error**: `FetchOperationStatusErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 404, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConversationsV2OperationStatus` | `twilio_sdk/models/conversations_v2_operation_status.py` |
| `FetchOperationStatusErrorBody` | `twilio_sdk/errors/fetch_operation_status_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio_sdk/models/accounts_calls_recordings_sid_json201041408_error1.py` |

