<!-- Generated file — do not edit; regenerated with the SDK. -->

# Contentv1ContentAndApprovalsApi — operations

Accessor: `client.contentv1_content_and_approvals_api` · Source: `twilio/apis/contentv1_content_and_approvals_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.contentv1_content_and_approvals_api.list_content_and_approvals

- **Route**: `GET /v1/ContentAndApprovals`
- **Server**: `default2`
- **Signature**: `def list_content_and_approvals(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListContentAndApprovalsResponse`
- **Returns (raw)**: `ApiResult[ListContentAndApprovalsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListContentAndApprovalsResponse` | `twilio/models/list_content_and_approvals_response.py` |

