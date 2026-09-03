<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV1PluginConfigurationApi — operations

Accessor: `client.flex_v1_plugin_configuration_api` · Source: `twilio_sdk/apis/flex_v1_plugin_configuration_api.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.flex_v1_plugin_configuration_api.create_plugin_configuration

- **Route**: `POST /v1/PluginService/Configurations`
- **Auth**: `account_sid_auth_token`
- **Server**: `default13`
- **Signature**: `def create_plugin_configuration(name: str, *, flex_metadata: str | None = None, plugins: list[Any] | None = None, description: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `name`
- **Params**: `flex_metadata` — header `Flex-Metadata` · `name` — form field `Name` · `plugins` — form field `Plugins` · `description` — form field `Description`
- **Returns (parsed)**: `FlexV1PluginConfiguration`
- **Returns (raw)**: `ApiResult[FlexV1PluginConfiguration, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1PluginConfiguration` | `twilio_sdk/models/flex_v1_plugin_configuration.py` |

### client.flex_v1_plugin_configuration_api.fetch_plugin_configuration

- **Route**: `GET /v1/PluginService/Configurations/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default13`
- **Signature**: `def fetch_plugin_configuration(sid: str, *, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sid`
- **Params**: `sid` — path `Sid` · `flex_metadata` — header `Flex-Metadata`
- **Returns (parsed)**: `FlexV1PluginConfiguration`
- **Returns (raw)**: `ApiResult[FlexV1PluginConfiguration, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1PluginConfiguration` | `twilio_sdk/models/flex_v1_plugin_configuration.py` |

### client.flex_v1_plugin_configuration_api.list_plugin_configuration

- **Route**: `GET /v1/PluginService/Configurations`
- **Auth**: `account_sid_auth_token`
- **Server**: `default13`
- **Signature**: `def list_plugin_configuration(*, page_size: int | None = None, page: int | None = None, page_token: str | None = None, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken` · `flex_metadata` — header `Flex-Metadata`
- **Returns (parsed)**: `ListPluginConfigurationResponse`
- **Returns (raw)**: `ApiResult[ListPluginConfigurationResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListPluginConfigurationResponse` | `twilio_sdk/models/list_plugin_configuration_response.py` |

