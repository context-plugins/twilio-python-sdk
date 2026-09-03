<!-- Generated file — do not edit; regenerated with the SDK. -->

# Contentv1ApprovalCreate — operations

Accessor: `client.contentv1_approval_create` · Source: `twilio_sdk/apis/contentv1_approval_create.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.contentv1_approval_create.create_approval_create

- **Route**: `POST /v1/Content/{ContentSid}/ApprovalRequests/whatsapp`
- **Auth**: `account_sid_auth_token`
- **Server**: `default2`
- **Signature**: `def create_approval_create(content_sid: str, body: ContentApprovalRequest | ContentApprovalRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_sid`, `body`
- **Params**: `content_sid` — path `ContentSid` · `body` — JSON body
- **Returns (parsed)**: `ContentV1ContentApprovalCreate`
- **Returns (raw)**: `ApiResult[ContentV1ContentApprovalCreate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentApprovalRequest` | `twilio_sdk/models/content_approval_request.py` |
| `ContentApprovalRequestDict` | `twilio_sdk/models/content_approval_request.py` |
| `ContentV1ContentApprovalCreate` | `twilio_sdk/models/content_v1_content_approval_create.py` |

