<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV1InsightsQuestionnairesQuestionApi — operations

Accessor: `client.flex_v1_insights_questionnaires_question_api` · Source: `twilio_sdk/apis/flex_v1_insights_questionnaires_question_api.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.flex_v1_insights_questionnaires_question_api.create_insights_questionnaires_question

- **Route**: `POST /v1/Insights/QualityManagement/Questions`
- **Server**: `default13`
- **Signature**: `def create_insights_questionnaires_question(category_sid: str, question: str, answer_set_id: str, allow_na: bool, *, authorization: str | None = None, description: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `category_sid`, `question`, `answer_set_id`, `allow_na`
- **Params**: `authorization` — header `Authorization` · `category_sid` — form field `CategorySid` · `question` — form field `Question` · `answer_set_id` — form field `AnswerSetId` · `allow_na` — form field `AllowNa` · `description` — form field `Description`
- **Returns (parsed)**: `FlexV1InsightsQuestionnairesQuestion`
- **Returns (raw)**: `ApiResult[FlexV1InsightsQuestionnairesQuestion, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1InsightsQuestionnairesQuestion` | `twilio_sdk/models/flex_v1_insights_questionnaires_question.py` |

### client.flex_v1_insights_questionnaires_question_api.delete_insights_questionnaires_question

- **Route**: `DELETE /v1/Insights/QualityManagement/Questions/{QuestionSid}`
- **Server**: `default13`
- **Signature**: `def delete_insights_questionnaires_question(question_sid: str, *, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `question_sid`
- **Params**: `question_sid` — path `QuestionSid` · `authorization` — header `Authorization`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.flex_v1_insights_questionnaires_question_api.list_insights_questionnaires_question

- **Route**: `GET /v1/Insights/QualityManagement/Questions`
- **Server**: `default13`
- **Signature**: `def list_insights_questionnaires_question(*, category_sid: list[str] | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `category_sid` — query `CategorySid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken` · `authorization` — header `Authorization`
- **Returns (parsed)**: `ListInsightsQuestionnairesQuestionResponse`
- **Returns (raw)**: `ApiResult[ListInsightsQuestionnairesQuestionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListInsightsQuestionnairesQuestionResponse` | `twilio_sdk/models/list_insights_questionnaires_question_response.py` |

### client.flex_v1_insights_questionnaires_question_api.update_insights_questionnaires_question

- **Route**: `POST /v1/Insights/QualityManagement/Questions/{QuestionSid}`
- **Server**: `default13`
- **Signature**: `def update_insights_questionnaires_question(question_sid: str, allow_na: bool, *, authorization: str | None = None, category_sid: str | None = None, question: str | None = None, description: str | None = None, answer_set_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `question_sid`, `allow_na`
- **Params**: `question_sid` — path `QuestionSid` · `authorization` — header `Authorization` · `allow_na` — form field `AllowNa` · `category_sid` — form field `CategorySid` · `question` — form field `Question` · `description` — form field `Description` · `answer_set_id` — form field `AnswerSetId`
- **Returns (parsed)**: `FlexV1InsightsQuestionnairesQuestion`
- **Returns (raw)**: `ApiResult[FlexV1InsightsQuestionnairesQuestion, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1InsightsQuestionnairesQuestion` | `twilio_sdk/models/flex_v1_insights_questionnaires_question.py` |

