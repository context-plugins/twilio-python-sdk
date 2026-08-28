<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV1Assessments — operations

Accessor: `client.flex_v1_assessments` · Source: `twilio/apis/flex_v1_assessments.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.flex_v1_assessments.create_insights_assessments

- **Route**: `POST /v1/Insights/QualityManagement/Assessments`
- **Server**: `default13`
- **Signature**: `def create_insights_assessments(category_sid: str, category_name: str, segment_id: str, agent_id: str, offset: float, metric_id: str, metric_name: str, answer_text: str, answer_id: str, questionnaire_sid: str, *, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `category_sid`, `category_name`, `segment_id`, `agent_id`, `offset`, `metric_id`, `metric_name`, `answer_text`, `answer_id`, `questionnaire_sid`
- **Params**: `authorization` — header `Authorization` · `category_sid` — form field `CategorySid` · `category_name` — form field `CategoryName` · `segment_id` — form field `SegmentId` · `agent_id` — form field `AgentId` · `offset` — form field `Offset` · `metric_id` — form field `MetricId` · `metric_name` — form field `MetricName` · `answer_text` — form field `AnswerText` · `answer_id` — form field `AnswerId` · `questionnaire_sid` — form field `QuestionnaireSid`
- **Returns (parsed)**: `FlexV1InsightsAssessments`
- **Returns (raw)**: `ApiResult[FlexV1InsightsAssessments, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1InsightsAssessments` | `twilio/models/flex_v1_insights_assessments.py` |

### client.flex_v1_assessments.list_insights_assessments

- **Route**: `GET /v1/Insights/QualityManagement/Assessments`
- **Server**: `default13`
- **Signature**: `def list_insights_assessments(*, segment_id: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `segment_id` — query `SegmentId` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken` · `authorization` — header `Authorization`
- **Returns (parsed)**: `ListInsightsAssessmentsResponse`
- **Returns (raw)**: `ApiResult[ListInsightsAssessmentsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListInsightsAssessmentsResponse` | `twilio/models/list_insights_assessments_response.py` |

### client.flex_v1_assessments.update_insights_assessments

- **Route**: `POST /v1/Insights/QualityManagement/Assessments/{AssessmentSid}`
- **Server**: `default13`
- **Signature**: `def update_insights_assessments(assessment_sid: str, offset: float, answer_text: str, answer_id: str, *, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `assessment_sid`, `offset`, `answer_text`, `answer_id`
- **Params**: `assessment_sid` — path `AssessmentSid` · `authorization` — header `Authorization` · `offset` — form field `Offset` · `answer_text` — form field `AnswerText` · `answer_id` — form field `AnswerId`
- **Returns (parsed)**: `FlexV1InsightsAssessments`
- **Returns (raw)**: `ApiResult[FlexV1InsightsAssessments, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1InsightsAssessments` | `twilio/models/flex_v1_insights_assessments.py` |

