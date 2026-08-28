<!-- Generated file — do not edit; regenerated with the SDK. -->

# InsightsV1GetAccountReport — operations

Accessor: `client.insights_v1_get_account_report` · Source: `twilio/apis/insights_v1_get_account_report.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.insights_v1_get_account_report.fetch_account_report

- **Route**: `GET /v2/Voice/Reports/{reportId}`
- **Server**: `default14`
- **Signature**: `def fetch_account_report(report_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `report_id`
- **Params**: `report_id` — path `reportId`
- **Returns (parsed)**: `InsightsV2AccountReport`
- **Returns (raw)**: `ApiResult[InsightsV2AccountReport, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InsightsV2AccountReport` | `twilio/models/insights_v2_account_report.py` |

