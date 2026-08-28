<!-- Generated file — do not edit; regenerated with the SDK. -->

# InsightsV1CreateOutboundPhoneNumbersReport — operations

Accessor: `client.insights_v1_create_outbound_phone_numbers_report` · Source: `twilio/apis/insights_v1_create_outbound_phone_numbers_report.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.insights_v1_create_outbound_phone_numbers_report.create_outbound_phone_numbers_report

- **Route**: `POST /v2/Voice/Reports/PhoneNumbers/Outbound`
- **Server**: `default14`
- **Signature**: `def create_outbound_phone_numbers_report(*, body: InsightsV2CreatePhoneNumbersReportRequest | InsightsV2CreatePhoneNumbersReportRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `InsightsV2CreateReportResponse`
- **Returns (raw)**: `ApiResult[InsightsV2CreateReportResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InsightsV2CreatePhoneNumbersReportRequest` | `twilio/models/insights_v2_create_phone_numbers_report_request.py` |
| `InsightsV2CreatePhoneNumbersReportRequestDict` | `twilio/models/insights_v2_create_phone_numbers_report_request.py` |
| `InsightsV2CreateReportResponse` | `twilio/models/insights_v2_create_report_response.py` |

