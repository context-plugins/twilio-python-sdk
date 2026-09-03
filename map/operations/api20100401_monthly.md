<!-- Generated file — do not edit; regenerated with the SDK. -->

# Api20100401Monthly — operations

Accessor: `client.api20100401_monthly` · Source: `twilio_sdk/apis/api20100401_monthly.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.api20100401_monthly.list_usage_record_monthly

- **Route**: `GET /2010-04-01/Accounts/{AccountSid}/Usage/Records/Monthly.json`
- **Auth**: `account_sid_auth_token`
- **Server**: `default`
- **Signature**: `def list_usage_record_monthly(account_sid: str, *, category: str | None = None, start_date: Date | None = None, end_date: Date | None = None, include_subaccounts: bool | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_sid`
- **Params**: `account_sid` — path `AccountSid` · `category` — query `Category` · `start_date` — query `StartDate` · `end_date` — query `EndDate` · `include_subaccounts` — query `IncludeSubaccounts` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListUsageRecordMonthlyResponse`
- **Returns (raw)**: `ApiResult[ListUsageRecordMonthlyResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListUsageRecordMonthlyResponse` | `twilio_sdk/models/list_usage_record_monthly_response.py` |

