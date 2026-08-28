<!-- Generated file — do not edit; regenerated with the SDK. -->

# ProxyV1Interaction — operations

Accessor: `client.proxy_v1_interaction` · Source: `twilio_sdk/apis/proxy_v1_interaction.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.proxy_v1_interaction.delete_interaction

- **Route**: `DELETE /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Interactions/{Sid}`
- **Server**: `default10`
- **Signature**: `def delete_interaction(service_sid: str, session_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `session_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `session_sid` — path `SessionSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.proxy_v1_interaction.fetch_interaction

- **Route**: `GET /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Interactions/{Sid}`
- **Server**: `default10`
- **Signature**: `def fetch_interaction(service_sid: str, session_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `session_sid`, `sid`
- **Params**: `service_sid` — path `ServiceSid` · `session_sid` — path `SessionSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ProxyV1ServiceSessionInteraction`
- **Returns (raw)**: `ApiResult[ProxyV1ServiceSessionInteraction, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProxyV1ServiceSessionInteraction` | `twilio_sdk/models/proxy_v1_service_session_interaction.py` |

### client.proxy_v1_interaction.list_interaction

- **Route**: `GET /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Interactions`
- **Server**: `default10`
- **Signature**: `def list_interaction(service_sid: str, session_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `session_sid`
- **Params**: `service_sid` — path `ServiceSid` · `session_sid` — path `SessionSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListInteractionResponse`
- **Returns (raw)**: `ApiResult[ListInteractionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListInteractionResponse` | `twilio_sdk/models/list_interaction_response.py` |

