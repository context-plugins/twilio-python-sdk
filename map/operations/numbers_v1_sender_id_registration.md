<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV1SenderIdRegistration — operations

Accessor: `client.numbers_v1_sender_id_registration` · Source: `twilio/apis/numbers_v1_sender_id_registration.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.numbers_v1_sender_id_registration.create_sender_id_registration

- **Route**: `POST /v1/SenderIdRegistrations`
- **Server**: `default5`
- **Signature**: `def create_sender_id_registration(body: NumbersV1CreateEmbeddedRegistrationRequest | NumbersV1CreateEmbeddedRegistrationRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `NumbersV1CreateEmbeddedRegistrationResponse`
- **Returns (raw)**: `ApiResult[NumbersV1CreateEmbeddedRegistrationResponse, CreateSenderIdRegistrationErrorBody]`
- **Error**: `CreateSenderIdRegistrationErrorBody` — **Case A (typed)**
- **Error arms**: `AccountsCallsRecordingsSidJson201041408Error1` [400, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `NumbersV1CreateEmbeddedRegistrationRequest` | `twilio/models/numbers_v1_create_embedded_registration_request.py` |
| `NumbersV1CreateEmbeddedRegistrationRequestDict` | `twilio/models/numbers_v1_create_embedded_registration_request.py` |
| `NumbersV1CreateEmbeddedRegistrationResponse` | `twilio/models/numbers_v1_create_embedded_registration_response.py` |
| `CreateSenderIdRegistrationErrorBody` | `twilio/errors/create_sender_id_registration_error.py` |
| `AccountsCallsRecordingsSidJson201041408Error1` | `twilio/models/accounts_calls_recordings_sid_json201041408_error1.py` |

