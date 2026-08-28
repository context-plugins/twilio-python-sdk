<!-- Generated file — do not edit; regenerated with the SDK. -->

# ProxyV1Session — operations

Accessor: `client.proxy_v1_session` · Source: `twilio/apis/proxy_v1_session.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.proxy_v1_session.create_session

- **Route**: `POST /v1/Services/{ServiceSid}/Sessions`
- **Server**: `default10`
- **Signature**: `def create_session(service_sid: str, *, unique_name: str | None = None, date_expiry: RFC3339DateTime | None = None, ttl: int | None = None, mode: SessionEnumModeOrStr | None = None, status: SessionEnumStatusOrStr | None = None, participants: list[Any] | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`
- **Params**: `service_sid` — path `ServiceSid` · `unique_name` — form field `UniqueName` · `date_expiry` — form field `DateExpiry` · `ttl` — form field `Ttl` · `mode` — form field `Mode` · `status` — form field `Status` · `participants` — form field `Participants`
- **Returns (parsed)**: `ProxyV1ServiceSession`
- **Returns (raw)**: `ApiResult[ProxyV1ServiceSession, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SessionEnumModeOrStr` | `twilio/models/enums/session_enum_mode.py` |
| `SessionEnumStatusOrStr` | `twilio/models/enums/session_enum_status.py` |
| `ProxyV1ServiceSession` | `twilio/models/proxy_v1_service_session.py` |

### client.proxy_v1_session.delete_session

- **Route**: `DELETE /v1/Services/{ServiceSid}/Sessions/{Sid}`
- **Server**: `default10`
- **Signature**: `def delete_session(service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.proxy_v1_session.fetch_session

- **Route**: `GET /v1/Services/{ServiceSid}/Sessions/{Sid}`
- **Server**: `default10`
- **Signature**: `def fetch_session(service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ProxyV1ServiceSession`
- **Returns (raw)**: `ApiResult[ProxyV1ServiceSession, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProxyV1ServiceSession` | `twilio/models/proxy_v1_service_session.py` |

### client.proxy_v1_session.list_session

- **Route**: `GET /v1/Services/{ServiceSid}/Sessions`
- **Server**: `default10`
- **Signature**: `def list_session(service_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`
- **Params**: `service_sid` — path `ServiceSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListSessionResponse`
- **Returns (raw)**: `ApiResult[ListSessionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListSessionResponse` | `twilio/models/list_session_response.py` |

### client.proxy_v1_session.update_session

- **Route**: `POST /v1/Services/{ServiceSid}/Sessions/{Sid}`
- **Server**: `default10`
- **Signature**: `def update_session(service_sid: str, sid: str, *, date_expiry: RFC3339DateTime | None = None, ttl: int | None = None, status: SessionEnumStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid` · `date_expiry` — form field `DateExpiry` · `ttl` — form field `Ttl` · `status` — form field `Status`
- **Returns (parsed)**: `ProxyV1ServiceSession`
- **Returns (raw)**: `ApiResult[ProxyV1ServiceSession, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SessionEnumStatusOrStr` | `twilio/models/enums/session_enum_status.py` |
| `ProxyV1ServiceSession` | `twilio/models/proxy_v1_service_session.py` |

