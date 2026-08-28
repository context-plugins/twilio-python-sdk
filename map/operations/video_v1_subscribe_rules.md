<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideoV1SubscribeRules — operations

Accessor: `client.video_v1_subscribe_rules` · Source: `twilio_sdk/apis/video_v1_subscribe_rules.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.video_v1_subscribe_rules.fetch_room_participant_subscribe_rule

- **Route**: `GET /v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/SubscribeRules`
- **Server**: `default6`
- **Signature**: `def fetch_room_participant_subscribe_rule(room_sid: str, participant_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `room_sid`, `participant_sid`
- **Params**: `room_sid` — path `RoomSid` · `participant_sid` — path `ParticipantSid`
- **Returns (parsed)**: `VideoV1RoomRoomParticipantRoomParticipantSubscribeRule`
- **Returns (raw)**: `ApiResult[VideoV1RoomRoomParticipantRoomParticipantSubscribeRule, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VideoV1RoomRoomParticipantRoomParticipantSubscribeRule` | `twilio_sdk/models/video_v1_room_room_participant_room_participant_subscribe_rule.py` |

### client.video_v1_subscribe_rules.update_room_participant_subscribe_rule

- **Route**: `POST /v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/SubscribeRules`
- **Server**: `default6`
- **Signature**: `def update_room_participant_subscribe_rule(room_sid: str, participant_sid: str, *, rules: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `room_sid`, `participant_sid`
- **Params**: `room_sid` — path `RoomSid` · `participant_sid` — path `ParticipantSid` · `rules` — form field `Rules`
- **Returns (parsed)**: `VideoV1RoomRoomParticipantRoomParticipantSubscribeRule`
- **Returns (raw)**: `ApiResult[VideoV1RoomRoomParticipantRoomParticipantSubscribeRule, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VideoV1RoomRoomParticipantRoomParticipantSubscribeRule` | `twilio_sdk/models/video_v1_room_room_participant_room_participant_subscribe_rule.py` |

