<!-- Generated file — do not edit; regenerated with the SDK. -->

# ProxyV1PhoneNumber — operations

Accessor: `client.proxy_v1_phone_number` · Source: `twilio_sdk/apis/proxy_v1_phone_number.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.proxy_v1_phone_number.create_phone_number2

- **Route**: `POST /v1/Services/{ServiceSid}/PhoneNumbers`
- **Auth**: `account_sid_auth_token`
- **Server**: `default10`
- **Signature**: `def create_phone_number2(service_sid: str, *, sid: str | None = None, phone_number: str | None = None, is_reserved: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — form field `Sid` · `phone_number` — form field `PhoneNumber` · `is_reserved` — form field `IsReserved`
- **Returns (parsed)**: `ProxyV1ServicePhoneNumber`
- **Returns (raw)**: `ApiResult[ProxyV1ServicePhoneNumber, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProxyV1ServicePhoneNumber` | `twilio_sdk/models/proxy_v1_service_phone_number.py` |

### client.proxy_v1_phone_number.delete_phone_number2

- **Route**: `DELETE /v1/Services/{ServiceSid}/PhoneNumbers/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default10`
- **Signature**: `def delete_phone_number2(service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.proxy_v1_phone_number.fetch_phone_number4

- **Route**: `GET /v1/Services/{ServiceSid}/PhoneNumbers/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default10`
- **Signature**: `def fetch_phone_number4(service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ProxyV1ServicePhoneNumber`
- **Returns (raw)**: `ApiResult[ProxyV1ServicePhoneNumber, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProxyV1ServicePhoneNumber` | `twilio_sdk/models/proxy_v1_service_phone_number.py` |

### client.proxy_v1_phone_number.list_phone_number2

- **Route**: `GET /v1/Services/{ServiceSid}/PhoneNumbers`
- **Auth**: `account_sid_auth_token`
- **Server**: `default10`
- **Signature**: `def list_phone_number2(service_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`
- **Params**: `service_sid` — path `ServiceSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListPhoneNumberResponse1`
- **Returns (raw)**: `ApiResult[ListPhoneNumberResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListPhoneNumberResponse1` | `twilio_sdk/models/list_phone_number_response1.py` |

### client.proxy_v1_phone_number.update_phone_number

- **Route**: `POST /v1/Services/{ServiceSid}/PhoneNumbers/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default10`
- **Signature**: `def update_phone_number(service_sid: str, sid: str, *, is_reserved: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid` · `is_reserved` — form field `IsReserved`
- **Returns (parsed)**: `ProxyV1ServicePhoneNumber`
- **Returns (raw)**: `ApiResult[ProxyV1ServicePhoneNumber, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProxyV1ServicePhoneNumber` | `twilio_sdk/models/proxy_v1_service_phone_number.py` |

