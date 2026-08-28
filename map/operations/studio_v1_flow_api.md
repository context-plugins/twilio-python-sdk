<!-- Generated file — do not edit; regenerated with the SDK. -->

# StudioV1FlowApi — operations

Accessor: `client.studio_v1_flow_api` · Source: `twilio/apis/studio_v1_flow_api.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.studio_v1_flow_api.delete_flow

- **Route**: `DELETE /v1/Flows/{Sid}`
- **Server**: `default11`
- **Signature**: `def delete_flow(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.studio_v1_flow_api.fetch_flow

- **Route**: `GET /v1/Flows/{Sid}`
- **Server**: `default11`
- **Signature**: `def fetch_flow(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `StudioV1Flow`
- **Returns (raw)**: `ApiResult[StudioV1Flow, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StudioV1Flow` | `twilio/models/studio_v1_flow.py` |

### client.studio_v1_flow_api.list_flow

- **Route**: `GET /v1/Flows`
- **Server**: `default11`
- **Signature**: `def list_flow(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListFlowResponse`
- **Returns (raw)**: `ApiResult[ListFlowResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListFlowResponse` | `twilio/models/list_flow_response.py` |

