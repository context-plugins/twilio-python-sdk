<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideoV1RoomRecording — operations

Accessor: `client.video_v1_room_recording` · Source: `twilio_sdk/apis/video_v1_room_recording.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.video_v1_room_recording.delete_room_recording

- **Route**: `DELETE /v1/Rooms/{RoomSid}/Recordings/{Sid}`
- **Server**: `default6`
- **Signature**: `def delete_room_recording(room_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `room_sid`, `sid`
- **Params**: `room_sid` — path `RoomSid` · `sid` — path `Sid`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.video_v1_room_recording.fetch_room_recording

- **Route**: `GET /v1/Rooms/{RoomSid}/Recordings/{Sid}`
- **Server**: `default6`
- **Signature**: `def fetch_room_recording(room_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `room_sid`, `sid`
- **Params**: `room_sid` — path `RoomSid` · `sid` — path `Sid`
- **Returns (parsed)**: `VideoV1RoomRoomRecording`
- **Returns (raw)**: `ApiResult[VideoV1RoomRoomRecording, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VideoV1RoomRoomRecording` | `twilio_sdk/models/video_v1_room_room_recording.py` |

### client.video_v1_room_recording.list_room_recording

- **Route**: `GET /v1/Rooms/{RoomSid}/Recordings`
- **Server**: `default6`
- **Signature**: `def list_room_recording(room_sid: str, *, status: RoomRecordingEnumStatusOrStr | None = None, source_sid: str | None = None, date_created_after: RFC3339DateTime | None = None, date_created_before: RFC3339DateTime | None = None, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `room_sid`
- **Params**: `room_sid` — path `RoomSid` · `status` — query `Status` · `source_sid` — query `SourceSid` · `date_created_after` — query `DateCreatedAfter` · `date_created_before` — query `DateCreatedBefore` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListRoomRecordingResponse`
- **Returns (raw)**: `ApiResult[ListRoomRecordingResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RoomRecordingEnumStatusOrStr` | `twilio_sdk/models/enums/room_recording_enum_status.py` |
| `ListRoomRecordingResponse` | `twilio_sdk/models/list_room_recording_response.py` |

