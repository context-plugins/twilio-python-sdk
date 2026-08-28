<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV1InsightsConversationsApi — operations

Accessor: `client.flex_v1_insights_conversations_api` · Source: `twilio_sdk/apis/flex_v1_insights_conversations_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.flex_v1_insights_conversations_api.list_insights_conversations

- **Route**: `GET /v1/Insights/Conversations`
- **Server**: `default13`
- **Signature**: `def list_insights_conversations(*, segment_id: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `segment_id` — query `SegmentId` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken` · `authorization` — header `Authorization`
- **Returns (parsed)**: `ListInsightsConversationsResponse`
- **Returns (raw)**: `ApiResult[ListInsightsConversationsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListInsightsConversationsResponse` | `twilio_sdk/models/list_insights_conversations_response.py` |

