<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideoV1RecordingRules — operations

Accessor: `client.video_v1_recording_rules` · Source: `twilio/apis/video_v1_recording_rules.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.video_v1_recording_rules.fetch_room_recording_rule

- **Route**: `GET /v1/Rooms/{RoomSid}/RecordingRules`
- **Server**: `default6`
- **Signature**: `def fetch_room_recording_rule(room_sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `room_sid`
- **Params**: `room_sid` — path `RoomSid`
- **Returns (parsed)**: `VideoV1RoomRoomRecordingRule`
- **Returns (raw)**: `ApiResult[VideoV1RoomRoomRecordingRule, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VideoV1RoomRoomRecordingRule` | `twilio/models/video_v1_room_room_recording_rule.py` |

### client.video_v1_recording_rules.update_room_recording_rule

- **Route**: `POST /v1/Rooms/{RoomSid}/RecordingRules`
- **Server**: `default6`
- **Signature**: `def update_room_recording_rule(room_sid: str, *, rules: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `room_sid`
- **Params**: `room_sid` — path `RoomSid` · `rules` — form field `Rules`
- **Returns (parsed)**: `VideoV1RoomRoomRecordingRule`
- **Returns (raw)**: `ApiResult[VideoV1RoomRoomRecordingRule, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VideoV1RoomRoomRecordingRule` | `twilio/models/video_v1_room_room_recording_rule.py` |

