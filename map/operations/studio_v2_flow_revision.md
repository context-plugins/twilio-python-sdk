<!-- Generated file — do not edit; regenerated with the SDK. -->

# StudioV2FlowRevision — operations

Accessor: `client.studio_v2_flow_revision` · Source: `twilio_sdk/apis/studio_v2_flow_revision.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.studio_v2_flow_revision.fetch_flow_revision

- **Route**: `GET /v2/Flows/{Sid}/Revisions/{Revision}`
- **Server**: `default11`
- **Signature**: `def fetch_flow_revision(sid: str, revision: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`, `revision`
- **Params**: `sid` — path `Sid` · `revision` — path `Revision`
- **Returns (parsed)**: `StudioV2FlowFlowRevision`
- **Returns (raw)**: `ApiResult[StudioV2FlowFlowRevision, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StudioV2FlowFlowRevision` | `twilio_sdk/models/studio_v2_flow_flow_revision.py` |

### client.studio_v2_flow_revision.list_flow_revision

- **Route**: `GET /v2/Flows/{Sid}/Revisions`
- **Server**: `default11`
- **Signature**: `def list_flow_revision(sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListFlowRevisionResponse`
- **Returns (raw)**: `ApiResult[ListFlowRevisionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListFlowRevisionResponse` | `twilio_sdk/models/list_flow_revision_response.py` |

