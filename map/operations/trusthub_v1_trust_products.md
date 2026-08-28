<!-- Generated file — do not edit; regenerated with the SDK. -->

# TrusthubV1TrustProducts — operations

Accessor: `client.trusthub_v1_trust_products` · Source: `twilio_sdk/apis/trusthub_v1_trust_products.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.trusthub_v1_trust_products.create_trust_product

- **Route**: `POST /v1/TrustProducts`
- **Server**: `default9`
- **Signature**: `def create_trust_product(friendly_name: str, email: str, policy_sid: str, *, status_callback: AnyUrl | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `friendly_name`, `email`, `policy_sid`
- **Params**: `friendly_name` — form field `FriendlyName` · `email` — form field `Email` · `policy_sid` — form field `PolicySid` · `status_callback` — form field `StatusCallback`
- **Returns (parsed)**: `TrusthubV1TrustProduct`
- **Returns (raw)**: `ApiResult[TrusthubV1TrustProduct, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrusthubV1TrustProduct` | `twilio_sdk/models/trusthub_v1_trust_product.py` |

### client.trusthub_v1_trust_products.delete_trust_product

- **Route**: `DELETE /v1/TrustProducts/{Sid}`
- **Server**: `default9`
- **Signature**: `def delete_trust_product(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.trusthub_v1_trust_products.fetch_trust_product

- **Route**: `GET /v1/TrustProducts/{Sid}`
- **Server**: `default9`
- **Signature**: `def fetch_trust_product(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `TrusthubV1TrustProduct`
- **Returns (raw)**: `ApiResult[TrusthubV1TrustProduct, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrusthubV1TrustProduct` | `twilio_sdk/models/trusthub_v1_trust_product.py` |

### client.trusthub_v1_trust_products.list_trust_product

- **Route**: `GET /v1/TrustProducts`
- **Server**: `default9`
- **Signature**: `def list_trust_product(*, status: TrustProductEnumStatusOrStr | None = None, friendly_name: str | None = None, policy_sid: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `status` — query `Status` · `friendly_name` — query `FriendlyName` · `policy_sid` — query `PolicySid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListTrustProductResponse`
- **Returns (raw)**: `ApiResult[ListTrustProductResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrustProductEnumStatusOrStr` | `twilio_sdk/models/enums/trust_product_enum_status.py` |
| `ListTrustProductResponse` | `twilio_sdk/models/list_trust_product_response.py` |

### client.trusthub_v1_trust_products.update_trust_product

- **Route**: `POST /v1/TrustProducts/{Sid}`
- **Server**: `default9`
- **Signature**: `def update_trust_product(sid: str, *, status: TrustProductEnumStatusOrStr | None = None, status_callback: AnyUrl | None = None, friendly_name: str | None = None, email: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `status` — form field `Status` · `status_callback` — form field `StatusCallback` · `friendly_name` — form field `FriendlyName` · `email` — form field `Email`
- **Returns (parsed)**: `TrusthubV1TrustProduct`
- **Returns (raw)**: `ApiResult[TrusthubV1TrustProduct, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrustProductEnumStatusOrStr` | `twilio_sdk/models/enums/trust_product_enum_status.py` |
| `TrusthubV1TrustProduct` | `twilio_sdk/models/trusthub_v1_trust_product.py` |

