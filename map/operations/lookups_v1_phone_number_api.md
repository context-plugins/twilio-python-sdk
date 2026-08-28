<!-- Generated file — do not edit; regenerated with the SDK. -->

# LookupsV1PhoneNumberApi — operations

Accessor: `client.lookups_v1_phone_number_api` · Source: `twilio_sdk/apis/lookups_v1_phone_number_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.lookups_v1_phone_number_api.fetch_phone_number2

- **Route**: `GET /v1/PhoneNumbers/{PhoneNumber}`
- **Server**: `default4`
- **Signature**: `def fetch_phone_number2(phone_number: str, *, country_code: str | None = None, type_: list[str] | None = None, add_ons: list[str] | None = None, add_ons_data: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `phone_number`
- **Params**: `phone_number` — path `PhoneNumber` · `country_code` — query `CountryCode` · `type_` — query `Type` · `add_ons` — query `AddOns` · `add_ons_data` — query `AddOnsData`
- **Returns (parsed)**: `LookupsV1PhoneNumber`
- **Returns (raw)**: `ApiResult[LookupsV1PhoneNumber, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LookupsV1PhoneNumber` | `twilio_sdk/models/lookups_v1_phone_number.py` |

