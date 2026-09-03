<!-- Generated file — do not edit; regenerated with the SDK. -->

# Contentv1ApprovalFetch — operations

Accessor: `client.contentv1_approval_fetch` · Source: `twilio_sdk/apis/contentv1_approval_fetch.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.contentv1_approval_fetch.fetch_approval_fetch

- **Route**: `GET /v1/Content/{Sid}/ApprovalRequests`
- **Auth**: `account_sid_auth_token`
- **Server**: `default2`
- **Signature**: `def fetch_approval_fetch(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `ContentV1ContentApprovalFetch`
- **Returns (raw)**: `ApiResult[ContentV1ContentApprovalFetch, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentV1ContentApprovalFetch` | `twilio_sdk/models/content_v1_content_approval_fetch.py` |

