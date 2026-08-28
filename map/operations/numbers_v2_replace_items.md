<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV2ReplaceItems — operations

Accessor: `client.numbers_v2_replace_items` · Source: `twilio_sdk/apis/numbers_v2_replace_items.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.numbers_v2_replace_items.create_replace_items

- **Route**: `POST /v2/RegulatoryCompliance/Bundles/{BundleSid}/ReplaceItems`
- **Server**: `default5`
- **Signature**: `def create_replace_items(bundle_sid: str, from_bundle_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `bundle_sid`, `from_bundle_sid`
- **Params**: `bundle_sid` — path `BundleSid` · `from_bundle_sid` — form field `FromBundleSid`
- **Returns (parsed)**: `NumbersV2RegulatoryComplianceBundleReplaceItems`
- **Returns (raw)**: `ApiResult[NumbersV2RegulatoryComplianceBundleReplaceItems, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV2RegulatoryComplianceBundleReplaceItems` | `twilio_sdk/models/numbers_v2_regulatory_compliance_bundle_replace_items.py` |

