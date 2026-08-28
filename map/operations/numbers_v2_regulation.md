<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV2Regulation — operations

Accessor: `client.numbers_v2_regulation` · Source: `twilio/apis/numbers_v2_regulation.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.numbers_v2_regulation.fetch_regulation

- **Route**: `GET /v2/RegulatoryCompliance/Regulations/{Sid}`
- **Server**: `default5`
- **Signature**: `def fetch_regulation(sid: str, *, include_constraints: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `include_constraints` — query `IncludeConstraints`
- **Returns (parsed)**: `NumbersV2RegulatoryComplianceRegulation`
- **Returns (raw)**: `ApiResult[NumbersV2RegulatoryComplianceRegulation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV2RegulatoryComplianceRegulation` | `twilio/models/numbers_v2_regulatory_compliance_regulation.py` |

### client.numbers_v2_regulation.list_regulation

- **Route**: `GET /v2/RegulatoryCompliance/Regulations`
- **Server**: `default5`
- **Signature**: `def list_regulation(*, end_user_type: RegulationEnumEndUserTypeOrStr | None = None, iso_country: str | None = None, number_type: str | None = None, include_constraints: bool | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `end_user_type` — query `EndUserType` · `iso_country` — query `IsoCountry` · `number_type` — query `NumberType` · `include_constraints` — query `IncludeConstraints` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListRegulationResponse`
- **Returns (raw)**: `ApiResult[ListRegulationResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RegulationEnumEndUserTypeOrStr` | `twilio/models/enums/regulation_enum_end_user_type.py` |
| `ListRegulationResponse` | `twilio/models/list_regulation_response.py` |

