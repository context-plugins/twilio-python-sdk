<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV1InsightsQuestionnairesApi — operations

Accessor: `client.flex_v1_insights_questionnaires_api` · Source: `twilio_sdk/apis/flex_v1_insights_questionnaires_api.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.flex_v1_insights_questionnaires_api.create_insights_questionnaires

- **Route**: `POST /v1/Insights/QualityManagement/Questionnaires`
- **Auth**: `account_sid_auth_token`
- **Server**: `default13`
- **Signature**: `def create_insights_questionnaires(name: str, *, authorization: str | None = None, description: str | None = None, active: bool | None = None, question_sids: list[str] | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `name`
- **Params**: `authorization` — header `Authorization` · `name` — form field `Name` · `description` — form field `Description` · `active` — form field `Active` · `question_sids` — form field `QuestionSids`
- **Returns (parsed)**: `FlexV1InsightsQuestionnaires`
- **Returns (raw)**: `ApiResult[FlexV1InsightsQuestionnaires, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1InsightsQuestionnaires` | `twilio_sdk/models/flex_v1_insights_questionnaires.py` |

### client.flex_v1_insights_questionnaires_api.delete_insights_questionnaires

- **Route**: `DELETE /v1/Insights/QualityManagement/Questionnaires/{QuestionnaireSid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default13`
- **Signature**: `def delete_insights_questionnaires(questionnaire_sid: str, *, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `questionnaire_sid`
- **Params**: `questionnaire_sid` — path `QuestionnaireSid` · `authorization` — header `Authorization`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.flex_v1_insights_questionnaires_api.fetch_insights_questionnaires

- **Route**: `GET /v1/Insights/QualityManagement/Questionnaires/{QuestionnaireSid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default13`
- **Signature**: `def fetch_insights_questionnaires(questionnaire_sid: str, *, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `questionnaire_sid`
- **Params**: `questionnaire_sid` — path `QuestionnaireSid` · `authorization` — header `Authorization`
- **Returns (parsed)**: `FlexV1InsightsQuestionnaires`
- **Returns (raw)**: `ApiResult[FlexV1InsightsQuestionnaires, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1InsightsQuestionnaires` | `twilio_sdk/models/flex_v1_insights_questionnaires.py` |

### client.flex_v1_insights_questionnaires_api.list_insights_questionnaires

- **Route**: `GET /v1/Insights/QualityManagement/Questionnaires`
- **Auth**: `account_sid_auth_token`
- **Server**: `default13`
- **Signature**: `def list_insights_questionnaires(*, include_inactive: bool | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `include_inactive` — query `IncludeInactive` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken` · `authorization` — header `Authorization`
- **Returns (parsed)**: `ListInsightsQuestionnairesResponse`
- **Returns (raw)**: `ApiResult[ListInsightsQuestionnairesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListInsightsQuestionnairesResponse` | `twilio_sdk/models/list_insights_questionnaires_response.py` |

### client.flex_v1_insights_questionnaires_api.update_insights_questionnaires

- **Route**: `POST /v1/Insights/QualityManagement/Questionnaires/{QuestionnaireSid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default13`
- **Signature**: `def update_insights_questionnaires(questionnaire_sid: str, active: bool, *, authorization: str | None = None, name: str | None = None, description: str | None = None, question_sids: list[str] | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `questionnaire_sid`, `active`
- **Params**: `questionnaire_sid` — path `QuestionnaireSid` · `authorization` — header `Authorization` · `active` — form field `Active` · `name` — form field `Name` · `description` — form field `Description` · `question_sids` — form field `QuestionSids`
- **Returns (parsed)**: `FlexV1InsightsQuestionnaires`
- **Returns (raw)**: `ApiResult[FlexV1InsightsQuestionnaires, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1InsightsQuestionnaires` | `twilio_sdk/models/flex_v1_insights_questionnaires.py` |

