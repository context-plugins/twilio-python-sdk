<!-- Generated file — do not edit; regenerated with the SDK. -->

# InsightsV1CreateAccountReport — operations

Accessor: `client.insights_v1_create_account_report` · Source: `twilio_sdk/apis/insights_v1_create_account_report.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.insights_v1_create_account_report.create_account_report

- **Route**: `POST /v2/Voice/Reports`
- **Server**: `default14`
- **Signature**: `def create_account_report(*, body: InsightsV2CreateAccountReportRequest | InsightsV2CreateAccountReportRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `InsightsV2CreateReportResponse`
- **Returns (raw)**: `ApiResult[InsightsV2CreateReportResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InsightsV2CreateAccountReportRequest` | `twilio_sdk/models/insights_v2_create_account_report_request.py` |
| `InsightsV2CreateAccountReportRequestDict` | `twilio_sdk/models/insights_v2_create_account_report_request.py` |
| `InsightsV2CreateReportResponse` | `twilio_sdk/models/insights_v2_create_report_response.py` |

