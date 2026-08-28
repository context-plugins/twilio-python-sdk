<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV1InteractionChannelInvite — operations

Accessor: `client.flex_v1_interaction_channel_invite` · Source: `twilio/apis/flex_v1_interaction_channel_invite.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.flex_v1_interaction_channel_invite.create_interaction_channel_invite

- **Route**: `POST /v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Invites`
- **Server**: `default13`
- **Signature**: `def create_interaction_channel_invite(interaction_sid: str, channel_sid: str, routing: Any, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `interaction_sid`, `channel_sid`, `routing`
- **Params**: `interaction_sid` — path `InteractionSid` · `channel_sid` — path `ChannelSid` · `routing` — form field `Routing`
- **Returns (parsed)**: `FlexV1InteractionInteractionChannelInteractionChannelInvite`
- **Returns (raw)**: `ApiResult[FlexV1InteractionInteractionChannelInteractionChannelInvite, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlexV1InteractionInteractionChannelInteractionChannelInvite` | `twilio/models/flex_v1_interaction_interaction_channel_interaction_channel_invite.py` |

### client.flex_v1_interaction_channel_invite.list_interaction_channel_invite

- **Route**: `GET /v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Invites`
- **Server**: `default13`
- **Signature**: `def list_interaction_channel_invite(interaction_sid: str, channel_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `interaction_sid`, `channel_sid`
- **Params**: `interaction_sid` — path `InteractionSid` · `channel_sid` — path `ChannelSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListInteractionChannelInviteResponse`
- **Returns (raw)**: `ApiResult[ListInteractionChannelInviteResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListInteractionChannelInviteResponse` | `twilio/models/list_interaction_channel_invite_response.py` |

