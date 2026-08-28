<!-- Generated file — do not edit; regenerated with the SDK. -->

# InsightsV1GetInboundPhoneNumbersReport — operations

Accessor: `client.insights_v1_get_inbound_phone_numbers_report` · Source: `twilio/apis/insights_v1_get_inbound_phone_numbers_report.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.insights_v1_get_inbound_phone_numbers_report.list_inbound_phone_numbers_report

- **Route**: `GET /v2/Voice/Reports/PhoneNumbers/Inbound/{reportId}`
- **Server**: `default14`
- **Signature**: `def list_inbound_phone_numbers_report(report_id: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `report_id`
- **Params**: `report_id` — path `reportId` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListInboundPhoneNumbersReports`
- **Returns (raw)**: `ApiResult[ListInboundPhoneNumbersReports, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListInboundPhoneNumbersReports` | `twilio/models/list_inbound_phone_numbers_reports.py` |

