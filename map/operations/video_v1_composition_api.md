<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideoV1CompositionApi — operations

Accessor: `client.video_v1_composition_api` · Source: `twilio_sdk/apis/video_v1_composition_api.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.video_v1_composition_api.create_composition

- **Route**: `POST /v1/Compositions`
- **Server**: `default6`
- **Signature**: `def create_composition(room_sid: str, *, video_layout: Any | None = None, audio_sources: list[str] | None = None, audio_sources_excluded: list[str] | None = None, resolution: str | None = None, format: CompositionEnumFormatOrStr | None = None, status_callback: AnyUrl | None = None, status_callback_method: AmdStatusCallbackMethodOrStr | None = None, trim: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `room_sid`
- **Params**: `room_sid` — form field `RoomSid` · `video_layout` — form field `VideoLayout` · `audio_sources` — form field `AudioSources` · `audio_sources_excluded` — form field `AudioSourcesExcluded` · `resolution` — form field `Resolution` · `format` — form field `Format` · `status_callback` — form field `StatusCallback` · `status_callback_method` — form field `StatusCallbackMethod` · `trim` — form field `Trim`
- **Returns (parsed)**: `VideoV1Composition`
- **Returns (raw)**: `ApiResult[VideoV1Composition, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CompositionEnumFormatOrStr` | `twilio_sdk/models/enums/composition_enum_format.py` |
| `AmdStatusCallbackMethodOrStr` | `twilio_sdk/models/enums/amd_status_callback_method.py` |
| `VideoV1Composition` | `twilio_sdk/models/video_v1_composition.py` |

### client.video_v1_composition_api.delete_composition

- **Route**: `DELETE /v1/Compositions/{Sid}`
- **Server**: `default6`
- **Signature**: `def delete_composition(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.video_v1_composition_api.fetch_composition

- **Route**: `GET /v1/Compositions/{Sid}`
- **Server**: `default6`
- **Signature**: `def fetch_composition(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `VideoV1Composition`
- **Returns (raw)**: `ApiResult[VideoV1Composition, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VideoV1Composition` | `twilio_sdk/models/video_v1_composition.py` |

### client.video_v1_composition_api.list_composition

- **Route**: `GET /v1/Compositions`
- **Server**: `default6`
- **Signature**: `def list_composition(*, status: CompositionEnumStatusOrStr | None = None, date_created_after: RFC3339DateTime | None = None, date_created_before: RFC3339DateTime | None = None, room_sid: str | None = None, page_size: int | None = 50, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `status` — query `Status` · `date_created_after` — query `DateCreatedAfter` · `date_created_before` — query `DateCreatedBefore` · `room_sid` — query `RoomSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListCompositionResponse`
- **Returns (raw)**: `ApiResult[ListCompositionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CompositionEnumStatusOrStr` | `twilio_sdk/models/enums/composition_enum_status.py` |
| `ListCompositionResponse` | `twilio_sdk/models/list_composition_response.py` |

