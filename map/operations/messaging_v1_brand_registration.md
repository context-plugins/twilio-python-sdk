<!-- Generated file — do not edit; regenerated with the SDK. -->

# MessagingV1BrandRegistration — operations

Accessor: `client.messaging_v1_brand_registration` · Source: `twilio_sdk/apis/messaging_v1_brand_registration.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.messaging_v1_brand_registration.create_brand_registrations

- **Route**: `POST /v1/a2p/BrandRegistrations`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def create_brand_registrations(customer_profile_bundle_sid: str, a2_p_profile_bundle_sid: str, *, brand_type: str | None = None, mock: bool | None = None, skip_automatic_sec_vet: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_profile_bundle_sid`, `a2_p_profile_bundle_sid`
- **Params**: `customer_profile_bundle_sid` — form field `CustomerProfileBundleSid` · `a2_p_profile_bundle_sid` — form field `A2PProfileBundleSid` · `brand_type` — form field `BrandType` · `mock` — form field `Mock` · `skip_automatic_sec_vet` — form field `SkipAutomaticSecVet`
- **Returns (parsed)**: `MessagingV1BrandRegistrations`
- **Returns (raw)**: `ApiResult[MessagingV1BrandRegistrations, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1BrandRegistrations` | `twilio_sdk/models/messaging_v1_brand_registrations.py` |

### client.messaging_v1_brand_registration.fetch_brand_registrations

- **Route**: `GET /v1/a2p/BrandRegistrations/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def fetch_brand_registrations(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `MessagingV1BrandRegistrations`
- **Returns (raw)**: `ApiResult[MessagingV1BrandRegistrations, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1BrandRegistrations` | `twilio_sdk/models/messaging_v1_brand_registrations.py` |

### client.messaging_v1_brand_registration.list_brand_registrations

- **Route**: `GET /v1/a2p/BrandRegistrations`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def list_brand_registrations(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListBrandRegistrationsResponse`
- **Returns (raw)**: `ApiResult[ListBrandRegistrationsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListBrandRegistrationsResponse` | `twilio_sdk/models/list_brand_registrations_response.py` |

### client.messaging_v1_brand_registration.update_brand_registrations

- **Route**: `POST /v1/a2p/BrandRegistrations/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def update_brand_registrations(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `MessagingV1BrandRegistrations`
- **Returns (raw)**: `ApiResult[MessagingV1BrandRegistrations, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1BrandRegistrations` | `twilio_sdk/models/messaging_v1_brand_registrations.py` |

