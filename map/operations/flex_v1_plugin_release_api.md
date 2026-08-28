<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV1PluginReleaseApi — operations

Accessor: `client.flex_v1_plugin_release_api` · Source: `twilio/apis/flex_v1_plugin_release_api.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.flex_v1_plugin_release_api.create_plugin_release

- **Route**: `POST /v1/PluginService/Releases`
- **Server**: `default13`
- **Signature**: `def create_plugin_release(configuration_id: str, *, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `configuration_id`
- **Params**: `flex_metadata` — header `Flex-Metadata` · `configuration_id` — form field `ConfigurationId`
- **Returns (parsed)**: `FlexV1PluginRelease`
- **Returns (raw)**: `ApiResult[FlexV1PluginRelease, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1PluginRelease` | `twilio/models/flex_v1_plugin_release.py` |

### client.flex_v1_plugin_release_api.fetch_plugin_release

- **Route**: `GET /v1/PluginService/Releases/{Sid}`
- **Server**: `default13`
- **Signature**: `def fetch_plugin_release(sid: str, *, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `flex_metadata` — header `Flex-Metadata`
- **Returns (parsed)**: `FlexV1PluginRelease`
- **Returns (raw)**: `ApiResult[FlexV1PluginRelease, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1PluginRelease` | `twilio/models/flex_v1_plugin_release.py` |

### client.flex_v1_plugin_release_api.list_plugin_release

- **Route**: `GET /v1/PluginService/Releases`
- **Server**: `default13`
- **Signature**: `def list_plugin_release(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken` · `flex_metadata` — header `Flex-Metadata`
- **Returns (parsed)**: `ListPluginReleaseResponse`
- **Returns (raw)**: `ApiResult[ListPluginReleaseResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListPluginReleaseResponse` | `twilio/models/list_plugin_release_response.py` |

