<!-- Generated file — do not edit; regenerated with the SDK. -->

# MessagingV1UsecaseApi — operations

Accessor: `client.messaging_v1_usecase_api` · Source: `twilio_sdk/apis/messaging_v1_usecase_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.messaging_v1_usecase_api.fetch_usecase

- **Route**: `GET /v1/Services/Usecases`
- **Server**: `default1`
- **Signature**: `def fetch_usecase(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `MessagingV1Usecase`
- **Returns (raw)**: `ApiResult[MessagingV1Usecase, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1Usecase` | `twilio_sdk/models/messaging_v1_usecase.py` |

