<!-- Generated file — do not edit; regenerated with the SDK. -->

# MessagingV1ShortCode — operations

Accessor: `client.messaging_v1_short_code` · Source: `twilio/apis/messaging_v1_short_code.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.messaging_v1_short_code.create_short_code

- **Route**: `POST /v1/Services/{ServiceSid}/ShortCodes`
- **Server**: `default1`
- **Signature**: `def create_short_code(service_sid: str, short_code_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `short_code_sid`
- **Params**: `service_sid` — path `ServiceSid` · `short_code_sid` — form field `ShortCodeSid`
- **Returns (parsed)**: `MessagingV1ServiceShortCode`
- **Returns (raw)**: `ApiResult[MessagingV1ServiceShortCode, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1ServiceShortCode` | `twilio/models/messaging_v1_service_short_code.py` |

### client.messaging_v1_short_code.delete_short_code

- **Route**: `DELETE /v1/Services/{ServiceSid}/ShortCodes/{Sid}`
- **Server**: `default1`
- **Signature**: `def delete_short_code(service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.messaging_v1_short_code.fetch_short_code2

- **Route**: `GET /v1/Services/{ServiceSid}/ShortCodes/{Sid}`
- **Server**: `default1`
- **Signature**: `def fetch_short_code2(service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `MessagingV1ServiceShortCode`
- **Returns (raw)**: `ApiResult[MessagingV1ServiceShortCode, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1ServiceShortCode` | `twilio/models/messaging_v1_service_short_code.py` |

### client.messaging_v1_short_code.list_short_code2

- **Route**: `GET /v1/Services/{ServiceSid}/ShortCodes`
- **Server**: `default1`
- **Signature**: `def list_short_code2(service_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`
- **Params**: `service_sid` — path `ServiceSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListShortCodeResponse1`
- **Returns (raw)**: `ApiResult[ListShortCodeResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListShortCodeResponse1` | `twilio/models/list_short_code_response1.py` |

