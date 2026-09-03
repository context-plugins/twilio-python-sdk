<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV1PortingPortabilityApi — operations

Accessor: `client.numbers_v1_porting_portability_api` · Source: `twilio_sdk/apis/numbers_v1_porting_portability_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.numbers_v1_porting_portability_api.fetch_porting_portability

- **Route**: `GET /v1/Porting/Portability/PhoneNumber/{PhoneNumber}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default5`
- **Signature**: `def fetch_porting_portability(phone_number: str, *, target_account_sid: str | None = None, address_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `phone_number`
- **Params**: `phone_number` — path `PhoneNumber` · `target_account_sid` — query `TargetAccountSid` · `address_sid` — query `AddressSid`
- **Returns (parsed)**: `NumbersV1PortingPortability`
- **Returns (raw)**: `ApiResult[NumbersV1PortingPortability, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV1PortingPortability` | `twilio_sdk/models/numbers_v1_porting_portability.py` |

