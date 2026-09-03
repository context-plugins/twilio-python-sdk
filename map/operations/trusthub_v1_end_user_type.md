<!-- Generated file — do not edit; regenerated with the SDK. -->

# TrusthubV1EndUserType — operations

Accessor: `client.trusthub_v1_end_user_type` · Source: `twilio_sdk/apis/trusthub_v1_end_user_type.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.trusthub_v1_end_user_type.fetch_end_user_type2

- **Route**: `GET /v1/EndUserTypes/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default9`
- **Signature**: `def fetch_end_user_type2(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `NumbersV2RegulatoryComplianceEndUserType`
- **Returns (raw)**: `ApiResult[NumbersV2RegulatoryComplianceEndUserType, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV2RegulatoryComplianceEndUserType` | `twilio_sdk/models/numbers_v2_regulatory_compliance_end_user_type.py` |

### client.trusthub_v1_end_user_type.list_end_user_type2

- **Route**: `GET /v1/EndUserTypes`
- **Auth**: `account_sid_auth_token`
- **Server**: `default9`
- **Signature**: `def list_end_user_type2(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListEndUserTypeResponse`
- **Returns (raw)**: `ApiResult[ListEndUserTypeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListEndUserTypeResponse` | `twilio_sdk/models/list_end_user_type_response.py` |

