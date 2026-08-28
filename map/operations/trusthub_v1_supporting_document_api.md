<!-- Generated file — do not edit; regenerated with the SDK. -->

# TrusthubV1SupportingDocumentApi — operations

Accessor: `client.trusthub_v1_supporting_document_api` · Source: `twilio/apis/trusthub_v1_supporting_document_api.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.trusthub_v1_supporting_document_api.create_supporting_document2

- **Route**: `POST /v1/SupportingDocuments`
- **Server**: `default9`
- **Signature**: `def create_supporting_document2(friendly_name: str, type_: str, *, attributes: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `friendly_name`, `type_`
- **Params**: `friendly_name` — form field `FriendlyName` · `type_` — form field `Type` · `attributes` — form field `Attributes`
- **Returns (parsed)**: `TrusthubV1SupportingDocument`
- **Returns (raw)**: `ApiResult[TrusthubV1SupportingDocument, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrusthubV1SupportingDocument` | `twilio/models/trusthub_v1_supporting_document.py` |

### client.trusthub_v1_supporting_document_api.delete_supporting_document2

- **Route**: `DELETE /v1/SupportingDocuments/{Sid}`
- **Server**: `default9`
- **Signature**: `def delete_supporting_document2(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.trusthub_v1_supporting_document_api.fetch_supporting_document2

- **Route**: `GET /v1/SupportingDocuments/{Sid}`
- **Server**: `default9`
- **Signature**: `def fetch_supporting_document2(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `TrusthubV1SupportingDocument`
- **Returns (raw)**: `ApiResult[TrusthubV1SupportingDocument, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrusthubV1SupportingDocument` | `twilio/models/trusthub_v1_supporting_document.py` |

### client.trusthub_v1_supporting_document_api.list_supporting_document2

- **Route**: `GET /v1/SupportingDocuments`
- **Server**: `default9`
- **Signature**: `def list_supporting_document2(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListSupportingDocumentResponse1`
- **Returns (raw)**: `ApiResult[ListSupportingDocumentResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListSupportingDocumentResponse1` | `twilio/models/list_supporting_document_response1.py` |

### client.trusthub_v1_supporting_document_api.update_supporting_document2

- **Route**: `POST /v1/SupportingDocuments/{Sid}`
- **Server**: `default9`
- **Signature**: `def update_supporting_document2(sid: str, *, friendly_name: str | None = None, attributes: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `friendly_name` — form field `FriendlyName` · `attributes` — form field `Attributes`
- **Returns (parsed)**: `TrusthubV1SupportingDocument`
- **Returns (raw)**: `ApiResult[TrusthubV1SupportingDocument, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrusthubV1SupportingDocument` | `twilio/models/trusthub_v1_supporting_document.py` |

