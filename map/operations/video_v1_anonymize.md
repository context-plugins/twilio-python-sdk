<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideoV1Anonymize — operations

Accessor: `client.video_v1_anonymize` · Source: `twilio/apis/video_v1_anonymize.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.video_v1_anonymize.update_room_participant_anonymize

- **Route**: `POST /v1/Rooms/{RoomSid}/Participants/{Sid}/Anonymize`
- **Server**: `default6`
- **Signature**: `def update_room_participant_anonymize(room_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `room_sid`, `sid`
- **Params**: `room_sid` — path `RoomSid` · `sid` — path `Sid`
- **Returns (parsed)**: `VideoV1RoomRoomParticipantRoomParticipantAnonymize`
- **Returns (raw)**: `ApiResult[VideoV1RoomRoomParticipantRoomParticipantAnonymize, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VideoV1RoomRoomParticipantRoomParticipantAnonymize` | `twilio/models/video_v1_room_room_participant_room_participant_anonymize.py` |

