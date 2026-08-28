<!-- Generated file — do not edit; regenerated with the SDK. -->

# MessagingV1PhoneNumber — operations

Accessor: `client.messaging_v1_phone_number` · Source: `twilio_sdk/apis/messaging_v1_phone_number.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.messaging_v1_phone_number.create_phone_number

- **Route**: `POST /v1/Services/{ServiceSid}/PhoneNumbers`
- **Server**: `default1`
- **Signature**: `def create_phone_number(service_sid: str, phone_number_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `phone_number_sid`
- **Params**: `service_sid` — path `ServiceSid` · `phone_number_sid` — form field `PhoneNumberSid`
- **Returns (parsed)**: `MessagingV1ServicePhoneNumber`
- **Returns (raw)**: `ApiResult[MessagingV1ServicePhoneNumber, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1ServicePhoneNumber` | `twilio_sdk/models/messaging_v1_service_phone_number.py` |

### client.messaging_v1_phone_number.delete_phone_number

- **Route**: `DELETE /v1/Services/{ServiceSid}/PhoneNumbers/{Sid}`
- **Server**: `default1`
- **Signature**: `def delete_phone_number(service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.messaging_v1_phone_number.fetch_phone_number

- **Route**: `GET /v1/Services/{ServiceSid}/PhoneNumbers/{Sid}`
- **Server**: `default1`
- **Signature**: `def fetch_phone_number(service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `MessagingV1ServicePhoneNumber`
- **Returns (raw)**: `ApiResult[MessagingV1ServicePhoneNumber, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1ServicePhoneNumber` | `twilio_sdk/models/messaging_v1_service_phone_number.py` |

### client.messaging_v1_phone_number.list_phone_number

- **Route**: `GET /v1/Services/{ServiceSid}/PhoneNumbers`
- **Server**: `default1`
- **Signature**: `def list_phone_number(service_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`
- **Params**: `service_sid` — path `ServiceSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListPhoneNumberResponse`
- **Returns (raw)**: `ApiResult[ListPhoneNumberResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListPhoneNumberResponse` | `twilio_sdk/models/list_phone_number_response.py` |

