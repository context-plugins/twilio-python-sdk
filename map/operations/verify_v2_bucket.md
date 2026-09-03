<!-- Generated file — do not edit; regenerated with the SDK. -->

# VerifyV2Bucket — operations

Accessor: `client.verify_v2_bucket` · Source: `twilio_sdk/apis/verify_v2_bucket.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.verify_v2_bucket.create_bucket

- **Route**: `POST /v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets`
- **Auth**: `account_sid_auth_token`
- **Server**: `default3`
- **Signature**: `def create_bucket(service_sid: str, rate_limit_sid: str, max: int, interval: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `rate_limit_sid`, `max`, `interval`
- **Params**: `service_sid` — path `ServiceSid` · `rate_limit_sid` — path `RateLimitSid` · `max` — form field `Max` · `interval` — form field `Interval`
- **Returns (parsed)**: `VerifyV2ServiceRateLimitBucket`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceRateLimitBucket, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2ServiceRateLimitBucket` | `twilio_sdk/models/verify_v2_service_rate_limit_bucket.py` |

### client.verify_v2_bucket.delete_bucket

- **Route**: `DELETE /v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default3`
- **Signature**: `def delete_bucket(service_sid: str, rate_limit_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `rate_limit_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `rate_limit_sid` — path `RateLimitSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.verify_v2_bucket.fetch_bucket

- **Route**: `GET /v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default3`
- **Signature**: `def fetch_bucket(service_sid: str, rate_limit_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `rate_limit_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `rate_limit_sid` — path `RateLimitSid` · `sid` — path `Sid`
- **Returns (parsed)**: `VerifyV2ServiceRateLimitBucket`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceRateLimitBucket, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2ServiceRateLimitBucket` | `twilio_sdk/models/verify_v2_service_rate_limit_bucket.py` |

### client.verify_v2_bucket.list_bucket

- **Route**: `GET /v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets`
- **Auth**: `account_sid_auth_token`
- **Server**: `default3`
- **Signature**: `def list_bucket(service_sid: str, rate_limit_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `rate_limit_sid`
- **Params**: `service_sid` — path `ServiceSid` · `rate_limit_sid` — path `RateLimitSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListBucketResponse`
- **Returns (raw)**: `ApiResult[ListBucketResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListBucketResponse` | `twilio_sdk/models/list_bucket_response.py` |

### client.verify_v2_bucket.update_bucket

- **Route**: `POST /v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default3`
- **Signature**: `def update_bucket(service_sid: str, rate_limit_sid: str, sid: str, *, max: int | None = None, interval: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `rate_limit_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `rate_limit_sid` — path `RateLimitSid` · `sid` — path `Sid` · `max` — form field `Max` · `interval` — form field `Interval`
- **Returns (parsed)**: `VerifyV2ServiceRateLimitBucket`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceRateLimitBucket, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2ServiceRateLimitBucket` | `twilio_sdk/models/verify_v2_service_rate_limit_bucket.py` |

