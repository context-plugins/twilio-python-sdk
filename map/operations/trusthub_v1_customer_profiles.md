<!-- Generated file — do not edit; regenerated with the SDK. -->

# TrusthubV1CustomerProfiles — operations

Accessor: `client.trusthub_v1_customer_profiles` · Source: `twilio/apis/trusthub_v1_customer_profiles.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.trusthub_v1_customer_profiles.create_customer_profile

- **Route**: `POST /v1/CustomerProfiles`
- **Server**: `default9`
- **Signature**: `def create_customer_profile(friendly_name: str, email: str, policy_sid: str, *, status_callback: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `friendly_name`, `email`, `policy_sid`
- **Params**: `friendly_name` — form field `FriendlyName` · `email` — form field `Email` · `policy_sid` — form field `PolicySid` · `status_callback` — form field `StatusCallback`
- **Returns (parsed)**: `TrusthubV1CustomerProfile`
- **Returns (raw)**: `ApiResult[TrusthubV1CustomerProfile, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrusthubV1CustomerProfile` | `twilio/models/trusthub_v1_customer_profile.py` |

### client.trusthub_v1_customer_profiles.delete_customer_profile

- **Route**: `DELETE /v1/CustomerProfiles/{Sid}`
- **Server**: `default9`
- **Signature**: `def delete_customer_profile(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.trusthub_v1_customer_profiles.fetch_customer_profile

- **Route**: `GET /v1/CustomerProfiles/{Sid}`
- **Server**: `default9`
- **Signature**: `def fetch_customer_profile(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `TrusthubV1CustomerProfile`
- **Returns (raw)**: `ApiResult[TrusthubV1CustomerProfile, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrusthubV1CustomerProfile` | `twilio/models/trusthub_v1_customer_profile.py` |

### client.trusthub_v1_customer_profiles.list_customer_profile

- **Route**: `GET /v1/CustomerProfiles`
- **Server**: `default9`
- **Signature**: `def list_customer_profile(*, status: CustomerProfileEnumStatusOrStr | None = None, friendly_name: str | None = None, policy_sid: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `status` — query `Status` · `friendly_name` — query `FriendlyName` · `policy_sid` — query `PolicySid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListCustomerProfileResponse`
- **Returns (raw)**: `ApiResult[ListCustomerProfileResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CustomerProfileEnumStatusOrStr` | `twilio/models/enums/customer_profile_enum_status.py` |
| `ListCustomerProfileResponse` | `twilio/models/list_customer_profile_response.py` |

### client.trusthub_v1_customer_profiles.update_customer_profile

- **Route**: `POST /v1/CustomerProfiles/{Sid}`
- **Server**: `default9`
- **Signature**: `def update_customer_profile(sid: str, *, status: CustomerProfileEnumStatusOrStr | None = None, status_callback: str | None = None, friendly_name: str | None = None, email: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `status` — form field `Status` · `status_callback` — form field `StatusCallback` · `friendly_name` — form field `FriendlyName` · `email` — form field `Email`
- **Returns (parsed)**: `TrusthubV1CustomerProfile`
- **Returns (raw)**: `ApiResult[TrusthubV1CustomerProfile, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CustomerProfileEnumStatusOrStr` | `twilio/models/enums/customer_profile_enum_status.py` |
| `TrusthubV1CustomerProfile` | `twilio/models/trusthub_v1_customer_profile.py` |

