<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV1PluginVersionArchiveApi — operations

Accessor: `client.flex_v1_plugin_version_archive_api` · Source: `twilio/apis/flex_v1_plugin_version_archive_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.flex_v1_plugin_version_archive_api.update_plugin_version_archive

- **Route**: `POST /v1/PluginService/Plugins/{PluginSid}/Versions/{Sid}/Archive`
- **Server**: `default13`
- **Signature**: `def update_plugin_version_archive(plugin_sid: str, sid: str, *, flex_metadata: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plugin_sid`, `sid`
- **Params**: `plugin_sid` — path `PluginSid` · `sid` — path `Sid` · `flex_metadata` — header `Flex-Metadata`
- **Returns (parsed)**: `FlexV1PluginVersionArchive`
- **Returns (raw)**: `ApiResult[FlexV1PluginVersionArchive, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1PluginVersionArchive` | `twilio/models/flex_v1_plugin_version_archive.py` |

