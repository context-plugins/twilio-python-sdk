<!-- Generated file — do not edit; regenerated with the SDK. -->

# MessagingV1BrandRegistrationOtp — operations

Accessor: `client.messaging_v1_brand_registration_otp` · Source: `twilio_sdk/apis/messaging_v1_brand_registration_otp.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.messaging_v1_brand_registration_otp.create_brand_registration_otp

- **Route**: `POST /v1/a2p/BrandRegistrations/{BrandRegistrationSid}/SmsOtp`
- **Server**: `default1`
- **Signature**: `def create_brand_registration_otp(brand_registration_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `brand_registration_sid`
- **Params**: `brand_registration_sid` — path `BrandRegistrationSid`
- **Returns (parsed)**: `MessagingV1BrandRegistrationsBrandRegistrationOtp`
- **Returns (raw)**: `ApiResult[MessagingV1BrandRegistrationsBrandRegistrationOtp, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MessagingV1BrandRegistrationsBrandRegistrationOtp` | `twilio_sdk/models/messaging_v1_brand_registrations_brand_registration_otp.py` |

