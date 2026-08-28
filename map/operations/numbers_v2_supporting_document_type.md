<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV2SupportingDocumentType — operations

Accessor: `client.numbers_v2_supporting_document_type` · Source: `twilio/apis/numbers_v2_supporting_document_type.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.numbers_v2_supporting_document_type.fetch_supporting_document_type

- **Route**: `GET /v2/RegulatoryCompliance/SupportingDocumentTypes/{Sid}`
- **Server**: `default5`
- **Signature**: `def fetch_supporting_document_type(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `NumbersV2RegulatoryComplianceSupportingDocumentType`
- **Returns (raw)**: `ApiResult[NumbersV2RegulatoryComplianceSupportingDocumentType, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV2RegulatoryComplianceSupportingDocumentType` | `twilio/models/numbers_v2_regulatory_compliance_supporting_document_type.py` |

### client.numbers_v2_supporting_document_type.list_supporting_document_type

- **Route**: `GET /v2/RegulatoryCompliance/SupportingDocumentTypes`
- **Server**: `default5`
- **Signature**: `def list_supporting_document_type(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListSupportingDocumentTypeResponse`
- **Returns (raw)**: `ApiResult[ListSupportingDocumentTypeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListSupportingDocumentTypeResponse` | `twilio/models/list_supporting_document_type_response.py` |

