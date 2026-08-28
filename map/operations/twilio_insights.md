<!-- Generated file — do not edit; regenerated with the SDK. -->

# TwilioInsights — operations

Accessor: `client.twilio_insights` · Source: `twilio/apis/twilio_insights.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.twilio_insights.create_query_results

- **Route**: `POST /v3/InsightsDomains/Conversations/Query`
- **Server**: `default14`
- **Signature**: `def create_query_results(body: InsightsQueryRequest | InsightsQueryRequestDict, *, page_size: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `page_size` — query `pageSize` · `body` — JSON body
- **Returns (parsed)**: `InsightsQueryResponse`
- **Returns (raw)**: `ApiResult[InsightsQueryResponse, CreateQueryResultsErrorBody]`
- **Error**: `CreateQueryResultsErrorBody` — **Case A (typed)**
- **Error arms**: `V3InsightsDomainsConversationsQuery400Error1` [400] · `V3InsightsDomainsConversationsQuery429Error1` [429] · `V3InsightsDomainsConversationsQuery500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `InsightsQueryRequest` | `twilio/models/insights_query_request.py` |
| `InsightsQueryRequestDict` | `twilio/models/insights_query_request.py` |
| `InsightsQueryResponse` | `twilio/models/insights_query_response.py` |
| `CreateQueryResultsErrorBody` | `twilio/errors/create_query_results_error.py` |
| `V3InsightsDomainsConversationsQuery400Error1` | `twilio/models/v3_insights_domains_conversations_query400_error1.py` |
| `V3InsightsDomainsConversationsQuery429Error1` | `twilio/models/v3_insights_domains_conversations_query429_error1.py` |
| `V3InsightsDomainsConversationsQuery500Error1` | `twilio/models/v3_insights_domains_conversations_query500_error1.py` |

### client.twilio_insights.fetch_metadata

- **Route**: `GET /v3/InsightsDomains/Conversations/Metadata`
- **Server**: `default14`
- **Signature**: `def fetch_metadata(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `InsightsMetadataResponse`
- **Returns (raw)**: `ApiResult[InsightsMetadataResponse, FetchMetadataErrorBody]`
- **Error**: `FetchMetadataErrorBody` — **Case A (typed)**
- **Error arms**: `V3InsightsDomainsConversationsMetadata400Error1` [400] · `V3InsightsDomainsConversationsMetadata429Error1` [429] · `V3InsightsDomainsConversationsMetadata500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `InsightsMetadataResponse` | `twilio/models/insights_metadata_response.py` |
| `FetchMetadataErrorBody` | `twilio/errors/fetch_metadata_error.py` |
| `V3InsightsDomainsConversationsMetadata400Error1` | `twilio/models/v3_insights_domains_conversations_metadata400_error1.py` |
| `V3InsightsDomainsConversationsMetadata429Error1` | `twilio/models/v3_insights_domains_conversations_metadata429_error1.py` |
| `V3InsightsDomainsConversationsMetadata500Error1` | `twilio/models/v3_insights_domains_conversations_metadata500_error1.py` |

### client.twilio_insights.fetch_query_results

- **Route**: `GET /v3/InsightsDomains/Conversations/Query`
- **Server**: `default14`
- **Signature**: `def fetch_query_results(page_token: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `page_token`
- **Params**: `page_token` — query `pageToken`
- **Returns (parsed)**: `InsightsQueryResponse`
- **Returns (raw)**: `ApiResult[InsightsQueryResponse, FetchQueryResultsErrorBody]`
- **Error**: `FetchQueryResultsErrorBody` — **Case A (typed)**
- **Error arms**: `V3InsightsDomainsConversationsQuery400Error1` [400] · `V3InsightsDomainsConversationsQuery429Error1` [429] · `V3InsightsDomainsConversationsQuery500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `InsightsQueryResponse` | `twilio/models/insights_query_response.py` |
| `FetchQueryResultsErrorBody` | `twilio/errors/fetch_query_results_error.py` |
| `V3InsightsDomainsConversationsQuery400Error1` | `twilio/models/v3_insights_domains_conversations_query400_error1.py` |
| `V3InsightsDomainsConversationsQuery429Error1` | `twilio/models/v3_insights_domains_conversations_query429_error1.py` |
| `V3InsightsDomainsConversationsQuery500Error1` | `twilio/models/v3_insights_domains_conversations_query500_error1.py` |

