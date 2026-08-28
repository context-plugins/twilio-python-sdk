<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV1ConfiguredPlugin — operations

Accessor: `client.flex_v1_configured_plugin` · Source: `twilio_sdk/apis/flex_v1_configured_plugin.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.flex_v1_configured_plugin.fetch_configured_plugin

- **Route**: `GET /v1/PluginService/Configurations/{ConfigurationSid}/Plugins/{PluginSid}`
- **Server**: `default13`
- **Signature**: `def fetch_configured_plugin(configuration_sid: str, plugin_sid: str, *, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `configuration_sid`, `plugin_sid`
- **Params**: `configuration_sid` — path `ConfigurationSid` · `plugin_sid` — path `PluginSid` · `flex_metadata` — header `Flex-Metadata`
- **Returns (parsed)**: `FlexV1PluginConfigurationConfiguredPlugin`
- **Returns (raw)**: `ApiResult[FlexV1PluginConfigurationConfiguredPlugin, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1PluginConfigurationConfiguredPlugin` | `twilio_sdk/models/flex_v1_plugin_configuration_configured_plugin.py` |

### client.flex_v1_configured_plugin.list_configured_plugin

- **Route**: `GET /v1/PluginService/Configurations/{ConfigurationSid}/Plugins`
- **Server**: `default13`
- **Signature**: `def list_configured_plugin(configuration_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `configuration_sid`
- **Params**: `configuration_sid` — path `ConfigurationSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken` · `flex_metadata` — header `Flex-Metadata`
- **Returns (parsed)**: `ListConfiguredPluginResponse`
- **Returns (raw)**: `ApiResult[ListConfiguredPluginResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListConfiguredPluginResponse` | `twilio_sdk/models/list_configured_plugin_response.py` |

