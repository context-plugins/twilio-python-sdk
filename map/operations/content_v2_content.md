<!-- Generated file — do not edit; regenerated with the SDK. -->

# ContentV2Content — operations

Accessor: `client.content_v2_content` · Source: `twilio_sdk/apis/content_v2_content.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.content_v2_content.list_content2

- **Route**: `GET /v2/Content`
- **Server**: `default2`
- **Signature**: `def list_content2(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, sort_by_date: str | None = None, sort_by_content_name: str | None = None, date_created_after: RFC3339DateTime | None = None, date_created_before: RFC3339DateTime | None = None, content_name: str | None = None, content: str | None = None, language: list[str] | None = None, content_type: list[str] | None = None, channel_eligibility: list[str] | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken` · `sort_by_date` — query `SortByDate` · `sort_by_content_name` — query `SortByContentName` · `date_created_after` — query `DateCreatedAfter` · `date_created_before` — query `DateCreatedBefore` · `content_name` — query `ContentName` · `content` — query `Content` · `language` — query `Language` · `content_type` — query `ContentType` · `channel_eligibility` — query `ChannelEligibility`
- **Returns (parsed)**: `ListContentResponse`
- **Returns (raw)**: `ApiResult[ListContentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListContentResponse` | `twilio_sdk/models/list_content_response.py` |

