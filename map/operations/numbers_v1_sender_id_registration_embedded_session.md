<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV1SenderIdRegistrationEmbeddedSession — operations

Accessor: `client.numbers_v1_sender_id_registration_embedded_session` · Source: `twilio/apis/numbers_v1_sender_id_registration_embedded_session.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.numbers_v1_sender_id_registration_embedded_session.create_sender_id_registration_embedded_session

- **Route**: `POST /v1/SenderIdRegistrations/{BundleSid}/EmbeddedSessions`
- **Server**: `default5`
- **Signature**: `def create_sender_id_registration_embedded_session(bundle_sid: str, body: NumbersV1CreateEmbeddedSessionRequest | NumbersV1CreateEmbeddedSessionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `bundle_sid`, `body`
- **Params**: `bundle_sid` — path `BundleSid` · `body` — JSON body
- **Returns (parsed)**: `NumbersV1CreateEmbeddedSessionResponse`
- **Returns (raw)**: `ApiResult[NumbersV1CreateEmbeddedSessionResponse, CreateSenderIdRegistrationEmbeddedSessionErrorBody]`
- **Error**: `CreateSenderIdRegistrationEmbeddedSessionErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 404, 409, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `NumbersV1CreateEmbeddedSessionRequest` | `twilio/models/numbers_v1_create_embedded_session_request.py` |
| `NumbersV1CreateEmbeddedSessionRequestDict` | `twilio/models/numbers_v1_create_embedded_session_request.py` |
| `NumbersV1CreateEmbeddedSessionResponse` | `twilio/models/numbers_v1_create_embedded_session_response.py` |
| `CreateSenderIdRegistrationEmbeddedSessionErrorBody` | `twilio/errors/create_sender_id_registration_embedded_session_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio/models/accounts_calls_recordings_sid_json201041408_error1.py` |

