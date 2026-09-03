<!-- Generated file — do not edit; regenerated with the SDK. -->

# MessagingV1BrandVetting — operations

Accessor: `client.messaging_v1_brand_vetting` · Source: `twilio_sdk/apis/messaging_v1_brand_vetting.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.messaging_v1_brand_vetting.create_brand_vetting

- **Route**: `POST /v1/a2p/BrandRegistrations/{BrandSid}/Vettings`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def create_brand_vetting(brand_sid: str, vetting_provider: BrandVettingEnumVettingProviderOrStr, *, vetting_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `brand_sid`, `vetting_provider`
- **Params**: `brand_sid` — path `BrandSid` · `vetting_provider` — form field `VettingProvider` · `vetting_id` — form field `VettingId`
- **Returns (parsed)**: `MessagingV1BrandRegistrationsBrandVetting`
- **Returns (raw)**: `ApiResult[MessagingV1BrandRegistrationsBrandVetting, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BrandVettingEnumVettingProviderOrStr` | `twilio_sdk/models/enums/brand_vetting_enum_vetting_provider.py` |
| `MessagingV1BrandRegistrationsBrandVetting` | `twilio_sdk/models/messaging_v1_brand_registrations_brand_vetting.py` |

### client.messaging_v1_brand_vetting.fetch_brand_vetting

- **Route**: `GET /v1/a2p/BrandRegistrations/{BrandSid}/Vettings/{BrandVettingSid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def fetch_brand_vetting(brand_sid: str, brand_vetting_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `brand_sid`, `brand_vetting_sid`
- **Params**: `brand_sid` — path `BrandSid` · `brand_vetting_sid` — path `BrandVettingSid`
- **Returns (parsed)**: `MessagingV1BrandRegistrationsBrandVetting`
- **Returns (raw)**: `ApiResult[MessagingV1BrandRegistrationsBrandVetting, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1BrandRegistrationsBrandVetting` | `twilio_sdk/models/messaging_v1_brand_registrations_brand_vetting.py` |

### client.messaging_v1_brand_vetting.list_brand_vetting

- **Route**: `GET /v1/a2p/BrandRegistrations/{BrandSid}/Vettings`
- **Auth**: `account_sid_auth_token`
- **Server**: `default1`
- **Signature**: `def list_brand_vetting(brand_sid: str, *, vetting_provider: BrandVettingEnumVettingProviderOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `brand_sid`
- **Params**: `brand_sid` — path `BrandSid` · `vetting_provider` — query `VettingProvider`
- **Returns (parsed)**: `ListBrandVettingResponse`
- **Returns (raw)**: `ApiResult[ListBrandVettingResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BrandVettingEnumVettingProviderOrStr` | `twilio_sdk/models/enums/brand_vetting_enum_vetting_provider.py` |
| `ListBrandVettingResponse` | `twilio_sdk/models/list_brand_vetting_response.py` |

