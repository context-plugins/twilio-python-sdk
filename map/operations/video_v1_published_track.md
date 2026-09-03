<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideoV1PublishedTrack — operations

Accessor: `client.video_v1_published_track` · Source: `twilio_sdk/apis/video_v1_published_track.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.video_v1_published_track.fetch_room_participant_published_track

- **Route**: `GET /v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/PublishedTracks/{Sid}`
- **Auth**: `account_sid_auth_token`
- **Server**: `default6`
- **Signature**: `def fetch_room_participant_published_track(room_sid: str, participant_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `room_sid`, `participant_sid`, `sid`
- **Params**: `room_sid` — path `RoomSid` · `participant_sid` — path `ParticipantSid` · `sid` — path `Sid`
- **Returns (parsed)**: `VideoV1RoomRoomParticipantRoomParticipantPublishedTrack`
- **Returns (raw)**: `ApiResult[VideoV1RoomRoomParticipantRoomParticipantPublishedTrack, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VideoV1RoomRoomParticipantRoomParticipantPublishedTrack` | `twilio_sdk/models/video_v1_room_room_participant_room_participant_published_track.py` |

### client.video_v1_published_track.list_room_participant_published_track

- **Route**: `GET /v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/PublishedTracks`
- **Auth**: `account_sid_auth_token`
- **Server**: `default6`
- **Signature**: `def list_room_participant_published_track(room_sid: str, participant_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `room_sid`, `participant_sid`
- **Params**: `room_sid` — path `RoomSid` · `participant_sid` — path `ParticipantSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListRoomParticipantPublishedTrackResponse`
- **Returns (raw)**: `ApiResult[ListRoomParticipantPublishedTrackResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListRoomParticipantPublishedTrackResponse` | `twilio_sdk/models/list_room_participant_published_track_response.py` |

