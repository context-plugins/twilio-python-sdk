<!-- Generated file — do not edit; regenerated with the SDK. -->

# FlexV1InteractionChannelParticipant — operations

Accessor: `client.flex_v1_interaction_channel_participant` · Source: `twilio/apis/flex_v1_interaction_channel_participant.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.flex_v1_interaction_channel_participant.create_interaction_channel_participant

- **Route**: `POST /v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Participants`
- **Server**: `default13`
- **Signature**: `def create_interaction_channel_participant(interaction_sid: str, channel_sid: str, type_: InteractionChannelParticipantEnumTypeOrStr, media_properties: Any, *, routing_properties: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `interaction_sid`, `channel_sid`, `type_`, `media_properties`
- **Params**: `interaction_sid` — path `InteractionSid` · `channel_sid` — path `ChannelSid` · `type_` — form field `Type` · `media_properties` — form field `MediaProperties` · `routing_properties` — form field `RoutingProperties`
- **Returns (parsed)**: `FlexV1InteractionInteractionChannelInteractionChannelParticipant`
- **Returns (raw)**: `ApiResult[FlexV1InteractionInteractionChannelInteractionChannelParticipant, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InteractionChannelParticipantEnumTypeOrStr` | `twilio/models/enums/interaction_channel_participant_enum_type.py` |
| `FlexV1InteractionInteractionChannelInteractionChannelParticipant` | `twilio/models/flex_v1_interaction_interaction_channel_interaction_channel_participant.py` |

### client.flex_v1_interaction_channel_participant.list_interaction_channel_participant

- **Route**: `GET /v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Participants`
- **Server**: `default13`
- **Signature**: `def list_interaction_channel_participant(interaction_sid: str, channel_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `interaction_sid`, `channel_sid`
- **Params**: `interaction_sid` — path `InteractionSid` · `channel_sid` — path `ChannelSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListInteractionChannelParticipantResponse`
- **Returns (raw)**: `ApiResult[ListInteractionChannelParticipantResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListInteractionChannelParticipantResponse` | `twilio/models/list_interaction_channel_participant_response.py` |

### client.flex_v1_interaction_channel_participant.update_interaction_channel_participant

- **Route**: `POST /v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Participants/{Sid}`
- **Server**: `default13`
- **Signature**: `def update_interaction_channel_participant(interaction_sid: str, channel_sid: str, sid: str, status: InteractionChannelParticipantEnumStatusOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `interaction_sid`, `channel_sid`, `sid`, `status`
- **Params**: `interaction_sid` — path `InteractionSid` · `channel_sid` — path `ChannelSid` · `sid` — path `Sid` · `status` — form field `Status`
- **Returns (parsed)**: `FlexV1InteractionInteractionChannelInteractionChannelParticipant`
- **Returns (raw)**: `ApiResult[FlexV1InteractionInteractionChannelInteractionChannelParticipant, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InteractionChannelParticipantEnumStatusOrStr` | `twilio/models/enums/interaction_channel_participant_enum_status.py` |
| `FlexV1InteractionInteractionChannelInteractionChannelParticipant` | `twilio/models/flex_v1_interaction_interaction_channel_interaction_channel_participant.py` |

