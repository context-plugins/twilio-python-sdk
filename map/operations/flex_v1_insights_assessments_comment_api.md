<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV1InsightsAssessmentsCommentApi — operations

Accessor: `client.flex_v1_insights_assessments_comment_api` · Source: `twilio_sdk/apis/flex_v1_insights_assessments_comment_api.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.flex_v1_insights_assessments_comment_api.create_insights_assessments_comment

- **Route**: `POST /v1/Insights/QualityManagement/Assessments/Comments`
- **Server**: `default13`
- **Signature**: `def create_insights_assessments_comment(category_id: str, category_name: str, comment: str, segment_id: str, agent_id: str, offset: float, *, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `category_id`, `category_name`, `comment`, `segment_id`, `agent_id`, `offset`
- **Params**: `authorization` — header `Authorization` · `category_id` — form field `CategoryId` · `category_name` — form field `CategoryName` · `comment` — form field `Comment` · `segment_id` — form field `SegmentId` · `agent_id` — form field `AgentId` · `offset` — form field `Offset`
- **Returns (parsed)**: `FlexV1InsightsAssessmentsComment`
- **Returns (raw)**: `ApiResult[FlexV1InsightsAssessmentsComment, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1InsightsAssessmentsComment` | `twilio_sdk/models/flex_v1_insights_assessments_comment.py` |

### client.flex_v1_insights_assessments_comment_api.list_insights_assessments_comment

- **Route**: `GET /v1/Insights/QualityManagement/Assessments/Comments`
- **Server**: `default13`
- **Signature**: `def list_insights_assessments_comment(*, segment_id: str | None = None, agent_id: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `segment_id` — query `SegmentId` · `agent_id` — query `AgentId` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken` · `authorization` — header `Authorization`
- **Returns (parsed)**: `ListInsightsAssessmentsCommentResponse`
- **Returns (raw)**: `ApiResult[ListInsightsAssessmentsCommentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListInsightsAssessmentsCommentResponse` | `twilio_sdk/models/list_insights_assessments_comment_response.py` |

