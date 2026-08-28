<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV2BundleCloneApi — operations

Accessor: `client.numbers_v2_bundle_clone_api` · Source: `twilio/apis/numbers_v2_bundle_clone_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.numbers_v2_bundle_clone_api.create_bundle_clone

- **Route**: `POST /v2/RegulatoryCompliance/Bundles/{BundleSid}/Clones`
- **Server**: `default5`
- **Signature**: `def create_bundle_clone(bundle_sid: str, target_account_sid: str, *, move_to_draft: bool | None = None, friendly_name: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `bundle_sid`, `target_account_sid`
- **Params**: `bundle_sid` — path `BundleSid` · `target_account_sid` — form field `TargetAccountSid` · `move_to_draft` — form field `MoveToDraft` · `friendly_name` — form field `FriendlyName`
- **Returns (parsed)**: `NumbersV2BundleClone`
- **Returns (raw)**: `ApiResult[NumbersV2BundleClone, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV2BundleClone` | `twilio/models/numbers_v2_bundle_clone.py` |

