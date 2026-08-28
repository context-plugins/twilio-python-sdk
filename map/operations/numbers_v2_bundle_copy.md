<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV2BundleCopy — operations

Accessor: `client.numbers_v2_bundle_copy` · Source: `twilio_sdk/apis/numbers_v2_bundle_copy.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.numbers_v2_bundle_copy.create_bundle_copy

- **Route**: `POST /v2/RegulatoryCompliance/Bundles/{BundleSid}/Copies`
- **Server**: `default5`
- **Signature**: `def create_bundle_copy(bundle_sid: str, *, friendly_name: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `bundle_sid`
- **Params**: `bundle_sid` — path `BundleSid` · `friendly_name` — form field `FriendlyName`
- **Returns (parsed)**: `NumbersV2RegulatoryComplianceBundleBundleCopy`
- **Returns (raw)**: `ApiResult[NumbersV2RegulatoryComplianceBundleBundleCopy, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV2RegulatoryComplianceBundleBundleCopy` | `twilio_sdk/models/numbers_v2_regulatory_compliance_bundle_bundle_copy.py` |

### client.numbers_v2_bundle_copy.list_bundle_copy

- **Route**: `GET /v2/RegulatoryCompliance/Bundles/{BundleSid}/Copies`
- **Server**: `default5`
- **Signature**: `def list_bundle_copy(bundle_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `bundle_sid`
- **Params**: `bundle_sid` — path `BundleSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListBundleCopyResponse`
- **Returns (raw)**: `ApiResult[ListBundleCopyResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListBundleCopyResponse` | `twilio_sdk/models/list_bundle_copy_response.py` |

