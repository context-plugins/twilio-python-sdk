<!-- Generated file — do not edit; regenerated with the SDK. -->

# MessagingV1Deactivations — operations

Accessor: `client.messaging_v1_deactivations` · Source: `twilio_sdk/apis/messaging_v1_deactivations.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.messaging_v1_deactivations.fetch_deactivation

- **Route**: `GET /v1/Deactivations`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def fetch_deactivation(*, date: Date | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `date` — query `Date`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

