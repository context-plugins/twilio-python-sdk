<!-- Generated file — do not edit; regenerated with the SDK. -->

# Contentv1ContentApi — operations

Accessor: `client.contentv1_content_api` · Source: `twilio_sdk/apis/contentv1_content_api.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.contentv1_content_api.create_content

- **Route**: `POST /v1/Content`
- **Auth**: `account_sid_auth_token`
- **Server**: `default2`
- **Signature**: `def create_content(body: ContentCreateRequest | ContentCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ContentV1Content`
- **Returns (raw)**: `ApiResult[ContentV1Content, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentCreateRequest` | `twilio_sdk/models/content_create_request.py` |
| `ContentCreateRequestDict` | `twilio_sdk/models/content_create_request.py` |
| `ContentV1Content` | `twilio_sdk/models/content_v1_content.py` |

### client.contentv1_content_api.delete_content

- **Route**: `DELETE /v1/Content/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default2`
- **Signature**: `def delete_content(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.contentv1_content_api.fetch_content

- **Route**: `GET /v1/Content/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default2`
- **Signature**: `def fetch_content(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `ContentV1Content`
- **Returns (raw)**: `ApiResult[ContentV1Content, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentV1Content` | `twilio_sdk/models/content_v1_content.py` |

### client.contentv1_content_api.list_content

- **Route**: `GET /v1/Content`
- **Auth**: `account_sid_auth_token`
- **Server**: `default2`
- **Signature**: `def list_content(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListContentResponse`
- **Returns (raw)**: `ApiResult[ListContentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListContentResponse` | `twilio_sdk/models/list_content_response.py` |

### client.contentv1_content_api.update_content

- **Route**: `PUT /v1/Content/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default2`
- **Signature**: `def update_content(sid: str, body: ContentUpdateRequest | ContentUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`, `body`
- **Params**: `sid` — path `Sid` · `body` — JSON body
- **Returns (parsed)**: `ContentV1Content`
- **Returns (raw)**: `ApiResult[ContentV1Content, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentUpdateRequest` | `twilio_sdk/models/content_update_request.py` |
| `ContentUpdateRequestDict` | `twilio_sdk/models/content_update_request.py` |
| `ContentV1Content` | `twilio_sdk/models/content_v1_content.py` |

