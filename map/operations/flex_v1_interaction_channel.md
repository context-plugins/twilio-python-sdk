<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV1InteractionChannel — operations

Accessor: `client.flex_v1_interaction_channel` · Source: `twilio_sdk/apis/flex_v1_interaction_channel.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.flex_v1_interaction_channel.fetch_interaction_channel

- **Route**: `GET /v1/Interactions/{InteractionSid}/Channels/{Sid}`
- **Server**: `default13`
- **Signature**: `def fetch_interaction_channel(interaction_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `interaction_sid`, `sid`
- **Params**: `interaction_sid` — path `InteractionSid` · `sid` — path `Sid`
- **Returns (parsed)**: `FlexV1InteractionInteractionChannel`
- **Returns (raw)**: `ApiResult[FlexV1InteractionInteractionChannel, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1InteractionInteractionChannel` | `twilio_sdk/models/flex_v1_interaction_interaction_channel.py` |

### client.flex_v1_interaction_channel.list_interaction_channel

- **Route**: `GET /v1/Interactions/{InteractionSid}/Channels`
- **Server**: `default13`
- **Signature**: `def list_interaction_channel(interaction_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `interaction_sid`
- **Params**: `interaction_sid` — path `InteractionSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListInteractionChannelResponse`
- **Returns (raw)**: `ApiResult[ListInteractionChannelResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListInteractionChannelResponse` | `twilio_sdk/models/list_interaction_channel_response.py` |

### client.flex_v1_interaction_channel.update_interaction_channel

- **Route**: `POST /v1/Interactions/{InteractionSid}/Channels/{Sid}`
- **Server**: `default13`
- **Signature**: `def update_interaction_channel(interaction_sid: str, sid: str, status: InteractionChannelEnumUpdateChannelStatusOrStr, *, routing: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `interaction_sid`, `sid`, `status`
- **Params**: `interaction_sid` — path `InteractionSid` · `sid` — path `Sid` · `status` — form field `Status` · `routing` — form field `Routing`
- **Returns (parsed)**: `FlexV1InteractionInteractionChannel`
- **Returns (raw)**: `ApiResult[FlexV1InteractionInteractionChannel, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InteractionChannelEnumUpdateChannelStatusOrStr` | `twilio_sdk/models/enums/interaction_channel_enum_update_channel_status.py` |
| `FlexV1InteractionInteractionChannel` | `twilio_sdk/models/flex_v1_interaction_interaction_channel.py` |

