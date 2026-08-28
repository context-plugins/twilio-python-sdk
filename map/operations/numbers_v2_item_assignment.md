<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV2ItemAssignment — operations

Accessor: `client.numbers_v2_item_assignment` · Source: `twilio/apis/numbers_v2_item_assignment.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.numbers_v2_item_assignment.create_item_assignment

- **Route**: `POST /v2/RegulatoryCompliance/Bundles/{BundleSid}/ItemAssignments`
- **Server**: `default5`
- **Signature**: `def create_item_assignment(bundle_sid: str, object_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `bundle_sid`, `object_sid`
- **Params**: `bundle_sid` — path `BundleSid` · `object_sid` — form field `ObjectSid`
- **Returns (parsed)**: `NumbersV2RegulatoryComplianceBundleItemAssignment`
- **Returns (raw)**: `ApiResult[NumbersV2RegulatoryComplianceBundleItemAssignment, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV2RegulatoryComplianceBundleItemAssignment` | `twilio/models/numbers_v2_regulatory_compliance_bundle_item_assignment.py` |

### client.numbers_v2_item_assignment.delete_item_assignment

- **Route**: `DELETE /v2/RegulatoryCompliance/Bundles/{BundleSid}/ItemAssignments/{Sid}`
- **Server**: `default5`
- **Signature**: `def delete_item_assignment(bundle_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `bundle_sid`, `sid`
- **Params**: `bundle_sid` — path `BundleSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.numbers_v2_item_assignment.fetch_item_assignment

- **Route**: `GET /v2/RegulatoryCompliance/Bundles/{BundleSid}/ItemAssignments/{Sid}`
- **Server**: `default5`
- **Signature**: `def fetch_item_assignment(bundle_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `bundle_sid`, `sid`
- **Params**: `bundle_sid` — path `BundleSid` · `sid` — path `Sid`
- **Returns (parsed)**: `NumbersV2RegulatoryComplianceBundleItemAssignment`
- **Returns (raw)**: `ApiResult[NumbersV2RegulatoryComplianceBundleItemAssignment, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV2RegulatoryComplianceBundleItemAssignment` | `twilio/models/numbers_v2_regulatory_compliance_bundle_item_assignment.py` |

### client.numbers_v2_item_assignment.list_item_assignment

- **Route**: `GET /v2/RegulatoryCompliance/Bundles/{BundleSid}/ItemAssignments`
- **Server**: `default5`
- **Signature**: `def list_item_assignment(bundle_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `bundle_sid`
- **Params**: `bundle_sid` — path `BundleSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListItemAssignmentResponse`
- **Returns (raw)**: `ApiResult[ListItemAssignmentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListItemAssignmentResponse` | `twilio/models/list_item_assignment_response.py` |

