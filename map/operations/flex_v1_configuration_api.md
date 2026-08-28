<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV1ConfigurationApi — operations

Accessor: `client.flex_v1_configuration_api` · Source: `twilio_sdk/apis/flex_v1_configuration_api.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.flex_v1_configuration_api.fetch_configuration3

- **Route**: `GET /v1/Configuration`
- **Server**: `default13`
- **Signature**: `def fetch_configuration3(*, ui_version: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `ui_version` — query `UiVersion`
- **Returns (parsed)**: `FlexV1Configuration`
- **Returns (raw)**: `ApiResult[FlexV1Configuration, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1Configuration` | `twilio_sdk/models/flex_v1_configuration.py` |

### client.flex_v1_configuration_api.update_configuration3

- **Route**: `POST /v1/Configuration`
- **Server**: `default13`
- **Signature**: `def update_configuration3(*, body: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `FlexV1Configuration`
- **Returns (raw)**: `ApiResult[FlexV1Configuration, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1Configuration` | `twilio_sdk/models/flex_v1_configuration.py` |

