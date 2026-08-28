<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV1InsightsQuestionnairesCategoryApi — operations

Accessor: `client.flex_v1_insights_questionnaires_category_api` · Source: `twilio_sdk/apis/flex_v1_insights_questionnaires_category_api.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.flex_v1_insights_questionnaires_category_api.create_insights_questionnaires_category

- **Route**: `POST /v1/Insights/QualityManagement/Categories`
- **Server**: `default13`
- **Signature**: `def create_insights_questionnaires_category(name: str, *, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `name`
- **Params**: `authorization` — header `Authorization` · `name` — form field `Name`
- **Returns (parsed)**: `FlexV1InsightsQuestionnairesCategory`
- **Returns (raw)**: `ApiResult[FlexV1InsightsQuestionnairesCategory, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1InsightsQuestionnairesCategory` | `twilio_sdk/models/flex_v1_insights_questionnaires_category.py` |

### client.flex_v1_insights_questionnaires_category_api.delete_insights_questionnaires_category

- **Route**: `DELETE /v1/Insights/QualityManagement/Categories/{CategorySid}`
- **Server**: `default13`
- **Signature**: `def delete_insights_questionnaires_category(category_sid: str, *, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `category_sid`
- **Params**: `category_sid` — path `CategorySid` · `authorization` — header `Authorization`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.flex_v1_insights_questionnaires_category_api.list_insights_questionnaires_category

- **Route**: `GET /v1/Insights/QualityManagement/Categories`
- **Server**: `default13`
- **Signature**: `def list_insights_questionnaires_category(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken` · `authorization` — header `Authorization`
- **Returns (parsed)**: `ListInsightsQuestionnairesCategoryResponse`
- **Returns (raw)**: `ApiResult[ListInsightsQuestionnairesCategoryResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListInsightsQuestionnairesCategoryResponse` | `twilio_sdk/models/list_insights_questionnaires_category_response.py` |

### client.flex_v1_insights_questionnaires_category_api.update_insights_questionnaires_category

- **Route**: `POST /v1/Insights/QualityManagement/Categories/{CategorySid}`
- **Server**: `default13`
- **Signature**: `def update_insights_questionnaires_category(category_sid: str, name: str, *, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `category_sid`, `name`
- **Params**: `category_sid` — path `CategorySid` · `authorization` — header `Authorization` · `name` — form field `Name`
- **Returns (parsed)**: `FlexV1InsightsQuestionnairesCategory`
- **Returns (raw)**: `ApiResult[FlexV1InsightsQuestionnairesCategory, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1InsightsQuestionnairesCategory` | `twilio_sdk/models/flex_v1_insights_questionnaires_category.py` |

