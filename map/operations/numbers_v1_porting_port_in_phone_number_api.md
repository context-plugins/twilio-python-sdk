<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV1PortingPortInPhoneNumberApi — operations

Accessor: `client.numbers_v1_porting_port_in_phone_number_api` · Source: `twilio_sdk/apis/numbers_v1_porting_port_in_phone_number_api.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.numbers_v1_porting_port_in_phone_number_api.delete_porting_port_in_phone_number

- **Route**: `DELETE /v1/Porting/PortIn/{PortInRequestSid}/PhoneNumber/{PhoneNumberSid}`
- **Server**: `default5`
- **Signature**: `def delete_porting_port_in_phone_number(port_in_request_sid: str, phone_number_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `port_in_request_sid`, `phone_number_sid`
- **Params**: `port_in_request_sid` — path `PortInRequestSid` · `phone_number_sid` — path `PhoneNumberSid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.numbers_v1_porting_port_in_phone_number_api.fetch_porting_port_in_phone_number

- **Route**: `GET /v1/Porting/PortIn/{PortInRequestSid}/PhoneNumber/{PhoneNumberSid}`
- **Server**: `default5`
- **Signature**: `def fetch_porting_port_in_phone_number(port_in_request_sid: str, phone_number_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `port_in_request_sid`, `phone_number_sid`
- **Params**: `port_in_request_sid` — path `PortInRequestSid` · `phone_number_sid` — path `PhoneNumberSid`
- **Returns (parsed)**: `NumbersV1PortingPortInPhoneNumber`
- **Returns (raw)**: `ApiResult[NumbersV1PortingPortInPhoneNumber, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV1PortingPortInPhoneNumber` | `twilio_sdk/models/numbers_v1_porting_port_in_phone_number.py` |

