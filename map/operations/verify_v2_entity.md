<!-- Generated file — do not edit; regenerated with the SDK. -->

# VerifyV2Entity — operations

Accessor: `client.verify_v2_entity` · Source: `twilio/apis/verify_v2_entity.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.verify_v2_entity.create_entity

- **Route**: `POST /v2/Services/{ServiceSid}/Entities`
- **Server**: `default3`
- **Signature**: `def create_entity(service_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `identity`
- **Params**: `service_sid` — path `ServiceSid` · `identity` — form field `Identity`
- **Returns (parsed)**: `VerifyV2ServiceEntity`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceEntity, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2ServiceEntity` | `twilio/models/verify_v2_service_entity.py` |

### client.verify_v2_entity.delete_entity

- **Route**: `DELETE /v2/Services/{ServiceSid}/Entities/{Identity}`
- **Server**: `default3`
- **Signature**: `def delete_entity(service_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `identity`
- **Params**: `service_sid` — path `ServiceSid` · `identity` — path `Identity`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.verify_v2_entity.fetch_entity

- **Route**: `GET /v2/Services/{ServiceSid}/Entities/{Identity}`
- **Server**: `default3`
- **Signature**: `def fetch_entity(service_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`, `identity`
- **Params**: `service_sid` — path `ServiceSid` · `identity` — path `Identity`
- **Returns (parsed)**: `VerifyV2ServiceEntity`
- **Returns (raw)**: `ApiResult[VerifyV2ServiceEntity, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VerifyV2ServiceEntity` | `twilio/models/verify_v2_service_entity.py` |

### client.verify_v2_entity.list_entity

- **Route**: `GET /v2/Services/{ServiceSid}/Entities`
- **Server**: `default3`
- **Signature**: `def list_entity(service_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_sid`
- **Params**: `service_sid` — path `ServiceSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListEntityResponse`
- **Returns (raw)**: `ApiResult[ListEntityResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListEntityResponse` | `twilio/models/list_entity_response.py` |

