<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV2SupportingDocument — operations

Accessor: `client.numbers_v2_supporting_document` · Source: `twilio/apis/numbers_v2_supporting_document.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.numbers_v2_supporting_document.create_supporting_document

- **Route**: `POST /v2/RegulatoryCompliance/SupportingDocuments`
- **Server**: `default5`
- **Signature**: `def create_supporting_document(friendly_name: str, type_: str, *, attributes: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `friendly_name`, `type_`
- **Params**: `friendly_name` — form field `FriendlyName` · `type_` — form field `Type` · `attributes` — form field `Attributes`
- **Returns (parsed)**: `NumbersV2RegulatoryComplianceSupportingDocument`
- **Returns (raw)**: `ApiResult[NumbersV2RegulatoryComplianceSupportingDocument, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV2RegulatoryComplianceSupportingDocument` | `twilio/models/numbers_v2_regulatory_compliance_supporting_document.py` |

### client.numbers_v2_supporting_document.delete_supporting_document

- **Route**: `DELETE /v2/RegulatoryCompliance/SupportingDocuments/{Sid}`
- **Server**: `default5`
- **Signature**: `def delete_supporting_document(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.numbers_v2_supporting_document.fetch_supporting_document

- **Route**: `GET /v2/RegulatoryCompliance/SupportingDocuments/{Sid}`
- **Server**: `default5`
- **Signature**: `def fetch_supporting_document(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `NumbersV2RegulatoryComplianceSupportingDocument`
- **Returns (raw)**: `ApiResult[NumbersV2RegulatoryComplianceSupportingDocument, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV2RegulatoryComplianceSupportingDocument` | `twilio/models/numbers_v2_regulatory_compliance_supporting_document.py` |

### client.numbers_v2_supporting_document.list_supporting_document

- **Route**: `GET /v2/RegulatoryCompliance/SupportingDocuments`
- **Server**: `default5`
- **Signature**: `def list_supporting_document(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListSupportingDocumentResponse`
- **Returns (raw)**: `ApiResult[ListSupportingDocumentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListSupportingDocumentResponse` | `twilio/models/list_supporting_document_response.py` |

### client.numbers_v2_supporting_document.update_supporting_document

- **Route**: `POST /v2/RegulatoryCompliance/SupportingDocuments/{Sid}`
- **Server**: `default5`
- **Signature**: `def update_supporting_document(sid: str, *, friendly_name: str | None = None, attributes: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `friendly_name` — form field `FriendlyName` · `attributes` — form field `Attributes`
- **Returns (parsed)**: `NumbersV2RegulatoryComplianceSupportingDocument`
- **Returns (raw)**: `ApiResult[NumbersV2RegulatoryComplianceSupportingDocument, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV2RegulatoryComplianceSupportingDocument` | `twilio/models/numbers_v2_regulatory_compliance_supporting_document.py` |

