<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV1InteractionTransfer — operations

Accessor: `client.flex_v1_interaction_transfer` · Source: `twilio_sdk/apis/flex_v1_interaction_transfer.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.flex_v1_interaction_transfer.create_interaction_transfer

- **Route**: `POST /v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Transfers`
- **Auth**: `account_sid_auth_token`
- **Server**: `default13`
- **Signature**: `def create_interaction_transfer(interaction_sid: str, channel_sid: str, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `interaction_sid`, `channel_sid`
- **Params**: `interaction_sid` — path `InteractionSid` · `channel_sid` — path `ChannelSid` · `body` — JSON body
- **Returns (parsed)**: `FlexV1InteractionInteractionChannelInteractionTransfer`
- **Returns (raw)**: `ApiResult[FlexV1InteractionInteractionChannelInteractionTransfer, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1InteractionInteractionChannelInteractionTransfer` | `twilio_sdk/models/flex_v1_interaction_interaction_channel_interaction_transfer.py` |

### client.flex_v1_interaction_transfer.fetch_interaction_transfer

- **Route**: `GET /v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Transfers/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default13`
- **Signature**: `def fetch_interaction_transfer(interaction_sid: str, channel_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `interaction_sid`, `channel_sid`, `sid`
- **Params**: `interaction_sid` — path `InteractionSid` · `channel_sid` — path `ChannelSid` · `sid` — path `Sid`
- **Returns (parsed)**: `FlexV1InteractionInteractionChannelInteractionTransfer`
- **Returns (raw)**: `ApiResult[FlexV1InteractionInteractionChannelInteractionTransfer, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1InteractionInteractionChannelInteractionTransfer` | `twilio_sdk/models/flex_v1_interaction_interaction_channel_interaction_transfer.py` |

### client.flex_v1_interaction_transfer.update_interaction_transfer

- **Route**: `POST /v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Transfers/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default13`
- **Signature**: `def update_interaction_transfer(interaction_sid: str, channel_sid: str, sid: str, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `interaction_sid`, `channel_sid`, `sid`
- **Params**: `interaction_sid` — path `InteractionSid` · `channel_sid` — path `ChannelSid` · `sid` — path `Sid` · `body` — JSON body
- **Returns (parsed)**: `FlexV1InteractionInteractionChannelInteractionTransfer`
- **Returns (raw)**: `ApiResult[FlexV1InteractionInteractionChannelInteractionTransfer, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1InteractionInteractionChannelInteractionTransfer` | `twilio_sdk/models/flex_v1_interaction_interaction_channel_interaction_transfer.py` |

