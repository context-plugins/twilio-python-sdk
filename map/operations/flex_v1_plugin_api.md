<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV1PluginApi — operations

Accessor: `client.flex_v1_plugin_api` · Source: `twilio_sdk/apis/flex_v1_plugin_api.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.flex_v1_plugin_api.create_plugin

- **Route**: `POST /v1/PluginService/Plugins`
- **Server**: `default13`
- **Signature**: `def create_plugin(unique_name: str, *, flex_metadata: str | None = None, friendly_name: str | None = None, description: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `unique_name`
- **Params**: `flex_metadata` — header `Flex-Metadata` · `unique_name` — form field `UniqueName` · `friendly_name` — form field `FriendlyName` · `description` — form field `Description`
- **Returns (parsed)**: `FlexV1Plugin`
- **Returns (raw)**: `ApiResult[FlexV1Plugin, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1Plugin` | `twilio_sdk/models/flex_v1_plugin.py` |

### client.flex_v1_plugin_api.fetch_plugin

- **Route**: `GET /v1/PluginService/Plugins/{Sid}`
- **Server**: `default13`
- **Signature**: `def fetch_plugin(sid: str, *, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `flex_metadata` — header `Flex-Metadata`
- **Returns (parsed)**: `FlexV1Plugin`
- **Returns (raw)**: `ApiResult[FlexV1Plugin, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1Plugin` | `twilio_sdk/models/flex_v1_plugin.py` |

### client.flex_v1_plugin_api.list_plugin

- **Route**: `GET /v1/PluginService/Plugins`
- **Server**: `default13`
- **Signature**: `def list_plugin(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken` · `flex_metadata` — header `Flex-Metadata`
- **Returns (parsed)**: `ListPluginResponse`
- **Returns (raw)**: `ApiResult[ListPluginResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListPluginResponse` | `twilio_sdk/models/list_plugin_response.py` |

### client.flex_v1_plugin_api.update_plugin

- **Route**: `POST /v1/PluginService/Plugins/{Sid}`
- **Server**: `default13`
- **Signature**: `def update_plugin(sid: str, *, flex_metadata: str | None = None, friendly_name: str | None = None, description: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `flex_metadata` — header `Flex-Metadata` · `friendly_name` — form field `FriendlyName` · `description` — form field `Description`
- **Returns (parsed)**: `FlexV1Plugin`
- **Returns (raw)**: `ApiResult[FlexV1Plugin, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1Plugin` | `twilio_sdk/models/flex_v1_plugin.py` |

