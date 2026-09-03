<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideoV1CompositionHookApi — operations

Accessor: `client.video_v1_composition_hook_api` · Source: `twilio_sdk/apis/video_v1_composition_hook_api.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.video_v1_composition_hook_api.create_composition_hook

- **Route**: `POST /v1/CompositionHooks`
- **Auth**: `account_sid_auth_token`
- **Server**: `default6`
- **Signature**: `def create_composition_hook(friendly_name: str, *, enabled: bool | None = None, video_layout: Any | None = None, audio_sources: list[str] | None = None, audio_sources_excluded: list[str] | None = None, resolution: str | None = None, format: CompositionHookEnumFormatOrStr | None = None, status_callback: str | None = None, status_callback_method: AmdStatusCallbackMethodOrStr | None = None, trim: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `friendly_name`
- **Params**: `friendly_name` — form field `FriendlyName` · `enabled` — form field `Enabled` · `video_layout` — form field `VideoLayout` · `audio_sources` — form field `AudioSources` · `audio_sources_excluded` — form field `AudioSourcesExcluded` · `resolution` — form field `Resolution` · `format` — form field `Format` · `status_callback` — form field `StatusCallback` · `status_callback_method` — form field `StatusCallbackMethod` · `trim` — form field `Trim`
- **Returns (parsed)**: `VideoV1CompositionHook`
- **Returns (raw)**: `ApiResult[VideoV1CompositionHook, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CompositionHookEnumFormatOrStr` | `twilio_sdk/models/enums/composition_hook_enum_format.py` |
| `AmdStatusCallbackMethodOrStr` | `twilio_sdk/models/enums/amd_status_callback_method.py` |
| `VideoV1CompositionHook` | `twilio_sdk/models/video_v1_composition_hook.py` |

### client.video_v1_composition_hook_api.delete_composition_hook

- **Route**: `DELETE /v1/CompositionHooks/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default6`
- **Signature**: `def delete_composition_hook(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.video_v1_composition_hook_api.fetch_composition_hook

- **Route**: `GET /v1/CompositionHooks/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default6`
- **Signature**: `def fetch_composition_hook(sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid`
- **Returns (parsed)**: `VideoV1CompositionHook`
- **Returns (raw)**: `ApiResult[VideoV1CompositionHook, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VideoV1CompositionHook` | `twilio_sdk/models/video_v1_composition_hook.py` |

### client.video_v1_composition_hook_api.list_composition_hook

- **Route**: `GET /v1/CompositionHooks`
- **Auth**: `account_sid_auth_token`
- **Server**: `default6`
- **Signature**: `def list_composition_hook(*, enabled: bool | None = None, date_created_after: RFC3339DateTime | None = None, date_created_before: RFC3339DateTime | None = None, friendly_name: str | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `enabled` — query `Enabled` · `date_created_after` — query `DateCreatedAfter` · `date_created_before` — query `DateCreatedBefore` · `friendly_name` — query `FriendlyName` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListCompositionHookResponse`
- **Returns (raw)**: `ApiResult[ListCompositionHookResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListCompositionHookResponse` | `twilio_sdk/models/list_composition_hook_response.py` |

### client.video_v1_composition_hook_api.update_composition_hook

- **Route**: `POST /v1/CompositionHooks/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default6`
- **Signature**: `def update_composition_hook(sid: str, friendly_name: str, *, enabled: bool | None = None, video_layout: Any | None = None, audio_sources: list[str] | None = None, audio_sources_excluded: list[str] | None = None, trim: bool | None = None, format: CompositionHookEnumFormatOrStr | None = None, resolution: str | None = None, status_callback: str | None = None, status_callback_method: AmdStatusCallbackMethodOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`, `friendly_name`
- **Params**: `sid` — path `Sid` · `friendly_name` — form field `FriendlyName` · `enabled` — form field `Enabled` · `video_layout` — form field `VideoLayout` · `audio_sources` — form field `AudioSources` · `audio_sources_excluded` — form field `AudioSourcesExcluded` · `trim` — form field `Trim` · `format` — form field `Format` · `resolution` — form field `Resolution` · `status_callback` — form field `StatusCallback` · `status_callback_method` — form field `StatusCallbackMethod`
- **Returns (parsed)**: `VideoV1CompositionHook`
- **Returns (raw)**: `ApiResult[VideoV1CompositionHook, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CompositionHookEnumFormatOrStr` | `twilio_sdk/models/enums/composition_hook_enum_format.py` |
| `AmdStatusCallbackMethodOrStr` | `twilio_sdk/models/enums/amd_status_callback_method.py` |
| `VideoV1CompositionHook` | `twilio_sdk/models/video_v1_composition_hook.py` |

