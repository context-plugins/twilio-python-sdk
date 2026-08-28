<!-- Generated file — do not edit; regenerated with the SDK. -->

# StudioV2FlowApi — operations

Accessor: `client.studio_v2_flow_api` · Source: `twilio_sdk/apis/studio_v2_flow_api.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.studio_v2_flow_api.create_flow

- **Route**: `POST /v2/Flows`
- **Server**: `default11`
- **Signature**: `def create_flow(friendly_name: str, status: FlowEnumStatusOrStr, definition: Any, *, commit_message: str | None = None, author_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `friendly_name`, `status`, `definition`
- **Params**: `friendly_name` — form field `FriendlyName` · `status` — form field `Status` · `definition` — form field `Definition` · `commit_message` — form field `CommitMessage` · `author_sid` — form field `AuthorSid`
- **Returns (parsed)**: `StudioV2Flow`
- **Returns (raw)**: `ApiResult[StudioV2Flow, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlowEnumStatusOrStr` | `twilio_sdk/models/enums/flow_enum_status.py` |
| `StudioV2Flow` | `twilio_sdk/models/studio_v2_flow.py` |

### client.studio_v2_flow_api.delete_flow2

- **Route**: `DELETE /v2/Flows/{Sid}`
- **Server**: `default11`
- **Signature**: `def delete_flow2(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.studio_v2_flow_api.fetch_flow2

- **Route**: `GET /v2/Flows/{Sid}`
- **Server**: `default11`
- **Signature**: `def fetch_flow2(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `StudioV2Flow`
- **Returns (raw)**: `ApiResult[StudioV2Flow, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StudioV2Flow` | `twilio_sdk/models/studio_v2_flow.py` |

### client.studio_v2_flow_api.list_flow2

- **Route**: `GET /v2/Flows`
- **Server**: `default11`
- **Signature**: `def list_flow2(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListFlowResponse1`
- **Returns (raw)**: `ApiResult[ListFlowResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListFlowResponse1` | `twilio_sdk/models/list_flow_response1.py` |

### client.studio_v2_flow_api.update_flow

- **Route**: `POST /v2/Flows/{Sid}`
- **Server**: `default11`
- **Signature**: `def update_flow(sid: str, status: FlowEnumStatusOrStr, *, friendly_name: str | None = None, definition: Any | None = None, commit_message: str | None = None, author_sid: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`, `status`
- **Params**: `sid` — path `Sid` · `status` — form field `Status` · `friendly_name` — form field `FriendlyName` · `definition` — form field `Definition` · `commit_message` — form field `CommitMessage` · `author_sid` — form field `AuthorSid`
- **Returns (parsed)**: `StudioV2Flow`
- **Returns (raw)**: `ApiResult[StudioV2Flow, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlowEnumStatusOrStr` | `twilio_sdk/models/enums/flow_enum_status.py` |
| `StudioV2Flow` | `twilio_sdk/models/studio_v2_flow.py` |

