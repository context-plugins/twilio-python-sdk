<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV2EndUserType — operations

Accessor: `client.numbers_v2_end_user_type` · Source: `twilio_sdk/apis/numbers_v2_end_user_type.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.numbers_v2_end_user_type.fetch_end_user_type

- **Route**: `GET /v2/RegulatoryCompliance/EndUserTypes/{Sid}`
- **Server**: `default5`
- **Signature**: `def fetch_end_user_type(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `NumbersV2RegulatoryComplianceEndUserType`
- **Returns (raw)**: `ApiResult[NumbersV2RegulatoryComplianceEndUserType, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV2RegulatoryComplianceEndUserType` | `twilio_sdk/models/numbers_v2_regulatory_compliance_end_user_type.py` |

### client.numbers_v2_end_user_type.list_end_user_type

- **Route**: `GET /v2/RegulatoryCompliance/EndUserTypes`
- **Server**: `default5`
- **Signature**: `def list_end_user_type(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListEndUserTypeResponse`
- **Returns (raw)**: `ApiResult[ListEndUserTypeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListEndUserTypeResponse` | `twilio_sdk/models/list_end_user_type_response.py` |

