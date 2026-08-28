<!-- Generated file — do not edit; regenerated with the SDK. -->

# VerifyV2RateLimit — operations

Accessor: `client.verify_v2_rate_limit` · Source: `twilio_sdk/apis/verify_v2_rate_limit.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.verify_v2_rate_limit.create_rate_limit

- **Route**: `POST /v2/Services/{ServiceSid}/RateLimits`
- **Server**: `default3`
- **Signature**: `def create_rate_limit(service_sid: str, unique_name: str, *, description: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `unique_name`
- **Params**: `service_sid` — path `ServiceSid` · `unique_name` — form field `UniqueName` · `description` — form field `Description`
- **Returns (parsed)**: `VerifyV2ServiceRateLimit`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceRateLimit, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2ServiceRateLimit` | `twilio_sdk/models/verify_v2_service_rate_limit.py` |

### client.verify_v2_rate_limit.delete_rate_limit

- **Route**: `DELETE /v2/Services/{ServiceSid}/RateLimits/{Sid}`
- **Server**: `default3`
- **Signature**: `def delete_rate_limit(service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.verify_v2_rate_limit.fetch_rate_limit

- **Route**: `GET /v2/Services/{ServiceSid}/RateLimits/{Sid}`
- **Server**: `default3`
- **Signature**: `def fetch_rate_limit(service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid`
- **Returns (parsed)**: `VerifyV2ServiceRateLimit`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceRateLimit, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2ServiceRateLimit` | `twilio_sdk/models/verify_v2_service_rate_limit.py` |

### client.verify_v2_rate_limit.list_rate_limit

- **Route**: `GET /v2/Services/{ServiceSid}/RateLimits`
- **Server**: `default3`
- **Signature**: `def list_rate_limit(service_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`
- **Params**: `service_sid` — path `ServiceSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListRateLimitResponse`
- **Returns (raw)**: `ApiResult[ListRateLimitResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListRateLimitResponse` | `twilio_sdk/models/list_rate_limit_response.py` |

### client.verify_v2_rate_limit.update_rate_limit

- **Route**: `POST /v2/Services/{ServiceSid}/RateLimits/{Sid}`
- **Server**: `default3`
- **Signature**: `def update_rate_limit(service_sid: str, sid: str, *, description: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `sid` — path `Sid` · `description` — form field `Description`
- **Returns (parsed)**: `VerifyV2ServiceRateLimit`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceRateLimit, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2ServiceRateLimit` | `twilio_sdk/models/verify_v2_service_rate_limit.py` |

