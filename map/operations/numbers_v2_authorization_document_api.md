<!-- Generated file — do not edit; regenerated with the SDK. -->

# NumbersV2AuthorizationDocumentApi — operations

Accessor: `client.numbers_v2_authorization_document_api` · Source: `twilio_sdk/apis/numbers_v2_authorization_document_api.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.numbers_v2_authorization_document_api.create_authorization_document

- **Route**: `POST /v2/HostedNumber/AuthorizationDocuments`
- **Server**: `default5`
- **Signature**: `def create_authorization_document(address_sid: str, email: str, contact_phone_number: str, hosted_number_order_sids: list[str], *, contact_title: str | None = None, cc_emails: list[str] | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `address_sid`, `email`, `contact_phone_number`, `hosted_number_order_sids`
- **Params**: `address_sid` — form field `AddressSid` · `email` — form field `Email` · `contact_phone_number` — form field `ContactPhoneNumber` · `hosted_number_order_sids` — form field `HostedNumberOrderSids` · `contact_title` — form field `ContactTitle` · `cc_emails` — form field `CcEmails`
- **Returns (parsed)**: `NumbersV2AuthorizationDocument`
- **Returns (raw)**: `ApiResult[NumbersV2AuthorizationDocument, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV2AuthorizationDocument` | `twilio_sdk/models/numbers_v2_authorization_document.py` |

### client.numbers_v2_authorization_document_api.delete_authorization_document

- **Route**: `DELETE /v2/HostedNumber/AuthorizationDocuments/{Sid}`
- **Server**: `default5`
- **Signature**: `def delete_authorization_document(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.numbers_v2_authorization_document_api.fetch_authorization_document

- **Route**: `GET /v2/HostedNumber/AuthorizationDocuments/{Sid}`
- **Server**: `default5`
- **Signature**: `def fetch_authorization_document(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `NumbersV2AuthorizationDocument`
- **Returns (raw)**: `ApiResult[NumbersV2AuthorizationDocument, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NumbersV2AuthorizationDocument` | `twilio_sdk/models/numbers_v2_authorization_document.py` |

### client.numbers_v2_authorization_document_api.list_authorization_document

- **Route**: `GET /v2/HostedNumber/AuthorizationDocuments`
- **Server**: `default5`
- **Signature**: `def list_authorization_document(*, email: str | None = None, status: AuthorizationDocumentEnumStatusOrStr | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `email` — query `Email` · `status` — query `Status` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListAuthorizationDocumentResponse`
- **Returns (raw)**: `ApiResult[ListAuthorizationDocumentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AuthorizationDocumentEnumStatusOrStr` | `twilio_sdk/models/enums/authorization_document_enum_status.py` |
| `ListAuthorizationDocumentResponse` | `twilio_sdk/models/list_authorization_document_response.py` |

