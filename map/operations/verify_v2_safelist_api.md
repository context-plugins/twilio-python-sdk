<!-- Generated file — do not edit; regenerated with the SDK. -->

# VerifyV2SafelistApi — operations

Accessor: `client.verify_v2_safelist_api` · Source: `twilio/apis/verify_v2_safelist_api.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.verify_v2_safelist_api.create_safelist

- **Route**: `POST /v2/SafeList/Numbers`
- **Server**: `default3`
- **Signature**: `def create_safelist(phone_number: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `phone_number`
- **Params**: `phone_number` — form field `PhoneNumber`
- **Returns (parsed)**: `VerifyV2Safelist`
- **Returns (raw)**: `ApiResult[VerifyV2Safelist, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2Safelist` | `twilio/models/verify_v2_safelist.py` |

### client.verify_v2_safelist_api.delete_safelist

- **Route**: `DELETE /v2/SafeList/Numbers/{PhoneNumber}`
- **Server**: `default3`
- **Signature**: `def delete_safelist(phone_number: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `phone_number`
- **Params**: `phone_number` — path `PhoneNumber`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.verify_v2_safelist_api.fetch_safelist

- **Route**: `GET /v2/SafeList/Numbers/{PhoneNumber}`
- **Server**: `default3`
- **Signature**: `def fetch_safelist(phone_number: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `phone_number`
- **Params**: `phone_number` — path `PhoneNumber`
- **Returns (parsed)**: `VerifyV2Safelist`
- **Returns (raw)**: `ApiResult[VerifyV2Safelist, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2Safelist` | `twilio/models/verify_v2_safelist.py` |

