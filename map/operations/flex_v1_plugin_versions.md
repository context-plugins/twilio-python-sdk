<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV1PluginVersions — operations

Accessor: `client.flex_v1_plugin_versions` · Source: `twilio_sdk/apis/flex_v1_plugin_versions.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.flex_v1_plugin_versions.create_plugin_version

- **Route**: `POST /v1/PluginService/Plugins/{PluginSid}/Versions`
- **Auth**: `account_sid_auth_token`
- **Server**: `default13`
- **Signature**: `def create_plugin_version(plugin_sid: str, version: str, plugin_url: str, *, flex_metadata: str | None = None, changelog: str | None = None, private: bool | None = None, cli_version: str | None = None, validate_status: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plugin_sid`, `version`, `plugin_url`
- **Params**: `plugin_sid` — path `PluginSid` · `flex_metadata` — header `Flex-Metadata` · `version` — form field `Version` · `plugin_url` — form field `PluginUrl` · `changelog` — form field `Changelog` · `private` — form field `Private` · `cli_version` — form field `CliVersion` · `validate_status` — form field `ValidateStatus`
- **Returns (parsed)**: `FlexV1PluginPluginVersion`
- **Returns (raw)**: `ApiResult[FlexV1PluginPluginVersion, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1PluginPluginVersion` | `twilio_sdk/models/flex_v1_plugin_plugin_version.py` |

### client.flex_v1_plugin_versions.fetch_plugin_version

- **Route**: `GET /v1/PluginService/Plugins/{PluginSid}/Versions/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default13`
- **Signature**: `def fetch_plugin_version(plugin_sid: str, sid: str, *, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plugin_sid`, `sid`
- **Params**: `plugin_sid` — path `PluginSid` · `sid` — path `Sid` · `flex_metadata` — header `Flex-Metadata`
- **Returns (parsed)**: `FlexV1PluginPluginVersion`
- **Returns (raw)**: `ApiResult[FlexV1PluginPluginVersion, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1PluginPluginVersion` | `twilio_sdk/models/flex_v1_plugin_plugin_version.py` |

### client.flex_v1_plugin_versions.list_plugin_version

- **Route**: `GET /v1/PluginService/Plugins/{PluginSid}/Versions`
- **Auth**: `account_sid_auth_token`
- **Server**: `default13`
- **Signature**: `def list_plugin_version(plugin_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plugin_sid`
- **Params**: `plugin_sid` — path `PluginSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken` · `flex_metadata` — header `Flex-Metadata`
- **Returns (parsed)**: `ListPluginVersionResponse`
- **Returns (raw)**: `ApiResult[ListPluginVersionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListPluginVersionResponse` | `twilio_sdk/models/list_plugin_version_response.py` |

